# -*- coding: utf-8 -*-
"""
《流量涨 16%，通信服务收入降 5.7%：这道算术题怎么解》配套图表

事实口径（2026 年中期业绩，2026-08-13）：
  · 营运收入 5380 亿元（-1.1%）；主营业务收入 4527 亿元（-3.1%）；
    其他业务收入 854 亿元（+11.2%）；股东应占利润 789 亿元（-6.3%）；
    EBITDA 1736 亿元（-6.6%），EBITDA 占主营业务收入比 38.4%。
    剔除增值税税目政策调整影响后同口径实现正增长。
  · 通信服务收入 3504 亿元，同比下降 5.7%。原因表述：新旧动能转换、
    市场环境因素及增值税税目政策调整等影响。
  · 用户与流量：移动客户 10.11 亿户（净增 588 万户）；5G 网络客户 6.87 亿户
    （净增 4474 万户）；手机上网流量同比增长 16.0%，增速显著提升；
    宽带联网客户 3.37 亿户（净增 770 万户）；物联网卡连接数 15.11 亿户
    （净增 2958 万户）。
  · 经营现金流：经营现金净流入 1149 亿元（+37.0%）；自由现金流 539 亿元
    （+111.6%），为近年较高水平。
  · 网络：累计开通 5G 基站 294 万个；千兆网络覆盖住户 5.6 亿户；
    高铁专网上下行平均速率提升超 15%；自智网络 21 个高价值场景实现 L4 级能力。
  · 中期股息每股 2.51 元（+0.3%），折合每股 2.9003 港元（+5.5%）；
    自 2026 年中期派息起以人民币计值及宣派。

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

    head(fig, ax, "一道反向的算术题",
         "流量涨了 16%，收入降了 5.7%",
         "同一块业务，用量和收入朝相反方向走——这是通信业的老问题，也是新问题",
         RED)

    # 上下两个方向相反的指标
    # 上升：流量
    ax.add_patch(FancyBboxPatch(
        (0.042, 0.640), 0.438, 0.116,
        boxstyle="round,pad=0,rounding_size=0.009",
        facecolor=WHITE, edgecolor="#e6eaee", linewidth=0.9, zorder=3))
    ax.add_patch(FancyBboxPatch(
        (0.042, 0.640), 0.0055, 0.116,
        boxstyle="round,pad=0,rounding_size=0.0028",
        facecolor=TEAL, edgecolor="none", zorder=4))
    ax.text(0.068, 0.716, "手机上网流量", fontsize=9.4, color=MUTED,
            ha="left", va="center", zorder=9)
    ax.text(0.068, 0.672, "+16.0%", fontsize=26, color=TEAL, weight="bold",
            ha="left", va="center", zorder=9)
    ax.annotate("", xy=(0.420, 0.720), xytext=(0.420, 0.664),
                arrowprops=dict(arrowstyle="-|>", color=TEAL, linewidth=2.4,
                                shrinkA=0, shrinkB=0))

    # 下降：收入
    ax.add_patch(FancyBboxPatch(
        (0.520, 0.640), 0.438, 0.116,
        boxstyle="round,pad=0,rounding_size=0.009",
        facecolor=WHITE, edgecolor="#e6eaee", linewidth=0.9, zorder=3))
    ax.add_patch(FancyBboxPatch(
        (0.520, 0.640), 0.0055, 0.116,
        boxstyle="round,pad=0,rounding_size=0.0028",
        facecolor=RED, edgecolor="none", zorder=4))
    ax.text(0.546, 0.716, "通信服务收入（3504 亿元）", fontsize=9.4,
            color=MUTED, ha="left", va="center", zorder=9)
    ax.text(0.546, 0.672, "-5.7%", fontsize=26, color=RED, weight="bold",
            ha="left", va="center", zorder=9)
    ax.annotate("", xy=(0.900, 0.664), xytext=(0.900, 0.720),
                arrowprops=dict(arrowstyle="-|>", color=RED, linewidth=2.4,
                                shrinkA=0, shrinkB=0))

    # 三个用户指标
    ax.text(0.042, 0.586, "同期用户规模仍在增长", fontsize=8.6, color=MUTED,
            ha="left", va="center")
    ax.plot([0.042, 0.958], [0.566, 0.566], color=HAIR, linewidth=1.0)

    users = [
        ("10.11 亿户", "移动客户", "净增 588 万户", NAVY),
        ("6.87 亿户", "5G 网络客户", "净增 4474 万户", TEAL),
        ("3.37 亿户", "宽带联网客户", "净增 770 万户", GOLD),
        ("15.11 亿户", "物联网卡连接", "净增 2958 万户", MUTED),
    ]
    x = 0.042
    w = 0.222
    gap = 0.017
    for num, label, note, color in users:
        panel(ax, x, 0.392, w, 0.140, color)
        ax.text(x + 0.020, 0.490, num, fontsize=15.0, color=color,
                weight="bold", ha="left", va="center", zorder=9)
        ax.text(x + 0.020, 0.452, label, fontsize=8.4, color=INK,
                ha="left", va="center", zorder=9)
        ax.text(x + 0.020, 0.418, note, fontsize=7.8, color=MUTED,
                ha="left", va="center", zorder=9)
        x += w + gap

    ax.text(0.042, 0.336, "用户还在涨，用量还在涨，但收入在降。三个事实同时成立。",
            fontsize=9.2, color=INK, ha="left", va="center")

    # 底部三个原因
    ax.text(0.042, 0.288, "财报给的三个原因", fontsize=8.6, color=MUTED,
            ha="left", va="center")

    reasons = [
        ("新旧动能转换", "传统业务让位新业务"),
        ("市场环境因素", "竞争与需求变化"),
        ("增值税税目调整", "口径变化"),
    ]
    x = 0.042
    for name, note in reasons:
        ax.add_patch(Circle((x + 0.010, 0.224), 0.0042, facecolor=RED,
                            edgecolor="none", zorder=8))
        ax.text(x + 0.024, 0.228, name, fontsize=8.8, color=INK,
                weight="bold", ha="left", va="center", zorder=9)
        ax.text(x + 0.024, 0.198, note, fontsize=7.6, color=MUTED,
                ha="left", va="center", zorder=9)
        x += 0.306

    outro(fig, ax, "增量不增收，是通信业最老的一道题，也是这轮转型的起点。")
    foot(fig, ax, "事实来源：中国移动 2026 年中期业绩（2026-08-13）；"
         "新华网 2026-08-13、上海证券报 2026-08-14")

    fig.savefig(OUT + "图1_反向算术.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(13.6, 8.0))
    ax = new_axes(fig)

    head(fig, ax, "收入结构变化",
         "主营收入降 3.1%，但内部结构在换",
         "通信服务在缩，算力与智能服务在长——三条线的方向不一致",
         NAVY)

    rows = [
        ("通信服务", 3504, "-5.7%", NAVY, False),
        ("算力服务", 529, "+14.0%", RED, True),
        ("智能服务", 493, "+0.9%", TEAL, True),
    ]

    ax.text(0.042, 0.758, "三项主业收入与同比", fontsize=8.6, color=MUTED,
            ha="left", va="center")
    ax.plot([0.042, 0.958], [0.738, 0.738], color=HAIR, linewidth=1.0)

    scale = 0.400 / 3504.0
    y = 0.664
    for name, val, gtxt, color, up in rows:
        ax.text(0.042, y + 0.016, name, fontsize=11.0, color=INK,
                weight="bold", ha="left", va="center", zorder=9)
        ax.text(0.042, y - 0.020, f"{val} 亿元", fontsize=8.4, color=MUTED,
                ha="left", va="center", zorder=9)
        ax.add_patch(FancyBboxPatch(
            (0.180, y - 0.048), val * scale, 0.030,
            boxstyle="round,pad=0,rounding_size=0.007",
            facecolor=color, edgecolor="none", zorder=6))

        gcol = color if up else MUTED
        ax.text(0.180 + val * scale + 0.014, y - 0.018, gtxt, fontsize=11.6,
                color=gcol, weight="bold", ha="left", va="center", zorder=9)
        y -= 0.128

    # 结构占比
    ax.text(0.042, 0.300, "算力 + 智能占主营业务收入比", fontsize=8.6,
            color=MUTED, ha="left", va="center")

    bar_x, bar_w = 0.042, 0.560
    ax.add_patch(FancyBboxPatch(
        (bar_x, 0.232), bar_w, 0.044,
        boxstyle="round,pad=0,rounding_size=0.008",
        facecolor="#e8ebef", edgecolor="none", zorder=4))
    ax.add_patch(FancyBboxPatch(
        (bar_x, 0.232), bar_w * 0.226, 0.044,
        boxstyle="round,pad=0,rounding_size=0.008",
        facecolor=RED, edgecolor="none", zorder=6))
    ax.text(bar_x + bar_w * 0.226 + 0.014, 0.254, "22.6%", fontsize=13.0,
            color=RED, weight="bold", ha="left", va="center", zorder=9)
    ax.text(bar_x, 0.208, "同比提升 2.2 个百分点", fontsize=8.0,
            color=MUTED, ha="left", va="center", zorder=9)

    # 右侧：现金流（下移，不与上方条形冲突）
    panel(ax, 0.610, 0.398, 0.348, 0.212, TEAL, face=WASH)
    ax.text(0.632, 0.572, "另两个向好指标", fontsize=8.4, color=MUTED,
            ha="left", va="center", zorder=9)
    ax.text(0.632, 0.520, "1149 亿元", fontsize=14.0, color=TEAL,
            weight="bold", ha="left", va="center", zorder=9)
    ax.text(0.632, 0.482, "经营现金净流入，同比 +37.0%", fontsize=7.8,
            color=INK, ha="left", va="center", zorder=9)
    ax.text(0.632, 0.446, "自由现金流 539 亿元，同比 +111.6%", fontsize=7.8,
            color=INK, ha="left", va="center", zorder=9)

    outro(fig, ax, "收入在降，现金流在涨——这两件事同时发生，说明钱的质量变了。")
    foot(fig, ax, "事实来源：中国移动 2026 年中期业绩；新华网 2026-08-13 对半年报的报道")

    fig.savefig(OUT + "图2_结构变化.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(13.6, 8.0))
    ax = new_axes(fig)

    head(fig, ax, "从 Byte 到 Token",
         "从卖流量到卖算力，中间隔着一整套计价方式",
         "同样一张网，卖的东西换了，收入的算法也就换了",
         GOLD)

    stages = [
        ("卖流量", "按 GB 计费", MUTED, [
            ("收入公式", "用量 × 单价"),
            ("增长来源", "用户数 × 人均用量"),
            ("天花板", "人口上限 + 资费下行"),
            ("当前状态", "用量涨 16%，单价在降"),
        ]),
        ("卖算力", "按卡时计费", NAVY, [
            ("收入公式", "算力规模 × 使用率 × 单价"),
            ("增长来源", "智算集群投产 + 使用率提升"),
            ("天花板", "资本开支 + 电力"),
            ("当前状态", "使用率超 90%"),
        ]),
        ("卖词元", "按 Token 计费", RED, [
            ("收入公式", "调用量 × 单价"),
            ("增长来源", "应用渗透率 × 单应用消耗"),
            ("天花板", "产业数字化程度"),
            ("当前状态", "起步阶段"),
        ]),
    ]

    x = 0.042
    w = 0.288
    gap = 0.019
    for i, (name, price, color, items) in enumerate(stages):
        panel(ax, x, 0.230, w, 0.510, color)

        ax.text(x + 0.026, 0.700, name, fontsize=15.5, color=color,
                weight="bold", ha="left", va="center", zorder=9)
        ax.text(x + 0.026, 0.664, price, fontsize=9.6, color=MUTED,
                ha="left", va="center", zorder=9)
        ax.plot([x + 0.026, x + w - 0.026], [0.640, 0.640], color=HAIR,
                linewidth=1.0, zorder=5)

        yy = 0.598
        for k, v in items:
            ax.text(x + 0.026, yy, k, fontsize=7.8, color=MUTED,
                    ha="left", va="center", zorder=9)
            ax.text(x + 0.026, yy - 0.028, v, fontsize=8.8, color=INK,
                    weight="bold", ha="left", va="center", zorder=9)
            yy -= 0.076

        if i < 2:
            ax.annotate("", xy=(x + w + gap - 0.001, 0.486),
                        xytext=(x + w + 0.001, 0.486),
                        arrowprops=dict(arrowstyle="-|>", color="#c9d0d8",
                                        linewidth=1.8, shrinkA=0, shrinkB=0))
        x += w + gap

    ax.add_patch(FancyBboxPatch(
        (0.042, 0.140), 0.916, 0.070,
        boxstyle="round,pad=0,rounding_size=0.008",
        facecolor=WASH, edgecolor="none", zorder=3))
    ax.text(0.062, 0.176,
            "每一次换轨，都在把收入的锚从「时间」换成「用量」，再换成「价值」。",
            fontsize=8.6, color=INK, ha="left", va="center", zorder=9)

    outro(fig, ax, "转型的本质不是换产品，是换计价单位。")
    foot(fig, ax, "事实来源：中国移动 2026 年中期业绩；注：卖词元的计价方式为行业通行理解，"
         "非公司财报口径")

    fig.savefig(OUT + "图3_计价换轨.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)
