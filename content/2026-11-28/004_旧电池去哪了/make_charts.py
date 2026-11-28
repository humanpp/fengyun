# -*- coding: utf-8 -*-
"""
《你换掉的旧电池，大部分没进正规回收厂》配套图表

事实口径（界面新闻 2026-11-27 调查报道及同期公开信息）：
  · 邦普循环 2025 年回收 21 万吨、营收 406.4 亿元；镍钴锰回收率 99.6%、锂 96.5%。
  · 格林美一季度回收 1.5 万吨、增 40%；锂 96.5%、镍钴超 99.5%。
  · 规范化回收率不足 25%；注册主体超 18 万家，白名单仅 156 家。
  · 2025 年退役量约 38 万吨，2030 年破 100 万吨；2026 年回收市场预计 527 亿元。
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "_kit")))

from chart_kit import (NAVY, RED, GRAY, SLATE, LIGHT, DARK, PALE, TEAL,
                       page, save, card, hbars, flow, columns, kpi_row)


def fig1():
    fig, ax = page(
        "技术能做到 96%，现实只做到 25%",
        "中间那 71 个百分点，差在渠道，不在工艺",
        source="来源：界面新闻 2026-11-27 调查报道。「不足 25%」为媒体调查口径，"
               "统计方法未完整披露。",
        punch="问题不在「能不能回收」，在「能不能收到」。",
        foot="事实来源：镍钴锰 99.6%、锂 96.5%（邦普循环）；规范化回收率不足 25%（界面新闻调查）。")

    card(ax, 0.045, 0.470, 0.400, 0.200, TEAL, lw=1.3)
    ax.text(0.070, 0.628, "金属回收率（头部企业）", fontsize=8.4, color=TEAL,
            weight="bold", ha="left", va="center", zorder=7)
    ax.text(0.070, 0.565, "99.6%", fontsize=28.0, color=TEAL,
            weight="bold", ha="left", va="center", zorder=7)
    ax.text(0.070, 0.505, "镍钴锰；锂为 96.5%", fontsize=7.6, color=SLATE,
            ha="left", va="center", zorder=7)

    card(ax, 0.545, 0.470, 0.400, 0.200, RED, lw=1.3)
    ax.text(0.570, 0.628, "实际进正规渠道的比例", fontsize=8.4, color=RED,
            weight="bold", ha="left", va="center", zorder=7)
    ax.text(0.570, 0.565, "不足 25%", fontsize=24.0, color=RED,
            weight="bold", ha="left", va="center", zorder=7)
    ax.text(0.570, 0.505, "媒体调查口径", fontsize=7.6, color=GRAY,
            ha="left", va="center", zorder=7)

    card(ax, 0.045, 0.300, 0.900, 0.130, LIGHT, face="white")
    ax.text(0.068, 0.400, "两个数字放在一起，说明什么", fontsize=8.6, color=DARK,
            weight="bold", ha="left", va="center", zorder=7)
    ax.text(0.068, 0.360, "·　工艺端已经过关：有价值的金属几乎都能提取。",
            fontsize=7.6, color=SLATE, ha="left", va="center", zorder=7)
    ax.text(0.068, 0.325, "·　回收端没有跟上：大部分退役电池流向了非正规渠道。",
            fontsize=7.6, color=SLATE, ha="left", va="center", zorder=7)

    save(fig, "图1_技术能力与现实回收")


def fig2():
    fig, ax = page(
        "小作坊为什么出价更高",
        "不是效率高，是成本少算了几项",
        source="来源：基于公开报道的机制梳理，非统计数据。",
        punch="劣币驱逐良币，不是因为劣币更好，是因为劣币不用承担成本。",
        foot="说明：本图为成本结构的定性对比，不含具体企业的成本数据。")

    columns(ax, [
        ("正规回收企业", NAVY, "三项成本都要算",
         "· 环保：废水处理、废气收集、防渗地面\n"
         "· 税负：采购要票、销售纳税\n"
         "· 合规：场地、设备、人员、全程记录\n"
         "· 出价参考：1.0",
         "结果", "收得规范，但出价低，\n抢不过上门收电池的。"),
        ("小作坊", RED, "三项成本几乎为零",
         "· 环保：废液直排，不做处理\n"
         "· 税负：现金交易，不开票\n"
         "· 合规：无资质、无记录、无追溯\n"
         "· 出价参考：1.2",
         "结果", "多出的 0.2，正是省下的成本，\n代价由环境和公共财政承担。"),
    ], y=0.340, h=0.400, x0=0.045, gap=0.024, w=0.438)

    save(fig, "图2_为什么小作坊抢得过")


def fig3():
    fig, ax = page(
        "三方角色的算盘",
        "同一块旧电池，三种不同的看法",
        source="来源：基于公开信息的机制梳理。",
        punch="让「不回收」这件事变得不划算，比劝人环保有效。",
        foot="说明：本图为角色动机的分析框架，不代表任何具体主体的实际行为。")

    card(ax, 0.045, 0.560, 0.288, 0.150, SLATE, lw=1.2)
    ax.text(0.070, 0.672, "车主", fontsize=9.4, color=SLATE, weight="bold",
            ha="left", va="center", zorder=7)
    ax.text(0.070, 0.632, "谁出价高卖给谁\n不知道电池去哪了", fontsize=7.4,
            color=DARK, ha="left", va="top", zorder=7, linespacing=1.9)

    card(ax, 0.346, 0.560, 0.288, 0.150, NAVY, lw=1.2)
    ax.text(0.371, 0.672, "正规回收企业", fontsize=9.4, color=NAVY, weight="bold",
            ha="left", va="center", zorder=7)
    ax.text(0.371, 0.632, "技术和产能都有\n但收不到足够的货", fontsize=7.4,
            color=DARK, ha="left", va="top", zorder=7, linespacing=1.9)

    card(ax, 0.647, 0.560, 0.288, 0.150, TEAL, lw=1.2)
    ax.text(0.672, 0.672, "监管", fontsize=9.4, color=TEAL, weight="bold",
            ha="left", va="center", zorder=7)
    ax.text(0.672, 0.632, "数字身份证＋\n车电一体报废", fontsize=7.4,
            color=DARK, ha="left", va="top", zorder=7, linespacing=1.9)

    card(ax, 0.045, 0.320, 0.900, 0.200, LIGHT, face="white")
    ax.text(0.068, 0.488, "数字身份证要解决的问题", fontsize=8.6, color=DARK,
            weight="bold", ha="left", va="center", zorder=7)
    ax.plot([0.068, 0.922], [0.468, 0.468], color=LIGHT, linewidth=0.9, zorder=7)

    rows = [
        ("溯源", "24 位编码串联 9 个环节 96 项信息，全程留痕。"),
        ("责任", "报废必须走指定渠道，不能随便卖给上门收的。"),
        ("监管", "车电一体报废，堵住「车报废、电池私卖」的口子。"),
    ]
    y = 0.428
    for tag, text in rows:
        ax.text(0.068, y, tag, fontsize=7.8, color=NAVY, weight="bold",
                ha="left", va="center", zorder=7)
        ax.text(0.150, y, text, fontsize=7.5, color=SLATE,
                ha="left", va="center", zorder=7)
        y -= 0.042

    save(fig, "图3_三方角色的算盘")


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", os.path.dirname(os.path.abspath(__file__)))
