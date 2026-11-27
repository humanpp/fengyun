# -*- coding: utf-8 -*-
"""
《光做线性运算，电做逻辑判断：绕开功耗墙的一条新路》配套图表

事实口径（C114 通信网 2026-11-13，报道 11 月 5 日 2026 移动网络大会发布）：
  · 中国移动正式推出"灵光"光电混合计算技术体系，联合曦智科技。
  · 四层架构：硬件层—基础软件层—模型算法层—应用层。
  · 三大特质：光算电控（光子承担高速线性运算，电路负责逻辑与非线性处理）、
    宽谱并行、极低功耗（破解芯片功耗墙）。
  · 两大痛点：光路扰动与器件偏差带来的光学精度误差；
    现有 AI 算法模型面向电芯片开发，难以直接适配光计算硬件。
  · 解法：算法层"误差感知自适应优化"；软件层"芯合-O"光计算基础软件栈。
  · 演示：曦智科技天枢·光立方光电混合计算系统 + 端网协同实时人脸检测。
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["figure.facecolor"] = "white"
plt.rcParams["axes.facecolor"] = "white"

NAVY = "#1f3a5f"
RED = "#b5544a"
GRAY = "#8a8f98"
SLATE = "#5f6673"
LIGHT = "#d8dbe0"
DARK = "#2b2f36"
PALE = "#eef0f3"
TEAL = "#3f6f6b"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep

Y_TITLE = 0.958
Y_SUB = 0.898
Y_PUNCH = 0.070
Y_FOOT = 0.020


def header(fig, title, sub):
    fig.text(0.045, Y_TITLE, title, fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, Y_SUB, sub, fontsize=10.6, color=GRAY,
             ha="left", va="top")


def footer(fig, text):
    fig.text(0.045, Y_FOOT, text, fontsize=7.6, color=GRAY,
             ha="left", va="bottom")


def punchline(fig, text):
    fig.text(0.045, Y_PUNCH, text, fontsize=10.4, color=DARK,
             ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


def card(ax, x, y, w, h, edge, face="white", lw=1.0, z=2):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.004,rounding_size=0.014",
        facecolor=face, edgecolor=edge, linewidth=lw, zorder=z))


def new_axes(fig):
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return ax


# ---------------------------------------------------------------- 图 1
def fig1():
    """光算电控"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "不是用光取代电，是分工",
           "官方三大特质之首：光算电控")

    card(ax, 0.048, 0.400, 0.420, 0.300, NAVY, lw=1.6)
    ax.text(0.072, 0.642, "光子", fontsize=15.0, color=NAVY,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.072, 0.582, "承担高速线性运算", fontsize=9.8, color=DARK,
            ha="left", va="center", zorder=6)
    rows_l = ["矩阵乘法这类操作为主", "传输近乎不损耗能量", "多波长可并行传输"]
    y = 0.536
    for r in rows_l:
        ax.text(0.072, y, "· " + r, fontsize=8.6, color=SLATE,
                ha="left", va="center", zorder=6)
        y -= 0.036
    ax.text(0.072, 0.424, "强项：算得快、算得省", fontsize=8.8, color=NAVY,
            weight="bold", ha="left", va="center", zorder=6)

    card(ax, 0.532, 0.400, 0.420, 0.300, RED, lw=1.6)
    ax.text(0.556, 0.642, "电路", fontsize=15.0, color=RED,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.556, 0.582, "负责逻辑与非线性处理", fontsize=9.8, color=DARK,
            ha="left", va="center", zorder=6)
    rows_r = ["条件判断、分支跳转", "激活函数等非线性环节", "状态与存储控制"]
    y = 0.536
    for r in rows_r:
        ax.text(0.556, y, "· " + r, fontsize=8.6, color=SLATE,
                ha="left", va="center", zorder=6)
        y -= 0.036
    ax.text(0.556, 0.424, "强项：做得对、管得住", fontsize=8.8, color=RED,
            weight="bold", ha="left", va="center", zorder=6)

    ax.text(0.500, 0.352, "两者叠起来，才叫「光算电控」", fontsize=10.0,
            color=DARK, ha="center", va="center")

    card(ax, 0.048, 0.148, 0.904, 0.086, TEAL, face=PALE, lw=1.2)
    ax.text(0.070, 0.202,
            "另外两个特质：宽谱并行（光子多通道并行）、极低功耗（近乎零功耗，破解芯片功耗墙）。",
            fontsize=9.2, color=DARK, ha="left", va="center", zorder=6)
    ax.text(0.070, 0.168,
            "三者是同一个物理特性在不同层面的体现。",
            fontsize=9.0, color=SLATE, ha="left", va="center", zorder=6)

    punchline(fig, "光计算赌的不是替代，是分工之后的能效比。")
    footer(fig, "事实来源：C114 通信网 2026-11-13《直击算力功耗墙！中国移动推出灵光光电混合计算体系》")
    fig.savefig(OUT + "图1_光算电控.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """两道工程关"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "真正的难点不在光，在这两道关",
           "物理特性早就成立，工程落地卡的是这两件事")

    # 关卡一
    card(ax, 0.048, 0.306, 0.440, 0.414, NAVY, lw=1.5)
    ax.text(0.072, 0.672, "第一关　精度", fontsize=12.0, color=NAVY,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.072, 0.620, "光路扰动、器件偏差", fontsize=9.2, color=DARK,
            ha="left", va="center", zorder=6)
    ax.text(0.072, 0.576, "结果会偏，且对温度、振动敏感", fontsize=8.6,
            color=SLATE, ha="left", va="center", zorder=6)
    ax.plot([0.072, 0.464], [0.550, 0.550], color=LIGHT, linewidth=1.0,
            zorder=6)
    ax.text(0.072, 0.508, "解法：误差感知自适应优化", fontsize=9.0,
            color=NAVY, weight="bold", ha="left", va="center", zorder=6)
    rows = ["误差前置训练", "光误差敏感权重标定", "模型感知反馈校正",
            "误差动态自适应"]
    y = 0.474
    for r in rows:
        ax.text(0.072, y, "· " + r, fontsize=8.4, color=SLATE,
                ha="left", va="center", zorder=6)
        y -= 0.035
    ax.text(0.072, 0.338, "思路：承认误差，让模型学会在误差里保持准确",
            fontsize=8.2, color=GRAY, ha="left", va="center", zorder=6)

    # 关卡二
    card(ax, 0.512, 0.306, 0.440, 0.414, RED, lw=1.5)
    ax.text(0.536, 0.672, "第二关　软件", fontsize=12.0, color=RED,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.536, 0.620, "现有 AI 算法都为电芯片开发", fontsize=9.2,
            color=DARK, ha="left", va="center", zorder=6)
    ax.text(0.536, 0.576, "算子、框架、编译链路搬不过来", fontsize=8.6,
            color=SLATE, ha="left", va="center", zorder=6)
    ax.plot([0.536, 0.928], [0.550, 0.550], color=LIGHT, linewidth=1.0,
            zorder=6)
    ax.text(0.536, 0.508, "解法：芯合-O 光计算基础软件栈", fontsize=9.0,
            color=RED, weight="bold", ha="left", va="center", zorder=6)
    rows2 = ["跨光子芯片迁移", "兼容主流 AI 模型", "光子算子抽象封装",
             "软硬件协同编译"]
    y = 0.474
    for r in rows2:
        ax.text(0.536, y, "· " + r, fontsize=8.4, color=SLATE,
                ha="left", va="center", zorder=6)
        y -= 0.035
    ax.text(0.536, 0.338, "思路：把底层硬件差异屏蔽掉，降低迁移成本",
            fontsize=8.2, color=GRAY, ha="left", va="center", zorder=6)

    ax.text(0.048, 0.258,
            "一个范式能不能活下来，往往不取决于硬件峰值，而取决于写代码的人愿不愿意用。",
            fontsize=9.4, color=DARK, ha="left", va="center")

    punchline(fig, "解决的不是「能不能算」，是「算得准不准、好不好用」。")
    footer(fig, "事实来源：C114 通信网 2026-11-13（两大痛点、误差感知自适应优化、芯合-O 四大能力）")
    fig.savefig(OUT + "图2_两道工程关.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """为什么选人脸检测"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "演示为什么挑人脸检测",
           "任务特性正好落在光计算现在能干的区间")

    rows = [
        ("线性运算密集", "光子的强项", True),
        ("数据量大", "本地处理省带宽", True),
        ("要求低时延", "边缘比上云快", True),
        ("可容忍一定精度误差", "检测框偏一点不影响使用", True),
        ("大模型复杂推理", "不在演示范围", False),
        ("科学计算高精度", "不在演示范围", False),
    ]

    y = 0.680
    ax.text(0.048, 0.752, "任务特性", fontsize=9.6, color=GRAY,
            ha="left", va="center")
    ax.text(0.470, 0.752, "和光计算的关系", fontsize=9.6, color=GRAY,
            ha="left", va="center")
    ax.plot([0.048, 0.952], [0.732, 0.732], color=LIGHT, linewidth=1.0)

    for name, why, good in rows:
        color = TEAL if good else GRAY
        mark = "适合" if good else "未涉及"
        ax.text(0.048, y, name, fontsize=9.4, color=DARK,
                ha="left", va="center")
        ax.text(0.470, y, why, fontsize=8.8, color=SLATE,
                ha="left", va="center")
        ax.text(0.940, y, mark, fontsize=8.6, color=color, weight="bold",
                ha="right", va="center")
        y -= 0.070

    ax.plot([0.048, 0.952], [0.318, 0.318], color=LIGHT, linewidth=1.0)

    ax.text(0.048, 0.268, "演示打通的是全链路：", fontsize=9.4, color=DARK,
            ha="left", va="center")
    chain = ["模型输入", "任务分发", "光子加速推理", "结果回传"]
    x = 0.048
    for i, c in enumerate(chain):
        w = 0.150
        card(ax, x, 0.210, w, 0.044, NAVY, face=PALE, lw=1.0)
        ax.text(x + w / 2, 0.232, c, fontsize=8.4, color=DARK,
                ha="center", va="center", zorder=6)
        if i < len(chain) - 1:
            ax.add_patch(FancyArrowPatch((x + w + 0.004, 0.232),
                                         (x + w + 0.026, 0.232),
                                         arrowstyle="-|>", mutation_scale=11,
                                         color=GRAY, linewidth=1.2, zorder=5))
        x += w + 0.030

    card(ax, 0.048, 0.122, 0.904, 0.052, LIGHT, face=PALE, lw=1.0)
    ax.text(0.070, 0.148,
            "选边缘视觉推理而不是大模型，说明团队清楚光计算现在能干什么。",
            fontsize=9.0, color=SLATE, ha="left", va="center", zorder=6)

    punchline(fig, "演示任务的选择，本身就是在划边界。")
    footer(fig, "事实来源：C114 通信网 2026-11-13（端网协同实时人脸检测系统、全链路闭环）")
    fig.savefig(OUT + "图3_为什么选人脸检测.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)


