# -*- coding: utf-8 -*-
"""
《欧洲谈 5000 亿，中国谈谁来担责》配套图表
事实来源：新华社都柏林 2026-11-13 电；欧盟委员会主席冯德莱恩记者会；
证监会主席吴清 2026-11-14 致辞；工信部工信厅信管〔2026〕42 号
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
    fig.subplots_adjust(left=0.055, right=0.955, top=0.755, bottom=0.215)

    fig.suptitle("5000 亿是缺口，300 亿是已规划",
                 fontsize=19, color=DARK, x=0.045, ha="left", y=0.955, weight="bold")
    fig.text(0.045, 0.885,
             "冯德莱恩在都柏林峰会后的两个数字（单位：亿欧元）",
             fontsize=10.8, color=GRAY, ha="left")

    ax.set_xlim(0, 5000)
    ax.set_ylim(0, 2.6)
    ax.axis("off")

    # 已规划
    ax.barh(1.55, 300, height=0.42, color=NAVY)
    ax.text(460, 1.62, "300 亿", fontsize=15, color=NAVY, weight="bold", va="center")
    ax.text(460, 1.36, "已规划的算力基础设施（七个 AI 大数据工厂）",
            fontsize=10.2, color=GRAY, va="center")

    # 缺口
    ax.barh(0.75, 5000, height=0.42, color=LIGHT)
    ax.barh(0.75, 300, height=0.42, color=NAVY)
    ax.text(460, 0.82, "5000 亿", fontsize=15, color=DARK, weight="bold", va="center")
    ax.text(460, 0.56, "她说的“至少需要”", fontsize=10.2, color=GRAY, va="center")

    # 差距标注
    ax.annotate("", xy=(4990, 0.28), xytext=(20, 0.28),
                arrowprops=dict(arrowstyle="<->", color=RED, lw=1.6))
    ax.text(2500, 0.10, "约 16.7 倍", fontsize=13, color=RED,
            weight="bold", ha="center")

    takeaway(fig, 0.093, "她说的是一个缺口，不是一个预算。")

    footer(fig, "数据：冯德莱恩 2026-11-13 都柏林欧盟领导人 AI 专题峰会记者会，据新华社等报道。")
    fig.savefig(OUT + "图1_钱与缺口.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig, ax = plt.subplots(figsize=(12, 6.8))
    fig.subplots_adjust(left=0.045, right=0.955, top=0.755, bottom=0.175)

    fig.suptitle("治理的重心，从原则宣示移到操作机制",
                 fontsize=19, color=DARK, x=0.045, ha="left", y=0.955, weight="bold")
    fig.text(0.045, 0.885,
             "两份文件，一套思路：可追溯、可定责",
             fontsize=10.8, color=GRAY, ha="left")

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 4.65)
    ax.axis("off")

    panels = [
        (0.030, "证监会：吴清 11.14 致辞", NAVY, [
            "责任认定",
            "数据安全 · 客户保护",
            "系统风险",
            "防范算法黑箱、AI 网络攻击",
            "提升金融基础设施韧性",
        ]),
        (0.530, "工信部：智能体进网管理 11.06", RED, [
            "进网检测开展适配验证",
            "智能体配备唯一身份码",
            "保证拿证前后一致性",
            "重大变化须报备并重新检测",
            "涉诈风险安全评估前置",
        ]),
    ]

    for x0, title, color, items in panels:
        ax.add_patch(plt.Rectangle((x0, 0.72), 0.440, 3.42,
                                   facecolor=PALE, edgecolor=LIGHT, linewidth=1.0))
        ax.add_patch(plt.Rectangle((x0, 4.00), 0.440, 0.14,
                                   facecolor=color, edgecolor="none"))
        ax.text(x0 + 0.028, 3.66, title, fontsize=12.5, color=color,
                weight="bold", va="center")
        for i, it in enumerate(items):
            y = 3.18 - i * 0.56
            ax.add_patch(plt.Circle((x0 + 0.038, y), 0.0055, facecolor=color,
                                    edgecolor="none"))
            ax.text(x0 + 0.060, y, it, fontsize=10.4, color=DARK, va="center")

    takeaway(fig, 0.082, "两份文件都不解决“能不能用”，只解决“用了出问题谁负责”。")

    footer(fig, "原文：证监会 2026-11-14 首届中国资本市场学术年会；工信厅信管〔2026〕42 号（2026-11-06）。")
    fig.savefig(OUT + "图2_治理重心迁移.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig, ax = plt.subplots(figsize=(12, 6.8))
    fig.subplots_adjust(left=0.045, right=0.955, top=0.755, bottom=0.175)

    fig.suptitle("两种路径，同一个前提",
                 fontsize=19, color=DARK, x=0.045, ha="left", y=0.955, weight="bold")
    fig.text(0.045, 0.885,
             "顺序不同，但都承认一件事：AI 已经在基础设施里了",
             fontsize=10.8, color=GRAY, ha="left")

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 4.55)
    ax.axis("off")

    cols = [
        (0.040, "欧洲", "先建机制，再谈投资", NAVY, [
            "5000 亿欧元缺口尚未落实",
            "300 亿算力基础设施已规划",
            "爱沙尼亚、芬兰要求建事件机制",
            "峰会日期被乌克兰议题盖过",
            "下次再议：预计 2027 年",
        ]),
        (0.540, "中国", "先给场景，同步立规", RED, [
            "智能体进网须有身份码",
            "重大变化须报备、重检",
            "金融 AI 要研究责任认定",
            "算法黑箱列入防范重点",
            "两条线并行推进",
        ]),
    ]

    for x0, name, sub, color, items in cols:
        ax.text(x0, 4.28, name, fontsize=17, color=color, weight="bold")
        ax.text(x0, 3.92, sub, fontsize=11, color=GRAY)
        ax.plot([x0, x0 + 0.42], [3.72, 3.72], color=color, lw=1.6)
        for i, it in enumerate(items):
            y = 3.34 - i * 0.55
            ax.text(x0, y, "· " + it, fontsize=10.6, color=DARK, va="center")

    ax.text(0.500, 0.42, "同一个前提：AI 已经进入基础设施", fontsize=13,
            color=DARK, ha="center", va="center", weight="bold",
            bbox=dict(boxstyle="round,pad=0.8", facecolor=PALE,
                      edgecolor=DARK, linewidth=1.2))

    takeaway(fig, 0.078, "一个不可解释的系统，接在一个不可承受的环节上——这才是风险点。")

    footer(fig, "据新华社、AI Safety HOT、证监会与工信部公开信息整理。")
    fig.savefig(OUT + "图3_两种路径.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")
