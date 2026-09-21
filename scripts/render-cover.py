"""Render cover.svg to cover.png for the monthly witness. Zero API spend.
Usage: python scripts/render-cover.py assets/cover-template.svg cristo/2026-09/cover.png
Tries cairosvg, then rsvg-convert, then Pillow fallback with a flat parchment card.
Requires hook text already substituted into the SVG by the visual-builder agent.
"""
import shutil
import subprocess
import sys


def main(src, dst):
    try:
        import cairosvg
        cairosvg.svg2png(url=src, write_to=dst, output_width=1456, output_height=816)
        print(f"rendered with cairosvg: {dst}")
        return
    except Exception as e:
        print(f"cairosvg unavailable ({e}), trying rsvg-convert")
    if shutil.which("rsvg-convert"):
        subprocess.run(["rsvg-convert", "-w", "1456", "-h", "816", "-o", dst, src], check=True)
        print(f"rendered with rsvg-convert: {dst}")
        return
    from PIL import Image, ImageDraw
    img = Image.new("RGB", (1456, 816), (255, 255, 255))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([80, 80, 1376, 736], radius=24, fill=(245, 240, 230), outline=(201, 168, 106))
    d.text((160, 300), "Cristo", fill=(26, 26, 46))
    img.save(dst)
    print(f"rendered fallback flat card (install cairosvg for full SVG): {dst}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
