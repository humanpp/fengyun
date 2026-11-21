# -*- coding: utf-8 -*-
"""
《264亿参数、20GB检查点，32GB Mac就能跑：这家公司用"循环层"反潮流，不堆参数了》配套图表

事实口径（全部核到官方发布、模型卡、第三方独立基准）：

一、发布与硬件
  · Thinking Machines Lab 于 2026-11-20 以 Apache 2.0 发布 Inkling 2 Mini，
    权重在 Hugging Face（thinkingmachines/Inkling-2-Mini）。据 TML 发布公告
    《Introducing Inkling 2 Mini》（2026-11-20）与模型卡。
  · 模型卡"Required hardware"：单个检查点约 20GB，混合 NVFP4 与 MXFP8；
    1× NVIDIA DGX Spark；Apple silicon 32GB 及以上（MacBook、Mac mini、Mac Studio）；
    其他平台建议 32GB 以上显存。
  · 公告原文场景：研究人员在一次航班上，用 MacBook Pro 离线运行它，
    几分钟内做出了一个可玩的飞行模拟器（演示机为 M5 Pro / 48GB，飞行模式）。

二、架构（模型卡第 2 节）
  · 多模态自回归 looped transformer；24 层 decoder-only + 稀疏 MoE 前馈；
    中间 12 层共享权重跑三遍 → 每 token 48 次层应用（6 + 3×12 + 6）。
  · 每层每 token 路由 8/128 个专家；注意力为局部层与全局层混合（20 局部 / 4 全局）。
  · 参数 26.4B，激活 3.4B。模型卡注：每多跑一遍循环层，约多 1.0B 等效激活参数；
    跑三遍即 5.4B 等效激活参数/token。
  · 上下文 100 万 token。原生多模态：图像经 23 层 ViT 编码。
  · vLLM 技术博客（2026-11-20）：24 层分 prelude（0–5）、loop core（6–17）、
    coda（18–23）；prelude 与 coda 各跑一次，core 跑三遍共享权重；
    每一遍有独立的 KV cache 与 conv-state cache，因此 24 层权重对应
    48 个 KV cache；后续每一遍每个核心子层各读一条 message，12 层 × 4 个输入
    = 每 token 每条后序遍读 48 条 message。
  · 思考（作者归纳，非官方表述）：若按"逻辑层"计，24 层权重换来 48 次层应用；
    循环替代的是存储更多权重，而不是替代参数总量。

三、能力与成本（第三方独立基准）
  · Artificial Analysis Intelligence Index v5.0.1：20.1；与 Qwen3.8-27B 同为 20.1；
    Gemma 4 31B 为 4.4；Muse Glimmer 为 6.3；Nemotron 3.5 Super VL 为 13.6。
  · AA 每 Intelligence Index 任务成本 0.59 美元、耗时 9.0 分钟；
    对照 Qwen3.8-27B 为 3.53 美元、38.2 分钟。价格为 TML 一方口径
    每百万 token 输入 0.15 美元、输出 0.50 美元、缓存命中 0.015 美元。
  · AA 流式输出速度约 280 token/秒。
  · TML 自述：在 DeepSWE v1.1 得 48.2%、Vals Index v2.2 得 46.5%，
    为 100B 以下全部开放权重模型之首；参数表标注该组数据为"自报"。
  · 官方明确指出循环的边界："While looping improves the model's reasoning,
    it doesn't enable its weights to store more facts—knowledge is mostly a
    function of total parameter count."研究版变循环模型上，
    长上下文基准（GraphWalks BFS、MRCR v2）随遍数提升，
    而知识型基准（AA-Omniscience、SimpleQA Verified 等）不随遍数提升。
  · 端到端实际花费并不等于低单价：Plotly 数据分析基准（2026-11-21）
    一次完整跑批 4.09 美元、179M token，高于更大的 Inkling 2 Small 的
    1.81 美元、22M token；原因是某一道题上跑了 585 次查询、约占全部
    工具调用的 46%，被其称为一次失控循环（runaway loop）。
    该基准得分 36/43。

风格：克制传媒风，白底、低饱和配色、标题即结论（沿用本工作区既有规范）
输出目录 = 脚本所在目录
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
BLUSH = "#fbf1ef"
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
    """24 层权重，48 次层应用"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "24 层权重，48 次层应用",
           "中间 12 层共享同一套权重跑三遍，每一遍各带自己的 KV cache")

    # ---------------- 左：24 个层方块
    n = 24
    x0 = 0.048
    total_w = 0.462
    gap = 0.0055
    bw = (total_w - (n - 1) * gap) / n

    base = 0.400
    bh = 0.130

    for i in range(n):
        x = x0 + i * (bw + gap)
        if 6 <= i < 18:
            face, edge = NAVY, NAVY
        else:
            face, edge = PALE, GRAY
        ax.add_patch(Rectangle((x, base), bw, bh,
                               facecolor=face, edgecolor=edge,
                               linewidth=0.9, zorder=4))

    # 数字序号
    for i in range(n):
        x = x0 + i * (bw + gap) + bw / 2
        ax.text(x, base - 0.026, str(i), fontsize=6.8, color=GRAY,
                ha="center", va="top", zorder=6)

    # 分组括号标注
    groups = [
        (0, 5, "前奏", "跑 1 次", GRAY),
        (6, 17, "循环核心", "共享权重跑 3 次", NAVY),
        (18, 23, "尾声", "跑 1 次", GRAY),
    ]
    for start, end, name, desc, color in groups:
        gx = x0 + start * (bw + gap)
        gw = (end - start) * (bw + gap)
        ax.plot([gx, gx + gw], [base + bh + 0.016] * 2, color=color,
                linewidth=1.4, zorder=5)
        ax.text(gx, base + bh + 0.032, name, fontsize=10.4, color=color,
                weight="bold", ha="left", va="bottom", zorder=6)
        ax.text(gx + gw, base + bh + 0.032, desc, fontsize=8.4, color=SLATE,
                ha="right", va="bottom", zorder=6)

    # ---------------- 左：三遍示意
    ax.text(0.048, 0.300, "循环核心的三遍", fontsize=9.8, color=GRAY,
            ha="left", va="center")
    ax.plot([0.048, 0.510], [0.278, 0.278], color=LIGHT, linewidth=1.0)

    passes = [
        ("第 1 遍", "从 prelude 输出开始", NAVY),
        ("第 2 遍", "读第 1 遍发出的 message", SLATE),
        ("第 3 遍", "读第 2 遍发出的 message", SLATE),
    ]
    y = 0.238
    for label, desc, color in passes:
        ax.add_patch(Rectangle((0.050, y - 0.013), 0.115, 0.026,
                               facecolor=color, edgecolor=color,
                               linewidth=0, alpha=0.88, zorder=4))
        ax.text(0.180, y, f"{label}　{desc}", fontsize=8.8,
                color=DARK, ha="left", va="center", zorder=6)
        y -= 0.050

    # ---------------- 右：四个数字
    stats = [
        ("26.4B", "总参数", NAVY, 0.580, 0.720),
        ("3.4B", "每 token 激活参数", DARK, 0.795, 0.720),
        ("5.4B", "含循环的等效激活参数", RED, 0.580, 0.548),
        ("48", "每 token 层应用次数", NAVY, 0.795, 0.548),
    ]
    for num, label, color, cx, cy in stats:
        ax.text(cx, cy, num, fontsize=24, color=color, weight="bold",
                ha="left", va="center")
        ax.text(cx, cy - 0.058, label, fontsize=8.8, color=GRAY,
                ha="left", va="center")

    ax.plot([0.580, 0.952], [0.462, 0.462], color=LIGHT, linewidth=1.0)

    ax.text(0.580, 0.424,
            "模型卡注：每多跑一遍循环层，约多 1.0B\n"
            "等效激活参数；跑三遍即 3.4B + 2×1.0B。",
            fontsize=9.2, color=SLATE, ha="left", va="top", linespacing=1.70)

    ax.text(0.580, 0.318,
            "循环核心每多跑一遍，每个核心子层\n"
            "（12 层 × 4 个输入）各读一条 message，\n"
            "即每 token 每遍读 48 条。",
            fontsize=9.2, color=SLATE, ha="left", va="top", linespacing=1.70)

    punchline(fig, "循环省下的是权重存储，不是参数总量。")
    footer(fig, "事实来源：TML《Introducing Inkling 2 Mini》与 Inkling 2 Mini 模型卡"
                "（2026-11-20）；vLLM 博客《Inkling 2 Mini on vLLM》（2026-11-20）")
    fig.savefig(OUT + "图1_24层48次.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """能力与账单分开看"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "同一档能力，四分之一的任务成本",
           "Artificial Analysis Intelligence Index v5.0.1，两者同为 20.1")

    models = [
        ("Qwen3.8-27B", 20.1, 3.53, 38.2, SLATE),
        ("Inkling 2 Mini", 20.1, 0.59, 9.0, RED),
    ]

    ax.text(0.052, 0.790, "分数与每个任务的开销", fontsize=10.0, color=GRAY,
            ha="left", va="center")
    ax.plot([0.052, 0.480], [0.762, 0.762], color=LIGHT, linewidth=1.0)

    y = 0.690
    for name, score, cost, mins, color in models:
        ax.text(0.052, y, name, fontsize=11.6, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(0.052, y - 0.044, f"指数 {score}", fontsize=9.4, color=GRAY,
                ha="left", va="center")
        ax.text(0.052, y - 0.084, f"{cost:.2f} 美元 / 任务", fontsize=12.6,
                color=color, weight="bold", ha="left", va="center")
        ax.text(0.052, y - 0.122, f"{mins:.1f} 分钟 / 任务", fontsize=9.0,
                color=SLATE, ha="left", va="center")
        y -= 0.240

    # 右：成本条形
    ax.text(0.560, 0.790, "每任务成本（美元）", fontsize=10.0, color=GRAY,
            ha="left", va="center")
    ax.plot([0.560, 0.950], [0.762, 0.762], color=LIGHT, linewidth=1.0)

    scale = 0.300 / 3.53
    yb = 0.660
    for name, score, cost, mins, color in models:
        ax.add_patch(Rectangle((0.560, yb - 0.024), cost * scale, 0.048,
                               facecolor=color, edgecolor=color,
                               linewidth=0, alpha=0.90, zorder=4))
        ax.text(0.560 + cost * scale + 0.012, yb, f"{cost:.2f}",
                fontsize=11.0, color=color, weight="bold",
                ha="left", va="center", zorder=6)
        yb -= 0.150

    ax.text(0.560, 0.400,
            "口径：TML 一方价格，每百万 token\n"
            "输入 0.15 美元、输出 0.50 美元、\n"
            "缓存命中 0.015 美元。\n"
            "流式输出约 280 token/秒。",
            fontsize=9.0, color=SLATE, ha="left", va="top", linespacing=1.75)

    # 下：边界
    card(ax, 0.052, 0.170, 0.898, 0.088, LIGHT, face=PALE, lw=1.0)
    ax.text(0.078, 0.214,
            "官方说明：循环提升的是推理，不能让权重存下更多事实——"
            "知识主要由参数总量决定。",
            fontsize=10.0, color=DARK, ha="left", va="center", zorder=6)

    punchline(fig, "分数持平，账单差四倍；但它省的不是每一道题。")
    footer(fig, "事实来源：Artificial Analysis Inkling 2 Mini 页面与发布说明（2026-11-20/21）；"
                "TML 发布公告与模型卡")
    fig.savefig(OUT + "图2_能力与账单.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """不是所有场景都需要大集群"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "它替代的是什么，不是参数而是机房",
           "同样一条要求：把 20GB 装进手边的机器")

    # 左：硬件门槛
    ax.text(0.052, 0.800, "官方列出的本地运行门槛", fontsize=10.0, color=GRAY,
            ha="left", va="center")
    ax.plot([0.052, 0.470], [0.772, 0.772], color=LIGHT, linewidth=1.0)

    rows = [
        ("检查点", "约 20GB，混合 NVFP4 / MXFP8", NAVY, True),
        ("Apple silicon", "32GB 及以上（MacBook / mini / Studio）", DARK, False),
        ("NVIDIA", "1× DGX Spark", DARK, False),
        ("其他平台", "建议 32GB 以上显存", DARK, False),
        ("上下文", "100 万 token", DARK, False),
    ]
    y = 0.706
    for label, value, color, big in rows:
        ax.text(0.052, y, label, fontsize=9.6, color=GRAY,
                ha="left", va="center")
        ax.text(0.052, y - 0.040, value,
                fontsize=15.0 if big else 10.4, color=color,
                weight="bold" if big else "normal",
                ha="left", va="center")
        y -= 0.104 if big else 0.086

    # 右：对照
    ax.text(0.560, 0.800, "同门对照", fontsize=10.0, color=GRAY,
            ha="left", va="center")
    ax.plot([0.560, 0.950], [0.772, 0.772], color=LIGHT, linewidth=1.0)

    card(ax, 0.560, 0.560, 0.390, 0.180, RED, lw=1.6)
    ax.text(0.582, 0.700, "Inkling 2 Mini", fontsize=12.0, color=RED,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.582, 0.652, "约 20GB，笔记本能跑", fontsize=9.6, color=DARK,
            ha="left", va="center", zorder=6)
    ax.text(0.582, 0.610, "AA 指数 20.1", fontsize=9.6, color=SLATE,
            ha="left", va="center", zorder=6)

    card(ax, 0.560, 0.340, 0.390, 0.180, SLATE, lw=1.2)
    ax.text(0.582, 0.480, "Inkling 2 Small", fontsize=12.0, color=SLATE,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.582, 0.432, "约 356GB 内存（4-bit 口径）", fontsize=9.6,
            color=DARK, ha="left", va="center", zorder=6)
    ax.text(0.582, 0.390, "要一整台机器，不是一台笔记本", fontsize=9.6,
            color=SLATE, ha="left", va="center", zorder=6)

    ax.text(0.560, 0.290,
            "参数只差一个量级，门槛差一个数量级。",
            fontsize=9.2, color=SLATE, ha="left", va="top")

    # 底部：落地场景
    card(ax, 0.052, 0.150, 0.898, 0.075, LIGHT, face=PALE, lw=1.0)
    ax.text(0.078, 0.188,
            "官方给的场景：研究人员在航班上，用 MacBook Pro 离线运行它，"
            "几分钟内做出一个可玩的飞行模拟器。",
            fontsize=9.6, color=DARK, ha="left", va="center", zorder=6)

    punchline(fig, "省下的不是电费，是「这件事得先有机房」那个前提。")
    footer(fig, "事实来源：Inkling 2 Mini 模型卡「Required hardware」；TML 发布公告；"
                "Plotly 数据分析基准（2026-11-21，Inkling 2 Small 内存口径）")
    fig.savefig(OUT + "图3_本地门槛.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)
