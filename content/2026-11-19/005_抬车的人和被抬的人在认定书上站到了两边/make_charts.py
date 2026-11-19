# -*- coding: utf-8 -*-
"""
《抬车的人和被抬的人，在认定书上站到了两边》配套图表
事实口径（2026-11-18 柳州官塘大桥）：
  · 11 月 18 日 8 时 40 分许，柳州官塘大桥早高峰，一辆新能源车与一辆
    二轮电动车碰撞，电动车驾驶人李某被卷入车底；
  · 过往七八名市民自发上前，合力抬起车辆，为伤者腾出救援空间；
  · 随后民辅警到场处置，伤者已得到妥善救治；
  · 交警初步调查认定：李某违反通行规定进入机动车道，承担主要责任；
    小车驾驶人陈某未确保通行安全，承担次要责任；
  · 交警提醒：非机动车禁止进入禁行区域，驾驶电动车应佩戴安全头盔。
风格：克制传媒风，白底、低饱和配色、标题即结论。输出目录 = 脚本所在目录。
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False

NAVY = "#1f3a5f"
RED = "#b5544a"
GRAY = "#8a8f98"
SLATE = "#5f6673"
LIGHT = "#d8dbe0"
DARK = "#2b2f36"
PALE = "#eef0f3"
SAND = "#f7f3ea"
GREEN = "#4f6b58"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep


def base(title, sub):
    fig = plt.figure(figsize=(12, 6.8))
    fig.patch.set_facecolor("white")
    fig.text(0.045, 0.950, title, fontsize=20, color=DARK, weight="bold",
             ha="left", va="top")
    fig.text(0.045, 0.878, sub, fontsize=10.8, color=GRAY, ha="left", va="top")
    return fig


def footer(fig, text):
    fig.text(0.045, 0.014, text, fontsize=8.2, color=GRAY, ha="left", va="center")


def punchline(fig, text, y=0.078):
    fig.text(0.045, y, text, fontsize=10.8, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.6", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


# ------------------------------------------------------------------ 图 1
def fig1():
    fig = base("那天早上，桥上发生了什么",
               "柳州官塘大桥 · 2026 年 11 月 18 日 8 时 40 分许 · 早高峰")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    items = [
        ("8 时 40 分许", "碰撞发生", "一辆新能源车与一辆二轮电动车\n在早高峰的桥面相撞"),
        ("紧接着", "人被卷进车底", "电动车驾驶人李某被卷入车底"),
        ("随即", "七八名路人停下", "过往市民自发上前，合力抬起车辆，\n为伤者腾出救援空间"),
        ("随后", "民辅警到场", "民警、辅警到场处置"),
        ("结果", "伤者已妥善救治", "报道未提及抬车者的姓名"),
    ]

    ax.plot([0.115, 0.115], [0.180, 0.830], color=LIGHT, linewidth=1.4)
    yy = 0.800
    for time, head, body in items:
        ax.plot([0.115], [yy], marker="o", markersize=7.0,
                color=RED if time in ("随即", "结果") else NAVY, zorder=3)
        ax.text(0.055, yy, time, fontsize=9.2, color=GRAY, weight="bold",
                ha="right", va="center")
        ax.text(0.155, yy, head, fontsize=10.6, color=DARK, weight="bold",
                ha="left", va="center")
        ax.text(0.420, yy, body, fontsize=8.8, color=SLATE, ha="left",
                va="center", linespacing=1.7)
        yy -= 0.160

    punchline(fig, "从碰撞到有人抬车，中间只隔了路人抬头的几秒。")
    footer(fig, "事实：过程与时间据 2026-11-18 柳州交警通报及媒体报道｜制图：本文")
    fig.savefig(OUT + "图1_那天早上桥上发生了什么.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("认定书上，被救的人是主责",
               "交警初步调查认定：一个主责，一个次责")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    cards = [
        ("李某 · 电动车驾驶人", "主要责任", RED,
         ["违反通行规定进入机动车道", "当时被卷入车底、被路人抬出"]),
        ("陈某 · 小车驾驶人", "次要责任", SLATE,
         ["未确保通行安全", "当时在车内"]),
    ]

    xs = [0.018, 0.532]
    for i, (name, duty, color, rows) in enumerate(cards):
        face = "#fbf3f1" if i == 0 else "#fafbfc"
        ax.add_patch(FancyBboxPatch((xs[i], 0.320), 0.450, 0.560,
                                    boxstyle="round,pad=0.012",
                                    facecolor=face, edgecolor=LIGHT,
                                    linewidth=1.0))
        ax.text(xs[i] + 0.028, 0.820, name, fontsize=10.4, color=NAVY,
                weight="bold", ha="left", va="center")
        ax.text(xs[i] + 0.028, 0.720, duty, fontsize=26.0, color=color,
                weight="bold", ha="left", va="center")
        ax.plot([xs[i] + 0.028, xs[i] + 0.422], [0.660, 0.660],
                color=LIGHT, linewidth=0.9)
        yy = 0.580
        for r in rows:
            ax.plot([xs[i] + 0.034], [yy + 0.006], marker="s", markersize=4.6,
                    color=color, zorder=3)
            ax.text(xs[i] + 0.056, yy, r, fontsize=9.0, color=SLATE,
                    ha="left", va="top", linespacing=1.8)
            yy -= 0.115

    ax.add_patch(FancyBboxPatch((0.018, 0.150), 0.964, 0.130,
                                boxstyle="round,pad=0.010", facecolor=SAND,
                                edgecolor="#d9cdb6", linewidth=1.0))
    ax.text(0.044, 0.215,
            "交警提醒：非机动车禁止进入禁行区域；驾驶电动车应佩戴安全头盔。",
            fontsize=9.8, color="#7a6746", ha="left", va="center")

    punchline(fig, "同一页纸上，救人的和被救的，不在同一边。")
    footer(fig, "事实：责任认定与交警提醒据 2026-11-18 交警初步调查结论｜制图：本文")
    fig.savefig(OUT + "图2_认定书上的主责与次责.png", dpi=150,
                facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("同一件事，两种关系",
               "桥面上，大家在一头；认定书上，两人在两头")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # 上：桥面上
    ax.add_patch(FancyBboxPatch((0.020, 0.505), 0.960, 0.290,
                                boxstyle="round,pad=0.012",
                                facecolor="#fafbfc", edgecolor=LIGHT,
                                linewidth=1.0))
    ax.text(0.048, 0.735, "① 桥面上：多数人站在一边", fontsize=10.4,
            color=NAVY, weight="bold", ha="left", va="center")
    ax.text(0.048, 0.660, "七八名路人", fontsize=15.0, color=GREEN,
            weight="bold", ha="left", va="center")
    ax.text(0.250, 0.660, "+  车底的李某", fontsize=15.0, color=GREEN,
            weight="bold", ha="left", va="center")
    ax.text(0.048, 0.575,
            "抬车这件事，不需要先分清谁对谁错。",
            fontsize=9.2, color=SLATE, ha="left", va="center")

    # 下：认定书上
    ax.add_patch(FancyBboxPatch((0.020, 0.170), 0.960, 0.290,
                                boxstyle="round,pad=0.012",
                                facecolor="#fbf3f1", edgecolor=LIGHT,
                                linewidth=1.0))
    ax.text(0.048, 0.400, "② 认定书上：两个人分到两边", fontsize=10.4,
            color=NAVY, weight="bold", ha="left", va="center")
    ax.text(0.048, 0.320, "李某 · 主要责任", fontsize=15.0, color=RED,
            weight="bold", ha="left", va="center")
    ax.text(0.330, 0.320, "｜", fontsize=15.0, color=GRAY, ha="left",
            va="center")
    ax.text(0.370, 0.320, "陈某 · 次要责任", fontsize=15.0, color=SLATE,
            weight="bold", ha="left", va="center")
    ax.text(0.048, 0.235,
            "定责这件事，只看谁违反了通行规定、谁没确保安全。",
            fontsize=9.2, color=SLATE, ha="left", va="center")

    punchline(fig, "善意和过错，可以同时出现在一个人身上。")
    footer(fig, "事实：两处表述分别来自现场救援报道与交警初步认定｜制图：本文")
    fig.savefig(OUT + "图3_同一件事两种关系.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)