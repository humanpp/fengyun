# -*- coding: utf-8 -*-
"""
《1600 元的烤全羊，剥不出一两肉》配套图表
事实口径（2026-11-17 四川绵阳张女士，平武县民宿）：
  · 张女士花 1600 元预订烤全羊，上桌后发现几乎全是骨架，
    剥离下来的羊肉不到一两（约 50 克）；
  · 民宿回应：上桌的是整只羊，只是烤制时火候偏大偏干；事发后已为
    游客赠送价值 300 元的烤鸡和多道配菜；并称游客当时“并没有提出异议”；
  · 平武文旅回应：已收到游客反映，相关部门正在对消费纠纷开展调查核实。
  · “约 32 元 / 克”为按 1600 元与 50 克两个数字直接相除得到的换算，
    文中已注明是粗算，不是涉事双方的说法。
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
    fig = base("1600 元，和一两肉",
               "四川绵阳 · 平武县一民宿 · 2026 年 11 月 17 日")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # 左：价格
    ax.text(0.060, 0.720, "1600 元", fontsize=54, color=DARK, weight="bold",
            ha="left", va="center")
    ax.text(0.060, 0.610, "一只烤全羊的预订价", fontsize=10.4, color=GRAY,
            ha="left", va="center")

    # 中间竖线
    ax.plot([0.480, 0.480], [0.420, 0.800], color=LIGHT, linewidth=1.0,
            linestyle=(0, (4, 4)))

    # 右：肉量
    ax.text(0.540, 0.720, "不到一两", fontsize=40, color=RED, weight="bold",
            ha="left", va="center")
    ax.text(0.540, 0.610, "剥离下来的羊肉，约 50 克", fontsize=10.4,
            color=GRAY, ha="left", va="center")

    # 对比条
    ax.plot([0.060, 0.940], [0.520, 0.520], color=LIGHT, linewidth=0.9)
    ax.text(0.060, 0.440, "上桌时：几乎全是骨架", fontsize=9.6, color=SLATE,
            ha="left", va="center")

    # 换算
    ax.add_patch(FancyBboxPatch((0.060, 0.150), 0.880, 0.150,
                                boxstyle="round,pad=0.012", facecolor=SAND,
                                edgecolor="#d9cdb6", linewidth=1.0))
    ax.text(0.085, 0.262, "按这两个数字直接相除：", fontsize=9.0,
            color="#8a7a5e", ha="left", va="center")
    ax.text(0.085, 0.196, "1600 元 ÷ 50 克 ≈ 32 元 / 克", fontsize=16.0,
            color="#7a6746", weight="bold", ha="left", va="center")
    ax.text(0.620, 0.196, "（粗算，烤制会失水）", fontsize=8.6, color="#8a7a5e",
            ha="left", va="center")

    punchline(fig, "这顿饭的价格，和盘子里的东西，不在一个量级上。")
    footer(fig, "事实：价格与肉量据张女士讲述及媒体报道；换算式为本文计算｜制图：本文")
    fig.savefig(OUT + "图1_1600块和一两肉.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("商家的三句话，各自能解释什么",
               "不是道歉，是三句说明：整只羊、火候偏大、送了 300 元烤鸡")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    rows = [
        ("① 上桌的是整只羊", "骨架在，羊就在。这句大概是真的。",
         "能解释“上桌的是羊”，解释不了“能吃的有多少”。"),
        ("② 烤制时火候偏大、偏干", "烤干会让肉缩水、变柴。",
         "缩水可以说，消失说不了：肉不会从骨头上走掉。"),
        ("③ 送了 300 元烤鸡和配菜，游客当时没提异议", "补偿是真的给了。",
         "一只羊的落差折价 300 元；当场不提，不等于认可。"),
    ]

    yy = 0.845
    for i, (head, can, cannot) in enumerate(rows):
        ax.add_patch(Rectangle((0.030, yy - 0.212), 0.006, 0.170,
                               facecolor=RED, edgecolor="none"))
        ax.text(0.056, yy, head, fontsize=11.0, color=DARK, weight="bold",
                ha="left", va="center")
        ax.text(0.056, yy - 0.058, can, fontsize=8.9, color=GRAY, ha="left",
                va="center")
        ax.text(0.056, yy - 0.108, cannot, fontsize=9.2, color=SLATE,
                ha="left", va="center")
        ax.plot([0.030, 0.960], [yy - 0.155, yy - 0.155], color=LIGHT,
                linewidth=0.8)
        yy -= 0.205

    punchline(fig, "三句都能解释一部分，合起来解释不了一两肉。")
    footer(fig, "事实：三句回应据涉事民宿答复媒体；点评为作者判断｜制图：本文")
    fig.savefig(OUT + "图2_商家的三句话.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("从一顿饭，到一次“调查核实”",
               "平武文旅：已收到游客反映，相关部门正在开展调查核实")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    items = [
        ("11 月 17 日", "预订并上桌", "1600 元的烤全羊，几乎全是骨架；\n剥下的肉不到一两"),
        ("当场", "游客未提出异议", "民宿方面的说法"),
        ("事后", "游客发帖讲述", "张女士向媒体讲述此事"),
        ("随后", "民宿回应", "上桌是整只羊，火候偏大偏干；\n已送价值 300 元烤鸡和多道配菜"),
        ("现在", "文旅介入", "平武文旅：已收到反映，\n正在对消费纠纷开展调查核实"),
    ]

    ax.plot([0.120, 0.120], [0.180, 0.830], color=LIGHT, linewidth=1.4)

    yy = 0.800
    for time, head, body in items:
        ax.plot([0.120], [yy], marker="o", markersize=7.0,
                color=RED if time == "现在" else NAVY, zorder=3)
        ax.text(0.055, yy, time, fontsize=9.4, color=GRAY, weight="bold",
                ha="right", va="center")
        ax.text(0.165, yy, head, fontsize=10.6, color=DARK, weight="bold",
                ha="left", va="center")
        ax.text(0.420, yy, body, fontsize=8.8, color=SLATE, ha="left",
                va="center", linespacing=1.7)
        yy -= 0.160

    punchline(fig, "“调查核实”意味着：还没有结论。")
    footer(fig, "事实：时间线与各方表述据 2026-11-17 报道及平武文旅回应｜制图：本文")
    fig.savefig(OUT + "图3_从一顿饭到一次调查核实.png", dpi=150,
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)