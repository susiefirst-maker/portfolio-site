from __future__ import annotations

from pathlib import Path
from textwrap import wrap

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "screenshots"

FONT_ROOT = Path("/System/Library/Fonts/Supplemental")
SERIF = FONT_ROOT / "Georgia.ttf"
SERIF_BOLD = FONT_ROOT / "Georgia Bold.ttf"
SANS = FONT_ROOT / "Arial.ttf"
SANS_BOLD = FONT_ROOT / "Arial Bold.ttf"


def font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(path), size)


TITLE = font(SERIF_BOLD, 66)
H2 = font(SERIF_BOLD, 31)
H3 = font(SANS_BOLD, 24)
BODY = font(SANS, 22)
BODY_SMALL = font(SANS, 18)
BODY_BOLD = font(SANS_BOLD, 22)
LABEL = font(SANS, 16)
LABEL_BOLD = font(SANS_BOLD, 16)
METRIC = font(SERIF_BOLD, 46)


def rounded(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], fill: str, outline: str | None = None, radius: int = 28) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=1 if outline else 0)


def write_wrapped(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    width: int,
    *,
    fill: str = "#394256",
    font_obj: ImageFont.FreeTypeFont = BODY,
    line_gap: int = 9,
    max_lines: int | None = None,
) -> int:
    x, y = xy
    avg_char = max(font_obj.getlength("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz") / 52, 8)
    chars = max(18, int(width / avg_char))
    lines = wrap(text, chars)
    if max_lines is not None:
        lines = lines[:max_lines]
    for line in lines:
        draw.text((x, y), line, font=font_obj, fill=fill)
        y += font_obj.size + line_gap
    return y


def card(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], label: str, value: str, caption: str) -> None:
    rounded(draw, box, "#ffffff", "#e4ded4", 30)
    x1, y1, _, _ = box
    draw.text((x1 + 28, y1 + 25), label.upper(), font=LABEL_BOLD, fill="#6e7788")
    draw.text((x1 + 28, y1 + 56), value, font=METRIC, fill="#1b2130")
    write_wrapped(
        draw,
        (x1 + 28, y1 + 119),
        caption,
        box[2] - box[0] - 56,
        fill="#596475",
        font_obj=BODY_SMALL,
        line_gap=5,
        max_lines=3,
    )


def draw_table(
    draw: ImageDraw.ImageDraw,
    origin: tuple[int, int],
    headers: list[str],
    rows: list[list[str]],
    widths: list[int],
) -> None:
    x, y = origin
    row_h = 48
    draw.rectangle((x, y, x + sum(widths), y + row_h), fill="#f4efe7")
    cursor = x
    for header, width in zip(headers, widths):
        draw.text((cursor + 14, y + 15), header.upper(), font=LABEL_BOLD, fill="#596475")
        cursor += width
    y += row_h
    for index, row in enumerate(rows):
        draw.rectangle((x, y, x + sum(widths), y + row_h), fill="#ffffff" if index % 2 == 0 else "#fbf8f3")
        cursor = x
        for value, width in zip(row, widths):
            draw.text((cursor + 14, y + 13), value, font=BODY_SMALL, fill="#1f2633")
            cursor += width
        y += row_h


