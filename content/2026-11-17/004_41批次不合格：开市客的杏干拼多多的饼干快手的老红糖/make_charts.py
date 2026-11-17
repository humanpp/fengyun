# -*- coding: utf-8 -*-
"""
《41 批次不合格：开市客的杏干、拼多多的饼干、快手的老红糖》配套图表
事实口径：2026-11-16 市场监管总局通报 41 批次食品抽检不合格、共抽检 1459 批次；
开市客（南京）土耳其进口杏干（山梨酸及其钾盐超标）；拼多多"霍尔果斯丝路甄选
中亚馆"哈萨克斯坦饼干（山梨酸超标）；快手"优选零食贰号店"老红糖（二氧化硫残留
量不合格）；另有贵州煨酒（甜蜜素）、宿州金钱饼（柠檬黄）、滑县食醋（甜蜜素）、
喀什辣椒酱（苯甲酸）。
风格：克制传媒风，白底、低饱和配色、标题即结论
输出目录 = 脚本所在目录
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch

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

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep


def footer(fig, text):
    fig.text(0.045, 0.020, text, fontsize=8.4, color=GRAY, ha="left", va="bottom")


def punchline(fig, text):
    fig.text(0.045, 0.072, text, fontsize=10.4, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


# ---------------------------------------------------------------- 图 1
def fig1():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.135, 0.910, 0.690])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "41 批次里，三个你熟悉的渠道", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.888, "11 月 16 日市场监管总局通报，本次抽检 1459 批次样品",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    stats = [
        (0.150, "41", "批次不合格", RED),
        (0.500, "1459", "批次被抽检", NAVY),
        (0.850, "约 2.8%", "不合格占比", SLATE),
    ]
    for x, num, label, color in stats:
        ax.text(x, 0.905, num, fontsize=27, color=color, weight="bold",
                ha="center", va="center")
        ax.text(x, 0.838, label, fontsize=9.6, color=GRAY, ha="center",
                va="center")

    cards = [
        ("开市客", "南京 · 会员制商超", "土耳其进口杏干", "山梨酸及其钾盐超标"),
        ("拼多多", "霍尔果斯丝路甄选中亚馆", "哈萨克斯坦饼干", "山梨酸超标"),
        ("快手", "优选零食贰号店", "老红糖", "二氧化硫残留量不合格"),
    ]

    top, bot = 0.740, 0.330
    for i, (channel, shop, goods, issue) in enumerate(cards):
        x0 = 0.012 + i * 0.338
        ax.add_patch(Rectangle((x0, bot), 0.300, top - bot, facecolor=PALE,
                               edgecolor=LIGHT, linewidth=1.0))
        ax.add_patch(Rectangle((x0, top - 0.012), 0.300, 0.012, facecolor=NAVY,
                               edgecolor="none"))
        ax.text(x0 + 0.022, top - 0.060, channel, fontsize=14, color=NAVY,
                weight="bold", va="center")
        ax.text(x0 + 0.022, top - 0.118, shop, fontsize=9, color=GRAY,
                va="center")
        ax.text(x0 + 0.022, top - 0.188, goods, fontsize=12.4, color=DARK,
                weight="bold", va="center")
        ax.plot([x0 + 0.022, x0 + 0.278], [top - 0.235, top - 0.235],
                color=LIGHT, linewidth=1.0)
        ax.text(x0 + 0.022, top - 0.285, issue, fontsize=10.2, color=RED,
                weight="bold", va="center")

    ax.add_patch(Rectangle((0.012, 0.130), 0.976, 0.150, facecolor="white",
                           edgecolor=LIGHT, linewidth=1.0))
    ax.text(0.032, 0.232, "名单上还有这几样：", fontsize=9.4, color=GRAY,
            va="center")
    ax.text(0.032, 0.176,
            "贵州煨酒（甜蜜素）·  宿州金钱饼（柠檬黄）·  滑县食醋（甜蜜素）·  喀什辣椒酱（苯甲酸）",
            fontsize=10.2, color=DARK, va="center")

    footer(fig, "数据据 2026 年 11 月 16 日市场监管总局抽检通报；2.8% 为 41÷1459 推算值。")
    fig.savefig(OUT + "图1_三个渠道.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.135, 0.910, 0.690])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "五个名字，五种用途", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.882, "不用记化学式，知道它是干什么的，就够了",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    ax.text(0.030, 0.808, "不合格项目", fontsize=10.2, color=GRAY, weight="bold",
            va="center")
    ax.text(0.330, 0.808, "它是干什么的", fontsize=10.2, color=GRAY, weight="bold",
            va="center")
    ax.text(0.640, 0.808, "这次出现在", fontsize=10.2, color=GRAY, weight="bold",
            va="center")
    ax.plot([0.012, 0.988], [0.775, 0.775], color=LIGHT, linewidth=1.4)

    rows = [
        ("山梨酸及其钾盐", "防腐剂，延长保质期", "进口杏干、哈萨克斯坦饼干"),
        ("二氧化硫", "漂白、防腐，让颜色好看", "老红糖"),
        ("甜蜜素", "甜味剂，代替一部分糖", "贵州煨酒、滑县食醋"),
        ("柠檬黄", "色素，让颜色更讨喜", "宿州金钱饼"),
        ("苯甲酸", "防腐剂", "喀什辣椒酱"),
    ]

    for i, (item, use, where) in enumerate(rows):
        y = 0.690 - i * 0.128
        if i % 2 == 0:
            ax.add_patch(Rectangle((0.012, y - 0.058), 0.976, 0.116,
                                   facecolor=PALE, edgecolor="none"))
        ax.text(0.030, y, item, fontsize=11.4, color=DARK, weight="bold",
                va="center")
        ax.text(0.330, y, use, fontsize=10.2, color=SLATE, va="center")
        ax.text(0.640, y, where, fontsize=10.2, color=RED, va="center")

    ax.plot([0.012, 0.988], [0.058, 0.058], color=LIGHT, linewidth=1.0)
    ax.text(0.030, 0.010,
            "标准范围内允许使用；不合格指的是超出限量，或用在不该用的品类上。",
            fontsize=9.6, color=GRAY, va="center")

    footer(fig, "用途为食品添加剂公开常识；不合格项目与对应品类据 2026 年 11 月 16 日通报。")
    fig.savefig(OUT + "图2_五个名字.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.135, 0.910, 0.690])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "打开购物记录，搜五个词", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.882, "先搜品类，再看店铺和生产日期——三分钟能做完",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    words = ["杏干", "红糖", "饼干", "辣椒酱", "食醋"]
    w, gap = 0.132, 0.038
    total = len(words) * w + (len(words) - 1) * gap
    x = (1 - total) / 2
    for word in words:
        ax.add_patch(FancyBboxPatch((x, 0.700), w, 0.105,
                                    boxstyle="round,pad=0.006,rounding_size=0.020",
                                    facecolor=NAVY, edgecolor="none"))
        ax.text(x + w / 2, 0.7525, word, fontsize=14, color="white",
                weight="bold", ha="center", va="center")
        x += w + gap

    steps = [
        ("01", "对店铺", "打开订单页，看店名是不是这三家：\n开市客、拼多多「丝路甄选中亚馆」、\n快手「优选零食贰号店」。"),
        ("02", "对包装", "看生产日期、批次和生产企业，\n和通报里的品类、产地能不能对上。"),
        ("03", "留证据", "包装别扔，订单截图存好，\n打 12315，或者直接找平台客服。"),
    ]

    for i, (no, title, body) in enumerate(steps):
        x0 = 0.012 + i * 0.338
        ax.add_patch(FancyBboxPatch((x0, 0.215), 0.300, 0.400,
                                    boxstyle="round,pad=0.010,rounding_size=0.012",
                                    facecolor=PALE, edgecolor=LIGHT, linewidth=1.0))
        ax.text(x0 + 0.024, 0.560, no, fontsize=13.5, color=GRAY, weight="bold",
                va="center")
        ax.text(x0 + 0.024, 0.485, title, fontsize=14, color=NAVY,
                weight="bold", va="center")
        ax.text(x0 + 0.024, 0.415, body, fontsize=9.2, color=DARK, va="top",
                linespacing=1.85)

    punchline(fig, "吃了一半也不用慌：留下包装和订单，别再买第二单。")
    footer(fig, "涉事店铺与品类据 2026 年 11 月 16 日市场监管总局抽检通报；12315 为全国投诉举报热线。")
    fig.savefig(OUT + "图3_搜五个词.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")
