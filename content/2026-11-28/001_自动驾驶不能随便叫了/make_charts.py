# -*- coding: utf-8 -*-
"""
《明年 7 月起，"自动驾驶"这四个字不能随便用了》配套图表

事实口径：
  · 《智能网联汽车 自动驾驶系统安全要求》2027-07-01 实施，国内首部 L3、L4
    级自动驾驶强制性国家标准，引望为主要起草单位之一（中国汽车工业信息网 2026-11-27）。
  · L0–L5 分级的核心是责任归属，而非技术能力排序。
  · 城区领航辅助下探至 15 万级车型（广州车展 2026-11-27 报道）。
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "_kit")))

from chart_kit import (NAVY, RED, GRAY, SLATE, LIGHT, DARK, PALE, TEAL,
                       page, save, card, flow, columns)


def fig1():
    fig, ax = page(
        "分级分的不是能力，是责任",
        "L0 到 L5，真正的分水岭在 L2 与 L3 之间",
        source="来源：SAE 分级定义及国内相关标准通行表述。"
               "强制性国标针对 L3、L4 级，2027-07-01 实施。",
        punch="不是「谁更聪明」，是「谁担责」。",
        foot="说明：本图为分级定义的示意，具体等级认定与技术指标以正式标准文本为准。")

    items = [
        ("L0", "无自动化", GRAY),
        ("L1", "单一辅助", GRAY),
        ("L2", "组合辅助", SLATE),
        ("L3", "有条件自动", TEAL),
        ("L4", "高度自动", NAVY),
        ("L5", "完全自动", NAVY),
    ]
    x = 0.045
    w = 0.130
    gap = 0.016
    for tag, name, color in items:
        card(ax, x, 0.640, w, 0.140, color, lw=1.2)
        ax.text(x + w / 2, 0.740, tag, fontsize=14.0, color=color,
                weight="bold", ha="center", va="center", zorder=7)
        ax.text(x + w / 2, 0.685, name, fontsize=7.4, color=SLATE,
                ha="center", va="center", zorder=7)
        x += w + gap

    ax.plot([0.045, 0.485], [0.615, 0.615], color=GRAY, linewidth=1.6)
    ax.text(0.265, 0.582, "责任在驾驶员", fontsize=8.6, color=GRAY,
            weight="bold", ha="center", va="center")
    ax.plot([0.505, 0.921], [0.615, 0.615], color=RED, linewidth=1.6)
    ax.text(0.713, 0.582, "责任转向系统与车企", fontsize=8.6, color=RED,
            weight="bold", ha="center", va="center")

    card(ax, 0.045, 0.380, 0.900, 0.110, LIGHT, face=PALE)
    ax.text(0.068, 0.452, "手能不能离开方向盘，是这条线的物理体现；"
                          "出事谁赔，是这条线的法律本质。",
            fontsize=8.0, color=SLATE, ha="left", va="center", zorder=7)
    ax.text(0.068, 0.412, "一个系统做得再流畅，只要它要求你随时准备接管，它就还是 L2。",
            fontsize=8.0, color=DARK, weight="bold", ha="left", va="center", zorder=7)

    save(fig, "图1_分级与责任")


def fig2():
    fig, ax = page(
        "同一个路口，两种责任",
        "L2 与 L3 的差别，不在传感器数量，在出事后谁签字",
        source="来源：SAE 分级定义。责任划分的实务认定须依据现行法律与生效裁判。",
        punch="宣传可以模糊，责任不能模糊。",
        foot="说明：本图为分级机制的对比，不构成法律意见，也不涉及任何车型的能力评价。")

    columns(ax, [
        ("L2 组合辅助", SLATE, "人在开，系统帮忙",
         "· 驾驶主体：驾驶员\n"
         "· 手可以短暂松开，但不能离开\n"
         "· 系统随时可能退出，人须立即接管\n"
         "· 出事故：驾驶员承担责任",
         "法律地位", "本质上仍是「辅助工具」，\n与倒车雷达同一法律类别。"),
        ("L3 有条件自动", RED, "系统在开，车企担责",
         "· 驾驶主体：系统（限特定条件）\n"
         "· 特定场景下可脱手、可转移注意力\n"
         "· 系统处理不了时须给足接管时间\n"
         "· 出事故：责任转向车企",
         "法律地位", "这是分水岭。\n所以车企宁可不叫 L3。"),
    ], y=0.340, h=0.400, x0=0.045, gap=0.024, w=0.438)

    save(fig, "图2_L2与L3的分水岭")


def fig3():
    fig, ax = page(
        "标准落地，改变的是三件事",
        "不是技术突破，是把模糊地带划清",
        source="来源：对中国汽车工业信息网 2026-11-27 报道的归纳。",
        punch="标准是开门，产品是过门，中间还有距离。",
        foot="说明：三个变化为基于报道的推断性归纳，具体执行以正式标准与主管部门要求为准。")

    flow(ax, [
        ("命名收敛", "配置表按等级标注\n形容词失效", NAVY),
        ("条件明确", "写好限速、路段\n与天气边界", TEAL),
        ("准入前置", "测试、认证、\n责任与保险配套", RED),
    ], y=0.590, x0=0.080, w=0.250, h=0.135, gap=0.065, arrow_color=GRAY)

    card(ax, 0.045, 0.320, 0.900, 0.190, LIGHT, face="white")
    ax.text(0.068, 0.478, "买车时该看什么", fontsize=8.6, color=DARK,
            weight="bold", ha="left", va="center", zorder=7)
    ax.plot([0.068, 0.922], [0.458, 0.458], color=LIGHT, linewidth=0.9, zorder=7)

    rows = [
        ("看等级", "配置表上写的是 L2 还是 L3，不宣传语。", NAVY),
        ("看边界", "能用在哪条路、多快、什么天气。", TEAL),
        ("看责任", "出事之后，合同里谁承担。", RED),
    ]
    y = 0.420
    for tag, text, color in rows:
        ax.text(0.068, y, tag, fontsize=7.8, color=color, weight="bold",
                ha="left", va="center", zorder=7)
        ax.text(0.160, y, text, fontsize=7.6, color=SLATE,
                ha="left", va="center", zorder=7)
        y -= 0.044

    save(fig, "图3_标准落地后的三个变化")


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", os.path.dirname(os.path.abspath(__file__)))
