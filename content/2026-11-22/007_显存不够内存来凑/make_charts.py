# -*- coding: utf-8 -*-
"""
《显存只有24G，模型有35B：MoE4All 把专家搬进了内存》配套图表

事实口径（核到项目 README 与 moe4all.com 性能页）：
  · MoE4All：Rust 编写、Apache-2.0，Vulkan 后端，分层存储（SSD/RAM/VRAM）。
  · 官方实测：RX 7900 XTX 24GB、Ryzen 5 5600X、64GB DDR4、Windows 11、
    Q8 KV、MTP 关闭；Qwen3.6 35B Balanced（约 5.91 bpw）。
    6K：预填充 3023.5 tok/s，单路解码 154.6，四路合计 248.3；
    30K：预填充 2988.7，单路解码 125.7；
    150K：预填充 1213.5，单路解码 65.1。

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
    """三级存储：SSD → RAM → VRAM → GPU"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "显存装不下的，交给内存和硬盘",
           "MoE4All 的分层：SSD → RAM → VRAM → GPU")

    tiers = [
        ("SSD", "完整权重", "只读 · 按需读", GRAY),
        ("RAM", "专家常驻", "热 / 冷队列", SLATE),
        ("VRAM", "当前专家 + KV", "24 GB", NAVY),
        ("GPU", "计算", "按路由结果执行", RED),
    ]
    w, gap = 0.205, 0.022
    x = 0.045
    for name, sub, note, color in tiers:
        card(ax, x, 0.420, w, 0.175, color, lw=1.4)
        ax.text(x + 0.020, 0.548, name, fontsize=14.0, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(x + 0.020, 0.492, sub, fontsize=9.4, color=DARK,
                ha="left", va="center", zorder=6)
        ax.text(x + 0.020, 0.456, note, fontsize=8.2, color=GRAY,
                ha="left", va="center", zorder=6)
        x += w + gap

    for i in range(3):
        xa = 0.045 + i * (w + gap) + w + 0.002
        ax.annotate("", xy=(xa + 0.016, 0.508), xytext=(xa, 0.508),
                    arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=1.4))

    ax.text(0.045, 0.315,
            "每步只搬路由选中的几个专家，不是整个模型。",
            fontsize=9.4, color=SLATE, ha="left", va="center")

    punchline(fig, "显存不够，往内存借；内存不够，往硬盘借。")
    footer(fig, "事实来源：MoE4All README 与 moe4all.com 性能页；GitHub Headmaster218/MoE4All")
    fig.savefig(OUT + "图1_三级存储.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """跑分：6K/30K/150K"""
    fig = plt.figure(figsize=(12, 6.9))

    header(fig, "上下文越长，速度降了，但没崩",
           "Qwen3.6 35B · RX 7900 XTX 24 GB · Q8 KV")

    ax1 = fig.add_axes([0.075, 0.330, 0.380, 0.400])
    ax2 = fig.add_axes([0.555, 0.330, 0.380, 0.400])

    xs = [0, 1, 2]
    labels = ["6K", "30K", "150K"]
    decode = [154.6, 125.7, 65.1]
    prefill = [3023.5, 2988.7, 1213.5]

    for ax, vals, title, top in [
        (ax1, decode, "解码  tok/s", 190),
        (ax2, prefill, "预填充  tok/s", 3650),
    ]:
        bars = ax.bar(xs, vals, width=0.55, color=NAVY, zorder=3)
        ax.set_xticks(xs)
        ax.set_xticklabels(labels, fontsize=9.5, color=SLATE)
        ax.set_ylim(0, top)
        ax.set_title(title, fontsize=10.6, color=SLATE, pad=10)
        ax.tick_params(axis="y", labelsize=8.2, colors=GRAY)
        ax.grid(axis="y", color=LIGHT, linewidth=0.8, alpha=0.7, zorder=0)
        for spine in ("top", "right"):
            ax.spines[spine].set_visible(False)
        for spine in ("left", "bottom"):
            ax.spines[spine].set_color(LIGHT)
        for b, v in zip(bars, vals):
            ax.text(b.get_x() + b.get_width() / 2, v + top * 0.018,
                    ("%.1f" % v) if v < 300 else ("%.1f" % v),
                    fontsize=8.6, color=DARK, ha="center", va="bottom")

    fig.text(0.075, 0.245,
             "官方实测：Ryzen 5 5600X · 64 GB DDR4 · Windows 11 · MTP 关闭；"
             "四路合计解码 248.3 tok/s。",
             fontsize=8.6, color=GRAY, ha="left", va="center")

    punchline(fig, "150K 还能跑 65 tok/s，这才是重点。")
    footer(fig, "事实来源：MoE4All README 跑分表（2026-11）；GitHub Headmaster218/MoE4All")
    fig.savefig(OUT + "图2_跑分.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """能与不能"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "长板够长，短板也清楚",
           "MoE4All 的能与不能")

    card(ax, 0.045, 0.285, 0.435, 0.390, NAVY, lw=1.5)
    ax.text(0.068, 0.625, "能", fontsize=22, color=NAVY, weight="bold",
            ha="left", va="center", zorder=6)
    ax.text(0.068, 0.560,
            "24 GB 显存跑 35B / 176B\n150K 上下文\nOpenAI 兼容 API\n四路以内并发",
            fontsize=11.0, color=DARK, ha="left", va="top",
            linespacing=1.85, zorder=6)

    card(ax, 0.520, 0.285, 0.435, 0.390, RED, lw=1.5)
    ax.text(0.543, 0.625, "不能", fontsize=22, color=RED, weight="bold",
            ha="left", va="center", zorder=6)
    ax.text(0.543, 0.560,
            "企业级多租户\n任意模型架构\n零调优满速\n高可用与审计",
            fontsize=11.0, color=DARK, ha="left", va="top",
            linespacing=1.85, zorder=6)

    punchline(fig, "它是单机神器，不是机房方案。")
    footer(fig, "事实来源：MoE4All README（支持家族、并发与 API）；moe4all.com")
    fig.savefig(OUT + "图3_边界.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)