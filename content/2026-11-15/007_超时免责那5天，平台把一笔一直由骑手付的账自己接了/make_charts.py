# -*- coding: utf-8 -*-
"""
《超时免责那 5 天，平台把一笔一直由骑手付的账，自己接了》配套图表
事实来源：深圳特区报·读特 2026-11-13 报道；深圳市公安局 APEC 交通管控通告
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
    fig.subplots_adjust(left=0.045, right=0.955, top=0.760, bottom=0.175)

    fig.suptitle("同一个超时，两个时间段，两个付账的人",
                 fontsize=19, color=DARK, x=0.045, ha="left", y=0.955, weight="bold")
    fig.text(0.045, 0.885,
             "免责这个动作的存在，本身就说明平时不免",
             fontsize=10.8, color=GRAY, ha="left")

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 4.55)
    ax.axis("off")

    panels = [
        (0.030, "平时（一年其余 360 天）", GRAY, [
            ("超时发生", "订单超过承诺时间"),
            ("后果", "影响收入、服务分、后续派单"),
            ("谁承担", "骑手"),
            ("平台动作", "按规则执行罚则"),
        ]),
        (0.530, "会期（11.16—11.20）", NAVY, [
            ("超时发生", "路封了，单还得送"),
            ("后果", "订单超时免责，不追罚"),
            ("谁承担", "平台"),
            ("平台动作", "免责 + 补贴 + 降负载"),
        ]),
    ]

    for x0, title, color, rows in panels:
        ax.add_patch(plt.Rectangle((x0, 0.72), 0.440, 3.42,
                                   facecolor=PALE, edgecolor=LIGHT, linewidth=1.0))
        ax.add_patch(plt.Rectangle((x0, 4.00), 0.440, 0.14,
                                   facecolor=color, edgecolor="none"))
        ax.text(x0 + 0.028, 3.66, title, fontsize=12, color=color,
                weight="bold", va="center")
        for i, (k, v) in enumerate(rows):
            y = 3.10 - i * 0.66
            ax.text(x0 + 0.028, y, k, fontsize=9.8, color=GRAY, va="center")
            ax.text(x0 + 0.150, y, v, fontsize=10.4, color=DARK, va="center")

    ax.text(0.500, 2.50, "→", fontsize=22, color=RED, ha="center",
            va="center", weight="bold")

    takeaway(fig, 0.082, "这是一次成本归属的临时转移，不是规则本身变了。")

    footer(fig, "据深圳特区报·读特 2026-11-13 报道整理；平时罚则为行业通行做法的一般描述。")
    fig.savefig(OUT + "图1_两个付账的人.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig, ax = plt.subplots(figsize=(12, 6.8))
    fig.subplots_adjust(left=0.045, right=0.955, top=0.760, bottom=0.175)

    fig.suptitle("三件事连起来，是一笔算过的账",
                 fontsize=19, color=DARK, x=0.045, ha="left", y=0.955, weight="bold")
    fig.text(0.045, 0.885,
             "单看每一条都是“善意”，合起来是一次风险与收入的重新分配",
             fontsize=10.8, color=GRAY, ha="left")

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 4.70)
    ax.axis("off")

    # 三块并排
    blocks = [
        (0.035, "免责", "免掉罚", "超时订单不追罚，\n取消订单在重点区域也免责", NAVY),
        (0.360, "降负载", "减少风险", "最高接单负载\n降低 2 至 3 单", RED),
        (0.685, "补贴", "补上收入", "跑单、调度、区域补贴\n＋积分保护", NAVY),
    ]

    for x0, name, sub, desc, color in blocks:
        ax.add_patch(plt.Rectangle((x0, 2.30), 0.280, 1.95,
                                   facecolor=PALE, edgecolor=LIGHT, linewidth=1.0))
        ax.add_patch(plt.Rectangle((x0, 4.13), 0.280, 0.12,
                                   facecolor=color, edgecolor="none"))
        ax.text(x0 + 0.140, 3.86, name, fontsize=15, color=color,
                weight="bold", ha="center")
        ax.text(x0 + 0.140, 3.50, sub, fontsize=10.6, color=DARK, ha="center")
        ax.text(x0 + 0.140, 2.93, desc, fontsize=9.4, color=GRAY,
                ha="center", va="center", linespacing=1.7)

    # 三条向下箭头指向结论
    for x in (0.175, 0.500, 0.825):
        ax.annotate("", xy=(x, 1.72), xytext=(x, 2.20),
                    arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=1.5))

    ax.add_patch(plt.Rectangle((0.115, 0.62), 0.770, 1.00,
                               facecolor="white", edgecolor=DARK, linewidth=1.3))
    ax.text(0.500, 1.32, "平台把平时由骑手承担的超时风险", fontsize=12,
            color=DARK, ha="center", va="center", weight="bold")
    ax.text(0.500, 0.90, "在这 5 天里接了过去", fontsize=13,
            color=RED, ha="center", va="center", weight="bold")

    footer(fig, "据美团 2026-11-13 骑手保障十项举措公开内容整理。")
    fig.savefig(OUT + "图2_一笔算过的账.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig, ax = plt.subplots(figsize=(12, 6.8))
    fig.subplots_adjust(left=0.075, right=0.940, top=0.755, bottom=0.215)

    fig.suptitle("5 天，和剩下的 360 天",
                 fontsize=19, color=DARK, x=0.045, ha="left", y=0.955, weight="bold")
    fig.text(0.045, 0.885,
             "把一年铺开看，5 天只占 1.4%——所以在整条上几乎看不见，必须放大",
             fontsize=10.8, color=GRAY, ha="left")

    ax.set_xlim(0, 365)
    ax.set_ylim(-0.35, 3.60)
    ax.axis("off")

    # 全年底条（5 天在这上面只有 1.4%，肉眼不可见）
    ax.barh(2.70, 365, height=0.42, color=LIGHT, edgecolor="white")
    ax.text(182, 2.70, "全年 365 天：按平台规则执行罚则",
            fontsize=11.5, color=DARK, ha="center", va="center")

    # 局部放大框：把 5 天放大成等宽 60 的示意条
    ax.add_patch(plt.Rectangle((3, 1.28), 150, 0.72,
                               facecolor="white", edgecolor=NAVY, linewidth=1.6))
    ax.barh(1.64, 150, height=0.30, color=NAVY, edgecolor="none")
    ax.text(78, 1.64, "11.16 — 11.20：免责 · 降负载 · 补贴",
            fontsize=10.6, color="white", ha="center", va="center", weight="bold")
    ax.text(3, 1.10, "↑ 放大后的 5 天（示意）", fontsize=9.4, color=NAVY)

    # 从原条引线到放大框
    ax.plot([3.5, 3.5], [2.48, 2.02], color=NAVY, lw=1.2, ls=(0, (4, 3)))
    ax.plot([3.5, 3.0], [2.02, 2.02], color=NAVY, lw=1.2, ls=(0, (4, 3)))

    # 时间刻度
    for d, label in [(0, "1 月"), (90, "4 月"), (182, "7 月"), (274, "10 月"), (365, "12 月")]:
        ax.plot([d, d], [2.40, 2.46], color=GRAY, lw=1.0)
        ax.text(d, 2.22, label, fontsize=9.6, color=GRAY, ha="center")

    # 对比数字
    ax.text(0, 0.35, "5", fontsize=44, color=NAVY, weight="bold", va="center")
    ax.text(24, 0.35, "天在免责", fontsize=13, color=DARK, va="center")
    ax.text(165, 0.35, "360", fontsize=44, color=RED, weight="bold", va="center")
    ax.text(228, 0.35, "天不免", fontsize=13, color=DARK, va="center")

    fig.text(0.045, 0.100,
             "它证明的不是平台有多好，而是默认设置可以改——改它需要一个足够大的理由。",
             fontsize=10.4, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))

    footer(fig, "示意：11 月 16—20 日为公开报道的免责时段，其余天数按常规规则执行；放大块宽度不代表实际比例。")
    fig.savefig(OUT + "图3_五天与三百六十天.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")