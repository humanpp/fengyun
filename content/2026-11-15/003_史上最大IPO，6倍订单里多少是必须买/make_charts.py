# -*- coding: utf-8 -*-
"""
《史上最大 IPO：6 倍订单里，有多少是“必须买”》配套图表
事实来源：彭博社 2026-11-13、Anthropic 招股文件、CNBC/金融时报、
Odaily/财经杂志、财联社/经济观察网/21 世纪经济报道
风格：克制传媒风，白底、低饱和配色、标题即结论
输出目录 = 脚本所在目录
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["figure.facecolor"] = "white"
plt.rcParams["axes.facecolor"] = "white"

NAVY = "#1f3a5f"
RED = "#b5544a"
GRAY = "#8a8f98"
LIGHT = "#d8dbe0"
DARK = "#2b2f36"
PALE = "#eef0f3"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep


def footer(fig, text):
    fig.text(0.045, 0.020, text, fontsize=8.4, color=GRAY, ha="left", va="bottom")


def takeaway(fig, y, text, size=10.4):
    fig.text(0.045, y, text, fontsize=size, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


# ---------------------------------------------------------------- 图 1
def fig1():
    fig, ax = plt.subplots(figsize=(12, 6.8))
    fig.subplots_adjust(left=0.045, right=0.955, top=0.765, bottom=0.175)

    fig.suptitle("6 倍订单，是三层东西叠在一起",
                 fontsize=19, color=DARK, x=0.045, ha="left", y=0.955, weight="bold")
    fig.text(0.045, 0.888,
             "同一份认购数据里，三种动机同时存在，且无法拆分",
             fontsize=10.8, color=GRAY, ha="left")

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 4.95)
    ax.axis("off")

    layers = [
        ("看好基本面", "愿意在上市前锁价", "真金白银判断", NAVY,
         "机构按 DCF、按收入曲线、按竞争格局定价"),
        ("必须配权重", "指数基金与 ETF 自动买入", "不问价格", RED,
         "上市即按权重被动流入，数百亿美元规模"),
        ("不敢偏离基准", "主动基金怕跑输", "职业风险", GRAY,
         "不买＝主动偏离，跌了也不比同行更差"),
    ]

    for i, (title, sub, tag, color, note) in enumerate(layers):
        y = 3.48 - i * 1.22
        ax.add_patch(plt.Rectangle((0.020, y - 0.48), 0.960, 0.96,
                                   facecolor=PALE, edgecolor=LIGHT, linewidth=1.0))
        ax.add_patch(plt.Rectangle((0.020, y - 0.48), 0.008, 0.96,
                                   facecolor=color, edgecolor="none"))
        ax.text(0.052, y + 0.22, title, fontsize=13.5, color=color,
                weight="bold", va="center")
        ax.text(0.052, y - 0.10, sub, fontsize=10.4, color=DARK, va="center")
        ax.text(0.052, y - 0.33, note, fontsize=9.0, color=GRAY, va="center")
        ax.text(0.950, y + 0.22, tag, fontsize=12, color=color,
                weight="bold", ha="right", va="center",
                bbox=dict(boxstyle="round,pad=0.42", facecolor="white",
                          edgecolor=color, linewidth=1.2))

    takeaway(fig, 0.085, "所以“6 倍”只能证明需求强度，证明不了估值水平。")

    footer(fig, "据彭博社 2026-11-13 报道及公开市场机制整理；三层比例为本文归纳，非披露数据。")
    fig.savefig(OUT + "图1_六倍订单的三层成分.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig, ax = plt.subplots(figsize=(12, 6.8))
    fig.subplots_adjust(left=0.045, right=0.955, top=0.765, bottom=0.175)

    fig.suptitle("定价窗口，撞上叙事动摇的窗口",
                 fontsize=19, color=DARK, x=0.045, ha="left", y=0.955, weight="bold")
    fig.text(0.045, 0.888,
             "2026 年 11 月：Anthropic 上市与英伟达财报几乎重叠",
             fontsize=10.8, color=GRAY, ha="left")

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 5.35)
    ax.axis("off")

    ax.plot([0.088, 0.088], [0.55, 5.00], color=LIGHT, lw=2.2, zorder=1)

    events = [
        ("11.10", "Anthropic 提交修订版招股文件", "定价 70–78 美元，发行 8.25 亿股", GRAY),
        ("11.12", "黄仁勋辞任英伟达 CEO", "当日收跌 4.34%，市值蒸发近 1820 亿美元", RED),
        ("11.13", "6 倍超额认购曝光", "费城半导体指数一度跌超 6%，AMD 跌 10%", NAVY),
        ("11.17", "英伟达 Q3 财报（盘后）", "主持电话会的是临时 CEO 克雷斯，不是黄仁勋", RED),
        ("11.18", "Anthropic 定价", "需要一个稳定的产业叙事背景", NAVY),
        ("11.19", "以 ANT 登陆纳斯达克", "上市首日表现接受检验", NAVY),
    ]

    for i, (date, what, note, color) in enumerate(events):
        y = 4.72 - i * 0.80
        ax.add_patch(plt.Circle((0.088, y), 0.009, facecolor=color,
                                edgecolor="white", linewidth=1.6, zorder=4))
        ax.text(0.020, y, date, fontsize=11, color=color, weight="bold",
                va="center", ha="left")
        ax.text(0.125, y + 0.135, what, fontsize=11.2, color=DARK,
                weight="bold", va="center")
        ax.text(0.125, y - 0.135, note, fontsize=10, color=GRAY, va="center")

    takeaway(fig, 0.075, "前者要后者确认“算力需求是真的”，后者要回答“这些钱能不能赚回来”。")

    footer(fig, "据 CNBC、财联社、经济观察网、21 世纪经济报道、工商时报公开报道整理。")
    fig.savefig(OUT + "图2_两个窗口重叠.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig, ax = plt.subplots(figsize=(12, 6.8))
    fig.subplots_adjust(left=0.045, right=0.955, top=0.765, bottom=0.175)

    fig.suptitle("260 亿美元的两种解释，账上分不开",
                 fontsize=19, color=DARK, x=0.045, ha="left", y=0.955, weight="bold")
    fig.text(0.045, 0.888,
             "七家基石投资者：既是现有股东，也全部是付费客户",
             fontsize=10.8, color=GRAY, ha="left")

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 4.55)
    ax.axis("off")

    # 左右两栏
    ax.add_patch(plt.Rectangle((0.030, 1.55), 0.400, 2.55,
                               facecolor=PALE, edgecolor=LIGHT, linewidth=1.0))
    ax.add_patch(plt.Rectangle((0.570, 1.55), 0.400, 2.55,
                               facecolor="#f3eceb", edgecolor=LIGHT, linewidth=1.0))

    ax.text(0.230, 3.85, "解释一：看好", fontsize=14, color=NAVY,
            weight="bold", ha="center")
    ax.text(0.230, 3.42, "愿意在公开市场之前锁价", fontsize=10.6,
            color=DARK, ha="center")
    for i, ln in enumerate(["按基本面定价", "长期持有意图", "对 Anthropic 的判断"]):
        ax.text(0.230, 3.00 - i * 0.36, "· " + ln, fontsize=10, color=GRAY,
                ha="center")

    ax.text(0.770, 3.85, "解释二：换订单", fontsize=14, color=RED,
            weight="bold", ha="center")
    ax.text(0.770, 3.42, "用股权换算力上的确定性", fontsize=10.6,
            color=DARK, ha="center")
    for i, ln in enumerate(["继续买自家芯片", "锁定产能与配额", "把补贴记成投资"]):
        ax.text(0.770, 3.00 - i * 0.36, "· " + ln, fontsize=10, color=GRAY,
                ha="center")

    # 中间问号
    ax.text(0.500, 2.85, "？", fontsize=30, color=DARK, ha="center",
            va="center", weight="bold")

    ax.add_patch(plt.Rectangle((0.115, 0.42), 0.770, 0.92,
                               facecolor="white", edgecolor=DARK, linewidth=1.2))
    ax.text(0.500, 1.05, "当买方同时是供应商和股东，两种解释都成立，",
            fontsize=12, color=DARK, ha="center", va="center", weight="bold")
    ax.text(0.500, 0.70, "而这笔钱在账上，只有一行。",
            fontsize=11.5, color=RED, ha="center", va="center", weight="bold")

    footer(fig, "据招股文件与公开报道整理；七家为谷歌、英伟达、AMD、博通、美光、微软、台积电等。")
    fig.savefig(OUT + "图3_260亿的两种解释.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")
