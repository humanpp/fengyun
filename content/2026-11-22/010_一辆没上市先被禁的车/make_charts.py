# -*- coding: utf-8 -*-
"""
《一辆还没在欧洲上市的车，先被禁了》配套图表（矩阵 / 双段时间线 / 三方对照）

事实口径（核到海牙地区法院 2026-11-20 临时禁令及路透社、联合早报、
观察者网、CnEVPost 报道）：
  · 禁令覆盖欧盟 27 国：禁止进口、生产、展示、销售、储存、交付；
    英国不在范围（法院对比亚迪英国子公司无管辖权）；
    匈牙利塞格德工厂禁产至案件了结；禁令送达一周后生效；
    罚则上限 1000 万欧元（据汽车媒体及 CnEVPost）。
  · JLR 须 6 个月内提起正式诉讼；BYD 称独立设计、强烈反对、将上诉。

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


def new_axes(fig):
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return ax


# ---------------------------------------------------------------- 图 1
def fig1():
    """禁令范围矩阵：地区 × 行为"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "一张禁令，管到哪",
           "海牙地区法院 2026-11-20 临时禁令：地区 × 行为")

    acts = ["进口", "生产", "销售", "储存", "交付"]
    x0, w, gap = 0.315, 0.118, 0.012
    for i, act in enumerate(acts):
        ax.text(x0 + i * (w + gap) + w / 2, 0.665, act, fontsize=9.6,
                color=SLATE, ha="center", va="center")

    rows = [
        ("欧盟 27 国", 0.500, NAVY, "white", "√"),
        ("英国", 0.365, "#eceef1", GRAY, "×"),
    ]
    for name, y, face, fg, mark in rows:
        ax.text(0.050, y + 0.050, name, fontsize=11.0,
                color=NAVY if name.startswith("欧盟") else SLATE,
                weight="bold", ha="left", va="center", zorder=5)
        for i in range(len(acts)):
            x = x0 + i * (w + gap)
            ax.add_patch(Rectangle((x, y), w, 0.100, facecolor=face,
                                   edgecolor="white", linewidth=1.2, zorder=3))
            ax.text(x + w / 2, y + 0.050, mark, fontsize=15,
                    color=fg, ha="center", va="center", zorder=4)

    ax.text(0.050, 0.330,
            "法院：对比亚迪英国子公司无管辖权，英国不在禁令范围。",
            fontsize=8.4, color=GRAY, ha="left", va="center")

    ax.text(0.050, 0.255,
            "罚则：上限 1000 万欧元  ·  禁令送达一周后生效  ·  匈牙利塞格德工厂禁产",
            fontsize=9.0, color=SLATE, ha="left", va="center")

    punchline(fig, "车还没上市，禁售先生效。")
    footer(fig, "事实来源：海牙地区法院 2026-11-20 临时禁令；路透社 2026-11-20；"
                "观察者网 2026-11-22；CnEVPost 2026-11-22")
    fig.savefig(OUT + "图1_禁令范围.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """双段时间线：已发生 / 接下来"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "临时禁令，只是第一回合",
           "从设计注册到下一步：已发生，与接下来")

    ax.text(0.045, 0.665, "已发生", fontsize=9.0, color=GRAY,
            weight="bold", ha="left", va="center")

    ty = 0.560
    ax.plot([0.060, 0.940], [ty, ty], color=LIGHT, linewidth=2.2, zorder=2)

    past = [
        (0.105, "2018", ["卫士外观", "欧盟注册"]),
        (0.290, "2019.09", ["卫士 110", "上市"]),
        (0.475, "2025", ["方程豹钛7", "中国上市"]),
        (0.660, "2026", ["捷豹路虎", "提起诉讼"]),
        (0.845, "2026.11.20", ["海牙法院", "临时禁令"]),
    ]
    for x, date, lines in past:
        ax.add_patch(plt.Circle((x, ty), 0.009, color=NAVY, zorder=4))
        ax.text(x, ty + 0.038, date, fontsize=9.2, color=NAVY,
                weight="bold", ha="center", va="bottom", zorder=5)
        yy = ty - 0.048
        for line in lines:
            ax.text(x, yy, line, fontsize=8.6, color=SLATE,
                    ha="center", va="top", zorder=5)
            yy -= 0.038

    ax.text(0.045, 0.400, "接下来", fontsize=9.0, color=RED,
            weight="bold", ha="left", va="center")

    ny = 0.300
    ax.plot([0.060, 0.940], [ny, ny], color=LIGHT, linewidth=2.2, zorder=2)
    nxt = [
        (0.200, "一周后", ["禁令生效"]),
        (0.500, "6 个月内", ["JLR 提起", "正式诉讼"]),
        (0.800, "上诉后", ["结果待定"]),
    ]
    for x, date, lines in nxt:
        ax.add_patch(plt.Circle((x, ny), 0.009, color=RED, zorder=4))
        ax.text(x, ny + 0.038, date, fontsize=9.2, color=RED,
                weight="bold", ha="center", va="bottom", zorder=5)
        yy = ny - 0.048
        for line in lines:
            ax.text(x, yy, line, fontsize=8.6, color=SLATE,
                    ha="center", va="top", zorder=5)
            yy -= 0.038

    punchline(fig, "设计权官司，打的是时间差。")
    footer(fig, "事实来源：路透社 2026-11-20；联合早报 2026-11-21；观察者网 2026-11-22；"
                "AutoCN 2026-11-21")
    fig.savefig(OUT + "图2_时间线.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """三方对照表"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "法院认的是外观，不是动机",
           "捷豹路虎、比亚迪、法院：立场、依据、下一步")

    cols = [
        ("捷豹路虎", NAVY, [
            "Ti7 抄袭卫士",
            "拥有多项欧盟设计权",
            "将保护知识产权",
        ]),
        ("比亚迪", RED, [
            "独立设计",
            "自主设计，未侵犯权利",
            "强烈反对，将上诉",
        ]),
        ("法院", TEAL, [
            "特征性元素均有体现",
            "整体印象无明显区别",
            "临时禁令，非终审",
        ]),
    ]

    col_x = [0.200, 0.450, 0.700]
    col_w = 0.230
    for (name, color, _), x in zip(cols, col_x):
        ax.text(x + col_w / 2, 0.610, name, fontsize=11.4, color=color,
                weight="bold", ha="center", va="center")
        ax.plot([x, x + col_w], [0.585, 0.585], color=color,
                linewidth=1.4, alpha=0.55)

    row_labels = ["立场", "依据", "下一步"]
    rows_y = [0.465, 0.350, 0.235]
    for label, ry in zip(row_labels, rows_y):
        ax.text(0.045, ry + 0.048, label, fontsize=9.0, color=GRAY,
                weight="bold", ha="left", va="center")

    for i, ry in enumerate(rows_y):
        for (name, color, items), x in zip(cols, col_x):
            ax.add_patch(Rectangle((x, ry), col_w, 0.095,
                                   facecolor="white", edgecolor=LIGHT,
                                   linewidth=0.9, zorder=2))
            ax.text(x + 0.014, ry + 0.048, items[i], fontsize=8.6,
                    color=DARK, ha="left", va="center", zorder=3)

    ax.text(0.045, 0.165,
            "法院处理的是特定欧盟注册外观设计权，不是“抄袭”的主观认定。",
            fontsize=9.0, color=SLATE, ha="left", va="center")

    punchline(fig, "像不像，法院说了算；抄没抄，不在这次裁决里。")
    footer(fig, "事实来源：路透社 2026-11-20；联合早报 2026-11-21；观察者网 2026-11-22；"
                "CnEVPost 2026-11-22")
    fig.savefig(OUT + "图3_三方主张.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)