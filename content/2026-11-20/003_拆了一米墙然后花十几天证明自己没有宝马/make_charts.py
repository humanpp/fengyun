# -*- coding: utf-8 -*-
"""
《拆了一米墙，然后花十几天证明自己没有宝马》配套图表
事实口径（均据安徽日报大皖新闻 2026-11-18 调查报道，记者韩喻、张楠、李常宝）：
  · 吕国江 74 岁，安徽六安霍邱县石店镇宽店村草楼组，老房与院墙建于 1995 年；
  · 2025 年 10 月秋收期间拆墙内退，巷道由两米多拓宽至三米多，
    自费硬化路面、硬化屋后菜地一角以便会车；
  · 女儿吕莉发视频后点赞超 20 万，随后出现三类传言；
  · 《宗地图》地基长 18.27 米，现场实测 17.06 米，内退 1.21 米；
  · 霍邱县融媒体中心：无吕姓工作人员；县相关部门：4 位子女无一人体制内、
    名下均无宝马车；车管所查询：吕莉名下大众、其夫比亚迪。
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
GOLD = "#c9a27a"
GREEN = "#5a7d6f"

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


def canvas(fig):
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return ax


# ------------------------------------------------------------------ 图 1
def fig1():
    fig = base("墙退了一米二",
               "《宗地图》登记的地基长度，与记者现场实测")
    ax = canvas(fig)

    base_y = 0.300
    ax.plot([0.080, 0.920], [base_y, base_y], color=LIGHT, linewidth=1.2)

    # 两条水平长度条：18.27 与 17.06
    x0 = 0.150
    scale = 0.030          # 每米对应的横向长度
    y1, y2, h = 0.660, 0.430, 0.120

    # 宗地图 18.27
    ax.add_patch(Rectangle((x0, y1), 18.27 * scale, h, facecolor="#e8edf3",
                           edgecolor=NAVY, linewidth=1.2))
    ax.text(x0 - 0.012, y1 + h / 2, "宗地图", fontsize=10.4, color=NAVY,
            weight="bold", ha="right", va="center")
    ax.text(x0 + 18.27 * scale / 2, y1 + h / 2, "18.27 米", fontsize=15.0,
            color=NAVY, weight="bold", ha="center", va="center")

    # 实测 17.06
    ax.add_patch(Rectangle((x0, y2), 17.06 * scale, h, facecolor="#f6e4e1",
                           edgecolor=RED, linewidth=1.2))
    ax.text(x0 - 0.012, y2 + h / 2, "现场实测", fontsize=10.4, color=RED,
            weight="bold", ha="right", va="center")
    ax.text(x0 + 17.06 * scale / 2, y2 + h / 2, "17.06 米", fontsize=15.0,
            color=RED, weight="bold", ha="center", va="center")

    # 差值括注
    dx = x0 + 17.06 * scale
    ax.annotate("", xy=(dx, y2 - 0.045), xytext=(dx, y1 + h + 0.045),
                arrowprops=dict(arrowstyle="<->", color=DARK, linewidth=1.1))
    ax.text(dx + 0.018, (y1 + h + y2) / 2, "退 1.21 米", fontsize=13.0,
            color=DARK, weight="bold", ha="left", va="center")

    # 说明：那截“凸出”是什么
    ax.add_patch(FancyBboxPatch((0.080, 0.150), 0.860, 0.150,
                                boxstyle="round,pad=0.012", facecolor=SAND,
                                edgecolor="#d9cdb6", linewidth=1.0))
    ax.text(0.105, 0.248, "所谓“凸出来”的那一截", fontsize=9.6,
            color="#8a7a5e", ha="left", va="center")
    ax.text(0.105, 0.196,
            "1995 年按户分地可盖 4 间，吕家手头紧只盖了 3 间——正房与院墙之间的地，"
            "是当年少盖一间空出来的，不是占道。",
            fontsize=10.0, color="#7a6746", ha="left", va="center")

    punchline(fig, "尺子量出来的是退让，不是纠错。")
    footer(fig, "事实：18.27 米据吕国江家《宗地图》，17.06 米为大皖新闻记者现场实测（2026-11-18）｜制图：本文")
    fig.savefig(OUT + "图1_墙退了一米二.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("三条传言，逐条查",
               "查证方：大皖新闻 2026 年 11 月 16—17 日实地采访，霍邱县相关部门、县融媒体中心、县公安局车管所")
    ax = canvas(fig)

    rows = [
        ("女儿是县融媒体中心记者\n借此策划炒作、准备升职",
         "该中心无吕姓工作人员；吕莉在六安\n经营音响生意，4 位子女无一人体制内"),
        ("为女儿新买的宝马 X5\n通行方便才拆墙",
         "视频中车为朋友张某东的宝马 X1；\n车管所查询：吕莉大众、其夫比亚迪"),
        ("院墙本就凸出占道\n拆墙只是“纠错”",
         "宗地图 18.27 米、实测 17.06 米；\n原村民组长与两户邻居均证实未占道"),
    ]

    y_top = 0.830
    row_h = 0.215
    for i, (rumor, fact) in enumerate(rows):
        y = y_top - i * row_h

        # 左：传言
        ax.add_patch(FancyBboxPatch((0.060, y - 0.150), 0.360, 0.160,
                                    boxstyle="round,pad=0.010",
                                    facecolor="#f6e4e1", edgecolor=RED,
                                    linewidth=1.0))
        ax.text(0.078, y - 0.020, "传言 %d" % (i + 1), fontsize=8.6, color=RED,
                weight="bold", ha="left", va="center")
        ax.text(0.078, y - 0.078, rumor, fontsize=9.4, color=DARK, ha="left",
                va="center", linespacing=1.5)

        # 中间箭头
        ax.annotate("", xy=(0.500, y - 0.070), xytext=(0.432, y - 0.070),
                    arrowprops=dict(arrowstyle="-|>", color=GRAY, linewidth=1.5))

        # 右：查证
        ax.add_patch(FancyBboxPatch((0.512, y - 0.150), 0.428, 0.160,
                                    boxstyle="round,pad=0.010",
                                    facecolor="#eaf0ec", edgecolor=GREEN,
                                    linewidth=1.0))
        ax.text(0.530, y - 0.020, "查证：不实", fontsize=8.6, color=GREEN,
                weight="bold", ha="left", va="center")
        ax.text(0.530, y - 0.078, fact, fontsize=9.4, color=DARK, ha="left",
                va="center", linespacing=1.5)

    punchline(fig, "三条传言，没有一条站得住。")
    footer(fig, "事实：安徽日报大皖新闻 2026-11-18 调查报道《“霍邱老人拆墙让路”调查：“女儿是记者”等网上传言不实》｜制图：本文")
    fig.savefig(OUT + "图2_三条传言与查证结果.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("澄清的成本",
               "造一条谣只要一行字；证伪它，要跑两个部门、翻 30 年前的账")
    ax = canvas(fig)

    # 左：造谣
    ax.add_patch(FancyBboxPatch((0.070, 0.560), 0.360, 0.230,
                                boxstyle="round,pad=0.012",
                                facecolor="#f6e4e1", edgecolor=RED,
                                linewidth=1.1))
    ax.text(0.095, 0.720, "造一条谣", fontsize=11.6, color=RED, weight="bold",
            ha="left", va="center")
    ax.text(0.095, 0.640, "在评论区打一行字", fontsize=12.6, color=DARK,
            weight="bold", ha="left", va="center")
    ax.text(0.095, 0.590, "零成本 · 零举证 · 零后果预期", fontsize=9.0,
            color=GRAY, ha="left", va="center")

    # 右：证伪
    ax.add_patch(FancyBboxPatch((0.500, 0.330), 0.440, 0.460,
                                boxstyle="round,pad=0.012",
                                facecolor="#eaf0ec", edgecolor=GREEN,
                                linewidth=1.1))
    ax.text(0.525, 0.740, "证伪它", fontsize=11.6, color=GREEN, weight="bold",
            ha="left", va="center")
    steps = [
        "进村采访当事人与女儿",
        "调《宗地图》并现场实测",
        "跑县公安局车管所查车辆",
        "问县融媒体中心人事",
        "找 1994 年主持分地的老组长",
        "问两户邻居、一名农机手",
    ]
    yy = 0.690
    for s in steps:
        ax.text(0.525, yy, "·  " + s, fontsize=9.8, color=DARK, ha="left",
                va="center")
        yy -= 0.058

    # 中间对比
    ax.annotate("", xy=(0.500, 0.560), xytext=(0.430, 0.560),
                arrowprops=dict(arrowstyle="-|>", color=GRAY, linewidth=1.6))
    ax.text(0.465, 0.505, "两天\n六步", fontsize=8.8, color=GRAY,
            ha="center", va="center", linespacing=1.5)

    ax.text(0.070, 0.420, "而澄清之后，质疑可以换一个角度重新开始：",
            fontsize=10.0, color=SLATE, ha="left", va="center")
    ax.text(0.070, 0.360,
            "“女儿不在编，那临时工呢”　“女儿没宝马，那女婿呢”",
            fontsize=11.4, color=DARK, weight="bold", ha="left", va="center")
    ax.text(0.070, 0.290, "（此句为对质疑逻辑的概括，非报道原文）",
            fontsize=8.4, color=GRAY, ha="left", va="center")

    punchline(fig, "自证的人，永远追不上换角度的人。")
    footer(fig, "事实：查证过程据大皖新闻 2026-11-18 报道；右栏为报道中记者实际走访与查询事项归纳｜制图：本文")
    fig.savefig(OUT + "图3_澄清的成本.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)
