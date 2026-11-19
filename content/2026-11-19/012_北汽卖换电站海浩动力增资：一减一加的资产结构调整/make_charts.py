# -*- coding: utf-8 -*-
"""
《北汽卖换电站，海浩动力增资》配套图表
事实口径（2026-11-19，逐条核对港交所公告与公开报道后）：
  · 北京汽车（01958.HK）11 月 17 日晚间公告：全资附属北汽动力总成拟通过北京产权交易所
    公开挂牌竞价，转让与 112 座换电站相关的资产组组合（存货、固定资产、在建工程、无形资产）；
    评估基准日 2026 年 9 月 30 日，账面价值约 2.74 亿元，成本法评估值约 2.78 亿元（不含税），
    增值约 1.54%；挂牌价不低于评估值；11 月底前提交北交所披露公告；
    意向受让方尚不明确，未签署协议；若年内按评估值完成，预计 2026 年综合溢利增加约 352 万元
    （公告、观点网 11-17、东方财富 11-17、证券日报 11-18）；
  · 出售的是资产组，不是换电运营主体股权（证券日报 11-18、环球网 11-17）；
  · 北汽自营换电网络规模变化：2019 年在 15 城运营 1.3 万辆换电出租车、建站 148 座；
    2021 年一季度 19 城 255 座；2026 年 11 月拟出售 112 座（OFweek 11-19）；
    2017 年擎天柱计划曾提出到 2022 年投资 100 亿元、建成 3000 座光储换电站（OFweek 11-19）；
  · 北汽集团 10 月 22 日与宁德时代签署全面深化换电业务合作协议，共建百万辆级换电生态；
    11 月 13 日极狐发布「极+时代」全民换电生态，宣布将与宁德时代共建 3 万座换电站，
    两年覆盖全国全部城市；截至 2026 年 9 月底巧克力换电已建成超 2500 座、覆盖 31 省 200 城
    （北汽集团官网 10-22、中新社 11-14、新浪财经 11-14）；
  · 北京海浩动力系统有限公司注册资本由约 6.75 亿元增至约 8.55 亿元，增幅约 27%；
    成立于 2023 年 7 月，法定代表人金勋；股东为北京海纳川汽车部件股份有限公司（北汽集团旗下）、
    嘉兴湾北科创发展集团有限公司、北京市绿色能源和低碳产业投资基金（有限合伙）、
    北京市先进制造和智能装备产业投资基金（有限合伙）、浩夫尔动力总成国际公司；
    北交金科 2026 年 9 月 14 日已挂出该增资项目（界面新闻 11-18、东方财富 11-18、北交金科）；
  · 北京汽车股价 11 月 18 日报 0.53 港元，跌 1.85%，盘中最低 0.525 港元，创上市以来新低
    （财华社 11-18）。
本文换算（非当事方口径）：2.78 亿 / 112 座 ≈ 248 万元 / 座；2.78 亿 / 8.55-6.75 亿 ≈ 1.54 倍；
352 万元 / 2.78 亿 ≈ 1.3%。
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

V_SALE = 2.78
V_INJECT = 8.55 - 6.75
PER_STATION = V_SALE * 10000 / 112.0
RATIO = V_SALE / V_INJECT


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


# ------------------------------------------------------------------ 图 1
def fig1():
    fig = base("自营换电站，座数一直在往下走",
               "北汽是国内最早把换电做成商业运营的车企，这张图是它自营网络的规模变化")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    x0 = 0.250
    scale = 0.400 / 300.0

    bars = [
        ("2019 年", "15 城 · 1.3 万辆换电出租车", 148, SLATE, 0.720),
        ("2021 年一季度", "19 城", 255, NAVY, 0.500),
        ("2026 年 11 月", "拟整体挂牌出售", 112, RED, 0.280),
    ]

    for date, note, n, color, y in bars:
        ax.add_patch(Rectangle((x0, y - 0.046), n * scale, 0.092,
                               facecolor=color, edgecolor="none"))
        ax.text(0.030, y + 0.028, date, fontsize=10.4, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(0.030, y - 0.022, note, fontsize=8.4, color=GRAY, ha="left",
                va="center")
        ax.text(x0 + n * scale + 0.018, y, "%d 座" % n, fontsize=15.0,
                color=DARK, weight="bold", ha="left", va="center")

    # 3000 座目标与 255 座峰值不在同一量级，改用文字标注，避免坐标轴压缩
    ax.plot([0.030, 0.960], [0.150, 0.150], color=LIGHT, linewidth=0.9)
    ax.text(0.030, 0.104,
            "2017 年擎天柱计划曾提出到 2022 年投资 100 亿元、建成 3000 座光储换电站——"
            "那座目标从未出现在这张图上。",
            fontsize=9.2, color=SLATE, ha="left", va="center")

    punchline(fig, "这次卖的不是换电业务的股权，是这条曲线剩下的那一段。")
    footer(fig, "事实：2019 与 2021 年数据据 OFweek 11-19 整理；2026 年 112 座据北京汽车 11-17 公告；"
                "擎天柱计划目标据 OFweek 11-19｜制图：本文")
    fig.savefig(OUT + "图1_座数在往下走.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("一减一加，量级相当",
               "卖换电站资产 2.78 亿元，海浩动力注册资本增加 1.8 亿元")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    x0 = 0.250
    scale = 0.420 / 3.0

    items = [
        ("减", "出售换电站资产组", "北汽动力总成 · 112 座", V_SALE, RED, 0.680),
        ("加", "海浩动力增资", "注册资本 6.75 亿 → 8.55 亿", V_INJECT, NAVY, 0.400),
    ]

    for tag, name, note, v, color, y in items:
        ax.add_patch(Rectangle((x0, y - 0.048), v * scale, 0.096,
                               facecolor=color, edgecolor="none"))
        ax.text(0.030, y + 0.040, tag, fontsize=15.0, color=color,
                weight="bold", ha="left", va="center")
        ax.text(0.086, y + 0.042, name, fontsize=10.6, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(0.086, y - 0.010, note, fontsize=8.4, color=GRAY, ha="left",
                va="center")
        ax.text(x0 + v * scale + 0.018, y, "%.2f 亿元" % v, fontsize=15.0,
                color=DARK, weight="bold", ha="left", va="center")

    ax.plot([0.030, 0.960], [0.310, 0.310], color=LIGHT, linewidth=0.9)
    ax.text(0.030, 0.250, "两个数放在一起看", fontsize=8.8, color=GRAY,
            ha="left", va="center")
    ax.text(0.250, 0.250,
            "卖出额是增资额的约 %.1f 倍　｜　折每座约 %.0f 万元　｜　"
            "按评估值完成，2026 年综合溢利增约 352 万元，约为交易额的 1.3%%"
            % (RATIO, PER_STATION),
            fontsize=9.2, color=SLATE, ha="left", va="center")

    ax.text(0.030, 0.170,
            "一进一出并不是同一层级的两件事：前者卖掉的是十年攒下的重资产，"
            "后者增加的是一笔可以继续投进去的资本金。",
            fontsize=9.2, color=SLATE, ha="left", va="center")

    punchline(fig, "减的是历史，加的是下一个十年，两笔钱的量级刚好相当。")
    footer(fig, "事实：出售金额据北京汽车 11-17 公告（评估值，不含税）；增资据界面新闻、"
                "东方财富 11-18（天眼查工商变更）｜倍数与单价为本文换算｜制图：本文")
    fig.savefig(OUT + "图2_一减一加.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("同一周，三个层各做各的事",
               "集团在扩网络，上市公司在退自营，动力板块在补资本金")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    cards = [
        (0.030, "集团层面", "北汽集团 × 宁德时代", NAVY,
         ["10 月 22 日签全面深化换电合作协议",
          "11 月 13 日极狐发布「极+时代」",
          "与宁德时代共建 3 万座换电站"]),
        (0.515, "上市公司层面", "北京汽车（01958.HK）", RED,
         ["112 座自营换电站资产组挂牌",
          "评估值约 2.78 亿元，成本法",
          "公告称集中资源于主营业务"]),
    ]

    for x, tag, name, color, lines in cards:
        ax.add_patch(FancyBboxPatch((x, 0.452), 0.455, 0.372,
                                    boxstyle="round,pad=0.010",
                                    facecolor="white", edgecolor=LIGHT,
                                    linewidth=1.0))
        ax.add_patch(Rectangle((x, 0.818), 0.455, 0.006, facecolor=color,
                               edgecolor="none"))
        ax.text(x + 0.030, 0.758, tag, fontsize=9.0, color=GRAY, ha="left",
                va="center")
        ax.text(x + 0.030, 0.696, name, fontsize=11.6, color=color,
                weight="bold", ha="left", va="center")
        ax.plot([x + 0.030, x + 0.425], [0.648, 0.648], color=LIGHT, lw=0.8)
        yy = 0.590
        for ln in lines:
            ax.text(x + 0.030, yy, ln, fontsize=8.6, color=DARK, ha="left",
                    va="center")
            yy -= 0.052

    # 第三层
    ax.add_patch(FancyBboxPatch((0.030, 0.170), 0.940, 0.230,
                                boxstyle="round,pad=0.010",
                                facecolor="white", edgecolor=LIGHT,
                                linewidth=1.0))
    ax.add_patch(Rectangle((0.030, 0.394), 0.940, 0.006, facecolor=SLATE,
                           edgecolor="none"))
    ax.text(0.060, 0.336, "动力板块", fontsize=9.0, color=GRAY, ha="left",
            va="center")
    ax.text(0.060, 0.276, "北京海浩动力系统", fontsize=11.6, color=SLATE,
            weight="bold", ha="left", va="center")
    ax.text(0.060, 0.212,
            "注册资本 6.75 亿 → 8.55 亿（+27%）｜成立于 2023 年 7 月｜"
            "海纳川等五方持股，非集团全资",
            fontsize=8.6, color=DARK, ha="left", va="center")

    ax.text(0.030, 0.108,
            "三件事方向不一致，但都指向同一件事：换电这张网，北汽决定不再自己扛，"
            "改由集团层面接入别人的网络。",
            fontsize=9.2, color=SLATE, ha="left", va="center")

    punchline(fig, "不是退出换电，是换一种方式留在换电里。")
    footer(fig, "事实：集团与宁德时代合作据北汽集团官网 10-22、中新社 11-14；"
                "上市公司公告据 11-17；海浩动力股东与增资据界面新闻 11-18、北交金科｜制图：本文")
    fig.savefig(OUT + "图3_三个层各做各的事.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)