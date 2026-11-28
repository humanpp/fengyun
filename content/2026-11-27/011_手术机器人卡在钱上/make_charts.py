# -*- coding: utf-8 -*-
"""
《手术机器人进医院，卡住的不是技术，是钱》配套图表

事实口径（北京市卫生健康委 2026-11-26 介绍，经媒体当日报道）：
  · 北京累计获批 45 个医用手术机器人注册证，数量居全国首位，覆盖骨科、神经外科、
    口腔、腹腔镜、介入等，并向眼科、心血管、放疗、儿科拓展。
  · 全国首创手术机器人融资租赁平台：租金分期、维保升级、替换保障、灵活处置。
  · 积水潭、世纪坛、友谊、安贞等 10 家机构完成 16 台租赁入院，另有 13 台推进中。
  · 截至前三季度，市属医院投入手术机器人 61 台，完成辅助操作 1.37 万余人次，
    同比增长 49%。
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "_kit")))

from chart_kit import (NAVY, RED, GRAY, SLATE, LIGHT, DARK, PALE, TEAL,
                       page, save, card, kpi_row, flow, columns)


def fig1():
    fig, ax = page(
        "能造、在买、在用",
        "三个数字，三个不同的阶段",
        source="来源：北京市卫生健康委 2026-11-26 介绍，经媒体当日报道。"
               "注册证数与设备台数、操作人次口径不同。",
        punch="技术过关只是第一步，能不能算得过账才是关键。",
        foot="事实来源：北京累计 45 个注册证；市属医院投入 61 台；"
             "前三季度辅助操作 1.37 万余人次、同比 +49%。")

    kpi_row(ax, [
        ("能造", "45 个", "累计获批注册证，全国首位", NAVY),
        ("在买", "61 台", "市属医院已投入", TEAL),
        ("在用", "1.37 万", "前三季度辅助操作人次", RED),
    ], x0=0.045, y=0.600, w_each=0.283, h=0.140, gap=0.025)

    card(ax, 0.045, 0.320, 0.900, 0.220, LIGHT, face="white")
    ax.text(0.068, 0.498, "三个数字分别说明什么", fontsize=8.6, color=DARK,
            weight="bold", ha="left", va="center", zorder=7)
    ax.plot([0.068, 0.922], [0.478, 0.478], color=LIGHT, linewidth=0.9, zorder=7)

    rows = [
        ("45 个证", "产品侧的成熟度：能造出来，也拿到了准入。", NAVY),
        ("61 台", "机构侧的采纳度：医院愿意买，也装得进去。", TEAL),
        ("1.37 万人次", "临床侧的使用度：真正跑起来了，同比 +49%。", RED),
    ]
    y = 0.438
    for tag, text, color in rows:
        ax.text(0.068, y, tag, fontsize=7.8, color=color, weight="bold",
                ha="left", va="center", zorder=7)
        ax.text(0.205, y, text, fontsize=7.5, color=SLATE,
                ha="left", va="center", zorder=7)
        y -= 0.046

    ax.text(0.068, 0.348, "注册证代表「能造」，使用量才代表「在用」——后者比前者更有信息量。",
            fontsize=7.6, color=GRAY, ha="left", va="center", zorder=7)

    save(fig, "图1_三个数字")


def fig2():
    fig, ax = page(
        "把「买设备」变成「买服务」",
        "融资租赁的四句话，对应四个真实痛点",
        source="来源：北京市卫生健康委 2026-11-26 介绍（全国首创手术机器人融资租赁平台）。",
        punch="设备国产化，才是租金降下来的前提。",
        foot="事实来源：平台提供「租金分期、维保升级、替换保障、灵活处置」全生命周期服务；"
             "10 家机构完成 16 台租赁入院，另有 13 台推进中。")

    rows = [
        ("租金分期", "一次性几百万资本开支 → 每年运营费用", NAVY),
        ("维保升级", "医院不必自建维护团队，也不必担心版本落后", TEAL),
        ("替换保障", "设备更新有通道，技术过时风险被转移", SLATE),
        ("灵活处置", "不再适用时有退出机制，不被设备绑住", RED),
    ]
    y = 0.640
    for tag, text, color in rows:
        card(ax, 0.045, y - 0.050, 0.900, 0.066, LIGHT, face="white", lw=0.8)
        ax.text(0.068, y - 0.017, tag, fontsize=8.2, color=color, weight="bold",
                ha="left", va="center", zorder=7)
        ax.text(0.230, y - 0.017, text, fontsize=7.6, color=SLATE,
                ha="left", va="center", zorder=7)
        y -= 0.088

    card(ax, 0.045, 0.280, 0.900, 0.065, LIGHT, face=PALE)
    ax.text(0.068, 0.312, "10 家医疗机构已完成 16 台租赁入院，另有 13 台正有序推进。",
            fontsize=8.0, color=NAVY, weight="bold", ha="left", va="center", zorder=7)

    save(fig, "图2_四句话对应四个痛点")


def fig3():
    fig, ax = page(
        "机器人改变了什么，没改变什么",
        "它是执行工具，不是决策主体",
        source="来源：基于公开医学信息的科普性梳理，不构成医疗建议。",
        punch="技术解决「做得更准」，不解决「谁来做、花多少钱」。",
        foot="说明：机器人辅助手术的适应症、费用与报销比例因地区与医保政策而异，"
             "应以主治医师意见及当地政策为准。")

    columns(ax, [
        ("改变了", NAVY, "精度与稳定性",
         "· 过滤人手小幅抖动，狭小空间更精细\n"
         "· 三维视野，解剖结构更清楚\n"
         "· 切口更小、出血更少、恢复更快\n"
         "· 术者操作更符合人体工学",
         "边界", "改善的是「执行质量」，\n不是「该不该做这台手术」。"),
        ("没改变", RED, "决策与费用",
         "· 手术方案仍由医生决定\n"
         "· 不是所有手术都适合用机器人\n"
         "· 通常涉及单独收费项目\n"
         "· 报销比例因地区与医保政策而异",
         "边界", "决定手术方式前，\n值得把费用问清楚。"),
    ], y=0.340, h=0.400, x0=0.045, gap=0.024, w=0.438)

    save(fig, "图3_改变与没改变")


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", os.path.dirname(os.path.abspath(__file__)))
