# -*- coding: utf-8 -*-
"""
《算力不按卡时卖，改按词元卖》配套图表

事实口径：
  · 2026-11-20，华为主办的“数智引领 苏智跃升——华为中国行 2026·江苏算力
    产业及应用生态会议”在南京举行。
  · 会上发布江苏首批 5 个昇腾 AI“词元工厂”：徐州人工智能公共服务平台、
    苏州工业园区数字政府智算资源服务平台、南通人工智能及数据要素协同创新基地、
    盐城超级计算中心、宿迁市数智新城算力底座。
  · 官方定义：词元工厂是 AI 时代的新型基础设施，通过五层技术架构与推理调度
    方案优化调度、大幅提升算力利用率，推动算力模式从售卖“卡时”转向输出
    “词元”产能，形成建设—运营—迭代的循环；本地算力供给从“按卡计费”走向
    “按词售卖”，服务颗粒度更贴近大模型推理与智能体应用的实际需求。
  · 五个工厂覆盖公共服务、数字政府、数据要素协同、超算、数智新城五类场景。
  · 同场启动“江苏鲲鹏昇腾新质生产力优秀实践联盟”，展出昇腾 950 超节点。

输出目录 = 脚本所在目录
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

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


def card(ax, x, y, w, h, edge, face="white", lw=1.2, z=2):
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
    """卡时 vs 词元：换的是计费单位"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "换的不是设备，是计费单位",
           "同一个机柜，按“卡时”卖和按“词元”卖，买方承担的东西不一样")

    card(ax, 0.045, 0.470, 0.410, 0.305, SLATE, lw=1.5)
    ax.text(0.072, 0.738, "按卡时", fontsize=14.0, color=SLATE,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.072, 0.703, "卖的是硬件占用时间", fontsize=9.0, color=GRAY,
            ha="left", va="center", zorder=6)
    ax.text(0.072, 0.658,
            "买什么：一块卡、一小时\n"
            "风险在谁：买方。卡空转也照付\n"
            "比价看什么：卡型、台数、单价\n"
            "适合谁：自己会调度的团队",
            fontsize=9.6, color=SLATE, ha="left", va="top",
            linespacing=1.95, zorder=6)

    card(ax, 0.545, 0.470, 0.410, 0.305, NAVY, lw=1.5)
    ax.text(0.572, 0.738, "按词元", fontsize=14.0, color=NAVY,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.572, 0.703, "卖的是实际产出的调用量", fontsize=9.0, color=GRAY,
            ha="left", va="center", zorder=6)
    ax.text(0.572, 0.658,
            "买什么：一个词元的输出\n"
            "风险在谁：卖方。调度不上就白搭\n"
            "比价看什么：同样芯片能出多少有效词元\n"
            "适合谁：直接用推理和智能体的客户",
            fontsize=9.6, color=SLATE, ha="left", va="top",
            linespacing=1.95, zorder=6)

    ax.add_patch(FancyArrowPatch((0.470, 0.620), (0.530, 0.620),
                                 arrowstyle="-|>", mutation_scale=18,
                                 color=RED, lw=2.0))

    card(ax, 0.045, 0.205, 0.910, 0.110, LIGHT, face=PALE, lw=1.0)
    ax.text(0.070, 0.260,
            "切换的实质：把“硬件占用”的成本风险，从买方挪到卖方身上——谁卖算力，谁就得证明自己调得动。",
            fontsize=9.6, color=DARK, ha="left", va="center", zorder=6)

    punchline(fig, "卡时卖的是资源，词元卖的是结果。")
    footer(fig, "事实来源：2026-11-20 华为中国行 2026·江苏算力产业及应用生态会议（经新华日报、"
                "人民网江苏、江苏省数据局转述）")
    fig.savefig(OUT + "图1_换的是计费单位.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """五个词元工厂，五类场景"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "首批 5 个，落在 5 类场景",
           "2026 年 11 月 20 日，南京，江苏首批昇腾 AI 词元工厂")

    rows = [
        ("徐州", "人工智能公共服务平台", "公共服务"),
        ("苏州工业园区", "数字政府智算资源服务平台", "数字政府"),
        ("南通", "人工智能及数据要素协同创新基地", "数据要素"),
        ("盐城", "超级计算中心", "超算"),
        ("宿迁", "数智新城算力底座", "数智新城"),
    ]

    y = 0.700
    for city, name, tag in rows:
        card(ax, 0.045, y, 0.910, 0.084, LIGHT, lw=1.1)
        ax.text(0.070, y + 0.042, city, fontsize=10.6, color=DARK,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(0.255, y + 0.042, name, fontsize=9.6, color=SLATE,
                ha="left", va="center", zorder=6)
        card(ax, 0.808, y + 0.021, 0.122, 0.042, NAVY, face=PALE, lw=1.0)
        ax.text(0.869, y + 0.042, tag, fontsize=8.6, color=NAVY,
                ha="center", va="center", zorder=8)
        y -= 0.098

    ax.text(0.045, 0.222,
            "五层技术架构 + 推理调度方案是共同底座：先提高利用率，再把省下来的算力按词元卖出去。",
            fontsize=9.4, color=SLATE, ha="left", va="center")
    ax.text(0.045, 0.178,
            "同场还启动了“江苏鲲鹏昇腾新质生产力优秀实践联盟”，并展出昇腾 950 超节点。",
            fontsize=9.0, color=GRAY, ha="left", va="center")

    punchline(fig, "规模不大，但计费口径换了。")
    footer(fig, "事实来源：新华日报·交汇点 2026-11-21；人民网江苏 2026-11-22；"
                "江苏省数据局 2026-11-22")
    fig.savefig(OUT + "图2_五个词元工厂.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """三方影响 + 新比价指标"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "同一块芯片，要证明能出多少词元",
           "计价颗粒度变细之后，三方的账都跟着改")

    cols = [
        ("云厂商与运营方", "调度能力变成核心竞争力。\n利用率上不去，卖词元就\n是在替客户兜底。", NAVY),
        ("模型公司", "推理成本从“租了几台卡”\n变成“每千词元多少钱”，\n预算更好做，也更好比价。", TEAL),
        ("应用开发者", "不必再为闲置算力付费，\n按实际调用量结算，\n试错门槛下降。", RED),
    ]
    x = 0.045
    w = 0.288
    for title, note, color in cols:
        card(ax, x, 0.420, w, 0.310, color, lw=1.5)
        ax.text(x + 0.022, 0.678, title, fontsize=10.6, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(x + 0.022, 0.625, note, fontsize=9.2, color=SLATE,
                ha="left", va="top", linespacing=1.95, zorder=6)
        x += w + 0.023

    card(ax, 0.045, 0.235, 0.910, 0.150, RED, face=PALE, lw=1.2)
    ax.text(0.070, 0.345, "新的比价指标：每卡有效词元产出", fontsize=10.8,
            color=RED, weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.070, 0.298,
            "过去比的是卡型和单价，现在要比“同样的卡、同样的时间，谁调出更多可交付的推理量”。"
            "这项指标一旦公开，调度能力差的运营方会被直接比下去。",
            fontsize=9.2, color=SLATE, ha="left", va="top", zorder=6)

    punchline(fig, "硬件在变贵，计价却在向产出靠拢——压力被推给了调度。")
    footer(fig, "事实来源：2026-11-20 江苏算力产业及应用生态会议官方表述（经新华日报、"
                "环球网、凤凰网科技转述）；三方影响为本文分析")
    fig.savefig(OUT + "图3_三方影响.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)