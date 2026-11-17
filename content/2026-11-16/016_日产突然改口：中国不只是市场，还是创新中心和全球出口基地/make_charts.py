# -*- coding: utf-8 -*-
"""
《日产突然改口：中国不只是市场，还是创新中心和全球出口基地》配套图表
事实来源：日产（中国）2026 年 10 月在华销量 22,295 辆、同比 -67.1%（去年同期
67,855 辆），4 月 -30.8%、9 月 -61.6%，自 4 月起连续 7 个月同比下滑；
日系三强 2026 上半年在华销量（丰田 69.47 万、日产 23.70 万、本田 20.58 万）；
NISSAN DAY 2026-11-13 珠海
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


def bare(ax):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(LIGHT)
    ax.tick_params(colors=DARK, labelsize=10.5, length=0)
    ax.set_axisbelow(True)


# ---------------------------------------------------------------- 图 1
def fig1():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6.8),
                                   gridspec_kw={"width_ratios": [1.0, 1.15]})
    fig.subplots_adjust(left=0.075, right=0.965, top=0.700, bottom=0.215,
                        wspace=0.28)

    fig.text(0.045, 0.955, "日产在华：销量塌了，降幅还在扩大", fontsize=19,
             color=DARK, weight="bold", ha="left", va="top")
    fig.text(0.045, 0.882, "左：10 月单月同比；右：同比降幅逐季加速",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    # 左：2025 vs 2026 年 10 月
    bare(ax1)
    vals = [67855, 22295]
    cols = [LIGHT, NAVY]
    ax1.bar([0, 1], vals, width=0.52, color=cols, edgecolor="none")
    ax1.set_ylim(0, 82000)
    ax1.set_xlim(-0.62, 1.62)
    ax1.set_xticks([0, 1])
    ax1.set_xticklabels(["2025 年 10 月", "2026 年 10 月"], fontsize=11)
    ax1.set_yticks([0, 20000, 40000, 60000, 80000])
    ax1.set_yticklabels(["0", "2 万", "4 万", "6 万", "8 万"])
    ax1.grid(axis="y", color=LIGHT, linewidth=0.8, alpha=0.55)
    ax1.text(0, 67855 + 1600, "67,855", fontsize=13, color=SLATE,
             ha="center", va="bottom", weight="bold")
    ax1.text(1, 22295 + 1600, "22,295", fontsize=13, color=NAVY,
             ha="center", va="bottom", weight="bold")
    ax1.set_title("10 月单月销量（辆）", fontsize=12.5, color=DARK,
                  weight="bold", loc="left", pad=14)

    # 右：降幅加速
    bare(ax2)
    months = ["4 月", "9 月", "10 月"]
    drops = [30.8, 61.6, 67.1]
    ax2.bar([0, 1, 2], drops, width=0.50, color=[GRAY, SLATE, RED],
            edgecolor="none")
    ax2.set_ylim(0, 88)
    ax2.set_xlim(-0.62, 2.62)
    ax2.set_xticks([0, 1, 2])
    ax2.set_xticklabels(months, fontsize=11)
    ax2.set_yticks([0, 20, 40, 60, 80])
    ax2.set_yticklabels(["0", "20%", "40%", "60%", "80%"])
    ax2.grid(axis="y", color=LIGHT, linewidth=0.8, alpha=0.55)
    for x, v in zip([0, 1, 2], drops):
        ax2.text(x, v + 2.4, f"−{v}%", fontsize=13, color=DARK,
                 ha="center", va="bottom", weight="bold")
    ax2.set_title("同比降幅", fontsize=12.5, color=DARK, weight="bold",
                  loc="left", pad=14)
    ax2.text(0.02, 0.93, "4 月起连续第 7 个月同比下滑",
             transform=ax2.transAxes, fontsize=10, color=GRAY, va="center")

    punchline(fig, "不是慢慢丢份额，是主力车型一年少卖三分之二。")
    footer(fig, "据日产（中国）投资有限公司公布的 2026 年 4、9、10 月中国区销量（含乘用车与轻型商用车）。")
    fig.savefig(OUT + "图1_日产销量.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.190, 0.210, 0.760, 0.545])

    fig.text(0.045, 0.955, "日系三强：2026 上半年在华销量全线下滑", fontsize=18.5,
             color=DARK, weight="bold", ha="left", va="top")
    fig.text(0.045, 0.882, "单位：万辆。括号内为同比变化",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    rows = [
        ("丰田", 69.47, "−17.1%", NAVY),
        ("日产", 23.70, "−15.0%", RED),
        ("本田", 20.58, "−34.7%", SLATE),
    ]

    ys = [2, 1, 0]
    for y, (name, val, drop, color) in zip(ys, rows):
        ax.barh([y], [val], height=0.46, color=color, edgecolor="none")
        ax.text(val + 1.4, y, f"{val:.2f} 万辆　{drop}", fontsize=12.5,
                color=DARK, va="center", ha="left", weight="bold")

    ax.set_yticks(ys)
    ax.set_yticklabels([r[0] for r in rows], fontsize=13)
    ax.set_xlim(0, 95)
    ax.set_ylim(-0.62, 2.62)
    ax.set_xticks([0, 20, 40, 60, 80])
    ax.tick_params(axis="x", colors=DARK, labelsize=10.5, length=0, pad=8)
    ax.tick_params(axis="y", colors=DARK, length=0)
    ax.set_axisbelow(True)
    ax.grid(axis="x", color=LIGHT, linewidth=0.8, alpha=0.55)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(LIGHT)

    ax.text(0, -0.50, "三家合计少卖近 30 万辆；本田降幅最大，丰田体量最大但同样两位数下滑",
            fontsize=10, color=GRAY, va="center")

    punchline(fig, "没有一家有资格谈从容——差别只在跌得快慢。")
    footer(fig, "据日本共同社、界面新闻、IT之家（2026 年 7 月公布数据）。")
    fig.savefig(OUT + "图2_三强下滑.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.150, 0.930, 0.690])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "两种再校准：放什么，守什么", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.882, "同样在中国加减法，两家的账本不一样",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    ax.text(0.290, 0.790, "日产：交开发权，赌出口", fontsize=12, color=NAVY,
            weight="bold", ha="center")
    ax.text(0.720, 0.790, "丰田：开采购，守混动", fontsize=12, color=RED,
            weight="bold", ha="center")
    ax.plot([0.010, 0.990], [0.752, 0.752], color=LIGHT, linewidth=1.2)

    rows = [
        ("开放的部分", "乘用车开发主导权、LCV 研发中心", "电动车型的零部件采购"),
        ("守住的部分", "品牌、渠道、定价权", "混动供应链与利润池"),
        ("赌的方向", "用中国产能与成本出口全球", "用混动现金流换电动追赶"),
        ("已发生动作", "NV200 PHEV 中国首发、30+ 国出口", "雷克萨斯上海 2027 投产、RCE 扩至 7 人"),
        ("验证指标", "NX7 订单转化、出口国翻倍", "上海项目量产时的供应商名单"),
    ]

    for i, (label, left, right) in enumerate(rows):
        y = 0.665 - i * 0.125
        if i % 2 == 0:
            ax.add_patch(Rectangle((0.010, y - 0.052), 0.980, 0.104,
                                   facecolor=PALE, edgecolor="none"))
        ax.text(0.022, y, label, fontsize=10.6, color=GRAY, va="center")
        ax.text(0.290, y, left, fontsize=10.8, color=DARK, va="center", ha="center")
        ax.text(0.480, y, "｜", fontsize=12, color=LIGHT, va="center", ha="center")
        ax.text(0.720, y, right, fontsize=10.8, color=DARK, va="center", ha="center")

    ax.text(0.010, 0.045, "同样的动作，一个把研发权交出去，一个把采购单打开来。",
            fontsize=10.8, color=DARK, ha="left", va="center")

    footer(fig, "据 NISSAN DAY 2026-11-13 公布内容、Caixin Global、《日经亚洲》、盖世汽车、凤凰网整理。")
    fig.savefig(OUT + "图3_两种再校准.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")