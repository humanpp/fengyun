# -*- coding: utf-8 -*-
"""
《固态电池先给机器人用，不上车：原因很现实》配套图表

事实口径：
  · 《新型电池产业发展"十五五"规划》：到 2030 年全固态电池初步实现规模化应用。
  · 利元亨今年交付数百兆瓦级全固态电池整线，覆盖混料（干法湿法并行）到高压化成。
  · 恩力动力张锋：今年是"机器人电池卡位之年"；2030 年之后再进车端。
  · 小鹏周德华：固态电池先从机器人切入，再迁移到车端。
  · 2030 展望：电动车约 3.1TWh、储能约 1.6TWh（周复）。
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "_kit")))

from chart_kit import (NAVY, RED, GRAY, SLATE, LIGHT, DARK, PALE, TEAL,
                       page, save, card, flow, columns, kpi_row, hbars)


def fig1():
    fig, ax = page(
        "落地的顺序，和想象的相反",
        "固态电池的第一批规模化客户，不是汽车",
        source="来源：中国网 2026-11-27 报道（行业会议发言）。"
               "2030 年为规划目标，非承诺时点。",
        punch="先卖给最愿意付溢价的人，再等它变便宜。",
        foot="事实来源：恩力动力张锋、小鹏汽车周德华、卫蓝新能源徐航宇在行业会议上的表述，"
             "据中国网 2026-11-27；《新型电池产业发展\"十五五\"规划》目标。")

    flow(ax, [
        ("机器人", "能量密度刚需\n价格容忍度高", NAVY),
        ("低空飞行器", "每克重量都影响滞空", TEAL),
        ("电动摩托", "迭代快、认证门槛低", SLATE),
        ("乘用车", "要既便宜又可靠\n才可能规模化", RED),
    ], y=0.610, x0=0.045, w=0.200, h=0.115, gap=0.025, arrow_color=GRAY)

    ax.text(0.045, 0.560, "现在", fontsize=7.8, color=NAVY, weight="bold",
            ha="left", va="center")
    ax.text(0.700, 0.560, "2030 年之后", fontsize=7.8, color=RED, weight="bold",
            ha="left", va="center")
    ax.plot([0.060, 0.685], [0.540, 0.540], color=LIGHT, linewidth=1.0)
    ax.plot([0.720, 0.945], [0.540, 0.540], color=LIGHT, linewidth=1.0)

    card(ax, 0.045, 0.290, 0.900, 0.195, LIGHT, face="white")
    ax.text(0.068, 0.458, "为什么车端排在最后", fontsize=8.6, color=DARK,
            weight="bold", ha="left", va="center", zorder=7)
    ax.plot([0.068, 0.922], [0.438, 0.438], color=LIGHT, linewidth=0.9, zorder=7)

    rows = [
        ("成本", "一辆 15 万的车，电池贵两三万，直接决定卖不卖得动。", RED),
        ("一致性", "车规要求百万分之一级失效率，界面阻抗与良率仍在解决。", NAVY),
        ("认证", "车规认证动辄两三年，还要叠加安全测试与整车匹配。", SLATE),
    ]
    y = 0.400
    for tag, text, color in rows:
        ax.text(0.068, y, tag, fontsize=7.8, color=color, weight="bold",
                ha="left", va="center", zorder=7)
        ax.text(0.150, y, text, fontsize=7.5, color=SLATE,
                ha="left", va="center", zorder=7)
        y -= 0.044

    save(fig, "图1_落地顺序")


def fig2():
    fig, ax = page(
        "同一块电池，两种市场的算法",
        "能量密度刚需程度，决定谁先买单",
        source="来源：张锋「机器人、无人机、电摩对能量密度要求非常高，"
               "但对价格敏感度大大低于汽车」（中国网 2026-11-27）。",
        punch="新技术落地不按「最重要的市场」排，按「最愿意付溢价的市场」排。",
        foot="说明：本图为定性对比，不对具体价格弹性作量化估计。")

    columns(ax, [
        ("早期场景", NAVY, "机器人 / 无人机 / 电摩",
         "· 能量密度是刚需，重量直接决定性能\n"
         "· 整机售价高，电池贵几千块占比小\n"
         "· 无车规级漫长准入，迭代以月计\n"
         "· 订单量小，但足以让产线跑起来",
         "诉求", "先能用，再谈便宜。\n工艺在这类场景里被磨熟。"),
        ("大众市场", RED, "乘用车",
         "· 电池是成本大头，贵两万就卖不动\n"
         "· 车规要求百万分之一级失效率\n"
         "· 认证周期两三年，叠加安全测试\n"
         "· 规模要求吉瓦时级，产线投入巨大",
         "诉求", "既便宜又可靠，缺一不可。\n所以排在最后。"),
    ], y=0.340, h=0.400, x0=0.045, gap=0.024, w=0.438)

    save(fig, "图2_两种市场的算法")


def fig3():
    fig, ax = page(
        "2030 年的两块蛋糕",
        "电动车 3.1TWh，储能 1.6TWh——固态电池要抢的是前者",
        source="来源：行业会议对 2030 年锂电市场空间的展望（周复），据中国网 2026-11-27。"
               "属预测值，非实际数据。",
        punch="储能是当下增长主力，车端是固态电池的远期目标。",
        foot="说明：3.1TWh 与 1.6TWh 均为 2030 年市场空间预测，存在偏差可能，仅示意量级对比。")

    hbars(ax, [
        ("电动车", 3.1, NAVY),
        ("储能", 1.6, TEAL),
    ], x_right=0.760, y_top=0.640, step=0.130, bar_h=0.070,
        value_fmt="{:.1f} TWh", label_size=9.0, value_size=10.0)

    card(ax, 0.045, 0.300, 0.900, 0.170, LIGHT, face=PALE)
    ax.text(0.068, 0.440, "两块蛋糕的性质不一样", fontsize=8.6, color=DARK,
            weight="bold", ha="left", va="center", zorder=7)
    ax.text(0.068, 0.400, "·　电动车：技术门槛最高，是固态电池的终局市场，也是最后才进的市场。",
            fontsize=7.6, color=SLATE, ha="left", va="center", zorder=7)
    ax.text(0.068, 0.362, "·　储能：当下拉动增长的主要力量，但对能量密度要求相对宽松。",
            fontsize=7.6, color=SLATE, ha="left", va="center", zorder=7)
    ax.text(0.068, 0.324, "·　机器人、低空、电摩：单量小，却是固态电池最早的真实订单来源。",
            fontsize=7.6, color=SLATE, ha="left", va="center", zorder=7)

    save(fig, "图3_2030的两块蛋糕")


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", os.path.dirname(os.path.abspath(__file__)))
