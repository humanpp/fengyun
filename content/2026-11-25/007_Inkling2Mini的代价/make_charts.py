# -*- coding: utf-8 -*-
"""
《知识不涨、多轮不行、循环绕圈：Inkling 2 Mini 的五个代价》配套图表

事实口径：

一、循环买不来知识
  · TML 公告原文：循环提升推理，但不能让权重存下更多事实，
    知识主要由参数总量决定。
  · 变循环研究版上：长上下文基准（GraphWalks BFS、MRCR v2）随遍数提升；
    知识型基准（AA-Omniscience、SimpleQA Verified、SimpleVQA、WorldVQA）不随遍数提升。
  · AA-Omniscience v1.1 得分（越高越好，负数表示错误多于正确）：
    Inkling 2 Mini -8.6（非幻觉率 63.4%）；Qwen3.8-27B -6.4（71.4%）；
    Nemotron 3.5 Super VL -2.9（69.5%）；Muse Glimmer -32.2（16.4%）；
    Gemma 4 31B -48.5（14.5%）；Beam 1.0 +2.3（59.0%）。

二、多轮与多约束
  · 官方 Limitations：MultiChallenge 50.0%、ComplexConstraints v1.1 33.4%，
    并称两项均落后于 Qwen3.8-27B。
  · 模型卡表格实际：ComplexConstraints v1.1 中 Inkling 2 Mini 33.4%，
    Qwen3.8-27B 为 30.1%、Gemma 4 31B 为 31.6%、Muse Glimmer 35.6%、Beam 1.0 42.9%；
    模型卡表格中未见 Qwen3.8-27B 的 MultiChallenge 数据。
    → 官方表述与自身表格不一致，图按表格口径呈现。

三、循环的三笔开销（vLLM 单卡 GB200，TP1，4K 上下文，仅前向）
  · 1 遍：解码 1.51 ms（batch 1）、KV 容量 352K token
  · 2 遍：2.67 ms / 233K
  · 3 遍：3.85 ms / 175K
  · 3 遍共享 KV cache：3.86 ms / 194K
  · 24 层对应 48 个 KV cache 与 48 个 conv-state cache

四、自报与第三方
  · 第三方指数：AA Index 20.1、Vals Index 46.5%
  · 其余代理编程/检索/终端类基准标注 reported score

风格：克制传媒风，白底、低饱和配色、标题即结论（沿用本工作区既有规范）
输出目录 = 脚本所在目录
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

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
    """循环买不来知识"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "循环买不来知识",
           "AA-Omniscience v1.1：负分表示幻觉多于答对，柱子越长越差")

    items = [
        ("Gemma 4 31B", -48.5, 14.5, GRAY),
        ("Muse Glimmer", -32.2, 16.4, GRAY),
        ("Inkling 2 Mini", -8.6, 63.4, RED),
        ("Qwen3.8-27B", -6.4, 71.4, SLATE),
        ("Nemotron 3.5 Super VL", -2.9, 69.5, SLATE),
        ("Beam 1.0", 2.3, 59.0, TEAL),
    ]

    x0 = 0.330
    span = 0.130
    maxv = 48.5
    y = 0.700

    for name, score, nonhall, color in items:
        ax.text(x0 + span + 0.024, y, name, fontsize=9.6,
                color=RED if name == "Inkling 2 Mini" else DARK,
                weight="bold" if name == "Inkling 2 Mini" else "normal",
                ha="left", va="center")
        w = abs(score) / maxv * span
        if score < 0:
            ax.add_patch(Rectangle((x0 - w, y - 0.019), w, 0.038,
                                   facecolor=color, edgecolor=color,
                                   linewidth=0, alpha=0.88, zorder=4))
            ax.text(x0 - w - 0.008, y, f"{score:.1f}", fontsize=9.0,
                    color=color, weight="bold", ha="right", va="center",
                    zorder=6)
        else:
            ax.add_patch(Rectangle((x0, y - 0.019), w, 0.038,
                                   facecolor=color, edgecolor=color,
                                   linewidth=0, alpha=0.88, zorder=4))
            ax.text(x0 + w + 0.008, y, f"+{score:.1f}", fontsize=9.0,
                    color=color, weight="bold", ha="left", va="center",
                    zorder=6)
        y -= 0.082

    ax.plot([x0, x0], [0.745, 0.228], color=SLATE, linewidth=1.2)
    ax.text(x0 + 0.006, 0.236, "0", fontsize=8.6, color=GRAY, ha="left", va="bottom")

    # 右侧：非幻觉率
    ax.text(0.700, 0.752, "非幻觉率", fontsize=9.6, color=GRAY,
            ha="left", va="center")
    ax.plot([0.700, 0.952], [0.732, 0.732], color=LIGHT, linewidth=1.0)

    y = 0.700
    for name, score, nonhall, color in items:
        ax.add_patch(Rectangle((0.700, y - 0.015), 0.190 * nonhall / 100.0, 0.030,
                               facecolor=color, edgecolor=color,
                               linewidth=0, alpha=0.75, zorder=4))
        ax.text(0.700 + 0.190 * nonhall / 100.0 + 0.007, y, f"{nonhall}%",
                fontsize=8.8, color=color, ha="left", va="center", zorder=6)
        y -= 0.082

    card(ax, 0.048, 0.132, 0.904, 0.058, LIGHT, face=PALE, lw=1.0)
    ax.text(0.070, 0.161,
            "官方原文：循环提升推理，但不能让权重存下更多事实——知识主要由参数总量决定。",
            fontsize=9.2, color=DARK, ha="left", va="center", zorder=6)

    punchline(fig, "在这一项上，加法没用：加遍数、加层应用，都不会让它多记住东西。")
    footer(fig, "事实来源：Inkling 2 Mini 模型卡评测表（2026-11-20，AA-Omniscience v1.1 得分与非幻觉率）；"
                "TML《Introducing Inkling 2 Mini》Capabilities 一节")
    fig.savefig(OUT + "图1_循环买不来知识.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """三笔开销"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "循环的三笔开销",
           "vLLM 在单卡 GB200 的实测：TP1、4K 上下文、仅前向")

    rows = [
        ("解码一步（batch 1）", "1.51 ms", "3.85 ms", "慢 2.55 倍"),
        ("KV cache 容量", "352K token", "175K token", "掉 50%"),
        ("缓存份数（对 24 层权重）", "24 份", "48 份", "翻倍"),
    ]

    x1, x2, x3 = 0.048, 0.400, 0.615
    y = 0.700
    ax.text(x1, 0.760, "项目", fontsize=9.2, color=GRAY, ha="left", va="center")
    ax.text(x2, 0.760, "1 遍", fontsize=9.2, color=GRAY, ha="left", va="center")
    ax.text(x3, 0.760, "3 遍", fontsize=9.2, color=GRAY, ha="left", va="center")
    ax.text(0.800, 0.760, "代价", fontsize=9.2, color=GRAY, ha="left", va="center")
    ax.plot([0.048, 0.952], [0.740, 0.740], color=LIGHT, linewidth=1.0)

    for label, a, b, cost in rows:
        ax.text(x1, y, label, fontsize=9.8, color=DARK, ha="left", va="center")
        ax.text(x2, y, a, fontsize=11.0, color=SLATE, ha="left", va="center")
        ax.text(x3, y, b, fontsize=11.0, color=RED, weight="bold",
                ha="left", va="center")
        ax.text(0.800, y, cost, fontsize=9.6, color=RED, weight="bold",
                ha="left", va="center")
        ax.plot([0.048, 0.952], [y - 0.055, y - 0.055], color="#eceef1",
                linewidth=0.8)
        y -= 0.095

    card(ax, 0.048, 0.168, 0.430, 0.168, LIGHT, face=PALE, lw=1.0)
    ax.text(0.068, 0.312, "共享 KV cache 救不回时间", fontsize=10.0,
            color=DARK, weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.068, 0.272,
            "容量 175K → 194K，但解码\n"
            "3.85 → 3.86 ms，几乎没变。",
            fontsize=9.2, color=SLATE, ha="left", va="top", linespacing=1.75,
            zorder=6)
    ax.text(0.068, 0.196, "因为 conv-state 仍按遍存储。", fontsize=8.8,
            color=GRAY, ha="left", va="center", zorder=6)

    card(ax, 0.522, 0.168, 0.430, 0.168, LIGHT, face="white", lw=1.0)
    ax.text(0.542, 0.312, "对做批处理服务的人意味着什么", fontsize=10.0,
            color=DARK, weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.542, 0.272,
            "同样的卡，能同时装下的\n"
            "上下文少了将近一半；\n"
            "解码也慢了一倍多。",
            fontsize=9.2, color=SLATE, ha="left", va="top", linespacing=1.75,
            zorder=6)

    punchline(fig, "同一个模型：本地是优点，机房是开销。")
    footer(fig, "事实来源：vLLM 博客《Inkling 2 Mini on vLLM: Day-0 Support for a Looped Model》"
                "（2026-11-20）；2.55 倍按 3.85÷1.51 计算，50% 按 175÷352 计算，均为本文算术")
    fig.savefig(OUT + "图2_三笔开销.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """自报与第三方"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "只有两个数字来自第三方",
           "模型卡把评测分成两组，两组的可信度不一样")

    card(ax, 0.048, 0.400, 0.430, 0.360, TEAL, lw=1.6)
    ax.text(0.072, 0.716, "第三方独立指数", fontsize=11.0, color=TEAL,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.072, 0.660, "AA Index", fontsize=9.6, color=GRAY,
            ha="left", va="center", zorder=6)
    ax.text(0.072, 0.612, "20.1", fontsize=22, color=DARK,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.072, 0.535, "Vals Index v2.2", fontsize=9.6, color=GRAY,
            ha="left", va="center", zorder=6)
    ax.text(0.072, 0.487, "46.5%", fontsize=22, color=DARK,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.072, 0.428, "两家机构独立评测，可直接引用", fontsize=8.8,
            color=SLATE, ha="left", va="center", zorder=6)

    card(ax, 0.522, 0.400, 0.430, 0.360, RED, lw=1.6)
    ax.text(0.546, 0.716, "reported score（自报口径）", fontsize=11.0,
            color=RED, weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.546, 0.668,
            "DeepSWE v1.1\n"
            "SWE-bench Pro v2\n"
            "SWE-bench Verified\n"
            "BrowseComp\n"
            "Terminal Bench",
            fontsize=9.2, color=SLATE, ha="left", va="top", linespacing=1.72,
            zorder=6)
    ax.text(0.546, 0.428, "各实验室自报，评测环境不完全统一", fontsize=8.8,
            color=SLATE, ha="left", va="center", zorder=6)

    ax.text(0.048, 0.330,
            "TML 在公告里也写明：Evaluation setups vary by model.",
            fontsize=9.6, color=DARK, ha="left", va="center")
    ax.text(0.048, 0.286,
            "发布不到一周，社区复现还没做完——这些分数现在只能当参考。",
            fontsize=9.6, color=SLATE, ha="left", va="center")

    card(ax, 0.048, 0.150, 0.904, 0.078, LIGHT, face=PALE, lw=1.0)
    ax.text(0.070, 0.189,
            "同样的谨慎适用于 AA「便宜六倍」的说法：它按每个 Intelligence Index 任务算，"
            "不是每 token 单价，两者不能互换。",
            fontsize=9.2, color=DARK, ha="left", va="center", zorder=6)

    punchline(fig, "别拿自报分数做采购决定：等独立复现，或者自己跑一遍。")
    footer(fig, "事实来源：Inkling 2 Mini 模型卡（2026-11-20）评测表分组与表注；"
                "TML《Introducing Inkling 2 Mini》公告")
    fig.savefig(OUT + "图3_自报与第三方.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)


