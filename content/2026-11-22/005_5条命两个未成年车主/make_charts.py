# -*- coding: utf-8 -*-
"""
《5条命，两个不满16岁的车主：不追刑责，追谁》配套图表

事实口径（核到郑州消防调查报告发布内容及新华社、澎湃、新浪财经转应急管理部报道）：
  · 2026-07-06 07:51，郑州惠济区和昌珑悦小区 A 座 628 室起火，
    过火面积约 15 平方米，5 人死亡、1 人受伤，直接经济损失 530.75 万元。
  · 起火原因：628 室内电动摩托车经改装的三元锂电池充电热失控后爆燃。
  · 蔓延扩大原因：房门敞开致烟气扩散；起火楼层自动喷水灭火系统管道无水。
  · 车辆 2025 年由刘某亮买给儿子刘某鸣（当年 12 岁），刘某鸣在邓某昊
    经营的改装店“陆续”改装，四次转卖后于 2026-06-14 到代某辉（15 岁）手中。
  · 处理建议：酒店和物业相关负责人、改装店店主及店员涉嫌刑事犯罪；
    刘某鸣（不满 14 岁）、代某辉（不满 16 岁）涉嫌失火罪，建议不追刑责。
  · 法律依据：《中华人民共和国刑法》第十七条。

输出目录 = 脚本所在目录
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei"]
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
TEAL = "#3f6f6b"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep

Y_TITLE = 0.958
Y_SUB = 0.898
Y_PUNCH = 0.068
Y_FOOT = 0.020


def header(fig, title, sub):
    fig.text(0.045, Y_TITLE, title, fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, Y_SUB, sub, fontsize=10.4, color=GRAY,
             ha="left", va="top")


def footer(fig, text):
    fig.text(0.045, Y_FOOT, text, fontsize=7.6, color=GRAY,
             ha="left", va="bottom")


def punchline(fig, text):
    fig.text(0.045, Y_PUNCH, text, fontsize=10.4, color=DARK,
             ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


def card(ax, x, y, w, h, edge, face="white", lw=1.0, z=2):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.004,rounding_size=0.014",
        facecolor=face, edgecolor=edge, linewidth=lw, zorder=z))


def new_axes(fig):
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return ax


# ---------------------------------------------------------------- 图 1
def fig1():
    """三个数字：15 平方米、5 人、530.75 万元"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "15 平方米，5 条命",
           "2026 年 7 月 6 日，郑州惠济区和昌珑悦小区 A 座 628 室；11 月 20 日晚调查报告公布")

    stats = [
        ("15", "平方米 · 过火面积", NAVY),
        ("5", "人遇难 · 另有 1 人受伤", RED),
        ("530.75", "万元 · 直接经济损失", NAVY),
    ]
    y = 0.630
    for num, desc, color in stats:
        ax.text(0.048, y, num, fontsize=34, color=color, weight="bold",
                ha="left", va="center")
        ax.text(0.048, y - 0.062, desc, fontsize=9.6, color=SLATE,
                ha="left", va="center")
        y -= 0.160

    card(ax, 0.585, 0.315, 0.370, 0.360, NAVY, lw=1.3)
    ax.text(0.607, 0.638, "起火", fontsize=10.8, color=NAVY, weight="bold",
            ha="left", va="center", zorder=6)
    ax.plot([0.607, 0.933], [0.614, 0.614], color=NAVY, linewidth=0.9,
            alpha=0.35, zorder=5)
    ax.text(0.607, 0.585,
            "电动摩托车\n\n非法改装 · 进楼入户充电\n\n三元锂电池热失控 → 爆燃",
            fontsize=9.2, color=DARK, ha="left", va="top",
            linespacing=1.6, zorder=6)

    ax.text(0.048, 0.185,
            "628 室 2 人、621 室 3 人遇难；烟气经敞开的房门蔓延至 6 层走廊。",
            fontsize=9.0, color=SLATE, ha="left", va="center")

    punchline(fig, "火只烧了 15 平方米，5 个人遇难。")
    footer(fig, "事实来源：郑州消防《郑州市惠济区和昌珑悦小区“7·6”较大火灾事故调查报告》"
                "（2026-11-20 发布）；澎湃新闻 2026-11-21；新浪财经转中国应急管理 2026-11-22")
    fig.savefig(OUT + "图1_三个数字.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """从 12 岁车主到 628 房间的责任链"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "一条链上，谁被追，谁没被追",
           "从车买回家，到 628 室爆燃，隔了一年多；从住进酒店到起火，隔了一夜")

    steps = [
        ("2025 年", "买给 12 岁儿子"),
        ("改装店", "“陆续”改装"),
        ("四次转卖", "前后五个车主"),
        ("2026-06-14", "到 15 岁车主"),
        ("7 月 5 日", "冒名住进 628"),
        ("7 月 6 日", "推车充电，爆燃"),
    ]
    w, h, gap = 0.134, 0.150, 0.018
    x = 0.045
    cy = 0.560
    for i, (title, body) in enumerate(steps):
        card(ax, x, cy, w, h, NAVY, lw=1.1)
        ax.text(x + 0.013, cy + 0.108, title, fontsize=8.2, color=NAVY,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(x + 0.013, cy + 0.052, body, fontsize=8.0, color=DARK,
                ha="left", va="center", zorder=6, wrap=False)
        if i < len(steps) - 1:
            ax.annotate("", xy=(x + w + gap - 0.002, cy + h / 2),
                        xytext=(x + w + 0.002, cy + h / 2),
                        arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=1.1))
        x += w + gap

    # 被追
    card(ax, 0.045, 0.235, 0.435, 0.205, RED, lw=1.4)
    ax.text(0.065, 0.402, "被追", fontsize=11.0, color=RED, weight="bold",
            ha="left", va="center", zorder=6)
    ax.text(0.065, 0.352,
            "改装店店主及店员\n酒店、小区物业相关负责人\n涉嫌刑事犯罪",
            fontsize=9.0, color=DARK, ha="left", va="top",
            linespacing=1.55, zorder=6)

    # 没被追
    card(ax, 0.520, 0.235, 0.435, 0.205, GRAY, lw=1.4)
    ax.text(0.540, 0.402, "没被追", fontsize=11.0, color=SLATE, weight="bold",
            ha="left", va="center", zorder=6)
    ax.text(0.540, 0.352,
            "刘某鸣（不满 14 岁）\n代某辉（15 岁）\n失火罪，依法不追",
            fontsize=9.0, color=DARK, ha="left", va="top",
            linespacing=1.55, zorder=6)

    ax.text(0.045, 0.170,
            "报告同时建议：惠济区委、区政府向市委、市政府作深刻检查。",
            fontsize=8.8, color=GRAY, ha="left", va="center")

    punchline(fig, "不追车主，不等于没人负责。")
    footer(fig, "事实来源：郑州消防调查报告（2026-11-20）；澎湃新闻 2026-11-21；"
                "新浪财经转中国应急管理 2026-11-22")
    fig.savefig(OUT + "图2_责任链.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """刑法第十七条：失火罪的责任年龄线"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "失火罪这条线，画在 16 岁",
           "《中华人民共和国刑法》第十七条；两名车主分别不满 14 岁、15 岁")

    x12, x14, x16, x18 = 0.10, 0.3667, 0.6333, 0.90
    y0, h = 0.400, 0.110

    zones = [
        (x12, x14, "#e8eaed", GRAY, "不满 14 岁", "不负刑事责任"),
        (x14, x16, "#f3e3e0", RED, "14—16 岁", "仅对八类罪负责"),
        (x16, x18, "#e3e8ef", NAVY, "16 岁及以上", "应当负刑事责任"),
    ]
    for xa, xb, face, edge, title, note in zones:
        ax.add_patch(Rectangle((xa, y0), xb - xa, h, facecolor=face,
                               edgecolor=edge, linewidth=1.0, zorder=3))
        ax.text((xa + xb) / 2, y0 + h - 0.028, title, fontsize=10.2,
                color=edge, weight="bold", ha="center", va="center", zorder=5)
        ax.text((xa + xb) / 2, y0 + 0.025, note, fontsize=8.8,
                color=DARK, ha="center", va="center", zorder=5)

    ax.text(x12 - 0.012, y0 - 0.030, "12 岁", fontsize=8.4, color=GRAY,
            ha="center", va="center")
    ax.text(x14, y0 - 0.030, "14 岁", fontsize=8.4, color=GRAY,
            ha="center", va="center")
    ax.text(x16, y0 - 0.030, "16 岁", fontsize=8.4, color=GRAY,
            ha="center", va="center")
    ax.text(x18 + 0.012, y0 - 0.030, "18 岁", fontsize=8.4, color=GRAY,
            ha="center", va="center")

    # 两个车主的位置
    def year_x(year):
        return x12 + (year - 12) * (x18 - x12) / 6.0

    ax.plot([year_x(13)], [y0 + h / 2], marker="o", markersize=8,
            color=DARK, zorder=6)
    ax.text(year_x(13), 0.528, "刘某鸣 13 岁", fontsize=8.6,
            color=DARK, ha="center", va="bottom", zorder=6)

    ax.plot([year_x(15)], [y0 + h / 2], marker="o", markersize=8,
            color=RED, zorder=6)
    ax.text(year_x(15), 0.528, "代某辉 15 岁", fontsize=8.6,
            color=RED, ha="center", va="bottom", zorder=6)

    ax.annotate("失火罪不在八类罪里",
                xy=(0.600, y0 + h + 0.004), xytext=(0.655, 0.565),
                fontsize=8.8, color=RED, ha="left", va="center",
                arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.0))

    ax.text(0.048, 0.295,
            "不满 14 周岁原则上不负刑责；12—14 周岁仅故意杀人、故意伤害致死等",
            fontsize=8.6, color=SLATE, ha="left", va="center")
    ax.text(0.048, 0.255,
            "极少数情形，经最高人民检察院核准追诉。",
            fontsize=8.6, color=SLATE, ha="left", va="center")
    ax.text(0.048, 0.205,
            "因不满 16 周岁不予刑事处罚的，责令父母或其他监护人管教；必要时专门矫治教育。",
            fontsize=9.0, color=DARK, ha="left", va="center")

    punchline(fig, "不追，是法律写好的结果，不是谁的手下留情。")
    footer(fig, "事实来源：《中华人民共和国刑法》第十七条；郑州消防调查报告（2026-11-20）")
    fig.savefig(OUT + "图3_年龄线.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)