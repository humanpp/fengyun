# -*- coding: utf-8 -*-
"""
《非 GPU 首次超过 GPU：英伟达的“确定性溢价”正在被重估》配套图表
事实来源：IDC 2026H1 中国数据中心 AI 加速器出货数据（路透社 2026-10-13 引用）、
英伟达股价与市值报道、安纳智芯 AX100 报道、英伟达入股英特尔公告
风格：克制传媒风，白底、低饱和配色、标题即结论
输出目录 = 脚本所在目录
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

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
SAND = "#b9a887"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep


def canvas(fig):
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return ax


def footer(fig, text):
    fig.text(0.045, 0.035, text, fontsize=8.4, color=GRAY, ha="left", va="bottom")


def takeaway(fig, y, text, size=10.4):
    fig.text(0.045, y, text, fontsize=size, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


def head(fig, title, sub):
    fig.text(0.045, 0.935, title, fontsize=19, color=DARK, ha="left",
             va="center", weight="bold")
    fig.text(0.045, 0.868, sub, fontsize=10.8, color=GRAY, ha="left", va="center")


# ---------------------------------------------------------------- 图 1
def fig1():
    fig = plt.figure(figsize=(12, 6.8))
    ax = canvas(fig)
    head(fig, "跌的是哪一层预期",
         "五个交易日 −12.75%；11 月 12 日辞任当日，盘中一度跌超 14%")

    # ---- 时间线
    ax.plot([0.095, 0.890], [0.700, 0.700], color=LIGHT, lw=2.2, zorder=1)
    events = [
        (0.095, "11.08", "致歉信", "五个交易日从这里算", GRAY),
        (0.360, "11.11", "收 173.73 美元", "市值 4.20 万亿", NAVY),
        (0.625, "11.12", "辞任", "盘中最低 148.80，\n收跌 4.34%", RED),
        (0.890, "11.17", "FY27Q3 财报", "下一个验证点", GRAY),
    ]
    for x, date, what, note, color in events:
        ax.add_patch(plt.Circle((x, 0.700), 0.010, facecolor=color,
                                edgecolor="white", linewidth=1.6, zorder=4))
        ax.text(x, 0.762, date, fontsize=9.6, color=color, weight="bold",
                ha="center", va="center")
        ax.text(x, 0.648, what, fontsize=10.4, color=DARK, weight="bold",
                ha="center", va="center")
        ax.text(x, 0.600, note, fontsize=8.8, color=GRAY, ha="center",
                va="center", linespacing=1.4)

    # ---- 三层确定性
    fig.text(0.045, 0.520, "“确定性溢价”的三层，只有一层在动摇",
             fontsize=12.5, color=DARK, weight="bold", va="center")

    cards = [
        ("需求确定", "订单在手", "还在", NAVY),
        ("交付确定", "产能量产跟得上", "还在", NAVY),
        ("路线确定", "下一代还领先", "在动摇", RED),
    ]
    xs = [0.055, 0.345, 0.635]
    for (title, note, status, color), x in zip(cards, xs):
        ax.add_patch(Rectangle((x, 0.305), 0.270, 0.135, facecolor="#fafafb",
                               edgecolor=LIGHT, linewidth=1.0))
        ax.add_patch(Rectangle((x, 0.305), 0.008, 0.135, facecolor=color,
                               edgecolor="none"))
        ax.text(x + 0.030, 0.398, title, fontsize=12.5, color=color,
                weight="bold", va="center")
        ax.text(x + 0.030, 0.348, note, fontsize=9.4, color=GRAY, va="center")
        ax.text(x + 0.245, 0.398, status, fontsize=10.4, color=color,
                weight="bold", ha="right", va="center")

    ax.text(0.055, 0.245, "市场这次卖的，是第三层——不是需求，也不是产能。",
            fontsize=10.0, color=DARK, va="center")

    takeaway(fig, 0.150, "一个月跌超 26%，跌的是溢价率，不是算力需求。")
    footer(fig, "据证券时报、新浪财经、GSM、ETtoday 报道整理；收盘价与盘中最低价均为当日公开行情数据。")
    fig.savefig(OUT + "图1_跌掉的是哪一层.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(12, 6.8))
    ax = canvas(fig)
    head(fig, "200.8 万颗里的结构变化",
         "2026 年上半年中国数据中心 AI 加速器出货；非 GPU 首次超过 GPU")

    # ---- 上：堆叠条
    left, right = 0.055, 0.945
    span = right - left
    cut = left + span * 99.1 / 200.8
    yb, hb = 0.650, 0.085
    ax.add_patch(Rectangle((left, yb), cut - left, hb, facecolor=NAVY,
                           edgecolor="none"))
    ax.add_patch(Rectangle((cut, yb), right - cut, hb, facecolor=RED,
                           edgecolor="none"))
    ax.text((left + cut) / 2, yb + hb / 2, "GPU 99.1 万颗", fontsize=11.5,
            color="white", ha="center", va="center", weight="bold")
    ax.text((cut + right) / 2, yb + hb / 2, "非 GPU 101.6 万颗", fontsize=11.5,
            color="white", ha="center", va="center", weight="bold")
    ax.text((left + cut) / 2, yb + hb + 0.038, "同比下降 26%", fontsize=9.4,
            color=NAVY, ha="center", va="center")
    ax.text((cut + right) / 2, yb + hb + 0.038, "同比增长近 80%", fontsize=9.4,
            color=RED, ha="center", va="center", weight="bold")
    ax.text(left, yb - 0.045, "总出货 200.8 万颗；非 GPU 比 GPU 多 2.5 万颗",
            fontsize=9.2, color=GRAY, ha="left", va="center")

    # ---- 左下：厂商份额
    fig.text(0.070, 0.545, "厂商份额（%）", fontsize=12.0, color=DARK,
             weight="bold", va="center")
    axb = fig.add_axes([0.075, 0.250, 0.430, 0.265])
    names = ["其他", "海光", "昆仑芯", "寒武纪", "平头哥", "华为", "英伟达"]
    vals = [19, 3, 4, 5, 7, 28, 34]
    cols = [LIGHT, GRAY, GRAY, GRAY, GRAY, SAND, NAVY]
    bars = axb.barh(names, vals, height=0.60, color=cols)
    for b, v in zip(bars, vals):
        axb.text(v + 0.7, b.get_y() + b.get_height() / 2, f"{v}", fontsize=9.6,
                 color=DARK, va="center")
    axb.set_xlim(0, 40)
    axb.tick_params(axis="y", labelsize=9.6, colors=DARK, length=0)
    axb.tick_params(axis="x", labelsize=8.4, colors=GRAY, length=0)
    for s in ("top", "right", "left", "bottom"):
        axb.spines[s].set_visible(False)

    # ---- 右下：要点
    notes = [
        ("31 → 6", "英伟达与华为的份额差，\n一年内从 31 个百分点收窄到 6 个"),
        ("9 / 11", "IDC 追踪的 11 家中国厂商中，\n9 家出货同比增长"),
        ("约 95%", "非 GPU 细分里，华为、平头哥、\n昆仑芯、寒武纪合计占比"),
    ]
    for i, (big, text) in enumerate(notes):
        y = 0.470 - i * 0.125
        ax.add_patch(Rectangle((0.545, y - 0.048), 0.400, 0.096,
                               facecolor="#fafafb", edgecolor=LIGHT,
                               linewidth=0.9))
        ax.text(0.565, y, big, fontsize=13, color=RED, weight="bold",
                va="center")
        ax.text(0.680, y, text, fontsize=8.8, color=DARK, va="center",
                linespacing=1.5)

    takeaway(fig, 0.100, "但这是出货量，不是收入，也不是性能：量先翻面，价还没翻。")
    footer(fig, "据 IDC 数据整理（路透社 2026-10-13 引用，经智东西、长桥证券等转述）；份额与出货量为 2026 年上半年口径。")
    fig.savefig(OUT + "图2_出货结构.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(12, 6.8))
    ax = canvas(fig)
    head(fig, "三条替代路径，各能覆盖到哪里",
         "一条抢量，一条抢切片，一条抢标准；没人碰训练那一块")

    cards = [
        ("国产非 GPU / ASIC", "华为、平头哥、寒武纪、昆仑芯",
         "推理侧：量大、对成本敏感", "训练与软件生态", NAVY),
        ("模拟计算", "安纳智芯 AX100，10 月流片",
         "矩阵求解这类切片，单次 <100 纳秒", "通用性：只解一类问题", SAND),
        ("平台整合", "英伟达 × 英特尔，50 亿美元入股",
         "标准与生态绑定，NVLink 进 x86", "客户是否愿意被绑定", RED),
    ]
    xs = [0.055, 0.345, 0.635]
    for (title, who, cover, limit, color), x in zip(cards, xs):
        ax.add_patch(Rectangle((x, 0.395), 0.270, 0.360, facecolor="#fafafb",
                               edgecolor=LIGHT, linewidth=1.0))
        ax.add_patch(Rectangle((x, 0.745), 0.270, 0.010, facecolor=color,
                               edgecolor="none"))
        ax.text(x + 0.022, 0.700, title, fontsize=13, color=color,
                weight="bold", va="center")
        ax.text(x + 0.022, 0.648, who, fontsize=8.8, color=GRAY, va="center")
        ax.plot([x + 0.022, x + 0.248], [0.612, 0.612], color=LIGHT, lw=1.0)
        ax.text(x + 0.022, 0.575, "能覆盖", fontsize=8.6, color=GRAY,
                va="center")
        ax.text(x + 0.022, 0.525, cover, fontsize=9.2, color=DARK, va="center")
        ax.text(x + 0.022, 0.455, "卡在哪", fontsize=8.6, color=GRAY,
                va="center")
        ax.text(x + 0.022, 0.410, limit, fontsize=9.6, color=RED, va="center")

    ax.add_patch(Rectangle((0.055, 0.270), 0.890, 0.080, facecolor="#f7f4ef",
                           edgecolor=LIGHT, linewidth=1.0))
    ax.text(0.075, 0.310, "三条线挤的不是同一块地，但都在挤压“非英伟达不可”这句话。",
            fontsize=9.8, color=DARK, va="center", weight="bold")

    takeaway(fig, 0.165, "出货量翻面，不等于定价权翻面；溢价率才是这次被重估的东西。")
    footer(fig, "据 IDC 数据、安纳智芯 AX100 报道（科技日报、IT之家 2026-11-15）、英伟达入股英特尔公告（2025-09-18）整理；“能覆盖/卡在哪”为本文归纳。")
    fig.savefig(OUT + "图3_三条替代路径.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")
