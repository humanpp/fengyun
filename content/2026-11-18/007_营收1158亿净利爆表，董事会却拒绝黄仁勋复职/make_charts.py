# -*- coding: utf-8 -*-
"""
《营收 1158 亿、净利爆表，董事会却拒绝黄仁勋复职：英伟达的「后创始人」难题》配套图表
事实口径（均已交叉核对）：
  · 2026-11-17 英伟达发布 2027 财年第三季度（截至 10 月 25 日）财报：
    营收 1158 亿美元（115.84B），同比 +103%，环比 +20%；市场预期 1091 亿美元（超约 6.2%）；
    数据中心 1076 亿美元，同比 +110%，环比 +21%，占总营收约 93%；
    调整后 EPS 2.68 美元，市场预期 2.48 美元；GAAP 毛利率 74.8%，非 GAAP 74.9%；
    第四财季营收指引约 1300 亿美元（约 +90%），高于共识 1251 亿美元。盘后涨超 3%。
    来源：英伟达官方新闻稿、CNBC 2026-11-17。
  · 2026-11-12 英伟达公告：黄仁勋辞去总裁、CEO 及董事会成员职务，即刻生效；
    CFO 科莱特·克雷斯（Colette Kress）任临时 CEO 并保留 CFO；董事会启动全球遴选，
    同时考虑内部与外部候选人；董事哈维·琼斯（Harvey C. Jones，73 岁，在董事会约 30 年）
    出任公司首任董事长。据 CNBC，董事会于前一夜作出让其去职的决定。
  · 2026-11-08 董事会曾公开表达对黄仁勋及管理团队的信任；11-10 聘请外部律所
    （Wachtell Lipton）就相关争议启动独立调查。来源：腾讯新闻 2026-11-12、CNBC。
  · 2026-11-13 开盘股价一度跌 13%–14%，市值蒸发约 5000 亿美元。来源：环球时报、CoinDesk。
  · 2026-11-16 网上联署要求黄仁勋回归者超 16 万人；马斯克等公开呼吁。来源：财新。
  · 2026-11-17 上午（美东）黄仁勋发布辞职后首份声明：若董事会认为回归符合股东、员工、
    公司及美国的最佳利益，愿重返 CEO；同时承认个人生活犯下严重错误、未达公司标准、
    给董事会造成问题，承诺配合独立调查。同日财报电话会上，董事长哈维·琼斯重申
    不打算让其复职、将考虑内部和外部候选人、不会仓促决定。
    美国财长贝森特及两党资深议员公开反对其复职；特朗普表示不介意。来源：财新 2026-11-18、
    中国日报、CNBC、AP。
  · 董事会另已成立「国家安全与出口管制监督委员会」。来源：财新 2026-11-17。
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


# ------------------------------------------------------------------ 图 1
def fig1():
    fig = base("这份财报没有一个数字难看",
               "2027 财年第三季度：五项核心指标，四项超预期，一项持平于高位")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    rows = [
        ("营收", "1158 亿美元", "同比 +103%｜环比 +20%",
         "预期 1091 亿，超出约 6.2%"),
        ("数据中心", "1076 亿美元", "同比 +110%｜环比 +21%",
         "占总营收约 93%"),
        ("调整后 EPS", "2.68 美元", "市场预期 2.48 美元",
         "超出约 8.1%"),
        ("毛利率", "74.9%", "非 GAAP；GAAP 为 74.8%",
         "卖硬件的公司，近乎反常的水平"),
        ("Q4 营收指引", "约 1300 亿美元", "共识 1251 亿美元",
         "隐含同比约 +90%"),
    ]

    yy = 0.905
    for name, big, mid, note in rows:
        ax.plot([0.045, 0.955], [yy + 0.045, yy + 0.045], color=LIGHT,
                linewidth=0.9)
        ax.text(0.045, yy - 0.030, name, fontsize=10.6, color=SLATE,
                ha="left", va="center")
        ax.text(0.215, yy - 0.030, big, fontsize=15.2, color=NAVY,
                weight="bold", ha="left", va="center")
        ax.text(0.520, yy - 0.014, mid, fontsize=9.6, color=DARK,
                ha="left", va="center")
        ax.text(0.520, yy - 0.052, note, fontsize=9.0, color=GRAY,
                ha="left", va="center")
        yy -= 0.148

    ax.add_patch(FancyBboxPatch((0.045, 0.100), 0.910, 0.076,
                                boxstyle="round,pad=0.008", facecolor=SAND,
                                edgecolor="#d9cdb6", linewidth=1.0, zorder=2))
    ax.text(0.500, 0.138,
            "这是没有黄仁勋坐镇的第一份季报，也是 CFO 兼临时 CEO 交出的第一份季报",
            fontsize=9.8, color="#7a6746", ha="center", va="center", zorder=3)

    punchline(fig, "业绩这一栏，董事会找不到可以挑刺的地方。")
    footer(fig, "数据：英伟达 2027 财年第三季度财报（2026-11-17）及 CNBC／LSEG 一致预期｜制图：本文")
    fig.savefig(OUT + "图1_这份财报没有一个数字难看.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("九天：从「有信心」到「不考虑」",
               "2026 年 11 月 8 日至 17 日，英伟达发生了什么")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    events = [
        ("11/08", "董事会公开表达信任", "称对黄仁勋及其管理团队有信心", NAVY),
        ("11/10", "外部律所介入", "就近期争议启动独立调查", NAVY),
        ("11/12", "三项职务一并辞去，即刻生效",
         "总裁、CEO、董事；CFO 克雷斯任临时 CEO；哈维·琼斯出任首任董事长", RED),
        ("11/13", "开盘一度跌 13%–14%", "市值蒸发约 5000 亿美元", RED),
        ("11/16", "联署要求回归者超 16 万", "马斯克等公开呼吁其复职", NAVY),
        ("11/17", "同一天，两个方向相反的动作",
         "上午黄仁勋发声明愿回归；晚间电话会，董事会重申不考虑让他复职", RED),
    ]

    ax.plot([0.132, 0.132], [0.130, 0.945], color=LIGHT, linewidth=1.4)

    ys = [0.905, 0.760, 0.615, 0.470, 0.325, 0.180]
    for (date, head, body, color), yy in zip(events, ys):
        ax.plot([0.132], [yy], marker="o", markersize=7, color=color,
                zorder=4, clip_on=False)
        ax.text(0.112, yy, date, fontsize=9.4, color=color, weight="bold",
                ha="right", va="center")
        ax.text(0.168, yy + 0.030, head, fontsize=11.2, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(0.168, yy - 0.040, body, fontsize=8.9, color=SLATE,
                ha="left", va="center")

    ax.add_patch(FancyBboxPatch((0.560, 0.830), 0.395, 0.098,
                                boxstyle="round,pad=0.010", facecolor=SAND,
                                edgecolor="#d9cdb6", linewidth=1.0, zorder=2))
    ax.text(0.578, 0.893, "哈维·琼斯：73 岁，在董事会约 30 年，", fontsize=8.8,
            color="#7a6746", ha="left", va="center", zorder=3)
    ax.text(0.578, 0.855, "11 月 12 日成为公司首任董事长。", fontsize=8.8,
            color="#7a6746", ha="left", va="center", zorder=3)

    punchline(fig, "九天前说「有信心」，九天后说「不考虑」。中间是一份独立调查。")
    footer(fig, "时间线据英伟达公告、CNBC（2026-11-12／17）、财新（2026-11-18）、环球时报、CoinDesk｜制图：本文")
    fig.savefig(OUT + "图2_九天从信任到关门.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("两套不通兑的账",
               "业绩可以打满分，治理没有分数线——而且两者不能互换")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # 左栏
    ax.add_patch(Rectangle((0.045, 0.500), 0.440, 0.400, facecolor="white",
                           edgecolor=LIGHT, linewidth=1.1, zorder=2))
    ax.text(0.068, 0.862, "财报能衡量的", fontsize=11.2, color=NAVY,
            weight="bold", ha="left", va="center", zorder=3)
    left = [
        ("+103%", "营收同比增速"),
        ("74.9%", "毛利率"),
        ("1300 亿", "下季度营收指引"),
        ("93%", "数据中心占总营收比重"),
    ]
    yy = 0.795
    for big, name in left:
        ax.text(0.068, yy, big, fontsize=13.4, color=NAVY, weight="bold",
                ha="left", va="center", zorder=3)
        ax.text(0.240, yy, name, fontsize=9.6, color=SLATE, ha="left",
                va="center", zorder=3)
        yy -= 0.076

    # 右栏
    ax.add_patch(Rectangle((0.515, 0.500), 0.440, 0.400, facecolor="white",
                           edgecolor=RED, linewidth=1.1, zorder=2))
    ax.text(0.538, 0.862, "财报衡量不了的", fontsize=11.2, color=RED,
            weight="bold", ha="left", va="center", zorder=3)
    right = [
        "独立调查仍在进行，结论未出",
        "新设国家安全与出口管制监督委员会",
        "财长与两党议员公开反对复职",
        "临时 CEO 授权到哪一天为止",
    ]
    yy = 0.795
    for item in right:
        ax.text(0.538, yy, "·  " + item, fontsize=9.2, color=SLATE,
                ha="left", va="center", zorder=3)
        yy -= 0.076

    # 中间分隔
    ax.plot([0.500, 0.500], [0.500, 0.900], color=LIGHT, linewidth=1.0,
            linestyle=(0, (4, 4)))

    ax.add_patch(FancyBboxPatch((0.045, 0.215), 0.910, 0.215,
                                boxstyle="round,pad=0.012", facecolor=SAND,
                                edgecolor="#d9cdb6", linewidth=1.0, zorder=2))
    ax.text(0.070, 0.372, "两边放同一张桌子上，就会出现这个局面：", fontsize=9.4,
            color="#7a6746", ha="left", va="center", zorder=3)
    ax.text(0.070, 0.310, "一份史上最好的季报，和一个「不考虑让创始人回来」的董事会决定，",
            fontsize=10.6, color="#7a6746", weight="bold", ha="left",
            va="center", zorder=3)
    ax.text(0.070, 0.252, "出现在同一个晚上。", fontsize=10.6, color="#7a6746",
            weight="bold", ha="left", va="center", zorder=3)

    punchline(fig, "财报能证明公司离得开他，但不能决定要不要他。")
    footer(fig, "推导为本刊判断；事实据英伟达公告、财报电话会、财新（2026-11-17／18）｜制图：本文")
    fig.savefig(OUT + "图3_两套不通兑的账.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)
