# -*- coding: utf-8 -*-
"""
《比赛还没开打，赛后报道已经发出来了》配套图表
事实口径：
  · 2026-11-18 晚 19:00，2026-2027 排超 A 级第四轮，
    天津渤海银行客场 3:2 胜上海光明优倍，
    五局比分（上海在前）：30:28、25:27、17:25、25:27、9:15
    —— 国家体育总局官网转《中国体育报》2026-11-19，作者苏畅；
  · 同日 15:31，某体育自媒体发布该场"赛后完整复盘"，
    含五局比分、外援得分（娜塔莉亚 25 分、32 次一传、到位率 84%、零失误）
    与上海队主教练赛后点评，距开赛 3 小时 29 分；
  · 截至 11-19，官方与两俱乐部未发声明，该文未被标注违规或下架。
说明：原始素材的"AI 批量生成""提前虚构内容占比超 60%"经检索无公开信源，
本图不采用；成因解释亦标为存疑。
风格：克制传媒风，白底、低饱和配色、标题即结论。输出目录 = 脚本所在目录。
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch, Circle

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
    fig = base("三个半小时",
               "2026 年 11 月 18 日：报道比比赛先到")
    ax = canvas(fig)

    # 时间轴：15:31 -> 19:00
    y = 0.560
    x0, x1 = 0.115, 0.885
    ax.plot([x0, x1], [y, y], color=LIGHT, linewidth=2.2)

    # 15:31 发稿
    ax.add_patch(Circle((x0, y), 0.020, facecolor=RED, edgecolor="white",
                        linewidth=1.8, zorder=6))
    ax.text(x0, y + 0.062, "15:31", fontsize=17.0, color=RED, weight="bold",
            ha="center", va="bottom")
    ax.text(x0, y - 0.052, "自媒体发布", fontsize=10.6, color=DARK,
            ha="center", va="top")
    ax.text(x0, y - 0.098, "“赛后完整复盘”", fontsize=9.4, color=GRAY,
            ha="center", va="top")

    # 19:00 开赛
    ax.add_patch(Circle((x1, y), 0.020, facecolor=NAVY, edgecolor="white",
                        linewidth=1.8, zorder=6))
    ax.text(x1, y + 0.062, "19:00", fontsize=17.0, color=NAVY, weight="bold",
            ha="center", va="bottom")
    ax.text(x1, y - 0.052, "比赛开球", fontsize=10.6, color=DARK,
            ha="center", va="top")
    ax.text(x1, y - 0.098, "排超 A 级第四轮", fontsize=9.4, color=GRAY,
            ha="center", va="top")

    # 中间跨度
    ax.annotate("", xy=(x1 - 0.022, y + 0.135), xytext=(x0 + 0.022, y + 0.135),
                arrowprops=dict(arrowstyle="<->", color=DARK, linewidth=1.2))
    ax.text((x0 + x1) / 2, y + 0.170, "相隔 3 小时 29 分", fontsize=14.0,
            color=DARK, weight="bold", ha="center", va="bottom")

    # 下方说明：稿子里已经有什么
    ax.add_patch(FancyBboxPatch((0.070, 0.180), 0.860, 0.180,
                                boxstyle="round,pad=0.012", facecolor=SAND,
                                edgecolor="#d9cdb6", linewidth=1.0))
    ax.text(0.095, 0.318, "比赛还没开始，稿子里已经有：", fontsize=10.0,
            color="#8a7a5e", weight="bold", ha="left", va="center")
    items = ["五局比分　28:30 / 27:25 / 17:25 / 27:25 / 15:9（天津在前）",
             "外援数据　娜塔莉亚 25 分、32 次一传、到位率 84%、零失误",
             "赛后点评　上海队主教练对年轻队员的评价"]
    yy = 0.268
    for it in items:
        ax.text(0.095, yy, "·  " + it, fontsize=9.8, color="#7a6746",
                ha="left", va="center")
        yy -= 0.042

    punchline(fig, "报道不是“早了一点”，是早在一件事发生之前。")
    footer(fig, "事实：发布时间据涉事账号原文截图之报道；比赛时间与比分据国家体育总局官网转《中国体育报》2026-11-19｜制图：本文")
    fig.savefig(OUT + "图1_时间线.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("预测和预写的距离",
               "赛前分析能给趋势，给不出这组数字")
    ax = canvas(fig)

    # 左：赛前分析能给出的
    ax.add_patch(FancyBboxPatch((0.060, 0.300), 0.400, 0.500,
                                boxstyle="round,pad=0.012", facecolor="#eaf0ec",
                                edgecolor=GREEN, linewidth=1.2))
    ax.text(0.085, 0.742, "赛前分析能给出", fontsize=12.0, color=GREEN,
            weight="bold", ha="left", va="center")
    ok = ["天津双外援 vs 上海单外援",
          "上海二传、副攻经验占优",
          "上海更依赖一传到位",
          "可能打满五局、天津略占优",
          "关键分谁更可能顶住"]
    yy = 0.672
    for it in ok:
        ax.text(0.085, yy, "·  " + it, fontsize=9.6, color=DARK, ha="left",
                va="center")
        yy -= 0.062
    ax.text(0.085, 0.345, "这是趋势判断", fontsize=9.2, color=GRAY,
            ha="left", va="center")

    # 右：实际要命中的数字
    ax.add_patch(FancyBboxPatch((0.500, 0.300), 0.440, 0.500,
                                boxstyle="round,pad=0.012", facecolor="#f6e4e1",
                                edgecolor=RED, linewidth=1.2))
    ax.text(0.525, 0.742, "要命中的具体数字", fontsize=12.0, color=RED,
            weight="bold", ha="left", va="center")
    no = ["五局全部比分，逐局对上",
          "其中 3 局打到延长分",
          "这 3 局分差都是 2 分",
          "两队总分恰好 114 : 114",
          "娜塔莉亚 25 分、到位率 84%",
          "赛前连教练点评都写好"]
    yy = 0.672
    for it in no:
        ax.text(0.525, yy, "·  " + it, fontsize=9.6, color=DARK, ha="left",
                va="center")
        yy -= 0.055
    ax.text(0.525, 0.330, "这是预写，不是预测", fontsize=9.2, color=RED,
            ha="left", va="center")

    ax.text(0.060, 0.230,
            "说明：左栏据 11 月 18 日 08:30 发布的赛前分析；右栏为赛前 3 小时 29 分那篇稿子已写明的数字。",
            fontsize=8.8, color=GRAY, ha="left", va="center")

    punchline(fig, "分析得出“谁强”，得不出“30 比 28”。")
    footer(fig, "事实：赛前分析据网易号「骑马寺的少年」2026-11-18；比分据国家体育总局官网转《中国体育报》2026-11-19｜制图：本文")
    fig.savefig(OUT + "图2_预测和预写的距离.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("先看时间",
               "看到任何“结果”，第一件事是看发布时间")
    ax = canvas(fig)

    # 三步卡片
    steps = [
        ("1", "看发布时间", "标题下面、正文开头\n或页面顶部的时间戳", NAVY),
        ("2", "对一下时间", "发布时间是否早于\n事情本身发生的时间", GOLD),
        ("3", "再决定信不信", "早于 = 不是结果\n是预测，或者别的", RED),
    ]

    y_top = 0.780
    h = 0.185
    for i, (n, title, desc, color) in enumerate(steps):
        x = 0.070 + i * 0.300
        ax.add_patch(FancyBboxPatch((x, y_top - h), 0.270, h,
                                    boxstyle="round,pad=0.012",
                                    facecolor="#f7f8fa", edgecolor=color,
                                    linewidth=1.2))
        ax.add_patch(Circle((x + 0.040, y_top - 0.045), 0.024, facecolor=color,
                            edgecolor="none", zorder=5))
        ax.text(x + 0.040, y_top - 0.045, n, fontsize=10.6, color="white",
                weight="bold", ha="center", va="center", zorder=6)
        ax.text(x + 0.078, y_top - 0.045, title, fontsize=11.6, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(x + 0.030, y_top - 0.115, desc, fontsize=9.4, color=SLATE,
                ha="left", va="center", linespacing=1.5)
        if i < 2:
            ax.annotate("", xy=(x + 0.298, y_top - h / 2),
                        xytext=(x + 0.274, y_top - h / 2),
                        arrowprops=dict(arrowstyle="-|>", color=GRAY,
                                        linewidth=1.6))

    # 下方：这套判断适用面
    ax.add_patch(FancyBboxPatch((0.070, 0.240), 0.860, 0.210,
                                boxstyle="round,pad=0.012", facecolor=SAND,
                                edgecolor="#d9cdb6", linewidth=1.0))
    ax.text(0.095, 0.400, "不只是体育", fontsize=10.0, color="#8a7a5e",
            weight="bold", ha="left", va="center")
    ax.text(0.095, 0.345,
            "凡是套路固定、有历史模板、结果高度可预期的事，都可能被提前写出来：",
            fontsize=9.8, color="#7a6746", ha="left", va="center")
    ax.text(0.095, 0.292,
            "赛事复盘　财报解读　会议通稿　事故通报",
            fontsize=10.6, color=DARK, weight="bold", ha="left", va="center")

    punchline(fig, "先看时间，再看内容——这一眼只要两秒钟。")
    footer(fig, "说明：本图为通用判断方法，非官方提示｜制图：本文")
    fig.savefig(OUT + "图3_先看时间.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)
