"""Build entry.png for the news-image-20261119 bounty (zech entry).

A poster titled "the world in four frames": a date banner on top and four
equal panels below, one verified news story per panel. All artwork is drawn
with Pillow primitives -- no external images, no network access.

Run:  python3 generate.py
Out:  entry.png  (1024x1024, PNG)
"""

import math
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W, H = 1024, 1024
BANNER_H = 168
PANEL_W, PANEL_H = W // 2, (H - BANNER_H) // 2

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_centered(draw, cx, y, lines, fnt, fill, spacing=4):
    for line in lines:
        w = draw.textlength(line, font=fnt)
        draw.text((cx - w / 2, y), line, font=fnt, fill=fill)
        y += fnt.size + spacing
    return y


def panel_skyline(draw, x0, y0, pw, ph):
    """Neon city skyline with a setting sun (GTA VI / Vice City)."""
    draw.rectangle([x0, y0, x0 + pw, y0 + ph], fill=(24, 8, 48))
    draw.ellipse([x0 + pw - 150, y0 + 18, x0 + pw - 30, y0 + 138],
                 fill=(255, 90, 160))
    heights = [150, 210, 120, 240, 170, 260, 140, 200]
    bw = pw // len(heights)
    for i, hh in enumerate(heights):
        bx = x0 + i * bw + 6
        top = y0 + ph - hh
        draw.rectangle([bx, top, bx + bw - 12, y0 + ph], fill=(58, 20, 92))
        for wy in range(top + 18, y0 + ph - 14, 26):
            draw.rectangle([bx + 8, wy, bx + bw - 20, wy + 10],
                           fill=(255, 214, 90))
    draw.rectangle([x0, y0 + ph - 8, x0 + pw, y0 + ph], fill=(255, 90, 160))


def panel_space(draw, x0, y0, pw, ph):
    """Voyager 1: stars, a dish antenna and a signal arc."""
    draw.rectangle([x0, y0, x0 + pw, y0 + ph], fill=(4, 12, 40))
    stars = [(30, 30), (90, 90), (170, 40), (250, 110), (330, 50),
             (410, 130), (60, 170), (460, 60), (300, 180), (140, 130)]
    for sx, sy in stars:
        draw.ellipse([x0 + sx - 3, y0 + sy - 3, x0 + sx + 3, y0 + sy + 3],
                     fill=(255, 255, 255))
    cx, cy = x0 + pw // 2, y0 + ph - 120
    draw.line([cx - 90, cy + 70, cx - 20, cy - 20], fill=(180, 200, 255), width=6)
    draw.line([cx - 20, cy - 20, cx + 60, cy - 60], fill=(180, 200, 255), width=6)
    draw.arc([cx - 110, cy - 130, cx + 10, cy - 10], 200, 340,
             fill=(120, 220, 255), width=7)
    draw.ellipse([cx - 26, cy - 66, cx + 6, cy - 34], fill=(255, 214, 90))
    for r in (150, 190):
        draw.arc([cx - r, cy - r, cx + r, cy + r], 300, 360,
                 fill=(120, 220, 255), width=3)


def panel_painting(draw, x0, y0, pw, ph):
    """Van Gogh: a swirling golden sky over a dark field."""
    draw.rectangle([x0, y0, x0 + pw, y0 + ph], fill=(255, 176, 32))
    for i in range(5):
        yy = y0 + 30 + i * 34
        draw.arc([x0 + 20, yy, x0 + pw - 20, yy + 60], 180, 360,
                 fill=(196, 110, 0), width=6)
    draw.ellipse([x0 + pw - 140, y0 + 16, x0 + pw - 40, y0 + 116],
                 fill=(255, 240, 150))
    draw.rectangle([x0, y0 + ph - 110, x0 + pw, y0 + ph], fill=(26, 60, 20))
    for i in range(7):
        fx = x0 + 30 + i * 66
        draw.line([fx, y0 + ph - 110, fx, y0 + ph - 30], fill=(60, 140, 50),
                  width=5)
        draw.ellipse([fx - 14, y0 + ph - 128, fx + 14, y0 + ph - 100],
                     fill=(255, 220, 60))
    draw.rectangle([x0 + 150, y0 + ph - 190, x0 + 362, y0 + ph - 110],
                   outline=(90, 40, 0), width=6)
    # Mini "starry night" canvas inside the frame: dark sky, yellow swirls.
    draw.rectangle([x0 + 162, y0 + ph - 178, x0 + 350, y0 + ph - 122],
                   fill=(16, 24, 72))
    for i, yy in enumerate((y0 + ph - 168, y0 + ph - 152, y0 + ph - 136)):
        draw.arc([x0 + 180 + i * 8, yy, x0 + 330 - i * 8, yy + 26], 180, 360,
                 fill=(255, 214, 90), width=4)
    for sx, sy in [(200, y0 + ph - 172), (300, y0 + ph - 160),
                   (250, y0 + ph - 140), (330, y0 + ph - 170)]:
        draw.ellipse([sx - 3, sy - 3, sx + 3, sy + 3], fill=(255, 240, 150))
    draw.ellipse([x0 + 306, y0 + ph - 168, x0 + 330, y0 + ph - 144],
                 fill=(255, 240, 150))


