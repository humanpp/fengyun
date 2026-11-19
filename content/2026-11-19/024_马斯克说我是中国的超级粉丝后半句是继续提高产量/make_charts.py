# -*- coding: utf-8 -*-
"""
《"我是中国的超级粉丝"，后半句是继续提高产量》配套图表
事实口径（2026-11-19，直接核对新华社电稿、央视稿、贸促会发布会实录与乘联会数据后）：
  · 2026 年 11 月 19 日，特斯拉 CEO 埃隆·马斯克在深圳说"我是中国的超级粉丝"，
    并称"中国很酷。我一直鼓励世界各地的人们来中国走走……""美中合作越多，
    各自也会越好"；中国贸促会会长任鸿斌当天在深圳会见马斯克（新华社 11-19、
    央视新闻 11-19）。马斯克表示特斯拉会继续在中国提高产量（央视财经 11-19）。
  · 2026 年是 APEC 中国年，中国第三次担任东道主；APEC 第三十三次领导人非正式
    会议在深圳举行，工商领导人峰会 11 月 17—18 日在深圳前海国际会议中心举办，
    由中国贸促会主办，主题"共促繁荣，共赢未来"，20 余个经济体 2000 余名政商
    界领袖参会，含 115 家《财富》世界 500 强企业，美国企业占参会方近 20%
    （中国贸促会 11-15 发布会实录、人民网 11-17、美通社 11-18）。
  · 马斯克 11 月 18 日抵达深圳，这是他首次公开到访深圳；19 日他还远程连线了
    在美国奥斯汀举行的 TomorrowX Summit，称"我是中国的粉丝，我总是鼓励人们
    来中国走走"（中新网 11-19、新浪财经 11-19）。
  · 特斯拉中国 10 月（乘联会）：批发 67,829 辆（同比 +10.3%，环比 -28.9%）；
    其中上海工厂出口 59,012 辆（同比 +66.3%，占批发 87%），国内零售 8,817 辆
    （同比 -66.1%，为 2022 年 7 月以来最低）；国内交付中 Model Y 7,807 辆、
    Model 3 1,010 辆（乘联会数据，经路透 11-03、凤凰网 11-11、AutoCN 11-10）。
  · 1—10 月（乘联会数据经 CnEVPost 汇总）：上海工厂交付 810,889 辆
    （同比 +21.4%），其中在华零售 389,905 辆（同比 -15.0%）、出口 420,984 辆
    （同比 +101.3%）；交付 = 零售 + 出口。
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
    fig = base("八成七的产量去了海外",
               "2026 年 10 月｜特斯拉上海超级工厂批发销量去向（乘联会数据）")
    ax = canvas(fig)

    ax.text(0.028, 0.820, "当月批发 67,829 辆", fontsize=10.0, color=SLATE,
            ha="left", va="center")
    ax.text(0.028, 0.735, "67,829", fontsize=34.0, color=DARK, weight="bold",
            ha="left", va="center")
    ax.text(0.028, 0.660, "同比 +10.3%，环比 -28.9%；连续 12 个月同比增长",
            fontsize=8.8, color=GRAY, ha="left", va="center")

    y, h = 0.520, 0.115
    w_export = 0.870 * 0.920
    w_dom = 0.130 * 0.920

    ax.add_patch(Rectangle((0.030, y), w_export, h, facecolor=NAVY,
                           edgecolor="white", linewidth=2.0))
    ax.add_patch(Rectangle((0.030 + w_export, y), w_dom, h, facecolor=RED,
                           edgecolor="white", linewidth=2.0))

    ax.text(0.030 + w_export / 2, y + h / 2, "出口 59,012 辆（87%）",
            fontsize=11.0, color="white", weight="bold", ha="center",
            va="center")
    ax.text(0.030 + w_export + w_dom / 2, y + h - 0.030, "8,817", fontsize=9.0,
            color="white", weight="bold", ha="center", va="center")
    ax.text(0.030 + w_export + w_dom / 2, y + 0.026, "国内零售", fontsize=8.0,
            color="white", ha="center", va="center")

    ax.text(0.030, 0.430,
            "出口同比 +66.3%，为年内第二高；国内零售同比 -66.1%，"
            "是 2022 年 7 月以来最低的单月水平。",
            fontsize=9.0, color=SLATE, ha="left", va="center")
    ax.text(0.030, 0.375,
            "国内交付里，Model Y 7,807 辆、Model 3 1,010 辆：两款主力车型一个月的"
            "国内零售加起来不到九千辆。",
            fontsize=9.0, color=SLATE, ha="left", va="center")

    ax.plot([0.030, 0.950], [0.310, 0.310], color=LIGHT, linewidth=0.9)

    ax.add_patch(FancyBboxPatch((0.030, 0.180), 0.920, 0.086,
                                boxstyle="round,pad=0.006",
                                facecolor="white", edgecolor=LIGHT,
                                linewidth=1.0))
    ax.text(0.054, 0.223,
            "同一座工厂、同一条产线：产量的增量几乎全部流向海外市场，"
            "中国消费者拿到的是降幅。",
            fontsize=9.0, color=SLATE, ha="left", va="center")

    punchline(fig, "产量在涨，卖给中国消费者的在少。")
    footer(fig, "事实：乘联会（CPCA）2026 年 10 月数据，经路透 11-03、AutoCN 11-10、"
                "凤凰网 11-11 转述；出口占比与同比为本文据上述数据换算｜制图：本文")
    fig.savefig(OUT + "图1_八成七去了海外.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("增量全在海外，国内在减",
               "2026 年 1—10 月｜特斯拉上海超级工厂交付结构（乘联会数据汇总）")
    ax = canvas(fig)

    rows = [
        ("上海工厂交付", 810889, "+21.4%", "含出口与国内零售", NAVY),
        ("其中：出口", 420984, "+101.3%", "同比翻倍", RED),
        ("其中：在华零售", 389905, "-15.0%", "国内消费者买到的新车", GRAY),
    ]

    x0 = 0.300
    scale = 0.560 / 850000.0

    y = 0.720
    for name, value, yoy, note, color in rows:
        ax.text(0.028, y + 0.020, name, fontsize=9.8, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(0.028, y - 0.026, note, fontsize=7.8, color=GRAY,
                ha="left", va="center")

        ax.add_patch(Rectangle((x0, y - 0.030), value * scale, 0.060,
                               facecolor=color, edgecolor="none"))
        ax.text(x0 + value * scale + 0.014, y, "{:,}".format(value),
                fontsize=11.4, color=DARK, weight="bold", ha="left",
                va="center")
        ax.text(x0 + value * scale + 0.014, y - 0.048, yoy, fontsize=8.6,
                color=(NAVY if yoy.startswith("+") else RED), ha="left",
                va="center")
        y -= 0.215

    ax.text(0.028, 0.178,
            "交付 = 在华零售 + 出口。三条线里，只有出口在加速：1—10 月出口同比"
            "翻了一倍还多，国内零售则连续第五个月同比下滑。",
            fontsize=9.0, color=SLATE, ha="left", va="center")
    ax.text(0.028, 0.120,
            "上海工厂年产能约 100 万辆，是特斯拉全球最大的生产基地和出口枢纽；"
            "所谓“提高在华产量”，先影响的是这条出口曲线。",
            fontsize=9.0, color=GRAY, ha="left", va="center")

    punchline(fig, "“在中国提高产量”和“在中国多卖车”，是两件事。")
    footer(fig, "事实：乘联会数据经 CnEVPost 汇总（1—10 月交付 810,889、零售 389,905、"
                "出口 420,984），10 月单月数据经路透 11-03；年产能为公开资料｜"
                "同比为原表口径｜制图：本文")
    fig.savefig(OUT + "图2_交付零售出口三条线.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("这句话说在深圳，这一周深圳很忙",
               "2026 年 APEC 中国年｜深圳的四个时间点")
    ax = canvas(fig)

    ax.plot([0.070, 0.950], [0.560, 0.560], color=LIGHT, linewidth=2.0,
            solid_capstyle="round")

    nodes = [
        (0.120, "11.15", "发布会", "贸促会通报：2000 余名\n政商领袖参会", True),
        (0.380, "11.17—18", "工商领导人峰会", "前海国际会议中心\n115 家世界 500 强", False),
        (0.645, "11.18", "马斯克抵深", "首次公开到访深圳\n随美方团队", True),
        (0.910, "11.19", "会见与发言", "任鸿斌会见；“超级粉丝”\n邀请明年参加链博会", False),
    ]

    for x, date, head, note, above in nodes:
        ax.plot([x], [0.560], marker="o", markersize=8.0, color=NAVY,
                markeredgecolor="white", markeredgewidth=1.4, zorder=5)
        if above:
            ax.plot([x, x], [0.580, 0.640], color=LIGHT, linewidth=1.2)
            ax.text(x, 0.660, date, fontsize=8.4, color=GRAY, ha="center",
                    va="bottom")
            ax.text(x, 0.712, head, fontsize=10.8, color=NAVY, weight="bold",
                    ha="center", va="bottom")
            ax.text(x, 0.775, note, fontsize=8.0, color=SLATE, ha="center",
                    va="bottom", linespacing=1.5)
        else:
            ax.plot([x, x], [0.480, 0.540], color=LIGHT, linewidth=1.2)
            ax.text(x, 0.462, date, fontsize=8.4, color=GRAY, ha="center",
                    va="top")
            ax.text(x, 0.404, head, fontsize=10.8, color=NAVY, weight="bold",
                    ha="center", va="top")
            ax.text(x, 0.338, note, fontsize=8.0, color=SLATE, ha="center",
                    va="top", linespacing=1.5)

    ax.text(0.028, 0.235,
            "这一周在深圳开的是 APEC 第三十三次领导人非正式会议，中国第三次担任"
            "东道主；工商峰会是配套活动，美国企业占参会方近 20%。",
            fontsize=9.0, color=SLATE, ha="left", va="center")
    ax.text(0.028, 0.180,
            "同一天，习近平在深圳会见特朗普。马斯克那句“美中合作越多，各自也会越好”，"
            "落在这个背景里。",
            fontsize=9.0, color=SLATE, ha="left", va="center")

    punchline(fig, "话说在深圳，生意也在深圳。")
    footer(fig, "事实：中国贸促会 11-15 专题发布会实录、人民网 11-17、美通社 11-18、"
                "中新网 11-19、新浪财经 11-19、第一财经 11-19；"
                "元首会晤据财新网 11-19｜制图：本文")
    fig.savefig(OUT + "图3_深圳这一周.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)
