# -*- coding: utf-8 -*-
"""
《600 亿压顶，MiMo 的钱从哪来》配套图表

事实口径（小米 2026 中报 / Q2 业绩公告，经车东西、老虎社区、雪球转述；
投资人反馈与 7 月摸底经《资本不熬夜》/虎嗅、AI·RADAR 转述）：
  · 手机毛利率：上年同期 11.5% → 二季报 8.5%。
  · 智能电动汽车及AI等创新业务：Q2 毛利率 26.4% → 19.2%；
    Q2 经营亏损 3 亿元 → 26 亿元；Q1 亏损 31 亿元，上半年合计 57 亿元；
    上半年分部收入 448 亿元、同比 +12.3%，经营开支 145 亿元、同比 +34.8%。
  · CFO 林世伟：毛利率下降含“AI 业务相关成本增加”；“大模型业务收入刚开始
    起步，对板块毛利率有负面影响”。
  · 罗福莉 7 月接触几轮基金投资人摸底单独融资，反馈不乐观，资金向头部集中。
  · 上半年「其他相关业务」收入 19 亿元、同比 +62.7%（含汽车售后服务）。
  · API 价目：MiMo-V2.6-Pro 每百万 token 输入 3 元、输出 6 元；
    小米披露在相近智能水平下价格为部分海外模型的 1/20 至 1/60。

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


def small_axes(fig, rect):
    ax = fig.add_axes(rect)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    for spine in ("left", "bottom"):
        ax.spines[spine].set_color(LIGHT)
    ax.tick_params(colors=GRAY, labelsize=8.2)
    return ax


# ---------------------------------------------------------------- 图 1
def fig1():
    """三条线同时往下走"""
    fig = plt.figure(figsize=(12, 6.9))

    header(fig, "三条线同时往下走",
           "手机毛利、创新业务毛利、创新业务亏损，都在往不利的方向走")

    panels = [
        (0.070, "手机毛利率", ["上年同期", "二季报"], [11.5, 8.5],
         "%", 14, NAVY, "零部件涨价"),
        (0.375, "创新业务毛利率（Q2）", ["2025 Q2", "2026 Q2"], [26.4, 19.2],
         "%", 30, RED, "AI 业务成本增加"),
        (0.680, "创新业务经营亏损（Q2）", ["2025 Q2", "2026 Q2"], [3, 26],
         "亿元", 30, SLATE, "同比扩大约 767%"),
    ]

    for x0, title, labels, vals, unit, top, color, note in panels:
        ax = small_axes(fig, [x0, 0.360, 0.245, 0.380])
        bars = ax.bar([0, 1], vals, width=0.46, color=[LIGHT, color], zorder=3)
        ax.set_xticks([0, 1])
        ax.set_xticklabels(labels, fontsize=9.0, color=SLATE)
        ax.set_ylim(0, top)
        ax.set_yticks([])
        ax.set_title(title, fontsize=10.0, color=SLATE, pad=10)
        for b, v in zip(bars, vals):
            txt = ("%.1f%%" % v) if unit == "%" else ("%d 亿元" % v)
            ax.text(b.get_x() + b.get_width() / 2, v + top * 0.035, txt,
                    fontsize=10.4, color=DARK, ha="center", va="bottom")
        ax.text(0.5, -0.28, note, transform=ax.transAxes, fontsize=8.2,
                color=GRAY, ha="center", va="top")

    axf = new_axes(fig)
    card(axf, 0.045, 0.215, 0.910, 0.085, LIGHT, face=PALE, lw=1.0)
    axf.text(0.068, 0.258,
             "CFO 林世伟在 Q2 电话会上把毛利率下滑归因于三件事：SU7 Ultra 交付占比下降、"
             "核心零部件涨价，以及 AI 业务相关成本增加。",
             fontsize=9.0, color=SLATE, ha="left", va="center", zorder=6)

    punchline(fig, "AI 还没挣到钱，先出现在毛利率的下降原因里。")
    footer(fig, "事实来源：小米 2026 年中期业绩与 Q2 业绩公告（经车东西、老虎社区、雪球转述）")
    fig.savefig(OUT + "图1_三条线同时往下走.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """估值摸底：一边是找不到生态位，一边是闭环场景"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "7 月摸的底，11 月才见报",
           "罗福莉问了几轮基金，反馈不算热情")

    card(ax, 0.045, 0.700, 0.910, 0.135, NAVY, lw=1.2)
    ax.text(0.070, 0.795, "7 月", fontsize=13.0, color=NAVY, weight="bold",
            ha="left", va="center", zorder=6)
    ax.text(0.150, 0.795,
            "罗福莉接触几轮基金投资人，摸底 MiMo 单独融资的可能；"
            "比 11 月 18 日消息见报早了四个月。",
            fontsize=9.6, color=SLATE, ha="left", va="center", zorder=6)
    ax.text(0.070, 0.733,
            "同期背景：手机毛利率 11.5%→8.5%，上半年创新业务经营亏损 57 亿元。",
            fontsize=9.0, color=SLATE, ha="left", va="center", zorder=6)

    card(ax, 0.045, 0.320, 0.440, 0.320, RED, lw=1.5)
    ax.text(0.068, 0.596, "一种看法：生态位不好找", fontsize=11.0, color=RED,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.068, 0.548,
            "独立后的 MiMo 要和月之暗面、DeepSeek 这类\n"
            "纯模型公司同场竞争，但它的订单主要来自\n"
            "小米自己。兴趣一般。",
            fontsize=9.4, color=SLATE, ha="left", va="top",
            linespacing=1.9, zorder=6)
    ax.text(0.068, 0.408,
            "反馈：资金越来越集中在头部，\nMiMo 还没到投资人对头部的标准。",
            fontsize=9.0, color=DARK, ha="left", va="top",
            linespacing=1.75, zorder=6)

    card(ax, 0.510, 0.320, 0.445, 0.320, TEAL, lw=1.5)
    ax.text(0.533, 0.596, "另一种看法：场景是现成的", fontsize=11.0, color=TEAL,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.533, 0.548,
            "小米的智能家居和智能座舱能给 MiMo\n"
            "现成的落地场景，十几亿台设备、\n"
            "7.6 亿月活，是别的模型公司没有的。",
            fontsize=9.4, color=SLATE, ha="left", va="top",
            linespacing=1.9, zorder=6)
    ax.text(0.533, 0.408,
            "两种看法来自同一个事实：\nMiMo 的价值和小米生态绑在一起。",
            fontsize=9.0, color=DARK, ha="left", va="top",
            linespacing=1.75, zorder=6)

    punchline(fig, "看空的和看多的，争的其实是同一件事：它能不能离开小米。")
    footer(fig, "事实来源：《资本不熬夜》2026-11-23（经虎嗅转载）；AI·RADAR 2026-11-18；"
                "小米 2026 中期业绩；月活与设备数为小米 2026 年 6 月披露口径")
    fig.savefig(OUT + "图2_估值摸底.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """三条造血的通道，最后汇进一个含汽车售后的数"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "MiMo 现在靠什么挣钱",
           "三条通道都有，但都还小；公开口径里没有单独营收")

    rows = [
        ("会员订阅", "桌面客户端已上线会员订阅", NAVY),
        ("开放平台 API", "按量计费：每百万 token 输入 3 元、输出 6 元", RED),
        ("集团内部调用", "小爱同学的基础模型由 MiMo 团队提供", TEAL),
    ]
    y = 0.620
    for name, note, color in rows:
        card(ax, 0.045, y, 0.395, 0.100, color, lw=1.3)
        ax.text(0.070, y + 0.064, name, fontsize=11.0, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(0.070, y + 0.030, note, fontsize=8.8, color=SLATE,
                ha="left", va="center", zorder=6)
        ax.add_patch(FancyArrowPatch((0.448, y + 0.050), (0.575, 0.520),
                                     arrowstyle="-|>", mutation_scale=13,
                                     color=GRAY, lw=1.2,
                                     connectionstyle="arc3,rad=0.06"))
        y -= 0.135

    card(ax, 0.580, 0.400, 0.375, 0.245, NAVY, lw=1.5)
    ax.text(0.603, 0.595, "「其他相关业务」收入", fontsize=9.6, color=GRAY,
            ha="left", va="center", zorder=6)
    ax.text(0.603, 0.535, "19 亿元", fontsize=21.0, color=NAVY,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.603, 0.472, "同比 +62.7%（上半年）\n含汽车售后服务，不等于 MiMo 营收",
            fontsize=8.8, color=SLATE, ha="left", va="top",
            linespacing=1.8, zorder=6)

    card(ax, 0.045, 0.195, 0.910, 0.115, LIGHT, face=PALE, lw=1.0)
    ax.text(0.070, 0.283,
            "价格是 MiMo 手里最硬的牌：小米披露，在相近模型智能水平下，",
            fontsize=9.4, color=SLATE, ha="left", va="center", zorder=6)
    ax.text(0.070, 0.232, "MiMo-V2.6-Pro 的价格仅为部分海外模型的 1/20 至 1/60。",
            fontsize=10.4, color=DARK, weight="bold", ha="left", va="center",
            zorder=6)

    punchline(fig, "便宜能换来订单，换不来一次训练的账单。")
    footer(fig, "事实来源：小米开放平台价目与官方披露（经观察者网、观点网转述）；"
                "上半年分部数据见小米 2026 中期业绩")
    fig.savefig(OUT + "图3_MiMo靠什么挣钱.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)
