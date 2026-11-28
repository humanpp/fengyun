# -*- coding: utf-8 -*-
"""
《AI 陪你聊过的天，可能被当成资产卖掉》配套图表

事实口径（媒体 2026-11-27 报道）：
  · Character.AI 已申请破产保护，拟出售平台资产。
  · 拟出售清单含逾 2,100 万个美国账户的私密聊天记录，
    涉逾 210 万个注册时自报未满 18 岁的账户。
  · 2026-11-20，美国 42 个州总检察长向特拉华州破产法院提出异议。
  · 法院定于 2026-12-03 至 04 举行出售听证会。
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "_kit")))

from chart_kit import (NAVY, RED, GRAY, SLATE, LIGHT, DARK, PALE, TEAL,
                       page, save, card, flow, kpi_row, columns)


def fig1():
    fig, ax = page(
        "一条资产出售链",
        "从破产申请，到聊天记录进入交易清单",
        source="来源：媒体 2026-11-27 报道。程序尚在进行，资产范围与交易对象均未确定。",
        punch="用户的心理预期是「这是对话」，平台的账本上写的是「这是数据」。",
        foot="事实来源：Character.AI 破产保护申请、拟出售资产含聊天记录、42 州总检察长异议、"
             "12-03 至 04 听证会，据 2026-11-27 媒体报道。")

    flow(ax, [
        ("申请破产保护", "进入清偿程序", GRAY),
        ("出售平台资产", "厂房、专利、数据库", SLATE),
        ("聊天记录在列", "2100 万账户", NAVY),
        ("监管提出异议", "42 州总检察长", RED),
    ], y=0.610, x0=0.045, w=0.200, h=0.115, gap=0.025, arrow_color=GRAY)

    card(ax, 0.045, 0.320, 0.900, 0.180, LIGHT, face="white")
    ax.text(0.068, 0.468, "关键在于这句话", fontsize=8.6, color=DARK,
            weight="bold", ha="left", va="center", zorder=7)
    ax.plot([0.068, 0.922], [0.448, 0.448], color=LIGHT, linewidth=0.9, zorder=7)
    ax.text(0.068, 0.400, "总检察长的诉求不是「禁止交易」，而是「把未成年人数据排除出去」。",
            fontsize=8.4, color=SLATE, ha="left", va="center", zorder=7)
    ax.text(0.068, 0.358, "换句话说：如果这部分不属于未成年人，这笔交易在法律上可能没什么障碍。",
            fontsize=8.4, color=RED, weight="bold", ha="left", va="center", zorder=7)

    save(fig, "图1_一条资产出售链")


def fig2():
    fig, ax = page(
        "三个数字，构成这次争议的规模",
        "不是个别案例，是一个平台的全部对话",
        source="来源：媒体 2026-11-27 报道。数字为报道口径，非法院认定。",
        punch="2100 万条对话背后，是 2100 万次「以为很私密」的倾诉。",
        foot="事实来源：逾 2,100 万美国账户、逾 210 万自报未满 18 岁账户、42 州总检察长，"
             "据 2026-11-27 媒体报道。")

    kpi_row(ax, [
        ("涉及账户", "2,100 万", "美国账户的聊天记录", NAVY),
        ("其中未成年", "210 万", "注册时自报未满 18 岁", RED),
        ("联名反对", "42 州", "总检察长向法院提异议", TEAL),
    ], x0=0.045, y=0.580, w_each=0.283, h=0.140, gap=0.025)

    card(ax, 0.045, 0.310, 0.900, 0.200, LIGHT, face="white")
    ax.text(0.068, 0.478, "为什么这两个数字要分开看", fontsize=8.6, color=DARK,
            weight="bold", ha="left", va="center", zorder=7)
    ax.plot([0.068, 0.922], [0.458, 0.458], color=LIGHT, linewidth=0.9, zorder=7)

    rows = [
        ("2,100 万", "说明这不是个案，而是平台全部用户对话的整体处置。", NAVY),
        ("210 万", "说明其中相当一部分内容涉及未成年人，触碰了监管底线。", RED),
        ("差额", "剩下近 1,900 万普通成年用户的记录，争议要小得多。", SLATE),
    ]
    y = 0.420
    for tag, text, color in rows:
        ax.text(0.068, y, tag, fontsize=7.8, color=color, weight="bold",
                ha="left", va="center", zorder=7)
        ax.text(0.180, y, text, fontsize=7.5, color=SLATE,
                ha="left", va="center", zorder=7)
        y -= 0.044

    save(fig, "图2_三个数字")


def fig3():
    fig, ax = page(
        "三种关系，三种义务",
        "「有人听你说话」和「有人替你保密」不是一回事",
        source="来源：对法定保密义务范围的通行表述。本图为机制对比，不构成法律意见。",
        punch="AI 陪伴产品提供的「倾听」，是一种服务，不是一个保密关系。",
        foot="说明：法定保密义务的范围以现行法律及职业规范为准；平台与用户之间以用户协议为权利基础。")

    rows = [
        ("医生与患者", "法定保密义务", "泄露患者隐私可能承担法律责任", NAVY),
        ("律师与委托人", "法定保密义务", "未经同意不得披露委托事项", NAVY),
        ("心理咨询师与来访者", "法定保密义务", "保密是执业的基本前提", NAVY),
        ("用户与 AI 平台", "合同约定", "只有隐私政策，且含「业务转让」条款", RED),
    ]
    y = 0.700
    for who, duty, note, color in rows:
        card(ax, 0.045, y - 0.052, 0.900, 0.070, color, lw=0.9 if color == NAVY else 1.4)
        ax.text(0.070, y - 0.017, who, fontsize=8.4, color=color, weight="bold",
                ha="left", va="center", zorder=7)
        ax.text(0.310, y - 0.017, duty, fontsize=8.4, color=color, weight="bold",
                ha="left", va="center", zorder=7)
        ax.text(0.470, y - 0.017, note, fontsize=7.4, color=SLATE,
                ha="left", va="center", zorder=7)
        y -= 0.082

    card(ax, 0.045, 0.300, 0.900, 0.075, LIGHT, face=PALE)
    ax.text(0.068, 0.337, "把「私密」和「永久」分开：真正不能外流的内容，不要输入到任何云端产品里。",
            fontsize=8.0, color=DARK, weight="bold", ha="left", va="center", zorder=7)

    save(fig, "图3_三种关系三种义务")


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", os.path.dirname(os.path.abspath(__file__)))
