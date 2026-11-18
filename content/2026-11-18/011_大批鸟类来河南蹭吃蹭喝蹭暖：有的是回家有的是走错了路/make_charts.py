# -*- coding: utf-8 -*-
"""
《大批鸟类来河南「蹭吃蹭喝蹭暖」：有的是回家，有的是走错了路》配套图表
事实口径（均已核对原始报道）：
  · 2026-11-17 大河网报道（记者刘瑞朝）：河南进入候鸟越冬季，大批候鸟返回，
    亦有部分「迷鸟」飞到河南，在河道沙洲之间觅食栖息。
  · 灵宝市银水湖：林业局日常巡护监测记录到黑鹳 20 余只，为灵宝市湿地范围内
    监测到的最大黑鹳种群，刷新当地观测纪录（此前金水湖仅零星数只）。
    黑鹳为国家一级重点保护野生动物，有「鸟中大熊猫」之称，是生态环境指示物种。
  · 郑州黄河湿地保护区中牟区域：11 月 12 日中午，郑州师范学院教授、鸟类专家
    李长看观测到一只混在银鸥群里的北极鸥，属迷鸟；该记录刷新河南鸟类纪录
    （央广网 2026-11-16）。是否留下越冬尚需进一步监测。
  · 驻马店汝南宿鸭湖湿地省级自然保护区：鸟类摄影爱好者拍到红胸黑雁与黑颈䴙䴘，
    两种均为国家二级保护野生动物；红胸黑雁在国内属罕见迷鸟。
  · 濮阳县黄河湿地省级自然保护区：上千只野鸭成群集结，形成「鸭浪」，
    以斑嘴鸭、绿头鸭、针尾鸭等雁形目鸭科水鸟为主；大鸨、白鹤等将接踵而至。
  · 河南位于东亚—澳大利西亚候鸟迁徙路线，是候鸟迁徙途中的停歇地与栖息地。
  · 黑鹳种群数据：据「湿地国际」统计，全球黑鹳种群约 24000—44000 只，
    中国约 1000 只左右（国家林草局、张掖黑河湿地保护区管理局等多方引用）。
  · 河南越冬水鸟：2026 年度全国越冬水鸟同步监测河南区域调查共记录水鸟 157 种、
    38.18 万只，较 2025 年同期分别增长 13% 和 6.8%；覆盖全省 18 个省辖市、
    设 122 个观测分区，197 人参与（国家林草局政府网 2026-01-23）。
    该调查为上一越冬季（2025—2026 年度）结果，非本季数据。
  · 河南湿地不足国土面积 5%，却生存着全省 68.9% 的脊椎动物；
    河南境内黄河湿地面积 14.24 万公顷，占全省湿地面积 22.67%。
  · 迷鸟 / 留鸟 / 候鸟定义据大河网原文：留鸟为一年四季都在当地生活的鸟类；
    候鸟为作规律性迁徙活动的鸟类；迷鸟为迁徙途中迷失道路的鸟类。
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
GREEN = "#4f6b58"

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
    fig = base("这个冬天，河南湿地来了谁",
               "同一条迁徙通道上，四个地方，四种消息")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    cells = [
        (0.045, 0.545, "灵宝 · 银水湖", "黑鹳 20 余只", GREEN,
         "国家一级保护，刷新当地纪录\n此前金水湖只零星见过几只"),
        (0.515, 0.545, "郑州 · 黄河湿地中牟", "北极鸥 1 只", RED,
         "迷鸟。混在银鸥群里被发现\n刷新河南鸟类纪录"),
        (0.045, 0.180, "驻马店 · 宿鸭湖", "红胸黑雁 · 黑颈䴙䴘", NAVY,
         "都是国家二级保护\n红胸黑雁在国内属罕见迷鸟"),
        (0.515, 0.180, "濮阳 · 黄河湿地", "上千只野鸭「鸭浪」", NAVY,
         "斑嘴鸭、绿头鸭、针尾鸭成群\n大鸨、白鹤将接踵而至"),
    ]

    for x, y, place, headline, color, body in cells:
        ax.add_patch(Rectangle((x, y), 0.440, 0.345, facecolor="white",
                               edgecolor=color, linewidth=1.1, zorder=2))
        ax.text(x + 0.022, y + 0.296, place, fontsize=9.4, color=GRAY,
                ha="left", va="center", zorder=3)
        ax.text(x + 0.022, y + 0.238, headline, fontsize=12.6, color=color,
                weight="bold", ha="left", va="center", zorder=3)
        ax.plot([x + 0.022, x + 0.418], [y + 0.192, y + 0.192], color=LIGHT,
                linewidth=0.9, zorder=3)
        ax.text(x + 0.022, y + 0.110, body, fontsize=8.7, color=SLATE,
                ha="left", va="center", linespacing=1.85, zorder=3)

    punchline(fig, "四个地方，三种是「回来了」，一种可能是「走错了」。")
    footer(fig, "依据：大河网（2026-11-17，记者刘瑞朝）、央广网（2026-11-16）｜制图：本文")
    fig.savefig(OUT + "图1_这个冬天河南湿地来了谁.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("留鸟、候鸟、迷鸟：三种身份，三套判据",
               "「来的鸟多」和「生态变好」之间，隔着一个分类问题")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    rows = [
        ("留鸟", "一年四季都在当地生活",
         "青头潜鸭：民权湿地 2017 年 4 只\n到 400 多只，部分已转为留鸟", GREEN),
        ("候鸟", "作规律性迁徙活动",
         "燕子在原地区春来秋去\n鸿雁则秋来春去", NAVY),
        ("迷鸟", "迁徙途中迷失了道路",
         "北极鸥在南迁时混进银鸥群\n一路偏航到郑州黄河湿地", RED),
    ]

    yy = 0.800
    for name, definition, example, color in rows:
        ax.add_patch(Rectangle((0.045, yy - 0.100), 0.910, 0.185,
                               facecolor="white", edgecolor=color,
                               linewidth=1.1, zorder=2))
        ax.text(0.070, yy + 0.024, name, fontsize=13.6, color=color,
                weight="bold", ha="left", va="center", zorder=3)
        ax.text(0.070, yy - 0.048, definition, fontsize=9.6, color=SLATE,
                ha="left", va="center", zorder=3)
        ax.plot([0.360, 0.360], [yy - 0.088, yy + 0.066], color=LIGHT,
                linewidth=0.9, zorder=3)
        ax.text(0.395, yy - 0.012, example, fontsize=9.2, color=DARK,
                ha="left", va="center", linespacing=1.85, zorder=3)
        yy -= 0.235

    punchline(fig, "迷鸟证明的是「导航出错」，不是「环境变好」。")
    footer(fig, "分类定义据大河网原文；青头潜鸭数据据新华网（2026-07-23）｜制图：本文")
    fig.savefig(OUT + "图2_留鸟候鸟迷鸟.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("数字在这一边：河南的鸟，确实在变多",
               "但要说准是哪一类在变多")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # 左：越冬水鸟（种与只量纲不同，分列两张数值卡，不做同轴柱状图）
    ax.text(0.060, 0.845, "越冬水鸟同步监测（河南）", fontsize=11.0, color=DARK,
            weight="bold", ha="left", va="center")
    ax.text(0.060, 0.795, "上一越冬季，全省 18 市、122 个观测分区、197 人参与",
            fontsize=8.6, color=GRAY, ha="left", va="center")

    cards = [
        (0.520, "157 种", "+13%", "记录到的水鸟种类"),
        (0.305, "38.18 万只", "+6.8%", "记录到的水鸟数量"),
    ]
    for y, big, delta, note in cards:
        ax.add_patch(Rectangle((0.060, y), 0.395, 0.165, facecolor="white",
                               edgecolor=LIGHT, linewidth=1.0, zorder=2))
        ax.text(0.082, y + 0.108, big, fontsize=15.0, color=NAVY,
                weight="bold", ha="left", va="center", zorder=3)
        ax.text(0.082, y + 0.050, note, fontsize=8.6, color=SLATE, ha="left",
                va="center", zorder=3)
        ax.add_patch(FancyBboxPatch((0.300, y + 0.088), 0.128, 0.052,
                                    boxstyle="round,pad=0.006",
                                    facecolor="#f2e4e1", edgecolor="none",
                                    zorder=3))
        ax.text(0.364, y + 0.114, delta, fontsize=9.4, color=RED,
                weight="bold", ha="center", va="center", zorder=4)

    ax.text(0.060, 0.262, "两项均为较上年同期", fontsize=8.2, color=GRAY,
            ha="left", va="center")

    ax.plot([0.500, 0.500], [0.180, 0.845], color=LIGHT, linewidth=1.0,
            linestyle=(0, (4, 4)))

    # 右：黑鹳的稀有程度
    ax.text(0.540, 0.845, "黑鹳到底有多稀有", fontsize=11.0, color=DARK,
            weight="bold", ha="left", va="center")
    ax.text(0.540, 0.795, "全球、中国、灵宝三个量级", fontsize=8.6,
            color=GRAY, ha="left", va="center")

    facts = [
        ("24000—44000 只", "全球黑鹳种群（湿地国际统计）", NAVY),
        ("约 1000 只", "中国黑鹳总数", RED),
        ("20 余只", "灵宝银水湖一次监测到的数量", GREEN),
    ]
    yy = 0.700
    for big, note, color in facts:
        ax.text(0.540, yy, big, fontsize=13.0, color=color, weight="bold",
                ha="left", va="center")
        ax.text(0.540, yy - 0.052, note, fontsize=8.6, color=SLATE,
                ha="left", va="center")
        yy -= 0.150

    ax.add_patch(FancyBboxPatch((0.540, 0.215), 0.415, 0.088,
                                boxstyle="round,pad=0.010", facecolor=SAND,
                                edgecolor="#d9cdb6", linewidth=1.0, zorder=2))
    ax.text(0.558, 0.278, "20 余只，约占中国已知总数的 2%", fontsize=8.8,
            color="#7a6746", ha="left", va="center", zorder=3)
    ax.text(0.558, 0.240, "所以「刷新当地纪录」不是客套", fontsize=8.8,
            color="#7a6746", ha="left", va="center", zorder=3)

    punchline(fig, "湿地不足国土 5%，养着全省 68.9% 的脊椎动物。")
    footer(fig, "数据：国家林草局（2026-01-23）、大河网（2026-11-17）、湿地国际统计口径；水鸟调查为上一越冬季结果｜制图：本文")
    fig.savefig(OUT + "图3_数字在这一边.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)