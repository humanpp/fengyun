# -*- coding: utf-8 -*-
"""
《国产 AI 芯片卖到韩国了，这次卖的不是一张卡》配套图表

事实口径：
  · 韩国媒体 2026-11-26：华为通过当地分销渠道在韩销售昇腾 950 系列，推介 Atlas 950
    超节点；含 950PR（推理）与 950DT（训练+推理解码）。
  · 华为公布规格：一套 Atlas 950 最多连接 8,192 颗 950DT。
  · 英国《金融时报》2026-11-26：英伟达暂停向马、新、泰、印尼交付搭载其芯片的服务器。
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "_kit")))

from chart_kit import (NAVY, RED, GRAY, SLATE, LIGHT, DARK, PALE, TEAL,
                       page, save, card, flow, columns, kpi_row)


def fig1():
    fig, ax = page(
        "同一个东西，两种卖法",
        "卖卡是把零件交给你，卖系统是把能力交给你",
        source="来源：韩国媒体 2026-11-26 报道；英国《金融时报》2026-11-26。"
               "本文不对任何产品的性能作比较。",
        punch="一边在收紧，一边在出海。这两件事发生在同一周。",
        foot="说明：本图为商业模式对比，不涉及具体产品的性能评价。")

    columns(ax, [
        ("卖卡", GRAY, "交付零件",
         "· 客户自己搭服务器、组网、调优\n"
         "· 软件栈围绕芯片架构生长\n"
         "· 生态一旦形成，迁移成本极高\n"
         "· 优势来源：十几年的开发者积累",
         "客户拿到", "一堆加速卡，\n以及一套必须学会的软件栈。"),
        ("卖系统", NAVY, "交付能力",
         "· 机柜、互联、供电、散热一起交付\n"
         "· 客户拿到的是「能跑模型的单元」\n"
         "· 降低客户的集成门槛\n"
         "· 优势来源：系统级设计与交付能力",
         "客户拿到", "一个能直接上电的集群，\n但软件迁移仍要自己做。"),
    ], y=0.340, h=0.400, x0=0.045, gap=0.024, w=0.438)

    save(fig, "图1_两种卖法")


def fig2():
    fig, ax = page(
        "8,192 这个数字在说什么",
        "大模型训练拼的不是单卡，是能连多宽",
        source="来源：华为公布的产品规格。为系统设计能力上限，不代表实际部署规模。",
        punch="瓶颈往往不在算力总量，而在卡与卡之间的通信效率。",
        foot="说明：8,192 颗为单套超节点的连接能力上限，实际部署规模以客户方案为准。")

    steps = [
        ("1 张卡", "单机算力有限", GRAY, 0.180),
        ("8 卡服务器", "一台机器内的互联", SLATE, 0.280),
        ("8,192 颗超节点", "跨机柜的大规模集群", NAVY, 0.375),
    ]
    x = 0.045
    for tag, note, color, w in steps:
        card(ax, x, 0.560, w, 0.130, color, lw=1.3)
        ax.text(x + w / 2, 0.640, tag, fontsize=10.0, color=color,
                weight="bold", ha="center", va="center", zorder=7)
        ax.text(x + w / 2, 0.592, note, fontsize=7.2, color=SLATE,
                ha="center", va="center", zorder=7)
        x += w + 0.030

    card(ax, 0.045, 0.320, 0.900, 0.180, LIGHT, face="white")
    ax.text(0.068, 0.468, "为什么互联比单卡更重要", fontsize=8.6, color=DARK,
            weight="bold", ha="left", va="center", zorder=7)
    ax.plot([0.068, 0.922], [0.448, 0.448], color=LIGHT, linewidth=0.9, zorder=7)

    rows = [
        ("训练", "几万张卡同时算，通信跟不上，卡就在等数据。"),
        ("推理", "并发请求越多，调度与带宽越关键。"),
        ("结论", "单卡再强，连不起来就是一堆孤岛。"),
    ]
    y = 0.412
    for tag, text in rows:
        ax.text(0.068, y, tag, fontsize=7.8, color=NAVY, weight="bold",
                ha="left", va="center", zorder=7)
        ax.text(0.140, y, text, fontsize=7.5, color=SLATE,
                ha="left", va="center", zorder=7)
        y -= 0.042

    save(fig, "图2_8192颗意味着什么")


def fig3():
    fig, ax = page(
        "出海最难的不是硬件",
        "三道门槛，一道比一道难",
        source="来源：基于公开产业信息的机制梳理。",
        punch="一台设备卖出去是订单，一套生态立起来是十年。",
        foot="说明：本图为出海门槛的分析框架，不代表任何具体市场的实际情况。")

    flow(ax, [
        ("软件生态", "框架、算子库、工具链\n都要重新适配", NAVY),
        ("合规与服务", "认证、数据要求\n本地团队支持", TEAL),
        ("长期信任", "客户要用三到五年\n会问「你还在不在」", RED),
    ], y=0.590, x0=0.080, w=0.250, h=0.135, gap=0.065, arrow_color=GRAY)

    card(ax, 0.045, 0.310, 0.900, 0.200, LIGHT, face="white")
    ax.text(0.068, 0.478, "迁移成本落在谁身上，是个博弈", fontsize=8.6, color=DARK,
            weight="bold", ha="left", va="center", zorder=7)
    ax.plot([0.068, 0.922], [0.458, 0.458], color=LIGHT, linewidth=0.9, zorder=7)
    ax.text(0.068, 0.420, "·　客户自己承担：采购意愿大幅下降，因为省下的硬件钱可能不够付迁移成本。",
            fontsize=7.6, color=SLATE, ha="left", va="center", zorder=7)
    ax.text(0.068, 0.382, "·　供应商承担：成本压在供应商身上，需要用规模摊薄。",
            fontsize=7.6, color=SLATE, ha="left", va="center", zorder=7)
    ax.text(0.068, 0.344, "·　这决定了「卖出去几套」和「留下几套」之间的差距。",
            fontsize=7.6, color=RED, weight="bold", ha="left", va="center", zorder=7)

    save(fig, "图3_出海的三道门槛")


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", os.path.dirname(os.path.abspath(__file__)))
