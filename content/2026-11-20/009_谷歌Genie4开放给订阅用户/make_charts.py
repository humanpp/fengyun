# -*- coding: utf-8 -*-
"""
《谷歌 Genie 4 开放给订阅用户：世界模型不再只是演示，能实时改天气、召唤角色》配套图表
事实口径（均经公开报道交叉核对）：
  · 2026-11-18（美东）Google 官方博客宣布：Genie 4 通过 Project Genie 向符合条件的
    Google AI Ultra 订阅用户开放；Google AI Pro 用户可加入候补名单。
  · Genie 4 于 2026-10-27 以研究预览形式面向受信任测试者发布，11-18 首次向订阅用户开放。
  · 能力：探索中实时输入提示词改写世界（改天气、引入角色、调整事件走向），无需重新开始；
    Genie 系列首次加入实时原生音频（环境音、音乐、角色对白）；
    新增 Project Genie 智能体（对话式辅助创作）与社区画廊（可发布、可再创作）。
  · Genie 3 仍保留在模型选择器中：单次会话由 60 秒延长至最长 3 分钟，支持多世界串联、
    360 度全景图作为新世界的种子。Genie 4 的单次会话时长 Google 未公布。
  · 谷歌自述限制：物体在不同视角间可能漂移或改变，复杂物理仍存在困难，
    生成的语音或文字可能不准确，相机延迟、实时音频精度、长期场景稳定性尚未解决；
    Google 仍将 Genie 3 与 Genie 4 称为前沿研究阶段模型。
  · 安全：全部生成视频与音频带 SynthID 水印，输入与输出均经安全筛查。
  · 价格：含在美国每月 199.99 美元的 Google AI Ultra 订阅中。
  · 沿革：Genie 于 2024 年亮相，初代从逾 20 万小时游戏录像中学习，可将单张图像转为可玩的
    2D 环境；Genie 2 进入三维；Project Genie 于 2026 年 1 月向美国成年 Ultra 订阅用户开放。
说明：素材称"迄今最逼真、最具交互性"为 Google 自身表述，来自其自家演示，尚无独立测试证据，
      图中与正文均按"谷歌称"处理。
风格：克制传媒风，白底、低饱和配色、标题即结论。输出目录 = 脚本所在目录。
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False

NAVY = "#1f3a5f"
RED = "#b5544a"
GRAY = "#8a8f98"
SLATE = "#5f6673"
LIGHT = "#d8dbe0"
DARK = "#2b2f36"
PALE = "#eef0f3"
SAND = "#f7f3ea"
GOLD = "#c9a27a"
GREEN = "#5a7d6f"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep


def base(title, sub):
    fig = plt.figure(figsize=(12, 6.8))
    fig.patch.set_facecolor("white")
    fig.text(0.045, 0.950, title, fontsize=20, color=DARK, weight="bold",
             ha="left", va="top")
    fig.text(0.045, 0.878, sub, fontsize=10.8, color=GRAY, ha="left", va="top")
    return fig


def footer(fig, text):
    fig.text(0.045, 0.014, text, fontsize=8.2, color=GRAY, ha="left", va="center")


def punchline(fig, text, y=0.078):
    fig.text(0.045, y, text, fontsize=10.8, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.6", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


def canvas(fig):
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return ax


# ------------------------------------------------------------------ 图 1
def fig1():
    fig = base("从研究预览到付费产品",
               "Genie 三代，两年，一次关键跳跃")
    ax = canvas(fig)

    y_line = 0.480
    ax.plot([0.075, 0.935], [y_line, y_line], color=LIGHT, linewidth=2.0,
            zorder=2)

    nodes = [
        ("2024", "Genie", "初代亮相\n从逾 20 万小时\n游戏录像中学习", "below", SLATE),
        ("2025", "Genie 2", "进入三维空间", "above", SLATE),
        ("2026.01", "Project Genie", "向美国成年\nUltra 订阅用户开放", "below", NAVY),
        ("2026.10.27", "Genie 4", "研究预览\n仅受信任测试者", "above", GOLD),
        ("2026.11.18", "开放给订阅用户", "符合条件的\nAI Ultra 用户可用", "below", RED),
    ]

    xs = [0.105, 0.290, 0.475, 0.680, 0.890]

    for x, (date, name, desc, where, col) in zip(xs, nodes):
        ax.add_patch(Circle((x, y_line), 0.012, facecolor=col, edgecolor="white",
                            linewidth=2.0, zorder=6))
        if where == "above":
            ax.text(x, y_line + 0.048, date, fontsize=9.2, color=col,
                    weight="bold", ha="center", va="bottom")
            ax.text(x, y_line + 0.084, name, fontsize=12.0, color=DARK,
                    weight="bold", ha="center", va="bottom")
            ax.text(x, y_line + 0.124, desc, fontsize=8.6, color=SLATE,
                    ha="center", va="bottom", linespacing=1.6)
        else:
            ax.text(x, y_line - 0.048, date, fontsize=9.2, color=col,
                    weight="bold", ha="center", va="top")
            ax.text(x, y_line - 0.084, name, fontsize=12.0, color=DARK,
                    weight="bold", ha="center", va="top")
            ax.text(x, y_line - 0.124, desc, fontsize=8.6, color=SLATE,
                    ha="center", va="top", linespacing=1.6)

    # 最后一步的时间跨度标注
    ax.annotate("", xy=(0.890, 0.760), xytext=(0.680, 0.760),
                arrowprops=dict(arrowstyle="<->", color=RED, linewidth=1.4))
    ax.text(0.785, 0.772, "相隔三周", fontsize=10.0, color=RED, weight="bold",
            ha="center", va="bottom")

    ax.text(0.075, 0.150,
            "研究预览到付费产品，用了三周。这是这一代模型里最短的一次。",
            fontsize=9.6, color=DARK, ha="left", va="center")

    punchline(fig, "世界模型第一次有了“用户”，而不只是“评审”。")
    footer(fig, "事实：时间线与各代能力据 Google 官方博客 2026-11-18、Google DeepMind 2026-10-27 研究博客及公开报道｜制图：本文")
    fig.savefig(OUT + "图1_两年代际.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("同一个产品里的两个模型",
               "Genie 3 与 Genie 4：一个换时长，一个换真实感")
    ax = canvas(fig)

    rows = [
        ("单次会话时长", "最长 3 分钟", "未公布", RED),
        ("实时原生音频", "无", "有（环境音 / 音乐 / 对白）", GREEN),
        ("探索中改写世界", "支持", "支持", GREEN),
        ("多世界串联", "支持", "—", GRAY),
        ("360 度全景图作种子", "支持", "—", GRAY),
        ("物体跨视角持久性", "会漂移", "会漂移（谷歌自述）", RED),
    ]

    x0 = 0.075
    col_w = [0.240, 0.250, 0.330]
    x_col = [x0, x0 + col_w[0], x0 + col_w[0] + col_w[1]]

    # 表头
    y_head = 0.845
    ax.add_patch(FancyBboxPatch((x0, y_head - 0.062), 0.860, 0.062,
                                boxstyle="round,pad=0.006",
                                facecolor="#f2f4f7", edgecolor="none"))
    heads = ["", "Genie 3", "Genie 4"]
    for i, h in enumerate(heads):
        ax.text(x_col[i] + (0.010 if i == 0 else col_w[i] / 2),
                y_head - 0.031, h, fontsize=10.4, color=DARK, weight="bold",
                ha="left" if i == 0 else "center", va="center")

    for j, (label, g3, g4, col) in enumerate(rows):
        y = y_head - 0.100 - j * 0.086
        if j % 2 == 0:
            ax.add_patch(FancyBboxPatch((x0, y - 0.036), 0.860, 0.072,
                                        boxstyle="square,pad=0",
                                        facecolor="#fafbfc", edgecolor="none"))
        ax.text(x_col[0] + 0.010, y, label, fontsize=9.4, color=DARK,
                ha="left", va="center")
        ax.text(x_col[1] + col_w[1] / 2, y, g3, fontsize=9.2, color=SLATE,
                ha="center", va="center")
        ax.text(x_col[2] + col_w[2] / 2, y, g4, fontsize=9.2, color=col,
                weight="bold", ha="center", va="center")

    ax.text(0.075, 0.178,
            "Genie 3 仍在模型选择器里：要探索得久用 Genie 3，要真实感和声音用 Genie 4。",
            fontsize=9.2, color=SLATE, ha="left", va="center")
    ax.text(0.075, 0.140,
            "谷歌同时承认：物体在不同视角间可能漂移，复杂物理仍存在困难。",
            fontsize=9.2, color=RED, weight="bold", ha="left", va="center")

    punchline(fig, "升级不是全面的：一边加时长，一边加真实感，谁也没全占。")
    footer(fig, "事实：据 Google 官方博客 2026-11-18；Genie 4 会话时长谷歌未公布；“会漂移”为谷歌自述限制｜制图：本文")
    fig.savefig(OUT + "图2_两个模型的分工.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("两把不同的尺子",
               "语言模型和世界模型，评价标准不是一套")
    ax = canvas(fig)

    # 左：语言模型
    ax.add_patch(FancyBboxPatch((0.060, 0.230), 0.410, 0.520,
                                boxstyle="round,pad=0.012", facecolor="#eef2f6",
                                edgecolor=NAVY, linewidth=1.2))
    ax.text(0.085, 0.700, "语言模型", fontsize=14.0, color=NAVY, weight="bold",
            ha="left", va="center")
    ax.text(0.085, 0.652, "问一次，答一次", fontsize=9.2, color=GRAY,
            ha="left", va="center")
    left_items = [
        "基准分数：考卷答对多少",
        "每百万 token 多少钱",
        "回答准不准、有没有幻觉",
        "一次调用的成本与延迟",
    ]
    yy = 0.575
    for it in left_items:
        ax.text(0.085, yy, "·  " + it, fontsize=9.6, color=DARK, ha="left",
                va="center")
        yy -= 0.080
    ax.text(0.085, 0.270, "比的是“单次输出”", fontsize=9.4, color=NAVY,
            weight="bold", ha="left", va="center")

    # 右：世界模型
    ax.add_patch(FancyBboxPatch((0.530, 0.230), 0.410, 0.520,
                                boxstyle="round,pad=0.012", facecolor="#f7eae8",
                                edgecolor=RED, linewidth=1.2))
    ax.text(0.555, 0.700, "世界模型", fontsize=14.0, color=RED, weight="bold",
            ha="left", va="center")
    ax.text(0.555, 0.652, "改一次，看它记不记得", fontsize=9.2, color=GRAY,
            ha="left", va="center")
    right_items = [
        "改了天气，那条街还在不在",
        "转过身，那个人还在原地吗",
        "推一下，东西按物理倒吗",
        "声音跟不跟得上画面",
    ]
    yy = 0.575
    for it in right_items:
        ax.text(0.555, yy, "·  " + it, fontsize=9.6, color=DARK, ha="left",
                va="center")
        yy -= 0.080
    ax.text(0.555, 0.270, "比的是“连续一致性”", fontsize=9.4, color=RED,
            weight="bold", ha="left", va="center")

    ax.text(0.060, 0.180,
            "前者可以离线打分，后者必须有人进去走一遍——这就是为什么它要开放给订阅用户。",
            fontsize=9.2, color=SLATE, ha="left", va="center")

    punchline(fig, "语言模型能考卷面，世界模型只能考“逛一圈还认不认得路”。")
    footer(fig, "说明：本图为分析框架，非当事方表述；“物体跨视角漂移”为谷歌官方承认的现存限制｜制图：本文")
    fig.savefig(OUT + "图3_两把尺子.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)
