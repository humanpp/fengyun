# -*- coding: utf-8 -*-
"""
《李斌呼吁给车重设限：车重 1.2 倍，道路破坏 2.07 倍》配套图表
事实口径：蔚来李斌在乌镇论坛上呼吁国家层面给车重设限，援引道路工程"四次方法则"：
车重达到 1.2 倍，对道路的破坏为 2.07 倍；部分车型电池包容量堆到 120 度、重量达
七八百公斤。该表态时间略早于本窗口，与 11 月 17 日蔚来因账款调研盘中跌超 5%
形成同一条"反内卷"线索的不同侧面：车重是产品定义端的无序堆料，账期是资金链端
的压力转移，两者都是整车环节在利润约束下寻找缓冲空间的表现形式。
风格：克制传媒风，白底、低饱和配色、标题即结论
输出目录 = 脚本所在目录
"""
import os
import numpy as np
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
    ax = fig.add_axes([0.100, 0.255, 0.855, 0.560])

    fig.text(0.045, 0.955, "为什么是 2.07 倍", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.888, "道路工程的「四次方法则」：破坏程度按车重的四次方增长",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    xs = np.linspace(1.0, 1.5, 240)
    ax.plot(xs, xs ** 4, color=NAVY, linewidth=2.6, solid_capstyle="round")

    # 基准点
    ax.scatter([1.0], [1.0], s=110, facecolor=SLATE, edgecolor="white",
               linewidth=2.0, zorder=4)
    ax.text(1.008, 0.62, "1.0 倍：基准", fontsize=9.4, color=SLATE, va="center")

    # 1.2 倍处
    ax.plot([1.2, 1.2], [0, 2.0736], color=RED, linewidth=1.2,
            linestyle=(0, (3, 3)))
    ax.plot([1.0, 1.2], [2.0736, 2.0736], color=RED, linewidth=1.2,
            linestyle=(0, (3, 3)))
    ax.scatter([1.2], [2.0736], s=150, facecolor=RED, edgecolor="white",
               linewidth=2.2, zorder=5)
    ax.text(1.218, 1.62, "1.2⁴ ≈ 2.07", fontsize=13, color=RED, weight="bold",
            va="center", ha="left")

    ax.set_xlim(1.0, 1.5)
    ax.set_ylim(0, 5.2)
    ax.set_xticks([1.0, 1.1, 1.2, 1.3, 1.4, 1.5])
    ax.set_xticklabels(["1.0", "1.1", "1.2", "1.3", "1.4", "1.5"], fontsize=9.5,
                       color=GRAY)
    ax.set_yticks([0, 1, 2, 3, 4, 5])
    ax.set_yticklabels(["0", "1", "2", "3", "4", "5 倍"], fontsize=9.5,
                       color=GRAY)
    ax.set_xlabel("车重（相对基准的倍数）", fontsize=9.8, color=SLATE,
                  labelpad=8)
    ax.set_ylabel("道路破坏程度（倍数）", fontsize=9.8, color=SLATE,
                  labelpad=8)

    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(LIGHT)
    ax.tick_params(axis="both", length=0, pad=6)
    ax.grid(color=LIGHT, linewidth=0.8, alpha=0.7)
    ax.set_axisbelow(True)

    punchline(fig, "车重多两成，路面多受一倍的罪。")
    footer(fig, "曲线按「四次方法则」（破坏 ∝ 轴重⁴）绘制；1.2⁴≈2.0736 与李斌在乌镇论坛援引的 2.07 倍一致。")
    fig.savefig(OUT + "图1_四次方法则.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.135, 0.910, 0.690])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "越堆越重的那个圈", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.888, "部分车型电池包容量堆到 120 度、重量达七八百公斤",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    steps = [
        ("01", "加大电池", "容量往上堆\n120 度、七八百公斤"),
        ("02", "车变更重", "同平台同尺寸\n整备质量上浮"),
        ("03", "能耗上升", "车重吃电\n单位里程耗电增加"),
        ("04", "续航焦虑", "账面续航不够\n回头再加电池"),
    ]

    w, gap = 0.212, 0.038
    y0, h = 0.420, 0.230
    for i, (no, title, body) in enumerate(steps):
        x0 = 0.020 + i * (w + gap)
        color = RED if i == 3 else NAVY
        ax.add_patch(Rectangle((x0, y0), w, h, facecolor=PALE,
                               edgecolor=LIGHT, linewidth=1.0))
        ax.add_patch(Rectangle((x0, y0 + h - 0.012), w, 0.012, facecolor=color,
                               edgecolor="none"))
        ax.text(x0 + 0.022, y0 + h - 0.058, no, fontsize=11, color=GRAY,
                weight="bold", va="center")
        ax.text(x0 + 0.022, y0 + h - 0.115, title, fontsize=12.5, color=color,
                weight="bold", va="center")
        ax.text(x0 + 0.022, y0 + 0.062, body, fontsize=8.8, color=DARK,
                va="center", linespacing=1.7)

        if i < len(steps) - 1:
            ax.annotate("", xy=(x0 + w + gap - 0.004, y0 + h / 2),
                        xytext=(x0 + w + 0.004, y0 + h / 2),
                        arrowprops=dict(arrowstyle="-|>", color=GRAY,
                                        linewidth=1.4, shrinkA=0, shrinkB=0))

    # 回环箭头
    x_last = 0.020 + 3 * (w + gap) + w / 2
    x_first = 0.020 + w / 2
    ax.plot([x_last, x_last], [y0, 0.320], color=RED, linewidth=1.5)
    ax.plot([x_last, x_first], [0.320, 0.320], color=RED, linewidth=1.5)
    ax.annotate("", xy=(x_first, y0 - 0.004), xytext=(x_first, 0.324),
                arrowprops=dict(arrowstyle="-|>", color=RED, linewidth=1.5,
                                shrinkA=0, shrinkB=0))

    ax.text(0.500, 0.262, "循环的起点不是技术，是「续航数字要好看」", fontsize=9.8,
            color=RED, ha="center", va="center")

    punchline(fig, "每一轮都解决了问题，也把问题推给下一轮。")
    footer(fig, "据「部分车型电池包 120 度、重七八百公斤」口径整理；循环链条为作者据行业常见做法所作归纳。")
    fig.savefig(OUT + "图2_堆料循环.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.135, 0.910, 0.690])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "同一个约束，两个出口", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.888, "利润薄的时候，压力总得找地方放",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    top, bot = 0.780, 0.330

    panels = [
        (0.020, "产品端：堆料", NAVY, [
            ("表现", "车越做越重，电池越堆越大"),
            ("代价", "道路破坏按四次方放大"),
            ("现状", "李斌呼吁国家层面设限"),
        ]),
        (0.530, "资金端：占款", RED, [
            ("表现", "账期越拖越长，票据替代现金"),
            ("代价", "压力转给供应商"),
            ("现状", "17 家车企账期进入年度抽查"),
        ]),
    ]

    for x0, title, color, rows in panels:
        ax.add_patch(Rectangle((x0, bot), 0.450, top - bot, facecolor=PALE,
                               edgecolor=LIGHT, linewidth=1.0))
        ax.add_patch(Rectangle((x0, top - 0.013), 0.450, 0.013, facecolor=color,
                               edgecolor="none"))
        ax.text(x0 + 0.030, top - 0.065, title, fontsize=13, color=color,
                weight="bold", va="center")
        for i, (label, value) in enumerate(rows):
            y = 0.640 - i * 0.115
            ax.text(x0 + 0.030, y, label, fontsize=9.2, color=GRAY,
                    va="center")
            ax.text(x0 + 0.030, y - 0.050, value, fontsize=10.4, color=DARK,
                    weight="bold", va="center")

    # 底部合流
    ax.annotate("", xy=(0.500, 0.284), xytext=(0.245, 0.324),
                arrowprops=dict(arrowstyle="-", color=GRAY, linewidth=1.4,
                                shrinkA=0, shrinkB=0,
                                connectionstyle="arc3,rad=-0.15"))
    ax.annotate("", xy=(0.500, 0.284), xytext=(0.755, 0.324),
                arrowprops=dict(arrowstyle="-", color=GRAY, linewidth=1.4,
                                shrinkA=0, shrinkB=0,
                                connectionstyle="arc3,rad=0.15"))
    ax.annotate("", xy=(0.500, 0.246), xytext=(0.500, 0.288),
                arrowprops=dict(arrowstyle="-|>", color=GRAY, linewidth=1.4,
                                shrinkA=0, shrinkB=0))

    ax.text(0.500, 0.200, "都指向同一件事：整车环节在找缓冲，而缓冲正在被逐一识别",
            fontsize=10.2, color=DARK, ha="center", va="center")

    punchline(fig, "堆料和拖账，本质是同一个动作的两种形态。")
    footer(fig, "车重表态与账期抽查均属「反内卷」线索；账期细节见 11 月 17 日第 011 篇。蔚来 11 月 17 日盘中跌超 5%。")
    fig.savefig(OUT + "图3_两个出口.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")