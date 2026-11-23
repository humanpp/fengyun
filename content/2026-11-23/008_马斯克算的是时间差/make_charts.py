# -*- coding: utf-8 -*-
"""
《马斯克算的不是泡沫，是时间差》配套图表

事实口径：
  · 2026-11-21（当地）Keras 创始人 François Chollet 在 X 发帖，列出：GPU 现货价
    仍在涨、算力难锁定；HBM 与 DRAM 到 2029 年产能基本订满，存储紧张预计延续到
    2030 年代；前沿模型训练算力约每 5 个月翻一番；AI 推理业务利润率 70%–85%。
  · 2026-11-22 马斯克回复：让这么大规模的算力设备通电、冷却并稳定运行极其困难；
    "明年的现金短缺也会非常疯狂"；若全行业从支付算力成本到设备稳定创收的时间
    累计推迟数月，仅营运资金就可能需额外数千亿美元；并反问"这些钱从哪里来"。
  · 原帖背景：半导体制造商股票估值相对其预期利润偏低。
  · 孙正义曾接洽华尔街机构，商讨为最高 1 万亿美元收购 SK 海力士融资（The
    Information 报道，约合 1346 万亿韩元）；软银发言人称对该选项不再积极考虑；
    SK 海力士称并不知情，并指按韩国法律外资收购须事先获政府批准。
  · SK 集团总市值 2026-11-16 收盘勉强守住 1000 万亿韩元；SK 海力士 11-20 收盘
    111.3 万韩元。
  · 软银已累计向 OpenAI 投资 646 亿美元、持股约 13%；2026 上半财年净亏损
    7680 亿日元，愿景基金合并口径投资收益同比降 79.3%；第三笔 100 亿美元来自
    9 月发行的外币高级债券。

输出目录 = 脚本所在目录
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

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
    """付款到创收之间的那段真空"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "马斯克算的不是泡沫，是时间差",
           "钱在设备通电之前就要付，收入要等设备稳定运行之后才来")

    boxes = [
        (0.055, "① 付钱", "买 GPU、建机房\n资本开支先出去", NAVY),
        (0.375, "② 通电、冷却、稳定运行", "并网、散热、调优\n这一段最容易拖", RED),
        (0.695, "③ 稳定创收", "推理收入开始覆盖\n折旧与电费", TEAL),
    ]
    for x, title, note, color in boxes:
        card(ax, x, 0.480, 0.260, 0.190, color, lw=1.5)
        ax.text(x + 0.022, 0.612, title, fontsize=10.4, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(x + 0.022, 0.560, note, fontsize=9.0, color=SLATE,
                ha="left", va="top", linespacing=1.8, zorder=6)

    for x0 in (0.320, 0.640):
        ax.add_patch(FancyArrowPatch((x0, 0.575), (x0 + 0.048, 0.575),
                                     arrowstyle="-|>", mutation_scale=16,
                                     color=GRAY, lw=1.6))

    ax.add_patch(FancyArrowPatch((0.380, 0.440), (0.632, 0.440),
                                 arrowstyle="<|-|>", mutation_scale=13,
                                 color=RED, lw=1.3))
    ax.text(0.506, 0.408, "这一段若累计推迟数月", fontsize=9.2, color=RED,
            ha="center", va="top")

    card(ax, 0.045, 0.205, 0.910, 0.150, NAVY, face=PALE, lw=1.2)
    ax.text(0.070, 0.318, "推迟的代价：", fontsize=9.8, color=NAVY,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.070, 0.272,
            "全行业仅营运资金就需额外投入数千亿美元。马斯克的反问是——这些钱从哪里来？",
            fontsize=9.8, color=SLATE, ha="left", va="center", zorder=6)

    punchline(fig, "芯片买得到，电和冷却不一定按时到；收入更不会。")
    footer(fig, "事实来源：马斯克 2026-11-22 在 X 的回复（经每经、财联社、澎湃、Business Insider 转述）")
    fig.savefig(OUT + "图1_时间差.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """1 万亿美元是什么量级"""
    fig = plt.figure(figsize=(12, 6.9))

    header(fig, "1 万亿美元是什么量级",
           "报价超过了整个 SK 集团的总市值")

    ax = fig.add_axes([0.115, 0.360, 0.360, 0.390])
    labels = ["SK 集团总市值\n2026-11-16 收盘", "传出收购报价\n最高 1 万亿美元"]
    vals = [1000, 1346]
    bars = ax.barh([0, 1], vals, height=0.40,
                   color=[LIGHT, RED], zorder=3)
    ax.set_yticks([0, 1])
    ax.set_yticklabels(labels, fontsize=9.2, color=SLATE)
    ax.set_xlim(0, 1650)
    ax.set_ylim(-0.60, 1.60)
    ax.set_xticks([])
    ax.set_title("单位：万亿韩元", fontsize=10.0, color=SLATE, pad=12)
    for spine in ("top", "right", "bottom"):
        ax.spines[spine].set_visible(False)
    ax.spines["left"].set_color(LIGHT)
    ax.tick_params(colors=GRAY)
    for b, v in zip(bars, vals):
        ax.text(v + 30, b.get_y() + b.get_height() / 2, "%d" % v,
                fontsize=11.0, color=DARK, weight="bold", va="center")

    axf = new_axes(fig)
    card(axf, 0.520, 0.345, 0.435, 0.405, TEAL, lw=1.4)
    axf.text(0.545, 0.700, "出钱的这一边", fontsize=10.6, color=TEAL,
             weight="bold", ha="left", va="center", zorder=6)
    axf.text(0.545, 0.640, "646 亿美元", fontsize=15.0, color=DARK,
             weight="bold", ha="left", va="center", zorder=6)
    axf.text(0.545, 0.598, "软银已累计投入 OpenAI，持股约 13%", fontsize=8.8,
             color=SLATE, ha="left", va="center", zorder=6)
    axf.text(0.545, 0.548,
             "2026 上半财年净亏损 7680 亿日元；\n"
             "愿景基金投资收益同比降 79.3%；\n"
             "第三笔 100 亿美元靠 9 月发债筹来。",
             fontsize=8.8, color=SLATE, ha="left", va="top",
             linespacing=1.85, zorder=6)
    axf.text(0.545, 0.432,
             "软银：对该选项不再积极考虑\nSK 海力士：并不知情；外资收购须韩国政府批准",
             fontsize=8.4, color=GRAY, ha="left", va="top",
             linespacing=1.8, zorder=6)

    axf.text(0.115, 0.290,
             "存储的战略价值被推到万亿级，愿意掏万亿的资金池没有同步变大。",
             fontsize=9.8, color=DARK, ha="left", va="center")

    punchline(fig, "万亿不是一个估值，是一次融资能不能凑出来的问题。")
    footer(fig, "事实来源：The Information 报道（经第一财经、韩联社、东亚日报、Digitimes 转述）；"
                "SK 集团总市值见 2026-11-16 韩媒收盘数据；软银财报见 2026-11-10 披露")
    fig.savefig(OUT + "图2_万亿的量级.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """三个约束要同时对上"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "三个约束，一个都不能慢",
           "芯片、并网、资金池，扩产的节奏取决于最慢的那一个")

    cols = [
        ("芯片供给", "HBM 与 DRAM 到 2029 年\n产能基本订满，紧张预计\n延续到 2030 年代", "紧", SLATE),
        ("并网时间", "通电、冷却、稳定运行\n极其困难；投运每晚一个\n月，现金就多垫一个月", "慢", RED),
        ("资金池", "愿意为万亿级资产出钱的\n机构没有同步增加；融资\n意愿跟不上资产定价", "缺", NAVY),
    ]
    x = 0.045
    w = 0.288
    for title, note, chip, color in cols:
        card(ax, x, 0.360, w, 0.330, color, lw=1.5)
        ax.text(x + 0.022, 0.630, title, fontsize=11.4, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(x + 0.022, 0.575, note, fontsize=9.0, color=SLATE,
                ha="left", va="top", linespacing=1.9, zorder=6)
        card(ax, x + 0.022, 0.395, 0.078, 0.048, color, face=color, lw=1.0)
        ax.text(x + 0.061, 0.419, chip, fontsize=9.0, color="white",
                weight="bold", ha="center", va="center", zorder=8)
        x += w + 0.023

    ax.text(0.045, 0.285,
            "三家各说各的：马斯克说时间差，软银碰壁在融资与审查，SK 海力士说不知情。",
            fontsize=9.4, color=SLATE, ha="left", va="center")
    ax.text(0.045, 0.222,
            "但它们指向同一件事——扩产不是买到芯片就结束，而是要等电、等收入、等钱同时到位。",
            fontsize=9.4, color=DARK, ha="left", va="center")

    punchline(fig, "AI 扩张的瓶颈，正在从“有没有芯片”变成“钱能不能撑到收入来”。")
    footer(fig, "事实来源：Chollet 2026-11-21 帖（HBM/DRAM 产能，经新浪财经转述）；"
                "马斯克 2026-11-22 回复；The Information 报道及双方回应")
    fig.savefig(OUT + "图3_三个约束.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)