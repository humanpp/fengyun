# -*- coding: utf-8 -*-
"""
《一边是千台协议，一边是 700 台已在跑：机器人落地走了两条路》配套图表

事实口径：
  · 2026-11-25 智元机器人与爱仕达签署灵犀系列千台生产合作协议；此前 2026-07
    战略合作、100 台人形机器人零售门店场景探索、四足机器人委托制造。
  · 2026-11-26 京东物流德国奥伯豪森 1 号仓：超 700 台自研「智狼」「天狼」机器人，
    单日出入库 35 万件，效率提升 3 倍；约 4 万㎡，可存超 900 万件；最快 15 分钟出库；
    「智狼」区约 30 万个周转箱位；已落地全球超 100 个仓库、海外仓覆盖 26 国。
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "_kit")))

from chart_kit import (NAVY, RED, GRAY, SLATE, LIGHT, DARK, PALE, TEAL,
                       page, save, card, columns, flow, kpi_row)


def fig1():
    fig, ax = page(
        "一千台是协议，七百台已经在跑",
        "人形机器人与仓储机器人，走的是两条不同的路",
        source="来源：2026-11-26 报道（智元与爱仕达千台协议）；每日经济新闻 2026-11-26"
               "（京东物流德国仓）。协议规模与已投用设备口径不同。",
        punch="排除不确定性，是机器人落地的第一性原理。",
        foot="事实来源：灵犀系列千台生产合作协议（2026-11-25）；京东物流德国奥伯豪森 1 号仓"
             "超 700 台机器人投用。")

    columns(ax, [
        ("人形机器人", NAVY, "千台级验证",
         "· 智元 × 爱仕达签千台生产协议\n"
         "· 此前：100 台零售门店场景探索\n"
         "· 技术公司出设计，制造公司出产能\n"
         "· 任务边界开放，需应对意外情况",
         "当前难点", "通用性与成本能否同时成立。\n千台之后能否到万台。"),
        ("仓储机器人", TEAL, "百仓级复制",
         "· 京东物流德国仓超 700 台已投用\n"
         "· 单日出入库 35 万件，效率提升 3 倍\n"
         "· 已落地全球超 100 个仓库\n"
         "· 任务边界封闭，流程固定可复现",
         "当前难点", "稳定性与投资回报测算。\n不同国家条件的复制差异。"),
    ], y=0.340, h=0.400, x0=0.045, gap=0.024, w=0.438)

    save(fig, "图1_两条路")


def fig2():
    fig, ax = page(
        "一个已经跑通的样本",
        "京东物流德国奥伯豪森 1 号仓的关键数字",
        source="来源：每日经济新闻 2026-11-26。「效率提升 3 倍」为对比传统操作模式口径。",
        punch="这不是演示项目，是可复制的产品。",
        foot="事实来源：超 700 台自研机器人；单日出入库 35 万件；效率提升 3 倍；"
             "约 4 万平方米、可存超 900 万件；最快 15 分钟出库。")

    kpi_row(ax, [
        ("自研机器人", "700+ 台", "德国 1 号仓投用", NAVY),
        ("单日出入库", "35 万件", "全流程处理量", TEAL),
        ("履约效率", "3 倍", "对比传统操作模式", RED),
    ], x0=0.045, y=0.580, w_each=0.283, h=0.135, gap=0.025)

    card(ax, 0.045, 0.300, 0.900, 0.210, LIGHT, face="white")
    ax.text(0.068, 0.478, "为什么仓储先跑通", fontsize=8.6, color=DARK,
            weight="bold", ha="left", va="center", zorder=7)
    ax.plot([0.068, 0.922], [0.458, 0.458], color=LIGHT, linewidth=0.9, zorder=7)

    rows = [
        ("场地固定", "4 万平方米的仓库，货架位置、通道宽度都是可设计的。"),
        ("任务明确", "把指定的箱子，从 A 搬到 B，不需要理解世界。"),
        ("收益可算", "省了多少人、提了多少件/小时，能直接换算成钱。"),
    ]
    y = 0.420
    for tag, text in rows:
        ax.text(0.068, y, tag, fontsize=7.8, color=TEAL, weight="bold",
                ha="left", va="center", zorder=7)
        ax.text(0.175, y, text, fontsize=7.5, color=SLATE,
                ha="left", va="center", zorder=7)
        y -= 0.044

    save(fig, "图2_跑通的样本")


def fig3():
    fig, ax = page(
        "机器人落地的三级台阶",
        "先把不确定性排除掉，再谈通用",
        source="来源：基于公开信息的产业路径梳理，非官方分类。",
        punch="视频可以剪，产线不会说谎。",
        foot="说明：本图为技术落地路径的归纳，不构成对任何企业技术路线或产品的评价。")

    flow(ax, [
        ("单点任务", "固定工位\n重复动作", GRAY),
        ("限定场景", "封闭环境\n流程清晰", TEAL),
        ("开放环境", "应对意外\n人机协作", NAVY),
    ], y=0.590, x0=0.080, w=0.250, h=0.135, gap=0.065, arrow_color=GRAY)

    card(ax, 0.045, 0.320, 0.900, 0.190, LIGHT, face=PALE)
    ax.text(0.068, 0.478, "判断一家机器人公司，看三个数", fontsize=8.6, color=DARK,
            weight="bold", ha="left", va="center", zorder=7)
    ax.text(0.068, 0.434, "·　交付了多少台——不是发了多少视频。",
            fontsize=7.6, color=SLATE, ha="left", va="center", zorder=7)
    ax.text(0.068, 0.396, "·　在多少个场景里连续跑了多久——不是单次演示。",
            fontsize=7.6, color=SLATE, ha="left", va="center", zorder=7)
    ax.text(0.068, 0.358, "·　客户有没有复购——复购是最硬的验证。",
            fontsize=7.6, color=SLATE, ha="left", va="center", zorder=7)

    save(fig, "图3_三级台阶")


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", os.path.dirname(os.path.abspath(__file__)))
