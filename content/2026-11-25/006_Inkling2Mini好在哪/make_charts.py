# -*- coding: utf-8 -*-
"""
《同分、六分之一价格、四倍速度：Inkling 2 Mini 真正值钱的地方在哪》配套图表

事实口径：

一、同分不同价（第三方独立指数）
  · Artificial Analysis Intelligence Index v5.0：Inkling 2 Mini 20.1，
    Qwen3.8-27B 20.1；每 Intelligence Index 任务 0.59 美元 / 9.0 分钟
    对 3.53 美元 / 38.2 分钟；AA 表述为约便宜六倍、约快四倍，
    算力约为对手三分之一（2.8 倍更少）。

二、编程与视觉（模型卡 reported score，非第三方独立复现）
  · DeepSWE v1.1：48.2%（Qwen3.8-27B 42.2%、Beam 1.0 44.4%、Gemma 4 31B 0.3%）
  · SWE-bench Pro v2 Hard：77.9%（Qwen 73.8%、Beam 77.2%）
  · SWE-bench Verified：79.2%
  · Terminal Bench v2.1：71.6%
  · OmniDocBench v1.6：92.8%（同表最高）

三、能效与本地吞吐（旁证，未独立复现）
  · 斯坦福 intelligence-per-joule 基准（arXiv 2511.07885），DGX Spark：
    Inkling 2 Mini 0.703；Qwen3.6-35B-A3B 0.430；Gemma-4-26B-A4B 0.159
  · Exo Labs：96GB M5 Ultra Mac Studio 解码 210 token/秒、prefill 3620 token/秒

四、本地门槛与生态
  · 单检查点约 20GB；1× DGX Spark；Apple silicon 32GB 及以上
  · 前 20 层原生 NVFP4、最后四层 MXFP8（VentureBeat 转述 TML）
  · Day-0：vLLM（Blackwell/Hopper/DGX Spark）、Ollama、Exo、SGLang、
    Unsloth、llama.cpp、Dynamo、Tokenspeed；Unsloth 称 GGUF 版 16GB 可跑

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
    """同分，不同价"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "分一样，账单差六倍",
           "Artificial Analysis Intelligence Index v5.0：两者同为 20.1")

    models = [
        ("Inkling 2 Mini", 0.59, 9.0, RED),
        ("Qwen3.8-27B", 3.53, 38.2, SLATE),
    ]

    # 左：分数
    ax.text(0.052, 0.792, "指数得分", fontsize=10.0, color=GRAY,
            ha="left", va="center")
    ax.plot([0.052, 0.310], [0.762, 0.762], color=LIGHT, linewidth=1.0)

    y = 0.690
    for name, cost, mins, color in models:
        ax.text(0.052, y, name, fontsize=11.0, color=DARK, weight="bold",
                ha="left", va="center")
        ax.text(0.052, y - 0.062, "20.1", fontsize=30, color=color,
                weight="bold", ha="left", va="center")
        y -= 0.215

    ax.text(0.052, 0.215, "同分。差别不在分数上。", fontsize=9.6,
            color=SLATE, ha="left", va="center")

    # 右：成本与耗时
    ax.text(0.420, 0.792, "每个 Intelligence Index 任务的开销",
            fontsize=10.0, color=GRAY, ha="left", va="center")
    ax.plot([0.420, 0.952], [0.762, 0.762], color=LIGHT, linewidth=1.0)

    ax.text(0.420, 0.722, "成本（美元）", fontsize=9.0, color=GRAY,
            ha="left", va="center")
    sc = 0.130 / 3.53
    yb = 0.652
    for name, cost, mins, color in models:
        ax.add_patch(Rectangle((0.560, yb - 0.020), cost * sc, 0.040,
                               facecolor=color, edgecolor=color,
                               linewidth=0, alpha=0.90, zorder=4))
        ax.text(0.560 + cost * sc + 0.010, yb, f"{cost:.2f}", fontsize=11.0,
                color=color, weight="bold", ha="left", va="center", zorder=6)
        yb -= 0.072

    ax.text(0.420, 0.520, "耗时（分钟）", fontsize=9.0, color=GRAY,
            ha="left", va="center")
    sm = 0.130 / 38.2
    yb = 0.450
    for name, cost, mins, color in models:
        ax.add_patch(Rectangle((0.560, yb - 0.020), mins * sm, 0.040,
                               facecolor=color, edgecolor=color,
                               linewidth=0, alpha=0.55, zorder=4))
        ax.text(0.560 + mins * sm + 0.010, yb, f"{mins:.1f}", fontsize=11.0,
                color=color, weight="bold", ha="left", va="center", zorder=6)
        yb -= 0.072

    card(ax, 0.420, 0.235, 0.532, 0.080, LIGHT, face=PALE, lw=1.0)
    ax.text(0.442, 0.275,
            "AA 表述：约便宜六倍、约快四倍；算力约为对手三分之一（2.8 倍更少）。",
            fontsize=9.4, color=DARK, ha="left", va="center", zorder=6)

    punchline(fig, "同分不是优点；同分还便宜六倍，才是。")
    footer(fig, "事实来源：Artificial Analysis Intelligence Index v5.0 与官方 X 帖"
                "（2026-11-20/21，x.com/ArtificialAnlys/status/2123877878568001635）")
    fig.savefig(OUT + "图1_同分不同价.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """能效与编程"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "同尺寸里最能打的两块：编程与能效",
           "左为模型卡 reported score，右为斯坦福 intelligence-per-joule（DGX Spark）")

    ax.text(0.048, 0.800, "智能体编程（百分制，越高越好）", fontsize=10.0,
            color=GRAY, ha="left", va="center")
    ax.plot([0.048, 0.470], [0.772, 0.772], color=LIGHT, linewidth=1.0)

    rows = [
        ("DeepSWE v1.1", 48.2, RED),
        ("SWE-bench Pro v2 Hard", 77.9, NAVY),
        ("SWE-bench Verified", 79.2, NAVY),
        ("Terminal Bench v2.1", 71.6, NAVY),
    ]
    y = 0.700
    for label, val, color in rows:
        ax.text(0.048, y, label, fontsize=9.6, color=DARK,
                ha="left", va="center")
        ax.add_patch(Rectangle((0.048, y - 0.038), 0.360 * val / 100.0, 0.024,
                               facecolor=color, edgecolor=color,
                               linewidth=0, alpha=0.88, zorder=4))
        ax.text(0.048 + 0.360 * val / 100.0 + 0.008, y - 0.026, f"{val}%",
                fontsize=9.4, color=color, weight="bold",
                ha="left", va="center", zorder=6)
        y -= 0.088

    ax.text(0.048, 0.300,
            "同表对照：DeepSWE 上 Qwen3.8-27B 为 42.2%、\n"
            "Beam 1.0 为 44.4%、Gemma 4 31B 为 0.3%。",
            fontsize=9.0, color=SLATE, ha="left", va="top", linespacing=1.75)

    # 右：每焦耳智能
    ax.text(0.540, 0.800, "每焦耳智能（DGX Spark）", fontsize=10.0,
            color=GRAY, ha="left", va="center")
    ax.plot([0.540, 0.952], [0.772, 0.772], color=LIGHT, linewidth=1.0)

    rows2 = [
        ("Inkling 2 Mini", 0.703, RED),
        ("Qwen3.6-35B-A3B", 0.430, SLATE),
        ("Gemma-4-26B-A4B", 0.159, GRAY),
    ]
    y = 0.690
    for label, val, color in rows2:
        ax.text(0.540, y, label, fontsize=9.6, color=DARK,
                ha="left", va="center")
        ax.add_patch(Rectangle((0.540, y - 0.040), 0.340 * val / 0.703, 0.026,
                               facecolor=color, edgecolor=color,
                               linewidth=0, alpha=0.88, zorder=4))
        ax.text(0.540 + 0.340 * val / 0.703 + 0.008, y - 0.027, f"{val:.3f}",
                fontsize=9.4, color=color, weight="bold",
                ha="left", va="center", zorder=6)
        y -= 0.098

    ax.text(0.540, 0.330,
            "本地吞吐旁证：Exo Labs 在 96GB M5 Ultra\n"
            "Mac Studio 上测得解码 210 token/秒、\n"
            "prefill 3620 token/秒。",
            fontsize=9.0, color=SLATE, ha="left", va="top", linespacing=1.75)

    card(ax, 0.048, 0.150, 0.904, 0.080, LIGHT, face=PALE, lw=1.0)
    ax.text(0.070, 0.190,
            "模型卡中 DeepSWE、SWE-bench、Terminal Bench 等行标注 reported score，"
            "属自报口径、评测环境不完全统一，尚未独立复现。",
            fontsize=9.2, color=DARK, ha="left", va="center", zorder=6)

    punchline(fig, "编程是它最能打的赛道，也是争议最大的一组数字。")
    footer(fig, "事实来源：Inkling 2 Mini 模型卡（2026-11-20）；斯坦福 intelligence-per-joule"
                "（arXiv 2511.07885，DGX Spark）；Exo Labs（2026-11-20 前后）")
    fig.savefig(OUT + "图2_能效与编程.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """从 20GB 到 16GB"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "从 20GB 到 16GB：门槛是一层层降下来的",
           "官方检查点与各运行时的落地形态")

    # 台阶
    steps = [
        ("原生检查点", "约 20GB", "NVFP4 + MXFP8", NAVY, 0.075),
        ("DGX Spark", "1× 起", "NVIDIA 官方支持", SLATE, 0.265),
        ("Apple silicon", "32GB 起", "Ollama / Exo Labs", TEAL, 0.455),
        ("GGUF 量化", "16GB 起", "Unsloth / llama.cpp", RED, 0.645),
    ]
    for label, big, desc, color, x in steps:
        card(ax, x, 0.380, 0.170, 0.300, color, lw=1.4)
        ax.text(x + 0.015, 0.640, label, fontsize=9.0, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(x + 0.015, 0.560, big, fontsize=21, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(x + 0.015, 0.480, desc, fontsize=8.4, color=SLATE,
                ha="left", va="center", zorder=6)
        ax.text(x + 0.015, 0.425, "官方/厂商口径", fontsize=7.8, color=GRAY,
                ha="left", va="center", zorder=6)

    ax.annotate("", xy=(0.952, 0.330), xytext=(0.075, 0.330),
                arrowprops=dict(arrowstyle="->", color=GRAY, lw=1.2))
    ax.text(0.075, 0.300, "门槛一路往下", fontsize=9.0, color=GRAY,
            ha="left", va="center")
    ax.text(0.952, 0.300, "能跑的机器越来越多", fontsize=9.0, color=GRAY,
            ha="right", va="center")

    ax.text(0.048, 0.240,
            "关键在于「原生」两个字：权重发布的数值格式就是训练时的格式，"
            "不需要事后再量化一遍。",
            fontsize=9.6, color=DARK, ha="left", va="center")
    ax.text(0.048, 0.196,
            "前 20 层按 4-bit NVFP4 训练和部署，最后四层 MXFP8。",
            fontsize=9.2, color=SLATE, ha="left", va="center")

    punchline(fig, "一个模型的真实门槛，往往不是权重多大，是第一天有没有人能跑起来。")
    footer(fig, "事实来源：Inkling 2 Mini 模型卡「Required hardware / Required software」；"
                "VentureBeat（2026-11-21）转述 TML 的 NVFP4/MXFP8 训练部署方式；"
                "Unsloth 称 GGUF 量化版 16GB 内存可跑")
    fig.savefig(OUT + "图3_从20GB到16GB.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)
