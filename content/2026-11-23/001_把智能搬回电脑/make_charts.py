# -*- coding: utf-8 -*-
"""
《把智能搬回自己的电脑：前 DeepSeek-VL 负责人张博开源 Linger》配套图表

事实口径（核到 heylinger.com、docs.heylinger.com、GitHub 仓库与媒体报道）：
  · 张博 2026-11-19 发布帖：1960 年代计算集中，PC 把算力交给个人；
    今天 AI 在数据中心训练、按 token 出租，智能应当是分布式的。
  · PolyStrata：MoE 热专家在显存，其余在内存 / SSD。
    官方硬件表：Qwen3.8-Flash-Next（125B）在 RTX 3060 12GB 上 45.5 tok/s，
    RTX 5090 32GB 上 179 tok/s。
  · 官方跑分为企业自测，36 氪明确提示未获充分第三方验证。
  · 文档写明：语音、连接应用、构建记忆的后台任务会用到外部服务。

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
    """三个时代：大型机 → 个人电脑 → 个人 Agent"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "三个时代，同一条路线",
           "算力先集中，再分散；智能正在走同一条路")

    eras = [
        ("1960s", "大型机", "计算在机房\n排队上机，按小时租", GRAY),
        ("1980s", "个人电脑", "算力到桌面\n一次买断，自己拥有", SLATE),
        ("2026", "个人 Agent", "智能到本机\n上下文与数据不出门", NAVY),
    ]
    w, gap = 0.28, 0.035
    x = 0.045
    for tag, name, note, color in eras:
        card(ax, x, 0.395, w, 0.270, color, lw=1.5)
        ax.text(x + 0.022, 0.612, tag, fontsize=11.0, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(x + 0.022, 0.552, name, fontsize=17.0, color=DARK,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(x + 0.022, 0.470, note, fontsize=10.0, color=SLATE,
                ha="left", va="top", linespacing=1.7, zorder=6)
        x += w + gap

    for i in range(2):
        xa = 0.045 + i * (w + gap) + w + 0.004
        ax.add_patch(FancyArrowPatch(
            (xa, 0.530), (xa + gap - 0.008, 0.530),
            arrowstyle="-|>", mutation_scale=16, color=GRAY, lw=1.4))

    ax.text(0.045, 0.300,
            "“1960 年代，计算是中心化的，直到 PC 把权力交到每个人手中。\n"
            "如今 AI 在数据中心训练，再以 token 的形式租给你。”",
            fontsize=10.6, color=SLATE, ha="left", va="top",
            linespacing=1.9)
    ax.text(0.045, 0.205, "——张博，2026-11-19 发布帖",
            fontsize=8.8, color=GRAY, ha="left", va="top")

    punchline(fig, "AI 也在等一次 PC 时刻。")
    footer(fig, "事实来源：张博 2026-11-19 发布帖；量子位、智东西 2026-11-20 报道")
    fig.savefig(OUT + "图1_三个时代.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """分层存储 + 官方速度"""
    fig = plt.figure(figsize=(12, 6.9))

    header(fig, "12GB 显卡，怎么装下 125B",
           "PolyStrata：热专家进显存，冷专家退到内存和 SSD")

    ax = fig.add_axes([0.045, 0.145, 0.455, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    tiers = [
        (0.720, "显存 VRAM", "热专家 + KV 缓存", "最快，也最贵", NAVY),
        (0.380, "内存 RAM", "冷专家常驻", "按需换入换出", SLATE),
        (0.040, "硬盘 SSD", "完整权重", "只读，兜底", GRAY),
    ]
    for y, name, sub, note, color in tiers:
        card(ax, 0.020, y, 0.960, 0.250, color, lw=1.4)
        ax.text(0.055, y + 0.172, name, fontsize=13.0, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(0.055, y + 0.092, sub, fontsize=9.6, color=DARK,
                ha="left", va="center", zorder=6)
        ax.text(0.640, y + 0.092, note, fontsize=8.8, color=GRAY,
                ha="left", va="center", zorder=6)

    for y0, y1 in [(0.720, 0.630), (0.380, 0.290)]:
        ax.add_patch(FancyArrowPatch(
            (0.500, y0), (0.500, y1),
            arrowstyle="<|-|>", mutation_scale=16, color=RED, lw=1.4))
    ax.text(0.520, 0.675, "搬进 / 搬出", fontsize=8.6, color=RED,
            ha="left", va="center")
    ax.text(0.520, 0.335, "搬进 / 搬出", fontsize=8.6, color=RED,
            ha="left", va="center")

    ax2 = fig.add_axes([0.600, 0.330, 0.360, 0.430])
    names = ["RTX 3060\n12 GB", "RTX 5090\n32 GB"]
    vals = [45.5, 179.0]
    bars = ax2.bar([0, 1], vals, width=0.52, color=[NAVY, NAVY], zorder=3)
    ax2.set_xticks([0, 1])
    ax2.set_xticklabels(names, fontsize=9.4, color=SLATE)
    ax2.set_ylim(0, 205)
    ax2.set_title("Qwen3.8-Flash-Next 125B · tok/s", fontsize=10.2,
                  color=SLATE, pad=12)
    ax2.tick_params(axis="y", labelsize=8.2, colors=GRAY)
    ax2.grid(axis="y", color=LIGHT, linewidth=0.8, alpha=0.7, zorder=0)
    for spine in ("top", "right"):
        ax2.spines[spine].set_visible(False)
    for spine in ("left", "bottom"):
        ax2.spines[spine].set_color(LIGHT)
    for b, v in zip(bars, vals):
        ax2.text(b.get_x() + b.get_width() / 2, v + 4,
                 "%.1f" % v, fontsize=10.0, color=DARK,
                 ha="center", va="bottom")

    fig.text(0.600, 0.268,
             "官方硬件表：3060 需 64 GB 系统内存；\n"
             "上述跑分为企业自测，未获第三方复现。",
             fontsize=8.6, color=GRAY, ha="left", va="top",
             linespacing=1.7)

    punchline(fig, "装不下就不装，按需搬运。")
    footer(fig, "事实来源：docs.heylinger.com 硬件与 PolyStrata 页；36氪 2026-11-21")
    fig.savefig(OUT + "图2_12GB跑125B.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """能与代价"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "本地是真的，零成本不是全部",
           "Linger 的能与代价")

    card(ax, 0.045, 0.250, 0.440, 0.425, NAVY, lw=1.5)
    ax.text(0.068, 0.620, "能", fontsize=22, color=NAVY, weight="bold",
            ha="left", va="center", zorder=6)
    ax.text(0.068, 0.552,
            "12 GB 显存跑 125B 模型\n"
            "本地推理不产生 token 账单\n"
            "记忆、规则、文件留在本机\n"
            "直接操作桌面与浏览器里的应用\n"
            "主动提醒会从你的回复里学规则",
            fontsize=10.6, color=DARK, ha="left", va="top",
            linespacing=1.95, zorder=6)

    card(ax, 0.515, 0.250, 0.440, 0.425, RED, lw=1.5)
    ax.text(0.538, 0.620, "代价", fontsize=22, color=RED, weight="bold",
            ha="left", va="center", zorder=6)
    ax.text(0.538, 0.552,
            "125B 要 12 GB 显存起步\n"
            "语音与连接应用走外部服务\n"
            "夜里建记忆的后台要用外部算力\n"
            "规则还没有集中管理页\n"
            "跑分为官方自测，未第三方复现",
            fontsize=10.6, color=DARK, ha="left", va="top",
            linespacing=1.95, zorder=6)

    punchline(fig, "它把智能搬回了家，也把麻烦搬回了家。")
    footer(fig, "事实来源：docs.heylinger.com（数据与隐私、个人记忆）；36氪 2026-11-21")
    fig.savefig(OUT + "图3_能与代价.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)
