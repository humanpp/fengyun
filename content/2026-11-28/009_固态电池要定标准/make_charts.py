# -*- coding: utf-8 -*-
"""
《固态电池要定标准了，先解决"什么才算固态"》配套图表

事实口径：
  · 工信部锂离子电池标准工作组拟成立"固态锂电池标准项目组"，编制推荐性国标，
    委托中国电子技术标准化研究院起草（2026-11-27 报道）。
  · 《2026中国固态电池行业发展蓝皮书》：混合固液 2026 年率先商业化，
    全年出货预计 11.4GWh；全固态完成车规级样件验证。
  · 国轩金石二代完成 0.2GWh 示范线，计划建 2GWh 预生产线。
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "_kit")))

from chart_kit import (NAVY, RED, GRAY, SLATE, LIGHT, DARK, PALE, TEAL,
                       page, save, card, flow, columns, kpi_row)


def fig1():
    fig, ax = page(
        "从路线之争，到定尺子",
        "标准解决的不是「谁能做」，是「怎么衡量」",
        source="来源：工信部锂离子电池标准工作组拟成立固态锂电池标准项目组（2026-11-27 报道）。"
               "标准仍处拟成立阶段，内容未公布。",
        punch="标准不是给技术设限，是给沟通建立共同语言。",
        foot="事实来源：拟成立固态锂电池标准项目组、编制推荐性国标、委托中国电子技术标准化研究院起草，"
             "据 2026-11-27 报道。")

    flow(ax, [
        ("路线之争", "半固态、全固态\n各说各话", GRAY),
        ("口径混乱", "含液量差好几倍\n宣传都叫固态", SLATE),
        ("统一术语", "推荐性国标\n给行业一把尺子", NAVY),
        ("量产可评价", "什么算量产\n有了判断依据", TEAL),
    ], y=0.585, x0=0.045, w=0.200, h=0.150, gap=0.025, arrow_color=GRAY)

    card(ax, 0.045, 0.320, 0.900, 0.180, LIGHT, face="white")
    ax.text(0.068, 0.468, "为什么定义模糊会伤害整个行业", fontsize=8.6, color=DARK,
            weight="bold", ha="left", va="center", zorder=7)
    ax.plot([0.068, 0.922], [0.448, 0.448], color=LIGHT, linewidth=0.9, zorder=7)

    rows = [
        ("消费者", "同样叫固态，续航与安全可能完全不同，无法分辨。"),
        ("采购方", "连「固态」定义都不统一，供应商之间无法比较。"),
        ("企业端", "没有标准，任何企业都可以宣称「率先量产」。"),
    ]
    y = 0.412
    for tag, text in rows:
        ax.text(0.068, y, tag, fontsize=7.8, color=NAVY, weight="bold",
                ha="left", va="center", zorder=7)
        ax.text(0.160, y, text, fontsize=7.5, color=SLATE,
                ha="left", va="center", zorder=7)
        y -= 0.042

    save(fig, "图1_从路线之争到定尺子")


def fig2():
    fig, ax = page(
        "半固态在跑，全固态在做样件",
        "两个词经常被混着用，但差了一整个阶段",
        source="来源：《2026中国固态电池行业发展蓝皮书》；国轩高科示范线与预生产线进度据公开报道。",
        punch="数百兆瓦级是「能验证」的量级，不是「能铺量」的量级。",
        foot="事实来源：混合固液 2026 年商业化、出货预计 11.4GWh；全固态完成车规级样件验证；"
             "国轩 0.2GWh 示范线、2GWh 预生产线规划。")

    columns(ax, [
        ("半固态（混合固液）", NAVY, "2026 年先商业化",
         "· 仍含少量液态电解质\n"
         "· 与现有产线兼容度高\n"
         "· 全年出货预计 11.4GWh\n"
         "· 卖点：安全性与能量密度提升",
         "状态", "已经有货在出，\n价格高于同级别液态电池车型。"),
        ("全固态", RED, "还在样件验证",
         "· 电解质完全固态\n"
         "· 制造工艺与现有产线差异大\n"
         "· 良率与成本仍在解决\n"
         "· 国轩 0.2GWh 示范线已建成",
         "状态", "2GWh 为规划预生产线，\n不是现有产能。"),
    ], y=0.340, h=0.400, x0=0.045, gap=0.024, w=0.438)

    save(fig, "图2_半固态与全固态")


def fig3():
    fig, ax = page(
        "三件事，标准管不了",
        "标准解决「怎么衡量」，不解决「能不能做到」",
        source="来源：行业公开讨论归纳（固固界面、材料成本、制造良率）。",
        punch="实验室指标和量产良率之间，隔着很长一段路。",
        foot="说明：三道难点为行业公开讨论的归纳，不同技术路线（硫化物、氧化物、聚合物）难点分布不同。")

    rows = [
        ("固固界面", "液态能浸润电极，固态是硬接触，接触不良导致内阻高。", NAVY),
        ("材料成本", "硫化锂等关键材料价格高、产能有限，成本不下来难普及。", TEAL),
        ("制造良率", "叠片、加压、封装工艺与液态差别大，产线要重新调试。", RED),
    ]
    y = 0.620
    for tag, text, color in rows:
        card(ax, 0.045, y - 0.080, 0.900, 0.095, color, lw=1.2)
        ax.text(0.070, y - 0.032, tag, fontsize=8.6, color=color, weight="bold",
                ha="left", va="center", zorder=7)
        ax.text(0.230, y - 0.032, text, fontsize=7.6, color=SLATE,
                ha="left", va="center", zorder=7)
        y -= 0.110

    card(ax, 0.045, 0.198, 0.900, 0.085, LIGHT, face=PALE)
    ax.text(0.068, 0.253, "参照：丰田的固态电池装车计划已经四次推迟。这不是不努力，是这类问题的共性。",
            fontsize=7.8, color=SLATE, ha="left", va="center", zorder=7)
    ax.text(0.068, 0.220, "看宣传时问一句：含液量多少？答不上来的，基本可判断为营销话术。",
            fontsize=8.0, color=DARK, weight="bold", ha="left", va="center", zorder=7)

    save(fig, "图3_三件事标准管不了")


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", os.path.dirname(os.path.abspath(__file__)))
