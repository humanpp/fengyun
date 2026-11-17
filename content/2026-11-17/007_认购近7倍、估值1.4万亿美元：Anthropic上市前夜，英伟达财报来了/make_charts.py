# -*- coding: utf-8 -*-
"""
《认购近 7 倍、估值 1.4 万亿美元：Anthropic 上市前夜，英伟达财报来了》配套图表
事实口径：Anthropic IPO 认购订单接近拟发行股份的 7 倍，高于 11 月 12 日约 6 倍；
拟发行 8.25 亿股、每股 70—78 美元，按上限估值约 1.4 万亿美元，叠加私募配售
整体筹资目标最高 904 亿美元；11 月 18 日定价、11 月 19 日以 "ANT" 登陆纳斯达克。
英伟达美东 11 月 17 日盘后（北京时间 11 月 18 日凌晨）发布 FY27Q3 财报，为黄仁勋
离任后首份；市场预期营收 1087—1091 亿美元、同比增长约 90%，关注四季度指引能否
达到约 1243 亿美元，以及 Vera Rubin 平台能否按期交付；董事会未讨论让黄仁勋重返
CEO，重点是推进独立调查。
风格：克制传媒风，白底、低饱和配色、标题即结论
输出目录 = 脚本所在目录
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
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

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep


def footer(fig, text):
    fig.text(0.045, 0.020, text, fontsize=8.4, color=GRAY, ha="left", va="bottom")


def punchline(fig, text):
    fig.text(0.045, 0.072, text, fontsize=10.4, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


# ---------------------------------------------------------------- 图 1
def fig1():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.135, 0.910, 0.690])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "定价前夜，认购涨到近 7 倍", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.888, "11 月 12 日约 6 倍，11 月 17 日近 7 倍，11 月 18 日定价",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    # 左：两次读数
    ax.text(0.020, 0.905, "超额认购倍数", fontsize=10.4, color=SLATE, va="center")

    rows = [("11 月 12 日", 6.0, "约 6 倍", SLATE),
            ("11 月 17 日", 7.0, "近 7 倍", RED)]
    bar_h = 0.095
    for i, (day, val, label, color) in enumerate(rows):
        y = 0.700 - i * 0.215
        w = val / 8.0 * 0.40
        ax.text(0.020, y + bar_h + 0.048, day, fontsize=9.4, color=GRAY,
                va="center")
        ax.add_patch(Rectangle((0.020, y), w, bar_h, facecolor=color,
                               edgecolor="none"))
        ax.text(0.020 + w + 0.016, y + bar_h / 2, label, fontsize=12.5,
                color=color, weight="bold", va="center")

    ax.text(0.020, 0.235, "认购可以撤、可以缩，配售比例由承销商定", fontsize=9.6,
            color=GRAY, va="center")

    # 右：发行参数
    ax.add_patch(Rectangle((0.520, 0.230), 0.455, 0.560, facecolor=PALE,
                           edgecolor=LIGHT, linewidth=1.0))
    ax.add_patch(Rectangle((0.520, 0.777), 0.455, 0.013, facecolor=NAVY,
                           edgecolor="none"))
    ax.text(0.545, 0.720, "发行参数", fontsize=13, color=NAVY, weight="bold",
            va="center")

    params = [
        ("发行股数", "8.25 亿股"),
        ("价格区间", "70—78 美元/股"),
        ("上限估值", "约 1.4 万亿美元"),
        ("合计筹资目标", "最高 904 亿美元"),
    ]
    for i, (label, value) in enumerate(params):
        y = 0.628 - i * 0.105
        ax.text(0.545, y, label, fontsize=9.8, color=SLATE, va="center")
        ax.text(0.950, y, value, fontsize=12, color=DARK, weight="bold",
                ha="right", va="center")
        if i < len(params) - 1:
            ax.plot([0.545, 0.950], [y - 0.052, y - 0.052], color=LIGHT,
                    linewidth=0.9)

    ax.text(0.545, 0.245, "含私募配售", fontsize=8.8, color=GRAY, va="center")

    punchline(fig, "多出来的这一档，不是基本面，是表态。")
    footer(fig, "据招股文件与 11 月 12 日「约 6 倍」、11 月 17 日「近 7 倍」两轮公开报道整理。")
    fig.savefig(OUT + "图1_认购前夜.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.135, 0.910, 0.690])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "今夜的考题不是 1090 亿", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.888, "英伟达 FY27Q3，美东 11 月 17 日盘后 · 北京时间 11 月 18 日凌晨",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    base_y, max_h, scale = 0.245, 0.560, 1400.0
    bars = [(0.115, 1090, "当季营收预期", "1087—1091 亿", NAVY),
            (0.345, 1243, "四季度需要摸到", "约 1243 亿", RED)]

    ax.plot([0.080, 0.520], [base_y, base_y], color=LIGHT, linewidth=1.6)
    for x, val, cap, note, color in bars:
        h = max_h * val / scale
        ax.add_patch(Rectangle((x, base_y), 0.135, h, facecolor=color,
                               edgecolor="none"))
        ax.text(x + 0.0675, base_y + h + 0.038, f"{val:,}", fontsize=17,
                color=color, weight="bold", ha="center", va="center")
        ax.text(x + 0.0675, base_y - 0.045, cap, fontsize=9.6, color=SLATE,
                ha="center", va="center")
        ax.text(x + 0.0675, base_y - 0.088, note + "美元", fontsize=8.8,
                color=GRAY, ha="center", va="center")

    ax.text(0.345 + 0.0675, base_y - 0.131, "较当季预期约 +14%", fontsize=10.4,
            color=RED, weight="bold", ha="center", va="center")

    # 右侧两个补充
    ax.plot([0.560, 0.560], [base_y - 0.090, 0.830], color=LIGHT, linewidth=1.0)

    items = [
        ("同比", "约 +90%", "当季营收同比增速", NAVY),
        ("第二道题", "Vera Rubin 能否按期交付", "不是财报科目，但决定明年曲线", SLATE),
    ]
    for i, (tag, big, note, color) in enumerate(items):
        y = 0.700 - i * 0.230
        ax.text(0.600, y, tag, fontsize=9.6, color=GRAY, va="center")
        ax.text(0.600, y - 0.062, big, fontsize=14, color=color, weight="bold",
                va="center")
        ax.text(0.600, y - 0.118, note, fontsize=9.2, color=GRAY, va="center")

    punchline(fig, "一个季度环比再涨 14%，比一份超预期的季报更值得看。")
    footer(fig, "当季与四季度数字为市场预期口径；+14% 为按 1090 亿与 1243 亿所做换算。")
    fig.savefig(OUT + "图2_今夜的数字.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.135, 0.910, 0.690])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "定价要看两份回答", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.888, "一份来自英伟达，一份来自董事会", fontsize=10.8,
             color=GRAY, ha="left", va="top")

    top, bot = 0.860, 0.200

    ax.add_patch(Rectangle((0.020, bot), 0.450, top - bot, facecolor=PALE,
                           edgecolor=LIGHT, linewidth=1.0))
    ax.add_patch(Rectangle((0.020, top - 0.013), 0.450, 0.013, facecolor=SLATE,
                           edgecolor="none"))
    ax.text(0.048, top - 0.058, "已经确定", fontsize=13.5, color=SLATE,
            weight="bold", va="center")

    known = [
        ("认购倍数", "接近 7 倍"),
        ("筹资目标", "最高 904 亿美元"),
        ("上限估值", "约 1.4 万亿美元"),
        ("挂牌", "11 月 19 日 · ANT"),
    ]

    ax.add_patch(Rectangle((0.530, bot), 0.450, top - bot, facecolor=PALE,
                           edgecolor=LIGHT, linewidth=1.0))
    ax.add_patch(Rectangle((0.530, top - 0.013), 0.450, 0.013, facecolor=RED,
                           edgecolor="none"))
    ax.text(0.558, top - 0.058, "还没回答", fontsize=13.5, color=RED,
            weight="bold", va="center")

    open_items = [
        ("四季度指引", "能否摸到约 1243 亿美元"),
        ("交付", "Vera Rubin 能否按期"),
        ("治理", "独立调查的结论"),
        ("人事", "董事会未讨论黄仁勋复职"),
    ]

    for i, ((l1, v1), (l2, v2)) in enumerate(zip(known, open_items)):
        y = 0.735 - i * 0.145
        ax.text(0.048, y, l1, fontsize=9.8, color=SLATE, va="center")
        ax.text(0.048, y - 0.055, v1, fontsize=11.8, color=DARK, weight="bold",
                va="center")
        ax.text(0.558, y, l2, fontsize=9.8, color=SLATE, va="center")
        ax.text(0.558, y - 0.055, v2, fontsize=11.8, color=RED, weight="bold",
                va="center")

    punchline(fig, "发行阶段的需求，证明不了上市后的价格。")
    footer(fig, "据招股文件、11 月 17 日认购读数、英伟达 FY27Q3 预期及董事会进展报道整理；董事会是否讨论复职为报道口径。")
    fig.savefig(OUT + "图3_两份回答.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")
