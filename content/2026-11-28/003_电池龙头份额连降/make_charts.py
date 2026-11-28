# -*- coding: utf-8 -*-
"""
《电池龙头的份额连降六个月，利润却创了新高》配套图表

事实口径（中国汽车动力电池产业创新联盟 / 中国证券报 2026-11-27）：
  · 10 月国内装车：宁德时代 39.6GWh、份额 40%、连续第六个月下滑；
    比亚迪 21.36%、中创新航 8.64%。
  · 10 月配套电池企业 28 家，处年内低位。
  · 前三季度宁德归母净利 645.30 亿元、营收同比 +56.19%；储能电池销量同比 +60%。
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "_kit")))

from chart_kit import (NAVY, RED, GRAY, SLATE, LIGHT, DARK, PALE, TEAL,
                       page, save, card, hbars, flow, kpi_row)


def fig1():
    fig, ax = page(
        "10 月装车格局：一家独大，但在松动",
        "国内动力电池装车量份额（按装车量口径）",
        source="来源：中国汽车动力电池产业创新联盟，经腾讯新闻 2026-11-27 报道。"
               "「其他」为余量推算，非官方单列口径。",
        punch="所谓下滑，是从更高的位置往下走，不是被追平。",
        foot="事实来源：宁德时代 39.6GWh、份额 40%、连续第六个月下滑；比亚迪 21.36%；"
             "中创新航 8.64%。其余为余量。")

    hbars(ax, [
        ("宁德时代", 40.0, NAVY),
        ("比亚迪", 21.36, TEAL),
        ("中创新航", 8.64, SLATE),
        ("其他企业合计", 30.0, GRAY),
    ], x_right=0.800, y_top=0.660, step=0.095, bar_h=0.055,
        value_fmt="{:.1f}%", label_size=8.6, value_size=8.8, scale=40.0)

    card(ax, 0.045, 0.245, 0.900, 0.075, LIGHT, face=PALE)
    ax.text(0.068, 0.282, "辅助信号：10 月配套电池企业 28 家，处年内低位——"
                          "小厂在出清，份额在头部之间再分配。",
            fontsize=7.8, color=SLATE, ha="left", va="center", zorder=7)

    save(fig, "图1_十月装车格局")


def fig2():
    fig, ax = page(
        "两个方向相反的数字",
        "份额向下，利润向上——这才是这条新闻的信息量",
        source="来源：装车份额据中国汽车动力电池产业创新联盟；利润与营收据中国证券报 2026-11-27。",
        punch="这叫「以份额换利润」，只有在龙头位置上才做得到。",
        foot="说明：份额为月度口径，利润为前三季度累计口径，量纲不同，仅示意方向。")

    card(ax, 0.045, 0.400, 0.400, 0.250, NAVY, lw=1.3)
    ax.text(0.070, 0.615, "装车份额", fontsize=8.6, color=NAVY,
            weight="bold", ha="left", va="center", zorder=7)
    ax.text(0.070, 0.545, "40%", fontsize=30.0, color=NAVY,
            weight="bold", ha="left", va="center", zorder=7)
    ax.text(0.070, 0.470, "连续第六个月下滑", fontsize=8.2, color=RED,
            weight="bold", ha="left", va="center", zorder=7)
    ax.text(0.070, 0.430, "月度装车口径", fontsize=7.4, color=GRAY,
            ha="left", va="center", zorder=7)

    card(ax, 0.545, 0.400, 0.400, 0.250, TEAL, lw=1.3)
    ax.text(0.570, 0.615, "归母净利润（前三季）", fontsize=8.6, color=TEAL,
            weight="bold", ha="left", va="center", zorder=7)
    ax.text(0.570, 0.545, "645.30 亿", fontsize=22.0, color=TEAL,
            weight="bold", ha="left", va="center", zorder=7)
    ax.text(0.570, 0.470, "营业收入同比 +56.19%", fontsize=8.2, color=TEAL,
            weight="bold", ha="left", va="center", zorder=7)
    ax.text(0.570, 0.430, "前三季度累计", fontsize=7.4, color=GRAY,
            ha="left", va="center", zorder=7)

    card(ax, 0.045, 0.300, 0.900, 0.075, LIGHT, face="white")
    ax.text(0.068, 0.337, "份额是比例，利润是绝对值。分母变大的时候，比例下降不代表数量下降。",
            fontsize=8.0, color=DARK, ha="left", va="center", zorder=7)

    save(fig, "图2_份额与利润的背离")


def fig3():
    fig, ax = page(
        "整车厂为什么一定要第二供应商",
        "这不是针对谁，是采购的基本常识",
        source="来源：基于公开产业信息的机制梳理。",
        punch="二线能拿到订单，不是因为更强，是因为整车厂需要它们存在。",
        foot="说明：本图为采购机制的定性说明，不涉及任何具体整车厂或电池厂的评价。")

    flow(ax, [
        ("议价", "一家只有一个价格\n两家才有得谈", NAVY),
        ("供应安全", "产能紧张时\n不能只能等", TEAL),
        ("技术路线", "锂电路线在变\n不能押单一方案", RED),
    ], y=0.600, x0=0.080, w=0.250, h=0.130, gap=0.065, arrow_color=GRAY)

    card(ax, 0.045, 0.290, 0.900, 0.230, LIGHT, face="white")
    ax.text(0.068, 0.492, "行业从金字塔，变成哑铃", fontsize=8.6, color=DARK,
            weight="bold", ha="left", va="center", zorder=7)
    ax.plot([0.068, 0.922], [0.472, 0.472], color=LIGHT, linewidth=0.9, zorder=7)

    rows = [
        ("整车厂", "好事：供应商多了，议价能力上来了", TEAL),
        ("头部电池厂", "中性：份额让出去，但利润守住", NAVY),
        ("二线电池厂", "机会窗口，但窗口不会一直开着", SLATE),
        ("小厂", "出清，没有第二条路", RED),
    ]
    y = 0.450
    for tag, text, color in rows:
        ax.text(0.068, y, tag, fontsize=7.8, color=color, weight="bold",
                ha="left", va="center", zorder=7)
        ax.text(0.180, y, text, fontsize=7.5, color=SLATE,
                ha="left", va="center", zorder=7)
        y -= 0.040

    save(fig, "图3_为什么需要第二供应商")


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", os.path.dirname(os.path.abspath(__file__)))
