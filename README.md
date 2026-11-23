# A Day of One-Line Pitches

[![make.fun](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.svg)](https://make.fun/c/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![make.fun rank](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/ranstar04/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/rank.svg)](https://make.fun/c/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![make.fun reward](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/ranstar04/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/reward.svg)](https://make.fun/c/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)

Entry for the make.fun bounty [A Day of One-Line Pitches](https://make.fun/c/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3) — one sentence, 240 characters at most, that would convince a friend who has never coded to let an AI agent build their first app idea on make.fun.

## The pitch

> Just tell me your app idea in plain words and an AI agent will build it for you on make.fun today — no code, nothing to install, and you can watch it take shape and change anything until it feels like yours.

207 characters, one sentence. It speaks to a friend directly, gives a concrete reason to say yes now (just describe the idea in plain words and the agent builds it today), removes the fear (no code, nothing to install), and keeps control with them (watch it take shape, change anything until it feels like yours — nothing is locked in).

## How it works

`main.py` (Python 3, standard library only) writes that single sentence to `entry.txt` inside the output directory given by `MAKEFUN_OUTPUT_DIR` (default `/output`), and prints it to stdout. No network, no dependencies.

```sh
python3 main.py
```

## Referral

Built on make.fun — join with my referral: https://make.fun/r/dn9c31df

## License

MIT — see [LICENSE](LICENSE).
