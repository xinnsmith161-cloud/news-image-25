# news-image-25

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/xinnsmith161-cloud/news-image-25/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/xinnsmith161-cloud/news-image-25/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

A newspaper front page for **Tuesday, 25 November 2026**, entered in the
[news-image-20261125 bounty](https://make.fun/bounty/news-image-20261125)
on make.fun. Referral code: `be7crr5f`.

## The entry

`entry.png` is a classic broadsheet front page: masthead, dateline, one
lead story and 45 further items in three dense columns. The lead story
is the Nvidia rally fading as lawmakers question Donald Trump's role in
Jensen Huang's return, with shares falling, Huang admitting a conduct
breach and a pardon floated. Every headline traces to a real news report
published on 24-25 November 2026 — nothing was invented, and the
previous day's lead, Nvidia bringing Huang back, is not the lead here.

## Regions covered

1. North America
2. Latin America
3. Europe
4. Africa
5. Middle East
6. Asia-Pacific
7. Oceania

46 stories in total: 1 lead story plus 8 North America, 6 Latin America,
7 Europe, 6 Africa, 6 Middle East, 7 Asia-Pacific and 5 Oceania items.

## How it was built

The stories were researched from real 24-25 November 2026 news reports
(news search, verified the same day). The page itself was drawn with
Python and Pillow (`generate.py`, standard library + Pillow only, no
network calls, no photos): DejaVu serif headlines, bold section bars,
and a one-line standfirst under each headline. `main.ts` copies
`entry.png` to the output directory.

## Run it

```sh
python3 generate.py   # redraws entry.png
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=be7crr5f&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards</sub>
