# -*- coding: utf-8 -*-
"""
《二线电池厂不跟宁德时代硬拼了，它们换了打法》配套图表

事实口径（中国经济网 / 新浪财经转中国证券报 2026-11-27）：
  · 亿纬锂能：截至 2026-08 船用电池累计出货超 1GWh；国内超 50% 电动船舶采用其方案；
    获 CCS、BV、DNV、ABS 认证；与 Fluence 签 206GWh 五年框架协议，2027 年已确定
    交付约 16GWh。
  · 国轩高科：沙特首批大型储能项目核心 6GWh 标段；乾元智储系统，-30℃ 至 55℃ 运行。
  · 宁德时代：前三季度储能电池销量同比 +60%；11-11 与中国民航大学共建航空电池
    适航技术创新联合实验室。
  · 2027 年消费税税率上调、出口退税退出、海外合规要求抬升。
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "_kit")))

from chart_kit import (NAVY, RED, GRAY, SLATE, LIGHT, DARK, PALE, TEAL,
                       page, save, card, columns, flow, kpi_row)


def fig1():
    fig, ax = page(
        "三条路，三个不同的门槛",
        "二线厂商避开主流赛道，各自找了一块「规模买不到」的地方",
        source="来源：中国经济网、新浪财经（转中国证券报）2026-11-27。"
               "协议规模、交付量、标段规模口径不同，不可直接相加。",
        punch="不在最大的池塘里当小鱼，去小的池塘里当大鱼。",
        foot="事实来源：亿纬锂能（船用 1GWh、Fluence 206GWh 框架）、国轩高科（沙特 6GWh 标段）、"
             "宁德时代（储能销量 +60%、航空电池实验室）。")

    columns(ax, [
        ("船舶", NAVY, "亿纬锂能",
         "· 船用电池累计出货超 1GWh（截至 2026-08）\n"
         "· 国内超 50% 电动船舶采用其方案\n"
         "· 已获 CCS、BV、DNV、ABS 四家船级社认证",
         "门槛", "认证。换供应商要重新做认证，\n一条船停航的成本高于电池差价。"),
        ("海外储能", TEAL, "国轩高科",
         "· 拿下沙特首批大型储能项目\n　核心 6GWh 标段\n"
         "· 乾元智储系统\n"
         "· 可在 -30℃ 至 55℃ 区间稳定运行",
         "门槛", "工况。高温风沙下的真实运行记录，\n实验室模拟不出来。"),
        ("电动航空", RED, "宁德时代",
         "· 前三季度储能电池销量同比 +60%\n"
         "· 11-11 与中国民航大学共建\n　航空电池适航技术创新联合实验室\n"
         "· 切入 eVTOL 电池适航验证",
         "门槛", "适航。要求比汽车严格一个量级，\n流程完整且漫长。"),
    ], y=0.330, h=0.410, x0=0.045, gap=0.018, w=0.290)

    save(fig, "图1_三条差异化路径")


def fig2():
    fig, ax = page(
        "门槛的本质，是时间",
        "认证、工况、适航——三样东西都无法用规模优势买断",
        source="来源：基于公开信息的机制梳理。认证周期与成本为行业通行情况，非具体企业数据。",
        punch="规模优势买不到的，才叫护城河。",
        foot="说明：本图为竞争机制的定性梳理，不构成对任何企业能力的评价。")

    flow(ax, [
        ("拿到认证", "两三年周期\n四套标准", NAVY),
        ("进入供应链", "客户切换成本高\n停航/停机代价大", TEAL),
        ("形成锁定", "订单随产品生命周期\n持续交付", RED),
    ], y=0.590, x0=0.080, w=0.250, h=0.135, gap=0.065, arrow_color=GRAY)

    card(ax, 0.045, 0.310, 0.900, 0.200, LIGHT, face="white")
    ax.text(0.068, 0.478, "两种赚钱方式，两种能力要求", fontsize=8.6, color=DARK,
            weight="bold", ha="left", va="center", zorder=7)
    ax.plot([0.068, 0.922], [0.458, 0.458], color=LIGHT, linewidth=0.9, zorder=7)

    ax.text(0.068, 0.420, "主流赛道：大规模 × 低毛利", fontsize=8.0, color=SLATE,
            weight="bold", ha="left", va="center", zorder=7)
    ax.text(0.330, 0.420, "靠出货量摊薄成本，单颗利润薄、总量巨大；核心能力是成本控制与产能爬坡。",
            fontsize=7.4, color=GRAY, ha="left", va="center", zorder=7)
    ax.text(0.068, 0.378, "细分场景：小规模 × 高毛利", fontsize=8.0, color=NAVY,
            weight="bold", ha="left", va="center", zorder=7)
    ax.text(0.330, 0.378, "靠认证与定制建立壁垒，订单量小但单价高；核心能力是场景理解与系统集成。",
            fontsize=7.4, color=GRAY, ha="left", va="center", zorder=7)
    ax.text(0.068, 0.336, "结论：这不是「更好的生意」，是「更适合二线做的生意」。",
            fontsize=8.0, color=RED, weight="bold", ha="left", va="center", zorder=7)

    save(fig, "图2_门槛的本质是时间")


def fig3():
    fig, ax = page(
        "这条路能活得好，但很难活得大",
        "四个必须承认的代价",
        source="来源：中国经济网、新浪财经 2026-11-27 报道及基于公开信息的分析。",
        punch="入场券不等于座位。",
        foot="事实来源：整机厂多供应商策略给二线入场券，但留住订单取决于产品一致性、交付节奏、"
             "本地化服务；2027 年消费税上调、出口退税退出、海外合规抬升。")

    rows = [
        ("天花板明确", "电动船舶、eVTOL、区域储能的规模，都远小于乘用车动力电池。", RED),
        ("难以规模化", "每个场景都要重新设计、验证、认证，研发投入无法摊薄。", NAVY),
        ("客户集中度高", "一个场景里可能只有几个大客户，丢一个就丢整条业务线。", TEAL),
        ("政策成本抬头", "2027 年消费税上调、出口退税退出、海外合规要求抬升。", SLATE),
    ]
    y = 0.620
    for tag, text, color in rows:
        card(ax, 0.045, y - 0.048, 0.900, 0.062, LIGHT, face="white", lw=0.8)
        ax.text(0.068, y - 0.017, tag, fontsize=8.2, color=color, weight="bold",
                ha="left", va="center", zorder=7)
        ax.text(0.235, y - 0.017, text, fontsize=7.5, color=SLATE,
                ha="left", va="center", zorder=7)
        y -= 0.082

    card(ax, 0.045, 0.285, 0.900, 0.055, LIGHT, face=PALE)
    ax.text(0.068, 0.312, "对二线厂商来说，这可能是当下最理性的选择：先活下来，再谈别的。",
            fontsize=8.0, color=NAVY, weight="bold", ha="left", va="center", zorder=7)

    save(fig, "图3_四个代价")


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", os.path.dirname(os.path.abspath(__file__)))