def panel_storm(draw, x0, y0, pw, ph):
    """Cyclone Akvan: spiral bands over a teal sea."""
    draw.rectangle([x0, y0, x0 + pw, y0 + ph], fill=(0, 74, 96))
    cx, cy = x0 + pw // 2, y0 + 118
    for k, (r, col) in enumerate([(120, (255, 255, 255)),
                                  (96, (140, 230, 255)),
                                  (72, (255, 255, 255)),
                                  (48, (140, 230, 255))]):
        draw.arc([cx - r, cy - r, cx + r, cy + r], 20 + k * 40, 300 + k * 40,
                 fill=col, width=10)
    draw.ellipse([cx - 22, cy - 22, cx + 22, cy + 22], fill=(255, 214, 90))
    draw.rectangle([x0, y0 + ph - 92, x0 + pw, y0 + ph], fill=(0, 40, 60))
    for i in range(4):
        wx = x0 + 40 + i * 120
        draw.arc([wx, y0 + ph - 88, wx + 90, y0 + ph - 28], 180, 360,
                 fill=(120, 220, 255), width=5)


PANELS = [
    ("GTA VI IS OUT",
     "Gamers return to Vice City after a 13-year wait as the global rollout begins.",
     panel_skyline, (255, 255, 255)),
    ("VOYAGER 1: ONE LIGHT-DAY",
     "NASA's probe reaches one light-day from Earth, 50 years after launch.",
     panel_space, (255, 255, 255)),
    ("VAN GOGH SELLS FOR $190.4M",
     "A record sale follows a historic Nazi-era dispute.",
     panel_painting, (40, 20, 0)),
    ("CYCLONE AKVAN STRENGTHENS",
     "The Bay of Bengal storm is expected to make landfall on 20 Nov on the Andhra Pradesh coast.",
     panel_storm, (255, 255, 255)),
]


def main():
    img = Image.new("RGB", (W, H), (10, 10, 26))
    draw = ImageDraw.Draw(img)

    # Banner: date in large type, subtitle below.
    draw.rectangle([0, 0, W, BANNER_H], fill=(10, 10, 26))
    draw.rectangle([0, BANNER_H - 8, W, BANNER_H], fill=(255, 214, 90))
    title_f = font(BOLD, 78)
    sub_f = font(BOLD, 30)
    draw_centered(draw, W // 2, 22, ["19 NOVEMBER 2026"], title_f,
                  (255, 255, 255))
    draw_centered(draw, W // 2, 112, ["THE WORLD IN FOUR FRAMES"], sub_f,
                  (255, 214, 90))

    title_f2 = font(BOLD, 30)
    body_f = font(REG, 24)
    for idx, (title, fact, artist, ink) in enumerate(PANELS):
        col, row = idx % 2, idx // 2
        x0 = col * PANEL_W
        y0 = BANNER_H + row * PANEL_H
        artist(draw, x0, y0, PANEL_W, 250)
        # Text block on a solid band under the illustration.
        draw.rectangle([x0, y0 + 250, x0 + PANEL_W, y0 + PANEL_H],
                       fill=(255, 255, 255))
        draw.rectangle([x0, y0 + 250, x0 + PANEL_W, y0 + 258],
                       fill=(255, 214, 90))
        tlines = wrap(draw, title, title_f2, PANEL_W - 32)
        y = y0 + 268
        for line in tlines:
            w = draw.textlength(line, font=title_f2)
            draw.text((x0 + (PANEL_W - w) / 2, y), line, font=title_f2,
                      fill=(10, 10, 26))
            y += 36
        blines = wrap(draw, fact, body_f, PANEL_W - 40)
        for line in blines:
            w = draw.textlength(line, font=body_f)
            draw.text((x0 + (PANEL_W - w) / 2, y), line, font=body_f,
                      fill=(40, 40, 40))
            y += 30

    # Panel dividers.
    draw.line([W // 2, BANNER_H, W // 2, H], fill=(255, 214, 90), width=6)
    draw.line([0, BANNER_H + PANEL_H, W, BANNER_H + PANEL_H],
              fill=(255, 214, 90), width=6)

    img.save(OUT, format="PNG", optimize=True)
    print(f"wrote {OUT} ({os.path.getsize(OUT)} bytes)")


if __name__ == "__main__":
    main()
