# -*- coding: utf-8 -*-
"""
《网络也能被"调用"：从修好给人用，到开放给程序用》配套图表

事实口径（新华网 2026-11-06 演讲全文）：
  · 通信网三个从……到……：人人通信到人机交互、地面覆盖到空天地海、
    尽力而为到确定保障。
  · "开放移动网络，让应用开发者便捷调用通信能力。"
  · 12580 智能助理：10 亿多手机客户、3 亿多家庭客户。
  · IPv6 全栈通用路由协议：全球互联网根技术，300 多家运营商规模部署，
    促进互联网传送效率提升 25% 以上。
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch

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
TEAL = "#3f6f6b"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep

Y_TITLE = 0.958
Y_SUB = 0.898
Y_PUNCH = 0.070
Y_FOOT = 0.020


def header(fig, title, sub):
    fig.text(0.045, Y_TITLE, title, fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, Y_SUB, sub, fontsize=10.6, color=GRAY,
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
    """三种交付方式"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "一张网的三代交付方式",
           "从自己用，到租给别人，到开放给程序调用")

    items = [
        ("第一代", "自用", "卖连接", "用户按月付流量费\n网络指标是内部考核", GRAY),
        ("第二代", "出租", "卖带宽", "按带宽/专线计价\n承诺写入合同", SLATE),
        ("第三代", "调用", "卖能力", "开发者调用接口\n程序直接使用网络", RED),
    ]

    x = 0.048
    w = 0.278
    gap = 0.020
    for gen, name, sell, desc, color in items:
        card(ax, x, 0.380, w, 0.320, color, lw=1.5)
        ax.text(x + w / 2, 0.664, gen, fontsize=9.0, color=GRAY,
                ha="center", va="center", zorder=6)
        ax.text(x + w / 2, 0.606, name, fontsize=17, color=color,
                weight="bold", ha="center", va="center", zorder=6)
        ax.text(x + w / 2, 0.540, sell, fontsize=10.0, color=DARK,
                ha="center", va="center", zorder=6)
        ax.plot([x + 0.030, x + w - 0.030], [0.508, 0.508],
                color=LIGHT, linewidth=1.0, zorder=6)
        ax.text(x + w / 2, 0.446, desc, fontsize=8.4, color=SLATE,
                ha="center", va="center", zorder=6, linespacing=1.8)
        x += w + gap

    ax.text(0.048, 0.318, "差别不在带宽大小，在于「谁在用」和「要不要给承诺」。",
            fontsize=9.8, color=DARK, ha="left", va="center")

    card(ax, 0.048, 0.148, 0.904, 0.086, NAVY, face=PALE, lw=1.2)
    ax.text(0.070, 0.202,
            "演讲原话：开放移动网络，让应用开发者便捷调用通信能力。",
            fontsize=9.6, color=DARK, ha="left", va="center", zorder=6)
    ax.text(0.070, 0.168,
            "这不是多开一个入口，是把网络从「服务」变成「产品」。",
            fontsize=9.0, color=SLATE, ha="left", va="center", zorder=6)

    punchline(fig, "使用者从人变成程序，要求就从「尽力而为」变成「说到做到」。")
    footer(fig, "事实来源：新华网 2026-11-06 陈忠岳《网络强基 智能共创》演讲全文")
    fig.savefig(OUT + "图1_三种交付.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """两端同一底座"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "两端，同一个底座",
           "一端是开发者，一端是十亿级用户")

    # 上：两端
    card(ax, 0.048, 0.520, 0.430, 0.190, SLATE, lw=1.3)
    ax.text(0.072, 0.664, "应用开发者", fontsize=12.0, color=SLATE,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.072, 0.612, "调用通信能力", fontsize=9.6, color=DARK,
            ha="left", va="center", zorder=6)
    ax.text(0.072, 0.564, "要的是可承诺时延、可计量指标", fontsize=8.6,
            color=SLATE, ha="left", va="center", zorder=6)

    card(ax, 0.522, 0.520, 0.430, 0.190, RED, lw=1.3)
    ax.text(0.546, 0.664, "10 亿多手机 + 3 亿多家庭", fontsize=12.0,
            color=RED, weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.546, 0.612, "12580 智能助理", fontsize=9.6, color=DARK,
            ha="left", va="center", zorder=6)
    ax.text(0.546, 0.564, "要的是不中断的连接、稳定上行", fontsize=8.6,
            color=SLATE, ha="left", va="center", zorder=6)

    # 中间箭头
    for cx in (0.263, 0.737):
        ax.add_patch(FancyArrowPatch((cx, 0.508), (cx, 0.452),
                                     arrowstyle="-|>", mutation_scale=16,
                                     color=GRAY, linewidth=1.4, zorder=5))
    ax.text(0.500, 0.480, "共用同一个前提", fontsize=9.4, color=GRAY,
            ha="center", va="center")

    # 下：底座
    card(ax, 0.048, 0.300, 0.904, 0.130, NAVY, lw=1.6)
    ax.text(0.500, 0.386, "从尽力而为到确定保障", fontsize=15.0,
            color=NAVY, weight="bold", ha="center", va="center", zorder=6)
    ax.text(0.500, 0.335,
            "没有这一条，开发者调不动，十亿人的助手也稳不住",
            fontsize=9.4, color=SLATE, ha="center", va="center", zorder=6)

    ax.text(0.048, 0.248,
            "另外两个「从……到……」讲的是连接对象和覆盖范围；这一个讲的是质量承诺的方式。",
            fontsize=9.2, color=SLATE, ha="left", va="center")

    punchline(fig, "对开发者开放和对十亿用户交付，看起来是两端，其实是同一件事。")
    footer(fig, "事实来源：新华网 2026-11-06 演讲全文（12580 智能助理、开放移动网络、三个从……到……）")
    fig.savefig(OUT + "图2_两端同一底座.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """路由是底座"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "为什么一家运营商要去做根技术",
           "IPv6 全栈通用路由协议：底下的东西决定了上层能跑多快")

    stats = [
        ("300 多家", "国内外运营商规模部署", NAVY, 0.048),
        ("25% 以上", "互联网传送效率提升", RED, 0.368),
        ("根技术", "全球互联网基础设施层级", TEAL, 0.688),
    ]
    for big, label, color, x in stats:
        card(ax, x, 0.470, 0.258, 0.230, color, lw=1.5)
        ax.text(x + 0.020, 0.640, big, fontsize=20, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(x + 0.020, 0.552, label, fontsize=8.8, color=SLATE,
                ha="left", va="center", zorder=6)

    ax.text(0.048, 0.410, "三个动作的顺序不能倒过来", fontsize=10.0,
            color=GRAY, ha="left", va="center")
    ax.plot([0.048, 0.952], [0.392, 0.392], color=LIGHT, linewidth=1.0)

    rows = [
        ("先有路由", "搭建全新的网络路由"),
        ("才谈分工", "通信网匹配智算方向、算力网供给词元调用、智能网满足服务需求"),
    ]
    y = 0.356
    for k, v in rows:
        ax.text(0.048, y, k, fontsize=9.6, color=RED, weight="bold",
                ha="left", va="center")
        ax.text(0.200, y, v, fontsize=9.0, color=SLATE,
                ha="left", va="center")
        y -= 0.062

    card(ax, 0.048, 0.148, 0.904, 0.086, LIGHT, face=PALE, lw=1.0)
    ax.text(0.070, 0.202,
            "接口再漂亮，如果底层路由在别人的框架里，效率损耗和适配成本就压不下去。",
            fontsize=9.4, color=DARK, ha="left", va="center", zorder=6)
    ax.text(0.070, 0.168,
            "这是「开放网络能力」这条路线真正的底座。",
            fontsize=9.0, color=SLATE, ha="left", va="center", zorder=6)

    punchline(fig, "路由是那种平时看不见、但决定了上层能跑多快的东西。")
    footer(fig, "事实来源：新华网 2026-11-06 演讲全文（IPv6 全栈通用路由协议、300 多家运营商、25% 以上）")
    fig.savefig(OUT + "图3_路由是底座.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)
