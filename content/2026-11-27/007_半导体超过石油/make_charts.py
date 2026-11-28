# -*- coding: utf-8 -*-
"""
《半导体出口额超过石油：世界贸易的底座，换了一块》配套图表

事实口径：
  · 德意志银行：受 AI 热潮推动，全球半导体出口总额首次超越石油与天然气（2026-11-27 报道）。
  · 2025 年全球半导体销售额 7,956 亿美元、同比 +26.2%；2026 年预计突破 1 万亿美元。
  · 2026Q1 全球销售额 2,985 亿美元、同比 +79%。
  · WSTS 预计 2026H1 7,020 亿美元、同比 +102%；存储器 +302%、逻辑电路 +42%。
  · 均据财通证券研报（经南方财经网 2026-11-27 引述）。
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "_kit")))

from chart_kit import (NAVY, RED, GRAY, SLATE, LIGHT, DARK, PALE, TEAL,
                       page, save, card, vbars, columns, flow, kpi_row)


def fig1():
    fig, ax = page(
        "斜率变了",
        "全球半导体销售额：从平稳增长，到一年翻倍",
        source="来源：财通证券研报（经南方财经网 2026-11-27 引述）、WSTS 预测。"
               "2026 年及以后为预测值。",
        punch="把出口额推过石油的，不是手机和家电，是数据中心。",
        foot="事实来源：2025 年全球半导体销售额 7,956 亿美元、同比 +26.2%；"
             "2026Q1 2,985 亿美元、同比 +79%；WSTS 预计 2026H1 7,020 亿美元。")

    vbars(ax, [
        ("2025 全年", 7956, NAVY),
        ("2026Q1", 2985, TEAL),
        ("2026H1（预计）", 7020, SLATE),
        ("2026 全年（预计）", 10000, RED),
    ], x0=0.075, base_y=0.320, max_h=0.310, width=0.170, gap=0.050,
        scale=10000, unit=" 亿美元", label_size=7.8, value_size=8.6)

    card(ax, 0.045, 0.180, 0.900, 0.070, LIGHT, face=PALE)
    ax.text(0.068, 0.215, "口径提示：季度、半年、全年数据量纲不同，本图用于呈现增长斜率，"
                          "不宜直接相加或横向比较绝对值。",
            fontsize=7.4, color=SLATE, ha="left", va="center", zorder=7)

    save(fig, "图1_半导体销售额的斜率")


def fig2():
    fig, ax = page(
        "两种商品，两种贸易结构",
        "石油的风险是断供，芯片的风险是断链",
        source="来源：基于公开行业信息的结构对比，非统计数据。",
        punch="从一种可替代的资源，变成了一种不可替代的能力。",
        foot="说明：本图为定性对比，用于呈现两种贸易品的结构差异，不含量化结论。")

    columns(ax, [
        ("石油", SLATE, "资源禀赋逻辑",
         "· 谁地下有油，谁有议价权\n"
         "· 产量受地质条件限制，短期难增\n"
         "· 价格受地缘政治强影响，波动剧烈\n"
         "· 运输依赖管道与油轮，通道即命脉",
         "主要风险", "断供——\n显性、地理性、看得见。"),
        ("芯片", NAVY, "技术能力逻辑",
         "· 谁掌握制程、设备、设计，谁有议价权\n"
         "· 产能可在两三年内靠资本开支扩张\n"
         "· 长期价格趋势向下，短期受周期影响\n"
         "· 一颗芯片跨几十国、上百道工序",
         "主要风险", "断链——\n隐性、结构性、不易察觉。"),
    ], y=0.340, h=0.400, x0=0.045, gap=0.024, w=0.438)

    save(fig, "图2_两种贸易结构")


def fig3():
    fig, ax = page(
        "为什么是 AI 把它推上去的",
        "需求的性质，从消费品变成了资本开支",
        source="来源：财通证券研报（存储器 +302%、逻辑电路 +42%）；"
               "铠侠与英伟达布局 AI 存储据 2026-11-26—27 报道。",
        punch="资本开支没有天花板，只有预算约束。",
        foot="事实来源：2026H1 存储器与逻辑电路分别增长 302% 与 42%（WSTS 预计，经财通证券引述）；"
             "铠侠联手英伟达探索用 SSD 缓解 HBM 容量压力。")

    flow(ax, [
        ("消费品逻辑", "一人一部手机\n增长平稳有上限", GRAY),
        ("基础设施逻辑", "一个智算中心\n投入百亿级", TEAL),
        ("存储成为瓶颈", "HBM 供不应求\n存储涨 302%", RED),
    ], y=0.580, x0=0.075, w=0.250, h=0.130, gap=0.060, arrow_color=GRAY)

    card(ax, 0.045, 0.320, 0.900, 0.190, LIGHT, face="white")
    ax.text(0.068, 0.478, "三个被改写的常识", fontsize=8.6, color=DARK,
            weight="bold", ha="left", va="center", zorder=7)
    ax.plot([0.068, 0.922], [0.458, 0.458], color=LIGHT, linewidth=0.9, zorder=7)

    rows = [
        ("存储", "从「配件」变成「战略物资」，因为它是算力的瓶颈。", RED),
        ("产能", "不再是按消费需求规划，而是按资本开支规划。", NAVY),
        ("周期", "过去的猪周期式波动，被长周期基建投资拉平。", TEAL),
    ]
    y = 0.420
    for tag, text, color in rows:
        ax.text(0.068, y, tag, fontsize=7.8, color=color, weight="bold",
                ha="left", va="center", zorder=7)
        ax.text(0.140, y, text, fontsize=7.5, color=SLATE,
                ha="left", va="center", zorder=7)
        y -= 0.044

    save(fig, "图3_需求性质改变")


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", os.path.dirname(os.path.abspath(__file__)))
