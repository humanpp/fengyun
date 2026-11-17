# -*- coding: utf-8 -*-
"""
《新车不好卖，车圈开始经营 3.7 亿辆存量车》配套图表
事实来源：极狐贝塔 T1 换电版车身价 5.20/6.00 万元、电池月租 399/599 元、
充电版 550 PRO 7.68 万元；巧克力换电站 2026-09 超 2,500 座、2027 年目标
6,000 座覆盖 297 城；柳州检测团购价 68/88/108 元对比常规 300 余元；
2026-11-13 贵阳 70 余家检测机构被四部门约谈
风格：克制传媒风，白底、低饱和配色、标题即结论
输出目录 = 脚本所在目录
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.lines import Line2D

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


def bare(ax, axis="y"):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(LIGHT)
    ax.tick_params(colors=DARK, labelsize=10.5, length=0)
    ax.set_axisbelow(True)
    ax.grid(axis=axis, color=LIGHT, linewidth=0.8, alpha=0.55)


# ---------------------------------------------------------------- 图 1
def fig1():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.085, 0.205, 0.885, 0.560])

    fig.text(0.045, 0.955, "换电的五年账：399 档打平，599 档更贵", fontsize=18.5,
             color=DARK, weight="bold", ha="left", va="top")
    fig.text(0.045, 0.882, "贝塔 T1 换电版与同款买断版，五年累计支出（元）",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    bare(ax)
    base = 52000
    cfg = [
        ("换电版\n399 元/月", base, 399 * 60, "租金 2.39 万", NAVY, "比买断低 860 元"),
        ("换电版\n599 元/月", base, 599 * 60, "租金 3.59 万", SLATE, "比买断高 11,140 元"),
        ("充电版\n买断电池", 76800, 0, "整车含电池", GRAY, "基准"),
    ]

    ax.set_ylim(0, 104000)
    ax.set_xlim(-0.62, 2.62)
    ax.set_xticks([0, 1, 2])
    ax.set_xticklabels([c[0] for c in cfg], fontsize=10.8, linespacing=1.6)
    ax.set_yticks([0, 20000, 40000, 60000, 80000])
    ax.set_yticklabels(["0", "2 万", "4 万", "6 万", "8 万"])

    for x, (_, b, rent, rlab, color, sub) in enumerate(cfg):
        ax.bar([x], [b], width=0.50, color=color, edgecolor="none")
        if rent:
            ax.bar([x], [rent], bottom=b, width=0.50, color=color,
                   alpha=0.45, edgecolor="none")
            ax.text(x, b + rent / 2, rlab, fontsize=10.5, color=DARK,
                    ha="center", va="center")
            ax.text(x, b / 2, "车身 5.20 万", fontsize=10.5, color="white",
                    ha="center", va="center")
        else:
            ax.text(x, b / 2, "整车 7.68 万", fontsize=10.5, color="white",
                    ha="center", va="center")

        total = b + rent
        ax.text(x, total + 3600, f"{total:,}", fontsize=13.5, color=DARK,
                ha="center", va="bottom", weight="bold")
        ax.text(x, total + 600, sub, fontsize=9.6, color=GRAY,
                ha="center", va="bottom")

    handles = [
        Line2D([0], [0], color=NAVY, linewidth=9, label="车身价（一次性）"),
        Line2D([0], [0], color=NAVY, linewidth=9, alpha=0.45, label="五年电池租金"),
    ]
    ax.legend(handles=handles, loc="upper left", frameon=False, fontsize=10.4,
              handlelength=1.6, bbox_to_anchor=(0.010, 1.010))

    punchline(fig, "5.2 万的门槛，是拿月租换来的——五年总账并不省钱。")
    footer(fig, "据极狐官方公布的贝塔 T1 换电版与充电版价格、电池月租方案计算；租金不含换电电费与服务费。")
    fig.savefig(OUT + "图1_换电的账.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.150, 0.235, 0.800, 0.510])

    fig.text(0.045, 0.955, "换电站：两年多要从 2500 座翻到 6000 座", fontsize=18.5,
             color=DARK, weight="bold", ha="left", va="top")
    fig.text(0.045, 0.882, "巧克力换电站累计建成数量（座）",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    bare(ax, axis="x")
    rows = [
        ("2026 年 9 月底\n已建成", 2500, GRAY, "2,500 座"),
        ("2027 年底\n目标", 6000, NAVY, "6,000 座"),
    ]
    ys = [1, 0]
    for y, (lab, val, color, txt) in zip(ys, rows):
        ax.barh([y], [val], height=0.42, color=color, edgecolor="none")
        ax.text(val + 120, y, txt, fontsize=14, color=color, weight="bold",
                va="center", ha="left")

    ax.set_yticks(ys)
    ax.set_yticklabels([r[0] for r in rows], fontsize=11, linespacing=1.6)
    ax.set_xlim(0, 7400)
    ax.set_ylim(-0.60, 1.60)
    ax.set_xticks([0, 2000, 4000, 6000])
    ax.tick_params(axis="x", pad=8)

    ax.annotate("", xy=(6000, 0.42), xytext=(2500, 0.86),
                arrowprops=dict(arrowstyle="-", color=RED, linewidth=1.4,
                                linestyle=(0, (4, 3)), connectionstyle="arc3,rad=-0.18"))
    ax.text(60, 1.44, "15 个月新增 3,500 座　≈ 每月 233 座",
            fontsize=12, color=RED, weight="bold", ha="left", va="center")
    ax.text(60, -0.46, "覆盖 297 座城市；截至 9 月底近 2 万块电池入仓",
            fontsize=9.8, color=GRAY, va="center")

    punchline(fig, "建站速度不是最难的一关，让不同品牌共用一个标准才是。")
    footer(fig, "据每日经济新闻（宁德时代市场体系联席总裁杨峻 2026-11-13 表态）及巧克力换电公开数据。")
    fig.savefig(OUT + "图2_换电网络.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.075, 0.215, 0.860, 0.545])

    fig.text(0.045, 0.955, "检测价格战：300 多元打到 68 元", fontsize=19,
             color=DARK, weight="bold", ha="left", va="top")
    fig.text(0.045, 0.882, "机动车检测单次价格（元）。常规价与团购价对比",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    bare(ax)
    labels = ["常规价", "团购一", "团购二", "团购三"]
    vals = [300, 108, 88, 68]
    cols = [GRAY, SLATE, SLATE, RED]

    ax.bar([0, 1, 2, 3], vals, width=0.46, color=cols, edgecolor="none")
    ax.set_ylim(0, 380)
    ax.set_xlim(-0.65, 3.65)
    ax.set_xticks([0, 1, 2, 3])
    ax.set_xticklabels(labels, fontsize=11)
    ax.set_yticks([0, 100, 200, 300])
    ax.set_yticklabels(["0", "100", "200", "300"])

    for x, v in zip([0, 1, 2, 3], vals):
        txt = "300+" if v == 300 else f"{v}"
        ax.text(x, v + 9, txt, fontsize=13.5, color=DARK, ha="center",
                va="bottom", weight="bold")

    ax.text(1.30, 250,
            "价格压到成本线以下，\n就只能靠放水检测和数据作弊补回来",
            fontsize=10.8, color=DARK, ha="left", va="center", linespacing=1.8,
            bbox=dict(boxstyle="round,pad=0.6", facecolor=PALE,
                      edgecolor=LIGHT, linewidth=0.9))

    punchline(fig, "11 月 13 日，贵阳 70 余家检测机构被四部门集中约谈。")
    footer(fig, "据广西新闻网（柳州检测站团购价 68/88/108 元对比常规 300 余元）、贵州省市场监管局 2026-11-13 约谈会。")
    fig.savefig(OUT + "图3_检测价格.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")