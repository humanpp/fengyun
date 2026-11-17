# -*- coding: utf-8 -*-
"""
《82 亿美元，李飞飞入职 AMD：芯片巨头不只卖算力，开始买「空间智能」》配套图表
事实口径：AMD 于 2026 年 11 月 16 日正式完成对空间智能公司 World Labs 的收购，
约 82 亿美元全股票交易，原定 2026 年底前交割、实际提前完成；World Labs 专注
创建和模拟交互式 3D 环境的 AI 模型，以及机器人学习与仿真技术；创始人李飞飞
即日起出任 AMD 执行副总裁兼首席科学家，直接向苏姿丰汇报。
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
    ax = fig.add_axes([0.045, 0.135, 0.910, 0.690])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "82 亿美元，全股票，提前完成", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.888, "AMD 收购 World Labs，2026 年 11 月 16 日完成交割",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    ax.text(0.030, 0.680, "82", fontsize=58, color=RED, weight="bold",
            ha="left", va="center")
    ax.text(0.180, 0.680, "亿美元", fontsize=20, color=RED, weight="bold",
            ha="left", va="center")
    ax.text(0.030, 0.560, "全股票交易，不占用现金", fontsize=11, color=SLATE,
            ha="left", va="center")

    ax.plot([0.037, 0.037], [0.430, 0.510], color=RED, linewidth=2.4,
            solid_capstyle="round")
    ax.text(0.060, 0.470, "成交结构：以 AMD 股票支付", fontsize=9.8, color=DARK,
            va="center")

    # 时间线
    ax.plot([0.100, 0.800], [0.280, 0.280], color=LIGHT, linewidth=2.2,
            solid_capstyle="round", zorder=1)

    ax.scatter([0.120], [0.280], s=260, facecolor=SLATE, edgecolor="white",
               linewidth=2.0, zorder=3)
    ax.scatter([0.760], [0.280], s=260, facecolor=RED, edgecolor="white",
               linewidth=2.0, zorder=3)

    ax.text(0.120, 0.362, "原定 2026 年底前交割", fontsize=9.6, color=GRAY,
            ha="center", va="center")
    ax.text(0.760, 0.362, "实际 11 月 16 日完成", fontsize=9.6, color=RED,
            ha="center", va="center")

    ax.annotate("", xy=(0.735, 0.280), xytext=(0.145, 0.280),
                arrowprops=dict(arrowstyle="-|>", color=RED, linewidth=1.3,
                                shrinkA=0, shrinkB=0))
    ax.text(0.440, 0.196, "提前约六周", fontsize=10.6, color=RED, weight="bold",
            ha="center", va="center")

    punchline(fig, "不是买一个模型，是买一个把算力变成需求的接口。")
    footer(fig, "据 AMD 2026 年 11 月 16 日完成收购的公开口径整理；「提前约六周」为按「年底前」与 11 月 16 日所做推算。")
    fig.savefig(OUT + "图1_交易三要素.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.135, 0.910, 0.690])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "直报 CEO 的位置", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.888, "李飞飞任执行副总裁兼首席科学家，向苏姿丰汇报",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    ax.add_patch(Rectangle((0.330, 0.680), 0.340, 0.140, facecolor=PALE,
                           edgecolor=LIGHT, linewidth=1.0))
    ax.add_patch(Rectangle((0.330, 0.807), 0.340, 0.013, facecolor=NAVY,
                           edgecolor="none"))
    ax.text(0.500, 0.775, "苏姿丰", fontsize=14, color=NAVY, weight="bold",
            ha="center", va="center")
    ax.text(0.500, 0.716, "AMD 董事长兼 CEO", fontsize=9.4, color=GRAY,
            ha="center", va="center")

    ax.annotate("", xy=(0.500, 0.575), xytext=(0.500, 0.665),
                arrowprops=dict(arrowstyle="-|>", color=GRAY, linewidth=1.5,
                                shrinkA=0, shrinkB=0))
    ax.text(0.520, 0.620, "直接汇报", fontsize=9.2, color=GRAY, ha="left",
            va="center")

    ax.add_patch(Rectangle((0.240, 0.430), 0.520, 0.140, facecolor=PALE,
                           edgecolor=LIGHT, linewidth=1.0))
    ax.add_patch(Rectangle((0.240, 0.557), 0.520, 0.013, facecolor=RED,
                           edgecolor="none"))
    ax.text(0.500, 0.512, "李飞飞", fontsize=15, color=RED, weight="bold",
            ha="center", va="center")
    ax.text(0.500, 0.458, "执行副总裁兼首席科学家", fontsize=10.4, color=DARK,
            ha="center", va="center")

    ax.text(0.500, 0.360, "World Labs 团队与空间智能研究随交易并入", fontsize=9.6,
            color=GRAY, ha="center", va="center")

    ax.plot([0.120, 0.880], [0.295, 0.295], color=LIGHT, linewidth=1.0)
    ax.text(0.500, 0.225, "挂在事业部下面，是产品投入；挂在 CEO 下面，是战略投入",
            fontsize=10.6, color=DARK, ha="center", va="center")

    punchline(fig, "汇报线，就是优先级。")
    footer(fig, "据 AMD 2026 年 11 月 16 日人事任命口径整理；「产品投入／战略投入」为作者判断。")
    fig.savefig(OUT + "图2_组织位置.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.135, 0.910, 0.690])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "从第一层买到第三层", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.888, "芯片公司的竞争，正在从卖算力往上延伸",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    layers = [
        ("层三", "模型层：空间智能与仿真", "新买 · 82 亿美元", RED),
        ("层二", "软件栈与工具链", "AMD 在补", SLATE),
        ("层一", "算力硬件（CPU / GPU）", "AMD 主营", NAVY),
    ]

    h = 0.150
    for i, (tag, name, status, color) in enumerate(layers):
        cy = 0.730 - i * 0.195
        ax.add_patch(Rectangle((0.040, cy - h / 2), 0.920, h, facecolor=PALE,
                               edgecolor=LIGHT, linewidth=1.0))
        ax.add_patch(Rectangle((0.040, cy - h / 2), 0.012, h, facecolor=color,
                               edgecolor="none"))
        ax.text(0.075, cy + 0.036, tag, fontsize=9.2, color=GRAY, va="center")
        ax.text(0.075, cy - 0.036, name, fontsize=13, color=DARK, weight="bold",
                va="center")
        ax.text(0.925, cy, status, fontsize=11.6, color=color, weight="bold",
                ha="right", va="center")

    ax.text(0.040, 0.200, "越往上，越接近「谁来决定买谁的芯片」", fontsize=9.6,
            color=GRAY, va="center")

    punchline(fig, "卖铲子的人开始买需求，说明铲子已经不够卖了。")
    footer(fig, "据 AMD 收购与人事公告整理；三层划分为作者为说明竞争位置所做，非公司口径。")
    fig.savefig(OUT + "图3_三层能力.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")
