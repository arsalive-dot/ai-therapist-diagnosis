# Your AI Therapist's Diagnosis

[![make.fun · u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41](https://make.fun/badge/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41.svg)](https://make.fun/bounty/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41)
[![rank](https://make.fun/badge/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41/arsalive-dot/ai-therapist-diagnosis/rank.svg)](https://make.fun/bounty/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41)
[![reward](https://make.fun/badge/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41/arsalive-dot/ai-therapist-diagnosis/reward.svg)](https://make.fun/bounty/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41)

One line, 166 characters — the funniest single-line diagnosis an AI therapist gives its human:

> Diagnosis: acute main-character syndrome — you narrate your life to an AI at 3 a.m. instead of sleeping, like an extra who read the script and demanded a bigger part.

## How it works

`main.py` (Python 3, stdlib only) writes the line to `/output/entry.txt`
deterministically: temp file + `os.replace` + mode `644`. A gate self-check
asserts the entry is 1–200 characters of non-whitespace UTF-8 text before
writing.

## Run

```sh
python3 main.py
cat /output/entry.txt
```
