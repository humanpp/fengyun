# -*- coding: utf-8 -*-
"""
《这一轮猪周期，剧本失灵了》配套图表
事实来源：第一财经 2026-11-09；国家统计局三季度生猪与能繁母猪数据；
同花顺财经 2026-11-11（PSY、均重、冻品库容率、卓创预测）
风格：克制传媒风，白底、低饱和配色、标题即结论
输出目录 = 脚本所在目录
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["figure.facecolor"] = "white"
plt.rcParams["axes.facecolor"] = "white"

NAVY = "#1f3a5f"
RED = "#b5544a"
GRAY = "#8a8f98"
LIGHT = "#d8dbe0"
DARK = "#2b2f36"
PALE = "#eef0f3"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep


def footer(fig, text):
    fig.text(0.045, 0.020, text, fontsize=8.4, color=GRAY, ha="left", va="bottom")


def takeaway(fig, y, text, size=10.4):
    fig.text(0.045, y, text, fontsize=size, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


# ---------------------------------------------------------------- 图 1
def fig1():
    fig, ax = plt.subplots(figsize=(12, 6.8))
    fig.subplots_adjust(left=0.045, right=0.955, top=0.750, bottom=0.180)

    fig.suptitle("老剧本四幕，前三幕都演了，第四幕没来",
                 fontsize=19, color=DARK, x=0.045, ha="left", y=0.955, weight="bold")
    fig.text(0.045, 0.878,
             "二十年不变的猪周期逻辑，这一轮走到第三步就停住了",
             fontsize=10.8, color=GRAY, ha="left")

    ax.set_xlim(0, 1)
    ax.set_ylim(0.20, 4.55)
    ax.axis("off")

    acts = [
        ("第一幕", "猪价跌破成本线", "8.63 元/公斤，近十年新低", NAVY, "已发生", True),
        ("第二幕", "养殖户撑不住，去产能", "能繁母猪 3602 万头，降至保有量 96.0%", NAVY, "已发生", True),
        ("第三幕", "供给减少，价格反弹", "三个对冲把减量吃掉了 →", RED, "卡在这里", False),
        ("第四幕", "大家回来养猪，再度过剩", "—— 本轮尚未进入 ——", GRAY, "未发生", None),
    ]

    for i, (act, title, note, color, status, done) in enumerate(acts):
        y = 4.02 - i * 1.02
        ax.add_patch(plt.Rectangle((0.030, y - 0.40), 0.830, 0.80,
                                   facecolor=PALE, edgecolor=color, linewidth=1.3))
        ax.add_patch(plt.Rectangle((0.030, y - 0.40), 0.007, 0.80,
                                   facecolor=color, edgecolor="none"))
        ax.text(0.058, y + 0.20, act, fontsize=9.6, color=GRAY, va="center")
        ax.text(0.058, y - 0.08, title, fontsize=12.5, color=DARK,
                weight="bold", va="center")
        ax.text(0.058, y - 0.30, note, fontsize=9.2, color=GRAY, va="center")

        # 状态标记：用汉字文字代替符号（雅黑缺 ✓/✕ 字形）
        if done is True:
            ax.text(0.795, y, "已", fontsize=12, color="white", ha="center",
                    va="center", weight="bold", zorder=5,
                    bbox=dict(boxstyle="circle,pad=0.32", facecolor=color,
                              edgecolor="none"))
        elif done is False:
            ax.text(0.795, y, "止", fontsize=12, color=color, ha="center",
                    va="center", weight="bold", zorder=5,
                    bbox=dict(boxstyle="circle,pad=0.32", facecolor="white",
                              edgecolor=color, linewidth=1.8))
        else:
            ax.text(0.795, y, "待", fontsize=12, color=GRAY, ha="center",
                    va="center", weight="bold", zorder=5,
                    bbox=dict(boxstyle="circle,pad=0.32", facecolor="white",
                              edgecolor=LIGHT, linewidth=1.4))
        ax.text(0.905, y, status, fontsize=10, color=color, ha="center",
                va="center", weight="bold")

    fig.text(0.045, 0.088,
             "老剧本的第三步失效了——产能确实在去，但价格没有跟着涨。",
             fontsize=10.4, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))

    footer(fig, "数据：第一财经 2026-11-09；国家统计局三季度末能繁母猪存栏数据。")
    fig.savefig(OUT + "图1_四幕剧本.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig, ax = plt.subplots(figsize=(12, 6.8))
    fig.subplots_adjust(left=0.045, right=0.955, top=0.750, bottom=0.180)

    fig.suptitle("三个“对冲”，把母猪减少带来的减量吃掉了",
                 fontsize=19, color=DARK, x=0.045, ha="left", y=0.955, weight="bold")
    fig.text(0.045, 0.878,
             "能繁母猪同比 -10.7%，但最终供给没有同比例下降——原因在这三处",
             fontsize=10.6, color=GRAY, ha="left")

    ax.set_xlim(0, 1)
    ax.set_ylim(0.20, 4.55)
    ax.axis("off")

    cards = [
        ("效率", "PSY 提升到 28 左右", "每头母猪年产仔更多，\n对冲母猪数量下降的减量", NAVY),
        ("体重", "均重 125.42 公斤，同比偏高", "压栏等价格，单头出肉更多，\n供给往后退一步", RED),
        ("库存", "冻品库容率 31.9%—32.2%", "同比高约 14 个百分点，\n现货一反弹冻品就出来平抑", RED),
    ]

    for i, (name, big, desc, color) in enumerate(cards):
        x0 = 0.030 + i * 0.325
        ax.add_patch(plt.Rectangle((x0, 1.85), 0.290, 2.50,
                                   facecolor=PALE, edgecolor=LIGHT, linewidth=1.0))
        ax.add_patch(plt.Rectangle((x0, 4.23), 0.290, 0.12,
                                   facecolor=color, edgecolor="none"))
        ax.text(x0 + 0.145, 3.92, name, fontsize=16, color=color,
                weight="bold", ha="center")
        ax.text(x0 + 0.145, 3.42, big, fontsize=10.4, color=DARK,
                ha="center", va="center", linespacing=1.6)
        ax.text(x0 + 0.145, 2.55, desc, fontsize=9.2, color=GRAY,
                ha="center", va="center", linespacing=1.8)

    ax.add_patch(plt.Rectangle((0.115, 0.85), 0.770, 0.72,
                               facecolor="white", edgecolor=DARK, linewidth=1.3))
    ax.text(0.500, 1.21, "母猪少了 10.7%，商品猪的减量却没那么多", fontsize=12,
            color=DARK, ha="center", va="center", weight="bold")

    footer(fig, "数据：同花顺财经 2026-11-11 引行业监测；国家统计局三季度末能繁母猪存栏 3602 万头（同比 -10.7%）。")
    fig.savefig(OUT + "图2_三个对冲.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig, ax = plt.subplots(figsize=(12, 6.8))
    fig.subplots_adjust(left=0.045, right=0.955, top=0.750, bottom=0.175)

    fig.suptitle("产能去化到价格反弹，中间隔着 10 到 12 个月",
                 fontsize=19, color=DARK, x=0.045, ha="left", y=0.955, weight="bold")
    fig.text(0.045, 0.878,
             "这决定了 2027 年等来的是“拐点”，而不是“暴涨”",
             fontsize=10.8, color=GRAY, ha="left")

    ax.set_xlim(0, 1)
    ax.set_ylim(0.85, 3.90)
    ax.axis("off")

    # 时间轴
    ax.plot([0.10, 0.92], [2.15, 2.15], color=LIGHT, lw=2.6, zorder=1)

    nodes = [
        (0.10, "2026 Q3", "能繁母猪 3602 万头", "为正常保有量 96.0%，\n两年半来首次跌破红线", NAVY, "上"),
        (0.51, "2027 Q2", "商品猪出栏明显收缩", "母猪减少传导到肥猪出栏", NAVY, "下"),
        (0.92, "2027 H1", "周期拐点", "卓创：2027 年均价\n或在 12.0—12.5 元/公斤", RED, "上"),
    ]

    for x, tag, title, note, color, side in nodes:
        ax.scatter([x], [2.15], s=135, facecolor=color, edgecolor="white",
                   linewidth=1.8, zorder=5)
        if side == "上":
            ax.text(x, 3.42, tag, fontsize=10, color=GRAY, ha="center")
            ax.text(x, 3.12, title, fontsize=11.8, color=DARK,
                    weight="bold", ha="center")
            ax.text(x, 2.80, note, fontsize=9.2, color=color,
                    ha="center", va="top", linespacing=1.7)
        else:
            ax.text(x, 1.86, tag, fontsize=10, color=GRAY, ha="center")
            ax.text(x, 1.56, title, fontsize=11.8, color=DARK,
                    weight="bold", ha="center")
            ax.text(x, 1.24, note, fontsize=9.2, color=color,
                    ha="center", va="top")

    # 两段传导区间标注
    ax.text(0.305, 2.34, "10—12 个月传导期", fontsize=9.8, color=NAVY,
            ha="center", weight="bold")
    ax.text(0.715, 2.34, "去化 → 价格", fontsize=9.8, color=RED,
            ha="center", weight="bold")

    fig.text(0.045, 0.088,
             "是拐点，不是暴涨：等来的价格大致就落在成本线附近。",
             fontsize=10.4, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))

    footer(fig, "数据：国家统计局三季度末能繁母猪存栏；机构一致预期与卓创资讯 2027 年均价预测，经同花顺财经转述。")
    fig.savefig(OUT + "图3_传导时间差.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")