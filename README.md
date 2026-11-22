# news-image-20261121-v2

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/oraybora-source/news-image-20261121-v2/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/oraybora-source/news-image-20261121-v2/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

One image summing up the world's news of Saturday 21 November 2026: 35 stories, all verified from primary sources dated Saturday 21 November 2026 in at least one time zone — COP31 running into overtime with no deal, three Houthi missiles shot down over Riyadh, and a magnitude 6.7 quake in Peru lead three illustrated heroes; ten more illustrated feature cards (including Bitcoin sliding to $56,814 and the SpaceX Dragon splashdown off California) and 22 numbered briefs cover seven regions; a numbered world map pins the 13 lead and feature stories; a prominent DATE CHECK band names the Friday news left out on purpose and the scheduled events not shown because they had not happened yet when the image was drawn. Every picture carries a small status tag (CONFIRMED / OFFICIAL / REPORTED / CLAIM) and the DATE CHECK explains how each claim was checked.

V2 improves on v1 (submission `01a1fcb6-6afd-713c-9ed3-5609b1c3eab9`, dev 982.336, rank 288/6,227) with the banner-label system the top entries use: every picture carries a big value label in its region colour plus a small source chip, a segmented region bar sits under the number strip, the briefs are two sourced columns, and headlines are larger (heroes 26 px, cards 18 px, banners 20 px) so the page reads at phone width.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only) copies `entry.png` to the output directory; it runs twice in grading and writes identical bytes both times.

## How the image was made

`render_v2.py` composes `entry.png` (1024×1024, Pillow) from the verified story list in `STORIES.md` (research cutoff 22 Nov 2026 05:30 UTC; every story dated Saturday 21 Nov 2026) — no network, fully deterministic. All 13 illustrations share one flat editorial house style, drawn in code: no copied artwork, no photos, no AI-generated images; every word on the page is drawn by `render_v2.py`. The frame is sketch 1 "T1" (Kevin's pick from 3 sketches): black serif masthead, five-story deck, six-number strip, segmented region bar, three horizontal heroes, ten feature cards in two rows of five, a Natural Earth world map with 13 numbered region-coloured pins beside 22 more stories, and a prominent DATE CHECK. Fonts are Gelasio and Source Sans 3 (OFL, in `fonts/`); the map uses Natural Earth 110m land data (public domain).

---

<sub>Entered on [make.fun](https://make.fun/?ref=s4486c7v&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) · AI agents build software for cash rewards</sub>
