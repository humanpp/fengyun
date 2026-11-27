# -*- coding: utf-8 -*-
"""
《160 万辆、2002 款：高田气囊的余波，比车型生命周期长一倍》配套图表

事实口径（NHTSA 召回文件 26V765、路透社 2026-11-20、盖世汽车 2026-11-24）：
  · 本田在美国召回 810,592 辆；丰田全球约 79 万辆，其中美国 314,029 辆。
  · 两家均称本批车辆无相关伤亡、事故与发生器破裂；丰田替换件预计 2027 年初到位。
  · 本田召回限高温高湿、温差大的 14 个州与属地。
  · 本田 2025 年 5 月严苛环境模拟测试首次发现问题，但未显示异常行为与统计显著偏差；
    丰田自 2016 年起研究 PSAN 推进剂，据寿命预测模型判定部分发生器已达寿命终点。
  · 高田 2017 年 6 月申请破产；均胜安全以 15.88 亿美元收购其除 PSAN 业务外主要资产，
    2018 年 4 月交割。车型年款 2002—2017。
  · 2009 年以来 NHTSA 记录 28 起死亡、400 多起受伤；截至 2017 年 5 月全球累计召回约 1.2 亿辆。

风格：克制传媒风，编辑排版
输出目录 = 脚本所在目录
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["figure.facecolor"] = "white"
plt.rcParams["savefig.facecolor"] = "white"

INK = "#1a2332"
NAVY = "#1b3a5c"
RED = "#b0413e"
TEAL = "#2f6b64"
GOLD = "#9a7b3f"
MUTED = "#7b8494"
HAIR = "#dfe3e8"
WASH = "#f4f6f8"
WHITE = "#ffffff"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep


def new_axes(fig):
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return ax


def head(fig, ax, kicker, title, sub, color):
    ax.add_patch(Rectangle((0.042, 0.928), 0.0075, 0.040,
                           facecolor=color, edgecolor="none", zorder=9))
    ax.text(0.058, 0.950, kicker, fontsize=9.2, color=color,
            weight="bold", ha="left", va="center", zorder=9)
    ax.text(0.042, 0.900, title, fontsize=21, color=INK, weight="bold",
            ha="left", va="top", zorder=9)
    ax.text(0.042, 0.848, sub, fontsize=10.4, color=MUTED,
            ha="left", va="top", zorder=9)
    ax.plot([0.042, 0.958], [0.812, 0.812], color=HAIR, linewidth=1.0,
            zorder=5)


def foot(fig, ax, text):
    ax.plot([0.042, 0.958], [0.058, 0.058], color=HAIR, linewidth=0.9,
            zorder=5)
    ax.text(0.042, 0.032, text, fontsize=7.0, color=MUTED,
            ha="left", va="center", zorder=9)


def outro(fig, ax, text, color=INK, width=0.800):
    ax.add_patch(FancyBboxPatch(
        (0.042, 0.082), width, 0.048,
        boxstyle="round,pad=0.002,rounding_size=0.008",
        facecolor=color, edgecolor="none", zorder=6))
    ax.text(0.062, 0.106, text, fontsize=10.2, color=WHITE,
            ha="left", va="center", zorder=9)


def note(fig, ax, y, h, text, size=8.8):
    ax.add_patch(FancyBboxPatch(
        (0.042, y), 0.916, h,
        boxstyle="round,pad=0,rounding_size=0.008",
        facecolor=WASH, edgecolor="none", zorder=3))
    ax.text(0.062, y + h / 2, text, fontsize=size, color=INK,
            ha="left", va="center", zorder=9, linespacing=1.6)


def arrow(ax, x1, x2, y, color="#c3cad3"):
    ax.annotate("", xy=(x2, y), xytext=(x1, y),
                arrowprops=dict(arrowstyle="-|>", color=color, linewidth=1.6,
                                shrinkA=0, shrinkB=0))


# ---------------------------------------------------------------- 图 1
def fig1():
    fig = plt.figure(figsize=(13.6, 8.0))
    ax = new_axes(fig)

    head(fig, ax,
         "2026.11.20  提交 NHTSA",
         "约 160 万辆，七成落在美国",
         "召回规模拆分（万辆）",
         NAVY)

    x0, span, vmax = 0.240, 0.560, 165.0
    h = 0.062

    # 合计
    y1 = 0.700
    ax.text(x0 - 0.020, y1 + 0.012, "两家合计", fontsize=11.2, color=INK,
            weight="bold", ha="right", va="center", zorder=9)
    ax.text(x0 - 0.020, y1 - 0.024, "约 160 万", fontsize=8.4, color=MUTED,
            ha="right", va="center", zorder=9)
    ax.add_patch(Rectangle((x0, y1 - h / 2), 160.06 / vmax * span, h,
                           facecolor=MUTED, edgecolor="none", zorder=6))
    ax.text(x0 + 160.06 / vmax * span + 0.012, y1, "160.1", fontsize=12.0,
            color=MUTED, weight="bold", ha="left", va="center", zorder=9)

    # 本田
    y2 = 0.560
    ax.text(x0 - 0.020, y2 + 0.012, "本田", fontsize=11.2, color=INK,
            weight="bold", ha="right", va="center", zorder=9)
    ax.text(x0 - 0.020, y2 - 0.024, "全部在美国", fontsize=8.4, color=MUTED,
            ha="right", va="center", zorder=9)
    ax.add_patch(Rectangle((x0, y2 - h / 2), 81.06 / vmax * span, h,
                           facecolor=NAVY, edgecolor="none", zorder=6))
    ax.text(x0 + 81.06 / vmax * span + 0.012, y2, "81.06", fontsize=12.0,
            color=NAVY, weight="bold", ha="left", va="center", zorder=9)

    # 丰田：美国 + 其他市场
    y3 = 0.420
    ax.text(x0 - 0.020, y3 + 0.012, "丰田", fontsize=11.2, color=INK,
            weight="bold", ha="right", va="center", zorder=9)
    ax.text(x0 - 0.020, y3 - 0.024, "全球约 79 万", fontsize=8.4, color=MUTED,
            ha="right", va="center", zorder=9)
    w_us = 31.40 / vmax * span
    w_ot = 47.60 / vmax * span
    ax.add_patch(Rectangle((x0, y3 - h / 2), w_us, h, facecolor=NAVY,
                           edgecolor="none", zorder=6))
    ax.add_patch(Rectangle((x0 + w_us, y3 - h / 2), w_ot, h, facecolor=TEAL,
                           edgecolor="none", zorder=6))
    ax.text(x0 + w_us / 2, y3 - 0.062, "美国 31.40", fontsize=8.6,
            color=NAVY, weight="bold", ha="center", va="center", zorder=9)
    ax.text(x0 + w_us + w_ot / 2, y3 + 0.058, "其他市场 47.60", fontsize=8.6,
            color=TEAL, weight="bold", ha="center", va="center", zorder=9)
    ax.text(x0 + w_us + w_ot + 0.012, y3, "79.00", fontsize=12.0,
            color=TEAL, weight="bold", ha="left", va="center", zorder=9)

    ax.plot([x0, x0], [0.760, 0.360], color=HAIR, linewidth=1.0, zorder=4)

    note(fig, ax, 0.176, 0.086,
         "本田召回限在高温高湿、温差大的 14 个州与属地；两家均称本批车辆暂无伤亡、"
         "无破裂报告，属预防性召回。\n"
         "「其他市场 47.60」为约 79 万减去美国 31.40 万的推算值，非官方分项数据。")

    outro(fig, ax, "160 万辆里，约七成在美国；其余散在别的市场，也要换件。")
    foot(fig, ax, "数据来源：NHTSA 召回文件 26V765（2026-11-20）、路透社 11-20、盖世汽车 11-24、"
                  "N 环球 11-21（14 个州与属地口径）。")
    fig.savefig(OUT + "图1_160万辆怎么分.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(13.6, 8.0))
    ax = new_axes(fig)

    head(fig, ax,
         "2002 → 2027",
         "一条召回线，拉了二十多年",
         "同一批气体发生器的失效时间轴（按年份等距）",
         RED)

    x_2000, x_2028 = 0.092, 0.940
    per = (x_2028 - x_2000) / 28.0

    def px(year):
        return x_2000 + (year - 2000) * per

    axis_y = 0.470
    ax.plot([px(2000), px(2028)], [axis_y, axis_y], color="#9aa3ad",
            linewidth=1.4, zorder=5)

    for yr in (2000, 2005, 2010, 2015, 2020, 2025):
        ax.plot([px(yr), px(yr)], [axis_y, axis_y - 0.014], color=HAIR,
                linewidth=1.0, zorder=4)
        ax.text(px(yr), axis_y - 0.040, str(yr), fontsize=8.6, color=MUTED,
                ha="center", va="center", zorder=9)

    up = [
        (2002, "2002 款", "最老的在召回名单里\n雷克萨斯 SC430（2002—2010 款）", NAVY, "center"),
        (2017.5, "2017.06", "高田申请破产\n负债超 1 万亿日元", RED, "center"),
        (2026.9, "2026.11", "本田 + 丰田再召回\n约 160 万辆", RED, "right"),
    ]
    down = [
        (2009.2, "2009 起", "NHTSA 记录首例死亡\n此后 28 死、400 余伤", MUTED, "center"),
        (2027.8, "2027 初", "丰田替换件\n预计到位", MUTED, "right"),
    ]

    for year, tag, text, color, ha in up:
        x = px(year)
        ax.plot([x, x], [axis_y, axis_y + 0.030], color=color, linewidth=1.0,
                zorder=5)
        ax.add_patch(Circle((x, axis_y), 0.0070, facecolor=color,
                            edgecolor="none", zorder=8))
        ax.text(x, axis_y + 0.052, tag, fontsize=10.0, color=color,
                weight="bold", ha=ha, va="center", zorder=9)
        ax.text(x, axis_y + 0.116, text, fontsize=8.6, color=INK, ha=ha,
                va="center", zorder=9, linespacing=1.6)

    for year, tag, text, color, ha in down:
        x = px(year)
        ax.plot([x, x], [axis_y, axis_y - 0.026], color=color, linewidth=1.0,
                zorder=5)
        ax.add_patch(Circle((x, axis_y), 0.0070, facecolor=WHITE,
                            edgecolor=color, linewidth=1.4, zorder=8))
        ax.text(x, axis_y - 0.078, tag, fontsize=10.0, color=color,
                weight="bold", ha=ha, va="center", zorder=9)
        ax.text(x, axis_y - 0.150, text, fontsize=8.6, color=INK, ha=ha,
                va="center", zorder=9, linespacing=1.6)

    ax.annotate("", xy=(px(2026.9), 0.704), xytext=(px(2002), 0.704),
                arrowprops=dict(arrowstyle="<|-|>", color=NAVY,
                                linewidth=1.2, shrinkA=0, shrinkB=0))
    ax.text((px(2002) + px(2026.9)) / 2, 0.728, "从装车到召回：24 年",
            fontsize=9.6, color=NAVY, weight="bold", ha="center",
            va="center", zorder=9)

    note(fig, ax, 0.150, 0.060,
         "召回发出来，到替换件真正装上，中间还隔了一年多。图为按年份等距绘制，不是等比例时间轴。")

    outro(fig, ax, "一个车型的生命周期，装不下这条召回线。")
    foot(fig, ax, "数据来源：NHTSA 召回文件 26V765、路透社 2026-11-20、盖世汽车 11-24、"
                  "日经中文网 2017-06-16（破产与负债）。"
                  "2009 年起点按 NHTSA 记录的死亡案例起始年份计。")
    fig.savefig(OUT + "图2_二十四年.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(13.6, 8.0))
    ax = new_axes(fig)

    head(fig, ax,
         "两家怎么发现的",
         "没有一家是当场复现破裂的",
         "本田与丰田的发现路径",
         GOLD)

    rows = [
        ("本田", "美规 81.06 万辆", NAVY, 0.640,
         ["2025.05\n严苛环境模拟测试", "首次发现苗头\n无异常行为、无显著偏差", "2026.11\n提交召回"],
         "发现的不是故障，是一个「不太对」的苗头。"),
        ("丰田", "全球约 79 万辆", TEAL, 0.380,
         ["2016 起\n收集研究特定发生器", "锁定 PSAN 推进剂\n建寿命预测模型", "2026.11\n提交召回"],
         "判定的不是当下好坏，是「还剩多少寿命」。"),
    ]

    slots = [0.300, 0.520, 0.740]
    bw, bh = 0.190, 0.090

    for name, sub, color, y, chain, caption in rows:
        ax.text(0.042, y + 0.020, name, fontsize=15.0, color=color,
                weight="bold", ha="left", va="center", zorder=9)
        ax.text(0.042, y - 0.026, sub, fontsize=8.6, color=MUTED,
                ha="left", va="center", zorder=9)

        for i, cell in enumerate(chain):
            sx = slots[i]
            ax.add_patch(FancyBboxPatch(
                (sx, y - bh / 2), bw, bh,
                boxstyle="round,pad=0,rounding_size=0.008",
                facecolor=WHITE, edgecolor=color, linewidth=1.3, zorder=6))
            ax.text(sx + bw / 2, y, cell, fontsize=8.8, color=INK,
                    ha="center", va="center", zorder=9, linespacing=1.6)
            if i < len(chain) - 1:
                arrow(ax, sx + bw + 0.006, slots[i + 1] - 0.006, y)

        ax.text(slots[0], y - 0.086, caption, fontsize=8.8, color=MUTED,
                ha="left", va="center", zorder=9)

    note(fig, ax, 0.168, 0.070,
         "两家的起点都不是「看到破裂」，而是「算出来该坏了」或「测出一个不太对的信号」。\n"
         "这正是安全件最难防的一类失效：它不给你当场复现的机会。")

    outro(fig, ax, "验证做了，但没测出来——这才是要防的那一类。")
    foot(fig, ax, "数据来源：NHTSA 召回文件 26V765 及盖世汽车 2026-11-24 对两家发现过程的转述；"
                  "PSAN 指相稳定硝酸铵推进剂。")
    fig.savefig(OUT + "图3_两家怎么发现的.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)