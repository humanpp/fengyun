# -*- coding: utf-8 -*-
"""
《后雾灯的一个符号，召回近18万辆车》配套图表

事实口径（核到市场监管总局 2026-11-20 召回公告）：
  · 奔驰：S2026M0149V 进口 21,639 辆、S2026M0150V 国产 157,715 辆，
    合计 179,354 辆；组合仪表控制单元软件开发偏差，后雾灯标志可能不符国标；
    属 2024-06-07 召回（进口 51,536 辆，同一原因）的扩大召回。
  · 捷豹路虎：S2026M0151V 揽胜运动版 17 辆（后副车架可能裂纹）；
    S2026M0152V 卫士 1 辆（PCM 的 PCB 装配定位偏差，极端情况失去动力）。
  · 福特：E2026M0148V F-150 54 辆（燃油箱固定带可能未正确固定）。

输出目录 = 脚本所在目录
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei"]
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
TEAL = "#3f6f6b"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep

Y_TITLE = 0.958
Y_SUB = 0.898
Y_PUNCH = 0.068
Y_FOOT = 0.020


def header(fig, title, sub):
    fig.text(0.045, Y_TITLE, title, fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, Y_SUB, sub, fontsize=10.4, color=GRAY,
             ha="left", va="top")


def footer(fig, text):
    fig.text(0.045, Y_FOOT, text, fontsize=7.6, color=GRAY,
             ha="left", va="bottom")


def punchline(fig, text):
    fig.text(0.045, Y_PUNCH, text, fontsize=10.4, color=DARK,
             ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


def card(ax, x, y, w, h, edge, face="white", lw=1.2, z=2):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.004,rounding_size=0.014",
        facecolor=face, edgecolor=edge, linewidth=lw, zorder=z))


def new_axes(fig):
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return ax


# ---------------------------------------------------------------- 图 1
def fig1():
    """三种量级"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "同一周，三种量级",
           "2026-11-20 市场监管总局集中披露：奔驰、捷豹路虎、福特")

    x0 = 0.235
    maxw = 0.600

    # 奔驰：进口 + 国产 堆叠
    y = 0.620
    w_in = 21639 / 179354 * maxw
    w_dn = 157715 / 179354 * maxw
    ax.add_patch(Rectangle((x0, y), w_in, 0.080, facecolor=SLATE,
                           edgecolor="white", linewidth=0.8, zorder=3))
    ax.add_patch(Rectangle((x0 + w_in, y), w_dn, 0.080, facecolor=NAVY,
                           edgecolor="white", linewidth=0.8, zorder=3))
    ax.text(0.045, y + 0.040, "奔驰", fontsize=12.0, color=DARK,
            weight="bold", ha="left", va="center", zorder=4)
    ax.text(x0 + maxw + 0.012, y + 0.058, "179,354 辆", fontsize=11.0,
            color=NAVY, weight="bold", ha="left", va="center")
    ax.text(x0 + maxw + 0.012, y + 0.026, "进口 21,639 · 国产 157,715",
            fontsize=8.2, color=GRAY, ha="left", va="center")

    small = [("捷豹路虎", 18, 0.440), ("福特", 54, 0.320)]
    for name, num, y in small:
        ax.add_patch(Rectangle((x0, y), 0.007, 0.080, facecolor=RED,
                               edgecolor="white", linewidth=0.8, zorder=3))
        ax.text(0.045, y + 0.040, name, fontsize=11.0, color=DARK,
                ha="left", va="center", zorder=4)
        ax.text(x0 + 0.020, y + 0.040, "%d 辆" % num, fontsize=9.0,
                color=RED, ha="left", va="center", zorder=4)

    ax.text(0.045, 0.215,
            "奔驰一家占三批总数的 99.96%；捷豹路虎 18 辆、福特 54 辆。",
            fontsize=9.0, color=SLATE, ha="left", va="center")

    punchline(fig, "软件召回一次覆盖近 18 万辆，硬件召回只有十几辆。")
    footer(fig, "事实来源：市场监管总局 2026-11-20 召回公告（奔驰 S2026M0149V / S2026M0150V、"
                "捷豹路虎 S2026M0151V / S2026M0152V、福特 E2026M0148V）")
    fig.savefig(OUT + "图1_三种量级.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """两次召回：2024 → 2026"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "一次没盖全，两年后补上",
           "奔驰同一软件缺陷的两次召回")

    card(ax, 0.045, 0.320, 0.400, 0.330, GRAY, lw=1.3)
    ax.text(0.065, 0.600, "2024-06-07", fontsize=10.0, color=GRAY,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.065, 0.548, "首次召回", fontsize=9.4, color=SLATE,
            ha="left", va="center", zorder=6)
    ax.text(0.065, 0.485, "51,536 辆", fontsize=18.0, color=DARK,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.065, 0.425, "进口 A 级、B 级、CLA、GLB / GLE / GLS", fontsize=8.0,
            color=GRAY, ha="left", va="center", zorder=6)
    ax.text(0.065, 0.385, "同一软件缺陷", fontsize=8.4, color=RED,
            ha="left", va="center", zorder=6)

    card(ax, 0.555, 0.320, 0.400, 0.330, RED, lw=1.5)
    ax.text(0.575, 0.600, "2026-11-20", fontsize=10.0, color=RED,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.575, 0.548, "扩大召回", fontsize=9.4, color=SLATE,
            ha="left", va="center", zorder=6)
    ax.text(0.575, 0.485, "179,354 辆", fontsize=18.0, color=NAVY,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.575, 0.425, "进口 21,639 + 国产 157,715", fontsize=8.0,
            color=GRAY, ha="left", va="center", zorder=6)
    ax.text(0.575, 0.385, "同一软件缺陷", fontsize=8.4, color=RED,
            ha="left", va="center", zorder=6)

    ax.annotate("", xy=(0.545, 0.485), xytext=(0.455, 0.485),
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.6))

    ax.text(0.045, 0.255,
            "扩大召回：把上次没覆盖到的车补进来。",
            fontsize=9.4, color=SLATE, ha="left", va="center")

    punchline(fig, "扩大召回，是给上一次召回打补丁。")
    footer(fig, "事实来源：市场监管总局 2024-06-07、2026-11-20 召回公告；"
                "2026 年公告明确表述为“扩大召回”")
    fig.savefig(OUT + "图3_扩大召回.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """两种读法：按辆数 vs 按召回编号"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "同一批召回，两种读法",
           "按辆数，软件占 99.96%；按召回编号，软件 2/5")

    x0, total_w = 0.260, 0.700

    # 第一行：按辆数
    y1 = 0.565
    w_sw = 0.692
    w_ot = 0.008
    ax.add_patch(Rectangle((x0, y1), w_sw, 0.105, facecolor=NAVY,
                           edgecolor="white", linewidth=1.0, zorder=3))
    ax.add_patch(Rectangle((x0 + w_sw, y1), w_ot, 0.105, facecolor=RED,
                           edgecolor="white", linewidth=1.0, zorder=3))
    ax.text(0.045, y1 + 0.052, "按辆数", fontsize=11.0, color=DARK,
            weight="bold", ha="left", va="center", zorder=4)
    ax.text(x0 + 0.020, y1 + 0.052, "软件 179,354 辆 · 99.96%", fontsize=9.6,
            color="white", weight="bold", ha="left", va="center", zorder=5)
    ax.text(0.045, y1 - 0.030, "硬件 / 装配合计 72 辆 · 0.04%", fontsize=8.6,
            color=RED, ha="left", va="center")

    # 第二行：按召回编号
    y2 = 0.330
    w2_sw = total_w * 0.4
    w2_ot = total_w * 0.6
    ax.add_patch(Rectangle((x0, y2), w2_sw, 0.105, facecolor=NAVY,
                           edgecolor="white", linewidth=1.0, zorder=3))
    ax.add_patch(Rectangle((x0 + w2_sw, y2), w2_ot, 0.105, facecolor=RED,
                           edgecolor="white", linewidth=1.0, zorder=3))
    ax.text(0.045, y2 + 0.052, "按召回编号", fontsize=11.0, color=DARK,
            weight="bold", ha="left", va="center", zorder=4)
    ax.text(x0 + w2_sw / 2, y2 + 0.052, "软件 2 起", fontsize=9.4,
            color="white", weight="bold", ha="center", va="center", zorder=5)
    ax.text(x0 + w2_sw + w2_ot / 2, y2 + 0.052, "硬件 / 装配 3 起", fontsize=9.4,
            color="white", weight="bold", ha="center", va="center", zorder=5)

    ax.text(0.045, 0.215,
            "软件 2 起：奔驰进口、国产各一张备案；硬件/装配 3 起：路虎 2 起、福特 1 起。",
            fontsize=8.6, color=SLATE, ha="left", va="center")

    punchline(fig, "软件是不是主因，看你按什么数。")
    footer(fig, "事实来源：市场监管总局 2026-11-20 召回公告（5 个召回编号，合计 179,426 辆）")
    fig.savefig(OUT + "图2_两种读法.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)