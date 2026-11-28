# -*- coding: utf-8 -*-
"""
《上海工厂 500 万辆下线，这厂越来越像出口基地》配套图表

事实口径（车研网 2026-11-27；盖世汽车 2026-11-27）：
  · 特斯拉副总裁陶琳 2026-11-25 透露：上海超级工厂第 500 万辆整车即将下线。
  · 该厂 2026 年前 10 个月出口 42 万辆、同比翻倍；零售端承压，产能向出口倾斜。
  · 2026 年前 9 个月中国产电动车占韩国新注册乘用 EV 四成三。
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "_kit")))

from chart_kit import (NAVY, RED, GRAY, SLATE, LIGHT, DARK, PALE, TEAL,
                       page, save, card, flow, kpi_row, columns)


def fig1():
    fig, ax = page(
        "500 万辆是里程碑，42 万辆才是信息",
        "一辆车从「在中国卖」到「从中国卖到全世界」",
        source="来源：车研网 2026-11-27。500 万辆为累计产量口径；42 万辆为 2026 年前 10 个月出口量。",
        punch="产能在哪里，正在变成一件需要在谈判桌上讨论的事。",
        foot="事实来源：第 500 万辆整车即将下线（2026-11-25 陶琳透露）；前 10 个月出口 42 万辆、同比翻倍。")

    card(ax, 0.045, 0.470, 0.400, 0.200, NAVY, lw=1.3)
    ax.text(0.070, 0.628, "累计产量", fontsize=8.4, color=NAVY,
            weight="bold", ha="left", va="center", zorder=7)
    ax.text(0.070, 0.565, "500 万辆", fontsize=25.0, color=NAVY,
            weight="bold", ha="left", va="center", zorder=7)
    ax.text(0.070, 0.505, "全球汽车工业第一梯队", fontsize=7.6, color=SLATE,
            ha="left", va="center", zorder=7)

    card(ax, 0.545, 0.470, 0.400, 0.200, TEAL, lw=1.3)
    ax.text(0.570, 0.628, "前 10 个月出口", fontsize=8.4, color=TEAL,
            weight="bold", ha="left", va="center", zorder=7)
    ax.text(0.570, 0.565, "42 万辆", fontsize=25.0, color=TEAL,
            weight="bold", ha="left", va="center", zorder=7)
    ax.text(0.570, 0.505, "同比翻倍", fontsize=7.6, color=SLATE,
            ha="left", va="center", zorder=7)

    card(ax, 0.045, 0.300, 0.900, 0.135, LIGHT, face="white")
    ax.text(0.068, 0.402, "为什么信息在第二个数字里", fontsize=8.6, color=DARK,
            weight="bold", ha="left", va="center", zorder=7)
    ax.text(0.068, 0.360, "500 万辆说明制造能力强——这是过去。",
            fontsize=8.0, color=SLATE, ha="left", va="center", zorder=7)
    ax.text(0.068, 0.325, "42 万辆说明产能正在向外走——这是未来。",
            fontsize=8.0, color=RED, weight="bold", ha="left", va="center", zorder=7)

    save(fig, "图1_五百万辆的量级")


def fig2():
    fig, ax = page(
        "两个方向，同一个决策",
        "国内竞争最烈，海外价格更好",
        source="来源：车研网、盖世汽车 2026-11-27。出口数据为 2026 年前 10 个月。",
        punch="用中国最好的制造能力，去供应全球价格更高的市场。",
        foot="说明：本图为产能分配的机制说明，企业未公布产能分配的具体比例。")

    rows = [
        ("国内市场", "竞争烈度全球最高", "价格战、迭代快、配置内卷，份额争夺成本极高。", RED),
        ("海外市场", "价格与利润空间更好", "中国供应链成本全球稀缺，出口比本地生产更划算。", TEAL),
    ]
    y = 0.620
    for name, label, note, color in rows:
        card(ax, 0.045, y - 0.130, 0.900, 0.145, color, lw=1.3)
        ax.text(0.070, y - 0.018, name, fontsize=9.2, color=color,
                weight="bold", ha="left", va="center", zorder=7)
        ax.text(0.230, y - 0.018, label, fontsize=8.4, color=DARK,
                ha="left", va="center", zorder=7)
        ax.text(0.070, y - 0.070, note, fontsize=7.5, color=SLATE,
                ha="left", va="center", zorder=7)
        y -= 0.170

    card(ax, 0.045, 0.205, 0.900, 0.090, LIGHT, face=PALE)
    ax.text(0.068, 0.265, "旁证：2026 年前 9 个月，中国产电动车占韩国新注册乘用电动车四成三。",
            fontsize=7.8, color=SLATE, ha="left", va="center", zorder=7)
    ax.text(0.068, 0.232, "北美也在为产能去留焦虑——加拿大表态愿以现金激励挽留 Stellantis 工厂。",
            fontsize=7.8, color=SLATE, ha="left", va="center", zorder=7)

    save(fig, "图2_两个方向")


def fig3():
    fig, ax = page(
        "角色的转变",
        "从「在中国的工厂」，到「中国的全球工厂」",
        source="来源：基于公开报道的产业观察。",
        punch="国内消费者会持续受益——竞争最激烈的市场，产品最好、价格最低。",
        foot="说明：本图为角色变化的归纳，不代表任何具体企业的战略表述。")

    flow(ax, [
        ("过去", "建厂为了卖车\n给中国人", GRAY),
        ("现在", "用中国供应链\n供应全球", NAVY),
        ("结果", "中国市场变成\n基地＋红海", TEAL),
    ], y=0.590, x0=0.080, w=0.250, h=0.135, gap=0.065, arrow_color=GRAY)

    card(ax, 0.045, 0.310, 0.900, 0.200, LIGHT, face="white")
    ax.text(0.068, 0.478, "对普通人的三层影响", fontsize=8.6, color=DARK,
            weight="bold", ha="left", va="center", zorder=7)
    ax.plot([0.068, 0.922], [0.458, 0.458], color=LIGHT, linewidth=0.9, zorder=7)

    rows = [
        ("车型", "很多车在中国与海外同源，质量统一，但专属定制少了。"),
        ("保值", "出口旺盛的车型，零配件与售后未必萎缩，对残值是隐性支撑。"),
        ("判断", "别把「工厂在哪」当品质保证，看具体车型的配置与测试标准。"),
    ]
    y = 0.420
    for tag, text in rows:
        ax.text(0.068, y, tag, fontsize=7.8, color=NAVY, weight="bold",
                ha="left", va="center", zorder=7)
        ax.text(0.150, y, text, fontsize=7.5, color=SLATE,
                ha="left", va="center", zorder=7)
        y -= 0.042

    save(fig, "图3_角色的转变")


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", os.path.dirname(os.path.abspath(__file__)))
