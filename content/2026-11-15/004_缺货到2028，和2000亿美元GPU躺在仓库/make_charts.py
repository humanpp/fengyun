# -*- coding: utf-8 -*-
"""
《缺货到 2028，和 2000 亿美元 GPU 躺在仓库》配套图表
事实来源：中芯国际 2026Q3 业绩报告及 11-13 业绩说明会；
《华尔街日报》2026-11-13 循环融资调查报道；Ed Zitron 公开估计
风格：克制传媒风，白底、低饱和配色、标题即结论
输出目录 = 脚本所在目录
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

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


def clean(ax, axis="y"):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(LIGHT)
    ax.tick_params(colors=DARK, labelsize=10.5, length=0)
    ax.set_axisbelow(True)
    ax.grid(axis=axis, color=LIGHT, linewidth=0.8, alpha=0.55)


# ---------------------------------------------------------------- 图 1
def fig1():
    fig, axes = plt.subplots(1, 3, figsize=(12, 6.8))
    fig.subplots_adjust(left=0.045, right=0.975, top=0.660, bottom=0.290, wspace=0.30)

    fig.suptitle("中芯三季度：三项指标同时越过指引上限",
                 fontsize=19, color=DARK, x=0.045, ha="left", y=0.955, weight="bold")
    fig.text(0.045, 0.880,
             "公司此前给的指引，全部被自己的实际数字超过",
             fontsize=10.6, color=GRAY, ha="left")

    panels = [
        ("销售毛利率", "26–28%", 28, 29.9, "%", 24, 32),
        ("收入环比增速", "2–4%", 4, 6.1, "%", 0, 8),
        ("产能利用率", "上季 93.7%", 93.7, 97.3, "%", 88, 100),
    ]

    for ax, (name, guide_txt, prev, actual, unit, ymin, ymax) in zip(axes, panels):
        ax.bar([0], [prev], width=0.54, color=LIGHT, label="指引上限 / 上季")
        ax.bar([1], [actual], width=0.54, color=NAVY, label="本季实际")
        ax.text(0, prev + (ymax - ymin) * 0.035, f"{prev:g}", ha="center",
                va="bottom", fontsize=13, color=GRAY)
        ax.text(1, actual + (ymax - ymin) * 0.035, f"{actual:g}", ha="center",
                va="bottom", fontsize=15, color=NAVY, weight="bold")

        ax.set_title(name, fontsize=12.5, color=DARK, pad=12, weight="bold")
        ax.set_xticks([0, 1])
        ax.set_xticklabels(["指引", "实际"], fontsize=10.5)
        ax.set_ylim(ymin, ymax)
        ax.set_xlim(-0.55, 1.55)

        # 只留左侧轴线，不做刻度干扰
        for s in ("top", "right", "left"):
            ax.spines[s].set_visible(False)
        ax.spines["bottom"].set_color(LIGHT)
        ax.set_yticks([])
        ax.tick_params(colors=DARK, length=0)
        ax.text(1.02, (ymin + ymax) / 2, "", fontsize=1)  # 占位
        ax.text(0.5, ymax - (ymax - ymin) * 0.10, guide_txt,
                ha="center", va="top", fontsize=9.6, color=GRAY)

    note = ("三季度收入 31.9 亿美元，同比 +33.9%；毛利率 29.9%，环比 +4.6pct；\n"
            "产能利用率 97.3%，环比 +3.6pct。前两项均超出公司指引区间上限。")
    fig.text(0.045, 0.155, note, fontsize=9.8, color=DARK, ha="left",
             va="center", linespacing=1.85,
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))

    footer(fig, "数据：中芯国际 2026 年第三季度业绩报告及 11 月 13 日业绩说明会。产能利用率无公开指引，故与上一季度对比。")
    fig.savefig(OUT + "图1_中芯三季报.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig, ax = plt.subplots(figsize=(12, 6.8))
    fig.subplots_adjust(left=0.045, right=0.955, top=0.765, bottom=0.175)

    fig.suptitle("两个方向的信号，可以同时为真",
                 fontsize=19, color=DARK, x=0.045, ha="left", y=0.955, weight="bold")
    fig.text(0.045, 0.888,
             "因为它们说的根本不是同一批芯片",
             fontsize=10.8, color=GRAY, ha="left")

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 4.60)
    ax.axis("off")

    panels = [
        (0.030, "供给端：造不出来", NAVY, [
            ("瓶颈", "先进制程、HBM、配套电源与控制器"),
            ("原因", "扩产周期长、良率爬坡慢"),
            ("时间", "钱砸下去也要 2–3 年"),
            ("含义", "结构性紧缺，短期无解"),
        ]),
        (0.530, "需求端：造出来用不上", RED, [
            ("现象", "特定型号堆在渠道与仓库"),
            ("原因", "缺电、缺终端付费需求"),
            ("规模", "约 2000 亿美元（Zitron 估计）"),
            ("含义", "价格支撑随库存释放而消失"),
        ]),
    ]

    for x0, title, color, rows in panels:
        ax.add_patch(plt.Rectangle((x0, 0.62), 0.440, 3.42,
                                   facecolor=PALE, edgecolor=LIGHT, linewidth=1.0))
        ax.add_patch(plt.Rectangle((x0, 3.90), 0.440, 0.14,
                                   facecolor=color, edgecolor="none"))
        ax.text(x0 + 0.028, 3.55, title, fontsize=13, color=color,
                weight="bold", va="center")
        for i, (k, v) in enumerate(rows):
            y = 3.08 - i * 0.68
            ax.text(x0 + 0.028, y, k, fontsize=10.2, color=GRAY, va="center")
            ax.text(x0 + 0.115, y, v, fontsize=10.6, color=DARK, va="center")

    ax.text(0.500, 2.30, "｜", fontsize=26, color=LIGHT, ha="center",
            va="center", weight="bold")

    fig.text(0.045, 0.080,
             "中芯押的是产能不够，英伟达押的是需求够久——两边都下了重注。",
             fontsize=10.4, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))

    footer(fig, "据中芯国际业绩说明会、华尔街日报调查报道及 Ed Zitron 公开估计整理。")
    fig.savefig(OUT + "图2_两种紧缺.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig, ax = plt.subplots(figsize=(12, 6.8))
    fig.subplots_adjust(left=0.045, right=0.955, top=0.765, bottom=0.175)

    fig.suptitle("“缺货”其实是三段，先松的只有存储",
                 fontsize=19, color=DARK, x=0.045, ha="left", y=0.955, weight="bold")
    fig.text(0.045, 0.888,
             "赵海军 11 月 13 日给出的时间表，拆开看是三种不同的紧缺",
             fontsize=10.8, color=GRAY, ha="left")

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 4.55)
    ax.axis("off")

    segs = [
        ("2027 年", "全行业产能非常紧缺", "行业共识，不只算力芯片", NAVY, "紧"),
        ("2028 年中后期", "存储芯片有望基本供需平衡", "已公布规划的存储产能将高于算力产能", RED, "先松"),
        ("2028 年之后", "算力及配套芯片大概率仍紧缺", "先进制程与 HBM 扩产慢，缺口仍在", NAVY, "仍紧"),
    ]

    for i, (when, what, why, color, tag) in enumerate(segs):
        y = 3.55 - i * 1.35
        ax.add_patch(plt.Rectangle((0.020, y - 0.52), 0.960, 1.04,
                                   facecolor=PALE, edgecolor=LIGHT, linewidth=1.0))
        ax.add_patch(plt.Rectangle((0.020, y - 0.52), 0.008, 1.04,
                                   facecolor=color, edgecolor="none"))
        ax.text(0.052, y + 0.26, when, fontsize=12, color=color,
                weight="bold", va="center")
        ax.text(0.052, y - 0.10, what, fontsize=12.5, color=DARK,
                weight="bold", va="center")
        ax.text(0.052, y - 0.38, why, fontsize=9.8, color=GRAY, va="center")
        ax.text(0.950, y + 0.10, tag, fontsize=13, color=color,
                weight="bold", ha="right", va="center",
                bbox=dict(boxstyle="round,pad=0.45", facecolor="white",
                          edgecolor=color, linewidth=1.2))

    fig.text(0.045, 0.078,
             "“缺货”作为定价理由，只在供给受物理约束时成立。",
             fontsize=10.4, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))

    footer(fig, "原文：中芯国际联合 CEO 赵海军 2026 年 11 月 13 日三季度业绩说明会。")
    fig.savefig(OUT + "图3_紧缺三段.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")
