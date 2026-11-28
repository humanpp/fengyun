# -*- coding: utf-8 -*-
"""
《电子行业利润涨了一倍，为什么你一点感觉都没有》配套图表

事实口径（国家统计局，2026 年 1—10 月）：
  · 电子行业利润同比 +1.0 倍，拉动全部规模以上工业企业利润增长 9.7 个百分点。
  · 计算机整机制造 +4.1 倍；电子专用材料制造 +2.2 倍；计算机外围设备制造 +2.0 倍；
    电子电路制造 +81.6%；光电子器件制造 +69.7%；半导体分立器件制造 +57.5%。
  · 戴尔 FY2027Q3：AI 优化服务器收入 220.31 亿美元，同比 +291%；
    单季新增 AI 服务器订单 602 亿美元；期末积压订单 1,323 亿美元。
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "_kit")))

from chart_kit import (NAVY, RED, GRAY, SLATE, LIGHT, DARK, PALE, TEAL,
                       page, save, card, hbars, flow, columns, kpi_row)


def fig1():
    fig, ax = page(
        "同一个行业，六个不同的温度",
        "2026 年 1—10 月电子行业细分领域利润同比增速",
        source="来源：国家统计局（规模以上工业企业口径），经南方财经网、腾讯新闻 2026-11-27 引述。"
               "增速受上年同期基数影响。",
        punch="同一个「电子行业」，内部温差可能超过 50 个百分点。",
        foot="事实来源：国家统计局，2026 年 1—10 月规模以上工业企业利润数据。"
             "「4.1 倍」即 +410%，本图统一折算为百分比。")

    hbars(ax, [
        ("计算机整机制造", 410, RED),
        ("电子专用材料制造", 220, NAVY),
        ("计算机外围设备", 200, NAVY),
        ("电子电路制造", 81.6, TEAL),
        ("光电子器件制造", 69.7, TEAL),
        ("半导体分立器件", 57.5, TEAL),
    ], x_right=0.800, y_top=0.672, step=0.070, bar_h=0.046,
        value_fmt="+{:.1f}%", label_size=8.4, value_size=8.6)

    card(ax, 0.045, 0.205, 0.900, 0.068, LIGHT, face=PALE)
    ax.text(0.068, 0.239, "全行业整体：利润同比 +1.0 倍，拉动规模以上工业企业利润增长 9.7 个百分点。",
            fontsize=7.8, color=SLATE, ha="left", va="center", zorder=7)

    save(fig, "图1_利润增速的分化")


def fig2():
    fig, ax = page(
        "营收涨两成，利润涨八成",
        "电子制造业的固定成本很高，利润弹性远大于营收",
        source="说明：本图为例示性测算，非任何企业的真实财务数据。",
        punch="「利润涨一倍」的真实含义是：产能利用率上去了。",
        foot="说明：示例假设固定成本不变、变动成本随营收同比例变化，仅用于说明经营杠杆原理。")

    rows = [
        ("营收", 10.0, 12.0, "亿元", 20, GRAY),
        ("成本", 9.0, 10.2, "亿元", 13, GRAY),
        ("利润", 1.0, 1.8, "亿元", 80, RED),
    ]
    y = 0.590
    for name, before, after, unit, pct, color in rows:
        ax.text(0.060, y, name, fontsize=9.0, color=DARK, weight="bold",
                ha="left", va="center", zorder=7)
        ax.text(0.185, y, f"{before:g} {unit}", fontsize=10.0, color=GRAY,
                ha="left", va="center", zorder=7)
        ax.annotate("", xy=(0.395, y), xytext=(0.340, y),
                    arrowprops=dict(arrowstyle="-|>", color=LIGHT, linewidth=1.4))
        ax.text(0.415, y, f"{after:g} {unit}", fontsize=10.0, color=DARK,
                ha="left", va="center", zorder=7)
        ax.text(0.620, y, f"+{pct}%", fontsize=11.0, color=color,
                weight="bold", ha="left", va="center", zorder=7)
        y -= 0.075

    card(ax, 0.045, 0.300, 0.900, 0.140, LIGHT, face="white")
    ax.text(0.068, 0.408, "为什么利润弹性这么大", fontsize=8.6, color=DARK,
            weight="bold", ha="left", va="center", zorder=7)
    ax.text(0.068, 0.360, "厂房折旧、设备、研发投入是刚性的：订单多的时候，多出来的收入几乎全是利润；"
                          "订单少的时候，少掉的收入几乎全是亏损。",
            fontsize=7.6, color=SLATE, ha="left", va="center", zorder=7)
    ax.text(0.068, 0.325, "所以同一套产能，在两个不同的开工率下，利润可以差出好几倍。",
            fontsize=7.6, color=SLATE, ha="left", va="center", zorder=7)

    save(fig, "图2_经营杠杆")


def fig3():
    fig, ax = page(
        "钱从哪来：一条最靠近订单的链",
        "AI 资本开支，先落到整机，再往上游传导",
        source="来源：戴尔投资者关系、中国证券网 2026-11-26；国家统计局 1—10 月数据。",
        punch="整机厂离订单最近，所以最先反映在利润表上。",
        foot="事实来源：戴尔 FY2027Q3 AI 服务器收入 220.31 亿美元（+291%）、"
             "单季新增订单 602 亿美元、积压订单 1,323 亿美元。")

    flow(ax, [
        ("云厂商资本开支", "算力中心建设", GRAY),
        ("服务器整机", "接单即出货", NAVY),
        ("芯片与存储", "产能紧张、涨价", TEAL),
        ("材料与设备", "扩产周期最长", SLATE),
    ], y=0.600, x0=0.045, w=0.200, h=0.115, gap=0.025, arrow_color=GRAY)

    kpi_row(ax, [
        ("AI 服务器收入", "291%", "戴尔单季同比", RED),
        ("单季新增订单", "602 亿美元", "戴尔 FY2027Q3", NAVY),
        ("期末积压订单", "1,323 亿美元", "创历史纪录", TEAL),
    ], x0=0.045, y=0.320, w_each=0.283, h=0.135, gap=0.025)

    save(fig, "图3_最靠近订单的环节")


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", os.path.dirname(os.path.abspath(__file__)))
