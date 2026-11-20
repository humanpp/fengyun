# -*- coding: utf-8 -*-
"""
《1125 元挂牌，790 元回收：同一克金，两个价》配套图表
事实口径（2026-11-19 / 11-20，均为媒体公开报道）：
  · 11 月 19 日：老庙黄金足金饰品 1125 元/克，较年内高点 1722 元/克
    跌 597 元，回撤接近 35%；老凤祥、周大福均报 1132 元/克；
    品牌金饰价格连续第 8 个交易日下跌；
  · 同日国际金价一度跌破 3700 美元/盎司（最低 3693.17），
    上海金 Au99.99 开盘 810.0 元/克、盘中最低 793.44 元/克；
  · 同日深圳水贝：挂牌 959 元/克（含税）、实际购买 847 元/克、
    回收 790 元/克（数分钟后报 789）；
  · 今年 1 月主流品牌足金饰品一度站上 1700 元/克（年内高点 1722）；
  · 11 月 2 日样本：Au99.99 约 833 元/克，品牌挂牌 1168 元/克，
    回收报价约 818 元/克；10 克品牌手镯 11680 元买入、8180 元回收；
  · 11 月 20 日早间：现货黄金跌破 3600 美元/盎司，金饰 9 连跌，
    老凤祥 1090 元/克、周大福 1088 元/克。
  · 文中“每克差 910 元 / 10 克差 9100 元”为两个公开报价直接相减的
    换算，工费另计，不是某位消费者的实际账单。
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
SAND = "#f7f3ea"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep


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


def canvas(fig):
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return ax


# ------------------------------------------------------------------ 图 1
def fig1():
    fig = base("1125 元，和 790 元",
               "2026 年 11 月 19 日 · 同一天，同一克金，两个价")
    ax = canvas(fig)

    ax.plot([0.075, 0.925], [0.320, 0.320], color=LIGHT, linewidth=1.0)

    # 左柱：挂牌
    ax.add_patch(Rectangle((0.130, 0.320), 0.150, 0.500, facecolor=NAVY,
                           edgecolor="none"))
    ax.text(0.205, 0.845, "1125", fontsize=34, color=NAVY, weight="bold",
            ha="center", va="bottom")
    ax.text(0.205, 0.272, "品牌挂牌价", fontsize=11.0, color=DARK,
            ha="center", va="top")
    ax.text(0.205, 0.205, "老庙足金饰品 · 元/克", fontsize=8.8, color=GRAY,
            ha="center", va="top")

    # 右柱：回收
    ax.add_patch(Rectangle((0.660, 0.320), 0.150, 0.351, facecolor=RED,
                           edgecolor="none"))
    ax.text(0.735, 0.696, "790", fontsize=34, color=RED, weight="bold",
            ha="center", va="bottom")
    ax.text(0.735, 0.272, "回收价", fontsize=11.0, color=DARK, ha="center",
            va="top")
    ax.text(0.735, 0.205, "深圳水贝 · 正规回收店铺", fontsize=8.8, color=GRAY,
            ha="center", va="top")

    # 原料金参照线
    ax.plot([0.300, 0.660], [0.683, 0.683], color=SLATE, linewidth=1.1,
            linestyle=(0, (5, 4)))
    ax.text(0.300, 0.660, "原料金 Au99.99 盘中最低 793.44", fontsize=9.0,
            color=SLATE, ha="left", va="top")

    # 落差箭头
    ax.annotate("", xy=(0.480, 0.828), xytext=(0.480, 0.683),
                arrowprops=dict(arrowstyle="<->", color=DARK, linewidth=1.1))
    ax.text(0.498, 0.795, "335 元 / 克", fontsize=15.0, color=DARK,
            weight="bold", ha="left", va="center")
    ax.text(0.498, 0.748, "不是手续费，是两套计价方式", fontsize=8.6,
            color=GRAY, ha="left", va="center")

    punchline(fig, "你看到的降价，和你能拿到的钱，从来不是同一个数。")
    footer(fig, "事实：价格据 2026-11-19 中新经纬、财联社梳理及 11-19《每日经济新闻》水贝实探｜制图：本文")
    fig.savefig(OUT + "图1_同一天两个价.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("从 1700 到 790：一笔买在金价高点的账",
               "按两个公开报价直接相减：年初品牌挂牌高点 1700 元/克，11 月 19 日回收 790 元/克")
    ax = canvas(fig)

    ax.plot([0.060, 0.940], [0.300, 0.300], color=LIGHT, linewidth=1.0)

    ax.add_patch(Rectangle((0.095, 0.300), 0.135, 0.520, facecolor=NAVY,
                           edgecolor="none"))
    ax.text(0.162, 0.832, "1700", fontsize=30, color=NAVY, weight="bold",
            ha="center", va="bottom")
    ax.text(0.162, 0.252, "1 月买入", fontsize=10.6, color=DARK, ha="center",
            va="top")
    ax.text(0.162, 0.192, "品牌足金挂牌价高点", fontsize=8.4, color=GRAY,
            ha="center", va="top")

    ax.add_patch(Rectangle((0.330, 0.300), 0.135, 0.242, facecolor=RED,
                           edgecolor="none"))
    ax.text(0.397, 0.554, "790", fontsize=30, color=RED, weight="bold",
            ha="center", va="bottom")
    ax.text(0.397, 0.252, "11 月 19 日卖出", fontsize=10.6, color=DARK,
            ha="center", va="top")
    ax.text(0.397, 0.192, "深圳水贝回收价", fontsize=8.4, color=GRAY,
            ha="center", va="top")

    ax.annotate("", xy=(0.495, 0.820), xytext=(0.495, 0.542),
                arrowprops=dict(arrowstyle="<->", color=DARK, linewidth=1.1))
    ax.text(0.512, 0.700, "−910 元 / 克", fontsize=15.0, color=RED,
            weight="bold", ha="left", va="center")
    ax.text(0.512, 0.655, "约 53%", fontsize=11.0, color=GRAY, ha="left",
            va="center")

    # 换算框
    ax.add_patch(FancyBboxPatch((0.660, 0.395), 0.280, 0.400,
                                boxstyle="round,pad=0.012", facecolor=SAND,
                                edgecolor="#d9cdb6", linewidth=1.0))
    ax.text(0.690, 0.720, "一只 10 克的镯子", fontsize=9.4, color="#8a7a5e",
            ha="left", va="center")
    ax.text(0.690, 0.640, "17 000 元 买入", fontsize=12.4, color=DARK,
            weight="bold", ha="left", va="center")
    ax.text(0.690, 0.545, "7 900 元 回收", fontsize=12.4, color=RED,
            weight="bold", ha="left", va="center")
    ax.plot([0.690, 0.910], [0.495, 0.495], color="#d9cdb6", linewidth=0.9)
    ax.text(0.690, 0.435, "差 9 100 元", fontsize=14.0, color="#7a6746",
            weight="bold", ha="left", va="center")

    ax.text(0.060, 0.135, "注：这是两个公开报价的相减，工费另计，也不是某位消费者的实际账单；"
                          "红包、以旧换新、银行渠道的回收价各不相同。",
            fontsize=8.6, color=GRAY, ha="left", va="center")

    punchline(fig, "买在高点的人，亏的不是“金价跌了”，是买价和卖价本来就是两套数。")
    footer(fig, "事实：1700 元/克为 2026 年 1 月品牌足金挂牌高点（年内高点 1722）；790 元/克据 11-19《每日经济新闻》水贝实探｜换算为本文计算｜制图：本文")
    fig.savefig(OUT + "图2_从1700到790.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("一克金，在柜台上被拆成四块",
               "11 月 19 日：挂牌 1125 元/克；其中跟着大盘走的金料约 793 元，其余 332 元买的是别的东西")
    ax = canvas(fig)

    # 总量条
    y0, h = 0.615, 0.145
    ax.add_patch(Rectangle((0.060, y0), 0.290, h, facecolor=NAVY,
                           edgecolor="none"))
    ax.add_patch(Rectangle((0.350, y0), 0.350, h, facecolor="#c9a27a",
                           edgecolor="none"))
    ax.text(0.205, y0 + h / 2, "金料 793", fontsize=13.0, color="white",
            weight="bold", ha="center", va="center")
    ax.text(0.525, y0 + h / 2, "加工与渠道 332", fontsize=12.0, color="white",
            weight="bold", ha="center", va="center")
    ax.text(0.060, y0 + h + 0.030, "挂牌价 1125 元 / 克", fontsize=10.0,
            color=DARK, ha="left", va="bottom")

    # 左下：回收端只取金料
    ax.annotate("", xy=(0.205, 0.545), xytext=(0.205, y0 - 0.008),
                arrowprops=dict(arrowstyle="-|>", color=RED, linewidth=1.3))
    ax.text(0.060, 0.495, "回收 790 元 / 克", fontsize=16.0, color=RED,
            weight="bold", ha="left", va="center")
    ax.text(0.060, 0.418, "只认金料这一块，还要再减提纯、", fontsize=9.0,
            color=GRAY, ha="left", va="center")
    ax.text(0.060, 0.373, "检测和资金占用的十几元。", fontsize=9.0,
            color=GRAY, ha="left", va="center")

    # 右下：另外三块买的是什么
    items = [
        ("工费", "古法金、5G 金等复杂工艺，每克可加 60—120 元甚至更高"),
        ("品牌溢价", "回收那一刻，logo 不参与计价"),
        ("门店成本", "租金、导购、售后：金价跌了，这些开销一分不少"),
    ]
    yy = 0.560
    for head, body in items:
        ax.add_patch(Rectangle((0.398, yy - 0.030), 0.005, 0.052,
                               facecolor="#c9a27a", edgecolor="none"))
        ax.text(0.418, yy - 0.002, head, fontsize=10.2, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(0.512, yy - 0.002, body, fontsize=8.9, color=SLATE, ha="left",
                va="center")
        yy -= 0.098

    # 11-02 对照
    ax.add_patch(FancyBboxPatch((0.060, 0.150), 0.880, 0.115,
                                boxstyle="round,pad=0.010", facecolor=SAND,
                                edgecolor="#d9cdb6", linewidth=0.9))
    ax.text(0.085, 0.208, "11 月 2 日的同一本账：", fontsize=8.8, color="#8a7a5e",
            ha="left", va="center")
    ax.text(0.300, 0.208, "大盘 833　＋　加工与渠道 335　＝　挂牌 1168　；　回收 818",
            fontsize=11.0, color="#7a6746", weight="bold", ha="left",
            va="center")

    punchline(fig, "买的时候四样都付了，卖的时候只算一样。")
    footer(fig, "事实：1125/793.44/790 据 2026-11-19 报道与实探；工费与 833/1168/818 样本据 11-02 报道｜制图：本文")
    fig.savefig(OUT + "图3_一克金的四块.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)
