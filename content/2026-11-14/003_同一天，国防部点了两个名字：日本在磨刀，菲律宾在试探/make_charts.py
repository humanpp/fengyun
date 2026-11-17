# -*- coding: utf-8 -*-
"""
《同一天，国防部点了两个名字》配套图表
数据来源：国防部 2026-11-13 例行发布会实录及公开报道
风格：克制传媒风，白底、低饱和配色、标题即结论
输出目录 = 脚本所在目录
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["figure.facecolor"] = "white"
plt.rcParams["axes.facecolor"] = "white"

NAVY = "#1f3a5f"
RED = "#b5544a"
GRAY = "#8a8f98"
LIGHT = "#d8dbe0"
DARK = "#2b2f36"
PALE = "#eef0f3"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep


def clean(ax, axis="x"):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(LIGHT)
    ax.tick_params(colors=DARK, labelsize=11, length=0)
    ax.set_axisbelow(True)
    ax.grid(axis=axis, color=LIGHT, linewidth=0.8, alpha=0.55)


def footer(fig, text):
    fig.text(0.045, 0.022, text, fontsize=8.4, color=GRAY, ha="left", va="bottom")


# ---------------------------------------------------------------- 图 1
def fig1():
    fig, ax = plt.subplots(figsize=(12, 6.8))
    fig.subplots_adjust(left=0.105, right=0.945, top=0.700, bottom=0.235)

    fig.suptitle("日本的五年军费：争的不是要不要扩，是扩多少",
                 fontsize=19, color=DARK, x=0.045, ha="left", y=0.955, weight="bold")
    fig.text(0.045, 0.885,
             "现行计划 43 万亿日元，防卫省要求 70 至 80 万亿，政府正按 60 万亿左右调整（单位：万亿日元）",
             fontsize=10.6, color=GRAY, ha="left")

    labels = ["现行五年计划\n2023—2027 财年", "新五年·政府\n调整方向", "新五年·防卫省\n要求额"]
    lo = [43, 60, 70]
    hi = [43, 60, 80]
    colors = [LIGHT, NAVY, RED]

    x = np.arange(3)
    for i, (l, h, c) in enumerate(zip(lo, hi, colors)):
        if l == h:
            ax.bar(i, h, width=0.40, color=c)
            ax.text(i, h + 2.0, f"{h}", ha="center", va="bottom",
                    fontsize=16, color=DARK, weight="bold")
        else:
            ax.bar(i, l, width=0.40, color=c, alpha=0.30)
            ax.bar(i, h - l, bottom=l, width=0.40, color=c)
            ax.text(i, h + 2.0, f"{l} – {h}", ha="center", va="bottom",
                    fontsize=16, color=DARK, weight="bold")

    # 基准虚线
    ax.axhline(43, color=GRAY, ls=(0, (5, 4)), lw=1.0, alpha=0.8)
    ax.text(2.42, 43, "现行 43", fontsize=9.5, color=GRAY,
            va="center", ha="right")

    # 增幅标注：放进柱内底部
    ax.text(1, 6, "×1.4", ha="center", va="bottom",
            fontsize=14, color="white", weight="bold")
    ax.text(2, 6, "×1.6–1.9", ha="center", va="bottom",
            fontsize=14, color="white", weight="bold")

    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=10.5, linespacing=1.55)
    ax.set_ylim(0, 102)
    ax.set_ylabel("五年防卫费总额（万亿日元）", fontsize=10.5, color=GRAY, labelpad=8)
    clean(ax, axis="y")

    note = ("防卫省要求额是记者在国防部发布会上引用的数字；政府内部正因\n"
            "“财源难以保证”向 60 万亿左右压缩。最终以年底修订的安保三文件为准。")
    box = dict(boxstyle="round,pad=0.7", facecolor=PALE, edgecolor=LIGHT, linewidth=0.9)
    fig.text(0.045, 0.088, note, fontsize=10, color=DARK, ha="left",
             va="center", linespacing=1.85, bbox=box)

    footer(fig, "数据：日本防卫省、日本《朝日新闻》2026-11-13、产经新闻、路透社；国防部 2026-11-13 例行发布会。")
    fig.savefig(OUT + "图1_日本防卫预算跳升.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig, ax = plt.subplots(figsize=(12, 6.8))
    fig.subplots_adjust(left=0.045, right=0.955, top=0.760, bottom=0.090)

    fig.suptitle("八个字背后，是三层递进",
                 fontsize=19, color=DARK, x=0.045, ha="left", y=0.955, weight="bold")
    fig.text(0.045, 0.888,
             "菲防长以“20 万菲侨”为由谈论台海，国防部逐层回应",
             fontsize=11, color=GRAY, ha="left")

    layers = [
        ("第一层｜讲性质",
         "台湾问题纯属中国内政，如何解决是中国人自己的事，不容他人置喙", NAVY),
        ("第二层｜点个人",
         "菲个别政客言论出于政治偏见和一己私利，背离菲政府在台湾问题上对中方作出的郑重承诺", RED),
        ("第三层｜给态度",
         "中方对此强烈不满，坚决反对。敦促菲方严格约束个别政客的危险言行", DARK),
    ]

    # 在数据坐标系里布局：每行高 1.0，从下往上
    box_h = 0.82
    for i, (title, body, color) in enumerate(layers):
        y = (2 - i) * 1.05
        ax.add_patch(plt.Rectangle((0.015, y - box_h / 2), 0.97, box_h,
                                   facecolor=PALE, edgecolor=LIGHT,
                                   linewidth=1.0, zorder=1))
        ax.add_patch(plt.Rectangle((0.015, y - box_h / 2), 0.006, box_h,
                                   facecolor=color, edgecolor="none", zorder=3))
        ax.text(0.045, y + 0.235, title, fontsize=11.8, color=color,
                weight="bold", va="center", zorder=4)
        ax.text(0.045, y - 0.135, body, fontsize=10.8, color=DARK,
                va="center", zorder=4)

    ax.set_xlim(0, 1)
    ax.set_ylim(-0.62, 2.72)
    ax.axis("off")

    footer(fig, "原文：国防部新闻发言人陈曦大校 2026-11-13 答记者问。菲防长言论见其近日采访。")
    fig.savefig(OUT + "图2_菲律宾回应三个层次.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig, ax = plt.subplots(figsize=(12, 6.8))
    fig.subplots_adjust(left=0.045, right=0.955, top=0.755, bottom=0.095)

    fig.suptitle("同一场发布会，两种应对逻辑",
                 fontsize=19, color=DARK, x=0.045, ha="left", y=0.955, weight="bold")
    fig.text(0.045, 0.888,
             "对日本从历史定性，对菲律宾划边界点人——分量不同的原因是动作性质不同",
             fontsize=10.8, color=GRAY, ha="left")

    # 坐标系：x 0-1，y 0-5
    ax.set_xlim(0, 1)
    ax.set_ylim(-0.35, 5.15)
    ax.axis("off")

    COL_J = 0.34   # 日本列（先讲，放左）
    COL_P = 0.66   # 菲律宾列

    # 表头
    ax.text(COL_J, 4.88, "日本", fontsize=16, color=NAVY, weight="bold", ha="center")
    ax.text(COL_P, 4.88, "菲律宾", fontsize=16, color=RED, weight="bold", ha="center")
    ax.text(COL_J, 4.52, "在动结构", fontsize=11, color=NAVY, ha="center", style="italic")
    ax.text(COL_P, 4.52, "在试水温", fontsize=11, color=RED, ha="center", style="italic")
    ax.plot([0.02, 0.98], [4.26, 4.26], color=DARK, lw=1.3)

    rows = [
        ("突破口", "安保三文件 / 无核三原则例外", "防长言论 / 20 万菲侨"),
        ("动作性质", "改写战后秩序框架，不可逆", "试探反应，可收可放"),
        ("回应重心", "揭历史、给定性", "划红线、点个人"),
        ("关键措辞", "“背叛”“公然挑衅”", "“强烈不满”“敦促约束”"),
    ]

    yy = [3.55, 2.65, 1.75, 0.85]
    for (label, jp, ph), y in zip(rows, yy):
        ax.text(0.02, y, label, fontsize=10.5, color=GRAY, va="center")
        ax.text(COL_J, y, jp, fontsize=11, color=DARK, va="center", ha="center")
        ax.text(COL_P, y, ph, fontsize=11, color=DARK, va="center", ha="center")
        ax.plot([0.02, 0.98], [y - 0.38, y - 0.38], color=LIGHT, lw=0.7, alpha=0.7)

    # 底部结论
    ax.add_patch(plt.Rectangle((0.02, -0.22), 0.96, 0.52,
                               facecolor=PALE, edgecolor=LIGHT, linewidth=1.0))
    ax.text(0.50, 0.04, "一个是掀桌子，一个是伸脚试深浅——回应的分量自然不同",
            fontsize=11.5, color=DARK, ha="center", va="center", weight="bold")

    footer(fig, "据国防部 2026-11-13 例行新闻发布会实录整理。")
    fig.savefig(OUT + "图3_两种姿态对比.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")
