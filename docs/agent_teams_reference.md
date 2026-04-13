# Agent Teams — Master Reference Guide

Source: https://code.claude.com/docs/pt/agent-teams
Purpose: Internal reference for building effective agent teams in future sessions.
Requires: Claude Code v2.1.32+ and experimental flag enabled.

---

## 1. Core Concept

Agent teams coordinate **multiple Claude Code instances** working together. One session is the **team lead**; the others are **teammates**, each in their own context window, each a full independent Claude Code session.

Unlike subagents (which only report back to a parent), teammates:
- Share a **task list**
- **Message each other directly** via a mailbox system
- Can be addressed **directly by the user** without going through the lead

### Subagents vs Agent Teams

| Dimension | Subagents | Agent Teams |
|---|---|---|
| Context | Own window; results return to caller | Own window; fully independent |
| Communication | Report to main agent only | Teammates message each other |
| Coordination | Main agent manages all work | Shared task list, self-coordination |
| Best for | Focused tasks where only the result matters | Complex work requiring discussion + collaboration |
| Token cost | Lower (summarized results) | Higher (each teammate is a full instance) |

**Rule of thumb:** Use subagents when workers just need to report back. Use teams when workers need to share findings, challenge each other, or co-own a problem.

---

## 2. When to Use Agent Teams

**Strong fits:**
- **Research & review** — multiple angles explored in parallel, then cross-examined
- **New modules/features** — each teammate owns a distinct slice
- **Debugging with competing hypotheses** — adversarial investigation to defeat anchoring bias
- **Cross-layer coordination** — frontend/backend/tests owned separately

**Poor fits (use single session or subagents):**
- Sequential tasks with heavy dependencies
- Multiple edits to the same file
- Routine/simple tasks where coordination overhead dominates
- Anything where token cost outweighs parallelism benefit

---

## 3. Enabling Agent Teams

Experimental and off by default. Enable in `settings.json` or env:

