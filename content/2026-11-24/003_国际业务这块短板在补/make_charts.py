# -*- coding: utf-8 -*-
"""
《国际市场涨 30.1%，是三大主业里增速最快的一块》配套图表

事实口径（2026 年中期业绩，2026-08-13）：
  · 国际市场收入 182 亿元，同比增长 30.1%（半年报口径 181.73 亿元）。
  · POP 点达到 463 个；国际传输能力达到 437Tbps。
  · 来访漫游业务量同比增长 59.9%；出访漫游客户 5,623 万户，同比增长 5.2%。
  · 能力出海项目数量同比增长 38.6%；累计服务中资出海企业数量较上年末增长 19.6%。
  · 对比：同期通信服务收入 3504 亿元（-5.7%）；算力服务 529 亿元（+14.0%）；
    智能服务 493 亿元（+0.9%）。
  · 董事长在报告书中表述：持续推动国内国际"两个市场"深度融通，加快能力规模出海。
  据新华网 2026-08-13、通信产业网/移动通信网 2026-08-17。

风格：克制传媒风，编辑排版
输出目录 = 脚本所在目录
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["figure.facecolor"] = "white"
plt.rcParams["savefig.facecolor"] = "white"

INK = "#1a2332"
NAVY = "#1b3a5c"
RED = "#b0413e"
TEAL = "#2f6b64"
GOLD = "#9a7b3f"
MUTED = "#7b8494"
HAIR = "#dfe3e8"
WASH = "#f4f6f8"
WHITE = "#ffffff"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep
Q_L, Q_R = "\u300c", "\u300d"


def new_axes(fig):
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return ax


def head(fig, ax, kicker, title, sub, color):
    ax.add_patch(Rectangle((0.042, 0.928), 0.0075, 0.040,
                           facecolor=color, edgecolor="none", zorder=9))
    ax.text(0.058, 0.950, kicker, fontsize=9.2, color=color,
            weight="bold", ha="left", va="center", zorder=9)
    ax.text(0.042, 0.900, title, fontsize=21, color=INK, weight="bold",
            ha="left", va="top", zorder=9)
    ax.text(0.042, 0.848, sub, fontsize=10.4, color=MUTED,
            ha="left", va="top", zorder=9)
    ax.plot([0.042, 0.958], [0.812, 0.812], color=HAIR, linewidth=1.0,
            zorder=5)


def foot(fig, ax, text):
    ax.plot([0.042, 0.958], [0.058, 0.058], color=HAIR, linewidth=0.9,
            zorder=5)
    ax.text(0.042, 0.028, text, fontsize=7.0, color=MUTED,
            ha="left", va="center", zorder=9)


def outro(fig, ax, text, color=INK):
    ax.add_patch(FancyBboxPatch(
        (0.042, 0.082), 0.700, 0.048,
        boxstyle="round,pad=0.002,rounding_size=0.008",
        facecolor=color, edgecolor="none", zorder=6))
    ax.text(0.062, 0.106, text, fontsize=10.2, color=WHITE,
            ha="left", va="center", zorder=9)


def panel(ax, x, y, w, h, accent, face=WHITE, bar=0.0055, shadow=True):
    if shadow:
        ax.add_patch(FancyBboxPatch(
            (x + 0.0035, y - 0.0035), w, h,
            boxstyle="round,pad=0,rounding_size=0.009",
            facecolor="#e9ecf0", edgecolor="none", zorder=2))
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0,rounding_size=0.009",
        facecolor=face, edgecolor="#e6eaee", linewidth=0.9, zorder=3))
    ax.add_patch(FancyBboxPatch(
        (x, y), bar, h,
        boxstyle="round,pad=0,rounding_size=0.0028",
        facecolor=accent, edgecolor="none", zorder=4))


# ---------------------------------------------------------------- 图 1
def fig1():
    fig = plt.figure(figsize=(13.6, 8.0))
    ax = new_axes(fig)

    head(fig, ax, "增速排名",
         "四大板块里，国际市场涨得最快",
         "30.1%，是通信服务（-5.7%）的反面，也是算力服务（14.0%）的两倍多",
         TEAL)

    ax.text(0.042, 0.758, "2026 年上半年同比增速", fontsize=8.6, color=MUTED,
            ha="left", va="center")
    ax.plot([0.042, 0.958], [0.738, 0.738], color=HAIR, linewidth=1.0)

    # 三正一负的条
    rows = [
        ("国际市场", 182, 30.1, TEAL, "182 亿元"),
        ("算力服务", 529, 14.0, RED, "529 亿元"),
        ("智能服务", 493, 0.9, GOLD, "493 亿元"),
        ("通信服务", 3504, -5.7, MUTED, "3504 亿元"),
    ]

    base_x = 0.230
    unit = 0.0092   # 每 1% 的宽度
    zero_x = base_x + 6 * unit   # 负值区

    ax.plot([zero_x, zero_x], [0.268, 0.700], color=HAIR, linewidth=1.0,
            zorder=4)

    y = 0.678
    for name, val, g, color, rev in rows:
        ax.text(0.042, y + 0.012, name, fontsize=10.8, color=INK,
                weight="bold", ha="left", va="center", zorder=9)
        ax.text(0.042, y - 0.022, rev, fontsize=8.2, color=MUTED,
                ha="left", va="center", zorder=9)

        if g >= 0:
            w = g * unit
            ax.add_patch(FancyBboxPatch(
                (zero_x, y - 0.020), w, 0.034,
                boxstyle="round,pad=0,rounding_size=0.007",
                facecolor=color, edgecolor="none", zorder=6))
            ax.text(zero_x + w + 0.012, y - 0.003, f"+{g:.1f}%",
                    fontsize=12.0, color=color, weight="bold",
                    ha="left", va="center", zorder=9)
        else:
            w = abs(g) * unit
            ax.add_patch(FancyBboxPatch(
                (zero_x - w, y - 0.020), w, 0.034,
                boxstyle="round,pad=0,rounding_size=0.007",
                facecolor=color, edgecolor="none", zorder=6))
            ax.text(zero_x - w - 0.012, y - 0.003, f"{g:.1f}%",
                    fontsize=12.0, color=color, weight="bold",
                    ha="right", va="center", zorder=9)
        y -= 0.108

    ax.text(zero_x, 0.252, "0", fontsize=8.0, color=MUTED,
            ha="center", va="center", zorder=9)

    # 说明
    panel(ax, 0.700, 0.290, 0.258, 0.396, TEAL, face=WASH)
    ax.text(0.720, 0.640, "体量最小的板块", fontsize=8.8, color=MUTED,
            ha="left", va="center", zorder=9)
    ax.text(0.720, 0.588, "182 亿元", fontsize=20.0, color=TEAL,
            weight="bold", ha="left", va="center", zorder=9)
    ax.text(0.720, 0.540,
            "只占营业收入的\n约 3.4%。",
            fontsize=8.4, color=INK, ha="left", va="top",
            linespacing=1.7, zorder=9)
    ax.text(0.720, 0.446,
            "增速最高，\n但盘子最小——\n这正是它还能\n保持高增速的原因。",
            fontsize=8.2, color=MUTED, ha="left", va="top",
            linespacing=1.7, zorder=9)

    outro(fig, ax, "增速榜第一名的意义，要看它在一个多小的盘子上跑出来。")
    foot(fig, ax, "事实来源：中国移动 2026 年中期业绩（2026-08-13）；新华网 2026-08-13")

    fig.savefig(OUT + "图1_增速排名.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(13.6, 8.0))
    ax = new_axes(fig)

    head(fig, ax, "30.1% 由什么拼成",
         "四组数字，指向两类完全不同的需求",
         "漫游恢复是" + Q_L + "人流" + Q_R + "，能力出海是" + Q_L + "业务流" + Q_R,
         NAVY)

    groups = [
        ("人流：出行恢复", TEAL, [
            ("来访漫游业务量", "+59.9%", "境外用户入境使用网络的量"),
            ("出访漫游客户", "5,623 万户", "同比 +5.2%，出境用户规模"),
        ]),
        ("业务流：企业出海", RED, [
            ("能力出海项目数", "+38.6%", "项目口径，反映交付规模"),
            ("服务中资出海企业", "+19.6%", "较上年末增长，存量客户扩张"),
        ]),
    ]

    x = 0.042
    for name, color, items in groups:
        panel(ax, x, 0.352, 0.438, 0.386, color)

        ax.text(x + 0.026, 0.700, name, fontsize=12.2, color=color,
                weight="bold", ha="left", va="center", zorder=9)
        ax.plot([x + 0.026, x + 0.432], [0.676, 0.676], color=HAIR,
                linewidth=1.0, zorder=5)

        y = 0.634
        for label, num, note in items:
            ax.text(x + 0.026, y, label, fontsize=8.4, color=MUTED,
                    ha="left", va="center", zorder=9)
            ax.text(x + 0.026, y - 0.034, num, fontsize=16.0, color=color,
                    weight="bold", ha="left", va="center", zorder=9)
            ax.text(x + 0.026, y - 0.066, note, fontsize=7.8, color=INK,
                    ha="left", va="center", zorder=9)
            y -= 0.104

        x += 0.478

    # 底座
    ax.text(0.042, 0.318, "支撑这两类需求的物理底座", fontsize=8.6,
            color=MUTED, ha="left", va="center")
    ax.plot([0.042, 0.958], [0.298, 0.298], color=HAIR, linewidth=1.0)

    infra = [
        ("463 个", "POP 点", "全球接入节点数量"),
        ("437Tbps", "国际传输能力", "跨境带宽总容量"),
    ]
    x = 0.042
    for num, label, note in infra:
        ax.text(x, 0.256, num, fontsize=17.0, color=NAVY, weight="bold",
                ha="left", va="center", zorder=9)
        ax.text(x, 0.222, label, fontsize=9.0, color=INK, weight="bold",
                ha="left", va="center", zorder=9)
        ax.text(x, 0.194, note, fontsize=7.6, color=MUTED,
                ha="left", va="center", zorder=9)
        x += 0.300

    ax.text(0.680, 0.226,
            "POP 点决定" + Q_L + "能连到哪" + Q_R + "，\n传输能力决定" + Q_L + "连得多粗" + Q_R + "。",
            fontsize=8.4, color=INK, ha="left", va="center",
            linespacing=1.7, zorder=9)

    outro(fig, ax, "增长的底子不在营销，在这 463 个接入点和 437Tbps 的管道上。")
    foot(fig, ax, "事实来源：中国移动 2026 年中期业绩；通信产业网 2026-08-17"
         "《半年大涨 30%：中国移动国际业务换挡提速》")

    fig.savefig(OUT + "图2_两类需求.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(13.6, 8.0))
    ax = new_axes(fig)

    head(fig, ax, "从连接出海到能力出海",
         "出海这件事，运营商换了三次姿势",
         "从卖国际长途，到卖跨境专线，再到把整套方案搬出去",
         GOLD)

    stages = [
        ("连接出海", "卖语音与带宽", MUTED, [
            ("客户是谁", "出国的个人、驻外机构"),
            ("卖的是什么", "国际长途、漫游、跨境专线"),
            ("竞争壁垒", "线路资源与结算价"),
            ("收入形态", "按分钟、按带宽"),
        ]),
        ("网络出海", "卖覆盖与节点", NAVY, [
            ("客户是谁", "跨国企业、云服务商"),
            ("卖的是什么", "POP 节点、数据中心、海缆容量"),
            ("竞争壁垒", "全球资源布局"),
            ("收入形态", "按容量、按机位"),
        ]),
        ("能力出海", "卖整套方案", RED, [
            ("客户是谁", "出海的中资企业"),
            ("卖的是什么", "网络 + 算力 + 平台 + 运维"),
            ("竞争壁垒", "懂中国企业的业务流程"),
            ("收入形态", "按项目、按服务"),
        ]),
    ]

    x = 0.042
    w = 0.288
    gap = 0.019
    for i, (name, tag, color, items) in enumerate(stages):
        panel(ax, x, 0.240, w, 0.490, color)

        ax.text(x + 0.026, 0.696, name, fontsize=15.0, color=color,
                weight="bold", ha="left", va="center", zorder=9)
        ax.text(x + 0.026, 0.660, tag, fontsize=9.4, color=MUTED,
                ha="left", va="center", zorder=9)
        ax.plot([x + 0.026, x + w - 0.026], [0.638, 0.638], color=HAIR,
                linewidth=1.0, zorder=5)

        yy = 0.594
        for k, v in items:
            ax.text(x + 0.026, yy, k, fontsize=7.6, color=MUTED,
                    ha="left", va="center", zorder=9)
            ax.text(x + 0.026, yy - 0.030, v, fontsize=8.6, color=INK,
                    weight="bold", ha="left", va="center", zorder=9)
            yy -= 0.080

        if i < 2:
            ax.annotate("", xy=(x + w + gap - 0.001, 0.480),
                        xytext=(x + w + 0.001, 0.480),
                        arrowprops=dict(arrowstyle="-|>", color="#c9d0d8",
                                        linewidth=1.8, shrinkA=0, shrinkB=0))
        x += w + gap

    ax.add_patch(FancyBboxPatch(
        (0.042, 0.146), 0.916, 0.072,
        boxstyle="round,pad=0,rounding_size=0.008",
        facecolor=WASH, edgecolor="none", zorder=3))
    ax.text(0.062, 0.182,
            "三次换轨的共同点：卖的东西越来越软，对客户业务的理解要求越来越高。",
            fontsize=8.6, color=INK, ha="left", va="center", zorder=9)

    outro(fig, ax, "能力出海项目数涨 38.6%，说明这条路已经跑出了规模。")
    foot(fig, ax, "事实来源：中国移动 2026 年中期业绩；注：三阶段划分为作者据公开材料的归纳，"
         "非公司官方口径")

    fig.savefig(OUT + "图3_三次换轨.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)
