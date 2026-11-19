# -*- coding: utf-8 -*-
"""
《腾讯、范式、商汤同日开源：发布即适配国产算力正在成为默认节奏》配套图表
事实口径（2026-11-19，逐条核对官方公告与公开报道后）：
  · 腾讯混元 Hy4 flash：11 月 16 日发布，11 月 18 日开源三个权重——Hy4 flash（指令微调）、
    Hy4 flash-FP8（8 位量化）、Hy4 flash Base（预训练基础）；GitHub / Hugging Face /
    ModelScope / GitCode 均可下载；总参 224B（含 64B Engram），每 token 激活 12B，
    支持多模态输入与 100 万 token 上下文；官方称正在加速开源 Hy4
    （IT之家 11-18、Hugging Face 模型卡、腾讯新闻 11-18）；
  · 范式智能（原第四范式，6682.HK）11 月 18 日发布 Phai 系列两款：Phai-A1（通用语言模型，
    原生百万级上下文，单张 RTX 3090 可跑，同卡下较 Qwen 27B 快约 8—10 倍）、
    Phai-M1（真人影视向视频生成，约 3 分钟出 15 秒 720P）；两款均在华为昇腾平台完成
    全流程国产算力训练优化；官方口径为「近期将在 Hugging Face 与 ModelScope 开放权重」，
    截至本文发稿权重尚未上线（范式官方新闻稿 11-18、极客公园 11-18、量子位 11-19、第一财经 11-18）；
  · 商汤 SenseNova Loop-9B：11 月 17 日发布并开源权重（Loop 结构复用层参数 + 流形约束
    超连接），约 9B 参数，4bit 量化后权重约 4.9GB、部署显存可低至 10GB 内；
    11 月 18 日补充 AWQ 与 GGUF 权重（商汤官网、GitHub README）；
  · Day 0 适配：沐曦 11 月 17 日率先完成（第一财经 11-17）、寒武纪 Day 0 完成并打通
    循环计算架构推理链路（IT之家 11-18）、海光 DCU 11 月 18 日完成（新浪财经 11-18）、
    曦智科技天枢光电智能计算卡 Day 0 深度适配（曦智科技 11-18）。
风格：克制传媒风，白底、低饱和配色、标题即结论。输出目录 = 脚本所在目录。
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False

NAVY = "#1f3a5f"
RED = "#b5544a"
GRAY = "#8a8f98"
SLATE = "#5f6673"
LIGHT = "#d8dbe0"
DARK = "#2b2f36"
PALE = "#eef0f3"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep


def base(title, sub):
    fig = plt.figure(figsize=(12, 6.8))
    fig.patch.set_facecolor("white")
    fig.text(0.045, 0.950, title, fontsize=20, color=DARK, weight="bold",
             ha="left", va="top")
    fig.text(0.045, 0.876, sub, fontsize=10.4, color=GRAY, ha="left", va="top")
    return fig


def footer(fig, text):
    fig.text(0.045, 0.014, text, fontsize=8.2, color=GRAY, ha="left", va="center")


def punchline(fig, text, y=0.078):
    fig.text(0.045, y, text, fontsize=10.8, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.6", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


# ------------------------------------------------------------------ 图 1
def fig1():
    fig = base("三家公司，落在同一张日历上",
               "2026 年 11 月 16—18 日｜发布、放权重、适配，被压进了 72 小时")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    cols = [0.252, 0.496, 0.740]
    heads = ["11 月 16 日", "11 月 17 日", "11 月 18 日"]
    for x, h in zip(cols, heads):
        ax.text(x + 0.112, 0.818, h, fontsize=9.6, color=GRAY, weight="bold",
                ha="center", va="center")
        ax.plot([x, x + 0.224], [0.788, 0.788], color=LIGHT, linewidth=0.9)

    rows = [
        (0.688, "腾讯混元", "Hy4 flash"),
        (0.455, "范式智能", "Phai 系列"),
        (0.222, "商汤科技", "Loop-9B"),
    ]
    for y, company, family in rows:
        ax.text(0.030, y + 0.052, company, fontsize=11.2, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(0.030, y + 0.006, family, fontsize=8.6, color=GRAY, ha="left",
                va="center")

    cells = [
        (0, 0, "发布 Hy4 flash", NAVY, True),
        (0, 2, "三版权重开源\nGitHub / HF / ModelScope / GitCode", RED, True),
        (1, 2, "Phai-A1、Phai-M1 发布\n昇腾全流程训练；权重「近期」开放", RED, False),
        (2, 1, "Loop-9B 发布并开源\n沐曦当日完成 Day 0 适配", RED, True),
        (2, 2, "寒武纪、海光、曦智\n适配陆续到位", SLATE, True),
    ]

    for r, c, text, color, filled in cells:
        y = rows[r][0]
        x = cols[c]
        if filled:
            ax.add_patch(FancyBboxPatch((x, y - 0.074), 0.224, 0.152,
                                        boxstyle="round,pad=0.006",
                                        facecolor=PALE, edgecolor="none"))
        ax.text(x + 0.014, y + 0.002, text, fontsize=8.4, color=color,
                ha="left", va="center", linespacing=1.9)

    ax.plot([0.030, 0.960], [0.112, 0.112], color=LIGHT, linewidth=0.9)
    ax.text(0.030, 0.072,
            "唯一还没放权重的是范式：官方说「近期」在 Hugging Face 与 ModelScope 开放。",
            fontsize=9.0, color=SLATE, ha="left", va="center")

    punchline(fig, "发布到权重上线，腾讯用了两天；到芯片适配，商汤用了当天。")
    footer(fig, "事实：IT之家 11-18、Hugging Face 模型卡、范式官方新闻稿 11-18、"
                "商汤官网与 GitHub README、第一财经 11-17｜制图：本文")
    fig.savefig(OUT + "图1_同一张日历.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("Loop-9B 开源之后，四家国产芯片陆续说自己跑通了",
               "从 11 月 17 日发布当天开始，GPU、DCU、光子计算卡各自完成推理适配")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    cards = [
        ("沐曦", "GPU", "11 月 17 日", "当日完成，四家里最早", RED),
        ("寒武纪", "AI 芯片", "Day 0", "打通循环计算架构推理链路", NAVY),
        ("海光", "DCU", "11 月 18 日", "完成推理适配", NAVY),
        ("曦智科技", "光子计算卡", "Day 0", "天枢卡深度适配", NAVY),
    ]

    for i, (name, kind, when, note, color) in enumerate(cards):
        x = 0.030 + i * 0.238
        ax.add_patch(FancyBboxPatch((x, 0.330), 0.215, 0.430,
                                    boxstyle="round,pad=0.010",
                                    facecolor="white", edgecolor=LIGHT,
                                    linewidth=1.0))
        ax.add_patch(Rectangle((x, 0.752), 0.215, 0.006, facecolor=color,
                               edgecolor="none"))
        ax.text(x + 0.022, 0.690, name, fontsize=14.0, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(x + 0.022, 0.632, kind, fontsize=8.6, color=GRAY, ha="left",
                va="center")
        ax.plot([x + 0.022, x + 0.193], [0.590, 0.590], color=LIGHT, lw=0.8)
        ax.text(x + 0.022, 0.536, when, fontsize=9.6, color=color,
                weight="bold", ha="left", va="center")
        ax.text(x + 0.022, 0.430, note, fontsize=8.4, color=SLATE, ha="left",
                va="center", linespacing=1.8)

    ax.text(0.030, 0.240,
            "Loop-9B 约 9B 参数，4bit 量化后权重约 4.9GB，部署显存可低至 10GB 内——"
            "这是四家芯片都能在当天给出结论的前提。",
            fontsize=9.2, color=SLATE, ha="left", va="center")
    ax.text(0.030, 0.170,
            "适配的语义也因此变了：不是「能不能跑」，是「开源当天就有一个可用的后端」。",
            fontsize=9.2, color=SLATE, ha="left", va="center")

    punchline(fig, "没有谁在排队等安排，四家都在抢第一个说「我们跑通了」。")
    footer(fig, "事实：沐曦据第一财经 11-17，寒武纪据 IT之家 11-18，海光据新浪财经 11-18，"
                "曦智据其 11-18 发布；Loop-9B 参数与显存据商汤官网｜制图：本文")
    fig.savefig(OUT + "图2_四家芯片的Day0.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("三款模型，把「跑得起来」的门槛压到同一档",
               "参数规模不一样，但都指向一件事：一张卡、十来个 G 显存、本地可部署")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    items = [
        ("Hy4 flash", "腾讯混元", "12B", "每 token 激活参数",
         "总参 224B（含 64B Engram），100 万 token 上下文", NAVY),
        ("Loop-9B", "商汤科技", "10GB", "部署显存上限",
         "约 9B 参数，4bit 量化后权重约 4.9GB", RED),
        ("Phai-A1", "范式智能", "1 张", "RTX 3090 即可运行",
         "同卡条件下较 Qwen 27B 快约 8—10 倍，百万级上下文", NAVY),
    ]

    for i, (name, owner, big, unit, note, color) in enumerate(items):
        y = 0.700 - i * 0.215
        ax.text(0.030, y + 0.048, name, fontsize=12.6, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(0.030, y - 0.004, owner, fontsize=8.4, color=GRAY, ha="left",
                va="center")
        ax.text(0.300, y + 0.038, big, fontsize=22.0, color=color,
                weight="bold", ha="left", va="center")
        ax.text(0.300, y - 0.014, unit, fontsize=8.4, color=GRAY, ha="left",
                va="center")
        ax.text(0.520, y + 0.030, note, fontsize=9.2, color=SLATE, ha="left",
                va="center")
        ax.plot([0.030, 0.960], [y - 0.072, y - 0.072], color=LIGHT,
                linewidth=0.8)

    ax.text(0.030, 0.130,
            "三家的数字口径不同：腾讯讲激活参数，商汤讲显存占用，范式讲同卡速度。"
            "但它们指向的方向一致——把部署成本压到一台机器能承担。",
            fontsize=9.0, color=SLATE, ha="left", va="center")

    punchline(fig, "开源模型的价值，正在从「榜上多少分」转向「在谁的卡上跑得动」。")
    footer(fig, "事实：三款模型的参数、显存与速度均为各自官方口径，口径并不统一，"
                "不可直接横向比较｜制图：本文")
    fig.savefig(OUT + "图3_门槛压到同一档.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)
