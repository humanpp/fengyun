# -*- coding: utf-8 -*-
"""
《中国车企出海变打法：一边降泰国合规成本，一边在英国先铺 100 个网点》配套图表
事实来源：中泰汽车产业合作谅解备忘录 2026-11-13 曼谷签署（五大领域、有效期 5 年）；
泰国 EV 3.5 本地生产配比 1:2、2027 年收紧至 1:3；
小鹏 2026-11-12/13 英国品牌日（5 款右舵车、约 100 个网点）；
比亚迪英国零售点 5 → 143、累计销量破 10 万辆
风格：克制传媒风，白底、低饱和配色、标题即结论
输出目录 = 脚本所在目录
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

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
    fig.text(0.045, 0.072, text, fontsize=10.4, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


# ---------------------------------------------------------------- 图 1
def fig1():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.175, 0.930, 0.640])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "泰国设的是配比，不是税率", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.882, "EV 3.5 方案：每进口 1 辆，必须本地生产对应台数",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    unit = 0.120  # 一辆对应的宽度
    x0 = 0.175

    rows = [
        ("2026 年", "现行", 2, "1 : 2", 0.640),
        ("2027 年起", "收紧", 3, "1 : 3", 0.360),
    ]

    for label, sub, n_local, ratio, y in rows:
        ax.text(0.012, y + 0.055, label, fontsize=14, color=DARK, weight="bold",
                va="center")
        ax.text(0.012, y - 0.020, sub, fontsize=10, color=GRAY, va="center")

        # 进口 1 辆
        ax.add_patch(Rectangle((x0, y - 0.055), unit, 0.145, facecolor=NAVY,
                               edgecolor="none"))
        ax.text(x0 + unit / 2, y + 0.018, "1", fontsize=16, color="white",
                weight="bold", ha="center", va="center")
        ax.text(x0 + unit / 2, y - 0.098, "进口", fontsize=9.6, color=NAVY,
                ha="center", va="top")

        # 本地生产 N 辆
        lx = x0 + unit + 0.040
        for i in range(n_local):
            bx = lx + i * (unit + 0.010)
            ax.add_patch(Rectangle((bx, y - 0.055), unit, 0.145, facecolor=RED,
                                   edgecolor="none", alpha=0.88))
            ax.text(bx + unit / 2, y + 0.018, "1", fontsize=16, color="white",
                    weight="bold", ha="center", va="center")
        ax.text(lx + (n_local * (unit + 0.010) - 0.010) / 2, y - 0.098,
                f"本地生产 {n_local} 辆", fontsize=9.6, color=RED,
                ha="center", va="top")

        # 比例标签
        ax.text(0.935, y + 0.018, ratio, fontsize=20, color=DARK, weight="bold",
                ha="right", va="center")
        ax.text(0.935, y - 0.030, "进口 : 本地", fontsize=9.4, color=GRAY,
                ha="right", va="center")

    # 收紧箭头
    ax.add_patch(FancyArrowPatch((0.905, 0.520), (0.905, 0.455),
                                 arrowstyle="-|>", mutation_scale=18,
                                 color=RED, linewidth=1.8))
    ax.text(0.892, 0.488, "本地义务 +50%", fontsize=9.8, color=RED,
            ha="right", va="center", weight="bold")

    punchline(fig, "合规成本可以谈，配额不能谈——省下来的钱仍要投进产能。")
    footer(fig, "据泰国 EV 3.5 方案（每进口 1 辆对应本地生产 2 辆、2027 年收紧至 3 辆），见 Gasgoo、Automotive World 报道。")
    fig.savefig(OUT + "图1_泰国配比.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.200, 0.930, 0.560])

    fig.text(0.045, 0.955, "英国：渠道数量先涨，份额随后", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.882, "单位：家。横轴同尺度，可直接比较绝对数量",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    rows = [
        ("中国品牌在英经销商", 95, "2024 年 5 月", 440, "2026 年 5 月", "×4.6", NAVY, 1.42),
        ("比亚迪英国零售网点", 5, "2023 年进入时", 143, "2026 年 7 月", "×28.6", RED, 0.48),
    ]

    ax.set_xlim(-20, 500)
    ax.set_ylim(0, 2.0)
    ax.set_yticks([])
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(LIGHT)
    ax.set_xticks([0, 100, 200, 300, 400, 500])
    ax.tick_params(axis="x", colors=DARK, labelsize=10.5, length=0, pad=8)
    ax.grid(axis="x", color=LIGHT, linewidth=0.8, alpha=0.5)
    ax.set_axisbelow(True)

    for name, v0, t0, v1, t1, mult, color, y in rows:
        ax.plot([v0, v1], [y, y], color=color, linewidth=3.0, alpha=0.35,
                solid_capstyle="round", zorder=2)
        ax.scatter([v0], [y], s=150, facecolor="white", edgecolor=color,
                   linewidth=2.2, zorder=4)
        ax.scatter([v1], [y], s=170, facecolor=color, edgecolor="white",
                   linewidth=2.0, zorder=5)

        ax.text(-8, y + 0.24, name, fontsize=12, color=DARK, weight="bold",
                ha="left", va="center")
        ax.text(v0, y - 0.20, f"{v0}　{t0}", fontsize=10.5, color=GRAY,
                ha="left", va="top")
        ax.text(v1 + 10, y + 0.02, f"{v1} 家（{mult}）", fontsize=13, color=color,
                weight="bold", ha="left", va="center")
        ax.text(v1, y - 0.20, t1, fontsize=10.5, color=GRAY, ha="right",
                va="top")

    ax.text(150, 0.95,
             "同期中国品牌占英国新车注册：\n2026 年上半年 15%，7 月接近五分之一",
             fontsize=10.4, color=DARK, ha="left", va="center", linespacing=1.7,
             bbox=dict(boxstyle="round,pad=0.55", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))

    punchline(fig, "小鹏要铺的 100 个网点，是追上队伍，不是拉开距离。")
    footer(fig, "据 Car Dealer Magazine、Autocar、《每日电讯报》援引 AutoTrader 数据、Fleet News。")
    fig.savefig(OUT + "图2_英国渠道.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.140, 0.930, 0.690])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "两条路：规则适配 vs 渠道前置", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.882, "都是「先付钱、后卖车」，但付的地方不一样",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    ax.text(0.235, 0.790, "泰国：先付产能", fontsize=11.8, color=NAVY,
            weight="bold", ha="center")
    ax.text(0.740, 0.790, "英国：先付门店", fontsize=11.8, color=RED,
            weight="bold", ha="center")
    ax.plot([0.010, 0.990], [0.752, 0.752], color=LIGHT, linewidth=1.2)

    rows = [
        ("主要动作", "标准与法规对接、本地化生产", "右舵车型导入、零售服务网络"),
        ("先付的钱", "厂房、产能、认证", "门店、备件、右舵化开发"),
        ("硬约束", "EV 3.5 配比 1:2，2027 年 1:3", "无配额，卡在服务半径与信任"),
        ("见效节奏", "慢，但上限清楚", "快，风险自担"),
        ("代表玩家", "比亚迪：罗勇三年近 10 万辆", "小鹏：2027 年约 100 个网点"),
    ]

    for i, (label, left, right) in enumerate(rows):
        y = 0.660 - i * 0.128
        if i % 2 == 0:
            ax.add_patch(Rectangle((0.010, y - 0.050), 0.980, 0.106,
                                   facecolor=PALE, edgecolor="none"))
        ax.text(0.022, y, label, fontsize=10.6, color=GRAY, va="center")
        ax.text(0.235, y, left, fontsize=11.2, color=DARK, va="center", ha="center")
        ax.text(0.485, y, "｜", fontsize=12, color=LIGHT, va="center", ha="center")
        ax.text(0.740, y, right, fontsize=11.2, color=DARK, va="center", ha="center")

    ax.text(0.010, 0.028, "过去是整车出口、找总代、比价格；现在是先把规则和门店办完。",
            fontsize=10.8, color=DARK, ha="left", va="center")

    footer(fig, "据中泰备忘录、泰国 EV 3.5 方案、小鹏英国品牌日公布内容与比亚迪英国渠道数据整理。")
    fig.savefig(OUT + "图3_两条路.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")