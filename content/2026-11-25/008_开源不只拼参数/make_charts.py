# -*- coding: utf-8 -*-
"""
《2800 亿开源、8B 会自己改图：同一天两个方向，国产开源不只在拼大小了》配套图表

事实口径：

一、百度文心 5.5 Flash Preview（ERNIE 5.5 Flash Preview）
  · 2026-11-11 发布，为 ERNIE 5.5 Flash Base 的首个后训练版本；
    官方发布页称权重"将以 Apache 2.0 开源"（原文 soon）。
    据 ERNIE 官方发布页 thinkingmachines 同级域名 ernie.baidu.com/release/ernie-5-5-flash-preview/。
  · 2026-11-24 正式开源，Apache 2.0，权重上架 Hugging Face 与 ModelScope，
    支持 vLLM、SGLang；MoE 架构，总参数 2800 亿，每 token 激活 140 亿，
    最长 100 万 token 上下文，生成速度每秒 200 token 以上。
    据 IT 之家 2026-11-24（经新浪科技转载）。
  · 榜单：AutomationBench 61.9（Claude Opus 5.5 为 58.0、DeepSeek V4.1 Flash 1017 为 57.2）；
    Terminal-Bench 4.0 46.5（Claude Opus 5.5 63.6、GPT-6.1 Sol 56.1、DeepSeek V4.1 Flash 40.9）；
    CodeArena WebDev 1668 分（DeepSeek-V4.1-Flash 1664、Kimi K3 1658、Qwen3.8-Max 1670）。
  · 2800 亿 ÷ 140 亿 ≈ 20，即每 token 约 1/20 的总参参与计算（本文算术）。

二、商汤 SenseNova U1.6
  · 2026-11-24 发布并开源，参数规模 8B，8B-MoT 架构，Apache-2.0；
    权重开放至 GitHub（OpenSenseNova/SenseNova-U1）、Hugging Face
    （sensenova/SenseNova-U1.6-8B-MoT）、ModelScope，同步接入 ComfyUI。
  · 延续 U 系列"理解与生成统一"范式；首次为该系列 8B 开源模型引入原生图像自修正。
  · 自修正流程：生成首稿 → 对照原始提示词检查画面 → 针对文字模糊、错字乱码、
    英文拼写错误、编号错乱提出修改意见 → 结合原提示与首稿输出修正版。
  · 商汤自测：开启自修正后 UltraTextBench 密集信息图由 86.04 升至 92.28
    （相对提升约 7%）；内部用户评测美学得分较 U1.5 Lite 高约 10%。

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
    """三个数字"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "2800 亿总参，只用二十分之一",
           "MoE 的三个数字各自管一件事，凑齐才成立")

    stats = [
        ("2800 亿", "总参数", "决定能力上限，也决定权重有多大", NAVY, 0.055),
        ("140 亿", "每 token 激活", "决定跑得快不快", RED, 0.372),
        ("100 万", "上下文 token", "决定一次能吃多少", TEAL, 0.689),
    ]
    for big, label, desc, color, x in stats:
        card(ax, x, 0.400, 0.258, 0.330, color, lw=1.5)
        ax.text(x + 0.020, 0.688, label, fontsize=9.6, color=GRAY,
                ha="left", va="center", zorder=6)
        ax.text(x + 0.020, 0.600, big, fontsize=27, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(x + 0.020, 0.478, desc, fontsize=9.0, color=SLATE,
                ha="left", va="center", zorder=6)

    # 比例条
    ax.text(0.055, 0.352, "每 token 实际参与计算的权重（140 亿 / 2800 亿 ≈ 1/20）",
            fontsize=9.6, color=DARK, ha="left", va="center")
    ax.add_patch(Rectangle((0.055, 0.300), 0.890, 0.034,
                           facecolor=LIGHT, edgecolor=LIGHT,
                           linewidth=0, zorder=3))
    ax.add_patch(Rectangle((0.055, 0.300), 0.890 / 20.0, 0.034,
                           facecolor=RED, edgecolor=RED,
                           linewidth=0, zorder=4))
    ax.text(0.962, 0.317, "1/20", fontsize=9.4, color=RED, weight="bold",
            ha="right", va="center", zorder=6)

    ax.text(0.055, 0.252,
            "总参 2800 亿、激活 140 亿是官方口径；1/20 为本文按两数相除计算，"
            "不是官方表述。",
            fontsize=9.0, color=SLATE, ha="left", va="center")

    card(ax, 0.055, 0.148, 0.890, 0.062, LIGHT, face=PALE, lw=1.0)
    ax.text(0.077, 0.179,
            "11 月 11 日发布，11 月 24 日以 Apache 2.0 正式开源，权重上架 Hugging Face 与 ModelScope。",
            fontsize=9.2, color=DARK, ha="left", va="center", zorder=6)

    punchline(fig, "三个数一起看才是可商用基线：够大、够快、够能装。")
    footer(fig, "事实来源：ERNIE 官方发布页（2026-11-11）；IT 之家 2026-11-24（经新浪科技转载）")
    fig.savefig(OUT + "图1_三个数字.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """自修正三步"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "生成 → 检查 → 修正，都在一次创作里",
           "SenseNova U1.6 的原生图像自修正：8B，同一个模型闭环")

    steps = [
        ("① 首稿", "按原始提示生成一张完整画面", NAVY, 0.048),
        ("② 检查", "对照原始提示词检查画面文字", SLATE, 0.372),
        ("③ 修正", "结合原提示与首稿输出修正版", RED, 0.696),
    ]
    for title, desc, color, x in steps:
        card(ax, x, 0.520, 0.248, 0.240, color, lw=1.5)
        ax.text(x + 0.018, 0.712, title, fontsize=11.4, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(x + 0.018, 0.600, desc, fontsize=9.2, color=DARK,
                ha="left", va="center", zorder=6, wrap=True)

    for x0 in (0.296, 0.620):
        ax.add_patch(FancyArrowPatch((x0 + 0.004, 0.640), (x0 + 0.072, 0.640),
                                     arrowstyle="-|>", mutation_scale=16,
                                     color=GRAY, linewidth=1.4, zorder=5))

    ax.text(0.048, 0.462, "检查环节能定位的文字问题", fontsize=9.6,
            color=GRAY, ha="left", va="center")
    ax.plot([0.048, 0.952], [0.444, 0.444], color=LIGHT, linewidth=1.0)

    items = ["错字", "乱码", "英文拼写错误", "编号错乱"]
    n = len(items)
    gap = 0.020
    w = (0.904 - (n - 1) * gap) / n
    x = 0.048
    for it in items:
        card(ax, x, 0.372, w, 0.048, GRAY, face=PALE, lw=0.9)
        ax.text(x + w / 2, 0.396, it, fontsize=9.4, color=DARK,
                ha="center", va="center", zorder=6)
        x += w + gap

    # 数据
    ax.text(0.048, 0.318, "UltraTextBench 密集信息图（商汤自测）", fontsize=9.6,
            color=GRAY, ha="left", va="center")
    ax.plot([0.048, 0.952], [0.300, 0.300], color=LIGHT, linewidth=1.0)

    rows = [
        ("单次生成", 86.04, SLATE),
        ("开启自修正", 92.28, RED),
    ]
    y = 0.248
    for label, val, color in rows:
        ax.text(0.048, y, label, fontsize=9.6, color=DARK,
                ha="left", va="center")
        w = 0.560 * val / 100.0
        ax.add_patch(Rectangle((0.230, y - 0.017), w, 0.034,
                               facecolor=color, edgecolor=color,
                               linewidth=0, alpha=0.88, zorder=4))
        ax.text(0.230 + w + 0.010, y, f"{val:.2f}", fontsize=10.0,
                color=color, weight="bold", ha="left", va="center", zorder=6)
        y -= 0.062

    ax.text(0.048, 0.148, "相对提升约 7%；厂商自测口径，未见第三方复现。",
            fontsize=8.8, color=SLATE, ha="left", va="center")

    punchline(fig, "它优化的不是画得更好看，是画出来的字对不对。")
    footer(fig, "事实来源：商汤日日新官网 U1.6 Lite 产品页；GitHub OpenSenseNova/SenseNova-U1；"
                "多家 2026-11-24 报道（UltraTextBench 86.04 → 92.28）")
    fig.savefig(OUT + "图2_自修正三步.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """两条路径"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "同一天，两种说服方式",
           "一个把基础做宽，一个把一处做穿")

    card(ax, 0.048, 0.360, 0.430, 0.400, NAVY, lw=1.6)
    ax.text(0.072, 0.712, "文心 5.5 Flash Preview", fontsize=12.0,
            color=NAVY, weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.072, 0.678, "百度 · 2800 亿总参", fontsize=9.4, color=GRAY,
            ha="left", va="center", zorder=6)
    rows_l = [
        ("Apache 2.0", "可直接商用"),
        ("Hugging Face / ModelScope", "权重双平台"),
        ("vLLM / SGLang", "主流框架支持"),
        ("100 万 token", "上下文"),
    ]
    y = 0.610
    for k, v in rows_l:
        ax.text(0.072, y, k, fontsize=9.4, color=DARK,
                ha="left", va="center", zorder=6)
        ax.text(0.455, y, v, fontsize=8.8, color=SLATE,
                ha="right", va="center", zorder=6)
        y -= 0.058
    ax.text(0.072, 0.392, "目标：成为默认选它不会错的基础模型", fontsize=9.2,
            color=NAVY, ha="left", va="center", zorder=6)

    card(ax, 0.522, 0.360, 0.430, 0.400, RED, lw=1.6)
    ax.text(0.546, 0.712, "SenseNova U1.6", fontsize=12.0,
            color=RED, weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.546, 0.678, "商汤 · 8B", fontsize=9.4, color=GRAY,
            ha="left", va="center", zorder=6)
    rows_r = [
        ("8B-MoT", "理解与生成统一"),
        ("原生自修正", "首稿→检查→修正"),
        ("UltraTextBench", "86.04 → 92.28"),
        ("ComfyUI / GitHub", "同步接入"),
    ]
    y = 0.610
    for k, v in rows_r:
        ax.text(0.546, y, k, fontsize=9.4, color=DARK,
                ha="left", va="center", zorder=6)
        ax.text(0.929, y, v, fontsize=8.8, color=SLATE,
                ha="right", va="center", zorder=6)
        y -= 0.058
    ax.text(0.546, 0.392, "目标：在信息图这一处做到别人替代不了", fontsize=9.2,
            color=RED, ha="left", va="center", zorder=6)

    ax.text(0.048, 0.300,
            "选型的三个问题也随之变了：许可能不能商用、框架认不认、在具体场景里是不是真的更好。",
            fontsize=9.8, color=DARK, ha="left", va="center")
    ax.text(0.048, 0.256,
            "前两个问许可与工具链，第三个只能靠实测——两家给出的答案不在同一个维度上。",
            fontsize=9.4, color=SLATE, ha="left", va="center")

    punchline(fig, "参数竞赛没有结束，但它不再是唯一分界线。")
    footer(fig, "事实来源：ERNIE 官方发布页；IT 之家 2026-11-24；商汤日日新官网与 GitHub；"
                "UltraTextBench 数字为商汤自测口径")
    fig.savefig(OUT + "图3_两条路径.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)


