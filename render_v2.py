#!/usr/bin/env python3
"""render_v2.py — ni21 V2 "Fair Kernel" improve (duel-loop attempt 1).

Perubahan vs V1 (hanya 5 CHANGES FOR IMPROVE dari loss_report_a1.md):
1. Banner-label + source strip di semua 13 gambar (banner = topik+nilai,
   putih bold 20px di blok warna solid = warna region; chip sumber kecil
   di bawah gambar). Warna banner tetangga ortogonal selalu beda >= 25
   (aturan Kevin: warna atas panel beda dari tetangga).
2. Bar region tersegmentasi di bawah strip angka (7 segmen sama lebar,
   hitungan dari 35 cerita kami: EUROPE 5, MIDDLE EAST 4, AFRICA 1,
   ASIA 12, AMERICAS 6, OCEANIA 4, WORLD 3).
3. Brief MORE STORIES -> 2 kolom: chip nomor warna region + kota merah
   tebal + brief 1 baris (fakta/angka kunci) + (Sumber).
4. Reselection feature-13: kartu Bitcoin ($56.814, -3,6%) + Dragon
   splashdown MASUK; Vietnam law + freight derail pindah ke brief;
   Rahul -> 136 / 344-2. TIDAK ada kartu Jumat (uranium/China-Jepang)
   — keputusan itu masih terbuka untuk Kevin; kemurnian Sabtu 35/35.
5. Legibility pass 390px: hero headline 26px, kartu 18px, banner 20px;
   peta lebih terang + pin warna per region.
6. REVERT (Keputusan Kevin 22 Nov 04:24 WIB — MEMBATALKAN keputusan
   20:28 WIB; why_we_lost_1.md change #1): kartu Jumat/Kamis KELUAR
   dari feature — #6 kembali BepiColombo (Darmstadt, GLOBAL,
   "TONIGHT 19:24") + #13 kembali ATP semis (Turin, EUROPE,
   "SEMIS TONIGHT"); uranium Iran + China–Jepang Taiwan kembali ke
   DATE CHECK "left out" (DITOLAK, bukan brief); brief hoki India +
   donor Tasmania dipulihkan; bar region kembali MIDDLE EAST 4 /
   OCEANIA 4; TIDAK ada lagi label tanggal hari sebelumnya di kartu.
   Dipertahankan dari FIX manual: Delhi AQI 279 (CPCB 07:00, B3 —
   angka 286 tidak terverifikasi).
7. Revisi Kevin 22 Nov 04:38 WIB: hapus brief #25 Bangkok ("Anutin
   calls emergency meeting") supaya kolom MORE STORIES rata 11/11;
   brief 26-36 jadi 25-35; total 35/35 Sabtu; ASIA 12.
8. Revisi Kevin 22 Nov 04:41 WIB: perbesar teks MORE STORIES supaya
   mengisi kotak (font kota/teks 10->11, sumber 9->10, chip 9->10,
   pitch 13->15, baris mulai y1+26); isi brief TIDAK berubah.
9. Revisi Kevin 22 Nov 04:43 WIB: perbesar chip hitam sumber di semua
   13 gambar supaya terbaca tanpa zoom (font 8->12, chip 12px->17px,
   padding lebar 10->12); nama sumber TIDAK berubah.
10. Revisi Kevin 22 Nov 04:44 WIB: perbesar pin peta (r=7->r=11, angka
   8pt->13pt, jarak minimum 18->25px, offset sampai 30px; acuan pin
   ni20 rev8) + label peta (judul 11->14, "Pins 1-13" 12->14, legenda
   8->11, chip 16px->20px); posisi kota + warna pin TIDAK berubah.
11. Revisi Kevin 22 Nov 04:46 WIB: perbesar teks ringkasan/deskripsi di
   bawah headline semua 13 kartu supaya kelihatan tanpa zoom —
   LANTAI 16px (aturan Kevin 22 Nov 04:47, MEMORY.md: tidak ada teks di
   bawah 16px di file; kalau tidak muat, potong kata, JANGAN kecilkan
   font; cek di lebar 390px). Hero 11->16pt, kartu 10->16pt, pitch
   19; HERO_H 216->222 (ringkasan mulai +76); 7 ringkasan dipersingkat
   supaya tetap <=2 baris (#5, #7, #8, #10, #11, #12, #13 — "both
   tonight" #13 sudah di banner SEMIS TONIGHT); fakta/angka TIDAK
   berubah; headline tetap.
+12. Opsi A Kevin 22 Nov 04:55 WIB (layout agar ringkasan 16pt muat):
+   CARD_H 156->170, CARD_Y baris-2 578->588, MAP_BOX/BRIEFS_BOX y1
+   742->762 (peta 194->174px, -10%); pitch ringkasan kartu 19->18
+   (bbox teks 16pt = 16px, celah 2px antar baris, tanpa overlap);
+   briefs pitch 15->14 + mulai y1+23 (chip 14px bersentuhan vertikal,
+   tanpa overlap) agar 22 brief tetap muat di kotak 174px.
+   Perhitungan awal agen sebelumnya (y1=766) SALAH: brief butuh
+   tinggi >=186px di pitch 15 dan pin Wellington butuh peta >=~176px.
+13. Revisi Kevin 22 Nov 05:06 WIB: DATE CHECK gaya v20 di 12pt
+   (opsi A — "kayak v20" MENANG atas lantai 16pt untuk kotak ini;
+   v20 sendiri pakai 12pt): chip merah "DATE CHECK" di kiri +
+   kolom kanan berisi daftar (2 baris) + brief ringkasan (1 baris),
+   teks tebal navy 12pt. Kotak + Sources TIDAK digeser (tinta 3 baris
+   terukur 36px, muat di kotak 50px). Isi daftar + brief tidak
+   menambah fakta baru.

YANG TIDAK BERUBAH: kerangka masthead + deck + strip + 3 hero + 10 kartu
+ peta + brief + DATE CHECK; kemurnian tanggal 35/35 Sabtu + angka
terverifikasi (3 / $56.814 / 2-42 / BepiColombo "tonight"); lead trio
COP31 / Riyadh / Peru; DATE CHECK jujur + menonjol; teknis <=1 MiB,
1024x1024, deterministik 2x, tanpa network; satu gaya ilustrasi datar;
subjek utuh + margin; warna atas panel beda dari tetangga; footer tanpa
catatan produksi.

Teknis: Pillow, deterministik (2x jalan byte sama), tanpa network.
Output: entry.png 1024x1024, <=1 MiB. Fonts OFL (Gelasio + Source
Sans 3) + Natural Earth 110m (Public Domain) di repo ini.
Model: Muse Spark. V1: makefun anchor 99ce6ca57c2f35489c4f906b7e0165c7c39ab2cf
round 34145189 (repo news-image-20261121, submission 01a1fcb6-...).
"""
import hashlib
import json
import os
import sys
from collections import Counter

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "fonts")
OUT = os.path.join(HERE, "entry.png")

W, H = 1024, 1024
PAPER = (247, 240, 220)      # kertas krem (sketsa)
NEAR_WHITE = (251, 250, 245)  # latar panel teks (diukur dari referensi ni20)
INK = (20, 20, 20)
NAVY = (31, 58, 95)
RED = (192, 57, 43)
RED_M = (176, 48, 38)
GOLD_M = (200, 150, 30)
WHITE = (255, 255, 255)
LINE = (120, 110, 90)
GREY = (110, 105, 90)
SLATE = (70, 75, 85)

# --- font (spesifikasi Kevin 21:37 WIB) ---
GEL700 = os.path.join(FONTS, "Gelasio-700.ttf")       # judul 700
GEL_IT = os.path.join(FONTS, "Gelasio-Italic.ttf")    # deck italic
SS400 = os.path.join(FONTS, "SourceSans3-400.ttf")    # isi 400
SS600 = os.path.join(FONTS, "SourceSans3-600.ttf")
SS700 = os.path.join(FONTS, "SourceSans3-700.ttf")    # angka strip 700
SS800 = os.path.join(FONTS, "SourceSans3-800.ttf")    # kicker/label 800


def F(path, size):
    return ImageFont.truetype(path, size)


