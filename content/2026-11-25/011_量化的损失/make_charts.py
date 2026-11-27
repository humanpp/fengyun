# -*- coding: utf-8 -*-
"""
《量化到底损失了什么：四个指标，两种陷阱，一个拐点》配套图表

事实口径（DataLearner AI 2026-08-19 所引 AtomicChat 统一 held-out 测试）：

一、KLD 与 Top-1 Agreement
  · Q8_0      28.9GB  KLD 0.00064  Top-1 98.92%
  · AD-Q6_K   25.0GB  KLD 0.00107  Top-1 98.67%
  · AD-Q5_K_M 20.2GB  KLD 0.00419  Top-1 97.34%
  · AD-Q5/Q4  18.6GB  KLD 0.00730  Top-1 96.43%
  · AD-Q4_K_M 17.1GB  KLD 0.01126  Top-1 95.59%
  · AD-IQ4_XS 16.5GB  KLD 0.01248  Top-1 95.39%
  · AD-IQ3_S  13.8GB  KLD 0.03247  Top-1 92.41%
  · AD-IQ3_XXS 12.1GB KLD 0.06972  Top-1 89.13%
  · AD-IQ2_S  11.1GB  KLD 0.09832  Top-1 87.18%
  · AD-IQ2_XXS 9.0GB  KLD 0.25663  Top-1 79.44%

二、同为 4bit 附近的横向对比（KLD）
  · LM Studio Q4_K_M      16.8GB  0.02094
  · ggml-org Q4_K_M       19.0GB  0.01470
  · AtomicChat AD-Q4_K_M  17.1GB  0.01126
  · Unsloth UD-Q4_K_XL   约17.9GB 0.00955

三、PPL（同一套 llama.cpp 配置，WikiText 类语料）
  · Q8_0 6.9557 / Q4_K_M 6.9576 / IQ4_XS 7.0130 /
    UD-Q3_K_XL 7.1113 / UD-IQ3_XXS 7.2441

风格：克制传媒风，白底、低饱和配色、标题即结论（沿用本工作区既有规范）
输出目录 = 脚本所在目录
"""
import os
import math

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

