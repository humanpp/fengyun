# -*- coding: utf-8 -*-
"""
《硬件成本降 70%，千台级 Robotaxi 要进北上广深：自动驾驶开始算经济账了》配套图表
事实口径：2026 年 11 月 16 日，小马智行与丰田合作研发并量产的第七代铂智 4X
Robotaxi 在广州正式投入示范运营，面向公众开放 L4 级自动驾驶服务，用户通过小马
智行 App 或小程序呼叫；硬件套件总成本较前代下降约 70%，核心零部件车规级并构建
多重安全冗余；三方合资公司计划 2026 年部署千台级铂智 4X Robotaxi，在北上广深
四城运营，运营维保依托丰田经销商网络与小马智行城市级运营经验分工。合作追溯至
2019 年；2023 年 8 月合资公司投资 10 亿元；2026 年 2 月首台量产版在广汽丰田
生产线下线。
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
    fig.text(0.045, 0.072, text, fontsize=10.4, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


# ---------------------------------------------------------------- 图 1
def fig1():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.135, 0.910, 0.690])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "七年，从合作到开跑", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.888, "小马智行与丰田：2019 年到 2026 年 11 月",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    y_line = 0.500
    ax.plot([0.070, 0.930], [y_line, y_line], color=LIGHT, linewidth=2.4,
            solid_capstyle="round", zorder=1)

    nodes = [
        (0.085, "2019", "合作起点", "双方开始\n技术合作", SLATE, True),
        (0.295, "2023.8", "合资落地", "三方合资公司\n投资 10 亿元", SLATE, False),
        (0.500, "2026.2", "首台下线", "量产版在广汽丰田\n生产线下线", NAVY, True),
        (0.705, "11.16", "广州开跑", "第七代铂智 4X\n面向公众运营", RED, False),
        (0.915, "2026 内", "千台级", "计划千台级\n北上广深四城", RED, True),
    ]

    for x, date, title, body, color, above in nodes:
        ax.scatter([x], [y_line], s=260, facecolor=color, edgecolor="white",
                   linewidth=2.0, zorder=3)
        if above:
            ax.text(x, 0.572, date, fontsize=9.2, color=GRAY, ha="center",
                    va="center")
            ax.text(x, 0.622, title, fontsize=12, color=color, weight="bold",
                    ha="center", va="center")
            ax.text(x, 0.742, body, fontsize=8.8, color=DARK, ha="center",
                    va="top", linespacing=1.7)
        else:
            ax.text(x, 0.428, date, fontsize=9.2, color=GRAY, ha="center",
                    va="center")
            ax.text(x, 0.378, title, fontsize=12, color=color, weight="bold",
                    ha="center", va="center")
            ax.text(x, 0.322, body, fontsize=8.8, color=DARK, ha="center",
                    va="top", linespacing=1.7)

    punchline(fig, "七年只做成一件事：把样车变成能上产线的车。")
    footer(fig, "据合作历程与 2026 年 11 月 16 日广州示范运营公开口径整理；千台级为计划目标，非已实现数量。")
    fig.savefig(OUT + "图1_七年时间线.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.135, 0.910, 0.690])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "套件成本，砍掉七成", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.888, "第七代铂智 4X 的硬件套件总成本，较前代下降约 70%",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    # 总量条：前代 100，第七代 30
    x0, total_w, bar_h, bar_y = 0.075, 0.860, 0.130, 0.620
    keep = 0.30

    ax.text(x0, 0.800, "以「前代套件成本 = 100」为指数", fontsize=9.4,
            color=GRAY, va="center")

    ax.add_patch(Rectangle((x0, bar_y), total_w * keep, bar_h,
                           facecolor=NAVY, edgecolor="none"))
    ax.add_patch(Rectangle((x0 + total_w * keep, bar_y), total_w * (1 - keep),
                           bar_h, facecolor=RED, edgecolor="none", alpha=0.85))

    ax.text(x0 + total_w * keep / 2, bar_y + bar_h / 2, "30", fontsize=20,
            color="white", weight="bold", ha="center", va="center")
    ax.text(x0 + total_w * keep + total_w * (1 - keep) / 2, bar_y + bar_h / 2,
            "降掉 70", fontsize=17, color="white", weight="bold",
            ha="center", va="center")

    ax.text(x0, bar_y - 0.055, "整条代表前代套件成本 100，其中 70 已被降掉", fontsize=9.4,
            color=GRAY, ha="left", va="center")

    # 三段说明
    ax.plot([x0, x0 + total_w], [0.500, 0.500], color=LIGHT, linewidth=1.1)

    notes = [
        ("成本", "同样一笔钱，能布约 3.3 倍的车"),
        ("可靠性", "核心零部件车规级，配多重安全冗余"),
        ("形态", "从改装车，变成产线下线的量产车型"),
    ]
    for i, (tag, text) in enumerate(notes):
        y = 0.430 - i * 0.105
        ax.text(x0, y, tag, fontsize=9.2, color=GRAY, va="center")
        ax.text(x0 + 0.105, y, text, fontsize=10.4, color=DARK, va="center")

    punchline(fig, "成本不降，千台级只是账面上的一句话。")
    footer(fig, "降幅为厂商公布口径；「3.3 倍」为按 1÷0.3 所做换算，未计运营与维保成本。")
    fig.savefig(OUT + "图2_成本七成.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.135, 0.910, 0.690])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "一台车要跑起来，得三方接上", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.888, "技术、产线、维保，缺一段就不成单元",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    def card(x0, y0, w, h, color, title, rows):
        ax.add_patch(Rectangle((x0, y0), w, h, facecolor=PALE,
                               edgecolor=LIGHT, linewidth=1.0))
        ax.add_patch(Rectangle((x0, y0 + h - 0.012), w, 0.012, facecolor=color,
                               edgecolor="none"))
        ax.text(x0 + 0.026, y0 + h - 0.062, title, fontsize=12.2, color=color,
                weight="bold", va="center")
        for i, line in enumerate(rows):
            ax.text(x0 + 0.026, y0 + h - 0.112 - i * 0.052, line, fontsize=9.2,
                    color=DARK, va="center")

    # 上：合资公司
    ax.add_patch(Rectangle((0.290, 0.660), 0.420, 0.155, facecolor="white",
                           edgecolor=NAVY, linewidth=1.4))
    ax.text(0.500, 0.765, "三方合资公司", fontsize=13.5, color=NAVY,
            weight="bold", ha="center", va="center")
    ax.text(0.500, 0.706, "2026 年目标：千台级 · 北上广深四城", fontsize=9.4,
            color=GRAY, ha="center", va="center")

    # 下左右两个主体
    card(0.030, 0.285, 0.420, 0.250, SLATE, "丰田", [
        "广汽丰田生产线负责量产",
        "经销商网络承接维保",
        "车规级零部件与冗余",
    ])
    card(0.550, 0.285, 0.420, 0.250, RED, "小马智行", [
        "L4 自动驾驶技术方案",
        "App／小程序直接面向乘客",
        "城市级运营经验复制",
    ])

    # 箭头
    ax.annotate("", xy=(0.395, 0.653), xytext=(0.320, 0.540),
                arrowprops=dict(arrowstyle="-|>", color=SLATE, linewidth=1.5,
                                shrinkA=0, shrinkB=0))
    ax.annotate("", xy=(0.605, 0.653), xytext=(0.680, 0.540),
                arrowprops=dict(arrowstyle="-|>", color=RED, linewidth=1.5,
                                shrinkA=0, shrinkB=0))

    ax.plot([0.030, 0.970], [0.212, 0.212], color=LIGHT, linewidth=1.1)
    ax.text(0.030, 0.155, "技术验证只证明「能开」，接上产线和维保才叫「能复制」",
            fontsize=9.8, color=DARK, va="center")

    punchline(fig, "能跑一台是技术，能跑一千台是体系。")
    footer(fig, "据合作分工公开口径整理；维保与运营的具体分工边界未在素材中细化。")
    fig.savefig(OUT + "图3_三方分工.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")