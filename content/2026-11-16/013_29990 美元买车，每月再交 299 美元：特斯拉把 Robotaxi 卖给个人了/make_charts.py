# -*- coding: utf-8 -*-
"""
《29990 美元买车，每月再交 299 美元：特斯拉把 Robotaxi 卖给个人了》配套图表
事实来源：特斯拉 @robotaxi 2026-11-13 订购页（29,990 美元 / 1,000 美元定金 /
299 美元月订阅 / 12 月奥斯汀交付）；马斯克自评合理价约 115 美元/月；
NHTSA 2026-09-04 立案（AQ26002）
风格：克制传媒风，白底、低饱和配色、标题即结论
输出目录 = 脚本所在目录
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.lines import Line2D

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

CAR = 29990
SUB_HIGH = 299
SUB_LOW = 115

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep


def footer(fig, text):
    fig.text(0.045, 0.020, text, fontsize=8.4, color=GRAY, ha="left", va="bottom")


def punchline(fig, text):
    fig.text(0.045, 0.072, text, fontsize=10.4, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


# ---------------------------------------------------------------- 图 1
def fig1():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.080, 0.205, 0.900, 0.570])

    fig.text(0.045, 0.955, "车价一次性，账单是月付的", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.882, "按 299 美元/月计，五年总支出 47,930 美元，比车价高出六成",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    xs = [i for i in range(9)]
    hi = [CAR + SUB_HIGH * 12 * x for x in xs]
    lo = [CAR + SUB_LOW * 12 * x for x in xs]

    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(LIGHT)
    ax.tick_params(colors=DARK, labelsize=10.5, length=0)
    ax.set_axisbelow(True)
    ax.grid(axis="y", color=LIGHT, linewidth=0.8, alpha=0.55)
    ax.set_xlim(-0.25, 8.55)
    ax.set_ylim(0, 64000)
    ax.set_xticks(xs)
    ax.set_xticklabels([str(x) for x in xs])
    ax.set_yticks([0, 20000, 40000, 60000])
    ax.set_yticklabels(["0", "2 万", "4 万", "6 万"])
    ax.set_xlabel("持有年数", fontsize=10.5, color=GRAY, labelpad=8)

    ax.axhline(CAR, color=SLATE, linewidth=1.2, linestyle=(0, (4, 3)), alpha=0.9)
    ax.text(8.50, CAR + 1400, "车价 29,990", fontsize=10, color=SLATE,
            ha="right", va="bottom")

    ax.plot(xs, hi, color=NAVY, linewidth=2.8, solid_capstyle="round", zorder=3)
    ax.plot(xs, lo, color=RED, linewidth=2.4, linestyle=(0, (5, 2.5)),
            solid_capstyle="round", zorder=3)

    ax.scatter([5], [hi[5]], s=90, facecolor=NAVY, edgecolor="white",
               linewidth=1.8, zorder=5)
    ax.annotate("5 年 47,930", xy=(5, hi[5]), xytext=(5.30, 43800),
                fontsize=12, color=NAVY, weight="bold", va="top")
    ax.scatter([8], [hi[8]], s=90, facecolor=NAVY, edgecolor="white",
               linewidth=1.8, zorder=5)
    ax.annotate("8 年 58,694", xy=(8, hi[8]), xytext=(7.95, 61200),
                fontsize=12, color=NAVY, weight="bold", ha="right", va="bottom")
    ax.annotate("8 年 41,030", xy=(8, lo[8]), xytext=(7.95, lo[8] - 2200),
                fontsize=11.5, color=RED, weight="bold", ha="right", va="top")

    handles = [
        Line2D([0], [0], color=NAVY, linewidth=2.8, label="每月 299 美元（现行）"),
        Line2D([0], [0], color=RED, linewidth=2.4, linestyle=(0, (5, 2.5)),
               label="每月 115 美元（马斯克自评合理价）"),
    ]
    ax.legend(handles=handles, loc="upper left", frameon=False, fontsize=10.6,
              bbox_to_anchor=(0.015, 0.985), handlelength=2.6)

    punchline(fig, "3 万美元买的是这台车，299 美元买的是它肯动。")
    footer(fig, "据特斯拉 2026-11-13 订购页价格与马斯克公开表态计算，未计税与保险。")
    fig.savefig(OUT + "图1_累计支出.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.235, 0.930, 0.540])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "八年之后，一台车的钱有一半来自订阅", fontsize=19,
             color=DARK, weight="bold", ha="left", va="top")
    fig.text(0.045, 0.882, "同一台 Cybercab，两种收入的累计口径",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    sub8 = SUB_HIGH * 12 * 8
    total = CAR + sub8
    frac_car = CAR / total

    bar_y, bar_h = 0.42, 0.235
    x0, x1 = 0.010, 0.990
    w_car = (x1 - x0) * frac_car

    ax.add_patch(Rectangle((x0, bar_y), w_car, bar_h, facecolor=NAVY, edgecolor="none"))
    ax.add_patch(Rectangle((x0 + w_car, bar_y), (x1 - x0) - w_car, bar_h,
                           facecolor=RED, edgecolor="none", alpha=0.85))

    ax.text(x0 + 0.012, bar_y + bar_h / 2, "车价 29,990", fontsize=13.5, color="white",
            weight="bold", va="center")
    ax.text(x0 + w_car + 0.012, bar_y + bar_h / 2, "订阅 28,704", fontsize=13.5,
            color="white", weight="bold", va="center")

    ax.text(x0 + w_car / 2, bar_y + bar_h + 0.055, f"{frac_car*100:.0f}%", fontsize=15,
            color=NAVY, weight="bold", ha="center", va="bottom")
    ax.text(x0 + w_car + ((x1 - x0) - w_car) / 2, bar_y + bar_h + 0.055,
            f"{(1-frac_car)*100:.0f}%", fontsize=15, color=RED, weight="bold",
            ha="center", va="bottom")
    ax.text(x0, bar_y + bar_h + 0.128, "八年累计收入构成（美元）", fontsize=10.6,
            color=GRAY, ha="left", va="bottom")

    notes = [
        ("订阅费", "299 美元/月 × 12 = 3,588 美元/年"),
        ("占车价", "每年 12%，五年 60%，八年 96%"),
        ("停缴", "车辆无法运行，可被远程停用"),
    ]
    for i, (k, v) in enumerate(notes):
        y = 0.245 - i * 0.075
        ax.text(0.012, y, k, fontsize=10.4, color=GRAY, va="center")
        ax.text(0.075, y, v, fontsize=10.8, color=DARK, va="center")

    punchline(fig, "卖车是一次性收入，订阅是终身年费——这才是 299 真正的意思。")
    footer(fig, "价格据特斯拉 2026-11-13 订购页；比例为本文按 299 美元/月、八年持有计算，未计税与保险。")
    fig.savefig(OUT + "图2_订阅占比.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.150, 0.930, 0.680])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "车卖给了个人，控制权没卖", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.882, "同一台车，卖给车队和卖给个人，账不一样",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    ax.text(0.230, 0.810, "此前：卖给车队", fontsize=11.5, color=SLATE,
            weight="bold", ha="center")
    ax.text(0.620, 0.810, "现在：卖给个人", fontsize=11.5, color=NAVY,
            weight="bold", ha="center")
    ax.plot([0.010, 0.990], [0.770, 0.770], color=LIGHT, linewidth=1.2)

    rows = [
        ("谁付钱", "运营商 / 车队", "车主自己（+1,000 定金）", "变了", RED),
        ("谁扛停运损失", "车队运营方", "车主", "变了", RED),
        ("行驶范围谁定", "特斯拉", "特斯拉", "没变", SLATE),
        ("能不能远程停用", "能", "能", "没变", SLATE),
    ]

    for i, (label, left, right, tag, tagcolor) in enumerate(rows):
        y = 0.640 - i * 0.145
        if i % 2 == 0:
            ax.add_patch(Rectangle((0.010, y - 0.055), 0.980, 0.118,
                                   facecolor=PALE, edgecolor="none"))
        ax.text(0.025, y, label, fontsize=10.8, color=GRAY, va="center")
        ax.text(0.230, y, left, fontsize=11.5, color=DARK, va="center", ha="center")
        ax.text(0.425, y, "→", fontsize=13, color=LIGHT, va="center", ha="center")
        ax.text(0.620, y, right, fontsize=11.5, color=DARK, va="center", ha="center")
        ax.text(0.905, y, tag, fontsize=10.5, color=tagcolor, weight="bold",
                ha="center", va="center",
                bbox=dict(boxstyle="round,pad=0.35", facecolor="white",
                          edgecolor=tagcolor, linewidth=1.0))

    ax.text(0.010, 0.105, "产权让渡了，路权没有。这笔交易真正卖出的，是一份许可。",
            fontsize=10.8, color=DARK, ha="left", va="center")

    footer(fig, "据特斯拉 2026-11-13 订购页与订单条款、Business Insider 所见条款、NHTSA 2026-09-04 立案文件。")
    fig.savefig(OUT + "图3_两套账.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")