def wrap(d, text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


# ------------------------------------------------------------------ registry
# (a) layout boxes: semua kotak tingkat atas tidak boleh overlap.
# (b) teks per tile: bbox teks di dalam satu tile tidak boleh overlap.
LAYOUT = []


def reg_layout(box, label):
    LAYOUT.append((box, label))


def check_layout(name):
    for i, (a, la) in enumerate(LAYOUT):
        for j in range(i + 1, len(LAYOUT)):
            b, lb = LAYOUT[j]
            if not (a[2] <= b[0] or b[2] <= a[0] or a[3] <= b[1]
                    or b[3] <= a[1]):
                raise SystemExit(f"OVERLAP layout {name}: {la} vs {lb}")
    print(f"  [cek] layout {name}: {len(LAYOUT)} kotak, tidak ada overlap")


class TileText:
    """Kumpulkan bbox teks satu tile; assert tidak ada yang overlap."""

    def __init__(self, label):
        self.label = label
        self.boxes = []

    def add(self, box, what):
        for b, w in self.boxes:
            if not (box[2] <= b[0] or b[2] <= box[0] or box[3] <= b[1]
                    or b[3] <= box[1]):
                raise SystemExit(
                    f"OVERLAP teks {self.label}: {what} vs {w}")
        self.boxes.append((box, what))

    def text(self, d, x, y, s, font, fill, anchor="la"):
        b = d.textbbox((x, y), s, font=font, anchor=anchor)
        d.text((x, y), s, font=font, fill=fill, anchor=anchor)
        self.add(b, repr(s[:24]))
        return b


def top_color(img):
    """Warna atas tile: warna PALING UMUM di strip atas 8px (banner solid;
    teks putih di banner adalah minoritas, jadi mode = warna banner)."""
    strip = img.crop((0, 0, img.size[0], 8))
    return Counter(strip.getdata()).most_common(1)[0][0]


def rgb_dist(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
            + (a[2] - b[2]) ** 2) ** 0.5


def contrast_white(bg):
    """Rasio kontras teks putih di atas bg (WCAG); banner 20px bold butuh
    >= 3,0 (teks besar)."""
    def lum(c):
        c = c / 255.0
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    l = 0.2126 * lum(bg[0]) + 0.7152 * lum(bg[1]) + 0.0722 * lum(bg[2])
    return 1.05 / (l + 0.05)


# ------------------------------------------------------------------ data
# 35 cerita Sabtu 21 Nov 2026, terverifikasi sumber primer (STORIES.md).
# CH4: Bitcoin (17->8) + Dragon (18->12) jadi kartu; Vietnam law (12->17)
# + freight derail (8->18) jadi brief; Rahul 136 / 344-2.
HEROES = [
    {"num": 1, "city": "Antalya", "place": "ANTALYA, TURKIYE",
     "topic": "COP31", "region": "GLOBAL",
     "title": "COP31 runs into overtime with no deal",
     "sum": ("Draft 2 drops fossil fuels; talks resume Saturday "
             "morning in Antalya."),
     "painter": "cop31", "map_city": "Antalya",
     "banner": "COP31: OVERTIME", "source": "AP · Reuters"},
    {"num": 2, "city": "Riyadh", "place": "RIYADH, SAUDI ARABIA",
     "topic": "MISSILES", "region": "MIDDLE EAST",
     "title": "Houthi missiles shot down over Riyadh",
     "sum": ("Third night of alerts; two blasts heard, no damage "
             "or casualties reported."),
     "painter": "riyadh", "map_city": "Riyadh",
     "banner": "3 MISSILES DOWN", "source": "Reuters"},
    {"num": 3, "city": "Junin", "place": "JUNIN, PERU",
     "topic": "QUAKE", "region": "AMERICAS",
     "title": "Strong quake hits Peru",
     "sum": ("Epicentre near Junin, 108 km deep; felt in Lima, "
             "no deaths, no tsunami threat."),
     "painter": "quake", "map_city": "Junin",
     "banner": "PERU: QUAKE 6.7", "source": "AFP · AP"},
]

CARDS = [
    {"num": 4, "city": "Kryvyi Rih", "place": "KRYVYI RIH, UKRAINE",
     "topic": "STRIKE", "region": "EUROPE",
     "title": "Kryvyi Rih double strike",
     "sum": "Double-tap on restaurant; 27 seriously hurt.",
     "painter": "kryvyi", "map_city": "Kryvyi Rih",
     "banner": "2 DEAD · 42 HURT", "source": "BBC · Kyiv Indep."},
    {"num": 5, "city": "Davao", "place": "DAVAO, PHILIPPINES",
     "topic": "AIR SAFETY", "region": "ASIA",
     "title": "Air Niugini jet lands in Davao",
     "sum": "Engine fire warning; all safe.",
     "painter": "davao", "map_city": "Davao",
     "banner": "ALL 146 SAFE", "source": "AP"},
    {"num": 6, "city": "Darmstadt", "place": "DARMSTADT, GERMANY",
     "topic": "SPACE", "region": "GLOBAL",
     "title": "BepiColombo arrives at Mercury",
     "sum": "Orbit burn due 19:24 CET tonight; 8-year trip ends.",
     "painter": "bepi", "map_city": "Darmstadt",
     "banner": "TONIGHT 19:24", "source": "ESA"},
    {"num": 7, "city": "Washington", "place": "WASHINGTON, USA",
     "topic": "TAX", "region": "AMERICAS",
     "title": "Trump vows tax on data centres",
     "sum": "US firms taxed if they build abroad.",
     "painter": "capitol", "map_city": "Washington",
     "banner": "TREMENDOUS TAX", "source": "Reuters"},
    {"num": 8, "city": "New York", "place": "GLOBAL MARKETS",
     "topic": "MARKETS", "region": "GLOBAL",
     "title": "Bitcoin slides early Saturday",
     "sum": "Down 3.6%; $1.5bn liquidated.",
     "painter": "bitcoin", "map_city": "New York",
     "banner": "BITCOIN $56,814", "source": "Reuters"},
    {"num": 9, "city": "Wellington", "place": "WELLINGTON, NZ",
     "topic": "CRICKET", "region": "OCEANIA",
     "title": "Rahul's century in Wellington",
     "sum": "Century No. 13; out 136, India 344/2 at tea.",
     "painter": "cricket", "map_city": "Wellington",
     "banner": "RAHUL 136", "source": "Reuters"},
    {"num": 10, "city": "Las Vegas", "place": "LAS VEGAS, USA",
     "topic": "FORMULA 1", "region": "AMERICAS",
     "title": "Las Vegas GP qualifying",
     "sum": "Antonelli fastest; Verstappen on pole.",
     "painter": "f1", "map_city": "Las Vegas",
     "banner": "ON POLE", "source": "Reuters · Sky"},
    {"num": 11, "city": "Hormuz", "place": "STRAIT OF HORMUZ",
     "topic": "DRONE", "region": "MIDDLE EAST",
     "title": "Iran says it downed MQ-9",
     "sum": "58th downing claimed; unverified.",
     "painter": "drone", "map_city": "Hormuz",
     "banner": "MQ-9 DOWN", "source": "Press TV"},
    {"num": 12, "city": "California", "place": "OFF CALIFORNIA, USA",
     "topic": "SPACE", "region": "AMERICAS",
     "title": "SpaceX Dragon splashdown",
     "sum": "Undocks from ISS; splashdown 16:55 EST.",
     "painter": "dragon", "map_city": "California Coast",
     "banner": "SPLASHDOWN", "source": "NASA"},
    {"num": 13, "city": "Turin", "place": "TURIN, ITALY",
     "topic": "TENNIS", "region": "EUROPE",
     "title": "ATP Finals semis in Turin",
     "sum": "Alcaraz–Shelton, Zverev–Medvedev.",
     "painter": "tennis", "map_city": "Turin",
     "banner": "SEMIS TONIGHT", "source": "ATP Tour"},
]

# Briefs 14-35: (nomor, kota, teks 1 baris + fakta/angka kunci, sumber,
# region). 2 kolom, 11/11 per kolom (brief #25 Bangkok dihapus 22 Nov
# atas permintaan Kevin supaya bawah kolom rata).
BRIEFS = [
    (14, "WARSAW", "Rutte flies to Warsaw today", "AP", "EUROPE"),
    (15, "IRAQ", "Road to Karbala reopens", "ANF", "MIDDLE EAST"),
    (16, "YEMEN", "Houthis warn ships off ports", "Dawn", "MIDDLE EAST"),
    (17, "VIETNAM", "Laws speed land seizures", "Reuters", "ASIA"),
    (18, "SEJONG", "Freight train derails", "Yonhap", "ASIA"),
    (19, "S. AFRICA", "ANC fights to keep key cities", "BBC", "AFRICA"),
    (20, "USA", "$811m migrants scam continues", "BBC", "AMERICAS"),
    (21, "INDIA", "India vs Korea tonight", "Hockey India", "ASIA"),
    (22, "LISBON", "CGTP marches today", "downriver", "EUROPE"),
    (23, "MANILA", "Pet cremation scam: 170 dumped", "BBC", "ASIA"),
    (24, "JAKARTA", "PLN signs clean-power deals", "Antara", "ASIA"),
    (25, "NEW DELHI", "Pakistani minister speaks", "The News", "ASIA"),
    (26, "E. INDIA", "Akvan rain soaks east India", "Jagran", "ASIA"),
    (27, "AUSTRALIA", "Cummins keeps the captaincy", "AAP", "OCEANIA"),
    (28, "ITALY", "Rail strike halts trains today", "Treniamo", "EUROPE"),
    (29, "NAGA", "Naga votes on city status", "PNA", "ASIA"),
    (30, "JAVA", "M4.6 quake off Java", "BMKG", "ASIA"),
    (31, "CHILE", "M4.7 quake in northern Chile", "USGS", "AMERICAS"),
    (32, "DELHI", "Delhi chokes: AQI 279", "CPCB", "ASIA"),
    (33, "VISAYAS", "Grid on yellow alert", "NGCP", "ASIA"),
    (34, "TASMANIA", "One Nation donors revealed", "ABC", "OCEANIA"),
    (35, "MELBOURNE", "T20 opener tonight", "cricket.com.au", "OCEANIA"),
]

NUMBERS = [("13", "DAY 13 \u00b7 COP31"), ("3", "MISSILES DOWNED"),
           ("6.7", "PERU QUAKE"), ("146", "SAFE IN DAVAO"),
           ("42", "HURT IN KRYVYI RIH"), ("$56,814", "BITCOIN SAT AM")]

# Bar region: hitungan dari 35 cerita KAMI (bukan angka rank 2 yang
# dikutip loss report — angka itu total 32 = cerita rank 2).
# Asia 12, Americas 6, Europe 5, Middle East 4, Oceania 4, Global 3,
# Africa 1 — lihat stories-21nov.md.
REGION_BAR = [("EUROPE", 5), ("MIDDLE EAST", 4), ("AFRICA", 1),
              ("ASIA", 12), ("AMERICAS", 6), ("OCEANIA", 4),
              ("WORLD", 3)]

# Warna region: dipakai banner + segmen bar region + pin peta (satu
# sistem). Semua cukup gelap untuk teks putih >= 3,0:1 (dicek di build).
REGION_COLORS = {
    "EUROPE": (31, 58, 95),
    "MIDDLE EAST": (176, 48, 38),
    "AFRICA": (140, 80, 25),
    "ASIA": (46, 110, 142),
    "AMERICAS": (30, 95, 75),
    "AMERICAS_ALT": (24, 80, 110),
    "OCEANIA": (90, 70, 140),
    "GLOBAL": (120, 88, 10),
}
# Varian AMERICAS dipakai bila dua panel AMERICAS bertetangga
# (H3 vs kartu 7; kartu 7 vs kartu 12) — greedy di assign_banners.
REGION_ALT = {"AMERICAS": "AMERICAS_ALT"}

DECK = ("COP31 in overtime  \u00b7  Three missiles down over Riyadh  \u00b7  "
        "Peru quake 6.7  \u00b7  Kryvyi Rih double strike  \u00b7  "
        "Davao: all 146 safe")

DATECHECK_LIST = ("Left out as Friday 20 Nov news: Kyiv bridges hit \u00b7 "
                  "missile in Poland \u00b7 Wall Street correction \u00b7 UK\u2013EU "
                  "deal \u00b7 Akvan landfall \u00b7 ICJ Myanmar ruling \u00b7 "
                  "Iran uranium \u00b7 Taiwan warning \u00b7 Shenzhen summit \u00b7 "
                  "Anthropic IPO \u00b7 GTA VI launch. "
                  "Not yet happened: BepiColombo (19:24 CET) \u00b7 ATP semis "
                  "\u00b7 T20 opener.")

DC_BRIEF = ("Every story here happened, or was first reported, on "
            "Saturday 21 Nov 2026. Friday\u2019s news was left out; "
            "tonight\u2019s events have not happened yet.")

SOURCES = ("Sources: Reuters \u00b7 AP \u00b7 AFP \u00b7 BBC \u00b7 USGS \u00b7 "
           "NASA \u00b7 Antara \u00b7 Yonhap \u00b7 ATP Tour \u00b7 ESA \u00b7 "
           "Kyiv Independent \u00b7 NGCP \u00b7 BMKG")

# ------------------------------------------------------------------ peta
# Outline benua DETAIL Natural Earth 110m land (Public Domain).
# Proyeksi referensi ni20 (diukur dari peta referensi 2048):
# x-scale 0,815 px/derajat, y-scale 1,0 px/derajat (regang 1,23x).
# V2 (CH5): peta lebih TERANG dari V1 (laut navy gelap -> biru muda).
MAP_LAND = (235, 225, 195)
MAP_LAND_OUT = (200, 180, 140)
MAP_SX, MAP_SY = 0.815, 1.0
MAP_LAT0 = 83.0
SEA = (70, 110, 150)


def load_land_polys():
    path = os.path.join(HERE, "ne_110m_land.geojson")
    with open(path) as fh:
        data = json.load(fh)
    polys = []
    for feat in data["features"]:
        for ring in feat["geometry"]["coordinates"]:
            if len(ring) < 4:
                continue
            lats = [p[1] for p in ring]
            if max(lats) < -60:
                continue
            xs = [p[0] for p in ring]
            ys = lats
            if (max(xs) - min(xs)) < 0.4 and (max(ys) - min(ys)) < 0.4:
                continue
            out = [ring[0]]
            for p in ring[1:]:
                if (abs(p[0] - out[-1][0]) > 0.12
                        or abs(p[1] - out[-1][1]) > 0.12):
                    out.append(p)
            if out[-1] != ring[-1]:
                out.append(ring[-1])
            polys.append(out)
    return polys


LAND_POLYS = load_land_polys()

# lon/lat pin 1-13 (lead + feature). #6 BepiColombo: ESOC Darmstadt
# (pusat kendali misi ESA) — tidak ada lokasi Bumi untuk Merkurius.
# #8 Bitcoin: proxy New York (pasar AS; Nasdaq -5,3% Jumat) — Bitcoin
# sendiri global, tidak punya lokasi; dicatat di improve_2026-11-21.md.
# #12 Dragon: zona splashdown lepas pantai California.
PLACES = {
    "Antalya": (30.7, 36.9), "Riyadh": (46.7, 24.7),
    "Junin": (-75.9, -10.9), "Kryvyi Rih": (33.4, 47.9),
    "Davao": (125.6, 7.1), "Darmstadt": (8.65, 49.87),
    "Washington": (-77.0, 38.9), "New York": (-74.0, 40.7),
    "Wellington": (174.8, -41.3), "Las Vegas": (-115.1, 36.2),
    "Hormuz": (56.5, 27.0), "California Coast": (-122.0, 34.0),
    "Turin": (7.7, 45.1),
}

# ------------------------------------------------------------------ painters
# SATU gaya ilustrasi datar. Aturan: banner (blok warna solid, 28-30px)
# menutupi strip atas gambar; ilustrasi digambar di zona di bawah banner.
# Subjek UTAMA besar di tengah + margin; konteks hidup kelihatan.

# 6 tint kalem (jarak RGB antar semua pasangan >= 28, dicek di bawah)
# — latar ilustrasi kartu (bukan warna atas; warna atas = banner region).
TINTS = {
    "steel": (178, 205, 224),
    "rose": (240, 180, 175),
    "gold": (242, 228, 185),
    "sage": (190, 220, 195),
    "lilac": (222, 210, 238),
    "peach": (245, 215, 160),
}
# Hero: latar gelap (hierarki — hero harus paling menonjol).
HERO_BG = {"cop31": (17, 54, 60), "riyadh": (64, 28, 34),
           "quake": (122, 88, 48)}

# ------------------------------------------------------------------ painters
# Hero painters digambar untuk zona ilustrasi h=70 (di bawah banner 30px).
# Card painters digambar untuk zona ilustrasi h=48 (di bawah banner 28px).
# Chip kecil V1 dihapus — info itu kini di banner + chip sumber.

def p_cop31(w, h):
    """Hero 1 COP31: panel teal gelap + globe + termometer + kartu putih
    'COP31 / NO DEAL' (fakta: overtime, draf tanpa fosil)."""
    bg = HERO_BG["cop31"]
    im = Image.new("RGB", (w, h), bg)
    d = ImageDraw.Draw(im)
    gx, gy, gr = 40, 36, 20
    d.ellipse([gx - gr, gy - gr, gx + gr, gy + gr], fill=(70, 130, 180),
              outline=NAVY, width=2)
    d.ellipse([gx - 11, gy - 8, gx + 1, gy + 3], fill=(90, 150, 90))
    d.ellipse([gx - 1, gy + 7, gx + 11, gy + 15], fill=(90, 150, 90))
    d.ellipse([gx + 5, gy - 13, gx + 13, gy - 3], fill=(90, 150, 90))
    tx = 76
    d.rounded_rectangle([tx, 12, tx + 10, 54], radius=5,
                        fill=(240, 244, 246), outline=NAVY, width=1)
    d.rectangle([tx + 3, 30, tx + 7, 50], fill=RED_M)
    d.ellipse([tx - 2, 48, tx + 12, 62], fill=RED_M, outline=NAVY, width=1)
    kx0, ky0, kx1, ky1 = 106, 8, w - 8, h - 8
    d.rectangle([kx0, ky0, kx1, ky1], fill=WHITE, outline=NAVY, width=1)
    d.text(((kx0 + kx1) // 2, ky0 + 5), "ANTALYA \u00b7 NOV 21",
           font=F(SS800, 7), fill=RED_M, anchor="ma")
    d.text(((kx0 + kx1) // 2, ky0 + 17), "COP31", font=F(GEL700, 22),
           fill=NAVY, anchor="ma")
    d.text(((kx0 + kx1) // 2, ky1 - 14), "NO DEAL",
           font=F(SS800, 7), fill=RED_M, anchor="ma")
    return im


def p_riyadh(w, h):
    """Hero 2 Riyadh: langit malam + skyline (menara Kingdom Centre) +
    TIGA jejak intersepsi + tiga ledakan putih (fakta: 3 rudal dicegat).
    """
    bg = HERO_BG["riyadh"]
    im = Image.new("RGB", (w, h), bg)
    d = ImageDraw.Draw(im)
    for (sx, sy) in [(20, 8), (70, 6), (130, 10), (180, 7), (230, 9),
                     (45, 16), (160, 14), (260, 15)]:
        d.ellipse([sx, sy, sx + 2, sy + 2], fill=(220, 220, 200))
    gy = h - 10
    d.rectangle([0, gy, w, h], fill=(30, 18, 22))
    # skyline: gedung-gedung gelap + menara Kingdom Centre (bukaan khas)
    for (bx, bw, bh) in [(0, 30, 30), (34, 22, 40), (60, 26, 24),
                         (180, 24, 32), (208, 30, 22), (242, 26, 38)]:
        d.rectangle([bx, gy - bh, bx + bw, gy], fill=(16, 14, 18))
        for wy in range(gy - bh + 6, gy - 4, 10):
            d.rectangle([bx + 4, wy, bx + bw - 4, wy + 3],
                        fill=(240, 200, 90))
    kx, kw = 92, 76
    d.rectangle([kx, gy - 56, kx + kw, gy], fill=(16, 14, 18))
    d.polygon([(kx + 16, gy - 56), (kx + kw - 16, gy - 56),
               (kx + kw // 2, gy - 34)], fill=bg)
    d.rectangle([kx + 5, gy - 52, kx + kw - 5, gy - 4], fill=(16, 14, 18))
    # TIGA jejak intersepsi emas + ledakan putih
    for (x0, y0, x1, y1) in [(30, gy - 2, 95, 22), (130, gy - 2, 185, 18),
                             (220, gy - 2, 258, 24)]:
        steps = 8
        for i in range(steps):
            fx0 = x0 + (x1 - x0) * i / steps
            fy0 = y0 + (y1 - y0) * i / steps
            fx1 = x0 + (x1 - x0) * (i + 0.55) / steps
            fy1 = y0 + (y1 - y0) * (i + 0.55) / steps
            d.line([(fx0, fy0), (fx1, fy1)], fill=(240, 200, 90), width=2)
        for (dx, dy) in [(0, 0), (-6, -2), (6, -2), (-3, 5), (3, 5)]:
            d.line([(x1, y1), (x1 + dx, y1 + dy)], fill=WHITE, width=2)
        d.ellipse([x1 - 3, y1 - 3, x1 + 3, y1 + 3], fill=WHITE)
    return im


def p_quake(w, h):
    """Hero 3 Peru: pegunungan Andes + garis seismograf + retakan tanah."""
    bg = HERO_BG["quake"]
    im = Image.new("RGB", (w, h), bg)
    d = ImageDraw.Draw(im)
    d.ellipse([w - 40, 8, w - 16, 32], fill=(250, 240, 200))
    gy = h - 14
    for (mx, mw, mh, snow) in [(14, 120, 44, True), (100, 140, 54, True),
                               (210, 100, 36, False)]:
        d.polygon([(mx, gy), (mx + mw // 2, gy - mh), (mx + mw, gy)],
                  fill=(70, 48, 30))
        if snow:
            d.polygon([(mx + mw // 2 - 10, gy - mh + 14),
                       (mx + mw // 2, gy - mh),
                       (mx + mw // 2 + 10, gy - mh + 14)],
                      fill=WHITE)
    d.rectangle([0, gy, w, h], fill=(52, 36, 22))
    d.line([(8, gy + 5), (50, gy + 9), (80, gy + 3), (120, gy + 10),
            (160, gy + 4), (200, gy + 9), (260, gy + 5)],
           fill=(40, 26, 16), width=3)
    pts = [(8, 30), (30, 30), (40, 22), (50, 38), (60, 30), (90, 30),
           (100, 25), (110, 35), (120, 30), (150, 30), (160, 24),
           (170, 36), (180, 30), (210, 30), (260, 30)]
    d.line(pts, fill=WHITE, width=2, joint="curve")
    return im


def p_kryvyi(w, h, bg):
    """Kartu 4: gedung kena serangan + bintang ledakan merah + asap."""
    im = Image.new("RGB", (w, h), bg)
    d = ImageDraw.Draw(im)
    gy = int(h * 0.86)
    d.rectangle([0, gy, w, h], fill=(90, 80, 70))
    bx0, bx1, by0 = int(w * 0.30), int(w * 0.66), int(h * 0.38)
    d.rectangle([bx0, by0, bx1, gy], fill=(70, 62, 58), outline=NAVY,
                width=1)
    d.polygon([(bx0, by0), (bx1, by0), (bx1 - 14, by0 - 10),
               (bx0 + 10, by0 - 10)], fill=(52, 46, 42))
    for wy in range(by0 + 8, gy - 6, 10):
        for wx in (bx0 + 6, bx0 + 20):
            d.rectangle([wx, wy, wx + 8, wy + 6], fill=(240, 210, 120))
    cx, cy = int(w * 0.78), int(h * 0.34)
    for (dx, dy) in [(0, -14), (10, -10), (14, 0), (10, 10), (0, 14),
                     (-10, 10), (-14, 0), (-10, -10)]:
        d.line([(cx, cy), (cx + dx, cy + dy)], fill=RED_M, width=3)
    d.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=RED_M)
    d.ellipse([int(w * 0.14), int(h * 0.22), int(w * 0.14) + 12,
               int(h * 0.22) + 8], fill=(235, 235, 230))
    d.ellipse([int(w * 0.20), int(h * 0.16), int(w * 0.20) + 9,
               int(h * 0.16) + 6], fill=(235, 235, 230))
    return im


def p_davao(w, h, bg):
    """Kartu 5: pesawat besar + landasan."""
    im = Image.new("RGB", (w, h), bg)
    d = ImageDraw.Draw(im)
    gy = int(h * 0.80)
    d.rectangle([0, gy, w, h], fill=(90, 90, 90))
    for x in range(0, w, 18):
        d.line([(x, gy + 6), (x + 9, gy + 6)], fill=WHITE, width=2)
    cx, cy = w // 2, int(h * 0.56)
    d.ellipse([cx - 52, cy - 9, cx + 52, cy + 9], fill=WHITE, outline=NAVY,
              width=1)
    d.polygon([(cx + 30, cy - 8), (cx + 52, cy - 20), (cx + 58, cy - 20),
               (cx + 44, cy - 6)], fill=WHITE, outline=NAVY)
    d.polygon([(cx - 8, cy - 8), (cx + 2, cy - 18), (cx + 12, cy - 18),
               (cx + 8, cy - 8)], fill=WHITE, outline=NAVY)
    d.polygon([(cx - 44, cy + 6), (cx - 30, cy + 20), (cx - 22, cy + 20),
               (cx - 30, cy + 6)], fill=WHITE, outline=NAVY)
    d.ellipse([cx + 40, cy - 4, cx + 48, cy + 4], fill=NAVY)
    return im


def p_bepi(w, h, bg):
    """Kartu 6: wahana BepiColombo + Merkurius."""
    im = Image.new("RGB", (w, h), bg)
    d = ImageDraw.Draw(im)
    for (sx, sy) in [(14, 6), (52, 10), (120, 5), (168, 8)]:
        d.ellipse([sx, sy, sx + 2, sy + 2], fill=WHITE)
    mx, my, mr = int(w * 0.72), int(h * 0.52), 15
    d.ellipse([mx - mr, my - mr, mx + mr, my + mr], fill=(150, 140, 130),
              outline=NAVY, width=1)
    d.ellipse([mx - 8, my - 5, mx - 2, my + 1], fill=(110, 100, 90))
    d.ellipse([mx + 2, my + 4, mx + 7, my + 9], fill=(110, 100, 90))
    cx, cy = int(w * 0.30), int(h * 0.50)
    d.rectangle([cx - 12, cy - 9, cx + 12, cy + 9], fill=GOLD_M,
                outline=NAVY, width=1)
    d.rectangle([cx - 34, cy - 5, cx - 12, cy + 5], fill=NAVY)
    d.rectangle([cx + 12, cy - 5, cx + 34, cy + 5], fill=NAVY)
    d.line([(cx + 34, cy), (mx - mr - 2, my)], fill=GOLD_M, width=2)
    d.ellipse([cx - 2, cy - 2, cx + 2, cy + 2], fill=RED_M)
    return im


def p_capitol(w, h, bg):
    """Kartu 7: kubah Capitol + bendera AS.
    (Tanpa figur presiden — aturan Kevin: presiden tidak seram.)"""
    im = Image.new("RGB", (w, h), bg)
    d = ImageDraw.Draw(im)
    gy = int(h * 0.84)
    d.rectangle([0, gy, w, h], fill=(120, 110, 90))
    cx = w // 2
    d.rectangle([cx - 52, gy - 8, cx + 52, gy], fill=WHITE, outline=NAVY,
                width=1)
    for i in range(5):
        d.rectangle([cx - 46 + i * 20, gy - 24, cx - 34 + i * 20, gy - 8],
                    fill=WHITE, outline=NAVY, width=1)
    d.ellipse([cx - 16, gy - 34, cx + 16, gy - 18], fill=WHITE,
              outline=NAVY, width=1)
    d.rectangle([cx - 18, gy - 24, cx + 18, gy - 20], fill=WHITE,
                outline=NAVY, width=1)
    return im


def p_bitcoin(w, h, bg):
    """Kartu 8 (BARU, CH4): koin Bitcoin besar + garis turun merah
    (fakta: -3,6% ke $56.814, terendah sejak Sep 2024)."""
    im = Image.new("RGB", (w, h), bg)
    d = ImageDraw.Draw(im)
    cx, cy, r = int(w * 0.30), int(h * 0.52), 15
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GOLD_M,
              outline=NAVY, width=1)
    d.ellipse([cx - r + 3, cy - r + 3, cx + r - 3, cy + r - 3],
              outline=WHITE, width=1)
    f_b = F(SS800, 18)
    b = d.textbbox((cx, cy), "B", font=f_b, anchor="mm")
    d.text((cx, cy), "B", font=f_b, fill=WHITE, anchor="mm")
    d.line([(cx - 4, b[1] - 2), (cx - 4, b[3] + 2)], fill=WHITE, width=2)
    d.line([(cx + 4, b[1] - 2), (cx + 4, b[3] + 2)], fill=WHITE, width=2)
    pts = [(int(w * 0.56), int(h * 0.22)), (int(w * 0.66), int(h * 0.40)),
           (int(w * 0.74), int(h * 0.34)), (int(w * 0.86), int(h * 0.66)),
           (int(w * 0.94), int(h * 0.60))]
    d.line(pts, fill=RED_M, width=3, joint="curve")
    ax, ay = pts[-1]
    d.polygon([(ax, ay), (ax - 8, ay - 1), (ax - 2, ay + 7)], fill=RED_M)
    return im


def p_cricket(w, h, bg):
    """Kartu 9: stumps + bat + bola + angka '136' besar (CH4: Rahul 136)."""
    im = Image.new("RGB", (w, h), bg)
    d = ImageDraw.Draw(im)
    gy = int(h * 0.88)
    d.rectangle([0, gy, w, h], fill=(90, 130, 80))
    for i in range(3):
        sx = int(w * (0.14 + i * 0.05))
        d.rectangle([sx, int(h * 0.40), sx + 4, gy], fill=GOLD_M,
                    outline=NAVY, width=1)
    d.rectangle([int(w * 0.14), int(h * 0.38), int(w * 0.26), int(h * 0.40)],
                fill=GOLD_M, outline=NAVY, width=1)
    d.polygon([(int(w * 0.52), int(h * 0.18)), (int(w * 0.58), int(h * 0.22)),
               (int(w * 0.44), int(h * 0.78)), (int(w * 0.38), int(h * 0.74))],
              fill=(150, 110, 70), outline=NAVY)
    d.ellipse([int(w * 0.62), int(h * 0.62), int(w * 0.62) + 9,
               int(h * 0.62) + 9], fill=RED_M, outline=NAVY, width=1)
    f136 = F(GEL700, 20)
    d.text((w - 6, int(h * 0.30)), "136", font=f136, fill=NAVY,
           anchor="ra")
    return im


def p_f1(w, h, bg):
    """Kartu 10: mobil F1 + bendera kotak-kotak."""
    im = Image.new("RGB", (w, h), bg)
    d = ImageDraw.Draw(im)
    gy = int(h * 0.82)
    d.rectangle([0, gy, w, h], fill=(70, 70, 70))
    for x in range(0, w, 16):
        d.line([(x, gy + 5), (x + 8, gy + 5)], fill=WHITE, width=2)
    cx, cy = w // 2, int(h * 0.52)
    d.polygon([(cx - 62, cy + 2), (cx - 30, cy - 2), (cx + 10, cy - 2),
               (cx + 58, cy + 6), (cx + 58, cy + 12), (cx - 62, cy + 12)],
              fill=RED_M, outline=NAVY)
    d.polygon([(cx - 6, cy - 2), (cx + 6, cy - 14), (cx + 16, cy - 14),
               (cx + 20, cy - 2)], fill=NAVY)
    d.ellipse([cx - 40, cy + 8, cx - 22, cy + 24], fill=INK, outline=WHITE,
              width=1)
    d.ellipse([cx + 30, cy + 8, cx + 48, cy + 24], fill=INK, outline=WHITE,
              width=1)
    for r in range(2):
        for c in range(3):
            col = WHITE if (r + c) % 2 == 0 else INK
            d.rectangle([w - 34 + c * 8, 10 + r * 8, w - 26 + c * 8,
                         18 + r * 8], fill=col, outline=NAVY, width=1)
    d.line([(w - 34, 10), (w - 34, 34)], fill=NAVY, width=2)
    return im


def p_drone(w, h, bg):
    """Kartu 11: drone quadcopter di atas laut
    (klaim Iran — belum terverifikasi independen)."""
    im = Image.new("RGB", (w, h), bg)
    d = ImageDraw.Draw(im)
    gy = int(h * 0.62)
    d.rectangle([0, gy, w, h], fill=(46, 110, 142))
    for x in range(0, w, 22):
        d.arc([x, gy + 2, x + 22, gy + 12], 0, 180, fill=WHITE, width=2)
    cx, cy = w // 2, int(h * 0.34)
    d.rectangle([cx - 16, cy - 6, cx + 16, cy + 6], fill=(60, 60, 60),
                outline=NAVY, width=1)
    for (dx, dy) in [(-26, -12), (26, -12), (-26, 12), (26, 12)]:
        d.line([(cx, cy), (cx + dx, cy + dy)], fill=NAVY, width=2)
        d.ellipse([cx + dx - 8, cy + dy - 2, cx + dx + 8, cy + dy + 2],
                  fill=(120, 120, 120), outline=NAVY, width=1)
    d.ellipse([cx - 3, cy - 3, cx + 3, cy + 3], fill=RED_M)
    return im


def p_dragon(w, h, bg):
    """Kartu 12 (BARU, CH4): kapsul Dragon + parasut + laut
    (fakta: splashdown lepas pantai California ~16:55 EST Sabtu)."""
    im = Image.new("RGB", (w, h), bg)
    d = ImageDraw.Draw(im)
    gy = int(h * 0.62)
    d.rectangle([0, gy, w, h], fill=(46, 110, 142))
    for x in range(0, w, 22):
        d.arc([x, gy + 2, x + 22, gy + 12], 0, 180, fill=WHITE, width=2)
    cx, cy = w // 2, int(h * 0.40)
    # parasut: tiga panel oranye/putih
    d.pieslice([cx - 34, cy - 26, cx + 34, cy + 6], 180, 360,
               fill=(230, 120, 40), outline=NAVY, width=1)
    d.pieslice([cx - 18, cy - 26, cx + 18, cy + 6], 180, 360,
               fill=WHITE, outline=NAVY, width=1)
    d.line([(cx - 34, cy - 8), (cx - 8, cy + 2)], fill=NAVY, width=1)
    d.line([(cx + 34, cy - 8), (cx + 8, cy + 2)], fill=NAVY, width=1)
    d.line([(cx, cy - 26), (cx, cy + 2)], fill=NAVY, width=1)
    # kapsul
    d.rounded_rectangle([cx - 14, cy + 2, cx + 14, cy + 16], radius=4,
                        fill=WHITE, outline=NAVY, width=1)
    d.ellipse([cx - 4, cy + 6, cx + 4, cy + 12], fill=NAVY)
    # percikan di laut
    for (sx, sy) in [(cx - 22, gy + 4), (cx + 20, gy + 6),
                     (cx - 8, gy + 8)]:
        d.arc([sx, sy, sx + 10, sy + 6], 180, 360, fill=WHITE, width=2)
    return im


def p_tennis(w, h, bg):
    """Kartu 13: bola tenis besar + garis lapangan."""
    im = Image.new("RGB", (w, h), bg)
    d = ImageDraw.Draw(im)
    gy = int(h * 0.84)
    d.rectangle([0, gy, w, h], fill=(60, 110, 70))
    d.line([(0, int(h * 0.60)), (w, int(h * 0.60))], fill=WHITE, width=2)
    cx, cy, r = int(w * 0.42), int(h * 0.50), 12
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(200, 220, 60),
              outline=NAVY, width=1)
    d.arc([cx - r, cy - r, cx + r, cy + r], 200, 340, fill=WHITE, width=2)
    d.arc([cx - r, cy - r, cx + r, cy + r], 20, 160, fill=WHITE, width=2)
    d.rectangle([int(w * 0.72), int(h * 0.30), int(w * 0.72) + 26,
                 int(h * 0.30) + 18], fill=WHITE, outline=NAVY, width=1)
    d.line([(int(w * 0.72), int(h * 0.30) + 9),
            (int(w * 0.72) + 26, int(h * 0.30) + 9)], fill=NAVY, width=1)
    return im


CARD_PAINTERS = {"kryvyi": p_kryvyi, "davao": p_davao, "bepi": p_bepi,
                 "capitol": p_capitol, "bitcoin": p_bitcoin,
                 "cricket": p_cricket, "f1": p_f1, "drone": p_drone,
                 "dragon": p_dragon, "tennis": p_tennis}
HERO_PAINTERS = {"cop31": p_cop31, "riyadh": p_riyadh, "quake": p_quake}


def panel_neighbors(panels):
    """Pasangan panel yang berbagi sisi (toleransi 12px) — untuk aturan
    warna atas tetangga."""
    out = {}
    for i, (x1, y1, x2, y2) in enumerate(panels):
        ns = []
        for j, (a1, b1, a2, b2) in enumerate(panels):
            if i == j:
                continue
            share_v = (abs(x2 - a1) <= 12 or abs(a2 - x1) <= 12) \
                and min(y2, b2) - max(y1, b1) > 0
            share_h = (abs(y2 - b1) <= 12 or abs(b2 - y1) <= 12) \
                and min(x2, a2) - max(x1, a1) > 0
            if share_v or share_h:
                ns.append(j)
        out[i] = ns
    return out


def assign_tints(panels):
    """Greedy: latar ilustrasi kartu tetangga selalu beda >= 25 (jarak
    RGB). Panel hero sudah punya latar gelap tetap."""
    nbrs = panel_neighbors(panels)
    fixed = [HERO_BG["cop31"], HERO_BG["riyadh"], HERO_BG["quake"]]
    colors = [None] * len(panels)
    for i in range(3):
        colors[i] = fixed[i]
    names = list(TINTS)
    for i in range(3, len(panels)):
        taken = [colors[j] for j in nbrs[i] if colors[j] is not None]
        pick = None
        for name in names:
            c = TINTS[name]
            if all(rgb_dist(c, t) >= 25 for t in taken):
                pick = c
                break
        if pick is None:
            raise SystemExit(f"tidak ada tint untuk panel {i}")
        colors[i] = pick
    for i in range(len(panels)):
        for j in nbrs[i]:
            assert rgb_dist(colors[i], colors[j]) >= 25, (
                f"tint tetangga sama/dekat: panel {i} vs {j}: "
                f"{rgb_dist(colors[i], colors[j]):.1f}")
    print(f"  [cek] tint ilustrasi: {len(panels)} panel, tetangga >= 25 "
          f"(min {min(rgb_dist(colors[i], colors[j]) for i in range(len(panels)) for j in nbrs[i]):.1f})")
    return colors


def assign_banners(panels, regions):
    """Greedy: warna BANNER (warna atas panel) = warna region panel;
    bila tetangga berbagi region, pakai varian alt region itu. Semua
    tetangga ortogonal harus beda >= 25; kontras putih >= 3,0."""
    nbrs = panel_neighbors(panels)
    colors = [None] * len(panels)
    for i, region in enumerate(regions):
        cands = [REGION_COLORS[region]]
        if region in REGION_ALT:
            cands.append(REGION_COLORS[REGION_ALT[region]])
        taken = [colors[j] for j in nbrs[i] if colors[j] is not None]
        pick = None
        for c in cands:
            if all(rgb_dist(c, t) >= 25 for t in taken):
                pick = c
                break
        if pick is None:
            raise SystemExit(
                f"tidak ada warna banner untuk panel {i} ({region})")
        colors[i] = pick
    for i in range(len(panels)):
        for j in nbrs[i]:
            assert rgb_dist(colors[i], colors[j]) >= 25, (
                f"banner tetangga sama/dekat: panel {i} vs {j}: "
                f"{rgb_dist(colors[i], colors[j]):.1f}")
        assert contrast_white(colors[i]) >= 3.0, (
            f"kontras banner panel {i} < 3,0: "
            f"{contrast_white(colors[i]):.2f}")
    print(f"  [cek] banner: {len(panels)} panel, tetangga >= 25 "
          f"(min {min(rgb_dist(colors[i], colors[j]) for i in range(len(panels)) for j in nbrs[i]):.1f}), "
          f"kontras putih min "
          f"{min(contrast_white(c) for c in colors):.2f}")
    return colors

# ------------------------------------------------------------------ layout
# Geometri V2 (berubah dari V1: +bar region 24px; hero lebih pendek,
# kartu lebih tinggi untuk headline 18px; map/briefs lebih pendek).
TITLE_Y = 16
STRIP_Y, STRIP_H = 108, 48
REGION_Y, REGION_H = 160, 24
HERO_Y, HERO_H = 190, 222
HERO_IMG_H = 100          # banner 30 + ilustrasi 70
HERO_BANNER_H = 30
HERO_X = [28, 354, 680]
HERO_W = 316
CARD_Y = [414, 588]
CARD_H = 170
CARD_IMG_H = 76           # banner 28 + ilustrasi 48
CARD_BANNER_H = 28
CARD_X = [28, 223, 418, 613, 808]
CARD_W = 186
MAP_BOX = (28, 762, 408, 936)
BRIEFS_BOX = (420, 762, 996, 936)
DC_BOX = (28, 942, 996, 992)
SRC_Y = 998
MAP_HEADER_H = 22


def tracked_width(d, text, font, tracking=-0.4):
    return (sum(d.textlength(ch, font=font) for ch in text)
            + tracking * (len(text) - 1))


def draw_tracked(d, cx, y, text, font, fill, tracking=-0.4):
    total = tracked_width(d, text, font, tracking)
    x = cx - total / 2.0
    x0 = x
    for ch in text:
        d.text((x, y), ch, font=font, fill=fill, anchor="la")
        x += d.textlength(ch, font=font) + tracking
    return x0, x0 + total


def draw_masthead(d):
    """Judul HITAM Gelasio 700 56px satu baris + deck merah Gelasio
    Italic 12px (5 cerita terbesar, tanpa awalan)."""
    tt = TileText("masthead")
    f_title = F(GEL700, 56)
    title = "Saturday 21 November 2026"
    tw = tracked_width(d, title, f_title)
    assert tw <= W - 56, f"judul terlalu lebar: {tw:.0f}px"
    tb = d.textbbox((W // 2, TITLE_Y), title, font=f_title, anchor="mt")
    x0, x1 = draw_tracked(d, W // 2, TITLE_Y, title, f_title, INK)
    tt.add((int(x0), tb[1], int(x1), tb[3]), "title")
    title_bottom = tb[3]
    f_deck = F(GEL_IT, 12)
    dw = d.textlength(DECK, font=f_deck)
    assert dw <= W - 56, f"deck terlalu lebar: {dw:.0f}px"
    b = d.textbbox((W // 2, title_bottom + 14), DECK, font=f_deck,
                   anchor="mt")
    d.text((W // 2, title_bottom + 14), DECK, font=f_deck, fill=RED,
           anchor="mt")
    tt.add(b, "deck")
    assert 13 <= b[1] - title_bottom <= 15, (
        f"celah judul->deck {b[1] - title_bottom}px")
    reg_layout((28, TITLE_Y, 996, b[3]), "masthead")
    return {"title_w": round(tw, 1), "deck_w": round(dw, 1),
            "deck_bottom": b[3],
            "title_pct": round(100 * tw / W, 1)}


def draw_strip(d):
    """Strip 6 angka: angka merah SS700 30pt + caption 9pt.
    TANPA garis pemisah ke hero (aturan Kevin)."""
    tt = TileText("strip")
    f_n = F(SS700, 30)
    f_c = F(SS800, 9)
    d.rectangle([28, STRIP_Y, 994, STRIP_Y + STRIP_H], outline=NAVY,
                width=1)
    d.rectangle([29, STRIP_Y + 1, 993, STRIP_Y + STRIP_H - 1],
                fill=NEAR_WHITE)
    reg_layout((28, STRIP_Y, 994, STRIP_Y + STRIP_H), "strip")
    widths = [156, 156, 156, 156, 156, 156]
    x = 28
    for i, (num, cap) in enumerate(NUMBERS):
        cw = widths[i]
        cx = x + cw // 2
        if i < 5:
            d.line([(x + cw, STRIP_Y + 4), (x + cw, STRIP_Y + STRIP_H - 4)],
                   fill=(200, 195, 185), width=1)
        b = d.textbbox((cx, STRIP_Y + 0), num, font=f_n, anchor="ma")
        d.text((cx, STRIP_Y + 0), num, font=f_n, fill=RED, anchor="ma")
        tt.add(b, f"strip-n{i + 1}")
        assert b[2] - b[0] <= cw - 4, f"angka strip {num} terlalu lebar"
        b = d.textbbox((cx, STRIP_Y + 35), cap, font=f_c, anchor="ma")
        d.text((cx, STRIP_Y + 33), cap, font=f_c, fill=NAVY, anchor="ma")
        tt.add(b, f"strip-c{i + 1}")
        assert b[2] - b[0] <= cw - 4, f"caption strip '{cap}' terlalu lebar"
        x += cw + 6
    assert x - 6 == 994, f"strip tidak berakhir di 994: {x - 6}"


def draw_region_bar(d):
    """CH2: bar region tersegmentasi di bawah strip angka — 7 segmen sama
    lebar, warna = warna region (konsisten dengan pin peta + banner)."""
    tt = TileText("regionbar")
    x1, y1, x2 = 28, REGION_Y, 994
    seg_w = (x2 - x1) // 7
    reg_layout((x1, y1, x2, y1 + REGION_H), "regionbar")
    f_r = F(SS800, 10)
    x = x1
    for i, (name, count) in enumerate(REGION_BAR):
        w = seg_w if i < 6 else x2 - x
        color = REGION_COLORS["GLOBAL" if name == "WORLD" else name]
        d.rectangle([x, y1, x + w, y1 + REGION_H], fill=color)
        label = f"{name} \u00b7 {count}"
        b = d.textbbox((x + w // 2, y1 + REGION_H // 2), label, font=f_r,
                       anchor="mm")
        d.text((x + w // 2, y1 + REGION_H // 2), label, font=f_r,
               fill=WHITE, anchor="mm")
        tt.add(b, f"region-{name}")
        assert b[2] - b[0] <= w - 4, f"segmen region '{label}' terlalu lebar"
        x += w
    d.rectangle([x1, y1, x2, y1 + REGION_H], outline=NAVY, width=1)
    assert x == x2, f"bar region tidak berakhir di {x2}: {x}"
    return {"segments": len(REGION_BAR),
            "total": sum(c for _, c in REGION_BAR)}


def make_panel_img(painter_img, banner_color, banner_text, source,
                   banner_h, source_left):
    """Susun gambar panel: banner blok warna solid di atas (teks putih
    bold 20px, rata kiri) + ilustrasi di bawah + chip sumber hitam di
    bawah gambar (kiri untuk hero, kanan untuk kartu; font 12px,
    tinggi 17px, terbaca tanpa zoom)."""
    w, ih = painter_img.size
    im = Image.new("RGB", (w, ih + banner_h), banner_color)
    d = ImageDraw.Draw(im)
    im.paste(painter_img, (0, banner_h))
    f_b = F(SS800, 20)
    bw = d.textlength(banner_text, font=f_b)
    assert bw <= w - 12, (
        f"banner '{banner_text}' terlalu lebar: {bw:.0f}px > {w - 12}px")
    d.text((6, banner_h // 2), banner_text, font=f_b, fill=WHITE,
           anchor="lm")
    f_s = F(SS800, 12)
    tw = d.textlength(source, font=f_s)
    cw, ch = int(tw) + 12, 17
    assert cw <= w - 12, (
        f"chip sumber '{source}' terlalu lebar: {cw}px > {w - 12}px")
    if source_left:
        sx = 6
    else:
        sx = w - 6 - cw
    sy = ih + banner_h - ch - 4
    d.rounded_rectangle([sx, sy, sx + cw, sy + ch], radius=2,
                        fill=(10, 18, 36))
    d.text((sx + cw // 2, sy + ch // 2), source, font=f_s, fill=WHITE,
           anchor="mm")
    return im


def draw_hero(im, d, hero, x, y, panel_img):
    """Hero: gambar atas 100px (banner 30 + ilustrasi 70) + kicker 9pt +
    judul Gelasio 26px (<=2 baris) + ringkasan 16pt (2 baris)."""
    tt = TileText(f"hero{hero['num']}")
    im.paste(panel_img, (x + 1, y + 1))
    reg_layout((x, y, x + HERO_W, y + HERO_H), f"hero{hero['num']}")
    d.rectangle([x + 1, y + HERO_IMG_H + 1, x + HERO_W - 1, y + HERO_H - 1],
                fill=NEAR_WHITE)
    d.rectangle([x, y, x + HERO_W, y + HERO_H], outline=INK, width=1)
    tx0, tx1 = x + 8, x + HERO_W - 8
    kick = f"{hero['num']:02d} \u00b7 {hero['place']}"
    tt.text(d, tx0, y + HERO_IMG_H + 4, kick, F(SS800, 9),
            {"GLOBAL": (150, 120, 20), "MIDDLE EAST": (192, 57, 43),
             "AMERICAS": (62, 124, 89)}.get(hero['region'], NAVY))
    tlines = wrap(d, hero["title"], F(GEL700, 26), tx1 - tx0)
    assert 1 <= len(tlines) <= 2, f"judul hero {hero['num']}: {tlines}"
    yy = y + HERO_IMG_H + 18
    for ln in tlines:
        tt.text(d, tx0, yy, ln, F(GEL700, 26), INK)
        yy += 29
    slines = wrap(d, hero["sum"], F(SS400, 16), tx1 - tx0)
    assert len(slines) == 2, f"ringkasan hero {hero['num']}: {slines}"
    yy = y + HERO_IMG_H + 76
    for ln in slines:
        tt.text(d, tx0, yy, ln, F(SS400, 16), (60, 58, 50))
        yy += 19
    assert yy <= y + HERO_H - 6, f"hero {hero['num']} meluber"
    return {"title_lines": len(tlines), "sum_lines": len(slines)}


def draw_card(im, d, card, x, y, panel_img):
    """Kartu: gambar atas 76px (banner 28 + ilustrasi 48) + kicker 8pt +
    judul Gelasio 18px (<=2 baris) + ringkasan 16pt (<=2 baris)."""
    tt = TileText(f"card{card['num']}")
    im.paste(panel_img, (x + 1, y + 1))
    reg_layout((x, y, x + CARD_W, y + CARD_H), f"card{card['num']}")
    d.rectangle([x + 1, y + CARD_IMG_H + 1, x + CARD_W - 1, y + CARD_H - 1],
                fill=NEAR_WHITE)
    d.rectangle([x, y, x + CARD_W, y + CARD_H], outline=NAVY, width=1)
    tx0, tx1 = x + 6, x + CARD_W - 6
    kick = f"{card['num']:02d} \u00b7 {card['place']}"
    tt.text(d, tx0, y + CARD_IMG_H + 2, kick, F(SS800, 8),
            {"EUROPE": (38, 66, 118), "ASIA": (46, 110, 142),
             "GLOBAL": (150, 120, 20), "AMERICAS": (125, 38, 40),
             "MIDDLE EAST": (155, 115, 35),
             "OCEANIA": (30, 108, 114)}.get(card['region'], NAVY))
    tlines = wrap(d, card["title"], F(GEL700, 18), tx1 - tx0)
    assert 1 <= len(tlines) <= 2, f"judul kartu {card['num']}: {tlines}"
    yy = y + CARD_IMG_H + 14
    for ln in tlines:
        tt.text(d, tx0, yy, ln, F(GEL700, 18), INK)
        yy += 20
    slines = wrap(d, card["sum"], F(SS400, 16), tx1 - tx0)
    assert 1 <= len(slines) <= 2, f"ringkasan kartu {card['num']}: {slines}"
    yy = y + CARD_IMG_H + 54
    for ln in slines:
        tt.text(d, tx0, yy, ln, F(SS400, 16), (60, 58, 50))
        yy += 18
    assert yy <= y + CARD_H - 2, f"kartu {card['num']} meluber ke bawah"
    return {"title_lines": len(tlines), "sum_lines": len(slines)}


def map_xy(lon, lat, x0, y0):
    return (x0 + (lon + 180.0) * MAP_SX, y0 + (MAP_LAT0 - lat) * MAP_SY)


def draw_map(im, d):
    """Peta kiri bawah (CH5: lebih terang + pin warna per region): strip
    header tan + navy + daratan Natural Earth + 13 pin bernomor warna
    region (r=11, angka 13pt) + legenda 2 chip."""
    x1, y1, x2, y2 = MAP_BOX
    ny = y1 + MAP_HEADER_H
    reg_layout(MAP_BOX, "map")
    d.rectangle([x1, y1, x2, y2], fill=(235, 230, 212), outline=NAVY,
                width=1)
    d.rectangle([x1, ny, x2, y2], fill=SEA)
    mtmp = Image.new("RGB", (x2 - x1 - 2, y2 - ny - 2), SEA)
    md = ImageDraw.Draw(mtmp)
    eq_y = int(ny + 1 + 13 + (MAP_LAT0 - 0) * MAP_SY) - (ny + 1)
    for xx in range(0, x2 - x1 - 2, 8):
        md.line([(xx, eq_y), (xx + 4, eq_y)], fill=(110, 140, 170), width=1)
    for poly in LAND_POLYS:
        pts = [(map_xy(lon, lat, x1 + 1 + 42, ny + 1 + 13)[0] - (x1 + 1),
                map_xy(lon, lat, x1 + 1 + 42, ny + 1 + 13)[1] - (ny + 1))
               for lon, lat in poly]
        md.polygon(pts, fill=MAP_LAND, outline=MAP_LAND_OUT)
    im.paste(mtmp, (x1 + 1, ny + 1))
    md = ImageDraw.Draw(im)
    fp = F(SS800, 13)
    placed = []
    offset_used = []
    skipped = []

    def place(px, py):
        for (qx, qy) in placed:
            if ((px - qx) ** 2 + (py - qy) ** 2) ** 0.5 < 25:
                return False
        placed.append((px, py))
        return True

    def place_with_offset(px, py):
        for dx, dy in [(0, 0), (0, 12), (0, -12), (14, 0), (-14, 0),
                       (10, 8), (10, -8), (-10, 8), (-10, -8),
                       (18, 0), (-18, 0), (0, 20), (0, -20),
                       (0, 18), (0, -18),
                       (14, 14), (14, -14), (-14, 14), (-14, -14),
                       (20, 0), (-20, 0), (24, 0), (-24, 0),
                       (0, 24), (0, -24),
                       (18, 18), (18, -18), (-18, 18), (-18, -18),
                       (26, 0), (-26, 0), (0, 26), (0, -26),
                       (30, 0), (-30, 0), (0, 30), (0, -30)]:
            if place(px + dx, py + dy):
                return (px + dx, py + dy), (dx, dy)
        return None, None

    panels = HEROES + CARDS
    for p in panels:
        city = p["map_city"]
        lon, lat = PLACES[city]
        px, py = map_xy(lon, lat, x1 + 1 + 42, ny + 1 + 13)
        pos, off = place_with_offset(px, py)
        if pos is None:
            skipped.append((city, p["num"], "collision"))
            continue
        if off != (0, 0):
            offset_used.append((p["num"], city, off))
        qx, qy = pos
        assert x1 + 12 <= qx <= x2 - 12 and ny + 12 <= qy <= y2 - 12, (
            f"pin {p['num']} keluar peta")
        pin_color = REGION_COLORS[p["region"]]
        md.ellipse([qx - 11, qy - 11, qx + 11, qy + 11], fill=pin_color,
                   outline=WHITE, width=1)
        mark = str(p["num"])
        md.text((qx, qy), mark, font=fp, fill=WHITE, anchor="mm")
    assert not skipped, f"pin hilang: {skipped}"
    assert len(placed) == 13, f"pin terpasang {len(placed)}, harus 13"
    # Header strip tan: dua teks SATU baseline (ref-7 Kevin 23:14 WIB).
    f_t = F(SS800, 14)
    f_n = F(SS800, 14)
    title = "WHERE IT HAPPENED"
    note = "Pins 1\u201313 (Lead & Feature)"
    hdr_cy = y1 + MAP_HEADER_H // 2
    tb = d.textbbox((x1 + 10, hdr_cy), title, font=f_t, anchor="lm")
    d.text((x1 + 10, hdr_cy), title, font=f_t, fill=NAVY, anchor="lm")
    nb = d.textbbox((x2 - 8, hdr_cy), note, font=f_n, anchor="rm")
    d.text((x2 - 8, hdr_cy), note, font=f_n, fill=NAVY, anchor="rm")
    assert nb[0] - tb[2] >= 6, "teks pins menabrak judul peta"
    assert tb[1] >= y1 + 1 and tb[3] < ny, "judul peta keluar strip"
    assert nb[1] >= y1 + 1 and nb[3] < ny, "teks pins keluar strip"
    assert abs((tb[1] + tb[3]) // 2 - (nb[1] + nb[3]) // 2) <= 1, (
        "judul peta dan teks pins tidak satu baseline")
    # Legenda 2 chip gelap DI DALAM laut, bawah-kiri.
    f_l = F(SS800, 11)
    ly = y2 - 27
    lx = x1 + 8
    for txt in ("1\u20133 Lead", "4\u201313 Feature Stories"):
        tw = d.textlength(txt, font=f_l)
        cw = int(tw) + 28
        d.rounded_rectangle([lx, ly, lx + cw, ly + 20], radius=3,
                            fill=(10, 18, 36))
        d.ellipse([lx + 6, ly + 7, lx + 12, ly + 13], fill=RED)
        d.text((lx + 16, ly + 10), txt, font=f_l, fill=WHITE, anchor="lm")
        lx += cw + 6
    return {"placed": len(placed), "offset_used": offset_used,
            "skipped": skipped}


def draw_briefs(d):
    """CH3: MORE STORIES 2 kolom — chip nomor warna region + kota merah
    tebal + brief 1 baris (fakta/angka kunci) + (Sumber). 11/11 per kolom.
    """
    x1, y1, x2, y2 = BRIEFS_BOX
    reg_layout(BRIEFS_BOX, "briefs")
    tt = TileText("briefs")
    d.rectangle([x1, y1, x2, y2], outline=NAVY, width=1)
    d.rectangle([x1 + 1, y1 + 1, x2 - 1, y2 - 1], fill=NEAR_WHITE)
    tt.text(d, x1 + 8, y1 + 4, "MORE STORIES", F(SS800, 13), INK)
    tt.text(d, x2 - 8, y1 + 4, "14\u201335", F(SS800, 11), RED, anchor="ra")
    d.line([(x1 + 8, y1 + 21), (x2 - 8, y1 + 21)], fill=RED, width=2)
    cw = (x2 - x1 - 16 - 12) // 2
    f_city = F(SS800, 11)
    f_txt = F(SS400, 11)
    f_src = F(SS400, 10)
    f_chip = F(SS800, 10)
    chip_h = 14
    pitch = 14
    per = [11, 11]
    idx = 0
    col_bottoms = []
    for c in range(2):
        cx = x1 + 8 + c * (cw + 12)
        yy = y1 + 23
        for k in range(per[c]):
            n, city, t, src, region = BRIEFS[idx]
            idx += 1
            chip_w = 20
            d.rounded_rectangle([cx, yy, cx + chip_w, yy + chip_h], radius=2,
                                fill=REGION_COLORS[region])
            nb = d.textbbox((cx + chip_w // 2, yy + chip_h // 2), str(n), font=f_chip,
                            anchor="mm")
            d.text((cx + chip_w // 2, yy + chip_h // 2), str(n), font=f_chip,
                   fill=WHITE, anchor="mm")
            tx = cx + chip_w + 4
            city_s = f"{city}: "
            cw_city = d.textlength(city_s, font=f_city)
            d.text((tx, yy), city_s, font=f_city, fill=RED, anchor="la")
            tx += cw_city
            src_s = f" ({src})"
            w_txt = d.textlength(t, font=f_txt)
            w_src = d.textlength(src_s, font=f_src)
            total = (chip_w + 4 + cw_city + w_txt + w_src)
            assert total <= cw, (
                f"brief {n} terlalu lebar 1 baris: {total:.0f}px > "
                f"{cw}px ({city}: {t} ({src}))")
            d.text((tx, yy), t, font=f_txt, fill=INK, anchor="la")
            d.text((tx + w_txt, yy), src_s, font=f_src, fill=GREY,
                   anchor="la")
            tt.add((cx, yy, cx + total, yy + chip_h), f"brief{n}")
            yy += pitch
        col_bottoms.append(yy - 13)
    assert idx == 22, f"briefs terpasang {idx}, harus 22"
    assert max(col_bottoms) - min(col_bottoms) <= 20, (
        f"kolom brief tidak rata: {col_bottoms}")
    assert max(col_bottoms) <= y2 - 8, "briefs meluber ke bawah"
    return {"col_bottoms": [int(b) for b in col_bottoms]}


def draw_footer(d):
    """DATE CHECK GAYA v20 (Keputusan Kevin 22 Nov 05:06 WIB, opsi A):
    chip merah "DATE CHECK" di kiri + kolom kanan berisi daftar
    (2 baris) + brief ringkasan (1 baris), teks tebal navy 12pt.
    "Kayak v20" MENANG atas lantai 16pt untuk kotak ini (v20 sendiri
    pakai 12pt). Kotak + Sources TIDAK digeser: tinta 3 baris terukur
    36px, muat di kotak 50px. TANPA catatan produksi/draf."""
    x1, y1, x2, y2 = DC_BOX
    reg_layout(DC_BOX, "datecheck")
    tt = TileText("footer")
    d.rectangle([x1, y1, x2, y2], outline=RED, width=2)
    d.rectangle([x1 + 2, y1 + 2, x2 - 2, y2 - 2], fill=(250, 235, 230))
    # --- chip merah "DATE CHECK" (ala v20: teks 10pt, chip 22px) ---
    f_chip = F(SS800, 10)
    chip_w = int(d.textlength("DATE CHECK", font=f_chip)) + 16
    chip_h = 22
    cx0 = x1 + 8
    cy0 = y1 + (y2 - y1 - chip_h) // 2
    d.rectangle([cx0, cy0, cx0 + chip_w, cy0 + chip_h], fill=RED)
    tt.text(d, (cx0 + cx0 + chip_w) // 2, (cy0 + cy0 + chip_h) // 2,
            "DATE CHECK", f_chip, WHITE, anchor="mm")
    # --- kolom kanan: daftar (2 baris) + brief (1 baris), navy tebal 12pt ---
    tx0 = cx0 + chip_w + 12
    max_w = x2 - 8 - tx0
    f_t = F(SS800, 12)
    list_lines = wrap(d, DATECHECK_LIST, f_t, max_w)
    brief_lines = wrap(d, DC_BRIEF, f_t, max_w)
    assert len(list_lines) == 2, (
        f"DATE CHECK daftar {len(list_lines)} baris: {list_lines}")
    assert len(brief_lines) == 1, (
        f"DATE CHECK brief {len(brief_lines)} baris: {brief_lines}")
    lines = list_lines + brief_lines
    lh = 12
    bb = d.textbbox((tx0, 0), lines[0], font=f_t, anchor="la")
    ink_top, ink_h = bb[1], bb[3] - bb[1]
    ink_span = (len(lines) - 1) * lh + ink_h
    y = y1 + (y2 - y1 - ink_span) // 2 - ink_top
    for ln in lines:
        tt.text(d, tx0, y, ln, f_t, NAVY)
        y += lh
    assert y - lh + ink_top + ink_h <= y2 - 2, "DATE CHECK meluber"
    tt.text(d, 28, SRC_Y, SOURCES, F(SS400, 9), GREY)
    return {"dc_lines": len(lines), "dc_pt": 12}


def measure(img):
    """Ink % (jarak RGB dari kertas > 40 — panel hampir-putih (251,250,245)
    TIDAK dihitung tinta, tint kalem tetap dihitung) + saturated %
    (S > 0,30). Metode ni20: ink ref-7 = 34,9%."""
    px = list(img.getdata())
    n = len(px)
    ink = sum(1 for r, g, b in px
              if ((r - PAPER[0]) ** 2 + (g - PAPER[1]) ** 2
                  + (b - PAPER[2]) ** 2) ** 0.5 > 40)
    sat = 0
    for r, g, b in px:
        mx, mn = max(r, g, b), min(r, g, b)
        if mx > 0 and (mx - mn) / mx > 0.30:
            sat += 1
    return {"ink_pct": round(100 * ink / n, 1),
            "sat_pct": round(100 * sat / n, 1)}


def build():
    im = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(im)
    # --- warna atas (banner region) + tint ilustrasi ---
    hero_boxes = [(HERO_X[i], HERO_Y, HERO_X[i] + HERO_W, HERO_Y + HERO_H)
                  for i in range(3)]
    card_boxes = []
    for r in range(2):
        for c in range(5):
            card_boxes.append((CARD_X[c], CARD_Y[r], CARD_X[c] + CARD_W,
                               CARD_Y[r] + CARD_H))
    panels = hero_boxes + card_boxes
    regions = [h["region"] for h in HEROES] + [c["region"] for c in CARDS]
    banner_colors = assign_banners(panels, regions)
    tints = assign_tints(panels)
    # --- render gambar panel (banner + ilustrasi + chip sumber) ---
    hero_imgs = []
    for i, h in enumerate(HEROES):
        illo = HERO_PAINTERS[h["painter"]](HERO_W - 2, HERO_IMG_H
                                           - HERO_BANNER_H)
        hero_imgs.append(make_panel_img(
            illo, banner_colors[i], h["banner"], h["source"],
            HERO_BANNER_H, source_left=True))
    card_imgs = []
    for i, c in enumerate(CARDS):
        illo = CARD_PAINTERS[c["painter"]](CARD_W - 2, CARD_IMG_H
                                           - CARD_BANNER_H, tints[3 + i])
        card_imgs.append(make_panel_img(
            illo, banner_colors[3 + i], c["banner"], c["source"],
            CARD_BANNER_H, source_left=False))
    # --- warna atas terukur dari gambar jadi (mode strip atas = banner) ---
    tops = ([top_color(im) for im in hero_imgs]
            + [top_color(im) for im in card_imgs])
    for i, t in enumerate(tops):
        assert t == banner_colors[i], (
            f"warna atas panel {i + 1} bukan banner: {t} vs "
            f"{banner_colors[i]}")
    # --- susun halaman ---
    info = {}
    info["masthead"] = draw_masthead(d)
    draw_strip(d)
    info["region_bar"] = draw_region_bar(d)
    for i, h in enumerate(HEROES):
        info[f"hero{h['num']}"] = draw_hero(im, d, h, HERO_X[i], HERO_Y,
                                             hero_imgs[i])
    for i, c in enumerate(CARDS):
        r, cc = divmod(i, 5)
        info[f"card{c['num']}"] = draw_card(im, d, c, CARD_X[cc],
                                            CARD_Y[r], card_imgs[i])
    info["map"] = draw_map(im, d)
    info["briefs"] = draw_briefs(d)
    info["footer"] = draw_footer(d)
    check_layout("v2")
    info["measure"] = measure(im)
    im.save(OUT, optimize=True)
    size = os.path.getsize(OUT)
    assert size <= 1024 * 1024, f"entry {size} byte > 1 MiB"
    sha = hashlib.sha256(open(OUT, "rb").read()).hexdigest()
    info["size"] = size
    info["sha256"] = sha
    print(json.dumps(info, indent=1, default=str))
    print(f"entry.png: {size} byte, sha256 {sha[:16]}...")
    return info


if __name__ == "__main__":
    build()
