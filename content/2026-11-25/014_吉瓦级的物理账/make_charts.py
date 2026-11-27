# -*- coding: utf-8 -*-
"""
《吉瓦之后：算力建设的瓶颈，从机房挪到了变电站》配套图表

事实口径（新华网 2026-11-06 演讲全文）：
  · 算力网三个从……到……：IDC 到 AIDC、CPU 到 GPU、云资源池到 Token 工厂。
  · "在建成多个万卡智算集群的基础上，正在布局建设多个超大规模智算集群，
    未来两年智算能力将连续翻番，建成多个吉瓦级智算园区。"
  · 连算成网：400G OTN、空芯光纤、CDN 扩容升级；算网大脑、算力并网、一体调度。
  · 共创：AIDC 全栈解决方案、共建定制化吉瓦级智算园区、卡间机间互联、
    源网荷储、绿电直连、风液同源 → 算电协同、算水协同；
    联建算力专网，支撑客户化 Token 工厂部署；升级移动云。
  · 2027 年：加大算力投资、确保智算能力倍增。
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
    """从机柜到瓦特"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "计量单位换了，选址逻辑也就换了",
           "IDC 与 AIDC 考核的不是同一件事")

    left = [
        ("IDC", "存数据的机房", GRAY),
        ("机柜出租率", "空间卖出去多少", GRAY),
        ("PUE", "电用得多不多", GRAY),
        ("上架率", "装机装得多满", GRAY),
    ]
    right = [
        ("AIDC", "产算力的车间", RED),
        ("吉瓦级", "要吃多少电", RED),
        ("电够不够", "选址第一问", RED),
        ("水冷不冷得下来", "散热是第一约束", RED),
    ]

    x1, x2 = 0.048, 0.522
    w = 0.430

    ax.text(x1, 0.762, "过去看", fontsize=9.6, color=GRAY, ha="left",
            va="center")
    ax.plot([x1, x1 + w], [0.742, 0.742], color=LIGHT, linewidth=1.0)
    ax.text(x2, 0.762, "现在看", fontsize=9.6, color=RED, ha="left",
            va="center")
    ax.plot([x2, x2 + w], [0.742, 0.742], color=LIGHT, linewidth=1.0)

    y = 0.672
    for i in range(4):
        lk, lv, lc = left[i]
        rk, rv, rc = right[i]
        ax.text(x1, y, lk, fontsize=9.6, color=DARK, weight="bold",
                ha="left", va="center")
        ax.text(x1, y - 0.036, lv, fontsize=8.4, color=SLATE,
                ha="left", va="center")
        ax.text(x2, y, rk, fontsize=9.6, color=DARK, weight="bold",
                ha="left", va="center")
        ax.text(x2, y - 0.036, rv, fontsize=8.4, color=SLATE,
                ha="left", va="center")
        y -= 0.102

    card(ax, 0.048, 0.148, 0.904, 0.092, NAVY, face=PALE, lw=1.2)
    ax.text(0.070, 0.208,
            "演讲原话：未来两年智算能力将连续翻番，建成多个吉瓦级智算园区。",
            fontsize=9.4, color=DARK, ha="left", va="center", zorder=6)
    ax.text(0.070, 0.172,
            "吉瓦是功率单位，不是算力单位——它说的是要吃多少电。",
            fontsize=9.0, color=SLATE, ha="left", va="center", zorder=6)

    punchline(fig, "算力越集中，选址的第一个问题就越像电厂而不是机房。")
    footer(fig, "事实来源：新华网 2026-11-06 陈忠岳《网络强基 智能共创》演讲全文")
    fig.savefig(OUT + "图1_从机柜到瓦特.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """三笔物理账"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "三项技术，算的是三笔物理账",
           "演讲原文并列给出：源网荷储、绿电直连、风液同源")

    items = [
        ("源网荷储", "电", "电源、电网、负荷、储能统筹", NAVY, 0.048),
        ("绿电直连", "碳", "风电光伏直接接到园区", TEAL, 0.368),
        ("风液同源", "热", "风冷与液冷共用一套冷源", RED, 0.688),
    ]
    for name, tag, desc, color, x in items:
        card(ax, x, 0.430, 0.258, 0.270, color, lw=1.5)
        ax.text(x + 0.020, 0.650, tag, fontsize=22, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(x + 0.020, 0.560, name, fontsize=11.4, color=DARK,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(x + 0.020, 0.482, desc, fontsize=8.2, color=SLATE,
                ha="left", va="center", zorder=6, linespacing=1.7)

    ax.add_patch(FancyArrowPatch((0.048, 0.392), (0.952, 0.392),
                                 arrowstyle="-|>", mutation_scale=16,
                                 color=GRAY, linewidth=1.3, zorder=5))
    ax.text(0.500, 0.360, "算电协同　＋　算水协同", fontsize=11.0,
            color=DARK, weight="bold", ha="center", va="center")

    ax.text(0.048, 0.306,
            "三个词连起来看，指向同一件事：算力的成本结构里，电和水的权重在上升。",
            fontsize=9.4, color=SLATE, ha="left", va="center")
    ax.text(0.048, 0.266,
            "过去主要算设备折旧和带宽，现在要算电价曲线、绿电可得性、水资源约束。",
            fontsize=9.4, color=SLATE, ha="left", va="center")

    card(ax, 0.048, 0.148, 0.904, 0.078, LIGHT, face=PALE, lw=1.0)
    ax.text(0.070, 0.200,
            "演讲还提到「共建定制化吉瓦级智算园区」——单个园区的投入规模，已不是一方能独立消化。",
            fontsize=9.2, color=DARK, ha="left", va="center", zorder=6)
    ax.text(0.070, 0.166, "注意「定制化」和「共建」这两个限定词。",
            fontsize=8.8, color=SLATE, ha="left", va="center", zorder=6)

    punchline(fig, "算力的账本上，多了电和水两个科目。")
    footer(fig, "事实来源：新华网 2026-11-06 演讲全文；三项技术的解释为通用含义说明")
    fig.savefig(OUT + "图2_三笔物理账.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """从卖资源到卖产出"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "投入侧换了单位，产出侧也换了",
           "从云资源池到 Token 工厂")

    # 两个模式对比
    card(ax, 0.048, 0.440, 0.430, 0.280, SLATE, lw=1.4)
    ax.text(0.072, 0.672, "云资源池", fontsize=13.0, color=SLATE,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.072, 0.616, "卖的是资源", fontsize=9.4, color=DARK,
            ha="left", va="center", zorder=6)
    rows_l = ["vCPU / 内存 / 存储", "按月或按小时计价", "利用率风险在买方"]
    y = 0.560
    for r in rows_l:
        ax.text(0.072, y, "· " + r, fontsize=8.8, color=SLATE,
                ha="left", va="center", zorder=6)
        y -= 0.042

    card(ax, 0.522, 0.440, 0.430, 0.280, RED, lw=1.4)
    ax.text(0.546, 0.672, "Token 工厂", fontsize=13.0, color=RED,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.546, 0.616, "卖的是产出", fontsize=9.4, color=DARK,
            ha="left", va="center", zorder=6)
    rows_r = ["按词元计价", "用户不关心底下几张卡", "效率风险在卖方"]
    y = 0.560
    for r in rows_r:
        ax.text(0.546, y, "· " + r, fontsize=8.8, color=SLATE,
                ha="left", va="center", zorder=6)
        y -= 0.042

    ax.text(0.048, 0.396, "两个前提，缺一不可", fontsize=10.0, color=GRAY,
            ha="left", va="center")
    ax.plot([0.048, 0.952], [0.378, 0.378], color=LIGHT, linewidth=1.0)

    rows2 = [
        ("算力并网、一体调度", "算力是散的、调度不通，就保证不了词元的稳定供给与成本"),
        ("客户化 Token 工厂", "不同客户要的模型、时延、精度不同，工厂得能按单改产线"),
    ]
    y = 0.344
    for k, v in rows2:
        ax.text(0.048, y, k, fontsize=9.4, color=RED, weight="bold",
                ha="left", va="center")
        ax.text(0.300, y, v, fontsize=8.6, color=SLATE,
                ha="left", va="center")
        y -= 0.062

    card(ax, 0.048, 0.148, 0.904, 0.070, NAVY, face=PALE, lw=1.2)
    ax.text(0.070, 0.183,
            "要按词元卖，就必须把整条链路的效率做到足够高，否则单价压不下来。",
            fontsize=9.4, color=DARK, ha="left", va="center", zorder=6)

    punchline(fig, "卖资源，风险在买方；卖词元，风险回到自己身上。")
    footer(fig, "事实来源：新华网 2026-11-06 演讲全文（云资源池到 Token 工厂、"
                "算网大脑、算力专网）")
    fig.savefig(OUT + "图3_从卖资源到卖产出.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)
