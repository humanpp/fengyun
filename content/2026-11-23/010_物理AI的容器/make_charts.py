# -*- coding: utf-8 -*-
"""
《AI 走出屏幕，资本先找容器》配套图表

事实口径：
  · 2026-11-23 早盘，物理AI概念股大涨：凡拓数创涨停、走出 2 连板（央广网称
    录得 20% 幅度两连板）；多伦科技涨停；上纬新材涨超 10%；宇树科技涨超 7%。
    当日午后机器人概念扩大涨幅，上纬新材 20cm 涨停，宇树科技等涨超 10%。
  · 宇树科技创始人、董事长王兴兴此前透露，前几个月公司已启动内部
    “物理AI模型自进化”计划：AI 模型自己采集数据、训练、迭代，人类只需参与打分；
    他认为当前全球顶尖大模型公司最主要的进步并非来自模型结构，而是来自这种
    自进化循环。
  · 至简动力（Simplexity Robotics），杭州，物理AI与具身机器人公司，由理想汽车
    前高管创办，联合创始人兼董事长王凯。2026-11-23 确认完成 1 亿美元 Pre-A 轮，
    蚂蚁集团领投，阿里巴巴、腾讯、红杉中国、蓝驰创投等老股东跟投，投后估值
    16 亿美元（约 106.8 亿元人民币）；此前半年内连融 5 轮、累计约 20 亿元。
    同期发布第二款人形机器人及 iX 轮式机器人，面向饮品递送、物品取送、导览、
    仓库分拣等场景做商业化探索。

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
    """当日盘面"""
    fig = plt.figure(figsize=(12, 6.9))

    header(fig, "一个早盘，四只票",
           "2026 年 11 月 23 日，物理AI 概念集体异动")

    ax = fig.add_axes([0.175, 0.345, 0.520, 0.410])
    names = ["宇树科技", "上纬新材", "多伦科技", "凡拓数创"]
    vals = [7, 10, 10, 20]
    tags = ["涨超 7%", "涨超 10%", "涨停", "涨停 · 2 连板"]
    colors = [TEAL, SLATE, RED, RED]
    bars = ax.barh([0, 1, 2, 3], vals, height=0.46, color=colors, zorder=3)
    ax.set_yticks([0, 1, 2, 3])
    ax.set_yticklabels(names, fontsize=10.2, color=SLATE)
    ax.set_xlim(0, 26)
    ax.set_ylim(-0.60, 3.60)
    ax.set_xticks([])
    ax.set_title("早盘涨幅（%）", fontsize=10.2, color=SLATE, pad=12)
    for spine in ("top", "right", "bottom"):
        ax.spines[spine].set_visible(False)
    ax.spines["left"].set_color(LIGHT)
    ax.tick_params(colors=GRAY)
    for b, v, t in zip(bars, vals, tags):
        ax.text(v + 0.6, b.get_y() + b.get_height() / 2, t, fontsize=9.8,
                color=DARK, weight="bold", va="center")

    axf = new_axes(fig)
    card(axf, 0.045, 0.195, 0.910, 0.105, LIGHT, face=PALE, lw=1.0)
    axf.text(0.070, 0.248,
             "口径提示：涨停幅度因板块而异（10% / 20%）。午后机器人概念扩大涨幅，"
             "上纬新材 20cm 涨停，宇树科技等涨超 10%。",
             fontsize=8.8, color=SLATE, ha="left", va="center", zorder=6)

    punchline(fig, "二级市场买的是概念，一级市场买的是公司。")
    footer(fig, "事实来源：上海证券报·中国证券网 2026-11-23；央广网 2026-11-23；第一财经 2026-11-23")
    fig.savefig(OUT + "图1_当日盘面.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """至简动力的三个数"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "半年，5 轮，20 亿",
           "至简动力的融资节奏，比产品节奏快得多")

    stats = [
        ("1 亿美元", "本轮 Pre-A 融资额\n蚂蚁集团领投", NAVY),
        ("16 亿美元", "投后估值\n约合人民币 106.8 亿元", RED),
        ("5 轮 / 约 20 亿元", "此前半年内连融 5 轮\n累计融资规模", TEAL),
    ]
    x = 0.045
    w = 0.288
    for big, note, color in stats:
        card(ax, x, 0.455, w, 0.280, color, lw=1.5)
        ax.text(x + 0.026, 0.660, big, fontsize=15.4 if len(big) < 10 else 12.6,
                color=color, weight="bold", ha="left", va="center", zorder=6)
        ax.text(x + 0.026, 0.590, note, fontsize=8.8, color=SLATE,
                ha="left", va="top", linespacing=1.85, zorder=6)
        x += w + 0.023

    card(ax, 0.045, 0.235, 0.910, 0.170, LIGHT, lw=1.0)
    ax.text(0.070, 0.355, "钱换来了什么", fontsize=10.2, color=DARK,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.070, 0.310,
            "同期发布第二款人形机器人与 iX 轮式机器人，已面向饮品递送、物品取送、导览、\n"
            "仓库分拣等场景做商业化探索；老股东阿里巴巴、腾讯、红杉中国、蓝驰创投跟投。",
            fontsize=9.0, color=SLATE, ha="left", va="top",
            linespacing=1.95, zorder=6)

    punchline(fig, "估值 16 亿美元，对应的是还没规模化的交付。")
    footer(fig, "事实来源：彭博社 2026-11-23（经联合早报、虎嗅、动点科技、网易科技转述）；"
                "董事长王凯确认融资与估值")
    fig.savefig(OUT + "图2_至简动力的三个数.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """两个概念，两个落点"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "同一个热词，两个落点",
           "物理AI 讲的是模型怎么变强，具身智能讲的是机器人怎么交货")

    card(ax, 0.045, 0.330, 0.440, 0.430, NAVY, lw=1.5)
    ax.text(0.070, 0.710, "物理AI", fontsize=13.0, color=NAVY,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.070, 0.665, "核心问题：模型在物理世界里，能不能自己变强", fontsize=8.8,
            color=GRAY, ha="left", va="center", zorder=6)
    ax.text(0.070, 0.615,
            "主张：AI 自己采集数据、训练、迭代，\n"
            "人类只负责打分（王兴兴的说法）\n\n"
            "证据形态：内部计划、技术路线\n"
            "可验证指标：单位算力下的能力增速\n"
            "眼下的状态：讲得清逻辑，拿不出财报",
            fontsize=9.2, color=SLATE, ha="left", va="top",
            linespacing=1.95, zorder=6)

    card(ax, 0.515, 0.330, 0.440, 0.430, RED, lw=1.5)
    ax.text(0.540, 0.710, "具身智能", fontsize=13.0, color=RED,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.540, 0.665, "核心问题：机器人能不能按时交付、被人用起来", fontsize=8.8,
            color=GRAY, ha="left", va="center", zorder=6)
    ax.text(0.540, 0.615,
            "主张：软硬件全栈自研，用模型定义本体\n\n"
            "证据形态：产品型号、场景、订单\n"
            "可验证指标：交付量、单机成本、复购\n"
            "眼下的状态：有产品和场景，规模未起",
            fontsize=9.2, color=SLATE, ha="left", va="top",
            linespacing=1.95, zorder=6)

    ax.text(0.045, 0.245,
            "两件事同一天发生，被同一个词概括；但一个卖的是效率叙事，一个卖的是硬件交付。",
            fontsize=9.6, color=DARK, ha="left", va="center")

    punchline(fig, "容器先找到了，里面装什么还没定。")
    footer(fig, "事实来源：王兴兴公开表述（经上海证券报转述）；至简动力融资与产品信息（彭博社，"
                "经虎嗅、网易科技转述）；框架为本文分析")
    fig.savefig(OUT + "图3_两个落点.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)