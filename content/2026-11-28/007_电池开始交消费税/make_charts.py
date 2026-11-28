# -*- coding: utf-8 -*-
"""
《电池开始交消费税了，2% 到 4% 只隔一年》配套图表

事实口径（财政部公告，经中国证券报 2026-11-27 引述）：
  · 2026-09 起锂离子蓄电池按 2% 征消费税；2027-09 提至 4%。
  · 同期出口退税下调。
  · 钠离子电池与固态电池 2026-09 起免征消费税至 2028 年底。
  · 亿纬锂能称已与多数客户就税改达成方案，四季度产能订满。
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "_kit")))

from chart_kit import (NAVY, RED, GRAY, SLATE, LIGHT, DARK, PALE, TEAL,
                       page, save, card, flow, columns)


def fig1():
    fig, ax = page(
        "一张税制时间表",
        "锂电从 2% 走到 4%，钠电与固态免税到 2028 年底",
        source="来源：财政部公告，经中国证券报 2026-11-27 引述。"
               "具体征管细则以正式文件为准。",
        punch="政策在用税差引导技术路线。",
        foot="事实来源：2026-09 起锂离子蓄电池 2%；2027-09 起 4%；"
             "钠离子与固态电池 2026-09 至 2028 年底免征。")

    items = [
        ("2026.09", "锂电 2%", "开始征收，进入成本表", NAVY),
        ("2027.09", "锂电 4%", "税率翻倍，缓冲期结束", RED),
        ("2028.12", "免税期满", "钠电与固态同台竞争", SLATE),
    ]
    x = 0.045
    w = 0.288
    for when, what, note, color in items:
        card(ax, x, 0.400, w, 0.230, color, lw=1.3)
        ax.text(x + 0.022, 0.578, when, fontsize=8.6, color=GRAY,
                ha="left", va="center", zorder=7)
        ax.text(x + 0.022, 0.520, what, fontsize=15.0, color=color,
                weight="bold", ha="left", va="center", zorder=7)
        ax.plot([x + 0.022, x + w - 0.022], [0.482, 0.482], color=LIGHT,
                linewidth=0.9, zorder=7)
        ax.text(x + 0.022, 0.448, note, fontsize=7.6, color=SLATE,
                ha="left", va="center", zorder=7)
        x += w + 0.018

    card(ax, 0.045, 0.300, 0.900, 0.075, LIGHT, face=PALE)
    ax.text(0.068, 0.337, "同期：出口退税下调。消费税增成本、退税降返还，两头挤。",
            fontsize=8.0, color=DARK, ha="left", va="center", zorder=7)

    save(fig, "图1_税制时间表")


def fig2():
    fig, ax = page(
        "2% 对不同企业，是不同重量",
        "按毛利率算，税负占利润的比例差了一倍",
        source="说明：本图为按不同毛利率所作的示意性测算，非任何企业的实际财务数据。",
        punch="越是靠薄利走量的企业，越难受。",
        foot="说明：测算假设 2% 消费税全部由企业当期承担、不向客户转嫁，仅用于说明量级差异。")

    rows = [
        ("毛利率 20%", "2% ÷ 20% = 10%", "利润被侵蚀约一成", TEAL),
        ("毛利率 10%", "2% ÷ 10% = 20%", "利润被侵蚀约两成", RED),
    ]
    y = 0.590
    for name, calc, note, color in rows:
        card(ax, 0.045, y - 0.060, 0.900, 0.100, color, lw=1.3)
        ax.text(0.070, y - 0.010, name, fontsize=10.0, color=color,
                weight="bold", ha="left", va="center", zorder=7)
        ax.text(0.330, y - 0.010, calc, fontsize=9.0, color=DARK,
                ha="left", va="center", zorder=7)
        ax.text(0.680, y - 0.010, note, fontsize=8.0, color=SLATE,
                ha="left", va="center", zorder=7)
        y -= 0.125

    card(ax, 0.045, 0.255, 0.900, 0.130, LIGHT, face="white")
    ax.text(0.068, 0.355, "谁受影响更大", fontsize=8.6, color=DARK,
            weight="bold", ha="left", va="center", zorder=7)
    ax.plot([0.068, 0.922], [0.337, 0.337], color=LIGHT, linewidth=0.9, zorder=7)
    ax.text(0.068, 0.305, "·　出口占比高的：消费税增加成本，出口退税下调减少返还，两头挤。",
            fontsize=7.6, color=SLATE, ha="left", va="center", zorder=7)
    ax.text(0.068, 0.273, "·　有品牌溢价与长期锁价协议的：可以把成本谈出去。",
            fontsize=7.6, color=SLATE, ha="left", va="center", zorder=7)

    save(fig, "图2_谁受影响最大")


def fig3():
    fig, ax = page(
        "政策在引导什么",
        "免税不是补贴，是指方向",
        source="来源：对财政部公告税目安排的公开信息解读。",
        punch="这两年，是政策给的加速期，也是倒计时。",
        foot="说明：本图为政策指向的分析，不代表主管部门的公开表述。")

    flow(ax, [
        ("锂：开始缴税", "成本基数上行", NAVY),
        ("钠 / 固态：免税", "两年成本优势", TEAL),
        ("2028 年底", "免税到期，同台竞争", RED),
    ], y=0.590, x0=0.080, w=0.250, h=0.135, gap=0.065, arrow_color=GRAY)

    card(ax, 0.045, 0.310, 0.900, 0.200, LIGHT, face="white")
    ax.text(0.068, 0.478, "为什么选这两个方向", fontsize=8.6, color=DARK,
            weight="bold", ha="left", va="center", zorder=7)
    ax.plot([0.068, 0.922], [0.458, 0.458], color=LIGHT, linewidth=0.9, zorder=7)

    rows = [
        ("钠电", "钠资源丰富、成本低，可缓解锂的对外依存压力。"),
        ("固态", "下一代技术方向，需要窗口期把产业链跑通。"),
        ("共性", "免税是优势，但技术成熟度、配套、客户接受度都不是税能解决的。"),
    ]
    y = 0.420
    for tag, text in rows:
        ax.text(0.068, y, tag, fontsize=7.8, color=NAVY, weight="bold",
                ha="left", va="center", zorder=7)
        ax.text(0.140, y, text, fontsize=7.5, color=SLATE,
                ha="left", va="center", zorder=7)
        y -= 0.044

    save(fig, "图3_政策在引导什么")


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", os.path.dirname(os.path.abspath(__file__)))
