# -*- coding: utf-8 -*-
"""
《胖东来今年 258 亿：一天卖 8709 万，310 台越野车只值一天半》配套图表
事实来源：于东来 2026-11-16 发布"集团销售仪表盘"：截至 11/15 累计 258.42 亿
（+26.34%）、11 月单月 11.23 亿（+25.56%）、11/15 单日 8709 万（+18.95%）；
2025 年全年 235.31 亿元；2024 年近 170 亿元；门店梯队；310 辆坦克 700、
2026 款指导价 42.8 万—50.8 万元
风格：克制传媒风，白底、低饱和配色、标题即结论
输出目录 = 脚本所在目录
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["figure.facecolor"] = "white"
plt.rcParams["axes.facecolor"] = "white"

NAVY = "#1f3a5f"
RED = "#b5544a"
GRAY = "#8a8f98"
SLATE = "#5f6673"
LIGHT = "#d8dbe0"
DARK = "#2b2f36"
PALE = "#eef0f3"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep


def footer(fig, text):
    fig.text(0.045, 0.020, text, fontsize=8.4, color=GRAY, ha="left", va="bottom")


def punchline(fig, text):
    fig.text(0.045, 0.072, text, fontsize=10.4, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


def bare(ax, axis="y"):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(LIGHT)
    ax.tick_params(colors=DARK, labelsize=10.5, length=0)
    ax.set_axisbelow(True)
    ax.grid(axis=axis, color=LIGHT, linewidth=0.8, alpha=0.55)


# ---------------------------------------------------------------- 图 1
def fig1():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.080, 0.210, 0.890, 0.550])

    fig.text(0.045, 0.955, "三年：从 170 亿到 258 亿", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.882, "集团销售额（亿元）。2026 年为截至 11 月 15 日的数据，非全年",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    bare(ax)
    labels = ["2024 年\n全年", "2025 年\n全年", "2026 年\n至 11 月 15 日"]
    vals = [170, 235.31, 258.42]
    cols = [GRAY, SLATE, NAVY]

    ax.bar([0, 1, 2], vals, width=0.48, color=cols, edgecolor="none")

    for x, v, c in zip([0, 1, 2], vals, cols):
        ax.text(x, v + 5.5, f"{v:g}", fontsize=14, color=DARK, ha="center",
                va="bottom", weight="bold")

    ax.annotate("同比 +26.34%", xy=(2, 258.42), xytext=(2.42, 258.42),
                fontsize=11, color=RED, weight="bold", va="center", ha="left")

    ax.set_ylim(0, 320)
    ax.set_xlim(-0.62, 2.62)
    ax.set_xticks([0, 1, 2])
    ax.set_xticklabels(labels, fontsize=11, linespacing=1.7)
    ax.set_yticks([0, 100, 200, 300])
    ax.set_yticklabels(["0", "100", "200", "300"])

    punchline(fig, "十个月半，超过去年一整年。")
    footer(fig, "据于东来 2026-11-16 公布的集团销售仪表盘、2025 年全年 235.31 亿元及此前披露的 2024 年近 170 亿元。")
    fig.savefig(OUT + "图1_三年规模.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.205, 0.205, 0.745, 0.550])

    fig.text(0.045, 0.955, "门店梯队：前三家占集团近一半", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.882, "2026 年累计销售额（亿元），截至 11 月 15 日",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    bare(ax, axis="x")
    rows = [
        ("时代广场店", 57.84, NAVY),
        ("天使城店", 32.71, NAVY),
        ("三胖店", 30.54, NAVY),
        ("生活广场店", 17.54, RED),
    ]
    ys = [3, 2, 1, 0]

    for y, (name, val, color) in zip(ys, rows):
        ax.barh([y], [val], height=0.46, color=color, edgecolor="none")
        ax.text(val + 1.0, y, f"{val:g}", fontsize=12.5, color=DARK,
                va="center", ha="left", weight="bold")

    ax.text(17.54, -0.42, "年底关闭", fontsize=9.6, color=RED, ha="center",
            va="center")

    ax.set_yticks(ys)
    ax.set_yticklabels([r[0] for r in rows], fontsize=11.5)
    ax.set_xlim(0, 70)
    ax.set_ylim(-0.70, 3.60)
    ax.set_xticks([0, 20, 40, 60])
    ax.tick_params(axis="x", pad=8)

    ax.text(0, 3.42, "前三合计 121 亿元，约占集团 258.42 亿元的 47%",
            fontsize=10.4, color=GRAY, va="center")

    punchline(fig, "单店效率极高，但增长被 13 处物业卡着。")
    footer(fig, "据于东来 2026-11-16 公布的门店销售榜（北京商报、新京报报道）；生活广场店 2026 年 12 月关闭。")
    fig.savefig(OUT + "图2_门店梯队.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.105, 0.215, 0.860, 0.540])

    fig.text(0.045, 0.955, "310 台车的账：约一天半流水", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.882, "单位：亿元。左侧为单日销售额，右侧为 310 辆坦克 700 采购额",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    bare(ax)
    labels = ["11 月 15 日\n单日销售额", "310 辆坦克 700\n按入门价 42.8 万计"]
    vals = [0.8709, 1.3004]
    cols = [NAVY, RED]

    ax.bar([0, 1], vals, width=0.44, color=cols, edgecolor="none")
    ax.text(0, 0.8709 + 0.028, "0.87", fontsize=14, color=DARK, ha="center",
            va="bottom", weight="bold")
    ax.text(1, 1.3004 + 0.028, "1.30", fontsize=14, color=DARK, ha="center",
            va="bottom", weight="bold")

    ax.annotate("", xy=(1.24, 1.3004), xytext=(1.24, 0.8709),
                arrowprops=dict(arrowstyle="<|-|>", color=RED, linewidth=1.5))
    ax.text(1.30, 1.086, "≈ 1.5 天", fontsize=12.5, color=RED, weight="bold",
            va="center", ha="left")

    ax.set_ylim(0, 1.72)
    ax.set_xlim(-0.62, 1.86)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(labels, fontsize=11, linespacing=1.7)
    ax.set_yticks([0, 0.5, 1.0, 1.5])
    ax.set_yticklabels(["0", "0.5", "1.0", "1.5"])

    fig.text(0.048, 0.822,
             "今年第三次批量订购同款：4 月 20 台、4 月下旬追加 100 台、这次 310 台",
             fontsize=9.8, color=GRAY, ha="left", va="center")

    punchline(fig, "一天半的流水，换成 310 台硬派越野。")
    footer(fig, "据于东来 2026-11-16 公告、凤凰网与快科技报道（2026 款坦克 700 指导价 42.8 万—50.8 万元，采购额为按入门价估算）。")
    fig.savefig(OUT + "图3_车的账.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")