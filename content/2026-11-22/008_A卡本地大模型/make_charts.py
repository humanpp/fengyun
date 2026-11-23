# -*- coding: utf-8 -*-
"""
《A 卡的本地大模型，终于有人认真做了》配套图表

事实口径（核到项目 README 与 moe4all.com）：
  · MoE4All：Rust、Apache-2.0、Vulkan 后端、分页 MoE；支持 AMD/NVIDIA/Intel；
    Windows 免安装包约 20 MB；OpenAI 兼容 API；并发实测到四路。
  · 官方实测：RX 7900 XTX 24GB、Ryzen 5 5600X、64GB DDR4、Windows 11、
    Q8 KV；Qwen3.6 35B（约 5.91 bpw）6K 单路 154.6 tok/s、四路 248.3，
    150K 单路 65.1 tok/s。

输出目录 = 脚本所在目录
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

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
    """过去 vs 现在"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "A 卡缺的不是算力，是路径",
           "同一张卡，两种走法")

    card(ax, 0.045, 0.300, 0.430, 0.380, GRAY, lw=1.4)
    ax.text(0.068, 0.625, "过去", fontsize=15.0, color=GRAY, weight="bold",
            ha="left", va="center", zorder=6)
    ax.text(0.068, 0.565,
            "通用后端\n能跑，但慢\n生态围着 CUDA 转",
            fontsize=11.0, color=DARK, ha="left", va="top",
            linespacing=1.9, zorder=6)

    card(ax, 0.520, 0.300, 0.430, 0.380, RED, lw=1.5)
    ax.text(0.543, 0.625, "现在", fontsize=15.0, color=RED, weight="bold",
            ha="left", va="center", zorder=6)
    ax.text(0.543, 0.565,
            "Vulkan + 分页 MoE\n6K 单路 154.6 tok/s\n150K 单路 65.1 tok/s\n"
            "免安装 · OpenAI API",
            fontsize=10.4, color=DARK, ha="left", va="top",
            linespacing=1.75, zorder=6)

    ax.text(0.045, 0.235,
            "绕开 CUDA，也绕开 ROCm 的版本地狱。",
            fontsize=9.6, color=SLATE, ha="left", va="center")

    punchline(fig, "同一张 24GB 的卡，换条路，结果不一样。")
    footer(fig, "事实来源：MoE4All README（2026-11）；moe4all.com；GitHub Headmaster218/MoE4All")
    fig.savefig(OUT + "图1_从慢到能用.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """三方定位"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "三个工具，三种场景",
           "不是替代关系，是分工")

    cols = [
        ("MoE4All", NAVY,
         ["A 卡 / 超显存", "长上下文", "部署简单"],
         ["带宽敏感", "低并发", "生态年轻"]),
        ("llama.cpp / Ollama", TEAL,
         ["生态最广", "硬件最全", "上手快"],
         ["超长上下文吃显存", "大模型易 OOM"]),
        ("vLLM", RED,
         ["高并发", "服务端部署", "调度成熟"],
         ["部署重", "消费卡不友好"]),
    ]

    w, gap = 0.292, 0.020
    x = 0.045
    for name, color, pros, cons in cols:
        card(ax, x, 0.285, w, 0.395, color, lw=1.4)
        ax.text(x + 0.018, 0.630, name, fontsize=11.6, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(x + 0.018, 0.570, "强项", fontsize=8.4, color=GRAY,
                weight="bold", ha="left", va="center", zorder=6)
        yy = 0.535
        for p in pros:
            ax.text(x + 0.018, yy, p, fontsize=8.8, color=DARK,
                    ha="left", va="center", zorder=6)
            yy -= 0.032
        ax.text(x + 0.018, 0.425, "短板", fontsize=8.4, color=GRAY,
                weight="bold", ha="left", va="center", zorder=6)
        yy = 0.390
        for c in cons:
            ax.text(x + 0.018, yy, c, fontsize=8.6, color=SLATE,
                    ha="left", va="center", zorder=6)
            yy -= 0.032
        x += w + gap

    ax.text(0.045, 0.225,
            "挑工具，先看你的场景：单卡、长上下文，还是多人在线。",
            fontsize=9.0, color=SLATE, ha="left", va="center")

    punchline(fig, "选工具，先看场景，不看星数。")
    footer(fig, "事实来源：MoE4All README；llama.cpp / Ollama / vLLM 的定位为一般性概括")
    fig.savefig(OUT + "图2_三方定位.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """长板与短板"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "长板很长，短板也明显",
           "MoE4All 的能力画像")

    card(ax, 0.045, 0.285, 0.435, 0.385, NAVY, lw=1.5)
    ax.text(0.068, 0.625, "长板", fontsize=15.0, color=NAVY, weight="bold",
            ha="left", va="center", zorder=6)
    ax.text(0.068, 0.570,
            "单卡跑超显存模型\n150K 长上下文\nA 卡专项优化\n上手门槛低",
            fontsize=10.6, color=DARK, ha="left", va="top",
            linespacing=1.75, zorder=6)

    card(ax, 0.520, 0.285, 0.435, 0.385, RED, lw=1.5)
    ax.text(0.543, 0.625, "短板", fontsize=15.0, color=RED, weight="bold",
            ha="left", va="center", zorder=6)
    ax.text(0.543, 0.570,
            "内存 / PCIe 带宽瓶颈\n并发只到四路\n架构覆盖有限\n生态仍年轻",
            fontsize=10.6, color=DARK, ha="left", va="top",
            linespacing=1.75, zorder=6)

    punchline(fig, "先把 A 卡玩家接住，再谈机房。")
    footer(fig, "事实来源：MoE4All README（并发实测、支持家族）；moe4all.com")
    fig.savefig(OUT + "图3_偏科生.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)