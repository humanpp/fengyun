# -*- coding: utf-8 -*-
"""
《一天开源四个模型：AI 竞赛的赛道，悄悄换了》配套图表

事实口径（均为发布方口径，无第三方复测）：
  · 蚂蚁百灵 Ling-3.2-air：原生多模态，MoE，总参 1,240 亿、每词元激活 55 亿；
    SWE-bench Pro 26.40 → 58.28；AutomationBench-AA 15.7% → 61%；
    Terminal-Bench 4.0 通过率 0 → 27%；MIT 许可，Hugging Face 上架。
  · 上海 AI Lab Sage-Interaction：全双工，可随时打断，响应时延约 1.29 秒。
  · 英伟达 Nemotron-Labs-Image-30B-A3B：总参约 300 亿、每词元激活约 30 亿。
  · 腾讯混元 DFly2：投机采样草稿模型，19 个评测集，单项最高提速 4.2 倍。
  · 小红书 3DCodeFactory：5,045 个复杂任务、5.52B tokens 数据集。
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "_kit")))

from chart_kit import (NAVY, RED, GRAY, SLATE, LIGHT, DARK, PALE, TEAL,
                       page, save, card, flow, kpi_row)


def fig1():
    fig, ax = page(
        "同一天，五个开源动作",
        "2026 年 11 月 26 日，三条战线同时推进",
        source="来源：各发布方 2026-11-26 公开信息及站长之家、腾讯新闻、界面新闻当日报道。",
        punch="没有一个是冲着「最大参数」去的。",
        foot="事实来源：蚂蚁百灵、上海人工智能实验室、英伟达、腾讯混元、小红书 2026-11-26 发布信息；"
             "技术指标均为发布方口径。")

    rows = [
        ("蚂蚁百灵", "Ling-3.2-air", "执行层　总参 1,240 亿，每词元只激活 55 亿", NAVY),
        ("上海 AI Lab", "Sage-Interaction", "交互层　全双工，可随时打断，时延约 1.29 秒", TEAL),
        ("腾讯混元", "DFly2", "工程层　旁挂加速，长上下文单项最高提速 4.2 倍", SLATE),
        ("英伟达", "Nemotron-Image-30B", "成本层　生图模型，每步激活约 30 亿", NAVY),
        ("小红书", "3DCodeFactory", "数据层　3D 合成框架，5.52B tokens 数据集", TEAL),
    ]

    card(ax, 0.045, 0.290, 0.900, 0.345, LIGHT, face="white")
    y = 0.598
    for org, name, desc, color in rows:
        ax.text(0.070, y, org, fontsize=8.0, color=GRAY, ha="left",
                va="center", zorder=7)
        ax.text(0.215, y, name, fontsize=9.2, color=color, weight="bold",
                ha="left", va="center", zorder=7)
        ax.text(0.430, y, desc, fontsize=7.6, color=SLATE, ha="left",
                va="center", zorder=7)
        y -= 0.062
        if y > 0.310:
            ax.plot([0.070, 0.920], [y + 0.026, y + 0.026], color="#f2f3f5",
                    linewidth=0.8, zorder=5)

    save(fig, "图1_同日开源的五件事")


def fig2():
    fig, ax = page(
        "Ling-3.2-air 的三个跃升",
        "官方给出的评测里，涨得最狠的都不是「答题」",
        source="来源：站长之家 2026-11-26 引述发布方评测数据。均为厂商自测口径，无第三方复测。",
        punch="三个指标的共同点是：都不是答题，而是干活。",
        foot="事实来源：蚂蚁百灵 Ling-3.2-air 发布信息（经站长之家 2026-11-26 转述）。"
             "分数定义与测试条件由发布方设定。")

    rows = [
        ("SWE-bench Pro", "26.40", "58.28", "代码仓库问题解决", NAVY),
        ("AutomationBench-AA", "15.7%", "61%", "多步骤自动化工作流", TEAL),
        ("Terminal-Bench 4.0", "0", "27%", "终端任务通过率", RED),
    ]

    y = 0.560
    for name, before, after, note, color in rows:
        ax.text(0.060, y + 0.038, name, fontsize=8.6, color=DARK,
                weight="bold", ha="left", va="center", zorder=7)
        ax.text(0.060, y + 0.006, note, fontsize=7.2, color=GRAY,
                ha="left", va="center", zorder=7)

        ax.text(0.360, y + 0.024, before, fontsize=13.0, color=GRAY,
                weight="bold", ha="center", va="center", zorder=7)
        ax.annotate("", xy=(0.520, y + 0.024), xytext=(0.415, y + 0.024),
                    arrowprops=dict(arrowstyle="-|>", color=LIGHT,
                                    linewidth=1.4), zorder=6)
        ax.text(0.620, y + 0.024, after, fontsize=17.0, color=color,
                weight="bold", ha="center", va="center", zorder=7)
        y -= 0.105

    card(ax, 0.045, 0.195, 0.900, 0.062, LIGHT, face=PALE)
    ax.text(0.068, 0.226, "上一代 → 本代，均为发布方口径；三组指标量纲不同，仅示意提升幅度。",
            fontsize=7.4, color=SLATE, ha="left", va="center", zorder=7)

    save(fig, "图2_三个跃升")


def fig3():
    fig, ax = page(
        "竞争的重心，正在往右移",
        "从「造更强的模型」，到「造更好用的流水线」",
        source="来源：2026-11-26 五个开源项目的技术定位归纳。",
        punch="技术扩散之后，竞争就落在工艺和成本上。",
        foot="说明：本图为对当日开源项目技术侧重点的归纳，非官方分类，不涉及能力排序。")

    flow(ax, [
        ("比参数规模", "谁的模型更大", GRAY),
        ("比跑分", "谁超过谁几分", SLATE),
        ("比单位任务成本", "跑一次多少钱", TEAL),
        ("比可部署性", "能不能塞进现有系统", NAVY),
    ], y=0.590, x0=0.045, w=0.200, h=0.110, gap=0.025, arrow_color=GRAY)

    card(ax, 0.045, 0.290, 0.900, 0.220, LIGHT, face="white")
    ax.text(0.068, 0.484, "四个模型各自对准的一项成本", fontsize=8.6, color=DARK,
            weight="bold", ha="left", va="center", zorder=7)
    ax.plot([0.068, 0.922], [0.464, 0.464], color=LIGHT, linewidth=0.9, zorder=7)

    rows = [
        ("推理成本", "Ling-3.2-air 把每词元激活压到 55 亿，总量 1,240 亿。", NAVY),
        ("等待成本", "Sage-Interaction 把响应时延做到约 1.29 秒，且可打断。", TEAL),
        ("长上下文成本", "DFly2 在 128K 场景下提升接收长度与加速比。", SLATE),
        ("部署成本", "30B 级生图模型，激活 3B，私有化门槛下降。", RED),
    ]
    y = 0.424
    for tag, text, color in rows:
        ax.text(0.068, y, tag, fontsize=7.6, color=color, weight="bold",
                ha="left", va="center", zorder=7)
        ax.text(0.185, y, text, fontsize=7.4, color=SLATE,
                ha="left", va="center", zorder=7)
        y -= 0.042

    save(fig, "图3_竞争重心迁移")


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", os.path.dirname(os.path.abspath(__file__)))
