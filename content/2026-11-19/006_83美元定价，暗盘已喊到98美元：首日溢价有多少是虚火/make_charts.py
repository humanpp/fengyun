# -*- coding: utf-8 -*-
"""
《83 美元定价，暗盘已喊到 98 美元》配套图表
事实口径（2026-11-19，逐条核对公开报道后）：
  · 发行价 83 美元，招股区间 70—78 美元 → 高于上限约 6.4%（路透 11-18 引述，财闻、星岛等转述）；
  · 场外暗盘：Hyperliquid 永续合约 98.39 美元，较 83 美元溢价超 18%（TradingKey 11-19）；
    同一合约上线初期曾报 138 美元、一度跌破 94 美元（华盛通 11-11）；
  · 8.25 亿股（新发约 8.014 亿 + 老股东 2360 万）× 83 = 公开募资约 685 亿美元；
    叠加 260 亿美元私募配售 → 合计约 945 亿美元，超过 SpaceX 6 月 IPO 含超额配售的约 860 亿美元；
    绿鞋最多 1.2375 亿股，按 83 美元可再增约 103 亿美元（财闻 11-19）；
  · 完全摊薄估值约 1.5 万亿美元；5 月私募轮 9650 亿美元；
  · 散户配售：招股阶段约 10%—15%（21 世纪经济报道 11-11），最终上限 20%，
    传统 IPO 通常 5%—10%（TradingKey 11-19）；认购总额逼近 5000 亿美元（华盛 11-19）；
  · 截至 9 月 30 日九个月营收 332.4 亿美元、同比约 +1200%；净亏损 1040 亿美元，
    主要来自可转换票据及衍生负债公允价值变动；Q3 营收 169.6 亿美元、环比 +47%，
    Q3 经营亏损 5.67 亿美元（Q2 经营利润 9.74 亿美元）；
    截至 10 月底年化收入运行规模 810 亿美元（较 9 月底 +100 亿）（华盛 11-19、TradingKey）。
本文换算（非当事方口径）：前三季度营收年化 ≈ 443 亿美元 → 83 美元约 34 倍、
98.39 美元约 40 倍市销率；按 810 亿 run-rate → 18.5 倍、22.0 倍。
风格：克制传媒风，白底、低饱和配色、标题即结论。输出目录 = 脚本所在目录。
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False

NAVY = "#1f3a5f"
RED = "#b5544a"
LITE_RED = "#c98a83"
GRAY = "#8a8f98"
SLATE = "#5f6673"
LIGHT = "#d8dbe0"
DARK = "#2b2f36"
PALE = "#eef0f3"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep

PRICE = 83.00
DARKP = 98.39

UP_RANGE = (PRICE / 78.0 - 1) * 100        # 6.41
UP_DARK = (DARKP / PRICE - 1) * 100        # 18.54
GAP = DARKP - PRICE                        # 15.39

REV_Y = 332.4 / 9 * 12                     # 443.2
RUNRATE = 810.0
VAL = 15000.0
VAL_D = VAL * DARKP / PRICE                # 17782

PS_LOW, PS_HIGH = VAL / REV_Y, VAL_D / REV_Y        # 33.8 / 40.1
PR_LOW, PR_HIGH = VAL / RUNRATE, VAL_D / RUNRATE     # 18.5 / 22.0


def base(title, sub):
    fig = plt.figure(figsize=(12, 6.8))
    fig.patch.set_facecolor("white")
    fig.text(0.045, 0.950, title, fontsize=20, color=DARK, weight="bold",
             ha="left", va="top")
    fig.text(0.045, 0.878, sub, fontsize=10.8, color=GRAY, ha="left", va="top")
    return fig


def footer(fig, text):
    fig.text(0.045, 0.014, text, fontsize=8.2, color=GRAY, ha="left", va="center")


def punchline(fig, text, y=0.078):
    fig.text(0.045, y, text, fontsize=10.8, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.6", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


# ------------------------------------------------------------------ 图 1
def fig1():
    fig = base("83 是定价，98.39 是喊价",
               "招股区间 70—78 美元｜11 月 18 日定价 83 美元｜场外永续合约现报 98.39 美元")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    x0 = 0.215
    scale = 0.50 / 110.0

    rows = [
        ("场外暗盘", DARKP, RED, 0.780, "永续合约", "美元｜较定价 +%.1f%%" % UP_DARK),
        ("发行定价", PRICE, NAVY, 0.600, "11 月 18 日",
         "美元｜较区间上限 +%.1f%%" % UP_RANGE),
        ("区间上限", 78.0, SLATE, 0.420, "招股文件", "美元"),
        ("区间下限", 70.0, LIGHT, 0.260, "招股文件", "美元"),
    ]

    for name, p, color, y, tag, note in rows:
        w = p * scale
        ax.add_patch(Rectangle((x0, y - 0.055), w, 0.110, facecolor=color,
                               edgecolor="none"))
        ax.text(0.030, y + 0.020, name, fontsize=11.0, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(0.030, y - 0.032, tag, fontsize=8.4, color=GRAY, ha="left",
                va="center")
        ax.text(x0 + w + 0.016, y + 0.020, "%.2f" % p, fontsize=17.0,
                color=SLATE if color is LIGHT else DARK, weight="bold",
                ha="left", va="center")
        ax.text(x0 + w + 0.016, y - 0.038, note, fontsize=8.4, color=GRAY,
                ha="left", va="center")

    ax.annotate("", xy=(x0 + DARKP * scale, 0.900),
                xytext=(x0 + PRICE * scale, 0.900),
                arrowprops=dict(arrowstyle="<->", color=RED, lw=1.2,
                                shrinkA=0, shrinkB=0))
    ax.text(x0 + (PRICE + DARKP) / 2 * scale, 0.935,
            "%.2f 美元" % GAP, fontsize=9.4, color=RED, ha="center",
            va="bottom", weight="bold")
    ax.text(x0 + (PRICE + DARKP) / 2 * scale, 0.880,
            "不是股票成交价，是场外合约报价", fontsize=8.4, color=GRAY,
            ha="center", va="top")

    ax.plot([0.030, 0.970], [0.140, 0.140], color=LIGHT, linewidth=0.9)
    ax.text(0.030, 0.098,
            "公开募资约 685 亿美元 + 260 亿美元私募配售 ≈ 945 亿美元｜完全摊薄估值约 1.5 万亿美元",
            fontsize=9.4, color=SLATE, ha="left", va="center")

    punchline(fig, "定价已经高过区间上限，场外还想在它上面再加 18%。")
    footer(fig, "事实：发行价、区间据路透 11-18 引述；98.39 为 Hyperliquid 永续合约报价（TradingKey 11-19）｜"
                "溢价为本文按上述价格计算｜制图：本文")
    fig.savefig(OUT + "图1_83和98之间的缺口.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("配售给散户的比例：从一成变成两成",
               "传统 IPO 通常 5%—10%｜本次招股阶段约 10%—15%｜最终上限提到 20%")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    x0 = 0.335
    scale = 0.520 / 24.0

    bars = [
        ("传统 IPO · 下限", 5.0, LIGHT, 0.760, "行业惯例"),
        ("传统 IPO · 上限", 10.0, SLATE, 0.600, "行业惯例"),
        ("本次 · 招股阶段", 15.0, LITE_RED, 0.440, "招股文件"),
        ("本次 · 最终上限", 20.0, RED, 0.280, "定价时"),
    ]

    for name, v, color, y, tag in bars:
        w = v * scale
        ax.add_patch(Rectangle((x0, y - 0.050), w, 0.100, facecolor=color,
                               edgecolor="none"))
        ax.text(0.030, y + 0.022, name, fontsize=10.6, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(0.030, y - 0.028, tag, fontsize=8.4, color=GRAY, ha="left",
                va="center")
        ax.text(x0 + w + 0.018, y, "%d%%" % int(v), fontsize=17.0,
                color=RED if color in (RED, LITE_RED) else DARK, weight="bold",
                ha="left", va="center")

    for t in (0, 5, 10, 15, 20):
        xx = x0 + t * scale
        ax.plot([xx, xx], [0.150, 0.830], color="#e8eaee", lw=0.8, zorder=0)
        ax.text(xx, 0.108, "%d%%" % t, fontsize=8.2, color=GRAY,
                ha="center", va="center")

    ax.text(0.030, 0.108, "占发行规模", fontsize=8.6, color=GRAY, ha="left",
            va="center")

    punchline(fig, "20% 是配售上限，不等于首日能自由买卖的股份占比——但拿到货的人多了，"
                   "开盘那半小时就更薄。")
    footer(fig, "事实：传统区间据 TradingKey 11-19；招股阶段比例据 21 世纪经济报道 11-11；"
                "最终上限据财闻、华盛 11-19｜机构获配部分通常附带锁定期｜制图：本文")
    fig.savefig(OUT + "图2_首日筹码.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("同一家公司，两个价格，两种年化口径",
               "83 美元与 98.39 美元对应的完全摊薄估值，以及按两种营收口径折算的市销率")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    cards = [
        (0.030, "发行定价 · 美元 / 股", "83.00", NAVY,
         "约 1.5 万亿美元", "约 18.5 倍", "约 34 倍"),
        (0.530, "场外暗盘 · 美元 / 股", "98.39", RED,
         "约 1.78 万亿美元", "约 22.0 倍", "约 40 倍"),
    ]

    for x, tag, px, color, val, ps_new, ps_old in cards:
        ax.add_patch(FancyBboxPatch((x, 0.150), 0.440, 0.720,
                                    boxstyle="round,pad=0.010",
                                    facecolor="white", edgecolor=LIGHT,
                                    linewidth=1.0))
        ax.add_patch(Rectangle((x, 0.864), 0.440, 0.006, facecolor=color,
                               edgecolor="none"))
        ax.text(x + 0.034, 0.802, tag, fontsize=9.8, color=GRAY, ha="left",
                va="center")
        ax.text(x + 0.034, 0.718, px, fontsize=32.0, color=DARK, weight="bold",
                ha="left", va="center")

        ax.plot([x + 0.034, x + 0.404], [0.658, 0.658], color=LIGHT, lw=0.9)
        ax.text(x + 0.034, 0.600, "完全摊薄估值", fontsize=8.8, color=GRAY,
                ha="left", va="center")
        ax.text(x + 0.034, 0.540, val, fontsize=14.0, color=DARK, weight="bold",
                ha="left", va="center")

        ax.plot([x + 0.034, x + 0.404], [0.482, 0.482], color=LIGHT, lw=0.9)
        ax.text(x + 0.034, 0.424, "市销率 · 按 10 月底 run-rate 810 亿",
                fontsize=8.8, color=GRAY, ha="left", va="center")
        ax.text(x + 0.034, 0.362, ps_new, fontsize=19.0, color=color,
                weight="bold", ha="left", va="center")

        ax.text(x + 0.034, 0.288, "市销率 · 按九个月营收年化 443 亿",
                fontsize=8.8, color=GRAY, ha="left", va="center")
        ax.text(x + 0.034, 0.228, ps_old, fontsize=19.0, color=SLATE,
                weight="bold", ha="left", va="center")

    ax.text(0.030, 0.090,
            "净亏损 1040 亿美元，公司称主要来自可转换票据及衍生负债的公允价值变动；"
            "上述倍数与年化营收为本文换算，810 亿为招股文件披露口径。",
            fontsize=8.6, color=SLATE, ha="left", va="center")

    punchline(fig, "同一笔估值，换一种年化口径，市销率就从 18.5 倍变成 34 倍。")
    footer(fig, "事实：发行价、估值、营收与亏损据路透 11-18 引述及华盛、TradingKey 11-19 报道｜"
                "营收年化与市销率为本文换算｜制图：本文")
    fig.savefig(OUT + "图3_34倍和40倍.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)
