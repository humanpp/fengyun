# -*- coding: utf-8 -*-
"""
《12GB 显存跑 125B：PolyStrata 的三层账本》配套图表

事实口径：
  · Qwen3.8-Flash-Next：125B 参数，24,576 个专家，每 token 用 10 个；
    2-bit 文件 39GB；3-bit 文件 55GB（官方文档）。
  · Q2_0 档内存 + 显存需求约 37.6GB，IQ2_XS 约 39.2GB；下载 66–76GB；
    建议留 80GB 磁盘（PolyStrata docs/MODELS.md，经 Mycelium Protocol 整理）。
  · 社区记录（RTX 3060 12GB / i7-12700 / 64GB / IQ2_XS / Strata 0.1.41）：
    4K 45.5 tok/s、首字约 5.0s；32K 40.8、约 35.4s；128K 37.6、约 143.6s。
  · 官方规划档 12GB+32GB（模拟硬件）：21.3 tok/s，首字约 3 分钟。
  · 无 PolyStrata 时整模需 H100 80GB。

输出目录 = 脚本所在目录
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei"]
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
Y_PUNCH = 0.068
Y_FOOT = 0.020


def header(fig, title, sub):
    fig.text(0.045, Y_TITLE, title, fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, Y_SUB, sub, fontsize=10.4, color=GRAY,
             ha="left", va="top")


def footer(fig, text):
    fig.text(0.045, Y_FOOT, text, fontsize=7.6, color=GRAY,
             ha="left", va="bottom")


def punchline(fig, text):
    fig.text(0.045, Y_PUNCH, text, fontsize=10.4, color=DARK,
             ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


def card(ax, x, y, w, h, edge, face="white", lw=1.2, z=2):
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
    """39GB 文件 vs 12GB 显存，以及三层分工"""
    fig = plt.figure(figsize=(12, 6.9))

    header(fig, "39GB 的账，分三层记",
           "2-bit 模型文件 39GB，RTX 3060 只有 12GB 显存")

    axb = fig.add_axes([0.215, 0.555, 0.720, 0.235])
    axb.set_xlim(0, 42)
    axb.set_ylim(-0.7, 1.7)
    axb.barh([1.0], [39.0], height=0.40, color=NAVY, zorder=3)
    axb.barh([0.0], [12.0], height=0.40, color=RED, zorder=3)
    axb.text(39.5, 1.0, "39 GB", fontsize=10.6, color=NAVY,
             weight="bold", ha="left", va="center")
    axb.text(12.5, 0.0, "12 GB", fontsize=10.6, color=RED,
             weight="bold", ha="left", va="center")
    axb.set_yticks([1.0, 0.0])
    axb.set_yticklabels(["125B 2-bit 文件", "3060 显存"], fontsize=9.8,
                        color=SLATE)
    axb.tick_params(axis="y", length=0, pad=6)
    axb.set_xticks([])
    for spine in axb.spines.values():
        spine.set_visible(False)

    ax = new_axes(fig)
    tiers = [
        ("显存 12 GB", "热专家 + KV 缓存", "只放最忙的那一撮", NAVY),
        ("内存 64 GB", "其余专家常驻", "CPU 从内存直接算", TEAL),
        ("硬盘 ~80 GB", "权重 39 GB\n＋ n-gram 表 28.8 GB", "冷数据与查找表", GRAY),
    ]
    w, gap = 0.292, 0.022
    x = 0.045
    for name, sub, note, color in tiers:
        card(ax, x, 0.180, w, 0.270, color, lw=1.4)
        ax.text(x + 0.020, 0.405, name, fontsize=11.6, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(x + 0.020, 0.345, sub, fontsize=9.0, color=DARK,
                ha="left", va="top", linespacing=1.7, zorder=6)
        ax.text(x + 0.020, 0.235, note, fontsize=8.4, color=GRAY,
                ha="left", va="top", zorder=6)
        x += w + gap

    punchline(fig, "显卡只负责它算得动的那部分。")
    footer(fig, "事实来源：PolyStrata README 与 docs/MODELS.md（39GB/37.6GB/28.8GB/80GB）；docs.heylinger.com")
    fig.savefig(OUT + "图1_三层账本.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """上下文越长：解码几乎不变，首字越来越久"""
    fig = plt.figure(figsize=(12, 6.9))

    header(fig, "上下文越长，首字等得越久",
           "同一张 3060：生成速度只掉 17%，首字时间翻了近 30 倍")

    labels = ["4K", "32K", "128K"]
    xs = [0, 1, 2]
    decode = [45.5, 40.8, 37.6]
    ttft = [5.0, 35.4, 143.6]

    ax1 = fig.add_axes([0.075, 0.335, 0.380, 0.395])
    ax2 = fig.add_axes([0.555, 0.335, 0.380, 0.395])

    for ax, vals, title, top, color in [
        (ax1, decode, "解码  tok/s", 56, NAVY),
        (ax2, ttft, "首字等待  秒", 170, RED),
    ]:
        bars = ax.bar(xs, vals, width=0.52, color=color, zorder=3)
        ax.set_xticks(xs)
        ax.set_xticklabels(labels, fontsize=10.0, color=SLATE)
        ax.set_ylim(0, top)
        ax.set_title(title, fontsize=10.6, color=SLATE, pad=10)
        ax.tick_params(axis="y", labelsize=8.2, colors=GRAY)
        ax.grid(axis="y", color=LIGHT, linewidth=0.8, alpha=0.7, zorder=0)
        for spine in ("top", "right"):
            ax.spines[spine].set_visible(False)
        for spine in ("left", "bottom"):
            ax.spines[spine].set_color(LIGHT)
        for b, v in zip(bars, vals):
            ax.text(b.get_x() + b.get_width() / 2, v + top * 0.02,
                    ("%.1f" % v), fontsize=9.4, color=DARK,
                    ha="center", va="bottom")

    fig.text(0.075, 0.262,
             "社区记录：RTX 3060 12GB · i7-12700 · 64GB 内存 · IQ2_XS · Strata 0.1.41（Windows）",
             fontsize=8.4, color=GRAY, ha="left", va="center")
    fig.text(0.075, 0.222,
             "官方规划档 12GB+32GB（模拟硬件）：21.3 tok/s，首字约 3 分钟。",
             fontsize=8.4, color=GRAY, ha="left", va="center")

    punchline(fig, "能读完整份文档，就是得先等两分多钟。")
    footer(fig, "事实来源：PolyStrata bench/results/2026-10-09-community-rtx-3060-0141；docs.heylinger.com Benchmarks")
    fig.savefig(OUT + "图2_上下文与首字.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """一套引擎，两条路线"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "一套引擎，两条路线",
           "Qwen3.8-Flash-Next 走 Strata 原引擎，其余模型走另写的 strata-poly")

    card(ax, 0.045, 0.545, 0.600, 0.215, NAVY, lw=1.5)
    ax.text(0.068, 0.690, "Strata 引擎（沿用）", fontsize=12.4, color=NAVY,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.068, 0.612, "Qwen3.8-Flash-Next · 125B · 24,576 个专家",
            fontsize=10.2, color=DARK, ha="left", va="center", zorder=6)
    ax.text(0.068, 0.570, "每 token 只用其中 10 个", fontsize=8.8,
            color=GRAY, ha="left", va="center", zorder=6)

    card(ax, 0.045, 0.300, 0.600, 0.215, SLATE, lw=1.5)
    ax.text(0.068, 0.445, "strata-poly（为 PolyStrata 另写）", fontsize=12.4,
            color=SLATE, weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.068, 0.367, "GLM 5.3 Flash、DeepSeek V4 Flash、Qwen3.6、",
            fontsize=10.2, color=DARK, ha="left", va="center", zorder=6)
    ax.text(0.068, 0.322, "Gemma 4 等 11 个模型 · 官方仍标实验性", fontsize=10.2,
            color=DARK, ha="left", va="center", zorder=6)

    card(ax, 0.680, 0.300, 0.275, 0.460, LIGHT, face=PALE, lw=1.2)
    ax.text(0.705, 0.690, "仓库", fontsize=9.0, color=GRAY,
            ha="left", va="center", zorder=6)
    ax.text(0.705, 0.640, "C++ · MIT", fontsize=13.0, color=DARK,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.705, 0.560, "2026-10-06 建仓", fontsize=9.4, color=SLATE,
            ha="left", va="center", zorder=6)
    ax.text(0.705, 0.500, "1,380 ★ · 185 fork", fontsize=9.4, color=SLATE,
            ha="left", va="center", zorder=6)
    ax.text(0.705, 0.420, "作者 VecSzn，18 岁", fontsize=10.2, color=DARK,
            ha="left", va="center", zorder=6)
    ax.text(0.705, 0.360, "在读计算机科学学生", fontsize=8.6, color=GRAY,
            ha="left", va="center", zorder=6)

    ax.text(0.045, 0.205,
            "一键安装（Windows / Linux）　·　localhost 暴露 OpenAI / Anthropic API"
            "　·　8GB 笔记本读提示比 llama.cpp 快 2.7–3.5 倍",
            fontsize=9.0, color=SLATE, ha="left", va="center")

    punchline(fig, "分层不是新发明，把它改到能装下才是活。")
    footer(fig, "事实来源：GitHub simplexai-labs/PolyStrata（2026-11-23）；36氪 2026-11-21；量子位 2026-11-20")
    fig.savefig(OUT + "图3_两条路线.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)
