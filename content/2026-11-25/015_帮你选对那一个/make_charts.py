# -*- coding: utf-8 -*-
"""
《模型泛滥之后，最值钱的本事是"帮你选对那一个"》配套图表

事实口径（新华网 2026-11-06 演讲全文）：
  · "中国移动致力于打造智能服务的'交换机''路由器'"。
  · MoMA 模型服务平台：全量接入主流模型，降低 Token 成本、提升使用效能，
    帮客户选择最匹配的模型、让客户享用高可信的服务。
  · 服务矩阵：MobileWork 智能体（赋能工作提效）；咪咕平台升级
    （体育视频、国风音乐、书香阅读）；移动天工平台（客户现场洞察、
    先进制造标杆应用）。
  · 泛全联盟、AI 定制终端、端网业高效协同。
  · 移动生态聚合平台：服务全球合作伙伴的统一入口，
    实现商机与产品、技术与场景、需求与交付、产业与投资的高效对接。
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
    """交换机的角色"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "为什么把自己比作「交换机」",
           "交换机不生产数据，它负责判断东西该往哪走")

    # 左：需求侧
    card(ax, 0.048, 0.500, 0.250, 0.220, SLATE, lw=1.3)
    ax.text(0.072, 0.664, "有需求的", fontsize=10.0, color=SLATE,
            weight="bold", ha="left", va="center", zorder=6)
    rows_l = ["要代码能力", "要长上下文", "要便宜", "要高可信"]
    y = 0.622
    for r in rows_l:
        ax.text(0.072, y, "· " + r, fontsize=8.8, color=DARK,
                ha="left", va="center", zorder=6)
        y -= 0.035

    # 中：MoMA
    card(ax, 0.360, 0.470, 0.280, 0.280, RED, lw=1.8)
    ax.text(0.500, 0.686, "MoMA", fontsize=15.0, color=RED,
            weight="bold", ha="center", va="center", zorder=6)
    ax.text(0.500, 0.624, "模型服务平台", fontsize=9.4, color=DARK,
            ha="center", va="center", zorder=6)
    ax.plot([0.386, 0.614], [0.596, 0.596], color=LIGHT, linewidth=1.0,
            zorder=6)
    mids = ["全量接入主流模型", "统一 Token 计价", "帮客户选最匹配的"]
    y = 0.566
    for m in mids:
        ax.text(0.500, y, m, fontsize=8.4, color=SLATE,
                ha="center", va="center", zorder=6)
        y -= 0.034

    # 右：供给侧
    card(ax, 0.702, 0.500, 0.250, 0.220, NAVY, lw=1.3)
    ax.text(0.726, 0.664, "有能力的", fontsize=10.0, color=NAVY,
            weight="bold", ha="left", va="center", zorder=6)
    rows_r = ["闭源大模型", "开源权重", "小模型", "专用模型"]
    y = 0.622
    for r in rows_r:
        ax.text(0.726, y, "· " + r, fontsize=8.8, color=DARK,
                ha="left", va="center", zorder=6)
        y -= 0.035

    for x0, x1 in ((0.302, 0.356), (0.644, 0.698)):
        ax.add_patch(FancyArrowPatch((x0, 0.610), (x1, 0.610),
                                     arrowstyle="-|>", mutation_scale=15,
                                     color=GRAY, linewidth=1.4, zorder=5))

    ax.text(0.048, 0.418, "选错的代价是具体的", fontsize=10.0, color=GRAY,
            ha="left", va="center")
    ax.plot([0.048, 0.952], [0.400, 0.400], color=LIGHT, linewidth=1.0)

    rows2 = [
        ("贵模型跑简单任务", "成本翻几倍"),
        ("便宜模型跑复杂推理", "效果直接崩"),
        ("不支持长上下文", "文档类任务根本跑不起来"),
    ]
    y = 0.362
    for k, v in rows2:
        ax.text(0.048, y, k, fontsize=9.2, color=DARK,
                ha="left", va="center")
        ax.text(0.380, y, v, fontsize=9.0, color=RED,
                ha="left", va="center")
        y -= 0.056

    card(ax, 0.048, 0.148, 0.904, 0.062, LIGHT, face=PALE, lw=1.0)
    ax.text(0.070, 0.179,
            "交换机让不同速率的端口互通，MoMA 让不同来源的模型互换。",
            fontsize=9.4, color=DARK, ha="left", va="center", zorder=6)

    punchline(fig, "不自己造模型，但负责把对的东西送到对的地方。")
    footer(fig, "事实来源：新华网 2026-11-06 陈忠岳《网络强基 智能共创》演讲全文")
    fig.savefig(OUT + "图1_交换机的角色.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """三类用户三条线"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "三条服务线，对应三类完全不同的用户",
           "从场景到平台、从终端到云端、从应用到模型")

    items = [
        ("MobileWork", "企业办公", "高频、轻量、单次价值不高\n但累积占掉大量时间",
         "替代重复动作\n不是替代判断", RED, 0.048),
        ("咪咕", "普通消费者", "体育视频、国风音乐、书香阅读\n都是内容形态",
         "落点不是给你助手\n是让你看的东西更好", TEAL, 0.368),
        ("移动天工", "制造业现场", "加强客户现场洞察\n推动数智赋能与场景适配",
         "工业场景没有通用解\n必须一家家看产线", NAVY, 0.688),
    ]
    for name, who, desc, note, color, x in items:
        card(ax, x, 0.330, 0.258, 0.390, color, lw=1.5)
        ax.text(x + 0.018, 0.686, name, fontsize=11.6, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(x + 0.018, 0.634, who, fontsize=9.4, color=DARK,
                ha="left", va="center", zorder=6)
        ax.plot([x + 0.018, x + 0.240], [0.608, 0.608], color=LIGHT,
                linewidth=1.0, zorder=6)
        ax.text(x + 0.018, 0.546, desc, fontsize=8.2, color=SLATE,
                ha="left", va="center", zorder=6, linespacing=1.8)
        ax.text(x + 0.018, 0.410, note, fontsize=8.2, color=color,
                ha="left", va="center", zorder=6, linespacing=1.8)

    ax.text(0.048, 0.276,
            "先有场景，才有平台；需求从应用倒推，而不是从模型正推。",
            fontsize=9.6, color=DARK, ha="left", va="center")

    card(ax, 0.048, 0.148, 0.904, 0.070, LIGHT, face=PALE, lw=1.0)
    ax.text(0.070, 0.183,
            "演讲原话：支撑从场景到平台、从终端到云端、从应用到模型的全链条智能服务。",
            fontsize=9.0, color=SLATE, ha="left", va="center", zorder=6)

    punchline(fig, "同一个「智能」，落到三类人身上是三件不同的事。")
    footer(fig, "事实来源：新华网 2026-11-06 演讲全文（移动智能服务矩阵）")
    fig.savefig(OUT + "图2_三类用户三条线.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """四组配对"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "一个新的统一入口，撮合四组配对",
           "移动生态聚合平台：每一组左边是需求，右边是能力")

    pairs = [
        ("商机", "产品"),
        ("技术", "场景"),
        ("需求", "交付"),
        ("产业", "投资"),
    ]

    y = 0.640
    for a, b in pairs:
        card(ax, 0.120, y - 0.030, 0.240, 0.060, SLATE, lw=1.2)
        ax.text(0.240, y, a, fontsize=10.4, color=DARK, weight="bold",
                ha="center", va="center", zorder=6)
        ax.add_patch(FancyArrowPatch((0.372, y), (0.436, y),
                                     arrowstyle="-|>", mutation_scale=14,
                                     color=GRAY, linewidth=1.4, zorder=5))
        card(ax, 0.448, y - 0.030, 0.240, 0.060, NAVY, lw=1.2)
        ax.text(0.568, y, b, fontsize=10.4, color=DARK, weight="bold",
                ha="center", va="center", zorder=6)
        ax.text(0.706, y, "高效对接", fontsize=8.6, color=RED,
                ha="left", va="center", zorder=6)
        y -= 0.090

    ax.text(0.120, 0.716, "有需求的", fontsize=9.0, color=GRAY,
            ha="center", va="center")
    ax.text(0.568, 0.716, "有能力的", fontsize=9.0, color=GRAY,
            ha="center", va="center")

    ax.text(0.120, 0.262, "MoMA 撮合的是", fontsize=9.4, color=DARK,
            ha="left", va="center")
    ax.text(0.120, 0.222, "要什么效果 → 哪个模型能给", fontsize=9.0,
            color=SLATE, ha="left", va="center")
    ax.text(0.560, 0.262, "生态平台撮合的是", fontsize=9.4, color=DARK,
            ha="left", va="center")
    ax.text(0.560, 0.222, "谁有需求 → 谁能交付", fontsize=9.0,
            color=SLATE, ha="left", va="center")

    card(ax, 0.048, 0.132, 0.904, 0.052, LIGHT, face=PALE, lw=1.0)
    ax.text(0.070, 0.158,
            "同一个思路，只是层次不同：一个撮合模型，一个撮合伙伴。",
            fontsize=9.0, color=SLATE, ha="left", va="center", zorder=6)

    punchline(fig, "供给充裕之后，中间那个「撮合的位置」反而变得更值钱。")
    footer(fig, "事实来源：新华网 2026-11-06 演讲全文（移动生态聚合平台、MoMA 模型服务平台）")
    fig.savefig(OUT + "图3_四组配对.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)


