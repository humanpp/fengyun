# -*- coding: utf-8 -*-
"""
《一只鸟，4 块 4》配套图表
事实口径（均经公开信息逐条核对）：
  · 潮新闻记者王嘉楠、季建荣、于瓅 2026-11-20 调查报道：走访时间为 2026 年 10 月以来，
    地点为广西柳州融水县、三江县，桂林荔浦市，贵州从江县。
    三江县饭店“红烧‘小鸡’20 只，88 元；烧烤‘小鸡’一只 6 元”，
    烧烤店老板“我拿货就要 4.5 元一只，总要让我赚一点”。
  · 荔浦市马岭镇地狮村陆某某棚子，多部门联合清点“活鸟及尸体共计 1599 只，
    其中禾花雀（黄胸鹀）8 只”。
  · 从江县刚边乡村民“网是 5 块钱一张买的，今天架了 3 张”。
  · 涉案物种：国家一级 黄胸鹀（禾花雀）；国家二级 红喉歌鸲、画眉、红胁绣眼鸟、
    北领角鸮；以及树鹨等大量“三有”保护动物。
  · 黄胸鹀：国家林业和草原局、农业农村部公告 2021 年第 3 号新版《国家重点保护
    野生动物名录》，2021-02-01 发布；IUCN 2017 年列为极危（CR）；
    浙江农林大学副教授何珂“三十来年间种群数量下降 84%～95%”。
  · 执法：2026-11-08 三江梅林乡车寨村相思屯 抓获 6 名、立案 3 起、鸟类 27 只；
    融水白云乡与拱洞乡 抓获 13 名、立案 11 起、查获上千只；
    2026-11-12 三江县公安局通报 7 人落网；2026-11-11 全区鸟类保护工作视频会议，
    执行 2026 年第 2 号总林长令。
换算说明：“88÷20＝4.4”“1599×4.5≈7200”为公开数字的直接相除与相乘，
     1599 只中绝大多数为“三有”鸟类而非黄胸鹀，折算只用于说明量级。
风格：克制传媒风，白底、低饱和配色、标题即结论。输出目录 = 脚本所在目录。
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False

NAVY = "#1f3a5f"
RED = "#a83f36"
GRAY = "#8a8f98"
SLATE = "#5f6673"
LIGHT = "#d8dbe0"
DARK = "#2b2f36"
PALE = "#eef0f3"
SAND = "#f7f3ea"
GOLD = "#c2a15c"
GREEN = "#5a7d6f"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep


def base(title, sub):
    fig = plt.figure(figsize=(12, 6.8))
    fig.patch.set_facecolor("white")
    fig.text(0.045, 0.950, title, fontsize=20, color=DARK, weight="bold",
             ha="left", va="top")
    fig.text(0.045, 0.878, sub, fontsize=10.8, color=GRAY, ha="left", va="top")
    return fig


def footer(fig, line1, line2):
    fig.text(0.045, 0.042, line1, fontsize=7.6, color=GRAY, ha="left", va="center")
    fig.text(0.045, 0.020, line2, fontsize=7.6, color=GRAY, ha="left", va="center")


def punchline(fig, text, y=0.080):
    fig.text(0.045, y, text, fontsize=10.8, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.6", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


def canvas(fig, bottom=0.135, height=0.700):
    ax = fig.add_axes([0.045, bottom, 0.915, height])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return ax


# ------------------------------------------------------------------ 图 1
def fig1():
    fig = base("一只鸟，4 块 4",
               "餐馆里一份红烧“小鸡”的价，除以只数")
    ax = canvas(fig)

    # 算式
    ax.add_patch(FancyBboxPatch((0.050, 0.700), 0.900, 0.195,
                                boxstyle="round,pad=0.012", facecolor=SAND,
                                edgecolor="#d9cdb6", linewidth=1.0))
    ax.text(0.090, 0.822, "88 元 ÷ 20 只 ＝ 4.4 元", fontsize=23, color=DARK,
            weight="bold", ha="left", va="center")
    ax.text(0.090, 0.742, "三江县一家饭店，红烧“小鸡”20 只 88 元", fontsize=9.6,
            color="#8a7a5e", ha="left", va="center")

    # 价格条
    VMAX = 7.0

    def X(v):
        return 0.340 + v / VMAX * 0.560

    bars = [
        (0.545, "烧烤店卖价", 6.0, NAVY, "一只"),
        (0.435, "烧烤店拿货", 4.5, SLATE, "一只"),
        (0.325, "红烧折算", 4.4, GOLD, "一只"),
    ]
    for i in range(0, 8, 2):
        ax.plot([X(i), X(i)], [0.285, 0.600], color="#eef0f3", linewidth=0.9,
                zorder=1)
        ax.text(X(i), 0.258, "%d" % i, fontsize=8.6, color=GRAY, ha="center",
                va="top")
    ax.text(0.340, 0.222, "元 / 只", fontsize=8.6, color=GRAY, ha="left",
            va="top")

    for y, name, val, col, unit in bars:
        ax.barh(y, X(val) - 0.340, left=0.340, height=0.078, color=col,
                edgecolor="none", zorder=3)
        ax.text(0.322, y, name, fontsize=11.0, color=DARK, ha="right",
                va="center")
        ax.text(X(val) + 0.014, y, "%.1f 元" % val, fontsize=11.0, color=col,
                weight="bold", ha="left", va="center")

    # 量的换算
    ax.text(0.340, 0.150,
            "荔浦那间棚子里 1599 只，按 4.5 元一只折算约 7200 元；一张捕鸟网 5 元。",
            fontsize=9.4, color=SLATE, ha="left", va="center")

    punchline(fig, "这条链上最便宜的一环，是一条命。")
    footer(fig,
           "事实：价格据潮新闻 2026-11-20 调查报道——三江县饭店红烧“小鸡”20 只 88 元、烧烤一只 6 元，烧烤店老板“我拿货就要 4.5 元一只”；",
           "荔浦市马岭镇地狮村棚内活鸟及尸体共 1599 只，据同报道；从江县村民“网是 5 块钱一张买的”｜制图：本文")
    fig.savefig(OUT + "图1_四块四.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("“小鸡”里装着的是什么",
               "同一批被查获的鸟，保护级别并不一样")
    ax = canvas(fig)

    cards = [
        (0.900, 0.660, RED, "#fdf6f5", "国家一级保护野生动物", "黄胸鹀（禾花雀）",
         "1 种"),
        (0.620, 0.390, NAVY, "#f6f8fa", "国家二级保护野生动物",
         "红喉歌鸲、画眉、红胁绣眼鸟、北领角鸮", "4 种"),
        (0.350, 0.135, GOLD, "#faf7f0", "“三有”保护动物",
         "树鹨等，数量最大的一类", "大量"),
    ]

    for top, bot, col, bg, tag, name, count in cards:
        ax.add_patch(FancyBboxPatch((0.050, bot), 0.550, top - bot,
                                    boxstyle="round,pad=0.010", facecolor=bg,
                                    edgecolor=LIGHT, linewidth=1.0))
        ax.add_patch(Rectangle((0.050, bot + 0.012), 0.010, top - bot - 0.024,
                               facecolor=col, edgecolor="none"))
        h = top - bot
        ax.text(0.078, top - h * 0.28, tag, fontsize=9.0, color=col,
                weight="bold", ha="left", va="center")
        ax.text(0.078, top - h * 0.66, name, fontsize=12.4, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(0.578, top - h * 0.50, count, fontsize=15.0, color=col,
                weight="bold", ha="right", va="center")

    # 右侧：黄胸鹀这一条线
    ax.add_patch(FancyBboxPatch((0.630, 0.390), 0.320, 0.510,
                                boxstyle="round,pad=0.012", facecolor=SAND,
                                edgecolor="#d9cdb6", linewidth=1.0))
    ax.text(0.658, 0.855, "黄胸鹀这一条", fontsize=9.6, color="#8a7a5e",
            weight="bold", ha="left", va="center")
    ax.text(0.658, 0.775, "2021 年 2 月", fontsize=10.4, color=DARK,
            weight="bold", ha="left", va="center")
    ax.text(0.658, 0.712, "列入新版《国家重点保护\n野生动物名录》，定为一级",
            fontsize=8.8, color=SLATE, ha="left", va="center", linespacing=1.8)
    ax.text(0.658, 0.618, "2017 年", fontsize=10.4, color=DARK,
            weight="bold", ha="left", va="center")
    ax.text(0.658, 0.572, "IUCN 列为“极危（CR）”", fontsize=8.8, color=SLATE,
            ha="left", va="center")
    ax.text(0.658, 0.488, "84%～95%", fontsize=17.0, color=RED, weight="bold",
            ha="left", va="center")
    ax.text(0.658, 0.428, "食鸟“习俗”产业化之后，\n三十来年间种群下降",
            fontsize=8.8, color=SLATE, ha="left", va="center", linespacing=1.8)

    punchline(fig, "菜单上写“小鸡”，名录上写一级、二级。")
    footer(fig,
           "事实：物种与保护级别据潮新闻 2026-11-20 调查报道；黄胸鹀列入国家一级据国家林业和草原局、农业农村部公告 2021 年第 3 号（2021-02-01 发布）；",
           "IUCN 红色名录 2017 年列为极危（CR）据江苏省林业局 2024-10-12；84%～95% 及“食鸟习俗产业化”据浙江农林大学副教授何珂在同报道中的表述｜制图：本文")
    fig.savefig(OUT + "图2_小鸡里有什么.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("抓了人，网又架起来",
               "11 月的执法动作，和村民口中的下一次")
    ax = canvas(fig)

    y0 = 0.660
    ax.plot([0.070, 0.945], [y0, y0], color=LIGHT, linewidth=2.2, zorder=2)

    ups = [
        (0.115, "11.08", "三江梅林乡", "抓获 6 名，立案 3 起，鸟 27 只", NAVY),
        (0.605, "11.11", "全区会议", "执行第 2 号总林长令", GOLD),
    ]
    downs = [
        (0.355, "11.08", "融水白云乡·拱洞乡", "抓获 13 名，立案 11 起，上千只", GREEN),
        (0.855, "11.12", "三江县公安局", "通报 7 人落网", RED),
    ]

    for x, date, name, desc, col in ups:
        ax.add_patch(Circle((x, y0), 0.0125, facecolor=col, edgecolor="white",
                            linewidth=2.0, zorder=6))
        ax.text(x, y0 + 0.042, date, fontsize=9.2, color=col, weight="bold",
                ha="center", va="bottom")
        ax.text(x, y0 + 0.078, name, fontsize=11.6, color=DARK, weight="bold",
                ha="center", va="bottom")
        ax.text(x, y0 + 0.120, desc, fontsize=8.4, color=SLATE, ha="center",
                va="bottom")

    for x, date, name, desc, col in downs:
        ax.add_patch(Circle((x, y0), 0.0125, facecolor=col, edgecolor="white",
                            linewidth=2.0, zorder=6))
        ax.text(x, y0 - 0.042, date, fontsize=9.2, color=col, weight="bold",
                ha="center", va="top")
        ax.text(x, y0 - 0.078, name, fontsize=11.6, color=DARK, weight="bold",
                ha="center", va="top")
        ax.text(x, y0 - 0.120, desc, fontsize=8.4, color=SLATE, ha="center",
                va="top")

    # 两段引语
    quotes = [
        (0.050, 0.420, "村民", "“政府知道了，网和杆子就收了拿去烧。\n今年来了两回。他们一走，网又搞起来了。”",
         RED, "#fdf6f5"),
        (0.520, 0.425, "浙江农林大学副教授 何珂",
         "“连续几年严打之后，盗猎压力并没有消失，\n只是转移到了其他鸟类身上。”",
         SLATE, "#f6f8fa"),
    ]
    for x, w, who, text, col, bg in quotes:
        ax.add_patch(FancyBboxPatch((x, 0.190), w, 0.260,
                                    boxstyle="round,pad=0.012", facecolor=bg,
                                    edgecolor=col, linewidth=1.1))
        ax.text(x + 0.026, 0.408, who, fontsize=8.8, color=col, weight="bold",
                ha="left", va="center")
        ax.text(x + 0.026, 0.302, text, fontsize=9.4, color=DARK, ha="left",
                va="center", linespacing=2.0)

    punchline(fig, "5 块钱一张网，烧了再买一张。")
    footer(fig,
           "事实：2026-11-08 三江侗族自治县梅林乡车寨村相思屯抓获 6 名、立案 3 起、查获鸟类 27 只，融水白云乡与拱洞乡抓获 13 名、立案 11 起、查获上千只，",
           "据柳州市林业和园林局 2026-11-18、广西新闻网 2026-11-15；三江县公安局 2026-11-12 通报；全区会议据广西林业局经国家林草局 2026-11-18｜制图：本文")
    fig.savefig(OUT + "图3_抓了又架.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)