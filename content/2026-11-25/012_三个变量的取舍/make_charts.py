# -*- coding: utf-8 -*-
"""
《质量、上下文、速度：三个变量抢同一块显存，你只能选两个》配套图表

事实口径（DataLearner AI 2026-08-19 所汇总的公开测试与社区讨论）：

一、速度谱系（典型输出速度）
  · RTX 3090 24GB  AWQ INT4 / SGLang            约 43 tok/s
  · RTX 5090 32GB  UD-Q6 / llama.cpp 无 MTP     约 52~56 tok/s
  · RTX 5090 32GB  Q5/Q6 + MTP                  常见约 90~120 tok/s
  · Radeon AI PRO R9700 32GB  Vulkan + MTP      最高约 51.8 tok/s
  · Ryzen AI Max+ 395  Vulkan + MTP             最高约 24.5 tok/s
  · M4 Max 36GB  MLX 4bit                       约 23.5 tok/s
  · M5 Max  优化 4bit + MTP                     社区约 50~60 tok/s

二、MTP
  · RTX 5090 同一 Q5 版本：不开 MTP 约 66 tok/s，开启约 121 tok/s
  · MTP 占用额外显存，压缩可用上下文

三、上下文与显存
  · Q4_K_M 权重 17.1GB；64K 上下文下峰值显存约 20.3GB

四、Reasoning Effort
  · Qwen3.8 默认开启 thinking，默认 reasoning_effort 为 xhigh
  · 模型卡另给 medium 与 low
  · 建议：普通聊天关 thinking 或 low；一般 Coding/Agent 用 medium；
    复杂调试、架构分析、数学问题用 xhigh

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
    """速度谱系"""
    fig = plt.figure(figsize=(12, 7.2))
    ax = new_axes(fig)

    header(fig, "20 到 120 tok/s，测的根本不是一回事",
           "同款模型在不同硬件与配置下的典型输出速度")

    items = [
        ("RTX 5090 · Q5/Q6 + MTP", 105, "90~120", RED),
        ("M5 Max · 4bit + MTP", 55, "50~60", TEAL),
        ("RTX 5090 · UD-Q6 无 MTP", 54, "52~56", NAVY),
        ("R9700 32GB · Vulkan + MTP", 51.8, "51.8", NAVY),
        ("RTX 3090 · AWQ INT4 / SGLang", 43, "43", NAVY),
        ("Ryzen AI Max+ 395 · Vulkan + MTP", 24.5, "24.5", GRAY),
        ("M4 Max 36GB · MLX 4bit", 23.5, "23.5", GRAY),
    ]

    x0 = 0.330
    span = 0.470
    maxv = 120.0

    y = 0.700
    for name, val, label, color in items:
        ax.text(0.048, y, name, fontsize=8.6, color=DARK,
                ha="left", va="center")
        w = span * val / maxv
        ax.add_patch(Rectangle((x0, y - 0.014), w, 0.028,
                               facecolor=color, edgecolor=color,
                               linewidth=0, alpha=0.90, zorder=4))
        ax.text(x0 + w + 0.008, y, label, fontsize=8.6, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        y -= 0.062

    ax.text(0.048, 0.196,
            "同一个 5090：不开 MTP 是 52~56，开了到 90~120。",
            fontsize=9.6, color=DARK, ha="left", va="center")
    ax.text(0.048, 0.160,
            "不说明量化、后端、上下文、MTP 这四项，tok/s 就没有可比性。",
            fontsize=9.0, color=SLATE, ha="left", va="center")

    punchline(fig, "看到速度数字，先问四个前提。")
    footer(fig, "事实来源：DataLearner AI（2026-08-19）汇总的公开测试"
                "（3090/SGLang 仓库、Unsloth 讨论区、AMD 博客、omlx.ai）")
    fig.savefig(OUT + "图1_速度谱系.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """MTP"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "MTP 让速度几乎翻倍，代价是显存",
           "RTX 5090、同一个 Q5 版本、同一上下文条件")

    bars = [
        ("不开 MTP", 66, SLATE),
        ("开启 MTP", 121, RED),
    ]

    x0 = 0.130
    span = 0.760
    maxv = 130.0
    base_y = 0.360
    max_h = 0.330

    for i, (name, val, color) in enumerate(bars):
        cx = x0 + span * (0.30 + i * 0.42)
        h = max_h * val / maxv
        ax.add_patch(Rectangle((cx - 0.070, base_y), 0.140, h,
                               facecolor=color, edgecolor=color,
                               linewidth=0, alpha=0.90, zorder=4))
        ax.text(cx, base_y + h + 0.022, f"{val}", fontsize=20, color=color,
                weight="bold", ha="center", va="bottom", zorder=6)
        ax.text(cx, base_y + h + 0.070, "tok/s", fontsize=9.0, color=GRAY,
                ha="center", va="bottom", zorder=6)
        ax.text(cx, base_y - 0.026, name, fontsize=10.4, color=DARK,
                weight="bold", ha="center", va="top")

    ax.plot([0.100, 0.952], [base_y, base_y], color=SLATE, linewidth=1.2)

    card(ax, 0.100, 0.150, 0.852, 0.120, RED, face="white", lw=1.3)
    ax.text(0.122, 0.234, "但 MTP 会吃掉额外显存，进而压缩可用上下文。",
            fontsize=9.8, color=DARK, weight="bold",
            ha="left", va="center", zorder=6)
    ax.text(0.122, 0.192,
            "所以它不是白给的速度：开了 MTP，就得接受上下文上限变低，"
            "或者接受更激进的量化。",
            fontsize=9.0, color=SLATE, ha="left", va="center", zorder=6)

    punchline(fig, "速度的每一分提升，都在显存里扣了钱。")
    footer(fig, "事实来源：DataLearner AI（2026-08-19）所引 Unsloth 讨论区 RTX 5090 测试")
    fig.savefig(OUT + "图2_MTP翻倍.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """上下文吃显存"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "上下文是显存的第二个买家",
           "Q4_K_M 权重 17.1GB，开 64K 上下文后峰值约 20.3GB")

    # 两条水平基线
    rows = [
        ("只加载权重", 17.1, [("权重 17.1GB", 17.1, NAVY)]),
        ("再开 64K 上下文", 20.3, [("权重 17.1GB", 17.1, NAVY),
                                   ("KV Cache 等 3.2GB", 3.2, RED)]),
    ]

    x0 = 0.048
    span = 0.870
    maxv = 22.0

    y = 0.620
    for label, total, parts in rows:
        ax.text(x0, y + 0.062, label, fontsize=10.0, color=DARK,
                ha="left", va="center")
        cur = x0
        for pname, pval, color in parts:
            w = span * pval / maxv
            ax.add_patch(Rectangle((cur, y), w, 0.052,
                                   facecolor=color, edgecolor="white",
                                   linewidth=1.4, alpha=0.92, zorder=4))
            ax.text(cur + w / 2, y + 0.026, pname, fontsize=8.6,
                    color="white" if w > 0.12 else DARK, weight="bold",
                    ha="center", va="center", zorder=6)
            cur += w
        ax.text(cur + 0.010, y + 0.026, f"合计 {total}GB", fontsize=9.0,
                color=SLATE, ha="left", va="center", zorder=6)
        y -= 0.130

    ax.text(0.048, 0.360, "多出来的 3.2GB，就是上下文的价钱。",
            fontsize=10.0, color=DARK, ha="left", va="center")

    rows2 = [
        ("32K～64K", "24GB 卡的现实区间"),
        ("128K", "KV Cache 大致再翻一倍，需往 32GB 或 48GB 走"),
    ]
    y = 0.322
    for k, v in rows2:
        ax.text(0.048, y, k, fontsize=9.6, color=RED, weight="bold",
                ha="left", va="center")
        ax.text(0.170, y, v, fontsize=9.2, color=SLATE,
                ha="left", va="center")
        y -= 0.058

    card(ax, 0.048, 0.132, 0.904, 0.078, NAVY, face=PALE, lw=1.2)
    ax.text(0.070, 0.184, "模型支持多少 token 是一回事，你的显存能撑住多少是另一回事。",
            fontsize=9.4, color=DARK, ha="left", va="center", zorder=6)
    ax.text(0.070, 0.150, "后者才是你能用的上限。",
            fontsize=9.0, color=SLATE, ha="left", va="center", zorder=6)

    punchline(fig, "上下文不是免费的开关，它有明码标价。")
    footer(fig, "事实来源：DataLearner AI（2026-08-19）；Q4_K_M 64K 上下文峰值约 20.3GB")
    fig.savefig(OUT + "图3_上下文吃显存.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 4
def fig4():
    """reasoning effort"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "默认档位是 xhigh：模型把时间花在「想太多」上",
           "reasoning_effort 三档，对等待时间的影响可能超过硬件")

    tiers = [
        ("low", "关闭 thinking\n或降到 low", "普通聊天", TEAL),
        ("medium", "中等思考", "一般 Coding / Agent", NAVY),
        ("xhigh", "最高档，也是默认", "复杂调试、架构分析、数学", RED),
    ]

    x = 0.048
    w = 0.278
    gap = 0.020
    for name, desc, use, color in tiers:
        card(ax, x, 0.380, w, 0.320, color, lw=1.5)
        ax.text(x + w / 2, 0.648, name, fontsize=17, color=color,
                weight="bold", ha="center", va="center", zorder=6)
        ax.text(x + w / 2, 0.566, desc, fontsize=9.0, color=DARK,
                ha="center", va="center", zorder=6, linespacing=1.7)
        ax.plot([x + 0.030, x + w - 0.030], [0.500, 0.500],
                color=LIGHT, linewidth=1.0, zorder=6)
        ax.text(x + w / 2, 0.440, "适合：\n" + use, fontsize=8.6,
                color=SLATE, ha="center", va="center", zorder=6,
                linespacing=1.7)
        x += w + gap

    ax.text(0.048, 0.322, "真正决定等待时间的是一个乘积：",
            fontsize=10.0, color=DARK, ha="left", va="center")
    ax.text(0.048, 0.280,
            "模型能力 × prefill 速度 × decode 速度 × 思维 token 数 × agent 轮数",
            fontsize=9.6, color=RED, weight="bold", ha="left", va="center")

    card(ax, 0.048, 0.150, 0.904, 0.086, LIGHT, face=PALE, lw=1.0)
    ax.text(0.070, 0.204,
            "decode 50 tok/s，但为一道简单题先想 20000 个思维 token，就是 400 秒。",
            fontsize=9.4, color=DARK, ha="left", va="center", zorder=6)
    ax.text(0.070, 0.170,
            "硬件再好也救不回来。很多人以为本地慢是硬件不够，其实只是默认档位太高。",
            fontsize=9.0, color=SLATE, ha="left", va="center", zorder=6)

    punchline(fig, "最该先调的不是显卡，是这个参数。")
    footer(fig, "事实来源：DataLearner AI（2026-08-19）；Qwen3.8 默认 reasoning_effort 为 xhigh，"
                "模型卡另给 medium 与 low")
    fig.savefig(OUT + "图4_思考档位.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 5
def fig5():
    """三角取舍"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "三个变量抢同一块显存",
           "给谁多一点，另外两个就少一点")

    cx, cy, r = 0.500, 0.470, 0.230

    pts = [
        ("质量", "往 Q5 / Q6 走", cx, cy + r, RED),
        ("上下文", "开得更长", cx - r * 0.87, cy - r * 0.50, NAVY),
        ("速度", "开 MTP", cx + r * 0.87, cy - r * 0.50, TEAL),
    ]

    # 三角连线
    for i in range(3):
        a = pts[i]
        b = pts[(i + 1) % 3]
        ax.plot([a[2], b[2]], [a[3], b[3]], color=LIGHT, linewidth=2.0,
                zorder=2)

    for name, note, px, py, color in pts:
        ax.plot([px], [py], marker="o", markersize=13, color=color,
                zorder=5)
        ax.text(px, py + 0.062, name, fontsize=13.0, color=color,
                weight="bold", ha="center", va="bottom", zorder=6)
        ax.text(px, py - 0.058, note, fontsize=9.0, color=SLATE,
                ha="center", va="top", zorder=6)

    ax.text(cx, cy + 0.012, "同一块显存", fontsize=10.4, color=DARK,
            weight="bold", ha="center", va="center")
    ax.text(cx, cy - 0.026, "总量是死的", fontsize=9.2, color=GRAY,
            ha="center", va="center")

    card(ax, 0.048, 0.132, 0.904, 0.080, RED, face="white", lw=1.3)
    ax.text(0.070, 0.184, "三个方向不可能同时拉满——这就是为什么没有标准答案。",
            fontsize=9.8, color=DARK, weight="bold",
            ha="left", va="center", zorder=6)
    ax.text(0.070, 0.150,
            "24GB 配 Q4 加 32K～64K 是多数人最舒服的起点；重度 Agent 则 32GB 配 Q5/Q6 更稳。",
            fontsize=9.0, color=SLATE, ha="left", va="center", zorder=6)

    punchline(fig, "问题不是最优解在哪，是你更愿意放弃哪一项。")
    footer(fig, "事实来源：DataLearner AI（2026-08-19）的取舍建议与本文归纳")
    fig.savefig(OUT + "图5_三角取舍.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    fig4()
    fig5()
    print("done ->", OUT)
