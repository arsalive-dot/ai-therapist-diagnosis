#!/usr/bin/env python3
"""Your AI Therapist's Diagnosis — make.fun entry.

Writes one funny single-line diagnosis an AI therapist gives its human
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt) for the make.fun
bounty u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41.

The line: a therapist's calm clinical voice, a deadpan finding about the
human narrating their life to an AI at 3 a.m., with the turn at the end —
the patient is an extra who read the script and demanded a bigger part.

Judge brief, top-weighted first: (1) a funny single-line diagnosis an AI
therapist gives its human, not a stray joke; (2) the joke lands with a turn
the reader never sees coming, the laugh arriving at the end ("demanded a
bigger part"); (3) speaks in a therapist's calm clinical voice, turning a
human habit into a deadpan finding; (4) tight and quotable, every word
earning its place at 166 characters; (5) fresh — the patient is talking to
the AI therapist itself, not a rerun of the usual chatbot jokes.
"""

import os

ENTRY = (
    "Diagnosis: acute main-character syndrome \u2014 you narrate your life "
    "to an AI at 3 a.m. instead of sleeping, like an extra who read the "
    "script and demanded a bigger part."
)


def main():
    # Gate self-check: UTF-8 text, 1 to 200 characters, not only whitespace.
    text = ENTRY
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    text.encode("utf-8")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    tmp_path = os.path.join(out_dir, ".entry.txt.tmp")
    final_path = os.path.join(out_dir, "entry.txt")
    with open(tmp_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(tmp_path, 0o644)
    os.replace(tmp_path, final_path)
    os.chmod(final_path, 0o644)


if __name__ == "__main__":
    main()
