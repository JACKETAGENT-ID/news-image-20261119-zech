# 19 November 2026 — The World in Four Frames

A poster that sums up 19 November 2026 in a single image: a bold date
banner on top, then four equal illustrated panels, one story per panel.

1. **GTA VI is out** — gamers return to Vice City after a 13-year wait as
   the global rollout begins.
2. **Voyager 1: one light-day** — NASA's probe reaches one light-day from
   Earth, 50 years after launch.
3. **Van Gogh sells for $190.4M** — a record sale follows a historic
   Nazi-era dispute.
4. **Cyclone Akvan strengthens** — the Bay of Bengal storm is expected to
   make landfall on 20 Nov on the Andhra Pradesh coast.

Every illustration is drawn in code (Pillow shapes only, no stock photos),
and every fact comes from the verified news list for 19 November 2026.

## How to run

```sh
python3 generate.py   # rebuilds entry.png (1024x1024)
MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.png
```

`main.py` uses only the Python standard library and copies the same
`entry.png` on every run, so repeated runs are byte-identical.
