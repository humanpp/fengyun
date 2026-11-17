# -*- coding: utf-8 -*-
"""
《419 万辆、每天 2.6 亿公里：比亚迪把智驾拖进数据规模战》配套图表
事实来源：比亚迪 2026-11-14 公布数据（截至 10-31 保有量 419 万辆、10 月
245,483 辆、天神之眼日生成 2.6 亿公里）；华为乾崑 10 月报告（172.7 亿累计、
14.8 亿/月、月活 95.2%）；2026 年 10 月新势力交付数据
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


# ---------------------------------------------------------------- 图 1
def fig1():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.235, 0.190, 0.720, 0.570])

    fig.text(0.045, 0.955, "10 月单月：一家对六家", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.882, "单位：万辆。比亚迪为辅助驾驶车型销量，其余为当月交付量",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    rows = [
        ("比亚迪（辅助驾驶车型）", 24.55, NAVY, "245,483 辆"),
        ("零跑", 10.61, SLATE, "106,127 辆"),
        ("小鹏", 5.02, LIGHT, "50,237 辆"),
        ("小米", 5.00, LIGHT, "超 5 万辆"),
        ("蔚来", 3.42, LIGHT, "34,246 辆"),
        ("鸿蒙智行", 3.35, LIGHT, "33,537 辆"),
        ("理想", 2.90, LIGHT, "29,025 辆"),
    ]

    ys = list(range(len(rows)))[::-1]
    for y, (name, val, color, detail) in zip(ys, rows):
        ax.barh([y], [val], height=0.52, color=color, edgecolor="none")
        tcolor = "white" if color == NAVY else DARK
        ax.text(val + 0.35, y, f"{val:.2f}", fontsize=12.5, color=DARK,
                weight="bold", va="center")
        ax.text(val - 0.4, y, detail, fontsize=9.6, color=tcolor,
                ha="right", va="center")

    ax.set_yticks(ys)
    ax.set_yticklabels([r[0] for r in rows], fontsize=11.2)
    ax.set_xlim(0, 30)
    ax.set_ylim(-0.65, len(rows) - 0.35)
    ax.set_xticks([0, 5, 10, 15, 20, 25, 30])
    ax.tick_params(axis="x", colors=DARK, labelsize=10.5, length=0)
    ax.tick_params(axis="y", colors=DARK, length=0)
    ax.set_axisbelow(True)
    ax.grid(axis="x", color=LIGHT, linewidth=0.8, alpha=0.55)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(LIGHT)

    ax.text(0.2, -0.55, "六家合计约 30.3 万辆，是比亚迪一家智驾车型销量的 1.23 倍",
            fontsize=9.8, color=GRAY, va="center")

    punchline(fig, "一家车企的智驾月销，顶得上一整批新势力。")
    footer(fig, "据比亚迪 2026-11-14 公布数据；2026 年 10 月新势力交付数据据 21 世纪经济报道、汽车之家等。")
    fig.savefig(OUT + "图1_十月单月.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.075, 0.205, 0.860, 0.560])
    ax2 = ax.twinx()

    fig.text(0.045, 0.955, "半年：保有量涨了百万辆，日数据同步抬升", fontsize=18.5,
             color=DARK, weight="bold", ha="left", va="top")
    fig.text(0.045, 0.882, "左侧为辅助驾驶车型保有量，右侧为天神之眼日生成数据",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    labels = ["5 月", "8 月底", "9 月底", "10 月底"]
    xs = [0, 1, 2, 3]
    fleet = [315, 372, 395, 419]
    data = [2.0, 2.3, 2.4, 2.6]

    ax.plot(xs, fleet, color=NAVY, linewidth=2.8, marker="o", markersize=8,
            markerfacecolor="white", markeredgewidth=2.2, markeredgecolor=NAVY,
            zorder=3)
    ax2.plot(xs, data, color=RED, linewidth=2.4, marker="s", markersize=7,
             markerfacecolor="white", markeredgewidth=2.0, markeredgecolor=RED,
             linestyle=(0, (5, 2.5)), zorder=3)

    for i, (x, v) in enumerate(zip(xs, fleet)):
        off = (-11, 9) if i == 0 else (0, 13)
        al = "right" if i == 0 else "center"
        ax.annotate(f"{v}", xy=(x, v), xytext=off, textcoords="offset points",
                    fontsize=12, color=NAVY, weight="bold", ha=al)
    for i, (x, v) in enumerate(zip(xs, data)):
        off = (14, -14) if i == 0 else (0, -20)
        al = "left" if i == 0 else "center"
        ax2.annotate(f"{v:.1f}", xy=(x, v), xytext=off, textcoords="offset points",
                     fontsize=11.5, color=RED, weight="bold", ha=al)

    ax.set_xlim(-0.35, 3.45)
    ax.set_ylim(280, 450)
    ax2.set_ylim(1.7, 3.0)
    ax.set_xticks(xs)
    ax.set_xticklabels(labels, fontsize=11)
    ax.set_yticks([300, 350, 400, 450])
    ax2.set_yticks([1.8, 2.2, 2.6, 3.0])
    ax.tick_params(colors=NAVY, labelsize=10.5, length=0)
    ax2.tick_params(colors=RED, labelsize=10.5, length=0)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(NAVY)
    ax.spines["bottom"].set_color(LIGHT)
    ax2.spines["top"].set_visible(False)
    ax2.spines["left"].set_visible(False)
    ax2.spines["right"].set_color(RED)
    ax2.spines["bottom"].set_visible(False)
    ax.set_ylabel("保有量（万辆）", fontsize=10.5, color=NAVY, labelpad=10)
    ax2.set_ylabel("日生成数据（亿公里）", fontsize=10.5, color=RED, labelpad=12)
    ax.grid(axis="y", color=LIGHT, linewidth=0.8, alpha=0.55)
    ax.set_axisbelow(True)

    ax.text(0.02, 0.06, "半年净增 104 万辆，平均每月约 20 万台",
            transform=ax.transAxes, fontsize=10, color=GRAY, va="center")

    punchline(fig, "规模不是买来的，是卖出来的——所以别人很难一夜追上。")
    footer(fig, "据比亚迪 2026 年 5 月、8 月底、9 月底、10 月底四次公布口径。")
    fig.savefig(OUT + "图2_半年曲线.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.150, 0.930, 0.680])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "三把尺子：三个数字，量的不是同一个东西", fontsize=18,
             color=DARK, weight="bold", ha="left", va="top")
    fig.text(0.045, 0.882, "把它们放进同一张图比大小，是在比较苹果和橘子",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    cards = [
        ("比亚迪", "2.6", "亿公里 / 天", "口径：生成的数据\n（含采集与存储，非激活里程）", NAVY),
        ("华为乾崑", "14.8", "亿公里 / 月", "口径：辅助驾驶激活里程\n（累计 172.7 亿公里）", SLATE),
        ("特斯拉", "160", "亿公里（累计）", "口径：累计 FSD 里程\n（行业汇总，截至 2026 年 5 月）", RED),
    ]

    cw, gap = 0.290, 0.030
    for i, (name, big, unit, note, color) in enumerate(cards):
        x0 = 0.010 + i * (cw + gap)
        ax.add_patch(Rectangle((x0, 0.270), cw, 0.565, facecolor=PALE,
                               edgecolor=LIGHT, linewidth=1.0))
        ax.add_patch(Rectangle((x0, 0.822), cw, 0.013, facecolor=color, edgecolor="none"))

        ax.text(x0 + 0.024, 0.770, name, fontsize=12.5, color=color, weight="bold",
                va="center")
        ax.text(x0 + 0.024, 0.640, big, fontsize=40, color=color, weight="bold",
                va="center", ha="left")
        ax.text(x0 + 0.024, 0.545, unit, fontsize=11.5, color=DARK, va="center")
        ax.plot([x0 + 0.024, x0 + cw - 0.024], [0.500, 0.500], color=LIGHT,
                linewidth=1.0)
        ax.text(x0 + 0.024, 0.452, note, fontsize=9.8, color=GRAY, va="top",
                linespacing=1.7)

        ax.text(x0 + cw / 2, 0.312, "不可直接比较", fontsize=10.2, color=color,
                weight="bold", ha="center", va="center",
                bbox=dict(boxstyle="round,pad=0.4", facecolor="white",
                          edgecolor=color, linewidth=1.1))

    ax.text(0.010, 0.185, "规模是真的，但把规模转成能力的比率，没有人公布。",
            fontsize=11, color=DARK, ha="left", va="center")

    footer(fig, "据比亚迪 2026-11-14 公布数据、华为乾崑 2026 年 10 月智驾报告；特斯拉数据为行业汇总口径。")
    fig.savefig(OUT + "图3_三把尺子.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")
