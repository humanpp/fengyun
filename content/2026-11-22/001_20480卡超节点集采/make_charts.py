# -*- coding: utf-8 -*-
"""
《20480 卡、117 亿、30 天：中国移动这笔算力大单，把三个数字同时摆上了公告》
配套图表

事实口径（核到招标公告、中标候选人公示与上市公司公告）：
  · 2026-09-29 中国移动发布「2026 年至 2027 年新一代人工智能超节点设备集中采购项目」
    招标公告，计划采购 AI 超节点合计 20480 卡，及配套 RoCE 交换机 448 台、
    存储 82 套。
  · 2026-10-28 中标候选人公示：四川华鲲振宇、宝德计算机、浙江华启智慧、
    百信信息、神州鲲泰五家入围，拟中标份额分别为 6144 卡、5120 卡、4096 卡、
    3072 卡、2048 卡，合计 20480 卡；交货期 30 天；项目金额预计 116 亿至
    117 亿元之间（各家报价均在 116 亿元上下）。
  · 2026-11-02 晚间，大华股份（002236）公告：子公司浙江华启智慧科技有限公司
    中标该项目，中标金额约 26.3 亿元（含税），超出董事会此前预计的 20.5 亿元上限。
  · 五家均为国产算力整机生态伙伴；华启智慧脱胎于大华股份（成立于 2022 年），
    算力业务为大华第二增长曲线；中国移动为大华股份持股 5% 以上股东，
    该笔交易构成关联交易。
  · 对照：中国电信 2026 年 6 月发布高性能服务器（2026-2027 年）集采，
    采购约 4 万台，总额约 115 亿元。
  据智东西/新浪 2026-11-02、C114 通信网 2026-10-28、21 经济网 2026-11-03、
  大华股份 2026-11-02 公告。

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

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep

Y_TITLE = 0.958
Y_SUB = 0.898
Y_PUNCH = 0.070
Y_FOOT = 0.020

Q_L = "\u300c"
Q_R = "\u300d"


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
    """五家分食 20480 卡"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "20480 卡，五家分完",
           "四川华鲲振宇、宝德、华启智慧、百信、神州鲲泰，份额按卡数公示")

    vendors = [
        ("四川华鲲振宇", 6144, NAVY, "6144 卡"),
        ("宝德计算机", 5120, NAVY, "5120 卡"),
        ("浙江华启智慧", 4096, RED, "4096 卡"),
        ("百信信息", 3072, TEAL, "3072 卡"),
        ("神州鲲泰", 2048, TEAL, "2048 卡"),
    ]

    x0 = 0.052
    bar_w = 0.150
    scale = 0.300 / 6144.0
    base = 0.360
    total = 20480.0

    # 厂商名手动断行，避免按字符位置硬切
    names_2line = {
        "四川华鲲振宇": ("四川", "华鲲振宇"),
        "宝德计算机": ("宝德", "计算机"),
        "浙江华启智慧": ("浙江", "华启智慧"),
        "百信信息": ("百信信息", ""),
        "神州鲲泰": ("神州鲲泰", ""),
    }

    for i, (name, cards, color, label) in enumerate(vendors):
        cx = x0 + i * 0.176
        h = cards * scale
        pct = cards / total * 100
        ax.add_patch(Rectangle((cx, base), bar_w, h,
                               facecolor=color, edgecolor=color,
                               linewidth=0, alpha=0.90, zorder=4))
        ax.text(cx + bar_w / 2, base + h + 0.038, label,
                fontsize=13.0, color=color, weight="bold",
                ha="center", va="bottom", zorder=6)
        ax.text(cx + bar_w / 2, base + h + 0.014, f"{pct:.1f}%",
                fontsize=8.6, color=GRAY, ha="center", va="bottom", zorder=6)

        l1, l2 = names_2line[name]
        ax.text(cx + bar_w / 2, base - 0.028, l1, fontsize=8.8, color=DARK,
                ha="center", va="top", zorder=6)
        if l2:
            ax.text(cx + bar_w / 2, base - 0.062, l2, fontsize=8.8,
                    color=DARK, ha="center", va="top", zorder=6)

    ax.plot([0.046, 0.960], [base, base], color=SLATE, linewidth=1.1, zorder=5)

    ax.text(0.052, 0.238,
            "合计 20480 卡，五家份额全部为 1024 的整数倍。",
            fontsize=9.4, color=SLATE, ha="left", va="center")
    ax.text(0.052, 0.196,
            "配套：RoCE 交换机 448 台、存储 82 套。",
            fontsize=9.4, color=SLATE, ha="left", va="center")

    punchline(fig, "卡数能精确到个位，这在过去的运营商采购里不多见。")
    footer(fig, "事实来源：中国移动 2026-2027 年新一代人工智能超节点设备集中采购项目"
                "中标候选人公示（2026-10-28）；大华股份公告（2026-11-02）")
    fig.savefig(OUT + "图1_五家分食.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """三个数字：117亿、30天、26.3亿"""
    fig = plt.figure(figsize=(12, 6.8))
    ax = new_axes(fig)

    header(fig, "三个数字，一个比一个少见于公告",
           "总额、交货期、单家中标额，同时公开在同一次采购里")

    rows = [
        ("116—117 亿元", "项目总金额",
         "五家投标报价均在 116 亿元上下", NAVY),
        ("30 天", "约定交货期",
         "从公示到交付的窗口，压在了一个月内", RED),
        ("约 26.3 亿元", "华启智慧单家中标额（含税）",
         "超出其董事会此前预计的 20.5 亿元上限", TEAL),
    ]

    top = 0.720
    for i, (num, label, note, color) in enumerate(rows):
        y = top - i * 0.190
        ax.text(0.052, y, num, fontsize=26, color=color, weight="bold",
                ha="left", va="center")
        ax.text(0.052, y - 0.058, label, fontsize=10.0, color=GRAY,
                ha="left", va="center")
        ax.text(0.520, y - 0.010, note, fontsize=9.2, color=SLATE,
                ha="left", va="center")
        if i < 2:
            ax.plot([0.052, 0.952], [y - 0.100] * 2, color=LIGHT,
                    linewidth=1.0)

    ax.text(0.052, 0.156,
            "对照：中国电信 2026 年 6 月高性能服务器集采采购约 4 万台，总额约 115 亿元。",
            fontsize=9.2, color=SLATE, ha="left", va="center")

    punchline(fig, "两家运营商的算力采购，规模已经落在同一个量级。")
    footer(fig, "事实来源：C114 通信网 2026-10-28；21 经济网 2026-11-03；"
                "大华股份 2026-11-02 公告")
    fig.savefig(OUT + "图2_三个数字.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """时间线：29天走完招标到中标"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "从发标到中标落定，29 天",
           "9 月 29 日发标，10 月 28 日公示候选人，11 月 2 日上市公司确认金额")

    nodes = [
        ("9 月 29 日", "发招标公告",
         "20480 卡、RoCE 交换机 448 台、\n存储 82 套", NAVY),
        ("10 月 28 日", "中标候选人公示",
         "五家入围，拟中标份额\n6144 / 5120 / 4096 / 3072 / 2048 卡", RED),
        ("11 月 2 日", "中标金额确认",
         "华启智慧公告 26.3 亿元（含税），\n并披露构成关联交易", TEAL),
    ]

    line_y = 0.500
    ax.plot([0.090, 0.910], [line_y, line_y], color=LIGHT, linewidth=3.0,
            zorder=2)

    for i, (date, title, detail, color) in enumerate(nodes):
        cx = 0.155 + i * 0.340
        ax.add_patch(plt.Circle((cx, line_y), 0.013, facecolor=color,
                                edgecolor="white", linewidth=2.0, zorder=6))
        ax.text(cx, line_y + 0.048, date, fontsize=11.6, color=color,
                weight="bold", ha="center", va="bottom", zorder=6)
        ax.text(cx, line_y + 0.020, title, fontsize=9.6, color=DARK,
                ha="center", va="bottom", zorder=6)
        ax.text(cx, line_y - 0.048, detail, fontsize=8.6, color=SLATE,
                ha="center", va="top", linespacing=1.62, zorder=6)

    # 底部两个说明块
    card(ax, 0.052, 0.180, 0.430, 0.160, NAVY, face=PALE, lw=1.2)
    ax.text(0.074, 0.302, "30 天交货期", fontsize=10.6, color=NAVY,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.074, 0.258,
            "公示口径写的是 30 天。对整机厂商来说，\n"
            "这更像库存与产能的检验，不是研发的检验。",
            fontsize=8.8, color=DARK, ha="left", va="top",
            linespacing=1.62, zorder=6)

    card(ax, 0.522, 0.180, 0.430, 0.160, RED, face="white", lw=1.4)
    ax.text(0.544, 0.302, "一笔关联交易", fontsize=10.6, color=RED,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.544, 0.258,
            "中国移动是大华股份持股 5% 以上股东，\n"
            "因此这笔中标按关联交易履行披露。",
            fontsize=8.8, color=DARK, ha="left", va="top",
            linespacing=1.62, zorder=6)

    punchline(fig, "发标到落定 29 天，真正被考验的是供应链手里的货。")
    footer(fig, "事实来源：中国移动招标公告（2026-09-29）、中标候选人公示（2026-10-28）、"
                "大华股份公告（2026-11-02）")
    fig.savefig(OUT + "图3_29天.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)
