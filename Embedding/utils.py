from __future__ import annotations
import os
import tempfile
from pathlib import Path
from moviepy import VideoFileClip

from config import SUPPORTED_IMAGE_EXT, SUPPORTED_VIDEO_EXT, SUPPORTED_TEXT_EXT, MAX_VIDEO_SECONDS


def detect_content_type(filepath: str) -> str | None:
    """Return 'text', 'image', 'video', or None if unsupported."""
    ext = Path(filepath).suffix.lower()
    if ext in SUPPORTED_TEXT_EXT:
        return "text"
    if ext in SUPPORTED_IMAGE_EXT:
        return "image"
    if ext in SUPPORTED_VIDEO_EXT:
        return "video"
    return None


def get_video_duration(filepath: str) -> float:
    """Return video duration in seconds."""
    with VideoFileClip(filepath) as clip:
        return clip.duration


def segment_video(filepath: str, *, max_seconds: float = MAX_VIDEO_SECONDS, output_dir: str | None = None) -> list[dict]:
    """
    Split a video into segments of at most max_seconds.

    Returns list of dicts:
      [{"path": "/tmp/seg_0.mp4", "index": 0, "start": 0.0, "end": 120.0}, ...]

    If the video is already <= max_seconds, returns a single-element list
    pointing to the original file (no re-encoding).
    """
    with VideoFileClip(filepath) as clip:
        duration = clip.duration
        if duration <= max_seconds:
            return [{"path": filepath, "index": 0, "start": 0.0, "end": duration}]

        if output_dir is None:
            output_dir = tempfile.mkdtemp(prefix="embedvid_")

        segments = []
        idx = 0
        start = 0.0
        while start < duration:
            end = min(start + max_seconds, duration)
            seg_path = os.path.join(output_dir, f"seg_{idx}.mp4")
            subclip = clip.subclipped(start, end)
            subclip.write_videofile(seg_path, logger=None)
            segments.append({"path": seg_path, "index": idx, "start": start, "end": end})
            start = end
            idx += 1

    return segments


def read_text_file(filepath: str, max_chars: int = 30_000) -> str:
    """Read a text file, truncating to max_chars."""
    return Path(filepath).read_text(encoding="utf-8", errors="replace")[:max_chars]
