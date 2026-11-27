# -*- coding: utf-8 -*-
"""
《量化到底是什么：把一个 27B 模型从 54.7GB 压到 17GB，钱省在哪，代价又在哪》配套图表

事实口径（全部取自 DataLearner AI 博客 2026-08-19 及其所引来源）：

一、模型
  · Qwen3.8-27B，27B dense，BF16 原始权重约 54.7GB。

二、Unsloth GGUF 尺寸曲线
  · BF16 54.7GB / Q8_0 29.0GB / Q6_K 22.9GB / Q5_K_M 19.8GB /
    UD-Q4_K_XL 17.9GB / Q4_K_M 17.1GB / UD-Q3_K_XL 13.4GB / UD-IQ2_XXS 9.0GB

三、运行显存 = 权重 + 额外占用
  · 额外占用含 KV Cache、Runtime Buffer、CUDA/Vulkan/Metal 后端开销、
    长上下文额外显存、视觉组件或 MTP 额外占用。
  · Q4_K_M 在 64K 上下文下峰值显存约 20.3GB（权重 17.1GB）。

四、命名规则
  · Q 后数字为位宽；K 为 K-quant 分块量化；M/S/XL/XXS 为同档精细度；
    I 开头为 importance-aware 格点量化；UD/AD 为动态量化。

五、档位推荐
  · 16GB：UD-Q3_K_XL 或社区定制约 14GB 混合版本，妥协档
  · 24GB：首选 UD-Q4_K_XL，次选 Q4_K_M，甜点区
  · 32GB：Q5_K_M / Q6_K，质量更舒服
  · 48GB+：Q6 / Q8 / BF16，工作站级

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
    """尺寸曲线"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "从 54.7GB 到 9.0GB：一条清晰的尺寸曲线",
           "Unsloth 发布的 Qwen3.8-27B GGUF 各版本文件大小")

    data = [
        ("BF16", 54.7, GRAY),
        ("Q8_0", 29.0, SLATE),
        ("Q6_K", 22.9, SLATE),
        ("Q5_K_M", 19.8, SLATE),
        ("UD-Q4_K_XL", 17.9, NAVY),
        ("Q4_K_M", 17.1, NAVY),
        ("UD-Q3_K_XL", 13.4, TEAL),
        ("UD-IQ2_XXS", 9.0, RED),
    ]

    x0 = 0.250
    span = 0.620
    maxv = 54.7
    y = 0.720

    for name, val, color in data:
        ax.text(0.048, y, name, fontsize=9.6, color=DARK,
                ha="left", va="center")
        w = span * val / maxv
        ax.add_patch(Rectangle((x0, y - 0.016), w, 0.032,
                               facecolor=color, edgecolor=color,
                               linewidth=0, alpha=0.90, zorder=4))
        ax.text(x0 + w + 0.010, y, f"{val}GB", fontsize=9.4, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        y -= 0.072

    ax.text(0.048, 0.126,
            "54.7GB 压到 17.1GB，体积不到三分之一。",
            fontsize=9.8, color=DARK, ha="left", va="center")

    punchline(fig, "量化不是优化选项，是能不能用的前置条件。")
    footer(fig, "事实来源：DataLearner AI（2026-08-19）所引 unsloth/Qwen3.8-27B-GGUF")
    fig.savefig(OUT + "图1_尺寸曲线.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """显存构成"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "17GB 的模型，吃掉了 20.3GB 显存",
           "Q4_K_M 在 64K 上下文下的峰值占用（GB）")

    ax.text(0.048, 0.760, "权重只是其中一块", fontsize=10.2, color=GRAY,
            ha="left", va="center")
    ax.plot([0.048, 0.952], [0.742, 0.742], color=LIGHT, linewidth=1.0)

    total = 20.3
    parts = [
        ("权重文件", 17.1, NAVY),
        ("KV Cache 与运行时等", 3.2, RED),
    ]

    x0 = 0.048
    span = 0.870
    y = 0.620
    cur = x0
    for name, val, color in parts:
        w = span * val / total
        ax.add_patch(Rectangle((cur, y), w, 0.090,
                               facecolor=color, edgecolor="white",
                               linewidth=1.6, alpha=0.92, zorder=4))
        # 数值标在色块内部居中；仅当块足够宽时标名称
        ax.text(cur + w / 2, y + 0.045, f"{val}GB", fontsize=11.0,
                color="white", weight="bold", ha="center", va="center",
                zorder=6)
        cur += w

    # 图例放在条形下方
    lx = 0.048
    for name, val, color in parts:
        ax.add_patch(Rectangle((lx, 0.566), 0.020, 0.020,
                               facecolor=color, edgecolor=color,
                               linewidth=0, alpha=0.92, zorder=6))
        ax.text(lx + 0.030, 0.576, f"{name}　{val}GB", fontsize=9.4,
                color=DARK, ha="left", va="center", zorder=6)
        lx += 0.050 * len(name) + 0.075

    ax.text(0.048, 0.520, f"峰值合计约 {total}GB", fontsize=12.0,
            color=DARK, weight="bold", ha="left", va="center")

    rows = [
        ("KV Cache", "随上下文长度线性增长，4K 与 64K 能差一个量级"),
        ("运行时 Buffer", "CUDA / Vulkan / Metal 各有预留，不体现在模型文件里"),
        ("附加组件", "视觉编码器、MTP 草稿头，都要额外空间"),
    ]
    y = 0.430
    for k, v in rows:
        ax.text(0.048, y, k, fontsize=9.6, color=DARK, weight="bold",
                ha="left", va="center")
        ax.text(0.230, y, v, fontsize=9.2, color=SLATE,
                ha="left", va="center")
        y -= 0.062

    card(ax, 0.048, 0.150, 0.904, 0.070, RED, face="white", lw=1.3)
    ax.text(0.070, 0.185,
            "所以第一原则是：先确定显存预算，再反推量化版本。顺序反了就是反复 OOM。",
            fontsize=9.6, color=DARK, ha="left", va="center", zorder=6)

    punchline(fig, "文件大小不等于运行显存——这是最容易踩的坑。")
    footer(fig, "事实来源：DataLearner AI（2026-08-19）；Q4_K_M 在 64K 上下文下峰值显存约 20.3GB")
    fig.savefig(OUT + "图2_显存构成.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """命名规则"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "Q4_K_M 这五个字符，各自在说什么",
           "看懂命名，才不会把「Q4」当成一回事")

    tokens = [
        ("UD-", "动态量化", "对特定模型挑层压：\n敏感层保高精度", TEAL, 0.048, 0.150),
        ("Q4", "主精度位宽", "每个权重大致\n占 4 位", NAVY, 0.218, 0.130),
        ("_K", "分块量化", "按块处理，\n每块单独算缩放", SLATE, 0.366, 0.140),
        ("_M", "精细程度", "同档位内\n的中等策略", GRAY, 0.524, 0.140),
    ]

    for tk, name, desc, color, x, w in tokens:
        card(ax, x, 0.480, w, 0.240, color, lw=1.5)
        ax.text(x + w / 2, 0.668, tk, fontsize=17, color=color,
                weight="bold", ha="center", va="center", zorder=6)
        ax.text(x + w / 2, 0.588, name, fontsize=9.6, color=DARK,
                ha="center", va="center", zorder=6)
        ax.text(x + w / 2, 0.516, desc, fontsize=8.2, color=SLATE,
                ha="center", va="center", zorder=6, linespacing=1.6)

    ax.text(0.048, 0.412, "另外两个常见前缀", fontsize=10.2, color=GRAY,
            ha="left", va="center")
    ax.plot([0.048, 0.952], [0.394, 0.394], color=LIGHT, linewidth=1.0)

    rows = [
        ("AD-", "另一种发布者的动态量化，与 UD- 同类思路"),
        ("IQ", "importance-aware 格点量化，用更少的位逼近精度，计算更绕"),
    ]
    y = 0.350
    for k, v in rows:
        ax.text(0.048, y, k, fontsize=11.0, color=TEAL, weight="bold",
                ha="left", va="center")
        ax.text(0.150, y, v, fontsize=9.2, color=SLATE,
                ha="left", va="center")
        y -= 0.066

    card(ax, 0.048, 0.140, 0.904, 0.086, RED, face="white", lw=1.3)
    ax.text(0.070, 0.198, "名字只告诉你位宽，不告诉你压得好不好。",
            fontsize=10.2, color=DARK, weight="bold",
            ha="left", va="center", zorder=6)
    ax.text(0.070, 0.160,
            "同样标 Q4，不同发布者的 KLD 能差 2.2 倍（0.00955 到 0.02094）。",
            fontsize=9.2, color=SLATE, ha="left", va="center", zorder=6)

    punchline(fig, "挑着压，还是齐着压，决定了同样的位宽能差多少。")
    footer(fig, "事实来源：DataLearner AI（2026-08-19）；GGUF 命名规则为通用格式说明")
    fig.savefig(OUT + "图3_命名规则.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 4
def fig4():
    """四个档位"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "四个显存档位，四种过日子",
           "先定预算，再反推版本")

    tiers = [
        ("16GB", "妥协档", "UD-Q3_K_XL\n或 14GB 混合版", "能跑，但 KV Cache 空间\n极紧，长上下文易 OOM", GRAY),
        ("24GB", "甜点区", "UD-Q4_K_XL\n其次 Q4_K_M", "模型完整进显存，\n32K～64K 现实", RED),
        ("32GB", "质量档", "Q5_K_M / Q6_K", "误差更低，长上下文\n和 MTP 都留有余量", NAVY),
        ("48GB+", "工作站", "Q6 / Q8 / BF16", "重点不再是能不能跑，\n而是开多大、服务几人", TEAL),
    ]

    x = 0.048
    w = 0.214
    gap = 0.020
    for name, tag, rec, desc, color in tiers:
        card(ax, x, 0.320, w, 0.380, color, lw=1.5)
        ax.text(x + w / 2, 0.652, name, fontsize=20, color=color,
                weight="bold", ha="center", va="center", zorder=6)
        ax.text(x + w / 2, 0.590, tag, fontsize=10.0, color=DARK,
                ha="center", va="center", zorder=6)
        ax.plot([x + 0.028, x + w - 0.028], [0.566, 0.566],
                color=LIGHT, linewidth=1.0, zorder=6)
        ax.text(x + w / 2, 0.512, rec, fontsize=8.6, color=color,
                weight="bold", ha="center", va="center", zorder=6,
                linespacing=1.7)
        ax.text(x + w / 2, 0.396, desc, fontsize=8.2, color=SLATE,
                ha="center", va="center", zorder=6, linespacing=1.7)
        x += w + gap

    ax.text(0.048, 0.262,
            "同样一张 24GB 卡，跑 Q4 版本时 32K～64K 是比较现实的区间——"
            "而不是文件大小暗示的「16GB 就够」。",
            fontsize=9.4, color=SLATE, ha="left", va="center")

    punchline(fig, "24GB 是最自然的落点，32GB 开始买「稳」。")
    footer(fig, "事实来源：DataLearner AI（2026-08-19）的分档推荐")
    fig.savefig(OUT + "图4_四个档位.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 5
def fig5():
    """54.7GB 这堵墙"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "54.7GB 这堵墙：常见显卡装不下原始权重",
           "BF16 权重与常见显存档位的对照（GB）")

    cards_vram = [
        ("RTX 4090", 24, GRAY),
        ("RTX 5090", 32, SLATE),
        ("R9700", 32, SLATE),
        ("统一内存", 48, TEAL),
    ]
    need = 54.7

    x0 = 0.185
    span = 0.450
    maxv = 60.0
    y = 0.660

    for name, vram, color in cards_vram:
        ax.text(0.048, y, name, fontsize=9.4, color=DARK,
                ha="left", va="center")
        w = span * vram / maxv
        ax.add_patch(Rectangle((x0, y - 0.017), w, 0.034,
                               facecolor=color, edgecolor=color,
                               linewidth=0, alpha=0.85, zorder=4))
        ax.text(x0 + w + 0.008, y, f"{vram}GB", fontsize=8.8, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        y -= 0.078

    # BF16 需求线
    xneed = x0 + span * need / maxv
    ax.plot([xneed, xneed], [0.720, 0.240], color=RED, linewidth=1.6,
            linestyle="--", zorder=5)
    ax.text(xneed - 0.008, 0.760, "BF16 权重 54.7GB", fontsize=9.4,
            color=RED, weight="bold", ha="right", va="center")

    ax.text(0.048, 0.380, "所有常见档位都够不到这条线。",
            fontsize=10.0, color=DARK, ha="left", va="center")
    ax.text(0.048, 0.336,
            "再加上 KV Cache、运行时与后端开销，BF16 想舒服跑，实际需求轻松过 60GB。",
            fontsize=9.2, color=SLATE, ha="left", va="center")

    card(ax, 0.048, 0.150, 0.904, 0.086, NAVY, face=PALE, lw=1.2)
    ax.text(0.070, 0.212, "量化的全部意义就在这道缝里：把「必须有机房」换成「你得有一张卡」。",
            fontsize=9.8, color=DARK, ha="left", va="center", zorder=6)
    ax.text(0.070, 0.174, "从 54.7GB 到 17.1GB，模型才有资格出现在桌面上。",
            fontsize=9.2, color=SLATE, ha="left", va="center", zorder=6)

    punchline(fig, "不是消费级硬件变强了，是模型被压小了。")
    footer(fig, "事实来源：DataLearner AI（2026-08-19）；BF16 权重 54.7GB 为其所列数据")
    fig.savefig(OUT + "图5_54.7GB的墙.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    fig4()
    fig5()
    print("done ->", OUT)