DATA = [
    ("Q8_0", 28.9, 0.00064, 98.92),
    ("AD-Q6_K", 25.0, 0.00107, 98.67),
    ("AD-Q5_K_M", 20.2, 0.00419, 97.34),
    ("AD-Q5/Q4", 18.6, 0.00730, 96.43),
    ("AD-Q4_K_M", 17.1, 0.01126, 95.59),
    ("AD-IQ4_XS", 16.5, 0.01248, 95.39),
    ("AD-IQ3_S", 13.8, 0.03247, 92.41),
    ("AD-IQ3_XXS", 12.1, 0.06972, 89.13),
    ("AD-IQ2_S", 11.1, 0.09832, 87.18),
    ("AD-IQ2_XXS", 9.0, 0.25663, 79.44),
]

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
    """KLD 曲线"""
    fig = plt.figure(figsize=(12, 7.2))
    ax = new_axes(fig)

    header(fig, "误差不是匀速上涨的",
           "KL Divergence：越低越接近 BF16。纵轴为对数刻度")

    x0 = 0.255
    span = 0.560
    lo = math.log10(0.00064)
    hi = math.log10(0.25663)

    def w_of(v):
        return span * (math.log10(v) - lo) / (hi - lo)

    y = 0.742
    for name, size, kld, top1 in DATA:
        color = RED if name in ("AD-Q4_K_M", "AD-IQ4_XS") else (
            TEAL if kld > 0.03 else (NAVY if kld < 0.005 else SLATE))
        ax.text(0.048, y, name, fontsize=9.0, color=DARK,
                ha="left", va="center")
        w = max(w_of(kld), 0.006)
        ax.add_patch(Rectangle((x0, y - 0.012), w, 0.024,
                               facecolor=color, edgecolor=color,
                               linewidth=0, alpha=0.90, zorder=4))
        ax.text(x0 + w + 0.008, y, f"{kld}", fontsize=8.4, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        y -= 0.058

    ax.text(0.048, 0.140,
            "Q8 到 Q4 误差爬得很慢；过了 Q4 往 Q3、Q2 走，误差开始加速。",
            fontsize=9.6, color=DARK, ha="left", va="center")

    punchline(fig, "这条曲线不是直线，它在 Q4 附近改了斜率。")
    footer(fig, "事实来源：DataLearner AI（2026-08-19）所引 AtomicChat 统一 held-out 测试")
    fig.savefig(OUT + "图1_KLD误差.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """Top-1 一致率"""
    fig = plt.figure(figsize=(12, 7.2))
    ax = new_axes(fig)

    header(fig, "和原模型意见一致的比例",
           "Top-1 Agreement：量化后仍选择 BF16 那个 token 的概率")

    x0 = 0.255
    span = 0.500
    lo_v, hi_v = 70.0, 100.0

    y = 0.742
    for name, size, kld, top1 in DATA:
        if top1 >= 96:
            color = NAVY
        elif top1 >= 92:
            color = SLATE
        else:
            color = RED
        ax.text(0.048, y, name, fontsize=9.0, color=DARK,
                ha="left", va="center")
        w = span * (top1 - lo_v) / (hi_v - lo_v)
        ax.add_patch(Rectangle((x0, y - 0.012), w, 0.024,
                               facecolor=color, edgecolor=color,
                               linewidth=0, alpha=0.88, zorder=4))
        ax.text(x0 + w + 0.008, y, f"{top1}%", fontsize=8.4, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        y -= 0.058

    ax.text(0.048, 0.140,
            "横轴自 70% 起算，用于放大差异。95.59% 意味着每 20 个 token 约 1 个与 BF16 不同。",
            fontsize=9.2, color=SLATE, ha="left", va="center")

    punchline(fig, "一致率跌到 92% 以下，Agent 链路就开始不可靠。")
    footer(fig, "事实来源：DataLearner AI（2026-08-19）所引 AtomicChat 统一 held-out 测试")
    fig.savefig(OUT + "图2_Top1一致率.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """拐点"""
    fig = plt.figure(figsize=(12, 7.2))
    ax = new_axes(fig)

    header(fig, "Q4 是个拐点：省显存开始变贵",
           "点上标编号，右侧为对照清单；纵轴为 KL Divergence（对数）")

    px0, pw = 0.075, 0.520
    py0, ph = 0.250, 0.450

    def X(v):
        return px0 + pw * v / 30.0

    lo = math.log10(0.00064)
    hi = math.log10(0.25663)

    def Y(v):
        return py0 + ph * (math.log10(v) - lo) / (hi - lo)

    ax.plot([px0, px0 + pw], [py0, py0], color=SLATE, linewidth=1.0)
    ax.plot([px0, px0], [py0, py0 + ph], color=SLATE, linewidth=1.0)
    ax.text(px0 + pw / 2, py0 - 0.026, "模型体积 GB",
            fontsize=8.6, color=GRAY, ha="center", va="top")
    ax.text(px0 - 0.010, py0 + ph / 2, "KLD", fontsize=8.6, color=GRAY,
            ha="right", va="center", rotation=90)

    # Q4 区间底纹
    ax.add_patch(Rectangle((X(16.0), py0), X(19.0) - X(16.0), ph,
                           facecolor=PALE, edgecolor="none", zorder=1))
    ax.text((X(16.0) + X(19.0)) / 2, py0 + ph + 0.016, "Q4 区间",
            fontsize=8.6, color=RED, weight="bold", ha="center", va="bottom")

    for i, (name, size, kld, top1) in enumerate(DATA, start=1):
        cx, cy = X(size), Y(kld)
        color = RED if 16.0 <= size <= 19.0 else (
            TEAL if kld > 0.03 else NAVY)
        ax.plot([cx], [cy], marker="o", markersize=8.5, color=color,
                zorder=6)
        ax.text(cx, cy, str(i), fontsize=6.4, color="white", weight="bold",
                ha="center", va="center", zorder=7)

    # 右侧清单
    ax.text(0.630, py0 + ph - 0.010, "编号对照", fontsize=9.2, color=GRAY,
            ha="left", va="center")
    ax.plot([0.630, 0.952], [py0 + ph - 0.028, py0 + ph - 0.028],
            color=LIGHT, linewidth=1.0)

    y = py0 + ph - 0.058
    for i, (name, size, kld, top1) in enumerate(DATA, start=1):
        color = RED if 16.0 <= size <= 19.0 else (
            TEAL if kld > 0.03 else NAVY)
        ax.text(0.630, y, f"{i}", fontsize=8.2, color=color, weight="bold",
                ha="left", va="center")
        ax.text(0.658, y, name, fontsize=8.2, color=DARK,
                ha="left", va="center")
        ax.text(0.952, y, f"{kld}", fontsize=8.2, color=color,
                ha="right", va="center")
        y -= 0.042

    card(ax, 0.048, 0.118, 0.904, 0.066, LIGHT, face=PALE, lw=1.0)
    ax.text(0.070, 0.151,
            "Q4 之前，每省 1GB 精度代价便宜；Q4 之后，同样 1GB 要贵得多。",
            fontsize=9.4, color=DARK, ha="left", va="center", zorder=6)

    punchline(fig, "「Q4 是甜点区」不是经验之谈，是曲线上一个转折。")
    footer(fig, "事实来源：DataLearner AI（2026-08-19）所引 AtomicChat 测试数据")
    fig.savefig(OUT + "图3_拐点.png", dpi=170)
    plt.close(fig)

# ---------------------------------------------------------------- 图 4
def fig4():
    """同为 Q4"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "同样标着 Q4，误差差 2.2 倍",
           "四个发布者的 4bit 版本，KL Divergence 对比")

    items = [
        ("LM Studio Q4_K_M", 16.8, 0.02094, GRAY),
        ("ggml-org Q4_K_M", 19.0, 0.01470, SLATE),
        ("AtomicChat AD-Q4_K_M", 17.1, 0.01126, NAVY),
        ("Unsloth UD-Q4_K_XL", 17.9, 0.00955, TEAL),
    ]

    x0 = 0.330
    span = 0.480
    maxv = 0.02094

    y = 0.660
    for name, size, kld, color in items:
        ax.text(0.048, y, name, fontsize=9.6, color=DARK,
                ha="left", va="center")
        w = span * kld / maxv
        ax.add_patch(Rectangle((x0, y - 0.018), w, 0.036,
                               facecolor=color, edgecolor=color,
                               linewidth=0, alpha=0.90, zorder=4))
        ax.text(x0 + w + 0.010, y, f"{kld}", fontsize=9.6, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(x0, y - 0.040, f"{size}GB", fontsize=8.0, color=GRAY,
                ha="left", va="top")
        y -= 0.098

    ax.text(0.048, 0.300, "为什么差这么多？", fontsize=10.0, color=GRAY,
            ha="left", va="center")
    ax.plot([0.048, 0.952], [0.282, 0.282], color=LIGHT, linewidth=1.0)

    rows = [
        "哪些 tensor 保留更高精度",
        "Attention / FFN / Output Head 之间怎么分配 bit",
        "用不用 importance matrix",
        "做不做架构感知的动态量化",
    ]
    x = 0.048
    yy = 0.222
    for i, r in enumerate(rows):
        ax.text(0.048 + (i % 2) * 0.470, 0.222 - (i // 2) * 0.048,
                "· " + r, fontsize=9.0, color=SLATE, ha="left", va="center")

    punchline(fig, "名字只告诉你位宽，不告诉你它压得好不好。")
    footer(fig, "事实来源：DataLearner AI（2026-08-19）所引 AtomicChat 对比；"
                "Unsloth 版本 KLD 见表中约 17.9GB 一栏")
    fig.savefig(OUT + "图4_同为Q4.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 5
def fig5():
    """PPL 陷阱"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "PPL 几乎没变，但这不是「无损」的证据",
           "同一套 llama.cpp 配置、WikiText 类语料下的困惑度")

    items = [
        ("Q8_0", 6.9557, SLATE),
        ("Q4_K_M", 6.9576, NAVY),
        ("IQ4_XS", 7.0130, NAVY),
        ("UD-Q3_K_XL", 7.1113, GRAY),
        ("UD-IQ3_XXS", 7.2441, RED),
    ]

    x0 = 0.190
    span = 0.700
    lo_v, hi_v = 6.9, 7.3

    y = 0.640
    for name, ppl, color in items:
        ax.text(0.048, y, name, fontsize=9.6, color=DARK,
                ha="left", va="center")
        w = span * (ppl - lo_v) / (hi_v - lo_v)
        ax.add_patch(Rectangle((x0, y - 0.017), w, 0.034,
                               facecolor=color, edgecolor=color,
                               linewidth=0, alpha=0.88, zorder=4))
        ax.text(x0 + w + 0.008, y, f"{ppl}", fontsize=9.4, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        y -= 0.076

    ax.text(0.048, 0.286,
            "Q8 与 Q4 只差 0.0019，看上去几乎一模一样。",
            fontsize=9.6, color=DARK, ha="left", va="center")

    card(ax, 0.048, 0.148, 0.904, 0.106, RED, face="white", lw=1.4)
    ax.text(0.070, 0.222, "但 PPL 只说明「总体语言建模误差」没明显变化。",
            fontsize=9.8, color=DARK, weight="bold",
            ha="left", va="center", zorder=6)
    ax.text(0.070, 0.180,
            "它不自动等于 Coding、数学推理、长链 reasoning、工具调用都没掉——"
            "而那几项才是 Agent 真正吃的东西。",
            fontsize=9.0, color=SLATE, ha="left", va="center", zorder=6)

    punchline(fig, "指标看着一样，行为可以不一样。")
    footer(fig, "事实来源：DataLearner AI（2026-08-19）所引社区 PPL 测试（WikiText 类语料）")
    fig.savefig(OUT + "图5_PPL陷阱.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    fig4()
    fig5()
    print("done ->", OUT)


