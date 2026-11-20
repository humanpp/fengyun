# -*- coding: utf-8 -*-
"""
《婚假最长 30 天，但“29 个省”这个数对不上》配套图表
事实口径（均经公开信息逐条核对）：
  · 省级统计口径随时点在变：央视网 2024-11-22 为 25 个省份；
    央视网 2025-07-18 为 28 个；《法治日报》2025-11-11 仍为 28 个，
    并明确“还未调整婚假时长的广东、广西仍是 3 天”；界面新闻 2026-08-12
    写“截至 2025 年 10 月底，全国已有 29 个省份延长婚假”；
    澎湃新闻 2026-11-20 仍写“29 个省区市”。
  · 广西：2026-09-24 自治区十四届人大常委会第二十七次会议通过修改决定，
    在《广西壮族自治区人口和计划生育条例》第二十七条增加一款
    “增加婚假十五天”，自公布之日起施行（2026-09-28 公布）。
    国家 3 天 + 地方 15 天 = 18 天，这 15 天是条例直接增加的婚假，不是婚检加假。
    —— 广西人大网 2026-09-28 公告（十四届第 60 号）。
  · 山西：《山西省人口和计划生育条例》（2021 修订）第二十五条
    “依法办理结婚登记的夫妻可以享受婚假三十日”，2021-09-29 起执行。
  · 甘肃：2016-04-01 省十二届人大常委会第二十二次会议通过修正版条例，婚假 30 天。
    —— 甘肃人大网 2016-04-11。比山西早 5 年 5 个月。
  · 婚检加假：河南 3+18=21 天，参加婚检 +7 → 28 天；
    四川 20 天，自愿婚检 +5 → 25 天；黑龙江 15 日，婚检 +10 → 25 日；
    陕西 国家 3 天 + 婚检 10 天 = 13 天；宁夏 10 天 + 婚检 3 天 = 13 天。
  · 湖南：为“鼓励用人单位延长至 20 天”，非强制，图中以虚线区分。
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


def footer(fig, line1, line2):
    fig.text(0.045, 0.042, line1, fontsize=7.6, color=GRAY, ha="left", va="center")
    fig.text(0.045, 0.020, line2, fontsize=7.6, color=GRAY, ha="left", va="center")


def punchline(fig, text, y=0.080):
    fig.text(0.045, y, text, fontsize=10.8, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.6", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


def canvas(fig, bottom=0.150, height=0.690):
    ax = fig.add_axes([0.045, bottom, 0.915, height])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return ax


# ------------------------------------------------------------------ 图 1
def fig1():
    fig = base("30 天到 3 天：一张不齐的表",
               "已核实省份的婚假天数（国家规定 3 天 + 地方增加）")
    ax = fig.add_axes([0.115, 0.185, 0.700, 0.640])
    ax.set_facecolor("white")

    rows = [
        ("甘肃", 30, 0, "solid", "", SLATE),
        ("山西", 30, 0, "solid", "", SLATE),
        ("河南", 21, 7, "solid", "婚检 +7", GOLD),
        ("四川", 20, 5, "solid", "婚检 +5", GOLD),
        ("黑龙江", 15, 10, "solid", "婚检 +10", GOLD),
        ("新疆", 23, 0, "solid", "", SLATE),
        ("广西", 18, 0, "solid", "国家 3 + 地方 15", SLATE),
        ("湖北", 15, 0, "solid", "", SLATE),
        ("陕西", 3, 10, "solid", "婚检 +10", GOLD),
        ("宁夏", 10, 3, "solid", "婚检 +3", GOLD),
        ("浙江", 13, 0, "solid", "", SLATE),
        ("湖南", 3, 17, "dashed", "", GOLD),
        ("广东", 3, 0, "solid", "", SLATE),
    ]

    n = len(rows)
    ys = list(range(n))[::-1]
    ax.set_ylim(-0.9, n - 0.1)
    ax.set_xlim(0, 40)
    ax.set_yticks(ys)
    ax.set_yticklabels([r[0] for r in rows], fontsize=11, color=DARK)
    ax.tick_params(axis="y", length=0, pad=8)

    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(LIGHT)
    ax.tick_params(axis="x", colors=GRAY, labelsize=9)
    ax.set_xticks([0, 5, 10, 15, 20, 25, 30])
    ax.grid(axis="x", color="#eef0f3", linewidth=0.9)
    ax.set_axisbelow(True)

    for y, (name, b, extra, style, note, ncol) in zip(ys, rows):
        ax.barh(y, b, height=0.58, color=NAVY, edgecolor="none", zorder=3)
        if extra:
            if style == "dashed":
                ax.barh(y, extra, left=b, height=0.58, facecolor="none",
                        edgecolor=GOLD, linewidth=1.6, linestyle=(0, (3, 2)),
                        zorder=3)
            else:
                ax.barh(y, extra, left=b, height=0.58, color=GOLD,
                        edgecolor="none", zorder=3)
        if style == "dashed":
            ax.text(b + extra + 0.7, y, "%d 天（鼓励至 %d）" % (b, b + extra),
                    fontsize=9.2, color=GOLD, weight="bold", ha="left",
                    va="center", zorder=4)
        else:
            ax.text(b + extra + 0.7, y, "%d 天" % (b + extra), fontsize=9.6,
                    color=DARK, weight="bold", ha="left", va="center", zorder=4)
        if note:
            ax.text(32.6, y, note, fontsize=8.4, color=ncol, ha="left",
                    va="center", zorder=4, weight="bold")

    fig.legend(
        handles=[
            Rectangle((0, 0), 1, 1, color=NAVY),
            Rectangle((0, 0), 1, 1, color=GOLD),
            Rectangle((0, 0), 1, 1, facecolor="none", edgecolor=GOLD,
                      linewidth=1.4, linestyle=(0, (3, 2))),
        ],
        labels=["条例规定的天数", "参加婚检后另加", "“鼓励”而非强制"],
        loc="upper right", bbox_to_anchor=(0.972, 0.928), frameon=False,
        fontsize=9, labelcolor=SLATE, handlelength=1.7, handleheight=0.85,
        labelspacing=0.55, borderaxespad=0.0)

    punchline(fig, "深色那一段是条例给的，浅色那一段要先去一趟婚检。")
    footer(fig,
           "事实：山西条例第25条、甘肃2016年修正条例、《黑龙江省人口和计划生育条例》第34条、陕西条例第45条、河南条例及周口市政府2025-09-19答复、新华网2025-11-28、",
           "广西人大常委会2026-09-24公告、宁夏条例第38条、央视网2025-07-18、人民日报海外版2025-11-26、界面新闻2026-08-12｜制图：本文")
    fig.savefig(OUT + "图1_30天到3天.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("“29 个”这个数，是 2025 年 10 月的",
               "同一时点 28 与 29 并存；广西 9 月落地后，按同一口径应为 30 个")
    ax = canvas(fig, bottom=0.150, height=0.690)

    y0 = 0.520
    ax.plot([0.060, 0.945], [y0, y0], color=LIGHT, linewidth=2.2, zorder=2)

    ups = [
        (0.105, "2024.11", "25 个省份", "央视网梳理", SLATE),
        (0.910, "2026.11", "报道仍写 29", "澎湃新闻，11 月 20 日", RED),
    ]
    downs = [
        (0.310, "2025.07", "28 个省份", "央视网梳理", SLATE),
        (0.500, "2025.10", "29 个省份", "界面新闻：截至 10 月底", GOLD),
        (0.735, "2026.09", "广西修法通过", "增加婚假 15 天，自公布起施行", GREEN),
    ]

    for x, date, name, desc, col in ups:
        ax.add_patch(Circle((x, y0), 0.0125, facecolor=col, edgecolor="white",
                            linewidth=2.0, zorder=6))
        ax.text(x, y0 + 0.042, date, fontsize=9.2, color=col, weight="bold",
                ha="center", va="bottom")
        ax.text(x, y0 + 0.078, name, fontsize=11.6, color=DARK, weight="bold",
                ha="center", va="bottom")
        ax.text(x, y0 + 0.122, desc, fontsize=8.2, color=SLATE, ha="center",
                va="bottom")

    for x, date, name, desc, col in downs:
        ax.add_patch(Circle((x, y0), 0.0125, facecolor=col, edgecolor="white",
                            linewidth=2.0, zorder=6))
        ax.text(x, y0 - 0.042, date, fontsize=9.2, color=col, weight="bold",
                ha="center", va="top")
        ax.text(x, y0 - 0.078, name, fontsize=11.6, color=DARK, weight="bold",
                ha="center", va="top")
        ax.text(x, y0 - 0.122, desc, fontsize=8.2, color=SLATE, ha="center",
                va="top")

    # 同一时点的另一个数：28（《法治日报》2025-11-11），挂在 2025.10 节点上方
    ax.plot([0.500, 0.500], [y0 + 0.020, 0.712], color=RED, linewidth=1.2,
            linestyle=(0, (3, 2)), zorder=4)
    ax.add_patch(FancyBboxPatch((0.300, 0.712), 0.400, 0.118,
                                boxstyle="round,pad=0.010", facecolor="#fdf6f5",
                                edgecolor=RED, linewidth=1.1, zorder=5))
    ax.text(0.326, 0.788, "2025.11.11　同一时点的另一个数：28 个",
            fontsize=9.4, color=RED, weight="bold", ha="left", va="center",
            zorder=6)
    ax.text(0.326, 0.746, "《法治日报》不完全统计，并点明“广东、广西仍是 3 天”",
            fontsize=8.4, color="#8a5a52", ha="left", va="center", zorder=6)

    # 底部：广西这一笔怎么算出来的
    ax.add_patch(FancyBboxPatch((0.060, 0.135), 0.885, 0.152,
                                boxstyle="round,pad=0.012", facecolor=SAND,
                                edgecolor="#d9cdb6", linewidth=1.0))
    ax.text(0.086, 0.242, "广西这一笔", fontsize=9.6, color="#8a7a5e",
            weight="bold", ha="left", va="center")
    ax.text(0.086, 0.198,
            "2026-09-24 自治区十四届人大常委会第二十七次会议通过修改决定："
            "“除享受国家规定的婚假以外，增加婚假十五天”，自公布之日起施行。",
            fontsize=8.8, color="#7a6746", ha="left", va="center")
    ax.text(0.086, 0.160,
            "国家 3 天 + 地方 15 天 = 18 天。广东、广西均为 3 天时全国是 29 个，"
            "广西落地后就该是 30 个。",
            fontsize=8.8, color=RED, weight="bold", ha="left", va="center")

    punchline(fig, "数字没更新，不是算错，是没跟着立法走。")
    footer(fig,
           "事实：央视网 2024-11-22（25 个）、2025-07-18（28 个）；《法治日报》2025-11-11（央视网转载，28 个）；界面新闻 2026-08-12（截至 2025 年 10 月底 29 个）；",
           "广西人大网 2026-09-28 公告（十四届第 60 号）；澎湃新闻 2026-11-20（29 个）｜制图：本文")
    fig.savefig(OUT + "图2_29是几月的事.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("30 天不是山西先给的",
               "报道称“山西 2021 年率先、甘肃随后跟进”，实际甘肃早了 5 年 5 个月")
    ax = canvas(fig, bottom=0.150, height=0.690)

    y0 = 0.600
    ax.plot([0.060, 0.945], [y0, y0], color=LIGHT, linewidth=2.2, zorder=2)

    ups = [
        (0.110, "2016.04", "甘肃 30 天", "省十二届人大常委会\n第二十二次会议通过修正", GREEN),
        (0.370, "2021.09", "山西 30 天", "新修订条例第 25 条\n2021-09-29 起执行", NAVY),
        (0.755, "2025.11", "四川 20 天", "婚检 +5，最多 25 天", SLATE),
        (0.912, "2026.09", "广西 18 天", "国家 3 + 地方 15", GOLD),
    ]
    downs = [
        (0.590, "2025.07", "湖北 15 天", "省政府办公厅若干措施", SLATE),
    ]

    for x, date, name, desc, col in ups:
        ax.add_patch(Circle((x, y0), 0.0125, facecolor=col, edgecolor="white",
                            linewidth=2.0, zorder=6))
        ax.text(x, y0 + 0.042, date, fontsize=9.2, color=col, weight="bold",
                ha="center", va="bottom")
        ax.text(x, y0 + 0.078, name, fontsize=12.0, color=DARK, weight="bold",
                ha="center", va="bottom")
        ax.text(x, y0 + 0.122, desc, fontsize=8.2, color=SLATE, ha="center",
                va="bottom", linespacing=1.8)

    for x, date, name, desc, col in downs:
        ax.add_patch(Circle((x, y0), 0.0125, facecolor=col, edgecolor="white",
                            linewidth=2.0, zorder=6))
        ax.text(x, y0 - 0.042, date, fontsize=9.2, color=col, weight="bold",
                ha="center", va="top")
        ax.text(x, y0 - 0.078, name, fontsize=12.0, color=DARK, weight="bold",
                ha="center", va="top")
        ax.text(x, y0 - 0.122, desc, fontsize=8.2, color=SLATE, ha="center",
                va="top", linespacing=1.8)

    # 甘肃 → 山西：5 年 5 个月（走主轴线下方的那条轨道）
    ax.annotate("", xy=(0.372, 0.478), xytext=(0.112, 0.478),
                arrowprops=dict(arrowstyle="<->", color=RED, linewidth=1.5))
    ax.text(0.242, 0.432, "5 年 5 个月", fontsize=11.4, color=RED,
            weight="bold", ha="center", va="top")

    # 底部说明
    ax.add_patch(FancyBboxPatch((0.060, 0.128), 0.885, 0.150,
                                boxstyle="round,pad=0.012", facecolor=SAND,
                                edgecolor="#d9cdb6", linewidth=1.0))
    ax.text(0.086, 0.232, "两句话的差别", fontsize=9.6, color="#8a7a5e",
            weight="bold", ha="left", va="center")
    ax.text(0.086, 0.190,
            "“率先”是一个排序判断，要看条例的通过时间，不是看谁被讨论得多。",
            fontsize=8.8, color="#7a6746", ha="left", va="center")
    ax.text(0.086, 0.155,
            "甘肃 2016 年就定了 30 天，山西 2021 年跟进。报道把这两句的顺序写反了。",
            fontsize=8.8, color=RED, weight="bold", ha="left", va="center")

    punchline(fig, "谁先谁后，条例的通过日期比报道的措辞可靠。")
    footer(fig,
           "事实：甘肃人大网 2016-04-11（2016-04-01 通过）；大同日报 2021-12-14、《山西省人口和计划生育条例》（2021 修订）第 25 条；",
           "澎湃新闻 2025-07-17（湖北）；新华网 2025-11-28（四川）；广西人大网 2026-09-28｜制图：本文")
    fig.savefig(OUT + "图3_甘肃比山西早五年.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)