# -*- coding: utf-8 -*-
"""
《华为 Mate X8 定档 11 月 24 日：三代同价 12999，这次可能要破了》配套图表
事实来源：华为终端 2026-11-16 官宣 Mate X8 定档 11/24 14:30、官网五款配色与
四档存储、价格"暂无报价"；Mate X5/X6/X7 起售价均 12,999 元；Counterpoint
存储涨价与 BOM 内存占比数据
风格：克制传媒风，白底、低饱和配色、标题即结论
输出目录 = 脚本所在目录
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch

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


def bare(ax, axis="y"):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(LIGHT)
    ax.tick_params(colors=DARK, labelsize=10.5, length=0)
    ax.set_axisbelow(True)
    ax.grid(axis=axis, color=LIGHT, linewidth=0.8, alpha=0.55)


# ---------------------------------------------------------------- 图 1
def fig1():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.135, 0.930, 0.690])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "哪些是官方说的，哪些还是爆料", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.882, "发布会前最该分清的一件事",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    panels = [
        (0.012, "官方已确认", NAVY, "华为终端 / 官网 / 余承东表态", [
            "发布日：11 月 24 日 14:30",
            "五款配色：紫金锦、青云锦、丹霞锦、雪域白、苍穹黑",
            "三款织金云锦纹理背板，两款纯色",
            "四档存储：12+256 至 16+512、1TB 典藏",
            "圆形星环镜头模组回归、鎏光腰线",
            "更轻更薄更宽，内外屏尺寸均增大",
        ]),
        (0.508, "仍是爆料", RED, "第三方渠道，未经华为确认", [
            "外屏 6.5 英寸、内屏 8.15 英寸",
            "麒麟 9050 Pro",
            "超 6000mAh 硅碳负极电池",
            "第三代红枫影像：5000 万像素",
            "1/1.28 英寸 RYYB、物理可变光圈",
            "全新分布式散热系统",
        ]),
    ]

    for x0, title, color, sub, items in panels:
        ax.add_patch(FancyBboxPatch((x0, 0.075), 0.480, 0.700,
                                    boxstyle="round,pad=0.010,rounding_size=0.012",
                                    facecolor=PALE, edgecolor=LIGHT, linewidth=1.0))
        ax.add_patch(Rectangle((x0, 0.760), 0.480, 0.015, facecolor=color,
                               edgecolor="none"))
        ax.text(x0 + 0.022, 0.700, title, fontsize=14.5, color=color,
                weight="bold", va="center")
        ax.text(x0 + 0.022, 0.648, sub, fontsize=9.4, color=GRAY, va="center")

        for i, line in enumerate(items):
            y = 0.578 - i * 0.075
            ax.text(x0 + 0.024, y, "·", fontsize=12, color=color, va="center")
            ax.text(x0 + 0.042, y, line, fontsize=10.3, color=DARK, va="center")

    ax.text(0.012, 0.030, "官网价格栏目前写的是「暂无报价」——参数可以爆料，价格只能等。",
            fontsize=10.6, color=DARK, ha="left", va="center")

    footer(fig, "据华为终端 2026-11-16 官宣、华为商城产品页、IT之家、太平洋科技、新浪科技；爆料部分已注明未经确认。")
    fig.savefig(OUT + "图1_官宣与爆料.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.085, 0.210, 0.885, 0.545])

    fig.text(0.045, 0.955, "三代同价 12,999，第四代还是问号", fontsize=19,
             color=DARK, weight="bold", ha="left", va="top")
    fig.text(0.045, 0.882, "华为 Mate X 系列起售价（元，12+256 版本）",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    bare(ax)
    xs = [0, 1, 2, 3]
    labels = ["Mate X5\n2023 年 9 月", "Mate X6\n2024 年 11 月",
              "Mate X7\n2025 年 11 月", "Mate X8\n2026 年 11 月 24 日"]
    vals = [12999, 12999, 12999]

    ax.bar(xs[:3], vals, width=0.46, color=NAVY, edgecolor="none")
    for x, v in zip(xs[:3], vals):
        ax.text(x, v + 260, "12,999", fontsize=13, color=DARK, ha="center",
                va="bottom", weight="bold")

    # X8：未知，画成虚线轮廓
    ax.bar([3], [12999], width=0.46, facecolor="none", edgecolor=RED,
           linewidth=2.0, linestyle=(0, (5, 3)))
    ax.text(3, 12999 / 2, "？", fontsize=30, color=RED, ha="center",
            va="center", weight="bold")
    ax.text(3, 12999 + 260, "待 11 月 24 日", fontsize=11.5, color=RED,
            ha="center", va="bottom", weight="bold")

    ax.axhline(12999, color=SLATE, linewidth=1.2, linestyle=(0, (4, 3)), alpha=0.85)
    ax.text(-0.42, 12999 + 900, "三代持平", fontsize=10.6, color=SLATE,
            ha="left", va="bottom")

    ax.set_ylim(0, 17200)
    ax.set_xlim(-0.62, 3.62)
    ax.set_xticks(xs)
    ax.set_xticklabels(labels, fontsize=10.6, linespacing=1.7)
    ax.set_yticks([0, 5000, 10000, 15000])
    ax.set_yticklabels(["0", "5,000", "10,000", "15,000"])

    punchline(fig, "不是「会不会涨」，是「凭什么不涨」——存储成本已经翻了一轮。")
    footer(fig, "据凤凰网（X5）、IT之家（X6、X7）公开发布价；X8 价格华为商城显示「暂无报价」。")
    fig.savefig(OUT + "图2_三代同价.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.100, 0.215, 0.845, 0.545])

    fig.text(0.045, 0.955, "存储变成了旗舰机最贵的那一块", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.882, "内存占 iPhone Pro 256GB 机型 BOM 成本的比重",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    bare(ax)
    xs = [0, 1, 2]
    labels = ["一年前", "2026 年 Q3", "2027 年上半年\n（预计）"]
    vals = [10, 34, 40]

    ax.plot(xs, vals, color=RED, linewidth=3.0, marker="o", markersize=10,
            markerfacecolor="white", markeredgewidth=2.4, markeredgecolor=RED,
            zorder=3)
    for x, v in zip(xs, vals):
        txt = f"{v}%" if v != 40 else "突破 40%"
        ax.text(x, v + 2.6, txt, fontsize=13.5, color=DARK, ha="center",
                va="bottom", weight="bold")

    ax.set_ylim(0, 56)
    ax.set_xlim(-0.40, 2.40)
    ax.set_xticks(xs)
    ax.set_xticklabels(labels, fontsize=11, linespacing=1.7)
    ax.set_yticks([0, 10, 20, 30, 40, 50])
    ax.set_yticklabels(["0", "10%", "20%", "30%", "40%", "50%"])
    ax.grid(axis="y", color=LIGHT, linewidth=0.8, alpha=0.55)

    ax.text(0.030, 0.905,
            "2026 年 Q1：DRAM 环比涨超 50%，NAND 涨超 90%\n"
            "2026 年 Q2：手机内存价格环比再涨超 80%，DRAM 已超过 SoC",
            transform=ax.transAxes, fontsize=10.2, color=DARK, ha="left",
            va="top", linespacing=1.9,
            bbox=dict(boxstyle="round,pad=0.55", facecolor=PALE,
                      edgecolor=LIGHT, linewidth=0.9))

    punchline(fig, "当内存比处理器还贵，旗舰的定价就不再由自己说了算。")
    footer(fig, "据 Counterpoint Research（经 IT之家、中央社转述）；40% 为 2027 年上半年预测值。")
    fig.savefig(OUT + "图3_存储成本.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")