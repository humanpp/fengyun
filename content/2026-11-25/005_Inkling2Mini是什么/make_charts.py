# -*- coding: utf-8 -*-
"""
《24 层权重、48 次层应用、20GB 检查点：Inkling 2 Mini 到底是个什么东西》配套图表

事实口径（全部核到官方发布、模型卡、推理框架技术博客）：

一、发布
  · Thinking Machines Lab 于 2026-11-20 以 Apache 2.0 发布 Inkling 2 Mini，
    权重在 Hugging Face（thinkingmachines/Inkling-2-Mini）。

二、架构（模型卡第 2 节 + vLLM 博客）
  · 24 层 decoder-only 稀疏 MoE，中间 12 层共享权重跑三遍
    → 每 token 48 次层应用（6 + 3×12 + 6）。
  · vLLM：prelude（层 0–5）、loop core（层 6–17）、coda（层 18–23）；
    prelude 与 coda 各跑一次，core 跑三遍，coda 从最后一遍继续。
  · 三遍全部从同一前奏输出出发，第 p+1 遍只通过 message 看到第 p 遍。
  · 每核心层每遍各有 KV cache 与 conv-state cache → 24 层对应 48 个 KV cache。
  · 每层每 token 路由 8/128 专家；20 层滑动窗口 + 4 层全注意力；图像经 23 层 ViT。

三、三个参数口径
  · 总参数 26.4B；激活 3.4B；含循环的等效激活 5.4B
    （模型卡注：每多一遍约增 1.0B，三遍即 3.4 + 2×1.0）。

四、vLLM 在单卡 GB200 的实测（TP1，4K 上下文，仅前向）
  · 1 遍：1.51 ms（batch 1）/ 3.81 ms（batch 32）/ KV cache 352K token
  · 2 遍：2.67 / 5.92 / 233K
  · 3 遍：3.85 / 8.11 / 175K
  · 3 遍共享 KV cache：3.86 / 8.10 / 194K

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
    """24 层权重，48 次层应用"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "24 层权重，48 次层应用",
           "中间 12 层共享同一套权重跑三遍；24 层，48 个 KV cache")

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
        ax.text(x + bw / 2, base - 0.026, str(i), fontsize=6.8, color=GRAY,
                ha="center", va="top", zorder=6)

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

    ax.text(0.048, 0.300, "三遍都从同一个前奏输出出发，不串接", fontsize=9.8,
            color=GRAY, ha="left", va="center")
    ax.plot([0.048, 0.510], [0.278, 0.278], color=LIGHT, linewidth=1.0)

    passes = [
        ("第 1 遍", "从前奏输出开始", NAVY),
        ("第 2 遍", "读第 1 遍的 48 条 message", SLATE),
        ("第 3 遍", "读第 2 遍的 48 条 message", SLATE),
    ]
    y = 0.238
    for label, desc, color in passes:
        ax.add_patch(Rectangle((0.050, y - 0.013), 0.115, 0.026,
                               facecolor=color, edgecolor=color,
                               linewidth=0, alpha=0.88, zorder=4))
        ax.text(0.180, y, f"{label}　{desc}", fontsize=8.8,
                color=DARK, ha="left", va="center", zorder=6)
        y -= 0.050

    stats = [
        ("26.4B", "总参数", NAVY, 0.580, 0.720),
        ("3.4B", "每 token 激活参数", DARK, 0.795, 0.720),
        ("5.4B", "含循环的等效激活", RED, 0.580, 0.548),
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

    ax.text(0.580, 0.300,
            "从第 2 遍起，每个核心子层输入（attention\n"
            "的 q/k/v 与 MLP，共 4 个）各读一条 message，\n"
            "12 层 × 4 = 每 token 每遍 48 条。",
            fontsize=9.2, color=SLATE, ha="left", va="top", linespacing=1.70)

    punchline(fig, "省下的是权重存储，花出去的是每 token 的层应用。")
    footer(fig, "事实来源：Inkling 2 Mini 模型卡（2026-11-20，architecture / parameters）；"
                "vLLM 博客《Inkling 2 Mini on vLLM: Day-0 Support for a Looped Model》（2026-11-20）")
    fig.savefig(OUT + "图1_24层48次.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """24 层权重，48 份缓存"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "24 层权重，48 份缓存",
           "每一遍都有自己的 KV cache 和 conv-state cache（vLLM，2026-11-20）")

    ax.text(0.048, 0.800, "每核心层每遍一份缓存", fontsize=10.0, color=GRAY,
            ha="left", va="center")
    ax.plot([0.048, 0.420], [0.772, 0.772], color=LIGHT, linewidth=1.0)

    rows = [
        ("24", "层权重", NAVY),
        ("48", "KV cache", RED),
        ("48", "conv-state cache", RED),
    ]
    y = 0.660
    for num, label, color in rows:
        ax.text(0.048, y, num, fontsize=30, color=color, weight="bold",
                ha="left", va="center")
        ax.text(0.170, y, label, fontsize=11.0, color=DARK,
                ha="left", va="center")
        y -= 0.145

    ax.text(0.048, 0.190,
            "第 p 遍只 attend 第 p 遍自己算出的\n"
            "key 与 value，所以缓存按遍数翻倍。",
            fontsize=9.4, color=SLATE, ha="left", va="top", linespacing=1.75)

    # 右：GB200 实测
    ax.text(0.520, 0.800, "GB200 单卡实测：遍数越多，解码越慢、容量越小",
            fontsize=10.0, color=GRAY, ha="left", va="center")
    ax.plot([0.520, 0.952], [0.772, 0.772], color=LIGHT, linewidth=1.0)

    rows2 = [
        ("1 遍", 1.51, 352, GRAY),
        ("2 遍", 2.67, 233, SLATE),
        ("3 遍", 3.85, 175, RED),
        ("3 遍·共享", 3.86, 194, TEAL),
    ]
    maxms = 3.86
    yb = 0.700
    for label, ms, kv, color in rows2:
        ax.text(0.520, yb, label, fontsize=9.6, color=DARK,
                ha="left", va="center")
        w = 0.150 * (ms / maxms)
        ax.add_patch(Rectangle((0.618, yb - 0.016), w, 0.032,
                               facecolor=color, edgecolor=color,
                               linewidth=0, alpha=0.90, zorder=4))
        ax.text(0.618 + w + 0.008, yb, f"{ms:.2f}", fontsize=9.0,
                color=color, weight="bold", ha="left", va="center", zorder=6)
        ax.text(0.952, yb, f"{kv}K", fontsize=9.0, color=SLATE,
                ha="right", va="center")
        yb -= 0.078

    ax.text(0.520, 0.756,
            "左列为解码一步毫秒（batch=1），右列为 KV 容量（token）",
            fontsize=8.6, color=GRAY, ha="left", va="center")

    ax.text(0.520, 0.420,
            "解码一步耗时为 batch=1、4K 上下文。\n"
            "共享 KV cache 把容量从 175K 拉回 194K，\n"
            "但解码时间几乎没变（3.86 对 3.85 ms）——\n"
            "因为 conv-state 仍按遍存储。",
            fontsize=9.0, color=SLATE, ha="left", va="top", linespacing=1.75)

    punchline(fig, "省下的是权重，翻倍的是缓存；共享缓存救不回时间。")
    footer(fig, "事实来源：vLLM 博客（2026-11-20），单张 GB200、TP1、4K 上下文、仅前向；"
                "模型卡（48 个 KV cache 与 conv-state cache 的结构见同博客 The Loop 一节）")
    fig.savefig(OUT + "图2_48份缓存.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """它是什么：一张规格卡"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "它是什么：九个字段说全",
           "2026-11-20 发布，Apache 2.0，权重在 Hugging Face")

    specs = [
        ("发布方", "Thinking Machines Lab, Inc."),
        ("架构", "24 层 decoder-only 稀疏 MoE，中间 12 层跑三遍"),
        ("参数", "26.4B 总 / 3.4B 激活 / 5.4B 等效激活"),
        ("专家", "每层每 token 路由 8/128"),
        ("注意力", "局部与全局混合（20 滑动窗口 + 4 全注意力）"),
        ("上下文", "100 万 token"),
        ("数值格式", "多数 NVFP4，最后四层 MXFP8，检查点约 20GB"),
        ("本地门槛", "1× DGX Spark；Apple silicon 32GB 及以上"),
        ("输入输出", "文本＋图像进，文本出（图像经 23 层 ViT）"),
    ]

    y = 0.792
    for i, (k, v) in enumerate(specs):
        if i % 2 == 0:
            card(ax, 0.048, y - 0.026, 0.904, 0.052, LIGHT, face=PALE, lw=0.8)
        ax.text(0.072, y, k, fontsize=9.6, color=GRAY, ha="left", va="center")
        ax.text(0.212, y, v, fontsize=10.4, color=DARK, weight="bold",
                ha="left", va="center", zorder=6)
        y -= 0.062

    card(ax, 0.048, 0.128, 0.904, 0.075, TEAL, face="white", lw=1.2)
    ax.text(0.072, 0.166,
            "官方场景：研究人员带它上飞机，飞行模式下用 MacBook Pro"
            "（M5 Pro / 48GB）离线跑，几分钟做出可玩的飞行模拟器。",
            fontsize=9.4, color=DARK, ha="left", va="center", zorder=6)

    punchline(fig, "它不是把大模型压缩了，是把存储省下来、把计算花出去。")
    footer(fig, "事实来源：Inkling 2 Mini 模型卡（2026-11-20）第 1–3 节；"
                "TML《Introducing Inkling 2 Mini》发布公告（2026-11-20）")
    fig.savefig(OUT + "图3_规格卡.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)
