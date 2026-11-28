# -*- coding: utf-8 -*-
"""
《电动自行车被约谈 15 家：这次管的是你的电池》配套图表

事实口径（市场监管总局 2026-11-27，经媒体报道）：
  · 集中约谈 15 家电动自行车企业。
  · 要求：严格执行「一车一池一充一码」；缺陷产品立即召回；
    不得以折价或证书恢复为由拒绝退车。
  · 充电器新国标 2026-12-01 施行；20 项回收拆解强标征求意见。
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "_kit")))

from chart_kit import (NAVY, RED, GRAY, SLATE, LIGHT, DARK, PALE, TEAL,
                       page, save, card, flow, columns)


def fig1():
    fig, ax = page(
        "约谈提出的三条硬要求",
        "每一条都指向同一个目标：让车、电池、充电器对得上",
        source="来源：市场监管总局 2026-11-27 约谈消息，经腾讯新闻、中国网等报道。",
        punch="过去那种「几百块换个电池多跑五十公里」的便宜，正在被算进安全账里。",
        foot="事实来源：一车一池一充一码、缺陷产品立即召回、不得以折价或证书恢复为由拒绝退车，"
             "据 2026-11-27 公开报道。")

    cards = [
        ("一车一池一充一码", NAVY,
         "一辆车、一块电池、一个充电器、\n一个编码，四者一一对应。\n\n"
         "让非标电池在系统和物理上\n都无法装进车里。"),
        ("缺陷产品立即召回", TEAL,
         "企业须建立追溯体系，\n能定位到具体批次。\n\n"
         "不再是「发现问题再研究」，\n而是发现即召回。"),
        ("不得拒绝退车", RED,
         "不得以折价、证书恢复\n等理由推诿退车。\n\n"
         "把售后的推诿空间\n从制度上堵掉。"),
    ]
    x = 0.045
    w = 0.288
    for title, color, body in cards:
        card(ax, x, 0.380, w, 0.330, color, lw=1.3)
        ax.text(x + 0.022, 0.660, title, fontsize=9.6, color=color,
                weight="bold", ha="left", va="center", zorder=7)
        ax.plot([x + 0.022, x + w - 0.022], [0.638, 0.638], color=LIGHT,
                linewidth=0.9, zorder=7)
        ax.text(x + 0.022, 0.605, body, fontsize=7.6, color=SLATE,
                ha="left", va="top", zorder=7, linespacing=2.0)
        x += w + 0.018

    card(ax, 0.045, 0.270, 0.900, 0.070, LIGHT, face=PALE)
    ax.text(0.068, 0.305, "配套时间点：充电器新国标 2026-12-01 施行；"
                          "20 项回收拆解强制性标准正在征求意见。",
            fontsize=7.8, color=SLATE, ha="left", va="center", zorder=7)

    save(fig, "图1_三条硬要求")


def fig2():
    fig, ax = page(
        "两种竞争逻辑，两套成本结构",
        "过去拼谁便宜，现在拼谁合规",
        source="来源：基于公开报道的机制梳理，非统计数据。",
        punch="合规是有成本的，而成本最终会体现在售价上。",
        foot="说明：本图为竞争逻辑的定性对比，不含具体企业的成本数据。")

    columns(ax, [
        ("过去十年", GRAY, "价格战",
         "· 同样续航、同样外观，谁便宜谁赢\n"
         "· 压成本：电池用便宜的、充电器用最低配\n"
         "· 非标电池与解速改装形成灰色产业链\n"
         "· 优势来源：规模与渠道",
         "代价", "安全成本被外部化，\n由使用者和公共消防承担。"),
        ("接下来", NAVY, "合规战",
         "· CCC 认证、飞行检查、一致性管控\n"
         "· 召回体系要求能定位到具体批次\n"
         "· 「一车一池一充一码」切断非标供应链\n"
         "· 优势来源：体系能力与售后",
         "代价", "合规投入前置，\n小厂要么补课要么退出。"),
    ], y=0.340, h=0.400, x0=0.045, gap=0.024, w=0.438)

    save(fig, "图2_两种竞争逻辑")


def fig3():
    fig, ax = page(
        "一条被忽视的链条",
        "改装为什么危险：省下的钱，风险在别处",
        source="来源：基于公开安全信息的机制梳理。事故原因认定以消防与交管部门结论为准。",
        punch="BMS 是按原装电池设计的，换了电池，它就看不见真实状态了。",
        foot="说明：本图为安全机制的科普性说明，不针对任何具体品牌或产品，不构成购车建议。")

    flow(ax, [
        ("换大容量电池", "几百元，续航翻倍", GRAY),
        ("BMS 失配", "监测不到真实状态", TEAL),
        ("过充过热", "热失控风险上升", RED),
        ("监管介入", "编码绑定＋强制召回", NAVY),
    ], y=0.600, x0=0.045, w=0.200, h=0.110, gap=0.025, arrow_color=GRAY)

    card(ax, 0.045, 0.285, 0.900, 0.250, LIGHT, face="white")
    ax.text(0.068, 0.510, "对骑车的人，四条现实提醒", fontsize=8.6, color=DARK,
            weight="bold", ha="left", va="center", zorder=7)
    ax.plot([0.068, 0.922], [0.490, 0.490], color=LIGHT, linewidth=0.9, zorder=7)

    rows = [
        ("改装车", "路检或事故认定时可能有麻烦，各地执行力度不同。"),
        ("充电器", "12-01 后买新的，认准新国标，别用不匹配的充电器。"),
        ("换电池", "优先原厂渠道，兼容电池省的钱可能以别的方式还回去。"),
        ("旧电池", "别随便卖，回收拆解正在纳入规范渠道。"),
    ]
    y = 0.450
    for tag, text in rows:
        ax.text(0.068, y, tag, fontsize=7.6, color=NAVY, weight="bold",
                ha="left", va="center", zorder=7)
        ax.text(0.150, y, text, fontsize=7.4, color=SLATE,
                ha="left", va="center", zorder=7)
        y -= 0.042

    save(fig, "图3_改装链条与提醒")


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", os.path.dirname(os.path.abspath(__file__)))
