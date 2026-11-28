# -*- coding: utf-8 -*-
"""
《合资电车涨了 69%，但份额只有 5.9%》配套图表

事实口径（乘联分会数据，经新浪网 2026-11-27 报道）：
  · 2026 年 10 月国内新能源乘用车零售同比 -13.7%。
  · 主流合资品牌新能源零售同比 +69%，内部渗透率由约 7% 升至 19.7%。
  · 合资新能源零售份额仍仅 5.9%；增量仅补上燃油车萎缩的一成出头。
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "_kit")))

from chart_kit import (NAVY, RED, GRAY, SLATE, LIGHT, DARK, PALE, TEAL,
                       page, save, card, kpi_row, columns, flow)


def fig1():
    fig, ax = page(
        "69% 和 5.9%，都是真的",
        "只看一个数，就会误判",
        source="来源：乘联分会数据，经新浪网 2026-11-27 报道。两个百分比分母不同，不可直接比较。",
        punch="结构性回归，不是反转。",
        foot="事实来源：合资新能源零售同比 +69%、内部渗透率 7%→19.7%、份额 5.9%，"
             "据乘联分会数据（2026 年 10 月）。")

    card(ax, 0.045, 0.470, 0.400, 0.200, TEAL, lw=1.3)
    ax.text(0.070, 0.628, "合资新能源零售同比", fontsize=8.4, color=TEAL,
            weight="bold", ha="left", va="center", zorder=7)
    ax.text(0.070, 0.565, "+69%", fontsize=30.0, color=TEAL,
            weight="bold", ha="left", va="center", zorder=7)
    ax.text(0.070, 0.505, "低基数上的高增长", fontsize=7.6, color=SLATE,
            ha="left", va="center", zorder=7)

    card(ax, 0.545, 0.470, 0.400, 0.200, RED, lw=1.3)
    ax.text(0.570, 0.628, "合资新能源零售份额", fontsize=8.4, color=RED,
            weight="bold", ha="left", va="center", zorder=7)
    ax.text(0.570, 0.565, "5.9%", fontsize=30.0, color=RED,
            weight="bold", ha="left", va="center", zorder=7)
    ax.text(0.570, 0.505, "全市场新能源车里占的比例", fontsize=7.6, color=SLATE,
            ha="left", va="center", zorder=7)

    card(ax, 0.045, 0.300, 0.900, 0.135, LIGHT, face="white")
    ax.text(0.068, 0.402, "更要紧的一句话", fontsize=8.6, color=DARK,
            weight="bold", ha="left", va="center", zorder=7)
    ax.text(0.068, 0.358, "合资新能源的增量，只够补上燃油车萎缩的一成出头。",
            fontsize=9.0, color=RED, weight="bold", ha="left", va="center", zorder=7)
    ax.text(0.068, 0.322, "总量还在往下走——它们不是在和自主竞争，是在和时间竞争。",
            fontsize=7.6, color=SLATE, ha="left", va="center", zorder=7)

    save(fig, "图1_两个数字")


def fig2():
    fig, ax = page(
        "两个百分比，两个分母",
        "内部渗透率说的是「自己进步了多少」，份额说的是「在大盘里占多少」",
        source="来源：乘联分会数据。本图用小店作类比，仅帮助理解分母差异。",
        punch="自己在进步，但在大盘里仍然很小。",
        foot="说明：19.7% 的分母为合资品牌总销量；5.9% 的分母为全市场新能源销量。")

    rows = [
        ("内部渗透率", "19.7%", "分母：合资品牌自己的总销量",
         "合资卖出的车里，约两成是新能源。", TEAL),
        ("市场份额", "5.9%", "分母：全市场新能源销量",
         "全市场的新能源车里，合资占不到六个点。", RED),
    ]
    y = 0.680
    for name, num, base, note, color in rows:
        card(ax, 0.045, y - 0.125, 0.900, 0.150, color, lw=1.3)
        ax.text(0.070, y - 0.020, name, fontsize=9.2, color=color,
                weight="bold", ha="left", va="center", zorder=7)
        ax.text(0.290, y - 0.020, num, fontsize=20.0, color=color,
                weight="bold", ha="left", va="center", zorder=7)
        ax.text(0.470, y - 0.005, base, fontsize=7.8, color=DARK,
                ha="left", va="center", zorder=7)
        ax.text(0.470, y - 0.048, note, fontsize=7.4, color=SLATE,
                ha="left", va="center", zorder=7)
        y -= 0.175

    card(ax, 0.045, 0.265, 0.900, 0.090, LIGHT, face=PALE)
    ax.text(0.068, 0.327, "类比：一家小店线上订单占自己营业额两成，"
                          "但整个商圈的外卖市场里只占五个点。",
            fontsize=7.8, color=SLATE, ha="left", va="center", zorder=7)
    ax.text(0.068, 0.292, "这两个「占比」说的不是一回事。",
            fontsize=8.0, color=DARK, weight="bold", ha="left", va="center", zorder=7)

    save(fig, "图2_两个分母")


def fig3():
    fig, ax = page(
        "合资开始补课的三步",
        "放下「全球平台优先」，接受「在中国、为中国」",
        source="来源：基于 2026-11-27 公开报道的产业观察。",
        punch="产品一旦跟上，渠道与服务的长板才能发挥作用。",
        foot="说明：本图为策略变化的归纳，不代表任何具体企业的战略表述。")

    flow(ax, [
        ("用中国供应链", "本土平台、本土电池\n本土智能方案", NAVY),
        ("价格对标自主", "进入 13–15 万\n主力价格带", TEAL),
        ("渠道与服务", "密集网点与售后\n是新势力难复制的", RED),
    ], y=0.590, x0=0.080, w=0.250, h=0.135, gap=0.065, arrow_color=GRAY)

    card(ax, 0.045, 0.310, 0.900, 0.200, LIGHT, face="white")
    ax.text(0.068, 0.478, "但真正的障碍不在产品", fontsize=8.6, color=DARK,
            weight="bold", ha="left", va="center", zorder=7)
    ax.plot([0.068, 0.922], [0.458, 0.458], color=LIGHT, linewidth=0.9, zorder=7)

    rows = [
        ("品牌认知", "「电车」和「新势力／自主」在很多人心里是绑定的。"),
        ("智能标签", "消费者对电车的期待里，智能座舱与辅助驾驶权重很高。"),
        ("决策机制", "两方股东协商，稳定期是优势，快变期是负担。"),
    ]
    y = 0.420
    for tag, text in rows:
        ax.text(0.068, y, tag, fontsize=7.8, color=NAVY, weight="bold",
                ha="left", va="center", zorder=7)
        ax.text(0.180, y, text, fontsize=7.5, color=SLATE,
                ha="left", va="center", zorder=7)
        y -= 0.042

    save(fig, "图3_合资的三步补课")


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", os.path.dirname(os.path.abspath(__file__)))
