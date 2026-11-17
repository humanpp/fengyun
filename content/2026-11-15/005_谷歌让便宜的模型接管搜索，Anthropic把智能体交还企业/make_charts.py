# -*- coding: utf-8 -*-
"""
《谷歌让“便宜的那个”接管搜索，Anthropic 把智能体交还给企业》配套图表
事实来源：谷歌 2026-11-12 Gemini 4 Hydrogen 发布；Artificial Analysis 模型页；
Anthropic 官方文档《自托管 Claude Managed Agents 中的数据与访问》
风格：克制传媒风，白底、低饱和配色、标题即结论
输出目录 = 脚本所在目录
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["figure.facecolor"] = "white"
plt.rcParams["axes.facecolor"] = "white"

NAVY = "#1f3a5f"
RED = "#b5544a"
GRAY = "#8a8f98"
LIGHT = "#d8dbe0"
DARK = "#2b2f36"
PALE = "#eef0f3"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep


def footer(fig, text):
    fig.text(0.045, 0.020, text, fontsize=8.4, color=GRAY, ha="left", va="bottom")


def takeaway(fig, y, text, size=10.4):
    fig.text(0.045, y, text, fontsize=size, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


# ---------------------------------------------------------------- 图 1
def fig1():
    fig, ax = plt.subplots(figsize=(12, 6.8))
    fig.subplots_adjust(left=0.045, right=0.955, top=0.760, bottom=0.180)

    fig.suptitle("一分之差背后，是排序逻辑换了",
                 fontsize=19, color=DARK, x=0.045, ha="left", y=0.955, weight="bold")
    fig.text(0.045, 0.885,
             "Artificial Analysis 智能指数：中端模型在默认档反超旗舰",
             fontsize=10.8, color=GRAY, ha="left")

    ax.set_xlim(0, 100)
    ax.set_ylim(0, 4.30)
    ax.axis("off")

    rows = [
        ("Gemini 4 Argon（旗舰）", 50, "默认 high 档", GRAY),
        ("Gemini 4 Hydrogen（中端）", 51, "默认 high 档", NAVY),
        ("Gemini 4 Hydrogen（xhigh）", 54, "最高 xhigh 档", RED),
    ]

    for i, (name, score, tag, color) in enumerate(rows):
        y = 3.30 - i * 1.10
        ax.text(0.5, y + 0.34, name, fontsize=12, color=DARK,
                weight="bold", va="center")
        ax.text(0.5, y + 0.02, tag, fontsize=9.6, color=GRAY, va="center")
        ax.barh(y - 0.30, score - 34, left=34, height=0.42, color=color, alpha=0.92)
        ax.text(34 + (score - 34) + 0.6, y - 0.30, f"{score}", fontsize=15,
                color=color, weight="bold", va="center")

    # 基准线
    ax.axvline(34, color=LIGHT, lw=1.0)
    ax.text(34.6, 0.30, "以下省略：为让 1 分之差可见，横轴自 34 分起",
            fontsize=9.2, color=GRAY, va="center")

    takeaway(fig, 0.085, "旗舰丢了默认位——省下的成本，比多出的那一分更值钱。")

    footer(fig, "数据：Artificial Analysis 模型对比页（Gemini 4 Hydrogen High vs Gemini 4 Argon High），2026-11。")
    fig.savefig(OUT + "图1_一分之差.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig, ax = plt.subplots(figsize=(12, 6.8))
    fig.subplots_adjust(left=0.045, right=0.955, top=0.760, bottom=0.175)

    fig.suptitle("托管与自托管：两条路同时在走",
                 fontsize=19, color=DARK, x=0.045, ha="left", y=0.955, weight="bold")
    fig.text(0.045, 0.885,
             "智能体跑在哪里、谁管密钥、日志归谁——正在成为采购决策的第一道题",
             fontsize=10.6, color=GRAY, ha="left")

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 4.55)
    ax.axis("off")

    panels = [
        (0.030, "厂商托管", GRAY, [
            ("跑在哪", "厂商的云"),
            ("谁管密钥", "厂商"),
            ("日志", "厂商可读"),
            ("适合", "开箱即用、快速上线"),
        ]),
        (0.530, "企业自托管", NAVY, [
            ("跑在哪", "自己的云或本地机房"),
            ("谁管密钥", "企业自己"),
            ("日志", "Anthropic 无法远程访问"),
            ("适合", "有审计与合规要求"),
        ]),
    ]

    for x0, title, color, rows in panels:
        ax.add_patch(plt.Rectangle((x0, 0.72), 0.440, 3.32,
                                   facecolor=PALE, edgecolor=LIGHT, linewidth=1.0))
        ax.add_patch(plt.Rectangle((x0, 3.90), 0.440, 0.14,
                                   facecolor=color, edgecolor="none"))
        ax.text(x0 + 0.028, 3.56, title, fontsize=13.5, color=color,
                weight="bold", va="center")
        for i, (k, v) in enumerate(rows):
            y = 3.08 - i * 0.62
            ax.text(x0 + 0.028, y, k, fontsize=10, color=GRAY, va="center")
            ax.text(x0 + 0.150, y, v, fontsize=10.6, color=DARK, va="center")

    takeaway(fig, 0.082, "托管和自托管同时在走，说明这个市场还没有标准答案。")

    footer(fig, "据 Anthropic 官方文档《自托管 Claude Managed Agents 中的数据与访问》，2026-11-12。")
    fig.savefig(OUT + "图2_两条路.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig, ax = plt.subplots(figsize=(12, 6.8))
    fig.subplots_adjust(left=0.045, right=0.955, top=0.760, bottom=0.175)

    fig.suptitle("从整包出售，到按模块交付",
                 fontsize=19, color=DARK, x=0.045, ha="left", y=0.955, weight="bold")
    fig.text(0.045, 0.885,
             "11 月 12 日前后几个动作，指向同一种产品形态",
             fontsize=10.8, color=GRAY, ha="left")

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 4.60)
    ax.axis("off")

    # 左侧：整包
    ax.add_patch(plt.Rectangle((0.040, 1.05), 0.330, 2.55,
                               facecolor=PALE, edgecolor=LIGHT, linewidth=1.0))
    ax.text(0.205, 3.32, "过去：整包", fontsize=12.5, color=GRAY,
            weight="bold", ha="center")
    ax.text(0.205, 2.35, "一个 App\n一套 API\n一份定价", fontsize=11.5,
            color=DARK, ha="center", va="center", linespacing=2.0)
    ax.text(0.205, 1.35, "要么全用，要么不用", fontsize=9.8, color=GRAY,
            ha="center")

    # 中间箭头
    ax.annotate("", xy=(0.560, 2.35), xytext=(0.395, 2.35),
                arrowprops=dict(arrowstyle="-|>", color=DARK, lw=2.0))

    # 右侧：模块
    ax.text(0.790, 3.32, "现在：积木", fontsize=12.5, color=NAVY,
            weight="bold", ha="center")
    modules = ["联网搜索", "文件解析", "语音", "工具调用"]
    for i, m in enumerate(modules):
        y = 3.00 - i * 0.58
        ax.add_patch(plt.Rectangle((0.640, y - 0.20), 0.300, 0.40,
                                   facecolor="white", edgecolor=NAVY, linewidth=1.1))
        ax.text(0.790, y, m, fontsize=10.6, color=NAVY, ha="center", va="center")
    ax.text(0.790, 0.85, "按需取一块，插进自己的产品", fontsize=9.8,
            color=GRAY, ha="center")

    takeaway(fig, 0.082, "对厂商不利（定价权下降），对市场有利（集成成本下降）。")

    footer(fig, "据谷歌、Anthropic、DeepSeek、腾讯混元 2026-11-12 前后的公开产品信息整理。")
    fig.savefig(OUT + "图3_模块化.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")
