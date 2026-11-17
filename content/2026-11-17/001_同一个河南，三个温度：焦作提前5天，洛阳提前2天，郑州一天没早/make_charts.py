# -*- coding: utf-8 -*-
"""
《同一个河南，三个温度：焦作提前 5 天，洛阳提前 2 天，郑州一天没早》配套图表
事实口径：2026-11-10 焦作城区集中供热提前启动；2026-11-13 零时洛阳主城区
采暖季起始时间由原定 11-15 零时提前；郑州按《郑州市城市供热与用热管理办法》
11-15 起进入供热期，能否提前"须由市人民政府决定"；焦作农村无集中供暖。
风格：克制传媒风，白底、低饱和配色、标题即结论
输出目录 = 脚本所在目录
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch

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


def punchline(fig, text, y=0.072):
    fig.text(0.045, y, text, fontsize=10.4, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


# ---------------------------------------------------------------- 图 1
def fig1():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.105, 0.930, 0.720])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "三个城市，一条时间线", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.885, "2026 年 11 月，河南三市集中供热的启动日：提前 5 天、提前 2 天、0 天",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    # 日期 → 横坐标（11/9 起算，线性映射）
    def xd(day):
        return 0.06 + (day - 9) * (0.88 / 7.0)

    y_line = 0.655
    ax.plot([0.04, 0.96], [y_line, y_line], color=LIGHT, linewidth=2.6,
            solid_capstyle="round", zorder=1)

    nodes = [
        (10, "焦作", NAVY, "提前 5 天", "11 月 10 日", "城区集中供热\n提前启动",
         "有居民说，家里踩地板\n已经「温温的」"),
        (13, "洛阳", SLATE, "提前 2 天", "11 月 13 日零时",
         "主城区采暖季\n起始时间", "由原定 15 日零时\n提前至 13 日零时"),
        (15, "郑州", RED, "提前 0 天", "11 月 15 日零时",
         "按《郑州市城市供热\n与用热管理办法》",
         "能否提前「须由市人民政府决定」\n截至 11 月 8 日未松口"),
    ]

    # 间距双箭头
    for d1, d2, label in [(10, 13, "5 天"), (13, 15, "2 天")]:
        x1, x2 = xd(d1), xd(d2)
        ax.annotate("", xy=(x2 - 0.012, 0.585), xytext=(x1 + 0.012, 0.585),
                    arrowprops=dict(arrowstyle="<->", color=GRAY, linewidth=1.1,
                                    shrinkA=0, shrinkB=0))
        ax.text((x1 + x2) / 2, 0.552, label, fontsize=10, color=GRAY,
                ha="center", va="center")

    bw, bh, by = 0.245, 0.330, 0.115
    for day, city, color, gap, date, head, body in nodes:
        x = xd(day)
        cx = min(max(x, 0.045 + bw / 2), 0.955 - bw / 2)

        ax.scatter([x], [y_line], s=210, facecolor=color, edgecolor="white",
                   linewidth=2.2, zorder=3)
        ax.text(x, 0.760, city, fontsize=14, color=color, weight="bold",
                ha="center", va="center")
        ax.text(x, 0.712, gap, fontsize=11.5, color=DARK, ha="center", va="center")

        ax.plot([cx, cx], [y_line - 0.020, by + bh], color=LIGHT, linewidth=1.3,
                zorder=1, linestyle=(0, (3, 2)))
        ax.add_patch(Rectangle((cx - bw / 2, by), bw, bh, facecolor=PALE,
                               edgecolor=LIGHT, linewidth=1.0, zorder=2))
        ax.add_patch(Rectangle((cx - bw / 2, by + bh - 0.012), bw, 0.012,
                               facecolor=color, edgecolor="none", zorder=3))
        ax.text(cx - bw / 2 + 0.016, by + bh - 0.050, date, fontsize=10.6,
                color=color, weight="bold", ha="left", va="top", zorder=4)
        ax.text(cx - bw / 2 + 0.016, by + bh - 0.104, head, fontsize=9.2,
                color=DARK, ha="left", va="top", zorder=4, linespacing=1.6)
        ax.text(cx - bw / 2 + 0.016, by + bh - 0.190, body, fontsize=9.2,
                color=SLATE, ha="left", va="top", zorder=4, linespacing=1.7)

    punchline(fig, "同样是 11 月 15 日这个起点，有人往前挪了 5 天，有人挪了 2 天，有人一步没动。")
    footer(fig, "启动日据素材口径整理；焦作「提前 5 天」以 11 月 15 日为常规起点推算。")
    fig.savefig(OUT + "图1_一条时间线.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.135, 0.930, 0.690])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "同样的降温，三种答法", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.882, "决定的主体是同一个，不同的只是「什么时候把字签下去」",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    cols = [(0.030, "城市"), (0.170, "启动时间"), (0.410, "依据"),
            (0.800, "相对 11/15")]
    ax.plot([0.012, 0.988], [0.742, 0.742], color=LIGHT, linewidth=1.4)
    for x, name in cols:
        ax.text(x, 0.780, name, fontsize=10.4, color=GRAY, weight="bold",
                va="center")

    rows = [
        ("焦作", "11 月 10 日", "提前启动城区集中供热", "提前 5 天", NAVY),
        ("洛阳", "11 月 13 日零时", "调整采暖季起始时间（原定 15 日零时）",
         "提前 2 天", SLATE),
        ("郑州", "11 月 15 日零时", "《郑州市城市供热与用热管理办法》",
         "0 天", RED),
    ]

    for i, (city, start, basis, delta, color) in enumerate(rows):
        y = 0.645 - i * 0.163
        if i % 2 == 0:
            ax.add_patch(Rectangle((0.012, y - 0.072), 0.976, 0.144,
                                   facecolor=PALE, edgecolor="none"))
        ax.text(0.030, y, city, fontsize=12.6, color=color, weight="bold",
                va="center")
        ax.text(0.170, y, start, fontsize=10.8, color=DARK, va="center")
        ax.text(0.410, y, basis, fontsize=10.4, color=SLATE, va="center")
        ax.text(0.800, y, delta, fontsize=12.2, color=color, weight="bold",
                va="center")

    ax.plot([0.012, 0.988], [0.222, 0.222], color=LIGHT, linewidth=1.2)
    ax.text(0.030, 0.172,
            "焦作、洛阳：市政府在冷空气到达之前改了日期。",
            fontsize=10.6, color=DARK, va="center")
    ax.text(0.030, 0.108,
            "郑州：日期写在《办法》里，改它要先有市政府的决定——这个决定没出来。",
            fontsize=10.6, color=DARK, va="center")

    punchline(fig, "条文写死了日子，改它要多一道签字；签字之前，冷空气不等。")
    footer(fig, "据素材口径整理：郑州常规供热期为 11 月 15 日至次年 3 月 15 日，提前须由市人民政府决定。")
    fig.savefig(OUT + "图2_三种答法.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.135, 0.930, 0.660])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.950, "第四个温度：同一个焦作，两种冬天", fontsize=19,
             color=DARK, weight="bold", ha="left", va="top")
    fig.text(0.045, 0.878, "「提前 5 天」这句话，只对供热管网铺到的地方成立",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    panels = [
        (0.012, "城区", NAVY, [
            ("热从哪来", "换热站 → 小区管网 → 入户"),
            ("有没有「开栓日」", "有，11 月 10 日提前启动"),
            ("谁来决定", "市政府统一决定"),
            ("这笔钱怎么算", "按面积或按热量计费，统一标准"),
        ]),
        (0.508, "农村", RED, [
            ("热从哪来", "电暖器、空调、天然气壁挂炉、燃煤"),
            ("有没有「开栓日」", "没有，用的时候自己开"),
            ("谁来决定", "一家一户自己决定"),
            ("这笔钱怎么算", "按电表、气表、煤价自己算"),
        ]),
    ]

    for x0, title, color, items in panels:
        ax.add_patch(FancyBboxPatch((x0, 0.140), 0.480, 0.660,
                                    boxstyle="round,pad=0.010,rounding_size=0.012",
                                    facecolor=PALE, edgecolor=LIGHT, linewidth=1.0))
        ax.add_patch(Rectangle((x0, 0.785), 0.480, 0.015, facecolor=color,
                               edgecolor="none"))
        ax.text(x0 + 0.024, 0.732, title, fontsize=15, color=color,
                weight="bold", va="center")

        for i, (label, value) in enumerate(items):
            y = 0.660 - i * 0.132
            ax.text(x0 + 0.026, y, label, fontsize=9.4, color=GRAY, va="center")
            ax.text(x0 + 0.026, y - 0.052, value, fontsize=10.6, color=DARK,
                    va="center")

    ax.text(0.012, 0.048,
            "对一个没有集中供暖的村子来说，冬天不是从「开栓日」开始的，是从炉子点着那天开始的。",
            fontsize=10.6, color=DARK, ha="left", va="center")

    footer(fig, "焦作农村不实行集中供暖；河南集中供热管网主要覆盖城区。")
    fig.savefig(OUT + "图3_第四个温度.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")
