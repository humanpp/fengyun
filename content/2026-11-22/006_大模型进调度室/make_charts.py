# -*- coding: utf-8 -*-
"""
《大模型不进聊天框，进调度室》配套图表

事实口径（核到科技日报、新京报、科创板日报、财联社）：
  · 2026-11-21，南水北调“天河”大模型 V2 在北京第三届国家水网论坛发布；
    接入遥感卫星 27 颗、气象雷达 237 部；防汛形势分析由小时级压缩至分钟级；
    2026 年汛期跟踪“巴威”“白海豚”等台风，开展中线交叉建筑物洪水模拟；
    水质监测数据入库 5000 万条，可模拟污染物、藻类迁移扩散，生成闸门
    调度建议及应急处置预案；2025—2026 年度冰期比计划多供水 1.58 亿立方米；
    东中线一期累计调水超 920 亿立方米、近 2 亿人受益。
  · 2026-11-20，财跃星辰在长沙发布 FinWork V1.0：220 余项金融 Skill，
    3 分钟完成客户持仓分析，单条内容生成成本约 3 分钱、耗时 8 秒，
    全链路溯源与企业级安全权限管控；国泰海通落地 1300 余个 Agent、
    260 余个场景；国金证券 150 余个场景、400 余个 Skill、调用超 8000 万次。

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
    """调度室与工位，两个操作层"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "同一个星期，两个“操作层”",
           "11 月 20 日长沙 FinWork V1.0；11 月 21 日北京 天河 V2")

    card(ax, 0.045, 0.300, 0.430, 0.420, NAVY, lw=1.5)
    ax.text(0.068, 0.660, "调度室", fontsize=26, color=NAVY, weight="bold",
            ha="left", va="center", zorder=6)
    ax.plot([0.068, 0.450], [0.628, 0.628], color=NAVY, linewidth=0.9,
            alpha=0.35, zorder=5)
    ax.text(0.068, 0.588,
            "27 颗遥感卫星\n237 部气象雷达\n\n防汛形势分析\n小时级 → 分钟级",
            fontsize=11.0, color=DARK, ha="left", va="top",
            linespacing=1.75, zorder=6)

    card(ax, 0.525, 0.300, 0.430, 0.420, TEAL, lw=1.5)
    ax.text(0.548, 0.660, "工位", fontsize=26, color=TEAL, weight="bold",
            ha="left", va="center", zorder=6)
    ax.plot([0.548, 0.930], [0.628, 0.628], color=TEAL, linewidth=0.9,
            alpha=0.35, zorder=5)
    ax.text(0.548, 0.588,
            "220+ 项金融 Skill\n3 分钟 客户持仓分析\n\n3 分钱 · 8 秒\n单条内容生成",
            fontsize=11.0, color=DARK, ha="left", va="top",
            linespacing=1.75, zorder=6)

    ax.text(0.045, 0.210,
            "一个把多源数据算成调度建议，一个把分析做成可审计、可计价的输出。",
            fontsize=9.4, color=SLATE, ha="left", va="center")

    punchline(fig, "一个进调度室，一个进工位。")
    footer(fig, "事实来源：科技日报 2026-11-21；新京报 2026-11-21；科创板日报 2026-11-21；"
                "财联社 2026-11-21")
    fig.savefig(OUT + "图1_两个场景.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """天河 V2：数据进得去，建议出得来"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "数据进得去，建议出得来",
           "天河 V2：从多源数据到闸门调度建议")

    sources = ["27 颗遥感卫星", "237 部气象雷达", "5000 万条水质监测"]
    ys = [0.620, 0.495, 0.370]
    for text, y in zip(sources, ys):
        card(ax, 0.045, y, 0.225, 0.095, GRAY, lw=1.0)
        ax.text(0.062, y + 0.047, text, fontsize=9.2, color=DARK,
                ha="left", va="center", zorder=6)

    card(ax, 0.330, 0.345, 0.255, 0.330, NAVY, lw=1.5)
    ax.text(0.352, 0.620, "天河 V2", fontsize=13.0, color=NAVY,
            weight="bold", ha="left", va="center", zorder=6)
    ax.plot([0.352, 0.562], [0.596, 0.596], color=NAVY, linewidth=0.9,
            alpha=0.35, zorder=5)
    ax.text(0.352, 0.565,
            "雨情 · 水情 · 工情\n\n污染物扩散模拟\n洪水模拟",
            fontsize=9.0, color=DARK, ha="left", va="top",
            linespacing=1.7, zorder=6)

    outputs = [
        ("防汛形势分析", "分钟级"),
        ("洪水模拟", "中线交叉建筑物"),
        ("闸门调度建议", "+ 应急处置预案"),
    ]
    for (head, note), y in zip(outputs, ys):
        card(ax, 0.645, y, 0.310, 0.095, RED, lw=1.1)
        ax.text(0.662, y + 0.058, head, fontsize=9.2, color=RED,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(0.662, y + 0.030, note, fontsize=8.4, color=SLATE,
                ha="left", va="center", zorder=6)

    ax.annotate("", xy=(0.325, 0.510), xytext=(0.275, 0.510),
                arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=1.4))
    ax.annotate("", xy=(0.640, 0.510), xytext=(0.590, 0.510),
                arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=1.4))

    ax.text(0.045, 0.255,
            "输出是建议——闸门开不开、开多大，最后仍由人定。",
            fontsize=9.4, color=RED, ha="left", va="center")

    punchline(fig, "分钟级，是把“看天”变成“算天”。")
    footer(fig, "事实来源：科技日报 2026-11-21《为国家水网装上“智慧大脑”，“天河”大模型V2发布》；"
                "新京报 2026-11-21")
    fig.savefig(OUT + "图2_水利链路.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """四个新指标：分钟、3 分钱、8 秒、可审计"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "跑分退场，账单上场",
           "两个场景，四个新指标")

    items = [
        ("分钟级", "防汛形势分析", "原为小时级", NAVY),
        ("3 分钱", "单条内容生成", "成本", RED),
        ("8 秒", "单条内容生成", "耗时", RED),
        ("可审计", "全链路溯源", "权限管控", TEAL),
    ]
    w, gap = 0.212, 0.019
    x = 0.045
    for metric, name, note, color in items:
        card(ax, x, 0.330, w, 0.330, color, lw=1.4)
        ax.text(x + 0.022, 0.590, metric, fontsize=24, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(x + 0.022, 0.505, name, fontsize=9.4, color=DARK,
                ha="left", va="center", zorder=6)
        ax.text(x + 0.022, 0.462, note, fontsize=8.8, color=GRAY,
                ha="left", va="center", zorder=6)
        x += w + gap

    ax.text(0.045, 0.235,
            "采购看的是：单位任务成本 × 可追溯性。",
            fontsize=10.2, color=DARK, ha="left", va="center")

    punchline(fig, "采购桌上，跑分让位于账单。")
    footer(fig, "事实来源：科技日报 2026-11-21；新京报 2026-11-21；科创板日报 2026-11-21")
    fig.savefig(OUT + "图3_四个指标.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)