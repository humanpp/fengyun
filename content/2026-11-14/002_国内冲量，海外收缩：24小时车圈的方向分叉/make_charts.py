# -*- coding: utf-8 -*-
"""
《国内冲量，海外收缩：24 小时车圈的方向分叉》配套图表
数据来源：文章正文及脚注所列公开报道
风格：克制传媒风，白底、低饱和配色、标题即结论
输出目录 = 脚本所在目录
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

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


def clean(ax, axis="x"):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(LIGHT)
    ax.tick_params(colors=DARK, labelsize=11, length=0)
    ax.set_axisbelow(True)
    ax.grid(axis=axis, color=LIGHT, linewidth=0.8, alpha=0.55)


def footer(fig, text):
    fig.text(0.045, 0.022, text, fontsize=8.4, color=GRAY, ha="left", va="bottom")


# ---------------------------------------------------------------- 图 1
def fig1():
    fig, ax = plt.subplots(figsize=(12, 7.0))
    fig.subplots_adjust(left=0.185, right=0.925, top=0.700, bottom=0.175)

    fig.suptitle("一天之内，价格带被从头到尾填满",
                 fontsize=19, color=DARK, x=0.045, ha="left", y=0.955, weight="bold")
    fig.text(0.045, 0.885,
             "11 月 13 日上市或预售的三款车，覆盖 12.99 万至 46.98 万元，区间几乎不重叠",
             fontsize=11, color=GRAY, ha="left")

    # (名称, 低, 高, 颜色, 副标题)
    cars = [
        ("问界新 M8\n增程 / 纯电", 37.98, 46.98, NAVY, "9 款配置 · 全系 ADS 5 + 4 颗激光雷达 · 研发投入 15 亿元"),
        ("启境 GT7 Ultra 舒享版\n增程 / 纯电", 22.19, 23.19, RED, "限时权益价，官方指导价 22.99 / 23.99 万 · L3 级八大冗余"),
        ("东风日产 NX7\n插电混动（预售）", 12.99, 14.99, GRAY, "3 款配置 · 宁德时代 40.9 度电池 · 纯电续航 320km"),
    ]

    for i, (name, lo, hi, color, _) in enumerate(cars):
        y = len(cars) - 1 - i
        # 价格区间投影条（浅色底）+ 实心范围
        ax.plot([0, hi], [y, y], color=LIGHT, lw=13, solid_capstyle="butt", zorder=1)
        ax.barh(y, hi - lo, left=lo, height=0.26, color=color, zorder=3)
        ax.text(hi + 1.2, y, f"{lo:g} – {hi:g} 万", va="center", ha="left",
                fontsize=14, color=DARK, weight="bold", zorder=4)

    ax.set_yticks(range(len(cars)))
    ax.set_yticklabels([c[0] for c in cars][::-1], fontsize=11.5, linespacing=1.5)
    for lbl, c in zip(ax.get_yticklabels(), cars[::-1]):
        lbl.set_color(c[3] if c[3] != GRAY else DARK)
        lbl.set_fontweight("bold")

    for i, (name, lo, hi, color, sub) in enumerate(cars):
        y = len(cars) - 1 - i
        ax.text(0, y - 0.215, sub, va="top", ha="left", fontsize=9.8,
                color=GRAY, style="italic")

    ax.set_xlim(0, 62)
    ax.set_ylim(-0.72, len(cars) - 0.28)
    ax.set_xlabel("官方指导价 / 预售价（万元）", fontsize=10.5, color=GRAY, labelpad=8)
    clean(ax)

    # 图例放在标题正下方，不遮挡数据
    fig.text(0.045, 0.845,
             "灰色 = 合资入门　　红色 = 新势力中段　　深蓝 = 高端旗舰　　三者价格带首尾相接，中间几无留白",
             fontsize=10, color=GRAY, ha="left", va="top")

    footer(fig, "数据：东风日产、启境汽车、鸿蒙智行发布会及汽车之家、IT之家、凤凰网等公开报道。NX7 为预售价，11 月 27 日正式上市。")
    fig.savefig(OUT + "图1_三款新车价格带.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig, (ax1, ax2) = plt.subplots(
        1, 2, figsize=(12, 7.0), gridspec_kw={"width_ratios": [1.25, 1]}
    )
    fig.subplots_adjust(left=0.085, right=0.945, top=0.730, bottom=0.185, wspace=0.32)

    fig.suptitle("剪刀差：总量在跌，渗透率在涨",
                 fontsize=19, color=DARK, x=0.045, ha="left", y=0.955, weight="bold")
    fig.text(0.045, 0.885,
             "新能源正在吃掉燃油车的份额，但还不足以对冲整体需求的回落",
             fontsize=11, color=GRAY, ha="left")

    # ---- 左：10 月产销同比
    cats = ["汽车\n产量", "汽车\n销量", "新能源\n产量", "新能源\n销量"]
    vals = [-8.8, -9.2, 13.8, 13.1]
    x = np.arange(len(cats))
    colors = [RED if v < 0 else NAVY for v in vals]

    ax1.bar(x, vals, width=0.52, color=colors)
    ax1.axhline(0, color=DARK, linewidth=1.0)
    for xi, v in zip(x, vals):
        off = 1.0 if v > 0 else -1.0
        va = "bottom" if v > 0 else "top"
        ax1.text(xi, v + off, f"{v:+.1f}%", ha="center", va=va,
                 fontsize=12.5, color=DARK, weight="bold")

    ax1.set_xticks(x)
    ax1.set_xticklabels(cats, fontsize=10.8, linespacing=1.5)
    ax1.set_ylim(-16, 20)
    ax1.set_ylabel("同比增速（%）", fontsize=10.5, color=GRAY, labelpad=8)
    clean(ax1, axis="y")
    ax1.set_title("10 月产销同比（中汽协）", fontsize=12, color=DARK,
                  loc="left", pad=12)

    # ---- 右：渗透率阶梯
    labels = ["10 月\n全月", "11 月 1—8 日"]
    pen = [64.3, 74.9]
    x2 = np.arange(len(labels))
    ax2.bar(x2, pen, width=0.40, color=[NAVY, RED])
    for xi, v in zip(x2, pen):
        ax2.text(xi, v + 1.8, f"{v}%", ha="center", va="bottom",
                 fontsize=14, color=DARK, weight="bold")

    ax2.set_xticks(x2)
    ax2.set_xticklabels(labels, fontsize=11, linespacing=1.5)
    ax2.set_ylim(0, 100)
    ax2.set_ylabel("新能源零售渗透率（%）", fontsize=10.5, color=GRAY, labelpad=8)
    clean(ax2, axis="y")
    ax2.set_title("渗透率（乘联会）", fontsize=12, color=DARK, loc="left", pad=12)

    # 说明两者口径不同
    ax2.text(0.5, 0.035, "↑ 两者口径不同：月度全月 vs 周度", transform=ax2.transAxes,
             fontsize=9.4, color=GRAY, ha="center", style="italic")

    box = dict(boxstyle="round,pad=0.6", facecolor=PALE, edgecolor=LIGHT, linewidth=0.9)
    fig.text(0.045, 0.085,
             "同一周的另一组数字：11 月 1—8 日全国乘用车零售 29.3 万辆，同比 −21%；"
             "而 10 月汽车出口 106.6 万辆，同比 +60.2%，连续 5 个月破百万。",
             fontsize=10, color=DARK, ha="left", va="center", bbox=box)

    footer(fig, "数据：中国汽车工业协会 2026 年 10 月数据；乘用车市场信息联席会 11 月 1—8 日周度数据。渗透率为新能源零售口径。")
    fig.savefig(OUT + "图2_产销与渗透率剪刀差.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig, (ax1, ax2) = plt.subplots(
        1, 2, figsize=(12, 7.0), gridspec_kw={"width_ratios": [1.15, 1]}
    )
    fig.subplots_adjust(left=0.075, right=0.945, top=0.720, bottom=0.275, wspace=0.42)

    fig.suptitle("禾赛科技：营收在涨，利润在降",
                 fontsize=19, color=DARK, x=0.045, ha="left", y=0.955, weight="bold")
    fig.text(0.045, 0.885,
             "2026 年第三季度，营收与出货量双增长，但两项增速均低于公司指引下限",
             fontsize=11, color=GRAY, ha="left")

    # ---- 左：增速对比
    items = ["营收", "激光雷达\n出货量", "GAAP 净利润", "毛利率\n(百分点)"]
    vals = [34.3, 65.3, -68.5, -1.1]
    x = np.arange(len(items))
    colors = [NAVY if v > 0 else RED for v in vals]

    ax1.bar(x, vals, width=0.50, color=colors)
    ax1.axhline(0, color=DARK, linewidth=1.0)
    for xi, v in zip(x, vals):
        off = 3.0 if v > 0 else -3.0
        va = "bottom" if v > 0 else "top"
        unit = "pp" if xi == 3 else "%"
        ax1.text(xi, v + off, f"{v:+.1f}{unit}", ha="center", va=va,
                 fontsize=12.5, color=DARK, weight="bold")

    ax1.set_xticks(x)
    ax1.set_xticklabels(items, fontsize=10.8, linespacing=1.4)
    ax1.set_ylim(-88, 82)
    ax1.set_ylabel("同比变化", fontsize=10.5, color=GRAY, labelpad=8)
    clean(ax1, axis="y")
    ax1.set_title("同比变化（%），净利受去年一次性收益基数影响",
                  fontsize=11.5, color=DARK, loc="left", pad=12)

    # ---- 右：分部经营利润
    segs = ["激光雷达\n分部", "SGI 分部\n(机器人+空间智能)"]
    profits = [1.45, -0.8288]
    x2 = np.arange(len(segs))
    c2 = [NAVY if v > 0 else RED for v in profits]
    ax2.bar(x2, profits, width=0.42, color=c2)
    ax2.axhline(0, color=DARK, linewidth=1.0)

    labels = ["+1.45 亿元\n同比 +88%", "−0.83 亿元\n环比亏损扩大"]
    for xi, v, lb in zip(x2, profits, labels):
        off = 0.08 if v > 0 else -0.08
        va = "bottom" if v > 0 else "top"
        ax2.text(xi, v + off, lb, ha="center", va=va, fontsize=11.5,
                 color=DARK, weight="bold", linespacing=1.5)

    ax2.set_xticks(x2)
    ax2.set_xticklabels(segs, fontsize=10.8, linespacing=1.4)
    ax2.set_ylim(-1.5, 1.95)
    ax2.set_ylabel("分部经营利润（亿元）", fontsize=10.5, color=GRAY, labelpad=8)
    clean(ax2, axis="y")
    ax2.set_title("主业赚钱，新业务还在烧钱",
                  fontsize=11.5, color=DARK, loc="left", pad=12)

    note = ("当季营收 10.68 亿元，激光雷达交付 72.97 万台，GAAP 净利润 8079 万元，毛利率 41.0%（上年同期 42.1%）。\n"
            "剔除 2025 年三季度约 1.85 亿元一次性收益后，净利润同比增长 13.7%；营收与出货量则双双低于指引下限。")
    box = dict(boxstyle="round,pad=0.7", facecolor=PALE, edgecolor=LIGHT, linewidth=0.9)
    fig.text(0.045, 0.088, note, fontsize=9.8, color=DARK, ha="left",
             va="center", linespacing=1.9, bbox=box)

    footer(fig, "数据：禾赛科技 2026 年第三季度未经审计财报及财报电话会。GAAP 口径。")
    fig.savefig(OUT + "图3_禾赛增收不增利.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")
