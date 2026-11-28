# -*- coding: utf-8 -*-
"""
《国产存储的份额从 3% 到 8%》配套图表

事实口径：
  · 长鑫科技 DRAM 全球市占：2025Q1 3% → 2026Q1 8%
  · 长江存储 NAND 全球市占：8% → 13%
  · 均据中原证券研报（经中国基金报、南方财经网 2026-11-27 引述）
  · SEMI 预计 2026 年全球半导体设备销售额 1,659 亿美元、同比 +23.2%，
    2028 年 2,295 亿美元
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "_kit")))

from chart_kit import (NAVY, RED, GRAY, SLATE, LIGHT, DARK, PALE, TEAL,
                       page, save, card, columns, flow, kpi_row, hbars)


def fig1():
    fig, ax = page(
        "四个季度，份额翻了近两倍",
        "国产存储的全球市占率变化（按金额口径）",
        source="来源：中原证券研报（经中国基金报、南方财经网 2026-11-27 引述）。"
               "不同机构对市占率的分母定义可能不同。",
        punch="8% 在存储行业里，仍然是「刚上牌桌」的位置。",
        foot="事实来源：长鑫科技 DRAM 3% → 8%（2025Q1 → 2026Q1）；"
             "长江存储 NAND 8% → 13%。均为研报引述口径。")

    kpi_row(ax, [
        ("DRAM　2025Q1", "3%", "长鑫科技，起点", GRAY),
        ("DRAM　2026Q1", "8%", "长鑫科技，翻近两倍", NAVY),
        ("NAND　2026Q1", "13%", "长江存储，由 8% 提升", TEAL),
    ], x0=0.045, y=0.580, w_each=0.283, h=0.135, gap=0.025)

    card(ax, 0.045, 0.300, 0.900, 0.200, LIGHT, face="white")
    ax.text(0.068, 0.470, "同一个数字，两种读法", fontsize=8.6, color=DARK,
            weight="bold", ha="left", va="center", zorder=7)
    ax.plot([0.068, 0.922], [0.450, 0.450], color=LIGHT, linewidth=0.9, zorder=7)

    rows = [
        ("看速度", "四个季度份额接近三倍，在重资产行业里属极快。", NAVY),
        ("看绝对值", "每 100 颗存储芯片里 8 颗，仍处早期阶段。", SLATE),
        ("看分母", "行业同期增长 302%，份额提升意味着出货更快。", RED),
    ]
    y = 0.410
    for tag, text, color in rows:
        ax.text(0.068, y, tag, fontsize=7.8, color=color, weight="bold",
                ha="left", va="center", zorder=7)
        ax.text(0.165, y, text, fontsize=7.5, color=SLATE,
                ha="left", va="center", zorder=7)
        y -= 0.044

    save(fig, "图1_份额的跃升")


def fig2():
    fig, ax = page(
        "三道门槛，没有一道能一年跨过",
        "存储份额是靠资本开支和良率，一轮一轮啃下来的",
        source="来源：基于公开行业信息的机制梳理，非统计数据。",
        punch="份额的自主，不等于链条的自主。",
        foot="说明：本图为行业机制的定性梳理，不含具体企业的技术评价。")

    columns(ax, [
        ("门槛一", NAVY, "专利墙",
         "· DRAM 是专利最密集的领域之一\n"
         "· 三大厂三十年积累，绕不开\n"
         "· 后来者必须在架构与工艺上\n　做自己的设计，不能直接复制",
         "代价", "研发投入长周期、高风险，\n短期看不到回报。"),
        ("门槛二", RED, "良率",
         "· 存储是标准化产品，价格由市场定\n"
         "· 成本由良率定，差 5 个点就是生死\n"
         "· 良率提升没有捷径\n　只能靠产线反复调试",
         "代价", "爬坡期必然亏损，\n且无法跳过低良率阶段。"),
        ("门槛三", TEAL, "设备",
         "· 依赖高端光刻、刻蚀、薄膜沉积设备\n"
         "· 买不买得到、何时到货、能否稳定运行\n　直接决定扩产节奏",
         "代价", "设备交付周期长，\n扩产节奏不完全自主。"),
    ], y=0.330, h=0.400, x0=0.045, gap=0.018, w=0.290)

    save(fig, "图2_三道门槛")


def fig3():
    fig, ax = page(
        "设备是先行指标",
        "厂还没建好，设备订单先到",
        source="来源：SEMI 预计（经中原证券研报引述），2026 年与 2028 年为预测值。",
        punch="看行业的国产化，不能只看一个数字。",
        foot="事实来源：SEMI 预计 2026 年全球半导体设备销售额 1,659 亿美元（+23.2%）、"
             "2028 年 2,295 亿美元。")

    hbars(ax, [
        ("2026 年（预计）", 1659, NAVY),
        ("2028 年（预计）", 2295, TEAL),
    ], x_right=0.730, y_top=0.640, step=0.140, bar_h=0.075,
        value_fmt="{:,.0f} 亿美元", label_size=8.8, value_size=9.6)

    card(ax, 0.045, 0.300, 0.900, 0.175, LIGHT, face=PALE)
    ax.text(0.068, 0.445, "为什么设备比份额更早反映趋势", fontsize=8.6, color=DARK,
            weight="bold", ha="left", va="center", zorder=7)
    ax.text(0.068, 0.404, "·　设备订单落地，通常早于产能释放 12—24 个月。",
            fontsize=7.6, color=SLATE, ha="left", va="center", zorder=7)
    ax.text(0.068, 0.366, "·　全球设备销售额两年增长约 38%，说明扩产不是个别行为。",
            fontsize=7.6, color=SLATE, ha="left", va="center", zorder=7)
    ax.text(0.068, 0.328, "·　但设备、材料环节的国产化进度，与芯片份额并不同步。",
            fontsize=7.6, color=SLATE, ha="left", va="center", zorder=7)

    save(fig, "图3_设备先行")


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", os.path.dirname(os.path.abspath(__file__)))
