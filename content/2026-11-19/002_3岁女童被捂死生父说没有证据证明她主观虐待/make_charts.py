# -*- coding: utf-8 -*-
"""
《3 岁女童被捂死，生父说“没有证据证明她主观虐待”》配套图表
事实口径（2026-11-18 江苏常熟一审宣判）：
  · 3 岁女童被生父同居女友邱某捂死案一审宣判；
  · 邱某犯故意杀人罪，判处无期徒刑；
  · 案发时邱某已怀孕，不适用死刑；
  · 据此前报道，女童生前身体多次骨折、被烫伤；
  · 女童生父在宣判后回应“女友是否虐待孩子”的争议时称
    “没有证据证明她主观虐待”，并称判决没有针对这一项量刑；
  · 女童生母表示将请求抗诉，并申请限制减刑；
  · 女童父亲称对判决结果不满意，“准备抗诉”。
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
    fig = base("判决书上的三行字",
               "江苏常熟 · 3 岁女童被生父同居女友捂死案，一审宣判")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    rows = [
        ("罪名", "故意杀人罪", DARK, 17.0,
         "邱某被认定的罪名"),
        ("刑罚", "无期徒刑", RED, 24.0,
         "判决结果"),
        ("死刑适用", "案发时被告已怀孕，不适用死刑", SLATE, 13.0,
         "依法不适用死刑"),
    ]

    yy = 0.760
    for i, (label, value, color, size, note) in enumerate(rows):
        ax.plot([0.040, 0.960], [yy + 0.085, yy + 0.085], color=LIGHT,
                linewidth=0.9)
        ax.text(0.048, yy, label, fontsize=9.8, color=GRAY, weight="bold",
                ha="left", va="center")
        ax.text(0.300, yy, value, fontsize=size, color=color, weight="bold",
                ha="left", va="center")
        ax.text(0.300, yy - 0.058, note, fontsize=8.6, color=GRAY,
                ha="left", va="center")
        yy -= 0.225

    ax.plot([0.040, 0.960], [0.110, 0.110], color=LIGHT, linewidth=0.9)
    ax.text(0.500, 0.170, "2026 年 11 月 18 日 · 一审", fontsize=9.2,
            color=GRAY, ha="center", va="center")

    punchline(fig, "这些是判决书上的字。法庭外，还有另一句话。")
    footer(fig, "事实：2026-11-18 江苏常熟一审宣判｜制图：本文")
    fig.savefig(OUT + "图1_判决书上的三行字.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("孩子生前的伤，和生父的那句话",
               "据此前报道：女童生前多次骨折、被烫伤；宣判后，生父回应“是否虐待”的争议")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # 左：孩子的伤
    ax.add_patch(FancyBboxPatch((0.018, 0.170), 0.450, 0.720,
                                boxstyle="round,pad=0.012",
                                facecolor=SAND, edgecolor="#d9cdb6",
                                linewidth=1.0))
    ax.text(0.044, 0.815, "3 岁女童 · 生前", fontsize=10.6, color="#7a6746",
            weight="bold", ha="left", va="center")
    ax.plot([0.044, 0.442], [0.772, 0.772], color="#d9cdb6", linewidth=1.0)

    injuries = [
        ("多次骨折", "据此前报道"),
        ("被烫伤", "据此前报道"),
    ]
    yy = 0.660
    for head, note in injuries:
        ax.text(0.048, yy, head, fontsize=17.0, color=RED, weight="bold",
                ha="left", va="center")
        ax.text(0.048, yy - 0.070, note, fontsize=8.8, color="#8a7a5e",
                ha="left", va="center")
        yy -= 0.200

    ax.text(0.048, 0.240,
            "一个 3 岁的孩子，伤在身上。",
            fontsize=9.0, color="#8a7a5e", ha="left", va="center")

    # 右：生父的话
    ax.add_patch(FancyBboxPatch((0.532, 0.170), 0.450, 0.720,
                                boxstyle="round,pad=0.012",
                                facecolor="#fbf3f1", edgecolor=LIGHT,
                                linewidth=1.0))
    ax.text(0.558, 0.815, "生父 · 宣判后", fontsize=10.6, color=NAVY,
            weight="bold", ha="left", va="center")
    ax.plot([0.558, 0.956], [0.772, 0.772], color=LIGHT, linewidth=1.0)

    ax.text(0.558, 0.600, "“没有证据证明\n她主观虐待”", fontsize=19.0,
            color=DARK, weight="bold", ha="left", va="center",
            linespacing=1.6)
    ax.text(0.558, 0.330,
            "他补充：因此判决没有\n针对这一项量刑。",
            fontsize=9.2, color=SLATE, ha="left", va="center", linespacing=1.8)
    ax.text(0.558, 0.230, "回应“女友是否虐待孩子”的争议",
            fontsize=8.6, color=GRAY, ha="left", va="center")

    punchline(fig, "什么才算“主观”的证据？")
    footer(fig, "事实：伤情据此前报道；生父表态据宣判后回应｜制图：本文")
    fig.savefig(OUT + "图2_孩子生前的伤和生父的那句话.png", dpi=150,
                facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("判决之后，两个家长都说“抗诉”",
               "生母表示将请求抗诉、申请限制减刑；生父称对判决不满意、“准备抗诉”")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    panels = [
        ("生母", "表示将请求抗诉", "表示将申请限制减刑",
         ["宣判后的公开表态"]),
        ("生父", "称对判决结果不满意", "“准备抗诉”",
         ["庭外先说：“没有证据证明她主观虐待”"]),
    ]

    xs = [0.018, 0.532]
    for i, (name, line1, line2, notes) in enumerate(panels):
        face = "#fafbfc" if i == 1 else "#fbf6f2"
        ax.add_patch(FancyBboxPatch((xs[i], 0.150), 0.450, 0.740,
                                    boxstyle="round,pad=0.012",
                                    facecolor=face, edgecolor=LIGHT,
                                    linewidth=1.0))
        ax.text(xs[i] + 0.028, 0.830, name, fontsize=11.0, color=NAVY,
                weight="bold", ha="left", va="center")
        ax.plot([xs[i] + 0.028, xs[i] + 0.422], [0.788, 0.788],
                color=LIGHT, linewidth=1.0)

        ax.text(xs[i] + 0.028, 0.700, line1, fontsize=12.4, color=RED,
                weight="bold", ha="left", va="center")
        ax.text(xs[i] + 0.028, 0.610, line2, fontsize=12.4, color=RED,
                weight="bold", ha="left", va="center")

        yy = 0.480
        for n in notes:
            ax.plot([xs[i] + 0.034], [yy + 0.006], marker="s", markersize=4.6,
                    color=SLATE, zorder=3)
            ax.text(xs[i] + 0.056, yy, n, fontsize=9.0, color=SLATE,
                    ha="left", va="top", linespacing=1.8)
            yy -= 0.105

    ax.text(0.500, 0.075, "抗诉由检察机关提起，家属能做的，是在法定期限内请求。",
            fontsize=8.8, color=GRAY, ha="center", va="center")

    punchline(fig, "同一声“抗诉”，指向的是同一个结果吗？")
    footer(fig, "事实：双方表态据宣判后回应；图为两方已公开的说法｜制图：本文")
    fig.savefig(OUT + "图3_判决之后两个家长都说抗诉.png", dpi=150,
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)
