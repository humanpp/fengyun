# -*- coding: utf-8 -*-
"""
《猪肉比青菜便宜，这笔账记在谁头上》配套图表
事实来源：第一财经 2026-11-09；国家统计局 10 月 CPI 与前三季度生猪数据；
中国商报/新浪财经猪企三季报统计；红星资本局、澎湃新闻 11-15 零售端走访
风格：克制传媒风，白底、低饱和配色、标题即结论
输出目录 = 脚本所在目录
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["figure.facecolor"] = "white"
plt.rcParams["axes.facecolor"] = "white"

NAVY = "#1f3a5f"
RED = "#b5544a"
GRAY = "#8a8f98"
LIGHT = "#d8dbe0"
DARK = "#2b2f36"
PALE = "#eef0f3"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep


def footer(fig, text):
    fig.text(0.045, 0.020, text, fontsize=8.4, color=GRAY, ha="left", va="bottom")


def takeaway(fig, y, text, size=10.4):
    fig.text(0.045, y, text, fontsize=size, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


# ---------------------------------------------------------------- 图 1
def fig1():
    fig, ax = plt.subplots(figsize=(12, 6.8))
    fig.subplots_adjust(left=0.235, right=0.945, top=0.745, bottom=0.215)

    fig.suptitle("按斤折算，菜已经比肉贵",
                 fontsize=19, color=DARK, x=0.045, ha="left", y=0.955, weight="bold")
    fig.text(0.045, 0.878,
             "11 月 15 日前后线上平台零售价，统一折算为元/斤",
             fontsize=10.8, color=GRAY, ha="left")

    items = [
        ("油麦菜 / 辣椒（部分产品）", 19.8, "9.9 元 / 半斤", RED),
        ("永辉·鲜猪五花肉", 10.9, "—", NAVY),
        ("大润发·带皮猪前腿肉", 9.95, "19.9 元 / 1000g", NAVY),
    ]

    y = range(len(items))
    for i, (name, price, note, color) in enumerate(items):
        ax.barh(i, price, height=0.52, color=color, alpha=0.92)
        ax.text(price + 0.30, i, f"{price:g} 元/斤", va="center",
                fontsize=13, color=color, weight="bold")
        if note != "—":
            ax.text(price + 3.5, i, note, va="center", fontsize=9.4, color=GRAY)

    ax.set_yticks(list(y))
    ax.set_yticklabels([it[0] for it in items], fontsize=11)
    ax.set_xlim(0, 26)
    ax.set_ylim(-0.65, 2.65)
    ax.invert_yaxis()
    ax.set_xlabel("元 / 斤", fontsize=10, color=GRAY, labelpad=6)

    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(LIGHT)
    ax.tick_params(colors=DARK, length=0)
    ax.set_axisbelow(True)
    ax.grid(axis="x", color=LIGHT, linewidth=0.8, alpha=0.55)

    takeaway(fig, 0.078, "同一张购物车里，蔬菜的单价接近猪肉的两倍。")

    footer(fig, "数据：红星资本局、澎湃新闻 2026-11-15 零售端走访；半斤价按 ×2 折算为斤价。")
    fig.savefig(OUT + "图1_菜比肉贵.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig, ax = plt.subplots(figsize=(12, 6.8))
    fig.subplots_adjust(left=0.045, right=0.955, top=0.755, bottom=0.175)

    fig.suptitle("同一个跌幅，两种读法",
                 fontsize=19, color=DARK, x=0.045, ha="left", y=0.955, weight="bold")
    fig.text(0.045, 0.880,
             "猪肉同比 -8.6%，在统计局是“物价温和”，在行业是“卖一斤亏一斤”",
             fontsize=10.6, color=GRAY, ha="left")

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 4.60)
    ax.axis("off")

    panels = [
        (0.030, "统计局的读法", GRAY, [
            ("猪肉同比", "-8.6%"),
            ("连同鲜菜 -16.9%、鲜果 -3.8%", "拖累 CPI 约 0.54 个百分点"),
            ("10 月 CPI 同比", "+0.7%（涨幅回落 0.2pct）"),
            ("结论", "食品是主要拖累，物价温和"),
        ]),
        (0.530, "行业的读法", RED, [
            ("25 家 A 股猪企前三季", "合计亏损 244.73 亿元"),
            ("牧原 9 月销售均价", "10.36 元/公斤"),
            ("牧原完全成本", "约 11.5 元/公斤"),
            ("结论", "卖一斤亏一斤，现金流亏超 9 个月"),
        ]),
    ]

    for x0, title, color, rows in panels:
        ax.add_patch(plt.Rectangle((x0, 0.68), 0.440, 3.46,
                                   facecolor=PALE, edgecolor=LIGHT, linewidth=1.0))
        ax.add_patch(plt.Rectangle((x0, 4.02), 0.440, 0.14,
                                   facecolor=color, edgecolor="none"))
        ax.text(x0 + 0.028, 3.70, title, fontsize=12.5, color=color,
                weight="bold", va="center")
        for i, (k, v) in enumerate(rows):
            y = 3.22 - i * 0.70
            ax.text(x0 + 0.028, y, k, fontsize=9.6, color=GRAY, va="center")
            ax.text(x0 + 0.028, y - 0.28, v, fontsize=10.6, color=DARK,
                    va="center", weight="bold")

    takeaway(fig, 0.080, "对宏观是好事，对报表是灾难——同一笔降价，两种记账方式。")

    footer(fig, "数据：国家统计局 2026 年 10 月 CPI；25 家 A 股猪企 2026 年三季报；牧原股份 9 月销售简报。")
    fig.savefig(OUT + "图2_两种读法.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig, ax = plt.subplots(figsize=(12, 6.8))
    fig.subplots_adjust(left=0.045, right=0.955, top=0.755, bottom=0.175)

    fig.suptitle("便宜是三股力量一起压出来的",
                 fontsize=19, color=DARK, x=0.045, ha="left", y=0.955, weight="bold")
    fig.text(0.045, 0.880,
             "供给还在增，需求没起来，冷库里还压着货",
             fontsize=10.8, color=GRAY, ha="left")

    ax.set_xlim(0, 1)
    ax.set_ylim(0.28, 4.80)
    ax.axis("off")

    forces = [
        ("供给：还在增", NAVY, [
            "前三季度出栏 5.37 亿头，同比 +1.4%",
            "猪肉产量 4508 万吨，同比 +3.2%",
        ]),
        ("需求：没转强", GRAY, [
            "四季度传统旺季未带来回暖",
            "消费端未见季节性转强",
        ]),
        ("库存：压着反弹", RED, [
            "冻品库容率 31.9%—32.2%",
            "同比高约 14 个百分点",
        ]),
    ]

    for i, (title, color, lines) in enumerate(forces):
        y = 4.05 - i * 1.26
        ax.add_patch(plt.Rectangle((0.030, y - 0.56), 0.940, 1.12,
                                   facecolor=PALE, edgecolor=color, linewidth=1.4))
        ax.add_patch(plt.Rectangle((0.030, y - 0.56), 0.008, 1.12,
                                   facecolor=color, edgecolor="none"))
        ax.text(0.062, y + 0.27, title, fontsize=13, color=color,
                weight="bold", va="center")
        ax.text(0.062, y - 0.07, lines[0], fontsize=10.2, color=DARK, va="center")
        ax.text(0.062, y - 0.36, lines[1], fontsize=9.6, color=GRAY, va="center")

    # 底部结论条
    ax.add_patch(plt.Rectangle((0.185, 0.38), 0.630, 0.50,
                               facecolor="white", edgecolor=RED, linewidth=1.4))
    ax.text(0.500, 0.63, "三股力量同向  →  价格往下压", fontsize=12,
            color=RED, ha="center", va="center", weight="bold")

    fig.text(0.045, 0.100,
             "便宜不是偶然，是三股力量同时朝一个方向推的结果。",
             fontsize=10.4, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))

    footer(fig, "数据：国家统计局前三季度生猪数据；农业农村部 11 月第 1 周监测；行业冻品库容率监测。")
    fig.savefig(OUT + "图3_三股力量.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")