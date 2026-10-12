---
name: youtube-transcript
description: Download a YouTube video's transcript and save it as a clean, readable markdown file (no timestamps, sentence-per-line formatting) in a directory you specify. Use this whenever the user pastes a youtube.com or youtu.be link and asks to save, download, grab, or archive the transcript — especially when they name a target folder or title, e.g. "save this transcript to notes/alex-hormozi" or "pull the transcript for this video into a new folder called X." Also use for batch requests like "grab transcripts for these three videos into the same folder."
---

# YouTube transcript downloader

Fetches a YouTube video's transcript and writes it as a reflowed, timestamp-free
markdown file into whatever directory the user asks for. Works from any project;
it depends on nothing in the current repo.

## When to use this

Trigger on a YouTube URL plus any request to save/download/archive its transcript.
Pay attention to two details the user usually gives you:

1. **Target directory** — where the file should live. Resolve plain-language
   locations ("the alex hormozi folder") to a real path in the current project
   before running the script. If they say "a new directory," create it. If no
   location is given, ask.
2. **Title** — if they give one, use it verbatim as `--title`. If not, leave
   `--title` off and the script looks up the real video title.

## Running it

```bash
python3 ~/.claude/skills/youtube-transcript/scripts/save_transcript.py "<youtube_url>" "<output_dir>" --title "<title>"
```

- `<output_dir>` is created if it doesn't exist.
- The filename is always a slugified version of the title (lowercase, hyphens).
- Output is reflowed into sentence-per-line paragraphs; no raw intermediate file.

After it runs, report the saved path (the script prints `Saved: <path>`).

## Multiple videos

Call the script once per URL with the same `output_dir`. Each gets its own file.

## If the fetch fails

`youtube_transcript_api` raises clear errors for videos with no captions,
disabled transcripts, or unavailable videos. Tell the user which video failed
and why rather than retrying silently.

## Dependency

Requires the `youtube-transcript-api` Python package:

```bash
pip install youtube-transcript-api
```
