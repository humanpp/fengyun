# -*- coding: utf-8 -*-
"""
《腾讯770B大模型全量开源，还附一份安全审计卡：开源不再只拼参数了》配套图表

事实口径（全部来自公开披露）：
  · 腾讯混元 Hy4 于 2026-11-20 开源权重，三个检查点上架 Hugging Face、
    ModelScope、GitCode：Hy4（指令微调，约 1.55TB）、Hy4-FP8（8bit 量化，
    约 0.79TB）、Hy4-base（预训练基座，约 1.54TB），合计约 3.9TB。
  · 规格：总参数 770B，每 token 激活 49B；78 层，首层为标准 FFN，其余 77 层
    为 MoE，每层 256 个路由专家 + 1 个共享专家，每 token 激活 top-8；
    主干外置 DFly2 草稿模型 3.3B 支持投机解码；上下文 100 万 token；
    支持文本、图像、视频理解。据 Hugging Face tencent/Hy4 README_CN。
  · Hy4 于 2026-11-04 API 首发，当时即预告"将于近期开源模型权重，
    发布模型系统卡片"。据腾讯官网 2026-11-04。
  · Hy4 flash：总参数 224B（含 64B Engram 参数），每 token 激活 12B，
    支持多模态与 100 万 token 上下文；权重 2026-11-17 先行放出。
    据腾讯官网 2026-11-16、科技日报 2026-11-16。
  · System Card（hy.tencent.ai/Hy4_system_card.pdf）：披露网络安全、生物安全
    等维度评估；训练数据仅纳入 PoC 生成、漏洞修复等防守性网络安全内容，
    剔除漏洞利用、逆向工程、渗透等攻击性数据；腾讯玄武实验室与科恩实验室
    审计未发现明显的进攻性能力风险。两家均为腾讯自有安全团队，
    属厂商内部评估，非第三方独立认证。据 IT之家 2026-11-20。
  · 许可证为 Tencent Hy License 1.0：LICENSE 首段载明
    "This License is not the Apache License, Version 2.0"，其派生自
    Apache 2.0；前 9 条基本沿用，第 10 条对 MaaS 运营者设门槛——
    连续 12 个月全球总营收超过 5000 万美元，或该模型用于月活跃用户超过
    1 亿的产品或服务，须另行取得腾讯书面授权；纯内部使用豁免；
    微调、量化、蒸馏、合并、剪枝版本计为衍生作品，同受约束。
    仅 Hy4 preview（2026-08-28）为 Apache 2.0。
    据 Hugging Face tencent/Hy4 与 tencent/Hy4-flash 的 LICENSE 原文，
    及鏈新聞 ABMedia、鉅亨網、ModelBrief、Daily Inference 2026-11-20 报道。
  · 模型卡基准表仅 6 行（MMLU 91.6、MMLU-Pro 73.9、SuperGPQA 62.7、
    SimpleQA 57.2、U-MATH 71.6、MBPP-plus 74.0），测的是 Hy4 Base 基座版、
    few-shot 且为腾讯自报。

风格：克制传媒风，白底、低饱和配色、标题即结论
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
BLUSH = "#fbf1ef"

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
    fig = plt.figure(figsize=(12, 6.8))
    ax = new_axes(fig)

    header(fig, "770B，每个 token 只激活 49B",
           "稀疏架构让体量和成本脱钩；这次放出来的不是一个模型，是三个检查点")

    # 左：规格
    ax.text(0.050, 0.742, "模型规格", fontsize=10.0, color=GRAY,
            ha="left", va="center")
    ax.plot([0.050, 0.470], [0.712, 0.712], color=LIGHT, linewidth=1.0)

    rows = [
        ("总参数", "770B", NAVY, True),
        ("每 token 激活", "49B", RED, True),
        ("层数", "78（首层 FFN，其余 77 层 MoE）", DARK, False),
        ("每层专家", "256 路由 + 1 共享，激活 top-8", DARK, False),
        ("上下文", "100 万 token", DARK, False),
        ("输入", "文本 · 图像 · 视频", DARK, False),
    ]
    y = 0.640
    for label, value, color, big in rows:
        ax.text(0.050, y, label, fontsize=9.8, color=GRAY,
                ha="left", va="center")
        ax.text(0.205, y, value,
                fontsize=16.0 if big else 10.2,
                color=color, weight="bold" if big else "normal",
                ha="left", va="center")
        y -= 0.083 if big else 0.070

    # 右：三个检查点
    ax.text(0.560, 0.742, "三个检查点", fontsize=10.0, color=GRAY,
            ha="left", va="center")
    ax.plot([0.560, 0.950], [0.712, 0.712], color=LIGHT, linewidth=1.0)

    ckpts = [
        ("Hy4", 1.55, NAVY, "指令微调版"),
        ("Hy4-FP8", 0.79, SLATE, "8bit 量化版"),
        ("Hy4-base", 1.54, NAVY, "预训练基座"),
    ]
    scale = 0.150 / 1.55
    y = 0.610
    for name, size, color, note in ckpts:
        ax.text(0.560, y + 0.040, name, fontsize=10.6, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(0.560, y + 0.006, note, fontsize=8.8, color=GRAY,
                ha="left", va="center")
        ax.add_patch(Rectangle((0.700, y - 0.004), size * scale, 0.030,
                               facecolor=color, edgecolor=color,
                               linewidth=0, zorder=4, alpha=0.88))
        ax.text(0.700 + size * scale + 0.012, y + 0.011, f"{size:.2f} TB",
                fontsize=9.6, color=SLATE, ha="left", va="center")
        y -= 0.118

    ax.text(0.560, 0.238, "合计约 3.9TB；另有社区 GGUF 版本", fontsize=9.4,
            color=SLATE, ha="left", va="center")

    ax.text(0.050, 0.185,
            "同系列的 Hy4 flash 更早一步：11 月 17 日已放出权重，"
            "总参数 224B（含 64B Engram），激活 12B。",
            fontsize=9.4, color=SLATE, ha="left", va="center")

    punchline(fig, "参数是名片，激活参数才是账单。")
    footer(fig, "事实来源：Hugging Face tencent/Hy4 模型卡；IT之家 2026-11-20；腾讯官网 2026-11-16")
    fig.savefig(OUT + "图1_770B的规格.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(12, 6.8))
    ax = new_axes(fig)

    header(fig, "训练数据里，只留下防守的那一半",
           "System Card 把“模型能干什么”写成了一份可以引用的文件")

    # 左：保留
    card(ax, 0.045, 0.300, 0.435, 0.420, NAVY, lw=1.3)
    ax.text(0.070, 0.660, "纳入", fontsize=11.0, color=GRAY,
            ha="left", va="center", zorder=6)
    ax.text(0.070, 0.596, "防守型网络安全内容", fontsize=15.0, color=NAVY,
            weight="bold", ha="left", va="center", zorder=6)
    ax.plot([0.070, 0.455], [0.556, 0.556], color=NAVY, linewidth=0.9,
            alpha=0.35, zorder=5)
    ax.text(0.070, 0.480, "· PoC 生成", fontsize=12.0, color=DARK,
            ha="left", va="center", zorder=6)
    ax.text(0.070, 0.400, "· 漏洞修复", fontsize=12.0, color=DARK,
            ha="left", va="center", zorder=6)

    # 右：剔除
    card(ax, 0.520, 0.300, 0.435, 0.420, RED, face=BLUSH, lw=1.5)
    ax.text(0.545, 0.660, "剔除", fontsize=11.0, color=GRAY,
            ha="left", va="center", zorder=6)
    ax.text(0.545, 0.596, "攻击性数据", fontsize=15.0, color=RED,
            weight="bold", ha="left", va="center", zorder=6)
    ax.plot([0.545, 0.930], [0.556, 0.556], color=RED, linewidth=0.9,
            alpha=0.35, zorder=5)
    for i, item in enumerate(["· 漏洞利用", "· 逆向工程", "· 渗透测试"]):
        ax.text(0.545, 0.492 - i * 0.072, item, fontsize=12.0, color=RED,
                ha="left", va="center", zorder=6)

    # 审计条
    card(ax, 0.045, 0.215, 0.910, 0.058, LIGHT, face=PALE, lw=1.0)
    ax.text(0.068, 0.244, "审计：腾讯玄武实验室 · 科恩实验室", fontsize=10.2,
            color=DARK, ha="left", va="center", zorder=6)
    ax.text(0.470, 0.244, "→  未发现明显的进攻性能力风险", fontsize=10.2,
            color=NAVY, weight="bold", ha="left", va="center", zorder=6)

    ax.text(0.045, 0.160,
            "但两家都是腾讯自有安全团队，属厂商内部评估，不是第三方独立认证。",
            fontsize=9.4, color=SLATE, ha="left", va="center")

    punchline(fig, "先划出边界，再谈开源。")
    footer(fig, "事实来源：腾讯混元 Hy4 模型安全评估卡片（System Card）；IT之家 2026-11-20")
    fig.savefig(OUT + "图2_安全卡留了什么.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "权重免费下载，规模使用要谈",
           "Hy4 用的是 Tencent Hy License 1.0，不是 Apache 2.0；门槛写在第 10 条")

    # 左：不受限
    card(ax, 0.045, 0.250, 0.435, 0.470, NAVY, lw=1.3)
    ax.text(0.070, 0.672, "第 10 条之外", fontsize=10.0, color=GRAY,
            ha="left", va="center", zorder=6)
    ax.text(0.070, 0.612, "不受此条限制", fontsize=14.0, color=NAVY,
            weight="bold", ha="left", va="center", zorder=6)
    ax.plot([0.070, 0.455], [0.576, 0.576], color=NAVY, linewidth=0.9,
            alpha=0.35, zorder=5)
    left_items = [
        "个人与小团队常规使用",
        "纯内部使用，模型与输出\n不提供给第三方",
        "只在特定功能内使用的\n终端产品，不算 MaaS",
    ]
    y = 0.514
    for item in left_items:
        ax.text(0.070, y, item, fontsize=9.6, color=DARK,
                ha="left", va="top", linespacing=1.60, zorder=6)
        y -= 0.055 if "\n" not in item else 0.092

    # 右：须授权
    card(ax, 0.520, 0.250, 0.435, 0.470, RED, face=BLUSH, lw=1.6)
    ax.text(0.545, 0.672, "第 10 条", fontsize=10.0, color=GRAY,
            ha="left", va="center", zorder=6)
    ax.text(0.545, 0.612, "须先取得腾讯书面授权", fontsize=14.0, color=RED,
            weight="bold", ha="left", va="center", zorder=6)
    ax.plot([0.545, 0.930], [0.576, 0.576], color=RED, linewidth=0.9,
            alpha=0.35, zorder=5)
    ax.text(0.545, 0.532, "经营 MaaS（通过 API 让第三方\n远程调用推理或微调），且：",
            fontsize=9.6, color=DARK, ha="left", va="top",
            linespacing=1.60, zorder=6)
    ax.text(0.545, 0.436, "连续 12 个月全球总营收\n超过 5000 万美元", fontsize=10.0,
            color=RED, weight="bold", ha="left", va="top",
            linespacing=1.55, zorder=6)
    ax.text(0.545, 0.352, "或  该模型用于月活跃用户\n超过 1 亿的产品或服务",
            fontsize=10.0, color=RED, weight="bold", ha="left", va="top",
            linespacing=1.55, zorder=6)

    ax.text(0.045, 0.186,
            "微调、量化、蒸馏、合并、剪枝的版本均计为衍生作品，同受本条约束；"
            "仅 8 月的 Hy4 preview 是 Apache 2.0。",
            fontsize=9.4, color=SLATE, ha="left", va="center")

    punchline(fig, "许可以前是背景板，现在成了规格书。")
    footer(fig, "事实来源：Hugging Face tencent/Hy4 LICENSE（Tencent Hy License 1.0）原文；"
                "鏈新聞、鉅亨網、ModelBrief 2026-11-20")
    fig.savefig(OUT + "图3_许可第10条.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)