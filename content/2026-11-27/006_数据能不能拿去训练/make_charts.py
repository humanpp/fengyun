# -*- coding: utf-8 -*-
"""
《你的数据能不能被拿去训练 AI？这份文件给了半个答案》配套图表

事实口径：
  · 国家数据局综合司 2026-11-26 发布《关于完善数据规则 赋能人工智能创新发展的
    若干意见（公开征求意见稿）》，征求意见至 2026-12-06。
  · 使用权人：可将数据用于 AI 训练和推理。
  · 经营权人：可将数据提供给他人用于 AI 训练和推理。
  · 三类可依规使用的数据：企业合法采集、经授权获取或复制转移、经加工形成实质
    改变的衍生数据。
  · 三项前提并列：不违反法律法规、不违反合同约定、不侵害他人合法权益。
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "_kit")))

from chart_kit import (NAVY, RED, GRAY, SLATE, LIGHT, DARK, PALE, TEAL,
                       page, save, card, flow, columns, kpi_row)


def fig1():
    fig, ax = page(
        "一份数据，两种权利人",
        "意见稿把「自己用」和「给别人用」拆开了",
        source="来源：国家数据局综合司 2026-11-26《关于完善数据规则 赋能人工智能创新发展的"
               "若干意见（公开征求意见稿）》。为征求意见稿，条文可能调整。",
        punch="能自己用，不等于能卖给别人用。",
        foot="事实来源：意见稿公开文本（2026-11-26 发布，征求意见至 12-06），经中国证券网报道。")

    flow(ax, [
        ("数据使用权人", "自己用于\n训练与推理", NAVY),
        ("数据经营权人", "提供给他人\n用于训练与推理", TEAL),
    ], y=0.600, x0=0.105, w=0.300, h=0.130, gap=0.150, arrow_color=GRAY)

    card(ax, 0.045, 0.290, 0.900, 0.235, LIGHT, face="white")
    ax.text(0.068, 0.492, "被点名的三类数据", fontsize=8.6, color=DARK,
            weight="bold", ha="left", va="center", zorder=7)
    ax.plot([0.068, 0.922], [0.472, 0.472], color=LIGHT, linewidth=0.9, zorder=7)

    rows = [
        ("一类", "企业生产经营中合法采集的数据", "日志、销售记录、传感器数据", NAVY),
        ("二类", "经授权获取或复制转移的数据", "来源须清楚，强调有授权", TEAL),
        ("三类", "经加工形成实质改变的衍生数据", "承认「加工」可以产生新权益", RED),
    ]
    y = 0.432
    for tag, text, note, color in rows:
        ax.text(0.068, y, tag, fontsize=7.6, color=color, weight="bold",
                ha="left", va="center", zorder=7)
        ax.text(0.125, y, text, fontsize=7.6, color=DARK,
                ha="left", va="center", zorder=7)
        ax.text(0.560, y, note, fontsize=7.2, color=GRAY,
                ha="left", va="center", zorder=7)
        y -= 0.052

    save(fig, "图1_两类权利人")


def fig2():
    fig, ax = page(
        "三道闸门同时成立，才叫「可以」",
        "这份文件给的是路径，不是豁免",
        source="来源：意见稿中三项并列前提（不违反法律法规、不违反合同约定、"
               "不侵害他人合法权益）。",
        punch="即使法律没禁止，你签的协议说了不能，那就是不能用。",
        foot="说明：本图为对意见稿前提条件的归纳，具体适用需结合合同条款与相关法律判断。")

    ax.text(0.045, 0.700, "三道闸门，必须同时成立", fontsize=11.0, color=DARK,
            weight="bold", ha="left", va="center")

    gates = [
        ("不违反\n法律法规", NAVY),
        ("不违反\n合同约定", TEAL),
        ("不侵害他人\n合法权益", RED),
    ]
    x = 0.070
    for name, color in gates:
        card(ax, x, 0.470, 0.240, 0.140, color, lw=1.3)
        ax.text(x + 0.120, 0.540, name, fontsize=9.0, color=color,
                weight="bold", ha="center", va="center", zorder=7,
                linespacing=1.7)
        x += 0.260

    ax.annotate("", xy=(0.845, 0.430), xytext=(0.070, 0.430),
                arrowprops=dict(arrowstyle="-|>", color=GRAY, linewidth=1.2))
    ax.text(0.045, 0.400, "才构成「可以用于训练和推理」", fontsize=8.6,
            color=NAVY, weight="bold", ha="left", va="center")

    card(ax, 0.045, 0.255, 0.900, 0.105, LIGHT, face=PALE)
    ax.text(0.068, 0.324, "三道闸门是并列关系，不是选择关系：任何一道不成立，"
                          "「可以用于训练」就不成立。",
            fontsize=7.8, color=SLATE, ha="left", va="center", zorder=7)
    ax.text(0.068, 0.285, "「不违反合同约定」这一条比很多人想的更硬——平台协议、"
                          "用户条款在这个意义上具有约束力。",
            fontsize=7.8, color=SLATE, ha="left", va="center", zorder=7)

    save(fig, "图2_三道闸门")


def fig3():
    fig, ax = page(
        "往前走了一步，但没走完",
        "解决了「有权益的人怎么用」，还没解决「权益怎么确定」",
        source="来源：对意见稿条款的公开信息梳理。「数据产权登记」为意见稿鼓励方向，"
               "配套规则尚未出台。",
        punch="确权是地基，这份文件先搭了框架，还没浇混凝土。",
        foot="说明：本图为基于意见稿文本的分析框架，不代表官方解读。")

    columns(ax, [
        ("已经明确", NAVY, "怎么用",
         "· 使用权人可自用于训练与推理\n"
         "· 经营权人可提供给他人使用\n"
         "· 三类数据依规可用\n"
         "· 鼓励产权登记、支持为数据付费",
         "状态", "规则已具雏形，\n方向明确。"),
        ("仍然待解", RED, "凭什么用",
         "· 公开数据中的作者权益如何界定\n"
         "· 平台格式条款能否替代授权\n"
         "· 衍生数据的「实质改变」如何认定\n"
         "· 数据定价与交易机制怎么建",
         "状态", "依赖后续配套制度，\n12-06 前仍是征求意见。"),
    ], y=0.340, h=0.400, x0=0.045, gap=0.024, w=0.438)

    save(fig, "图3_明确与待解")


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", os.path.dirname(os.path.abspath(__file__)))
