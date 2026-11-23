# -*- coding: utf-8 -*-
"""
《15元盒饭「售完为止」：你上次在高铁上吃到它，是哪一年》配套图表

事实口径（核到央广网、羊城晚报、光明网、新京报）：
  · 2026-11-20，博主发帖称“以后高铁的‘15元盒饭’貌似就要消失了”，
    晒出上海局盒饭页面档位：19、29、39、49、59 元。
  · 羊城晚报记者看到的截图原图：G7463 次（亳州南—温州南），
    剁椒鸡/宫保鸡丁 19 元、狮子头 29 元、叉烧肉 39 元，未见 15 元盒饭；
    同一报道中，网友晒出的 G8253 次（连云港—上海）页面仍有 15 元拌面。
  · 2026-11-21，12306 客服：不同车次餐食种类、价格、库存不同，提供
    高、中、低不同价位餐食，实行“售完为止”，并非统一取消低价餐食。
  · 2015-01-01 施行《铁路旅客运输服务质量规范》第九条要求“2 元预包装
    饮用水和 15 元盒饭不断供”；2017-01-01 起以“内部要求”停止执行，
    售完即止、中途不补货（新京报 2017-01-12）。

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


def card(ax, x, y, w, h, edge, face="white", lw=1.0, dashed=False, z=2):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.004,rounding_size=0.014",
        facecolor=face, edgecolor=edge, linewidth=lw,
        linestyle=(0, (4, 3)) if dashed else "-", zorder=z))


def new_axes(fig):
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return ax


# ---------------------------------------------------------------- 图 1
def fig1():
    """G7463 页面上的五个档位，15 元未出现"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "一张订餐页面上，最低一档是 19 元",
           "博主晒出的 G7463 次（亳州南—温州南）盒饭页面，共 5 档")

    x0 = 0.170
    scale = 0.440 / 59.0
    bh = 0.052

    rows = [
        (15, "该页面未显示", None, True),
        (19, "湘味剁椒鸡、宫保鸡丁", RED, False),
        (29, "红烧狮子头", NAVY, False),
        (39, "港式叉烧肉", NAVY, False),
        (49, "套餐", NAVY, False),
        (59, "套餐", NAVY, False),
    ]
    y = 0.655
    for price, dish, color, ghost in rows:
        w = price * scale
        if ghost:
            ax.add_patch(Rectangle((x0, y - bh / 2), w, bh, facecolor="#f4f5f7",
                                   edgecolor=GRAY, linewidth=1.1,
                                   linestyle=(0, (4, 3)), zorder=3))
            pcolor = GRAY
            dcolor = GRAY
        else:
            ax.add_patch(Rectangle((x0, y - bh / 2), w, bh, facecolor=color,
                                   edgecolor="none", zorder=3))
            pcolor = color
            dcolor = SLATE
        ax.text(0.045, y, "%d 元" % price, fontsize=12.0, color=pcolor,
                weight="bold", ha="left", va="center", zorder=4)
        ax.text(x0 + w + 0.014, y, dish, fontsize=8.8, color=dcolor,
                ha="left", va="center", zorder=4)
        y -= 0.089

    ax.text(0.045, 0.145,
            "注：49 元、59 元两档的套餐名称未见披露；报道未给出各档配餐数量。",
            fontsize=8.2, color=GRAY, ha="left", va="center")

    card(ax, 0.665, 0.190, 0.290, 0.445, NAVY, lw=1.3)
    ax.text(0.685, 0.600, "同一报道，另一张页面", fontsize=10.6, color=NAVY,
            weight="bold", ha="left", va="center", zorder=6)
    ax.plot([0.685, 0.933], [0.576, 0.576], color=NAVY, linewidth=0.9,
            alpha=0.35, zorder=5)
    ax.text(0.685, 0.545,
            "G8253 次（连云港—上海）\n\n仍有 15 元的\n卤肉杂酱拌面\n\n"
            "→ 一张页面\n不能推断全国取消",
            fontsize=9.0, color=DARK, ha="left", va="top",
            linespacing=1.55, zorder=6)

    punchline(fig, "15 元不是每趟都有——这张没有，另一张有。")
    footer(fig, "事实来源：羊城晚报·羊城派 2026-11-21（博主 2026-11-20 帖文及截图）；"
                "光明网转经济日报 2026-11-21")
    fig.savefig(OUT + "图1_五档.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """“售完为止”管的是哪一段"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "「售完为止」管的是卖完之后，不是卖之前",
           "12306 客服 2026-11-21 的回应；2017 年起售完即止、中途不补货")

    steps = [
        ("1  发车", ["按车次配餐", "配几份？", "未公开"], GRAY, True),
        ("2  售卖", ["先到先得", "售完即止"], NAVY, False),
        ("3  售罄", ["中途不补货", "不追加"], RED, False),
        ("4  之后", ["页面只剩", "其他档位"], SLATE, False),
    ]

    w, h = 0.204, 0.215
    xs = [0.045, 0.288, 0.531, 0.774]
    top = 0.625
    for (title, lines, color, dashed), x in zip(steps, xs):
        card(ax, x, top - h, w, h, color, lw=1.4, dashed=dashed)
        ax.text(x + 0.018, top - 0.035, title, fontsize=10.6, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        yy = top - 0.082
        for line in lines:
            ax.text(x + 0.018, yy, line, fontsize=9.2, color=DARK,
                    ha="left", va="center", zorder=6)
            yy -= 0.040

    for i in range(3):
        xa = xs[i] + w + 0.004
        xb = xs[i + 1] - 0.004
        ax.annotate("", xy=(xb, top - h / 2), xytext=(xa, top - h / 2),
                    arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=1.2))

    ax.text(0.045, 0.345,
            "「售完为止」回答的是第 2 步之后的事：卖完了，就不补。",
            fontsize=9.6, color=DARK, ha="left", va="center")
    ax.text(0.045, 0.290,
            "它不回答第 1 步：这趟车发车时，到底带了几份 15 元的盒饭。",
            fontsize=9.6, color=RED, ha="left", va="center")

    punchline(fig, "规则说得清售完怎么办，说不清一开始有几份。")
    footer(fig, "事实来源：央广网 2026-11-22；羊城晚报 2026-11-21；"
                "新京报 2017-01-12（2017 年起售完即止、中途不补货）")
    fig.savefig(OUT + "图3_售完为止.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """2015 → 2017 → 2026 的时间线"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "「售完为止」，已经执行了九年多",
           "2015 年的「不断供」、2017 年的停止执行，与 2026 年的这次争论")

    ty = 0.470
    ax.plot([0.060, 0.945], [ty, ty], color=LIGHT, linewidth=2.2, zorder=2)

    nodes = [
        (0.135, "2015.01", "《规范》施行", ["2 元水、15 元盒饭", "不断供"], NAVY),
        (0.345, "2017.01", "停止执行", ["售完即止", "中途不补货"], RED),
        (0.655, "2026.11.20", "博主晒图", ["上海局页面", "最低 19 元"], SLATE),
        (0.865, "2026.11.21", "12306 回应", ["并非统一取消", "售完为止"], TEAL),
    ]
    for x, date, label, lines, color in nodes:
        ax.add_patch(plt.Circle((x, ty), 0.0085, color=color, zorder=4))
        ax.text(x, ty + 0.038, date, fontsize=10.6, color=color,
                weight="bold", ha="center", va="bottom", zorder=5)
        ax.text(x, ty - 0.048, label, fontsize=9.4, color=DARK,
                ha="center", va="top", zorder=5)
        yy = ty - 0.100
        for line in lines:
            ax.text(x, yy, line, fontsize=8.8, color=SLATE,
                    ha="center", va="top", zorder=5)
            yy -= 0.043

    ax.text(0.045, 0.170,
            "2017 年改成「售完即止」之后，旅客看到的结果没有变：",
            fontsize=9.4, color=DARK, ha="left", va="center")

    punchline(fig, "规则换了说法，问题还是同一个：一开始配了几份。")
    footer(fig, "事实来源：新京报 2017-01-12；羊城晚报 2026-11-21；央广网 2026-11-22")
    fig.savefig(OUT + "图2_九年.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)