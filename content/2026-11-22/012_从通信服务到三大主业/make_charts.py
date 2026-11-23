# -*- coding: utf-8 -*-
"""
《营收只涨 0.9%，但结构换了一层：三大主业这件事，财务上是什么样子》配套图表

事实口径（2025 年年度业绩，2026-03-26 公布）：

一、整体
  · 营运收入 10,502 亿元，同比增长 0.9%；
    主营业务收入 8,955 亿元，同比增长 0.7%。
  · 通信服务收入 7,149 亿元，同比下降 1.0%；
    通信服务收入占主营业务收入比 79.8%。
  · 算力服务、智能服务收入合计占主营业务收入比 20.2%，同比提升 1.4 个百分点。

二、三项服务（口径来自年报及央广网、中国证券报报道）
  · 通信服务：移动客户 10.05 亿户；5G 网络客户 6.42 亿户，净增 8,960 万户，
    渗透率 63.9%；宽带联网客户 3.29 亿，净增 999 万，宽带网络收入同比增长 7.1%；
    物联网卡连接数 14.8 亿，AIoT 平台为全球最大连接管理平台；
    获颁卫星移动通信业务经营许可。
  · 算力服务：收入 898 亿元，同比增长 11.1%；
    数据中心收入同比增长 8.7%，其中 AIDC 收入同比增长 35.4%；
    智算服务收入增速 279%，拉动云算服务收入同比增长 13.9%；
    云盘月活跃客户 2.1 亿户，云视频客户超 8,670 万户。
    智算总规模 92.5 EFLOPS（FP16），百卡至超万卡全规格；
    城域 1ms / 省域 5ms / 全国 20ms 三级算力时延圈；
    省际骨干 400G OTN 基本覆盖全国；对外服务 IDC 标准机架超 150 万架（2.5KW 折合）。
  · 智能服务：收入 908 亿元，同比增长 5.3%；
    升级九天基础大模型 3.0；推出超 100 款 AI+ 产品及应用解决方案、
    29 款垂类智能体；自主打造高质量数据集 3500TB；
    数据算法收入同比增长 12.6%，数智文化收入同比增长 13.3%；
    重点布局超 50 款自研行业大模型；AI 智能助理灵犀智能体月活跃客户超 1 亿。
  · 收入百亿级产品 13 项，客户超亿户产品 17 项。

风格：克制传媒风，白底、低饱和配色、标题即结论
输出目录 = 脚本所在目录
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

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
AMBER = "#9a7b4f"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep

Y_TITLE = 0.962
Y_SUB = 0.912
Y_PUNCH = 0.052
Y_FOOT = 0.014

Q_L = "\u300c"
Q_R = "\u300d"


def header(fig, title, sub):
    fig.text(0.040, Y_TITLE, title, fontsize=18.5, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.040, Y_SUB, sub, fontsize=10.2, color=GRAY,
             ha="left", va="top")


def footer(fig, text):
    fig.text(0.040, Y_FOOT, text, fontsize=7.2, color=GRAY,
             ha="left", va="bottom")


def punchline(fig, text):
    fig.text(0.040, Y_PUNCH, text, fontsize=10.0, color=DARK,
             ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.65", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


def card(ax, x, y, w, h, edge, face="white", lw=1.0, z=2):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.003,rounding_size=0.012",
        facecolor=face, edgecolor=edge, linewidth=lw, zorder=z))


def new_axes(fig):
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return ax


# ---------------------------------------------------------------- 图 1
def fig1():
    """三条收入曲线：一降两升"""
    fig = plt.figure(figsize=(13.2, 7.4))
    ax = new_axes(fig)

    header(fig, "三条收入，一条在降，两条在升",
           "2025 年主营业务收入 8,955 亿元，只涨 0.7%——差一点就是零增长")

    rows = [
        ("通信服务", 7149, -1.0, "占主营业务收入 79.8%", NAVY, "降"),
        ("算力服务", 898, 11.1, "智算服务增速 279%", RED, "升"),
        ("智能服务", 908, 5.3, "灵犀智能体月活超 1 亿", TEAL, "升"),
    ]

    ax.text(0.048, 0.760, "收入规模与同比增速", fontsize=10.0, color=GRAY,
            ha="left", va="center")
    ax.plot([0.048, 0.960], [0.736, 0.736], color=LIGHT, linewidth=1.0)

    scale = 0.560 / 7149.0

    y = 0.680
    for name, val, growth, note, color, direction in rows:
        ax.text(0.048, y + 0.010, name, fontsize=11.4, color=DARK,
                weight="bold", ha="left", va="center", zorder=6)
        w = val * scale
        ax.add_patch(Rectangle((0.048, y - 0.048), w, 0.030,
                               facecolor=color, edgecolor=color,
                               linewidth=0, alpha=0.88, zorder=4))
        ax.text(0.048, y - 0.080, f"{val:,} 亿元", fontsize=9.6, color=color,
                weight="bold", ha="left", va="top", zorder=6)
        ax.text(0.700, y + 0.010, f"{growth:+.1f}%", fontsize=13.0,
                color=color if growth > 0 else SLATE, weight="bold",
                ha="left", va="center", zorder=6)
        ax.text(0.700, y - 0.028, note, fontsize=8.2, color=GRAY,
                ha="left", va="center", zorder=6)
        y -= 0.175

    ax.text(0.048, 0.168,
            "把 79.8% 与 20.2% 相加是 100%——这是一次结构定义，不只是业务盘点。",
            fontsize=9.2, color=DARK, ha="left", va="center")

    punchline(fig, "总量几乎不动的时候，能看的只剩结构。")
    footer(fig, "事实来源：中国移动 2025 年年度业绩（2026-03-26 公布）；"
                "央广网 2026-03-26；中国证券报 2026-03-27")
    fig.savefig(OUT + "图1_三条收入.png", dpi=160)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """79.8 / 20.2 的结构"""
    fig = plt.figure(figsize=(13.2, 7.4))
    ax = new_axes(fig)

    header(fig, "79.8 与 20.2：一个百分比的迁移",
           "算力与智能服务合计占主营业务收入 20.2%，同比提升 1.4 个百分点")

    # 左侧：堆叠条
    bar_x = 0.060
    bar_w = 0.360
    bar_y = 0.470
    bar_h = 0.070

    seg1 = bar_w * 0.798
    seg2 = bar_w * 0.202

    ax.add_patch(Rectangle((bar_x, bar_y), seg1, bar_h,
                           facecolor=NAVY, edgecolor="white",
                           linewidth=1.5, zorder=4))
    ax.add_patch(Rectangle((bar_x + seg1, bar_y), seg2, bar_h,
                           facecolor=RED, edgecolor="white",
                           linewidth=1.5, zorder=4))

    ax.text(bar_x + seg1 / 2, bar_y + bar_h / 2, "通信服务 79.8%",
            fontsize=11.0, color="white", weight="bold",
            ha="center", va="center", zorder=6)
    ax.text(bar_x + seg1 + seg2 / 2, bar_y + bar_h + 0.030, "20.2%",
            fontsize=10.4, color=RED, weight="bold",
            ha="center", va="bottom", zorder=6)

    # 标注
    ax.annotate("", xy=(bar_x + seg1, bar_y - 0.012),
                xytext=(bar_x + bar_w, bar_y - 0.012),
                arrowprops=dict(arrowstyle="<|-|>", color=RED,
                                linewidth=1.2, shrinkA=0, shrinkB=0))
    ax.text(bar_x + seg1 + seg2 / 2, bar_y - 0.030,
            "算力 + 智能", fontsize=8.6, color=RED,
            ha="center", va="top")

    ax.text(bar_x, bar_y + bar_h + 0.075, "2025 年主营业务收入 8,955 亿元的结构",
            fontsize=9.6, color=GRAY, ha="left", va="center")

    # 同比提升
    ax.text(0.060, 0.360, "同比 +1.4 个百分点", fontsize=14.0, color=RED,
            weight="bold", ha="left", va="center")
    ax.text(0.060, 0.312,
            "在主营业务收入只增长 0.7% 的一年里，\n这部分占比反而抬升了 1.4 个百分点——\n说明它的增速快于整体。",
            fontsize=9.0, color=SLATE, ha="left", va="top", linespacing=1.75)

    # 右侧：两个新主业的支撑指标
    ax.text(0.580, 0.760, "支撑这两块的两组指标", fontsize=10.0, color=GRAY,
            ha="left", va="center")
    ax.plot([0.580, 0.960], [0.736, 0.736], color=LIGHT, linewidth=1.0)

    items = [
        ("算力服务", "898 亿元 · +11.1%", [
            "智算总规模 92.5 EFLOPS（FP16）",
            "AIDC 收入增速 35.4%",
            "IDC 标准机架超 150 万架",
        ], RED),
        ("智能服务", "908 亿元 · +5.3%", [
            "九天大模型升级至 3.0",
            "29 款垂类智能体、超 100 款 AI+ 方案",
            "自建数据集 3,500TB",
        ], TEAL),
    ]
    y = 0.680
    for name, headline, points, color in items:
        ax.text(0.580, y, name, fontsize=10.6, color=color, weight="bold",
                ha="left", va="center", zorder=6)
        ax.text(0.580, y - 0.036, headline, fontsize=8.8, color=DARK,
                ha="left", va="center", zorder=6)
        yy = y - 0.078
        for p in points:
            ax.text(0.598, yy, "· " + p, fontsize=8.2, color=SLATE,
                    ha="left", va="center", zorder=6)
            yy -= 0.042
        y -= 0.246

    punchline(fig, "新主业还小，但它是在存量不动的时候长出来的。")
    footer(fig, "事实来源：中国移动 2025 年年度业绩（2026-03-26 公布）；央广网 2026-03-26")
    fig.savefig(OUT + "图2_结构迁移.png", dpi=160)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """为什么必须换引擎：连接见顶"""
    fig = plt.figure(figsize=(13.2, 7.4))
    ax = new_axes(fig)

    header(fig, "连接还在涨，但涨的速度已经不够用了",
           "用户规模接近天花板，通信服务收入 2025 年同比 -1.0%")

    # 上：三组连接数
    ax.text(0.048, 0.760, "三张连接表（2025 年末）", fontsize=10.0, color=GRAY,
            ha="left", va="center")
    ax.plot([0.048, 0.960], [0.736, 0.736], color=LIGHT, linewidth=1.0)

    conns = [
        ("移动客户", "10.05 亿户", "", NAVY, 1.00),
        ("5G 网络客户", "6.42 亿户", "净增 8,960 万户 · 渗透率 63.9%", RED, 0.64),
        ("物联网卡连接", "14.8 亿", "AIoT 为全球最大连接管理平台", TEAL, 1.00),
    ]

    y = 0.664
    for name, val, note, color, ratio in conns:
        ax.text(0.048, y + 0.012, name, fontsize=9.4, color=GRAY,
                ha="left", va="center", zorder=6)
        ax.text(0.190, y + 0.012, val, fontsize=12.4, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        if note:
            ax.text(0.400, y + 0.012, note, fontsize=8.2, color=SLATE,
                    ha="left", va="center", zorder=6)
        ax.add_patch(Rectangle((0.048, y - 0.028), 0.380 * ratio, 0.018,
                               facecolor=color, edgecolor=color,
                               linewidth=0, alpha=0.75, zorder=4))
        y -= 0.086

    # 下：三个转折点
    ax.text(0.048, 0.400, "三个转折信号", fontsize=10.0, color=GRAY,
            ha="left", va="center")
    ax.plot([0.048, 0.960], [0.376, 0.376], color=LIGHT, linewidth=1.0)

    signals = [
        ("收入曲线掉头", "通信服务收入 7,149 亿元，\n同比下降 1.0%", NAVY),
        ("增长重心换位", "宽带网络收入 +7.1%，\n高于通信服务整体", TEAL),
        ("新牌照落地", "获颁卫星移动通信业务\n经营许可，进入商业化运营", RED),
    ]
    x = 0.048
    for title, detail, color in signals:
        card(ax, x, 0.196, 0.286, 0.150, color, lw=1.3)
        ax.text(x + 0.020, 0.312, title, fontsize=9.8, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(x + 0.020, 0.272, detail, fontsize=8.4, color=DARK,
                ha="left", va="top", linespacing=1.65, zorder=6)
        x += 0.306

    punchline(fig, "用户数还会涨，但「靠连接数换收入」这条路已经走到头。")
    footer(fig, "事实来源：中国移动 2025 年年度业绩（2026-03-26 公布）；"
                "央广网 2026-03-26 对年报的报道")
    fig.savefig(OUT + "图3_连接见顶.png", dpi=160)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)
