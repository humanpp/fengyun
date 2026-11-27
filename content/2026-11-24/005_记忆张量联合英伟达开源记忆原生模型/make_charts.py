# -*- coding: utf-8 -*-
"""
《554B 参数、59B 激活，记忆张量联合英伟达开源"记忆原生"模型》配套图表

事实口径：
  · MemT-1.0-Pro：554B 总参 / 59B 激活，底座 NVIDIA-Nemotron-3-Ultra-550B-A55B，
    Megatron-Core 与 Megatron Bridge 支撑分布式训练（第一财经 2026-11-23、钛媒体）。
  · 家族：Nano 36B / 3B，Flash 288B / 17B（MemTensor 官方模型页 memt.memtensor.cn）。
  · 论文 arXiv:2610.26825《MemT-1.0: Towards Memory-Native Evolution》：记忆模块与注意力
    并行插入选定层，Gated DeltaNet-2 逐 token 更新，Mixture-of-Storage 扩容量；
    128K 历史下 Nano 端到端推理约 1.86 倍加速、持久化存储较全上下文 KV cache 减少 66 倍；
    平均超过参数记忆基线、与检索增强方法持平。
  · 蚂蚁 LingSante：air-VL 124B / 激活 5.5B、flash 560B（1M 上下文）、Pulse 150 余项疾病
    六年风险、MedGuard 安全防护（界面新闻 2026-11-23）。
  · 大晓 ACE-Brain-0.7：9B，六基准均分 76.5，GPT-6 Astra 72.7、Claude Opus 5.5 73.5
    （arXiv:2611.26519）。

风格：克制传媒风，编辑排版
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
plt.rcParams["savefig.facecolor"] = "white"

INK = "#1a2332"
NAVY = "#1b3a5c"
RED = "#b0413e"
TEAL = "#2f6b64"
GOLD = "#9a7b3f"
MUTED = "#7b8494"
HAIR = "#dfe3e8"
WASH = "#f4f6f8"
WHITE = "#ffffff"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep


def new_axes(fig):
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return ax


def head(fig, ax, kicker, title, sub, color):
    ax.add_patch(Rectangle((0.042, 0.928), 0.0075, 0.040,
                           facecolor=color, edgecolor="none", zorder=9))
    ax.text(0.058, 0.950, kicker, fontsize=9.2, color=color,
            weight="bold", ha="left", va="center", zorder=9)
    ax.text(0.042, 0.900, title, fontsize=21, color=INK, weight="bold",
            ha="left", va="top", zorder=9)
    ax.text(0.042, 0.848, sub, fontsize=10.4, color=MUTED,
            ha="left", va="top", zorder=9)
    ax.plot([0.042, 0.958], [0.812, 0.812], color=HAIR, linewidth=1.0,
            zorder=5)


def foot(fig, ax, text):
    ax.plot([0.042, 0.958], [0.058, 0.058], color=HAIR, linewidth=0.9,
            zorder=5)
    ax.text(0.042, 0.032, text, fontsize=7.0, color=MUTED,
            ha="left", va="center", zorder=9)


def outro(fig, ax, text, color=INK, width=0.760):
    ax.add_patch(FancyBboxPatch(
        (0.042, 0.082), width, 0.048,
        boxstyle="round,pad=0.002,rounding_size=0.008",
        facecolor=color, edgecolor="none", zorder=6))
    ax.text(0.062, 0.106, text, fontsize=10.2, color=WHITE,
            ha="left", va="center", zorder=9)


def arrow(ax, x1, x2, y, color="#c3cad3"):
    ax.annotate("", xy=(x2, y), xytext=(x1, y),
                arrowprops=dict(arrowstyle="-|>", color=color, linewidth=1.6,
                                shrinkA=0, shrinkB=0))


# ---------------------------------------------------------------- 图 1
def fig1():
    rows = [
        ("Nemotron 3 Ultra", "记忆张量接入的底座", 550, 55, MUTED),
        ("MemT-1.0-Pro", "550 + 4　·　55 + 4", 554, 59, NAVY),
        ("MemT-1.0-Flash", "同一套机制，中尺寸", 288, 17, TEAL),
        ("MemT-1.0-Nano", "同一套机制，最小尺寸", 36, 3, GOLD),
    ]

    fig = plt.figure(figsize=(13.6, 8.0))
    ax = new_axes(fig)

    head(fig, ax,
         "2026.11.23  同一套机制，四个尺寸",
         "同一个底座，两头各加 4B",
         "总参数与激活参数（十亿，B）",
         NAVY)

    x0, span, vmax = 0.300, 0.520, 600.0
    ys = [0.700, 0.566, 0.432, 0.298]
    h, gap = 0.028, 0.008

    for (name, tag, total, act, color), y in zip(rows, ys):
        ax.text(x0 - 0.020, y + 0.012, name, fontsize=12.0, color=INK,
                weight="bold", ha="right", va="center", zorder=9)
        ax.text(x0 - 0.020, y - 0.020, tag, fontsize=8.6, color=MUTED,
                ha="right", va="center", zorder=9)

        ax.add_patch(Rectangle((x0, y + gap / 2), total / vmax * span, h,
                               facecolor=color, edgecolor="none", zorder=6))
        ax.add_patch(Rectangle((x0, y - gap / 2 - h), act / vmax * span, h,
                               facecolor=RED, alpha=0.85, edgecolor="none",
                               zorder=6))
        ax.text(x0 + total / vmax * span + 0.010, y + gap / 2 + h / 2,
                "%d" % total, fontsize=10.0, color=color, weight="bold",
                ha="left", va="center", zorder=9)
        ax.text(x0 + act / vmax * span + 0.010, y - gap / 2 - h / 2,
                "%d" % act, fontsize=10.0, color=RED, weight="bold",
                ha="left", va="center", zorder=9)

    ax.plot([x0, x0], [0.760, 0.256], color=HAIR, linewidth=1.0, zorder=4)

    ax.add_patch(Rectangle((0.780, 0.792), 0.016, 0.013, facecolor=NAVY,
                           edgecolor="none", zorder=9))
    ax.text(0.802, 0.798, "总参数", fontsize=8.6, color=MUTED, ha="left",
            va="center", zorder=9)
    ax.add_patch(Rectangle((0.880, 0.792), 0.016, 0.013, facecolor=RED,
                           edgecolor="none", zorder=9))
    ax.text(0.902, 0.798, "激活参数", fontsize=8.6, color=MUTED, ha="left",
            va="center", zorder=9)

    ax.add_patch(FancyBboxPatch(
        (0.042, 0.168), 0.916, 0.058,
        boxstyle="round,pad=0,rounding_size=0.008",
        facecolor=WASH, edgecolor="none", zorder=3))
    ax.text(0.062, 0.197,
            "550 → 554、55 → 59：不是从零训一个 500B，是把记忆模块接到现成底座上，账单是 4B。",
            fontsize=8.8, color=INK, ha="left", va="center", zorder=9)

    outro(fig, ax, "Pro 与底座差 4B，与 Flash 差一个数量级的激活量。")
    foot(fig, ax, "数据来源：第一财经 2026-11-23、澎湃新闻 2026-11-23（Pro 554B／59B）；"
                  "MemTensor 官方模型页（Nano 36B／3B、Flash 288B／17B）；"
                  "底座口径 NVIDIA-Nemotron-3-Ultra-550B-A55B（钛媒体 2026-11-23 引官方仓库）。")
    fig.savefig(OUT + "图1_同一个底座多出4B.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(13.6, 8.0))
    ax = new_axes(fig)

    head(fig, ax,
         "记忆到底存在谁身上",
         "三条路，分岔点只有一处",
         "同一件事（让模型记住），三种放法",
         TEAL)

    rows = [
        ("上下文窗口", "最常见", NAVY,
         [("对话历史",), ("上下文窗口",), ("本轮结束即清空",)],
         "长度一涨，KV cache 跟着涨；窗口到期，记忆归零。"),
        ("外挂检索", "RAG", GOLD,
         [("文档与日志",), ("向量库",), ("召回后重读",)],
         "记忆在另一个系统里，模型每一轮都要重新读一遍。"),
        ("架构内记忆", "MemT 的走法", RED,
         [("注意力（层内）", "记忆模块（并行）"), ("读 → 写 → 更新",), ("下一轮接着用",)],
         "Gated DeltaNet-2 逐 token 更新状态，Mixture-of-Storage 撑容量。"),
    ]

    ys = [0.716, 0.500, 0.284]
    slots = [0.300, 0.500, 0.700]
    bw, bh = 0.172, 0.050

    for (name, tag, color, chain, note), y in zip(rows, ys):
        ax.text(0.042, y + 0.014, name, fontsize=13.0, color=color,
                weight="bold", ha="left", va="center", zorder=9)
        ax.text(0.042, y - 0.020, tag, fontsize=8.6, color=MUTED,
                ha="left", va="center", zorder=9)

        for i, cell in enumerate(chain):
            sx = slots[i]
            if len(cell) == 1:
                ax.add_patch(FancyBboxPatch(
                    (sx, y - bh / 2), bw, bh,
                    boxstyle="round,pad=0,rounding_size=0.006",
                    facecolor=WHITE, edgecolor=color, linewidth=1.2,
                    zorder=6))
                ax.text(sx + bw / 2, y, cell[0], fontsize=9.4, color=INK,
                        ha="center", va="center", zorder=9)
            else:
                for k, label in enumerate(cell):
                    by = y + 0.016 - k * 0.040
                    ax.add_patch(FancyBboxPatch(
                        (sx, by - 0.017), bw, 0.034,
                        boxstyle="round,pad=0,rounding_size=0.005",
                        facecolor=WHITE, edgecolor=color, linewidth=1.2,
                        zorder=6))
                    ax.text(sx + bw / 2, by, label, fontsize=9.0, color=INK,
                            ha="center", va="center", zorder=9)
            if i < len(chain) - 1:
                arrow(ax, sx + bw + 0.006, slots[i + 1] - 0.006, y)

        ax.text(0.300, y - 0.062, note, fontsize=8.8, color=MUTED,
                ha="left", va="center", zorder=9)

    outro(fig, ax, "前两条把记忆放在模型外面；第三条把它放进计算里。", width=0.700)
    foot(fig, ax, "结构示意据 arXiv:2610.26825（MemT-1.0）技术路线与厂商说明综合绘制；"
                  "图为原理示意，非实际张量布局；RAG 一路为通用做法归纳，不指向具体产品。")
    fig.savefig(OUT + "图2_记忆放在哪.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    cards = [
        ("记忆架构", "MemT-1.0-Pro", "记忆张量 × 英伟达", NAVY,
         [("规模", "554B 总参 · 59B 激活"),
          ("关键数", "128K 下 1.86× 加速\n存储较 KV cache 少 66×"),
          ("怎么评", "记忆任务 + 通用能力\n+ 智能体成功率"),
          ("落点", "让底座自己长出记忆")]),
        ("垂直专用", "蚂蚁百灵 LingSante", "蚂蚁阿福 · 医疗健康", GOLD,
         [("规模", "124B（激活 5.5B）\n与 560B 两款主力"),
          ("关键数", "150+ 种疾病\n未来六年风险预测"),
          ("怎么评", "影像报告、皮损识别\n报告解读等医疗评测"),
          ("落点", "一台笔记本能跑的医生")]),
        ("具身推理", "ACE-Brain-0.7", "大晓机器人 · 9B", TEAL,
         [("规模", "9B（Qwen3.5-9B 微调）"),
          ("关键数", "六基准均分 76.5\nAstra 72.7、Opus 5.5 73.5"),
          ("怎么评", "任务推理 + 空间定位\n+ 进度估计"),
          ("落点", "机器人读懂任务进度")]),
    ]

    fig = plt.figure(figsize=(13.6, 8.0))
    ax = new_axes(fig)

    head(fig, ax,
         "2026.11.23  同一天落地",
         "三条赛道，三套评分表",
         "参数不再是唯一的坐标轴",
         GOLD)

    w = 0.2853
    gap = 0.030
    x = 0.042

    for name, model, by, color, items in cards:
        ax.add_patch(FancyBboxPatch(
            (x, 0.212), w, 0.512,
            boxstyle="round,pad=0,rounding_size=0.010",
            facecolor=WHITE, edgecolor=HAIR, linewidth=1.2, zorder=4))
        ax.add_patch(Rectangle((x, 0.664), w, 0.060, facecolor=color,
                               edgecolor="none", zorder=6))
        ax.text(x + 0.018, 0.700, name, fontsize=11.6, color=WHITE,
                weight="bold", ha="left", va="center", zorder=9)
        ax.text(x + 0.018, 0.640, model, fontsize=9.6, color=INK,
                weight="bold", ha="left", va="center", zorder=9)
        ax.text(x + 0.018, 0.608, by, fontsize=8.0, color=MUTED,
                ha="left", va="center", zorder=9)
        ax.plot([x + 0.018, x + w - 0.018], [0.586, 0.586], color=HAIR,
                linewidth=1.0, zorder=5)

        yy = 0.532
        for label, value in items:
            ax.text(x + 0.018, yy, label, fontsize=7.6, color=color,
                    weight="bold", ha="left", va="center", zorder=9)
            ax.text(x + 0.018, yy - 0.032, value, fontsize=8.6, color=INK,
                    ha="left", va="center", zorder=9, linespacing=1.5)
            yy -= 0.086

        x += w + gap

    outro(fig, ax,
          "记忆往架构里走，能力往科室里走，判断往执行状态里走。",
          width=0.780)
    foot(fig, ax, "数据来源：第一财经／澎湃／钛媒体 2026-11-23、arXiv:2610.26825（MemT-1.0）；"
                  "界面新闻 2026-11-23、IT 之家 2026-11-23（LingSante）；"
                  "arXiv:2611.26519、第一财经 2026-11-23（ACE-Brain-0.7）。"
                  "各栏数字为发布方或论文口径，跨栏不可直接比较。")
    fig.savefig(OUT + "图3_同一天三条赛道.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)