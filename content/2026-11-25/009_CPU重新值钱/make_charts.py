# -*- coding: utf-8 -*-
"""
《AMD 把 2030 年服务器 CPU 市场从 1200 亿调到 2200 亿：AI 推理在重估 CPU》配套图表

事实口径：

一、TAM 上调链条（服务器 CPU 市场，2030 年口径）
  · 2024-11 分析师日：约 600 亿美元，年增 18%（Morningstar 记为 Six months ago
    at the November Analyst Day 约 600 亿 / 18%）
  · 2026-05 财报电话会（5 月 5 日美东盘后）：年增速上调至超 35%，
    2030 年超 1200 亿美元。据第一财经 2026-05-06。
  · 2026-07-23 Advancing AI 2026：上调至 2200 亿美元。
    据 Morningstar（Brian Colello，2026-07-24）：$220B，up from March forecast of $120B。
  · 2026-10-12 OCP Global Summit：苏姿丰称"过去九个月已三次上调 TAM"，
    当时对外口径为"2030 年超 2000 亿美元"。据 TrendForce 2026-10-13。
  · 一年前该市场约 200 亿美元、年增个位数（TrendForce 引苏姿丰原话）。

二、CPU:GPU 比例
  · 苏姿丰 2026-05 财报电话会原话（第一财经）："过去主要节点中的 CPU、GPU
    比例在 1:8 到 1:4 之间，现在已经在往 1:1 的比例演进。"
  · 2026 是"推理之年"，推理约占市场 60% 并成为常态（TrendForce，OCP 演讲）。
  · 分析师分歧：Northland（Gus Richard）训练 1:8、推理 1:4、智能体 1:2；
    Evercore ISI（Mark Lipacis）可能由 1:8 翻转到 8:1。
    据 TradingKey。属第三方观点，非 AMD 口径。

三、同期系统侧数据
  · 中国移动第二批 AI 超节点集采（2026-11-20）：合计 52160 卡，
    6—7 家中标人，每家每配置承诺至少 30% 供货量。
  · 中国电信智算超节点（N 系列）集采（2026-11-16）：
    最高投标限价 257.88 亿元（含税），须通过集群联调性能测试。
  · 戴尔 FY27 Q3（2026-11-24）：单季新增 AI 服务器订单 602 亿美元，
    确认收入 220 亿美元，期末积压 1323 亿美元。

四、Helion 机架（OCP 合规）
  · 标准 21 英寸机架、风冷或液冷、最高 32000+ Zen 6 核心（较其他竞品机架多 40%）、
    可装最多 32 颗 Instinct MI350 GPU。据 TrendForce 引苏姿丰 OCP 演讲。

风格：克制传媒风，白底、低饱和配色、标题即结论（沿用本工作区既有规范）
输出目录 = 脚本所在目录
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
    """三次上调"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "九个月，这个预测上调了三次",
           "AMD 对 2030 年服务器 CPU 市场规模的判断（亿美元）")

    data = [
        ("2024.11", "分析师日", 600, GRAY, "年增 18%"),
        ("2026.05", "财报电话会", 1200, SLATE, "年增超 35%"),
        ("2026.07", "Advancing AI", 2200, RED, "本次上调"),
    ]

    base_y = 0.360
    max_h = 0.330
    maxv = 2200.0

    for i, (date, where, val, color, note) in enumerate(data):
        cx = 0.152 + i * 0.300
        h = max_h * val / maxv
        ax.add_patch(Rectangle((cx - 0.062, base_y), 0.124, h,
                               facecolor=color, edgecolor=color,
                               linewidth=0, alpha=0.90, zorder=4))
        ax.text(cx, base_y + h + 0.026, f"{val}", fontsize=17, color=color,
                weight="bold", ha="center", va="bottom", zorder=6)
        ax.text(cx, base_y - 0.028, date, fontsize=10.0, color=DARK,
                weight="bold", ha="center", va="top")
        ax.text(cx, base_y - 0.062, where, fontsize=8.4, color=GRAY,
                ha="center", va="top")
        ax.text(cx, base_y - 0.094, note, fontsize=8.4, color=color,
                ha="center", va="top")

    ax.plot([0.052, 0.952], [base_y, base_y], color=SLATE, linewidth=1.2)

    ax.text(0.052, 0.752, "单位：亿美元 / 2030 年市场规模", fontsize=9.4,
            color=GRAY, ha="left", va="center")
    ax.plot([0.052, 0.952], [0.732, 0.732], color=LIGHT, linewidth=1.0)

    card(ax, 0.052, 0.140, 0.900, 0.070, LIGHT, face=PALE, lw=1.0)
    ax.text(0.074, 0.175,
            "一年前，这块市场还被认为是约 200 亿美元、年增个位数。"
            "苏姿丰在 10 月 OCP 峰会上说：九个月里已上调三次。",
            fontsize=9.4, color=DARK, ha="left", va="center", zorder=6)

    punchline(fig, "不是模型算错了，是需求变了。")
    footer(fig, "事实来源：AMD 各期口径经 Morningstar（2026-07-24）、第一财经（2026-05-06）、"
                "TrendForce（2026-10-13）记录；2200 亿为 7 月 Advancing AI 大会口径")
    fig.savefig(OUT + "图1_三次上调.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """比例迁移"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "从 1:8 到 1:1，方向有共识，数字没有",
           "CPU 与 GPU 的配比：一条官方趋势线，三种不同的估法")

    # 官方趋势
    ax.text(0.048, 0.780, "苏姿丰 2026 年 5 月财报电话会的表述", fontsize=10.0,
            color=GRAY, ha="left", va="center")
    ax.plot([0.048, 0.952], [0.760, 0.760], color=LIGHT, linewidth=1.0)

    stages = [
        ("过去", "1 : 8 ~ 1 : 4", "主要节点中的常见比例", GRAY),
        ("现在", "往 1 : 1 演进", "苏姿丰：这个数据很难准确判断", RED),
    ]
    y = 0.680
    for label, ratio, note, color in stages:
        ax.text(0.048, y, label, fontsize=10.4, color=SLATE,
                ha="left", va="center")
        ax.text(0.180, y, ratio, fontsize=19, color=color,
                weight="bold", ha="left", va="center")
        ax.text(0.470, y, note, fontsize=9.2, color=SLATE,
                ha="left", va="center")
        y -= 0.110

    # 分析师分歧
    ax.text(0.048, 0.470, "卖方分析师给的分段估计（第三方观点，非 AMD 口径）",
            fontsize=10.0, color=GRAY, ha="left", va="center")
    ax.plot([0.048, 0.952], [0.450, 0.450], color=LIGHT, linewidth=1.0)

    views = [
        ("Northland", "训练 1:8 → 推理 1:4 → 智能体 1:2", SLATE),
        ("Evercore ISI", "可能由 1:8 翻转至 8:1", TEAL),
    ]
    y = 0.386
    for who, view, color in views:
        ax.text(0.048, y, who, fontsize=9.6, color=DARK, weight="bold",
                ha="left", va="center")
        ax.text(0.240, y, view, fontsize=9.4, color=color,
                ha="left", va="center")
        y -= 0.070

    card(ax, 0.048, 0.150, 0.900, 0.106, RED, face="white", lw=1.3)
    ax.text(0.070, 0.232, "可以确认的是方向，不能确认的是具体倍数。",
            fontsize=10.0, color=DARK, weight="bold",
            ha="left", va="center", zorder=6)
    ax.text(0.070, 0.188,
            "苏姿丰说的是「往 1:1 演进」，并强调这个比例本身难以准确判断；"
            "把它当作既成事实会读错。",
            fontsize=9.2, color=SLATE, ha="left", va="center", zorder=6)

    punchline(fig, "CPU 变重是真的，但别把趋势当现状。")
    footer(fig, "事实来源：第一财经 2026-05-06（苏姿丰原话）；"
                "Northland 与 Evercore ISI 估计据 TradingKey 报道")
    fig.savefig(OUT + "图2_比例迁移.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """瓶颈挪位"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "瓶颈从「有没有卡」挪到了「能不能交系统」",
           "同期三组数据，指向同一件事")

    rows = [
        ("中国移动 第二批超节点集采",
         "52160 卡", "6—7 家中标人，每配置承诺至少 30% 供货量", NAVY, "11.20"),
        ("中国电信 智算超节点集采",
         "257.88 亿元", "含税限价，须过集群联调性能测试", NAVY, "11.16"),
        ("戴尔 FY27 第三季度",
         "1323 亿美元", "AI 订单积压创纪录，审核客户资金、土地与电力", RED, "11.24"),
    ]

    y = 0.660
    for name, big, note, color, date in rows:
        card(ax, 0.048, y - 0.076, 0.904, 0.116, color, lw=1.2)
        ax.text(0.070, y + 0.006, name, fontsize=9.8, color=DARK,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(0.070, y - 0.036, big, fontsize=15.0, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(0.330, y - 0.036, note, fontsize=8.8, color=SLATE,
                ha="left", va="center", zorder=6)
        ax.text(0.930, y + 0.006, date, fontsize=8.6, color=GRAY,
                ha="right", va="center", zorder=6)
        y -= 0.140

    ax.add_patch(FancyArrowPatch((0.048, 0.256), (0.952, 0.256),
                                 arrowstyle="-|>", mutation_scale=16,
                                 color=GRAY, linewidth=1.3, zorder=5))
    ax.text(0.048, 0.222, "买卡", fontsize=9.4, color=GRAY,
            ha="left", va="center")
    ax.text(0.952, 0.222, "买可交付的系统", fontsize=9.4, color=RED,
            weight="bold", ha="right", va="center")

    card(ax, 0.048, 0.128, 0.904, 0.070, LIGHT, face=PALE, lw=1.0)
    ax.text(0.070, 0.163,
            "而系统里负责调度、编排、拼装的那一环，是 CPU。",
            fontsize=9.8, color=DARK, ha="left", va="center", zorder=6)

    punchline(fig, "CPU 从配套变成决定一套系统跑不跑得顺的那一环。")
    footer(fig, "事实来源：中国移动 2026-11-20 招标公告、中国电信 2026-11-16 集采公告、"
                "戴尔 2027 财年第三季度业绩（2026-11-24）")
    fig.savefig(OUT + "图3_瓶颈挪位.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)



