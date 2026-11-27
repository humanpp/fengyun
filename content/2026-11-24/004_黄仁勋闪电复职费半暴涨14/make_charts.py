# -*- coding: utf-8 -*-
"""
《黄仁勋闪电复职，英伟达一夜涨出 9520 亿美元》配套图表

事实口径（美东 2026-11-23 收盘）：
  · 英伟达 165.05 美元，+31.48%，市值 3.98 万亿美元，单日增加 9520 亿美元
    （美国上市公司单日市值增幅纪录；2003 年 5 月 9 日以来最大单日涨幅）。
  · 费城半导体指数 +14.03%；道指 +3.01%、标普 500 +4.73%、纳指 +6.51%。
  · SK 海力士 ADR +20.00%、美光 +19.04%、CoreWeave +22.32%、甲骨文 +12.34%、
    特斯拉 +11.46%、台积电 +14.00%；Lumentum 与迈威尔涨超 18%、英特尔涨超 16%、
    Nebius 涨超 20%（"超"值为媒体口径，图上不加总）。
  · 10 月初市值约 5.8 万亿美元（新华社）；辞职后累计蒸发超 2 万亿美元（新华社）。
  据财联社 2026-11-24、21 经济网 2026-11-24、新华财经 2026-11-24、新华社 2026-11-24。

风格：克制传媒风，编辑排版
输出目录 = 脚本所在目录
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle

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
Q_L, Q_R = "\u300c", "\u300d"


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
            ha="left", va="center", zorder=9, linespacing=1.5)


def outro(fig, ax, text, color=INK, width=0.700):
    ax.add_patch(FancyBboxPatch(
        (0.042, 0.082), width, 0.048,
        boxstyle="round,pad=0.002,rounding_size=0.008",
        facecolor=color, edgecolor="none", zorder=6))
    ax.text(0.062, 0.106, text, fontsize=10.2, color=WHITE,
            ha="left", va="center", zorder=9)


# ---------------------------------------------------------------- 图 1
def fig1():
    rows = [
        ("英伟达", 31.48, NAVY, "个股"),
        ("CoreWeave", 22.32, TEAL, "算力新云"),
        ("SK 海力士 ADR", 20.00, GOLD, "存储"),
        ("美光科技", 19.04, GOLD, "存储"),
        ("费城半导体指数", 14.03, RED, "指数"),
        ("台积电", 14.00, INK, "个股"),
        ("甲骨文", 12.34, INK, "个股"),
        ("特斯拉", 11.46, INK, "个股"),
        ("纳斯达克综指", 6.51, MUTED, "大盘"),
        ("标普 500", 4.73, MUTED, "大盘"),
        ("道琼斯指数", 3.01, MUTED, "大盘"),
    ]

    fig = plt.figure(figsize=(13.6, 8.0))
    ax = new_axes(fig)

    head(fig, ax,
         "2026.11.23  美东收盘",
         "一天之内，谁涨得最凶",
         "11 月 23 日涨跌幅，按幅度排序（%）",
         NAVY)

    x0, span = 0.250, 0.560
    vmax = 34.0
    top, step, h = 0.752, 0.0500, 0.0265

    for i, (name, val, color, group) in enumerate(rows):
        y = top - i * step
        ax.plot([x0 - 0.030, x0 - 0.030], [top + 0.019, y - 0.019],
                color=HAIR, linewidth=0.8, zorder=3)
        ax.plot([x0, x0], [top + 0.024, y - 0.024], color=HAIR,
                linewidth=1.0, zorder=3)
        ax.text(x0 - 0.042, y, name, fontsize=10.6, color=INK,
                ha="right", va="center", zorder=9)
        w = val / vmax * span
        ax.add_patch(Rectangle((x0, y - h / 2), w, h, facecolor=color,
                               edgecolor="none", zorder=6))
        ax.text(x0 + w + 0.010, y, "%.2f" % val, fontsize=10.6, color=color,
                weight="bold", ha="left", va="center", zorder=9)
        ax.text(0.885, y, group, fontsize=8.2, color=MUTED,
                ha="left", va="center", zorder=9)

    ax.text(x0 - 0.030, top + 0.040, "0", fontsize=8.0, color=MUTED,
            ha="center", va="center", zorder=9)

    note = ("未进榜但同样暴涨：Lumentum、迈威尔涨超 18%，Nebius 涨超 20%，"
            "英特尔涨超 16%。\n"
            "注：媒体对上述四家只给下限，故不画入排序。")
    ax.add_patch(FancyBboxPatch(
        (0.042, 0.150), 0.916, 0.088,
        boxstyle="round,pad=0,rounding_size=0.008",
        facecolor=WASH, edgecolor="none", zorder=3))
    ax.text(0.062, 0.194, note, fontsize=8.8, color=INK, ha="left",
            va="center", zorder=9, linespacing=1.7)

    outro(fig, ax, "英伟达自己涨 31.48%，比它更凶的是替它配套的人。")
    foot(fig, ax, "数据来源：财联社、21 经济网、新华财经、GSM 收盘播报（均 2026-11-23／24）；"
                  "个股为常规交易时段收盘价，SK 海力士为美国存托凭证口径。")
    fig.savefig(OUT + "图1_一天涨了多少.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    events = [
        ("11.17", "周一", "董事长哈维·琼斯在财报电话会上说，董事会不打算让黄仁勋复职。", NAVY, False),
        ("11.22", "周日", "据彭博社，董事会当天下午作出决定，未事先征询高级管理层。", NAVY, False),
        ("11.22", "夜里", "特朗普致电黄仁勋，只提一个要求：好好工作。", GOLD, False),
        ("11.23", "周一", "上午公告：董事会一致投票，即日起恢复总裁、CEO 及董事职务。", RED, False),
        ("11.23", "盘中", "特朗普在 CNBC：我跟他们谈过，而且我说服了他们。", RED, False),
        ("11.23", "收盘", "英伟达 +31.48%，费半 +14.03%，纳指 +6.51%。", RED, False),
        ("12.01", "待定", "众议院三个委员会闭门转录访谈。", MUTED, True),
        ("12.02", "待定", "总法律顾问蒂姆·泰特接受问询。", MUTED, True),
        ("12.03", "10:00", "参议院银行委员会公开听证，目前列出的证人只有他一个。", MUTED, True),
    ]

    fig = plt.figure(figsize=(13.6, 8.0))
    ax = new_axes(fig)

    head(fig, ax,
         "六天，然后排期表",
         "反转只用六天，问询排到了 12 月 3 日",
         "从 11 月 17 日到 12 月 3 日（当地时间）",
         RED)

    lx, dx, rx = 0.080, 0.205, 0.230
    top, step = 0.744, 0.0682

    ax.plot([dx, dx], [top + 0.030, top - (len(events) - 1) * step - 0.030],
            color=HAIR, linewidth=1.6, zorder=3)

    for i, (day, tag, text, color, future) in enumerate(events):
        y = top - i * step
        ax.text(lx, y + 0.008, day, fontsize=11.0, color=color,
                weight="bold", ha="left", va="center", zorder=9)
        ax.text(lx, y - 0.020, tag, fontsize=8.0, color=MUTED,
                ha="left", va="center", zorder=9)
        if future:
            ax.add_patch(Circle((dx, y), 0.0075, facecolor=WHITE,
                                edgecolor=MUTED, linewidth=1.6, zorder=8))
        else:
            ax.add_patch(Circle((dx, y), 0.0085, facecolor=color,
                                edgecolor="none", zorder=8))
        ax.text(rx, y, text, fontsize=9.6,
                color=MUTED if future else INK,
                ha="left", va="center", zorder=9)

    y17 = top
    y23 = top - 5 * step
    ax.annotate("", xy=(0.640, y23), xytext=(0.640, y17),
                arrowprops=dict(arrowstyle="<|-|>", color=RED,
                                linewidth=1.4, shrinkA=0, shrinkB=0))
    ax.text(0.660, (y17 + y23) / 2, "六天", fontsize=9.4, color=RED,
            weight="bold", rotation=90, ha="center", va="center", zorder=9)

    outro(fig, ax, "董事会改主意的成本是六天；国会那三场会的日程一天没动。",
          width=0.780)
    foot(fig, ax, "时间线据新华社 2026-11-24、中新网 2026-11-23、彭博社 2026-11-23（凤凰网转述）、"
                  "第一财经 2026-11-24、TipRanks 2026-11-23；"
                  "12 月三场为委员会已公布日程，均未发生。")
    fig.savefig(OUT + "图2_六天反转.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(13.6, 8.0))
    ax = new_axes(fig)

    head(fig, ax,
         "0.952 万亿的分量",
         "补回的是折价，不是那 2 万亿",
         "英伟达市值，单位：万亿美元",
         GOLD)

    x0 = 0.230
    unit = 0.108          # 每 1 万亿美元对应的宽度
    h = 0.072
    y_peak, y_now = 0.716, 0.622
    x_peak = x0 + 5.80 * unit
    x_now = x0 + 3.98 * unit
    x_mid = 0.560

    # 峰值参考线
    ax.plot([x0, x_peak], [y_peak, y_peak], color=MUTED, linewidth=1.1,
            linestyle=(0, (5, 3)), zorder=6)
    ax.plot([x_peak, x_peak], [y_peak, y_peak - 0.026], color=MUTED,
            linewidth=1.0, zorder=6)
    ax.text(0.164, y_peak, "10 月初峰值", fontsize=10.0, color=MUTED,
            ha="right", va="center", zorder=9)
    ax.text(x_peak + 0.012, y_peak, "5.80", fontsize=10.4, color=MUTED,
            weight="bold", ha="left", va="center", zorder=9)

    # 收盘：已经回来的 + 还差着的
    ax.text(0.164, y_now, "11 月 23 日收盘", fontsize=10.6, color=INK,
            ha="right", va="center", zorder=9)
    ax.add_patch(Rectangle((x0, y_now - h / 2), 3.98 * unit, h,
                           facecolor=NAVY, edgecolor="none", zorder=6))
    ax.add_patch(Rectangle((x_now, y_now - h / 2), 1.82 * unit, h,
                           facecolor=WASH, edgecolor=MUTED, linewidth=1.0,
                           linestyle=(0, (4, 2)), zorder=6))
    ax.text(x_now - 0.014, y_now, "3.98", fontsize=10.8, color=WHITE,
            weight="bold", ha="right", va="center", zorder=9)
    ax.text(x_now + 0.014, y_now, "还差 1.82", fontsize=9.8, color=MUTED,
            ha="left", va="center", zorder=9)

    ax.plot([0.042, 0.958], [0.520, 0.520], color=HAIR, linewidth=1.0,
            zorder=5)

    y_evap, y_day = 0.436, 0.318

    ax.text(0.164, y_evap, "辞职后累计蒸发", fontsize=10.6, color=INK,
            ha="right", va="center", zorder=9)
    ax.add_patch(Rectangle((x0, y_evap - h / 2), 2.00 * unit, h,
                           facecolor=HAIR, edgecolor="none", zorder=6))
    ax.text(x0 + 2.00 * unit + 0.012, y_evap, "超 2.00", fontsize=10.4,
            color=MUTED, weight="bold", ha="left", va="center", zorder=9)

    ax.text(0.164, y_day, "11 月 23 日单日", fontsize=10.6, color=INK,
            ha="right", va="center", zorder=9)
    ax.add_patch(Rectangle((x0, y_day - h / 2), 0.952 * unit, h,
                           facecolor=RED, edgecolor="none", zorder=6))
    ax.text(x0 + 0.952 * unit + 0.012, y_day, "0.952", fontsize=10.4,
            color=RED, weight="bold", ha="left", va="center", zorder=9)

    ax.plot([x_mid, x_mid], [y_day, y_evap], color=RED, linewidth=1.1,
            linestyle=(0, (3, 3)), zorder=4)
    ax.text(x_mid + 0.014, (y_day + y_evap) / 2,
            "补回的比例：约 48%（按下限 2.00 算）", fontsize=9.4, color=RED,
            ha="left", va="center", zorder=9)

    ax.add_patch(FancyBboxPatch(
        (0.042, 0.176), 0.916, 0.070,
        boxstyle="round,pad=0,rounding_size=0.008",
        facecolor=WASH, edgecolor="none", zorder=3))
    ax.text(0.062, 0.211,
            "读法：5.80 − 3.98 = 1.82，这是还没回来的市值；0.952 ÷ 2.00 ≈ 48%，这是这一天补回的比例。",
            fontsize=8.8, color=INK, ha="left", va="center", zorder=9)

    outro(fig, ax, "一天补回 0.952 万亿，账上还有 1.82 万亿没回来。",
          width=0.720)
    foot(fig, ax, "数据来源：10 月初市值约 5.8 万亿美元、辞职后累计蒸发超 2 万亿美元（新华社 2026-11-24）；"
                  "11 月 23 日收盘 3.98 万亿美元、单日增加 9520 亿美元（新华财经 2026-11-24）。"
                  "注：1.82 与 48% 为按上述公开数字所作的减法与除法，非机构口径。")
    fig.savefig(OUT + "图3_补回多少.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)