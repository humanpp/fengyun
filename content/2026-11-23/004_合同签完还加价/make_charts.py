# -*- coding: utf-8 -*-
"""
《合同签完还能加价 45%：AI 服务器的账开始往回算》配套图表

事实口径（FT 2026-11-22，经 Chip Dispatch / Seeking Alpha / DIGITIMES / 经济观察网转述）：
  · 整机订单加价 25% / 30% / 45%；GPU 服务器至少 20%–30%；
    大内存 CPU 节点价格三倍以上；内存自 2024 年初涨超 400%（引摩根大通）。
  · XTX 诉戴尔：5.49 亿美元固定价、另付 500 万美元买价格确定性、
    戴尔追加 6200 万–7000 万美元、1680 台服务器、约 7000 万美元托管、延期至 12 月。
  · 亚马逊接近 75 亿美元收购 Decart（FT 2026-11-21）；Anthropic 曾出价约 60 亿美元后放弃。

输出目录 = 脚本所在目录
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei"]
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
TEAL = "#3f6f6b"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep

Y_TITLE = 0.958
Y_SUB = 0.898
Y_PUNCH = 0.068
Y_FOOT = 0.020


def header(fig, title, sub):
    fig.text(0.045, Y_TITLE, title, fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, Y_SUB, sub, fontsize=10.4, color=GRAY,
             ha="left", va="top")


def footer(fig, text):
    fig.text(0.045, Y_FOOT, text, fontsize=7.6, color=GRAY,
             ha="left", va="bottom")


def punchline(fig, text):
    fig.text(0.045, Y_PUNCH, text, fontsize=10.4, color=DARK,
             ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


def card(ax, x, y, w, h, edge, face="white", lw=1.2, z=2):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.004,rounding_size=0.014",
        facecolor=face, edgecolor=edge, linewidth=lw, zorder=z))


def new_axes(fig):
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return ax


# ---------------------------------------------------------------- 图 1
def fig1():
    """左：加价三档；右：成本推手"""
    fig = plt.figure(figsize=(12, 6.9))

    header(fig, "加价从哪来",
           "整机订单 25%–45%，推手是内存")

    ax = fig.add_axes([0.085, 0.335, 0.400, 0.420])
    vals = [25, 30, 45]
    bars = ax.bar([0, 1, 2], vals, width=0.50, color=NAVY, zorder=3)
    ax.set_xticks([0, 1, 2])
    ax.set_xticklabels(["常见档", "较高档", "最高档"], fontsize=9.6, color=SLATE)
    ax.set_ylim(0, 55)
    ax.set_title("已签合同的加价幅度  %", fontsize=10.6, color=SLATE, pad=12)
    ax.tick_params(axis="y", labelsize=8.2, colors=GRAY)
    ax.grid(axis="y", color=LIGHT, linewidth=0.8, alpha=0.7, zorder=0)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    for spine in ("left", "bottom"):
        ax.spines[spine].set_color(LIGHT)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + 1.2, "%d%%" % v,
                fontsize=10.4, color=DARK, ha="center", va="bottom")

    rows = [
        ("内存（2024 年初至今）", "+400% 以上", NAVY, "引摩根大通研究"),
        ("大内存 CPU 节点", "价格三倍以上", RED, "涨得比 GPU 整机凶"),
        ("GPU 服务器", "+20%–30%", TEAL, "含英伟达芯片的整机"),
    ]
    y = 0.640
    for name, value, color, note in rows:
        fig.text(0.560, y + 0.030, name, fontsize=9.2, color=GRAY,
                 ha="left", va="center")
        fig.text(0.560, y - 0.020, value, fontsize=15.0, color=color,
                 weight="bold", ha="left", va="center")
        fig.text(0.560, y - 0.062, note, fontsize=8.2, color=SLATE,
                 ha="left", va="center")
        y -= 0.150

    fig.text(0.560, 0.228,
             "厂商未确认：HPE、超微拒评，戴尔、联想未回应。",
             fontsize=8.4, color=GRAY, ha="left", va="center")

    punchline(fig, "合同锁的是价格，不是成本。")
    footer(fig, "事实来源：FT 2026-11-22（经 Chip Dispatch、Seeking Alpha、经济观察网转述）")
    fig.savefig(OUT + "图1_加价从哪来.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """一张订单的时间线"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "一张订单的后半程",
           "签字不是终点，交付前还有一次报价")

    ax.add_patch(FancyArrowPatch((0.070, 0.560), (0.930, 0.560),
                                 arrowstyle="-|>", mutation_scale=18,
                                 color=LIGHT, lw=2.0))
    nodes = [
        (0.135, "6 月签约", "5.49 亿美元固定价\n另付 500 万买确定性", NAVY),
        (0.395, "排产、等交付", "设备备齐要几个月\n价格在这段时间变了", SLATE),
        (0.655, "交付前重新报价", "+25%–45%\nXTX 被要求再加 6200–7000 万美元", RED),
        (0.900, "结果", "多数客户付了\nXTX 起诉，延期到 12 月", GRAY),
    ]
    for x, title, note, color in nodes:
        ax.plot([x], [0.560], "o", markersize=9, color=color,
                markeredgecolor="white", markeredgewidth=1.2, zorder=6)
        ax.text(x, 0.640, title, fontsize=11.2, color=DARK,
                weight="bold", ha="center", va="bottom")
        ax.text(x, 0.505, note, fontsize=9.0, color=SLATE,
                ha="center", va="top", linespacing=1.7)

    card(ax, 0.045, 0.245, 0.910, 0.175, LIGHT, face=PALE, lw=1.0)
    ax.text(0.070, 0.372, "为什么合同拦不住", fontsize=10.6, color=DARK,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.070, 0.320,
            "不少合同写的是“指示性价格”，不是锁死的成交价。买家原话：签的时候是个参考价，"
            "交付时可能高得离谱。",
            fontsize=9.2, color=SLATE, ha="left", va="center", zorder=6)
    ax.text(0.070, 0.276,
            "XTX 这笔：1680 台服务器、1.5 万平方米数据中心、约 7000 万美元进托管账户。",
            fontsize=9.2, color=SLATE, ha="left", va="center", zorder=6)

    punchline(fig, "加价发生在交付前，不是下一次采购。")
    footer(fig, "事实来源：FT 2026-11-22；爱尔兰时报 2026-06（XTX 案细节，经 Chip Dispatch 转述）")
    fig.savefig(OUT + "图2_订单时间线.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """硬件加价 vs 效率溢价"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "硬件与效率，两个价签",
           "同一周的两笔定价：硬件按合同加价，效率按公司估值")

    card(ax, 0.045, 0.405, 0.400, 0.300, RED, lw=1.5)
    ax.text(0.068, 0.655, "硬件：加价", fontsize=11.4, color=RED,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.068, 0.590, "+25%–45%", fontsize=20.0, color=DARK,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.068, 0.520, "戴尔、HPE、联想、超微\n对已签合同重新报价\n推手：内存涨 400% 以上",
            fontsize=9.6, color=SLATE, ha="left", va="top",
            linespacing=1.9, zorder=6)

    card(ax, 0.555, 0.405, 0.400, 0.300, TEAL, lw=1.5)
    ax.text(0.578, 0.655, "效率：被收购", fontsize=11.4, color=TEAL,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.578, 0.590, "75 亿美元", fontsize=20.0, color=DARK,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.578, 0.520, "亚马逊接近收购 Decart\n让模型在任何芯片上跑得更省\nAnthropic 曾出价约 60 亿美元后放弃",
            fontsize=9.6, color=SLATE, ha="left", va="top",
            linespacing=1.9, zorder=6)

    ax.add_patch(FancyArrowPatch((0.455, 0.555), (0.545, 0.555),
                                 arrowstyle="<|-|>", mutation_scale=16,
                                 color=GRAY, lw=1.4))
    ax.text(0.500, 0.598, "换", fontsize=9.0, color=GRAY,
            ha="center", va="center")

    ax.text(0.045, 0.335, "对自建数据中心的人来说，算力越贵，“省算力”就越值钱。",
            fontsize=10.0, color=DARK, ha="left", va="center")

    chips = ["算力租赁报价", "项目回本周期", "推理成本模型"]
    x = 0.045
    for text in chips:
        w = 0.240
        card(ax, x, 0.225, w, 0.070, LIGHT, lw=1.0)
        ax.text(x + w / 2, 0.260, text, fontsize=9.6, color=SLATE,
                ha="center", va="center", zorder=6)
        x += w + 0.025

    punchline(fig, "省算力，正在变成一门比卖算力更贵的生意。")
    footer(fig, "事实来源：FT 2026-11-22（加价）；FT 2026-11-21（Decart，经 Seeking Alpha、Livemint 转述）")
    fig.savefig(OUT + "图3_两个价签.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)
