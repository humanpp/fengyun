# -*- coding: utf-8 -*-
"""
《加拿大突然放话：可能转向中国车企？北美汽车供应链出现裂缝》配套图表
事实来源：卡尼 2026-11-16 金边表态（美联社、卫报、路透社）；
2026-01-16《中加经贸问题初步联合安排》（加拿大总理府）；
2026-08-24 美方 50% 关税宣布（路透社、POLITICO）；安省三厂公告
风格：克制传媒风，白底、低饱和配色、标题即结论
输出目录 = 脚本所在目录
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["figure.facecolor"] = "white"
plt.rcParams["axes.facecolor"] = "white"

NAVY = "#1f3a5f"
RED = "#b5544a"
GRAY = "#8a8f98"
SLATE = "#5f6673"
LIGHT = "#d8dbe0"
DARK = "#2b2f36"
PALE = "#eef0f3"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep


def footer(fig, text):
    fig.text(0.045, 0.020, text, fontsize=8.4, color=GRAY, ha="left", va="bottom")


def punchline(fig, text):
    fig.text(0.045, 0.075, text, fontsize=10.4, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


# ---------------------------------------------------------------- 图 1
def fig1():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.135, 0.930, 0.680])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "一条链上的四个结点", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.882, "2026 年，北美汽车供应链从“降税”走到“放话”",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    nodes = [
        (0.130, "1 月 16 日", "中加降税", NAVY,
         "中国电动车关税\n100% → 6.1%\n配额 4.9 万辆/年起"),
        (0.378, "8 月 24 日", "美方翻倍", RED,
         "谈判破裂，整车与\n零部件关税 → 50%\n（2027 年 1 月 1 日起）"),
        (0.626, "11 月 9—13 日", "安省三厂", SLATE,
         "布兰普顿厂卖给 Roshel\n奥克维尔复产\n阿利斯顿加投 8.67 亿加元"),
        (0.874, "11 月 16 日", "转向放话", NAVY,
         "谈不拢就找中国、\n欧洲、日本车企\n门槛：超出组装环节"),
    ]

    ax.plot([0.050, 0.955], [0.740, 0.740], color=LIGHT, linewidth=2.6,
            solid_capstyle="round", zorder=1)

    bw, bh, by = 0.218, 0.240, 0.185
    for x, date, title, color, body in nodes:
        ax.scatter([x], [0.740], s=200, facecolor=color, edgecolor="white",
                   linewidth=2.2, zorder=3)
        ax.text(x, 0.862, title, fontsize=13.5, color=color, weight="bold",
                ha="center", va="center")
        ax.text(x, 0.800, date, fontsize=10.6, color=DARK, ha="center", va="center")

        ax.plot([x, x], [0.700, by + bh], color=LIGHT, linewidth=1.4, zorder=1)
        ax.add_patch(Rectangle((x - bw / 2, by), bw, bh, facecolor=PALE,
                               edgecolor=LIGHT, linewidth=1.0, zorder=2))
        ax.add_patch(Rectangle((x - bw / 2, by + bh - 0.013), bw, 0.013,
                               facecolor=color, edgecolor="none", zorder=3))
        ax.text(x, by + bh - 0.040, body, fontsize=9.5, color=DARK,
                ha="center", va="top", linespacing=1.75, zorder=4)

    punchline(fig, "同一张网上，有的结点在加固，有的在被剪断。")
    footer(fig, "据美联社、《卫报》、路透社、加拿大总理府新闻稿、Stellantis 与本田公告整理。")
    fig.savefig(OUT + "图1_四个结点.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig, axes = plt.subplots(1, 2, figsize=(12, 6.8))
    fig.subplots_adjust(left=0.055, right=0.975, top=0.700, bottom=0.205, wspace=0.20)

    fig.text(0.045, 0.955, "两个方向的税：进来的开得很小，出去的在关上",
             fontsize=18, color=DARK, weight="bold", ha="left", va="top")
    fig.text(0.045, 0.888, "同一张北美地图，两套税率奔着相反的方向",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    panels = [
        (axes[0], "进来：中国电动车 → 加拿大",
         [("2024 年 10 月起", 100.0, LIGHT, DARK, "100%"),
          ("现行（2026 年 1 月起）", 6.1, NAVY, NAVY, "6.1%")],
         "↓ 降 94 个百分点", NAVY,
         "配额起步 4.9 万辆/年\n≈ 加拿大年销 190 万辆的 2.6%"),
        (axes[1], "出去：加拿大整车 → 美国",
         [("现行", 25.0, LIGHT, DARK, "25%"),
          ("2027 年 1 月 1 日起", 50.0, RED, RED, "50%")],
         "↑ 翻倍", RED,
         "在加拿大造的车\n基本只能卖给加拿大自己"),
    ]

    for ax, title, rows, tag, tagcolor, note in panels:
        ax.set_xlim(0, 116)
        ax.set_ylim(-0.42, 2.30)
        ax.set_yticks([])
        for s in ("top", "right", "left"):
            ax.spines[s].set_visible(False)
        ax.spines["bottom"].set_color(LIGHT)
        ax.tick_params(axis="x", colors=DARK, labelsize=10.5, length=0, pad=8)
        ax.set_xticks([0, 25, 50, 75, 100])
        ax.set_xticklabels(["0", "25%", "50%", "75%", "100%"])
        ax.grid(axis="x", color=LIGHT, linewidth=0.8, alpha=0.55)
        ax.set_axisbelow(True)

        ax.set_title(title, fontsize=13, color=DARK, weight="bold",
                     loc="left", pad=16)

        for y, (label, val, color, tcolor, txt) in zip([1.62, 0.72], rows):
            ax.barh([y], [val], height=0.40, color=color, edgecolor="none")
            ax.text(1.0, y + 0.285, label, fontsize=9.8, color=GRAY,
                    ha="left", va="bottom")
            ax.text(val + 2.2, y, txt, fontsize=14, color=tcolor,
                    ha="left", va="center", weight="bold")

        ax.text(64, 1.17, tag, fontsize=11.5, color=tagcolor, weight="bold",
                ha="center", va="center",
                bbox=dict(boxstyle="round,pad=0.45", facecolor="white",
                          edgecolor=tagcolor, linewidth=1.2))

        ax.text(1.0, -0.075, note, fontsize=9.4, color=DARK, ha="left", va="top",
                linespacing=1.65)

    punchline(fig, "6.1% 那扇门后面站着配额；50% 那堵墙后面站着 2027 年。")
    footer(fig, "税率据加拿大总理府 2026-01-16 联合安排、路透社与 POLITICO 2026-08-24 报道；年销 190 万辆据 TD Economics。")
    fig.savefig(OUT + "图2_两个方向的税.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.150, 0.930, 0.680])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "卡尼给中国投资开的三道闸门", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.882, "“这不只是关于组装车。必须要有制造环节。”",
             fontsize=11.2, color=GRAY, ha="left", va="top")

    cards = [
        ("01", "制造环节", "投资必须有实质性制造，不只是\n进口成套零部件、在本地做简单\n组装。", NAVY, "组装不算"),
        ("02", "劳工标准", "要符合适当的劳工标准，不能靠\n压低的用工成本，换取落地资格。", NAVY, "低薪不算"),
        ("03", "本地供应链", "供应链要随时间成长，电动车里\n要用上加拿大的关键矿产。", RED, "只买矿不算"),
    ]

    cw, gap = 0.286, 0.031
    for i, (no, name, body, color, tag) in enumerate(cards):
        x0 = 0.010 + i * (cw + gap)
        ax.add_patch(Rectangle((x0, 0.285), cw, 0.585, facecolor=PALE,
                               edgecolor=LIGHT, linewidth=1.0))
        ax.add_patch(Rectangle((x0, 0.857), cw, 0.013, facecolor=color, edgecolor="none"))

        ax.text(x0 + 0.024, 0.800, no, fontsize=12, color=GRAY, va="center")
        ax.text(x0 + 0.068, 0.800, name, fontsize=15, color=DARK,
                weight="bold", va="center")
        ax.plot([x0 + 0.024, x0 + cw - 0.024], [0.745, 0.745],
                color=LIGHT, linewidth=1.0)
        ax.text(x0 + 0.024, 0.690, body, fontsize=10.5, color=DARK,
                ha="left", va="top", linespacing=2.05)

        ax.text(x0 + cw / 2, 0.330, tag, fontsize=11.5, color=color,
                weight="bold", ha="center", va="center",
                bbox=dict(boxstyle="round,pad=0.45", facecolor="white",
                          edgecolor=color, linewidth=1.2))

    ax.text(0.010, 0.130, "门槛设在制造，不在出口。谁能把工厂搬过来，谁才进得了门。",
            fontsize=10.8, color=DARK, ha="left", va="center")

    footer(fig, "原话与三项条件据卡尼 2026-11-16 在金边法语国家峰会期间答记者问（美联社、《卫报》报道）。")
    fig.savefig(OUT + "图3_三道闸门.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")
