# -*- coding: utf-8 -*-
"""
《英伟达停发四国服务器：这次被管住的，不只是芯片》配套图表

事实口径：
  · 英国《金融时报》2026-11-26：英伟达通知制造合作伙伴，暂停向马来西亚、新加坡、
    泰国、印度尼西亚交付搭载其芯片的服务器；戴尔、超微电脑已通知四国买家订单无法
    发货，恢复时间不明确。
  · 美国商务部《管控对先进半导体的远程访问》临时最终规则：2026-11-16 发布、
    11-19 生效；向新加坡、马来西亚、泰国、印尼和巴西出口先进 AI 芯片须获许可，
    管制延伸至海外数据中心远程算力访问。
  · 彭博 2026-11-25—26：Bridge Data Centres 66 亿美元贷款被暂缓；Digital Halo
    3.72 亿美元融资重新尽调；新规致数千颗 B300 GPU 寻求转售。
  · 广东省《算力发展"十五五"规划》（2026-11-26 印发）：2028 年智算规模突破
    1000EFlops（FP16），鼓励算力中心优先使用国产算力芯片。
  · MiniMax 2026-11-26 内部全员会：加快引入华为昇腾、阿里平头哥国产芯片。
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "_kit")))

from chart_kit import (NAVY, RED, GRAY, SLATE, LIGHT, DARK, PALE, TEAL,
                       page, save, card, title_row, kpi_row, columns, flow)


def fig1():
    fig, ax = page(
        "同一个算力，被三层管住",
        "管制对象从芯片，扩到服务器整机，再到远程访问",
        source="规则依据：美国商务部《管控对先进半导体的远程访问》临时最终规则，"
               "2026-11-16 发布、11-19 生效；发货暂停据英国《金融时报》2026-11-26。",
        punch="管的不是东西在哪，而是能力被谁用了。",
        foot="事实来源：英国《金融时报》2026-11-26；美国商务部临时最终规则（2026-11-16 发布、11-19 生效）。")

    flow(ax, [
        ("第一层　管实物", "芯片能不能卖", NAVY),
        ("第二层　管载体", "整机算不算管制物项", SLATE),
        ("第三层　管访问", "网络连上算不算使用", TEAL),
        ("结果", "算力带上归属", RED),
    ], y=0.640, x0=0.045, w=0.200, h=0.105, gap=0.025, arrow_color=GRAY)

    card(ax, 0.045, 0.320, 0.900, 0.215, LIGHT, face="white")
    ax.text(0.068, 0.498, "三层各自堵住的路", fontsize=8.6, color=DARK,
            weight="bold", ha="left", va="center", zorder=7)
    ax.plot([0.068, 0.922], [0.478, 0.478], color=LIGHT, linewidth=0.9, zorder=7)

    rows = [
        ("实物层", "堵的是直接采购：谁能买、买多少、算力密度多高。", NAVY),
        ("载体层", "堵的是第三国组装再转手：芯片运出去，在当地装成服务器。", SLATE),
        ("访问层", "堵的是跨境调用：机器不动，通过网络远程使用算力。", TEAL),
    ]
    y = 0.438
    for tag, text, color in rows:
        ax.text(0.068, y, tag, fontsize=7.8, color=color, weight="bold",
                ha="left", va="center", zorder=7)
        ax.text(0.150, y, text, fontsize=7.6, color=SLATE,
                ha="left", va="center", zorder=7)
        y -= 0.044

    save(fig, "图1_管制的三级递进")


def fig2():
    fig, ax = page(
        "规则切换时，最先反应的是钱",
        "被暂缓的融资、发不出的订单、转手的卡",
        source="来源：彭博 2026-11-25—26 报道；英国《金融时报》2026-11-26。"
               "金额与进度以当事方及银行公告为准。",
        punch="银行不会等到机房建好才评估风险。",
        foot="事实来源：Bridge Data Centres 66 亿美元贷款被暂缓、Digital Halo 3.72 亿美元融资重新尽调，"
             "据彭博 2026-11-25—26；数千颗 B300 GPU 寻求转售、订单无法发货，据同期报道。")

    kpi_row(ax, [
        ("马来西亚　Bridge Data Centres", "66 亿美元", "贷款被暂缓", RED),
        ("Digital Halo", "3.72 亿美元", "融资重新尽调", SLATE),
        ("已到手的加速卡", "数千颗", "B300 寻求转售", NAVY),
    ], x0=0.045, y=0.600, w_each=0.283, h=0.120, gap=0.025)

    card(ax, 0.045, 0.300, 0.900, 0.240, LIGHT, face=PALE)
    ax.text(0.068, 0.508, "为什么金融端比产业端更早动", fontsize=8.6, color=DARK,
            weight="bold", ha="left", va="center", zorder=7)
    ax.plot([0.068, 0.922], [0.488, 0.488], color=LIGHT, linewidth=0.9, zorder=7)

    lines = [
        "机房建设周期以年计，贷款审批以月计。许可一旦存在不确定性，第一件事是停贷、重新审。",
        "所以即使将来许可放开，这些项目的资金成本与进度也已经改变——这部分损失不可逆。",
        "订单端同理：组装厂通知买家无法发货，但订单、定金、交付条款都已生效。",
    ]
    y = 0.448
    for t in lines:
        ax.text(0.068, y, "·　" + t, fontsize=7.6, color=SLATE,
                ha="left", va="center", zorder=7)
        y -= 0.045

    save(fig, "图2_被暂缓的钱和发不出的货")


def fig3():
    fig, ax = page(
        "两条路径，同一个方向",
        "一边是采购导向，一边是不得不适配",
        source="来源：广东省《算力发展\"十五五\"规划》2026-11-26 印发；"
               "MiniMax 内部全员会消息据 2026-11-26 报道。",
        punch="一条是「要求用」，一条是「不得不用」。",
        foot="事实来源：广东省政务服务和数据管理局、广东省发展和改革委员会 2026-11-26；"
             "MiniMax 加快引入昇腾、平头哥，据 2026-11-26 报道。规划目标与已落地产能是两回事。")

    columns(ax, [
        ("政策导向", NAVY, "广东：优先用国产",
         "《算力发展\"十五五\"规划》提出，到 2028 年\n"
         "智算规模突破 1000EFlops（FP16）；\n"
         "明确鼓励算力中心优先使用国产算力芯片；\n"
         "并提出缩小单芯片算力性能的代际差距。",
         "性质", "采购导向开始具体化。\n「鼓励」不等于强制，但会改变招标口径。"),
        ("企业适配", TEAL, "MiniMax：换供应来源",
         "创始人兼 CEO 闫俊杰在内部全员会表示，\n"
         "加快引入华为昇腾、阿里平头哥等国产芯片，\n"
         "降低对英伟达 GPU 的依赖。\n"
         "今年 8 月 H3 开源当天，昇腾、摩尔线程、\n沐曦已完成适配。",
         "性质", "不是主动选择，是供应约束下的\n必然动作。迁移成本真实存在。"),
    ], y=0.360, h=0.400, x0=0.045, gap=0.024, w=0.438)

    save(fig, "图3_政策与企业两条路径")


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", os.path.dirname(os.path.abspath(__file__)))
