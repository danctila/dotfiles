#!/usr/bin/env python3
"""
save_transcript.py — fetch a YouTube transcript and save it as a clean,
readable markdown file (sentence-per-line, no timestamps) in any directory.

Self-contained: needs only the `youtube-transcript-api` package.

Usage:
    python3 save_transcript.py <youtube_url> <output_dir> [--title "Custom Title"]

If --title is omitted, the video's real title (via YouTube oembed) is used.
The output filename is always a slugified version of the title.
"""
import re
import sys
import json
import argparse
import textwrap
import urllib.parse
import urllib.request
from pathlib import Path

try:
    from youtube_transcript_api import YouTubeTranscriptApi
except ImportError:
    sys.exit("Missing dependency. Run: pip install youtube-transcript-api")

SENTENCES_PER_PARAGRAPH = 6
LINE_WIDTH = 100


def extract_video_id(url):
    patterns = [
        r"youtu\.be/([0-9A-Za-z_-]{11})",
        r"(?:v=|/)([0-9A-Za-z_-]{11})",
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    raise ValueError(f"Could not extract video ID from URL: {url}")


def get_title(video_id):
    watch = urllib.parse.quote(f"https://www.youtube.com/watch?v={video_id}", safe="")
    oembed_url = f"https://www.youtube.com/oembed?url={watch}&format=json"
    try:
        with urllib.request.urlopen(oembed_url, timeout=10) as resp:
            return json.load(resp).get("title", video_id)
    except Exception:
        return video_id


def fetch_transcript(video_id):
    fetched = YouTubeTranscriptApi().fetch(video_id)
    text = " ".join(snippet.text.strip() for snippet in fetched)
    return re.sub(r"\s+", " ", text).strip()


def slugify_filename(title):
    safe = re.sub(r"[^\w\s-]", "", title).strip()
    safe = re.sub(r"\s+", "-", safe).lower()
    return safe[:150] or "untitled"


def reflow(text):
    """One sentence per line, blank line every SENTENCES_PER_PARAGRAPH sentences."""
    sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+(?=[A-Z"‘’])', text) if s.strip()]
    paragraphs = []
    for i in range(0, len(sentences), SENTENCES_PER_PARAGRAPH):
        lines = [
            textwrap.fill(s, width=LINE_WIDTH, break_long_words=False, break_on_hyphens=False)
            for s in sentences[i:i + SENTENCES_PER_PARAGRAPH]
        ]
        paragraphs.append("\n".join(lines))
    return "\n\n".join(paragraphs)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument("output_dir", help="Directory to save the transcript markdown into")
    parser.add_argument("--title", help="Override title (defaults to the video's real title)")
    args = parser.parse_args()

    video_id = extract_video_id(args.url)
    title = args.title or get_title(video_id)
    body = reflow(fetch_transcript(video_id))

    out_dir = Path(args.output_dir).expanduser()
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / (slugify_filename(title) + ".md")
    out_path.write_text(f"# {title}\n\nSource: {args.url}\n\n---\n\n{body}\n", encoding="utf-8")

    print(f"Saved: {out_path}")


if __name__ == "__main__":
    main()
