# -*- coding: utf-8 -*-
"""
《8000 亿进场：这笔钱不盖楼，只垫第一块砖》配套图表

事实口径（新华社、经济参考报、21 世纪经济报道、第一财经，2026-10-28/29）：
  · 截至 2026-10-28，2026 年新型政策性金融工具全部完成投放，共 8000 亿元，
    较 2025 年的 5000 亿元增加 3000 亿元、增幅 60%；全部用于补充项目资本金。
  · 国开行 3650 亿元，涉及项目总投资 5.5 万亿元；
    农发行 3150 亿元，支持项目 3027 个，项目总投资约 4.39 万亿元；
    进出口银行 1200 亿元，支持项目超 500 个，拉动总投资逾 1.7 万亿元。
  · 合计撬动项目总投资约 11.59 万亿元（界面新闻统计为 11.6 万亿元，杠杆逾 14 倍）。
  · 节奏：2025 年 5000 亿元在约一个月内投完；2026 年 8000 亿元自 9 月初开始，
    历时近两个月。
  · 投向：国开行向人工智能、数字经济、绿色低碳、生物医药、消费等领域投放
    1790.1 亿元、占比 49%；农发行重点支持人工智能、数字经济、低空经济、消费、
    绿色低碳，金额近 2000 亿元、占比约 60%；进出口银行推动 220 余个数字经济和
    人工智能等新兴产业项目落地、放款占比近五成。
  · 民间投资：国开行 1279.9 亿元、占比 35.1%；农发行 378 个项目、651.54 亿元、
    占比 20.7%；进出口银行 210 余个项目、放款占比近四成；综合占比超 30%。
  · 经济大省：国开行向 11 个经济体量较大省份投放 2778.6 亿元、占比 76.1%；
    进出口银行对 11 个经济大省 330 余个项目、放款占比超七成。
  · 农发行项目数占全国新工具项目数六成以上；市县级客户占比 63%、县级 45%。
  · 案例：国开行 7.8 亿元支持内蒙古乌兰察布 3 个算力基础设施项目；7000 万元支持
    歌尔股份 AI 驱动 VR 可穿戴产品工厂；1.02 亿元支持欣旺达储能项目。
  · 9 月金融数据：委托贷款新增 802 亿元，企业中长期贷款新增 8900 亿元。

输出目录 = 脚本所在目录
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

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
    """三家银行的账本"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "8000 亿怎么分的，撬动了多少",
           "截至 2026 年 10 月 28 日，三家政策性银行全部完成投放")

    rows = [
        ("国开行", 3650, "5.5 万亿元", NAVY),
        ("农发行", 3150, "4.39 万亿元", TEAL),
        ("进出口银行", 1200, "逾 1.7 万亿元", SLATE),
    ]
    y = 0.655
    for name, amt, total, color in rows:
        card(ax, 0.045, y, 0.910, 0.110, LIGHT, lw=1.1)
        ax.text(0.070, y + 0.074, name, fontsize=11.0, color=DARK,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(0.300, y + 0.074, "%d 亿元" % amt, fontsize=12.4, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(0.520, y + 0.074, "涉及项目总投资 " + total, fontsize=9.2,
                color=SLATE, ha="left", va="center", zorder=6)
        bar_w = amt / 4000.0 * 0.330
        ax.add_patch(FancyBboxPatch(
            (0.070, y + 0.024), max(bar_w, 0.012), 0.015,
            boxstyle="round,pad=0.0,rounding_size=0.005",
            facecolor=color, edgecolor="none", linewidth=0, zorder=6))
        y -= 0.125

    card(ax, 0.045, 0.215, 0.910, 0.135, NAVY, face=PALE, lw=1.3)
    ax.text(0.070, 0.315, "8000 亿元  →  约 11.59 万亿元", fontsize=13.6,
            color=NAVY, weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.070, 0.258,
            "全部用于补充项目资本金，杠杆撬动逾 14 倍；较 2025 年的 5000 亿元增加 3000 亿元。",
            fontsize=9.2, color=SLATE, ha="left", va="center", zorder=6)

    punchline(fig, "它不盖楼、不买设备，只替项目垫上开工前那笔资本金。")
    footer(fig, "事实来源：新华社 2026-10-28；经济参考报 2026-10-29；"
                "21 世纪经济报道 2026-10-29；第一财经 2026-10-29")
    fig.savefig(OUT + "图1_三家账本.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """两年对比：额度、节奏、去向"""
    fig = plt.figure(figsize=(12, 6.9))

    header(fig, "额度涨了六成，节奏反而放慢",
           "2025 年一个月投完 5000 亿，2026 年用近两个月投完 8000 亿")

    ax = fig.add_axes([0.105, 0.400, 0.360, 0.330])
    labels = ["2025 年", "2026 年"]
    vals = [5000, 8000]
    bars = ax.bar([0, 1], vals, width=0.46, color=[LIGHT, NAVY], zorder=3)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(labels, fontsize=10.0, color=SLATE)
    ax.set_ylim(0, 9600)
    ax.set_yticks([])
    ax.set_title("投放规模  亿元", fontsize=10.2, color=SLATE, pad=12)
    for spine in ("top", "right", "left"):
        ax.spines[spine].set_visible(False)
    ax.spines["bottom"].set_color(LIGHT)
    ax.tick_params(colors=GRAY)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + 160, "%d" % v,
                fontsize=11.0, color=DARK, weight="bold", ha="center",
                va="bottom")

    axf = new_axes(fig)
    card(axf, 0.510, 0.400, 0.445, 0.330, TEAL, lw=1.4)
    axf.text(0.535, 0.685, "为什么慢了，反而更合理", fontsize=10.6, color=TEAL,
             weight="bold", ha="left", va="center", zorder=6)
    axf.text(0.535, 0.635,
             "今年进一步向新兴产业倾斜，这类项目尽调更复杂、\n"
             "资本金合规要求更严，需要时间筛选论证；\n"
             "平滑投放也能减少资金闲置。",
             fontsize=9.0, color=SLATE, ha="left", va="top",
             linespacing=1.95, zorder=6)
    axf.text(0.535, 0.500,
             "同期金融数据：9 月委托贷款新增 802 亿元、\n"
             "企业中长期贷款新增 8900 亿元。",
             fontsize=9.0, color=DARK, ha="left", va="top",
             linespacing=1.95, zorder=6)

    axf.text(0.045, 0.300,
             "额度多了 60%，时间多了一倍——这一次的取向是“挑项目”，不是“赶进度”。",
             fontsize=9.8, color=DARK, ha="left", va="center")

    punchline(fig, "投放慢下来，说明这轮钱挑得更细。")
    footer(fig, "事实来源：21 世纪经济报道 2026-10-29（节奏与节奏解释、9 月金融数据引述）；"
                "新华社 2026-10-28")
    fig.savefig(OUT + "图2_两年对比.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """钱去了哪"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "三个去向，一个案例",
           "新兴产业约占一半，民间投资超三成，七成落在经济大省")

    items = [
        ("新兴产业", "国开行 49%（1790.1 亿元）\n农发行约 60%（近 2000 亿元）\n进出口银行近五成", NAVY),
        ("民间投资", "国开行 35.1%（1279.9 亿元）\n农发行 20.7%（651.54 亿元）\n进出口银行近四成", TEAL),
        ("经济大省", "国开行 76.1%（2778.6 亿元，11 省）\n进出口银行超七成（330 余个项目）", SLATE),
    ]
    x = 0.045
    w = 0.288
    for title, note, color in items:
        card(ax, x, 0.430, w, 0.310, color, lw=1.4)
        ax.text(x + 0.022, 0.690, title, fontsize=10.8, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(x + 0.022, 0.645, note, fontsize=8.6, color=SLATE,
                ha="left", va="top", linespacing=1.95, zorder=6)
        x += w + 0.023

    card(ax, 0.045, 0.235, 0.910, 0.150, RED, face=PALE, lw=1.2)
    ax.text(0.070, 0.345, "落到具体项目上是什么样", fontsize=10.4, color=RED,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.070, 0.300,
            "国开行 7.8 亿元支持内蒙古乌兰察布 3 个算力基础设施项目；7000 万元支持歌尔股份 "
            "AI 驱动的 VR 工厂；\n1.02 亿元支持欣旺达储能项目。农发行项目数占全国六成以上，"
            "市县级客户占 63%。",
            fontsize=8.8, color=SLATE, ha="left", va="top",
            linespacing=1.95, zorder=6)

    punchline(fig, "同样是政策性资金，落点从“修路架桥”挪到了“算力、储能、产线”。")
    footer(fig, "事实来源：21 世纪经济报道 2026-10-29；第一财经 2026-10-29（三家银行投放结构与案例）")
    fig.savefig(OUT + "图3_钱去了哪.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)