```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

---

## 4. Architecture

| Component | Role |
|---|---|
| **Team lead** | Primary session: creates team, spawns teammates, coordinates |
| **Teammates** | Separate Claude Code instances, each working assigned tasks |
| **Task list** | Shared work queue; teammates claim items |
| **Mailbox** | Inter-agent messaging system |

**Storage (local, auto-managed — do NOT hand-edit):**
- Team config: `~/.claude/teams/{team-name}/config.json`
- Task list: `~/.claude/tasks/{team-name}/`

The config contains a `members` array (name, agent ID, agent type) which teammates read to discover each other. Project-level team config is NOT supported.

**Task states:** pending → in progress → completed. Tasks may have dependencies — blocked tasks cannot be claimed until prerequisites finish. File-locking prevents race conditions on claims. Dependency unblocking is automatic.

---

## 5. Starting a Team

Just describe the task and team structure in natural language:

```
I'm designing a CLI tool that tracks TODO comments. Create an agent team to
explore this from different angles: one teammate on UX, one on technical
architecture, one playing devil's advocate.
```

Claude creates the team, spawns teammates, gives them a shared task list, and synthesizes findings at the end.

**Two ways teams start:**
1. User explicitly asks for one
2. Claude proposes a team when parallelism would help (user must confirm)

---

## 6. Controlling the Team

### Display Modes

- **In-process** (works anywhere): all teammates run in main terminal. `Shift+Down` cycles teammates; type to message directly. `Enter` opens a teammate's session; `Escape` interrupts their turn; `Ctrl+T` toggles task list.
- **Split panes** (requires tmux or iTerm2 + `it2` CLI): each teammate gets its own pane.

Default is `"auto"` (split panes if already in tmux, else in-process). Override globally in `~/.claude.json`:

```json
{ "teammateMode": "in-process" }
```

Or per-session: `claude --teammate-mode in-process`

Split-pane mode is NOT supported in VS Code integrated terminal, Windows Terminal, or Ghostty.

### Specifying Teammates and Models

```
Create a team with 4 teammates to refactor these modules in parallel.
Use Sonnet for each teammate.
```

### Plan-Approval Gate (for risky work)

```
Spawn an architect teammate to refactor the authentication module.
Require plan approval before they make any changes.
```

Teammate works read-only in plan mode → submits plan → lead approves or rejects with feedback → teammate revises and resubmits → once approved, implements.

Lead approves autonomously. Influence its judgment with explicit criteria in the prompt:
> "Only approve plans that include test coverage."
> "Reject any plan that modifies the database schema."

### Task Assignment

- **Lead assigns**: tell the lead which task goes to which teammate
- **Auto-claim**: teammates pick up the next unblocked task after finishing

### Using Subagent Definitions as Teammate Types

Any [subagent](https://code.claude.com/docs/pt/sub-agents) scope (project/user/plugin/CLI) can be reused as a teammate type. The teammate inherits the subagent's system prompt, tools, and model:

```
Spawn a teammate using the security-reviewer agent type to audit the auth module.
```

This is the right place to define reusable roles (security-reviewer, test-runner, etc.).

### Shutting Down

Graceful shutdown of one teammate:
```
Ask the researcher teammate to shut down
```
Teammate can approve (exit) or reject with explanation.

Full cleanup at end of work:
```
Clean up the team
```
**Always** have the lead do cleanup — teammates may leave resources in inconsistent state. Cleanup fails if any teammate is still running; shut them down first.

---

## 7. Quality Gates via Hooks

Enforce rules with hooks that run on team events:

- **`TeammateIdle`** — fires when a teammate is about to idle. Exit code 2 sends feedback and keeps them working.
- **`TaskCreated`** — fires on task creation. Exit code 2 blocks the task with feedback.
- **`TaskCompleted`** — fires on task completion. Exit code 2 blocks completion with feedback.

Useful for: enforcing test coverage, blocking risky file edits, requiring documentation.

---

## 8. Context, Communication, Permissions

**What teammates inherit on spawn:**
- Project context: `CLAUDE.md`, MCP servers, skills
- The lead's spawn prompt
- Lead's permission mode (including `--dangerously-skip-permissions`)

**What they do NOT inherit:**
- Lead's conversation history

**Implication:** put task-specific context into the spawn prompt. Example of a good spawn prompt:
```
Spawn a security reviewer teammate with the prompt: "Review the authentication
module at src/auth/ for security vulnerabilities. Focus on token handling,
session management, and input validation. The app uses JWT tokens stored in
httpOnly cookies. Report any issues with severity ratings."
```

**Messaging primitives:**
- `message` — send to a specific teammate
- `broadcast` — send to all; use sparingly (cost scales with team size)

Message delivery and idle notifications are automatic — no polling needed.

**Permissions caveat:** modes are set at spawn time from the lead. You can change individual teammate modes post-spawn but cannot set per-teammate modes upfront.

---

## 9. Use Case Patterns

### Parallel Code Review
```
Create an agent team to review PR #142. Spawn three reviewers:
- One focused on security implications
- One checking performance impact
- One validating test coverage
Have them each review and report findings.
```
Each reviewer applies a distinct filter on the same PR; lead synthesizes.

### Adversarial Investigation (competing hypotheses)
```
Users report the app exits after one message instead of staying connected.
Spawn 5 agent teammates to investigate different hypotheses. Have them talk
to each other to try to disprove each other's theories, like a scientific
debate. Update the findings doc with whatever consensus emerges.
```
The debate structure defeats anchoring bias — the surviving theory is more likely to be the real root cause.

### Other strong patterns
- Cross-layer feature (frontend/backend/tests teammates)
- Refactor multiple modules in parallel (one teammate per module)
- Library research (compare N options simultaneously)

---

## 10. Best Practices

1. **Start with research/review tasks.** Clear boundaries, no shared file edits, fastest win.
2. **Team size: 3–5 teammates** for most workflows. Three focused often beats five scattered. Costs scale linearly; coordination overhead grows faster.
3. **Task sizing: 5–6 tasks per teammate.** Keeps everyone busy, gives lead room to rebalance when someone is stuck.
4. **Avoid file conflicts.** Divide work so each teammate owns a disjoint file set.
5. **Rich spawn prompts.** Teammates don't see lead's history — include constraints, file paths, focus areas, acceptance criteria.
6. **Don't let the lead implement.** If lead starts coding instead of delegating, tell it: *"Wait for your teammates to complete their tasks before proceeding."*
7. **Monitor and redirect.** Don't leave a team running unsupervised for long stretches — wasted effort compounds fast.
8. **Pre-approve common permissions** before spawning — reduces interrupt prompts to the lead.
9. **Use plan-approval for risky work** (refactors, schema changes, auth).
10. **Use subagent definitions for reusable roles** — define once, reuse as subagent or teammate.

---

## 11. Troubleshooting

| Symptom | Fix |
|---|---|
| Teammates don't appear | In-process: `Shift+Down` to cycle. Verify task was complex enough. Check `which tmux` / iTerm2 `it2` + Python API. |
| Too many permission prompts | Pre-approve in permissions settings before spawning. |
| Teammate stops on error | `Shift+Down` into it, give instructions, or spawn a replacement. |
| Lead wraps up too early | Tell it to continue, or "wait for teammates to finish before proceeding". |
| Task status stuck | Verify work is actually done; manually update status or nudge teammate via lead. |
| Orphan tmux session | `tmux ls` → `tmux kill-session -t <name>`. |

---

## 12. Known Limitations (Experimental)

- `/resume` and `/rewind` do NOT restore in-process teammates. If the lead messages a ghost teammate, spawn replacements.
- Task status can lag — teammates sometimes forget to mark complete, blocking dependents.
- Shutdown is slow — teammates finish their current tool call first.
- **One team per session** — clean up before starting another.
- **No nested teams** — teammates cannot spawn their own teams.
- **Lead is fixed** — cannot transfer leadership or promote a teammate.
- Permissions cannot be set per-teammate at spawn.
- Split panes not supported in VS Code integrated terminal, Windows Terminal, or Ghostty.

---

## 13. Decision Checklist (use before spawning a team)

1. Does the task have 3+ genuinely independent workstreams? → Yes: team. No: single session or subagents.
2. Do workers need to talk to each other? → Yes: team. No: subagents.
3. Will work touch overlapping files? → Yes: redesign split or use single session.
4. Is parallelism worth ~Nx the token cost? → No: single session.
5. Is there a reusable role? → Use a subagent definition as the teammate type.
6. Is the work risky/hard to reverse? → Require plan approval.
7. Are there quality gates to enforce? → Wire up `TaskCompleted` / `TeammateIdle` hooks.
8. Team size? Default **3–5**, tasks sized to **5–6 per teammate**.
9. Spawn prompts complete? Each should include: objective, files/scope, constraints, acceptance criteria, output format.
10. Cleanup plan? Lead runs `Clean up the team` at the end.