def render_struct() -> None:
    img = Image.new("RGB", (1440, 1100), "#f7f2ea")
    draw = ImageDraw.Draw(img)
    draw.ellipse((-180, -220, 420, 360), fill="#efe1d2")
    draw.ellipse((1050, -160, 1640, 380), fill="#dce8e4")

    rounded(draw, (86, 66, 1354, 238), "#ffffffcc", "#e5ddd2", 34)
    draw.text((116, 96), "struct-devpred benchmark", font=TITLE, fill="#1c2433")
    write_wrapped(
        draw,
        (120, 176),
        "Leakage-resistant antibody developability ablations across descriptor families, model classes, six Jain-2017 endpoints, and bootstrap confidence intervals.",
        1080,
        fill="#4f5c70",
        font_obj=BODY,
    )

    card(draw, (86, 274, 392, 470), "Best endpoint rho", "+0.41", "HIC retention time with physicochemical descriptors.")
    card(draw, (420, 274, 726, 470), "Best family mean rho", "+0.333", "hybrid_seq_struct ranks first across all endpoints.")
    card(draw, (754, 274, 1060, 470), "CV design", "5-fold", "GroupKFold blocks V-gene x CDR-H3 leakage.")
    card(draw, (1088, 274, 1354, 470), "Study size", "137", "Jain antibodies with six biophysical labels.")

    rounded(draw, (86, 512, 760, 1018), "#ffffff", "#e4ded4", 30)
    draw.text((116, 544), "Best descriptor x model per endpoint", font=H2, fill="#1c2433")
    draw_table(
        draw,
        (116, 602),
        ["Endpoint", "Descriptor", "Model", "rho"],
        [
            ["hic_rt", "physicochem", "RF", "+0.41"],
            ["expression", "hybrid_seq_struct", "ridge", "+0.36"],
            ["tm_onset_c", "aggregation", "RF", "+0.35"],
            ["psr_score", "hybrid_seq_struct", "ridge", "+0.35"],
            ["ac_sins", "hybrid_seq_struct", "GB", "+0.34"],
            ["bvp_score", "composition", "GB", "+0.32"],
        ],
        [158, 250, 120, 90],
    )

    rounded(draw, (792, 512, 1354, 1018), "#ffffff", "#e4ded4", 30)
    draw.text((824, 544), "Descriptor ranking", font=H2, fill="#1c2433")
    bars = [
        ("hybrid_seq_struct", 0.333, "#1b6d85"),
        ("composition", 0.301, "#3b8f6f"),
        ("hybrid_all", 0.262, "#7a9474"),
        ("esm2_t12", 0.245, "#b18b5c"),
        ("structure_informed", 0.245, "#b18b5c"),
        ("physicochem", 0.236, "#c07d62"),
    ]
    max_value = 0.36
    y = 614
    for name, value, color in bars:
        draw.text((824, y), name, font=BODY_BOLD, fill="#1f2633")
        bar_x = 824
        bar_y = y + 32
        bar_w = int(430 * value / max_value)
        rounded(draw, (bar_x, bar_y, bar_x + 430, bar_y + 23), "#eee7dd", None, 12)
        rounded(draw, (bar_x, bar_y, bar_x + bar_w, bar_y + 23), color, None, 12)
        draw.text((1270, y + 24), f"{value:+.3f}", font=BODY_SMALL, fill="#394256")
        y += 66

    path = OUT / "struct-devpred" / "benchmark_overview.png"
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path)


def render_bo() -> None:
    img = Image.new("RGB", (1440, 1100), "#f8f3e9")
    draw = ImageDraw.Draw(img)
    draw.ellipse((-210, -230, 520, 430), fill="#efe1d0")
    draw.ellipse((1040, -210, 1630, 420), fill="#dde9df")

    rounded(draw, (86, 66, 1354, 238), "#ffffffcc", "#e5ddd2", 34)
    draw.text((116, 96), "bo-protein-dms", font=TITLE, fill="#1c2433")
    write_wrapped(
        draw,
        (120, 176),
        "Retrospective Bayesian optimization benchmark on a GB1-like 160,000-variant protein fitness landscape with discrete, sequence-aware strategies.",
        1100,
        fill="#4f5c70",
        font_obj=BODY,
    )

    card(draw, (86, 274, 392, 470), "Budget", "96", "Queries per campaign: one 96-well plate.")
    card(draw, (420, 274, 726, 470), "Seeds", "20", "Repeated campaigns with bootstrap CIs.")
    card(draw, (754, 274, 1060, 470), "Best active", "5.99", "Active strategies reach the global optimum.")
    card(draw, (1088, 274, 1354, 470), "Random", "2.57", "Random search stalls below the optimum.")

    rounded(draw, (86, 512, 884, 1018), "#ffffff", "#e4ded4", 30)
    draw.text((116, 544), "Best-so-far convergence", font=H2, fill="#1c2433")
    plot_path = OUT / "bo-protein-dms" / "synthetic_best_so_far.png"
    plot = Image.open(plot_path).convert("RGB")
    plot.thumbnail((724, 410), Image.Resampling.LANCZOS)
    px = 122
    py = 608
    rounded(draw, (px - 10, py - 10, px + plot.width + 10, py + plot.height + 10), "#fbfaf7", "#eee6dc", 18)
    img.paste(plot, (px, py))

    rounded(draw, (916, 512, 1354, 1018), "#ffffff", "#e4ded4", 30)
    draw.text((948, 544), "Convergence summary", font=H2, fill="#1c2433")
    draw_table(
        draw,
        (948, 606),
        ["Strategy", "90% max", "Final"],
        [
            ["turbo_lite", "31 rounds", "5.99"],
            ["gp_hamming", "32 rounds", "5.99"],
            ["ridge", "49 rounds", "5.99"],
            ["random", "never", "2.57"],
        ],
        [170, 128, 92],
    )
    write_wrapped(
        draw,
        (948, 842),
        "Takeaway: the corrected discrete BO design dominates random search with non-overlapping confidence intervals, avoiding high-dimensional qNEHVI failure modes.",
        360,
        fill="#596475",
        font_obj=BODY_SMALL,
        line_gap=7,
    )

    path = OUT / "bo-protein-dms" / "benchmark_overview.png"
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path)


def main() -> None:
    render_struct()
    render_bo()


if __name__ == "__main__":
    main()
