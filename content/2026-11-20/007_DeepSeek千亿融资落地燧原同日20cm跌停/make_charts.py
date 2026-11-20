# -*- coding: utf-8 -*-
"""
《DeepSeek 千亿融资落地，燧原同日 20cm 跌停：国产算力同一天冰火两重天》配套图表
事实口径（均经公开报道交叉核对）：
  · DeepSeek 工商主体杭州深度求索 2026-11-17 完成变更，注册资本 1644.7496 万元 → 1991.8707 万元，
    增幅约 21.1%，新增股东杭州程砚企业管理咨询合伙企业（有限合伙），持股约 17.265%；
  · 杭州程砚登记出资额 0.6 万元 → 约 34.39 亿元，合伙人增至 32 名（新增 31 家即本轮外部股东）；
  · 出资比例：上海珩岫（腾讯）9.5653%、宁德时代三只基金合计 9.5653%、中移投资控股 7.6522%、
    中信证券投资 7.6522%、天津砺思星深 7.1740%、青岛城鑫致达（国寿）4.7826%、
    杭州石溪兆易一号/博裕肖河/杭州源峰磐睿/拾象尚势/宁波智兴悦恒各 3.3479%、天津云程创投（IDG）3.3236%、
    中国电信/维沃/vivo/美的投资/福州荟珠（美团龙珠）/杭州君联嘉途/天津高榕长赢各 2.87%
    —— 第一财经、每日经济新闻 2026-11-19 据企查查/天眼查穿透；
  · 燧原科技（SH688801）2026-11-19 收 364.33 元、跌 20%，成交 19.62 亿元、换手 28.35%；
    11-13 收盘 570.68 元（盘中最高 613 元）→ 11-16 收 500.00（-12.39%）→ 11-17 收 483.40（-3.32%）
    → 11-18 收 455.41（-5.79%）→ 11-19 收 364.33（-20.00%），四日累计回撤 36.16%；
    总市值 1960 亿 → 1568 亿元，单日蒸发 392 亿元；无限售流通股 1790.0325 万股，占总股本 4.1595%
    —— 每日经济新闻 2026-11-19 引公司《股票交易异常波动公告》及三季报。
说明：融资额 1055 亿元、投后估值 6155 亿元为媒体口径（The Information 引知情人士），公司未回应，
      图中不呈现，仅正文标注为"媒体口径"；11-14 为周六，故 11-13 之后下一交易日为 11-16。
风格：克制传媒风，白底、低饱和配色、标题即结论。输出目录 = 脚本所在目录。
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle

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
GOLD = "#c9a27a"
GREEN = "#5a7d6f"

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
    fig = base("同一天，两个方向",
               "2026 年 11 月 19 日：钱进了 DeepSeek，股价砸向燧原")
    ax = canvas(fig)

    # 左：DeepSeek
    ax.add_patch(FancyBboxPatch((0.050, 0.230), 0.415, 0.560,
                                boxstyle="round,pad=0.012", facecolor="#edf2f0",
                                edgecolor=GREEN, linewidth=1.3))
    ax.text(0.078, 0.735, "DeepSeek", fontsize=17.0, color=GREEN, weight="bold",
            ha="left", va="center")
    ax.text(0.078, 0.688, "工商变更完成 · 11 月 17 日", fontsize=9.6,
            color=SLATE, ha="left", va="center")

    left_rows = [
        ("注册资本", "1644.75 万 → 1991.87 万元"),
        ("", "+21.1%"),
        ("新增股东", "杭州程砚，持股 17.265%"),
        ("外部出资方", "31 家，登记出资额约 34.39 亿元"),
    ]
    yy = 0.612
    for lab, val in left_rows:
        if lab:
            ax.text(0.078, yy, lab, fontsize=9.2, color=GRAY, ha="left",
                    va="center")
            ax.text(0.078, yy - 0.048, val, fontsize=11.0, color=DARK,
                    weight="bold", ha="left", va="center")
            yy -= 0.128
        else:
            ax.text(0.078, yy + 0.048, val, fontsize=11.0, color=GREEN,
                    weight="bold", ha="left", va="center")

    # 右：燧原
    ax.add_patch(FancyBboxPatch((0.535, 0.230), 0.415, 0.560,
                                boxstyle="round,pad=0.012", facecolor="#f7eae8",
                                edgecolor=RED, linewidth=1.3))
    ax.text(0.563, 0.735, "燧原科技", fontsize=17.0, color=RED, weight="bold",
            ha="left", va="center")
    ax.text(0.563, 0.688, "科创板 688801 · 11 月 19 日收盘", fontsize=9.6,
            color=SLATE, ha="left", va="center")

    right_rows = [
        ("收盘价", "364.33 元"),
        ("", "−20.00%　跌停"),
        ("成交 / 换手", "19.62 亿元　28.35%"),
        ("四个交易日", "回撤 36.16%，市值蒸发 1070 亿"),
    ]
    yy = 0.612
    for lab, val in right_rows:
        if lab:
            ax.text(0.563, yy, lab, fontsize=9.2, color=GRAY, ha="left",
                    va="center")
            ax.text(0.563, yy - 0.048, val, fontsize=11.0, color=DARK,
                    weight="bold", ha="left", va="center")
            yy -= 0.128
        else:
            ax.text(0.563, yy + 0.048, val, fontsize=11.0, color=RED,
                    weight="bold", ha="left", va="center")

    # 中间日期
    ax.text(0.500, 0.500, "11·19", fontsize=13.0, color=GRAY, weight="bold",
            ha="center", va="center", rotation=90)

    punchline(fig, "同一个行业，同一天：一边在签字，一边在跌停。")
    footer(fig, "事实：DeepSeek 据企查查/天眼查工商信息（第一财经、每日经济新闻 2026-11-19）；燧原据公司异动公告与三季报（每日经济新闻 2026-11-19）｜制图：本文")
    fig.savefig(OUT + "图1_同一天两个方向.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("31 家进了同一个平台",
               "杭州程砚的出资比例：谁在这轮 DeepSeek 融资里排前面")
    ax = canvas(fig)

    rows = [
        ("腾讯（上海珩岫）", 9.5653, GREEN),
        ("宁德时代（三只基金合计）", 9.5653, GREEN),
        ("中国移动（中移投资控股）", 7.6522, NAVY),
        ("中信证券投资", 7.6522, NAVY),
        ("砺思资本（天津砺思星深）", 7.1740, GOLD),
        ("国寿股权（青岛城鑫致达）", 4.7826, NAVY),
        ("石溪资本（杭州石溪兆易一号）", 3.3479, SLATE),
        ("博裕 / CPE 源峰 / 拾象 / 正心谷", 3.3479, SLATE),
        ("IDG（天津云程创投）", 3.3236, SLATE),
        ("中国电信 / vivo / 美的", 2.8700, SLATE),
        ("美团龙珠 / 君联 / 高榕", 2.8700, SLATE),
    ]

    x_left = 0.300
    x_scale = 0.520 / 10.0

    for i, (name, pct, col) in enumerate(rows):
        y = 0.800 - i * 0.060
        ax.text(x_left - 0.016, y, name, fontsize=9.4, color=DARK,
                ha="right", va="center")
        w = pct * x_scale
        ax.add_patch(FancyBboxPatch((x_left, y - 0.019), w, 0.038,
                                    boxstyle="round,pad=0.001",
                                    facecolor=col, edgecolor="none",
                                    alpha=0.92, zorder=3))
        ax.text(x_left + w + 0.010, y, f"{pct:.2f}%", fontsize=9.6, color=col,
                weight="bold", ha="left", va="center")

    ax.text(0.075, 0.145,
            "另有 13 家单家出资低于 2.87%：立臻精密、杭州雷火万相、嘉兴聚源曜辉、兆易创新、上海科慧、",
            fontsize=8.6, color=GRAY, ha="left", va="center")
    ax.text(0.075, 0.098,
            "横店柏晖、嘉兴弘卓科擎、中金河钢、行吟信息（小红书）、浙江吉利产投、中金浦成等。",
            fontsize=8.6, color=GRAY, ha="left", va="center")

    punchline(fig, "电和网，第一次以数十亿元级同轮进了大模型公司的股东名单。")
    footer(fig, "事实：出资比例据企查查/天眼查穿透，第一财经、每日经济新闻 2026-11-19；杭州程砚共 32 名合伙人（含执行事务合伙人杭州程策）｜制图：本文")
    fig.savefig(OUT + "图2_31家同一个平台.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("四个交易日，36%",
               "燧原科技 688801：11/13 收盘 570.68 元 → 11/19 收盘 364.33 元")
    ax = canvas(fig)

    pts = [
        ("11/13", 570.68, None, None),
        ("11/16", 500.00, "−12.39%", None),
        ("11/17", 483.40, "−3.32%", None),
        ("11/18", 455.41, "−5.79%", None),
        ("11/19", 364.33, "−20.00%", "跌停"),
    ]

    def y_of(p):
        return 0.300 + (p - 340.0) / 300.0 * 0.600

    for p in (400, 450, 500, 550, 600):
        y = y_of(p)
        ax.plot([0.085, 0.955], [y, y], color="#eceef1", linewidth=0.9, zorder=1)
        ax.text(0.072, y, str(p), fontsize=8.6, color=GRAY, ha="right",
                va="center")
    ax.text(0.072, 0.930, "元", fontsize=8.4, color=GRAY, ha="right",
            va="center")

    xs = [0.130, 0.320, 0.510, 0.700, 0.880]
    ys = [y_of(p[1]) for p in pts]

    ax.plot(xs, ys, color=NAVY, linewidth=2.4, solid_capstyle="round", zorder=4)

    for i, (x, y, (lab, price, note, extra)) in enumerate(zip(xs, ys, pts)):
        col = RED if i >= 1 else NAVY
        ax.add_patch(Circle((x, y), 0.011, facecolor=col, edgecolor=col,
                            linewidth=2.0, zorder=6))
        ax.text(x, 0.240, lab, fontsize=9.8, color=DARK, ha="center",
                va="center")
        ax.text(x, y + 0.034, f"{price:,.2f}", fontsize=10.2, color=col,
                weight="bold", ha="center", va="bottom")
        if note:
            ax.text(x, y - 0.036, note, fontsize=9.8, color=RED, weight="bold",
                    ha="center", va="top")
        if extra:
            ax.text(x + 0.020, y, extra, fontsize=9.6, color=RED, weight="bold",
                    ha="left", va="center")

    # 累计回撤标注
    ax.annotate("", xy=(0.930, y_of(364.33)), xytext=(0.930, y_of(570.68)),
                arrowprops=dict(arrowstyle="<->", color=RED, linewidth=1.5))
    ax.text(0.918, (y_of(364.33) + y_of(570.68)) / 2, "−36.16%", fontsize=12.0,
            color=RED, weight="bold", ha="right", va="center")

    # 底部说明
    ax.text(0.085, 0.168,
            "市值：11-18 约 1960 亿元 → 11-19 1568 亿元，单日蒸发 392 亿元；较 11-13 收盘缩水约 1070 亿元。",
            fontsize=9.2, color=SLATE, ha="left", va="center")
    ax.text(0.085, 0.112,
            "无限售流通股 1790.03 万股，占总股本 4.1595%。",
            fontsize=9.2, color=RED, weight="bold", ha="left", va="center")

    punchline(fig, "4% 的流通盘，20% 的跌停，不需要多少筹码。")
    footer(fig, "事实：收盘价据每日经济新闻 2026-11-19 引公司公告及行情；11-14 为周六，故 11-13 之后下一交易日为 11-16｜制图：本文")
    fig.savefig(OUT + "图3_四个交易日36%.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)
