# -*- coding: utf-8 -*-
"""
《一线二手房连涨 8 个月，70 城里还有 58 个在跌》配套图表
事实口径（2026-11-19，直接核对国家统计局解读稿与财新、每经原文后）：
  · 2026 年 11 月 16 日 09:30，国家统计局城市司高级统计师杨彩芳解读 10 月
    70 城房价：一线二手住宅环比上涨 0.2%（涨幅与上月相同），上海、广州、
    深圳分别上涨 0.5%、0.2%、0.1%，北京持平；二线、三线二手环比均下降
    0.3%（二线降幅扩大 0.1 个百分点，三线持平）。
  · 同比：一线二手下降 0.4%（降幅收窄 1.1 个百分点），北京、广州、深圳分别
    下降 1.5%、1.8%、0.5%，上海上涨 2.2%；二线、三线二手同比分别下降
    4.1%、5.0%，降幅均收窄 0.4 个百分点。
  · 新房：一线新建商品住宅环比由上月上涨 0.1% 转为持平（上海 +0.2%、深圳
    +0.1%、广州持平、北京 -0.1%），同比 -0.1%（收窄 0.4 个百分点）。
  · 70 城中二手住宅环比上涨城市 7 个（比上月少 2 个）；财新补充：5 个持平、
    58 个下跌，上涨城市为上海、广州、深圳、沈阳、合肥、重庆、徐州，上海与
    徐州均涨 0.5% 居首；9 月上涨城市为 9 个。
  · "连续 8 个月"：自 2026 年 3 月以来一线二手环比连续上涨，10 月为第 8 个月
    （每日经济新闻 11-16）。
  · 上海首次同比转正发生在 2026 年 9 月（+0.8%），为 2024 年 1 月以来 70 城
    二手住宅同比"连续 32 个月无一城上涨"之后的首个转正城市；10 月 +2.2%，
    仍是 70 城中唯一同比上涨的城市，沈阳为二线首个同比止跌城市
    （财新 10-21、羊城派 10-19、每日经济新闻 11-16）。
  · 成交量：上海 10 月二手网签 24653 套（含商业、车位），环比 +10.9%、
    同比 +33%，创近 6 年同期新高；3 月以来连续 8 个月在 2.3 万套以上
    （网上房地产数据，经每日经济新闻 11-16）。
  · 面上仍在跌：中指研究院百城口径 10 月二手住宅均价 12376 元/平方米，
    环比 -0.61%（跌幅较 9 月扩大 0.01 个百分点），同比 -6.72%，仅 1 城上涨
    （央广网 11-12）。
  · 量在价先：1—10 月全国二手房交易网签面积 67971 万平方米，同比 +11.4%
    （住建部数据，经财新 11-16、每经 11-16）。
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
GRAY = "#8a8f98"
SLATE = "#5f6673"
LIGHT = "#d8dbe0"
DARK = "#2b2f36"
PALE = "#eef0f3"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep


def base(title, sub):
    fig = plt.figure(figsize=(12, 6.8))
    fig.patch.set_facecolor("white")
    fig.text(0.045, 0.950, title, fontsize=20, color=DARK, weight="bold",
             ha="left", va="top")
    fig.text(0.045, 0.876, sub, fontsize=10.4, color=GRAY, ha="left", va="top")
    return fig


def footer(fig, text):
    fig.text(0.045, 0.014, text, fontsize=8.2, color=GRAY, ha="left", va="center")


def punchline(fig, text, y=0.078):
    fig.text(0.045, y, text, fontsize=10.8, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.6", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


def canvas(fig):
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return ax


# ------------------------------------------------------------------ 图 1
def fig1():
    fig = base("一线微涨，二线三线还在跌",
               "2026 年 10 月｜70 个大中城市二手住宅价格，分城市层级")
    ax = canvas(fig)

    ax.text(0.380, 0.860, "环比（比上月）", fontsize=9.6, color=DARK,
            weight="bold", ha="center", va="center")
    ax.text(0.780, 0.860, "同比（比去年同月）", fontsize=9.6, color=DARK,
            weight="bold", ha="center", va="center")

    x0_mom, x0_yoy = 0.380, 0.780
    s_mom, s_yoy = 0.150, 0.022

    rows = [
        ("一线城市", 0.2, -0.4),
        ("二线城市", -0.3, -4.1),
        ("三线城市", -0.3, -5.0),
    ]

    for i, (name, mom, yoy) in enumerate(rows):
        y = 0.700 - i * 0.160
        color = NAVY if mom > 0 else RED
        c_yoy = NAVY if yoy > 0 else RED
        ax.text(0.028, y, name, fontsize=10.2, color=DARK, weight="bold",
                ha="left", va="center")

        ax.plot([x0_mom, x0_mom], [0.300, 0.790], color=LIGHT, linewidth=1.0)
        ax.plot([x0_yoy, x0_yoy], [0.300, 0.790], color=LIGHT, linewidth=1.0)

        w = mom * s_mom
        ax.add_patch(Rectangle((min(x0_mom, x0_mom + w), y - 0.030),
                               abs(w), 0.060, facecolor=color,
                               edgecolor="none"))
        ax.text(x0_mom + w + (0.012 if w >= 0 else -0.012), y,
                "%+.1f%%" % mom, fontsize=10.4, color=color, weight="bold",
                ha=("left" if w >= 0 else "right"), va="center")

        w = yoy * s_yoy
        ax.add_patch(Rectangle((min(x0_yoy, x0_yoy + w), y - 0.030),
                               abs(w), 0.060, facecolor=c_yoy,
                               edgecolor="none"))
        ax.text(x0_yoy + w - 0.012, y, "%.1f%%" % yoy, fontsize=10.4,
                color=c_yoy, weight="bold", ha="right", va="center")

    ax.text(0.028, 0.235,
            "同一份数据里的另一半：一线新建商品住宅环比由上涨 0.1% 转为持平，"
            "同比 -0.1%（降幅收窄 0.4 个百分点）。",
            fontsize=8.8, color=SLATE, ha="left", va="center")
    ax.text(0.028, 0.180,
            "二手房的连涨只属于四个一线城市；二线、三线环比仍在下跌，"
            "降幅分别扩大和持平。",
            fontsize=8.8, color=SLATE, ha="left", va="center")

    punchline(fig, "四个城市在涨，其余六十多个在看。")
    footer(fig, "事实：国家统计局城市司高级统计师杨彩芳解读 2026 年 10 月 70 城"
                "房价（2026-11-16 09:30）、财新 11-16、每日经济新闻 11-16｜制图：本文")
    fig.savefig(OUT + "图1_一线微涨二线三线还在跌.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("70 城二手房价：7 涨、5 平、58 跌",
               "2026 年 10 月｜环比上涨城市比 9 月又少 2 个")
    ax = canvas(fig)

    ax.text(0.028, 0.800, "二手住宅环比：70 个城市的分布", fontsize=10.4,
            color=DARK, weight="bold", ha="left", va="center")

    left, total_w = 0.030, 0.940
    y, h = 0.660, 0.110
    segs = [("上涨 7", 7, NAVY), ("持平 5", 5, GRAY), ("下跌 58", 58, RED)]
    x = left
    for label, n, color in segs:
        w = total_w * n / 70.0
        ax.add_patch(Rectangle((x, y), w, h, facecolor=color, edgecolor="white",
                               linewidth=1.6))
        ax.text(x + w / 2, y + h / 2, label, fontsize=9.6, color="white",
                weight="bold", ha="center", va="center")
        x += w

    ax.text(left, 0.590, "9 月上涨 9 个　→　10 月上涨 7 个", fontsize=9.4,
            color=SLATE, ha="left", va="center")

    ax.plot([left, left + total_w], [0.520, 0.520], color=LIGHT, linewidth=0.9)

    ax.text(0.028, 0.455, "涨的这 7 个城市", fontsize=10.0, color=DARK,
            weight="bold", ha="left", va="center")

    cities = [("上海", "0.5%"), ("徐州", "0.5%"), ("广州", "0.2%"),
              ("深圳", "0.1%"), ("沈阳", "上涨"), ("合肥", "上涨"),
              ("重庆", "上涨")]
    x = 0.030
    for name, pct in cities:
        ax.add_patch(FancyBboxPatch((x, 0.330), 0.122, 0.075,
                                    boxstyle="round,pad=0.004",
                                    facecolor="white", edgecolor=LIGHT,
                                    linewidth=1.0))
        ax.text(x + 0.061, 0.383, name, fontsize=9.0, color=DARK,
                weight="bold", ha="center", va="center")
        ax.text(x + 0.061, 0.350, pct, fontsize=8.0,
                color=(NAVY if pct.startswith("0") else GRAY),
                ha="center", va="center")
        x += 0.134

    ax.text(0.028, 0.240,
            "上海与徐州均涨 0.5%，并列 70 城第一；徐州是三线城市。"
            "另有 5 城持平、58 城下跌。",
            fontsize=8.8, color=SLATE, ha="left", va="center")
    ax.text(0.028, 0.185,
            "作为对照：中指研究院百城口径 10 月二手住宅均价 12376 元/平方米，"
            "环比 -0.61%，同比 -6.72%。",
            fontsize=8.8, color=SLATE, ha="left", va="center")

    punchline(fig, "一个月里，能涨的城市又少了两个。")
    footer(fig, "事实：国家统计局 10 月 70 城数据（上涨 7 个、比上月少 2 个）；"
                "财新 11-16（5 平、58 跌与城市名单）；中指研究院数据经央广网 11-12｜制图：本文")
    fig.savefig(OUT + "图2_七涨五平五十八跌.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("上海这个“首个”，是 9 月的事",
               "上海二手住宅价格同比｜10 月的说法差了一个月")
    ax = canvas(fig)

    cards = [
        ("2026 年 9 月", "+0.8%", "首次同比转正", NAVY, 0.020),
        ("2026 年 10 月", "+2.2%", "仍是 70 城唯一", RED, 0.510),
    ]
    for label, value, note, color, x in cards:
        ax.add_patch(FancyBboxPatch((x, 0.560), 0.470, 0.300,
                                    boxstyle="round,pad=0.006",
                                    facecolor="white", edgecolor=LIGHT,
                                    linewidth=1.1))
        ax.text(x + 0.032, 0.812, label, fontsize=9.6, color=GRAY,
                ha="left", va="center")
        ax.text(x + 0.032, 0.716, value, fontsize=27.0, color=color,
                weight="bold", ha="left", va="center")
        ax.text(x + 0.032, 0.616, note, fontsize=9.6, color=SLATE,
                ha="left", va="center")

    ax.add_patch(FancyBboxPatch((0.020, 0.300), 0.960, 0.150,
                                boxstyle="round,pad=0.006",
                                facecolor="white", edgecolor=LIGHT,
                                linewidth=1.0))
    ax.text(0.044, 0.392,
            "2024 年 1 月—2026 年 8 月：70 城二手住宅同比连续 32 个月无一城上涨。",
            fontsize=9.4, color=DARK, ha="left", va="center")
    ax.text(0.044, 0.338,
            "9 月上海以 +0.8% 打破这个记录，10 月 +2.2%；10 月同比上涨的城市仍只有它一个。",
            fontsize=9.4, color=SLATE, ha="left", va="center")

    ax.text(0.028, 0.210, "量先动：上海 10 月二手网签 24653 套（含商业、车位），"
                          "同比 +33%，创近 6 年同期新高。",
            fontsize=8.8, color=SLATE, ha="left", va="center")
    ax.text(0.028, 0.155, "对照面：二三线二手同比仍降 4.1% 和 5.0%，"
                          "只是降幅都在收窄。",
            fontsize=8.8, color=GRAY, ha="left", va="center")

    punchline(fig, "“首个”发生在 9 月；10 月已经是第二个月。")
    footer(fig, "事实：国家统计局 10 月数据（上海二手同比 +2.2%）、财新 10-21"
                "（9 月上海二手同比三年来首次转涨）、羊城派 10-19（32 个月无一城上涨）、"
                "每日经济新闻 11-16（网签 24653 套、同比 +33%）｜制图：本文")
    fig.savefig(OUT + "图3_首个是9月的事.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)
