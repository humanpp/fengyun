# -*- coding: utf-8 -*-
"""
《退款排队 5 到 8 年：700 多人、上千万，和一句没人信得过的承诺》配套图表
事实口径：头部羽毛球主播"龙宝羽毛球"以"工厂直供""限时低价"带货、多场直播
销售额破百万元；自上月下旬起订单延迟发货、物流停滞、客服失联；退款回应为
"排队 5 至 8 年"；随后小程序关停、账号停更；受害者自发统计 700 多人、超千万元；
2026-11-11 武汉警方确认立案、移交经侦大队，定性经营不善、资金链断裂无法履约。
风格：克制传媒风，白底、低饱和配色、标题即结论
输出目录 = 脚本所在目录
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch

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

    fig.text(0.045, 0.955, "三个数字，一条时间线", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.888, "从 10 月下旬的延迟发货，到 11 月 11 日的立案",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    stats = [
        (0.150, "700+", "人", "受害者自统计", NAVY),
        (0.500, "超千万", "元", "涉及金额自统计", NAVY),
        (0.850, "5—8", "年", "退款排队期", RED),
    ]
    for x, num, unit, label, color in stats:
        ax.text(x - 0.030, 0.905, num, fontsize=26, color=color, weight="bold",
                ha="right", va="center")
        ax.text(x - 0.022, 0.890, unit, fontsize=11, color=color, va="center")
        ax.text(x, 0.828, label, fontsize=9.4, color=GRAY, ha="center",
                va="center")

    y_line = 0.500
    ax.plot([0.075, 0.925], [y_line, y_line], color=LIGHT, linewidth=2.4,
            solid_capstyle="round", zorder=1)

    nodes = [
        (0.090, "10 月下旬", "发货", "大量订单延迟发货\n物流停滞不动", SLATE),
        (0.295, "之后", "失联", "客服失联\n没人回消息", SLATE),
        (0.500, "退款时", "回应", "所有退款排队\n5 至 8 年结清", NAVY),
        (0.705, "再之后", "关店", "店铺小程序关停\n账号停更", SLATE),
        (0.910, "11 月 11 日", "立案", "武汉警方确认立案\n定性：资金链断裂", RED),
    ]

    for x, when, stage, body, color in nodes:
        ax.scatter([x], [y_line], s=320, facecolor=color, edgecolor="white",
                   linewidth=2.0, zorder=3)
        ax.text(x, 0.600, when, fontsize=9.2, color=GRAY, ha="center",
                va="center")
        ax.text(x, 0.556, stage, fontsize=12, color=color, weight="bold",
                ha="center", va="center")
        ax.text(x, 0.420, body, fontsize=9.4, color=DARK, ha="center",
                va="top", linespacing=1.75)

    punchline(fig, "前两个数字是损失，第三个数字是态度。")
    footer(fig, "据受害者自发统计与 2026 年 11 月 11 日武汉警方确认信息整理。")
    fig.savefig(OUT + "图1_三个数字.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.135, 0.910, 0.690])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "5 到 8 年，换算成别的东西", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.882, "同一句话，换个单位就有重量了", fontsize=10.8,
             color=GRAY, ha="left", va="top")

    ax.text(0.155, 0.640, "5—8", fontsize=62, color=RED, weight="bold",
            ha="center", va="center")
    ax.text(0.155, 0.520, "年", fontsize=20, color=RED, weight="bold",
            ha="center", va="center")
    ax.text(0.155, 0.440, "退款排队期", fontsize=10.4, color=GRAY,
            ha="center", va="center")
    ax.text(0.155, 0.390, "合 60—96 个月", fontsize=9.6, color=GRAY,
            ha="center", va="center")

    ax.plot([0.320, 0.320], [0.330, 0.800], color=LIGHT, linewidth=1.2)

    rows = [
        ("约 2920 天", "按 8 年算。平均到每一天，要退 3400 多元才够上千万。"),
        ("一个孩子读完小学和高中", "8 年，正好够他从一年级念到毕业。"),
        ("2026 → 2034", "现在排上队，兑现是下一个十年的事。"),
        ("约 292 万元", "就算每天退 1000 元，8 年也只退到总额的三成不到。"),
    ]

    for i, (value, note) in enumerate(rows):
        y = 0.760 - i * 0.150
        ax.text(0.370, y, value, fontsize=15.5, color=DARK, weight="bold",
                va="center")
        ax.text(0.370, y - 0.058, note, fontsize=9.6, color=SLATE,
                va="center")

    punchline(fig, "这不是还款计划，是把「还不上」翻译成了一句像流程的话。")
    footer(fig, "时间与金额换算基于 700 多人、超千万元的自统计数据，非当事人承诺。")
    fig.savefig(OUT + "图2_换算.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.135, 0.910, 0.690])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "信任攒得慢，兑得快", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.882, "三段：一条视频一条视频地攒，一单接一单地花",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    steps = [
        ("01", "攒信任", "常年解说、拆拍、测评，\n讲得清楚，圈里认。",
         "这条路他走了好几年", NAVY),
        ("02", "变现", "「工厂直供」「限时低价」，\n多场直播销售额破百万。",
         "信任一次性兑成订单", NAVY),
        ("03", "断链", "延迟发货 → 失联 →\n排队 5—8 年 → 关停。",
         "预付款早就不在账上", RED),
    ]

    top, bot = 0.780, 0.320
    for i, (no, title, body, note, color) in enumerate(steps):
        x0 = 0.012 + i * 0.338
        ax.add_patch(Rectangle((x0, bot), 0.300, top - bot, facecolor=PALE,
                               edgecolor=LIGHT, linewidth=1.0))
        ax.add_patch(Rectangle((x0, top - 0.012), 0.300, 0.012, facecolor=color,
                               edgecolor="none"))
        ax.text(x0 + 0.024, top - 0.070, no, fontsize=13, color=GRAY,
                weight="bold", va="center")
        ax.text(x0 + 0.024, top - 0.150, title, fontsize=15.5, color=color,
                weight="bold", va="center")
        ax.text(x0 + 0.024, top - 0.235, body, fontsize=9.6, color=DARK,
                va="top", linespacing=1.8)
        ax.text(x0 + 0.024, bot + 0.070, note, fontsize=9.4, color=color,
                va="center")
        if i < 2:
            ax.annotate("", xy=(x0 + 0.330, (top + bot) / 2),
                        xytext=(x0 + 0.306, (top + bot) / 2),
                        arrowprops=dict(arrowstyle="-|>", color=GRAY,
                                        linewidth=1.3, shrinkA=0, shrinkB=0))

    punchline(fig, "低价不是问题，「先收钱、后发货」才是。")
    footer(fig, "据 2026 年 11 月 11 日武汉警方确认信息及受害者自统计整理；资金腾挪为同类案件的一般情形，非本案认定。")
    fig.savefig(OUT + "图3_信任变现.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")
