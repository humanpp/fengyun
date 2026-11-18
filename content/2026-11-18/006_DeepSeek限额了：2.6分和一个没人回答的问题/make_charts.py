# -*- coding: utf-8 -*-
"""
《DeepSeek 限额了：2.6 分的评论区，在问同一个问题》配套图表
事实口径（第一财经 2026-11-16 报道、21 经济网 11-16、《正在新闻》11-17 等）：
  · 11-16 "DeepSeek 使用额度已达上限"登上微博热搜，用户反映 App/网页版调整：
    不再支持超过 7 天不活跃的长对话（也有用户反映为 72 小时）、单次文字输入上限
    缩短至约 4 万字、每日对话额度受限，触顶提示"因服务器繁忙，使用额度已达上限"；
  · 有用户连续使用不到两小时即触顶；官方未发布统一规则、未披露解除时间；
  · 限额主要针对 C 端 App 与网页版，API 为独立规则与按量计费；
  · 官方未提供付费选项，用户称"并非不愿付费"；
  · OpenRouter：11-09 至 11-15 一周 DeepSeek V4.1 Flash 1017 完成 59.2 万亿 Token
    调用，居全球首位；9-14 当周为 15.8 万亿，两个月增长近三倍；
  · 10 月以来平台至少 5 起部分服务中断或异常，10-15 崩溃 5 小时；
  · 10 月完成二轮融资 1055 亿元，估值约 6155 亿元，资金主要投向算力基础设施；
  · 11-17《正在新闻》：小米应用商店 DeepSeek 评分 2.6 分，1.3 万条评价中差评占 63%。
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
GREEN = "#4f6b58"
SAND = "#f7f3ea"

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


# ------------------------------------------------------------------ 图 1
def fig1():
    fig = base("这次到底限了什么",
               "三项调整，一个提示语。没人告诉你上限是多少")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    rows = [
        ("① 长对话", "不再支持超过 7 天不活跃的长对话",
         "系统建议：新开一个对话，或者导出历史记录\n换到别的应用里继续", "7 天"),
        ("② 输入长度", "单次文字输入上限，缩短至约 4 万字",
         "对写论文、整理论文、长文档的人影响最大", "4 万字"),
        ("③ 每日额度", "每天能用的对话总量设了上限",
         "触顶后弹窗：因服务器繁忙，使用额度已达上限", "次日恢复"),
    ]

    yy = 0.820
    for head, main, note, tag in rows:
        ax.add_patch(FancyBboxPatch((0.050, yy - 0.155), 0.640, 0.155,
                                    boxstyle="round,pad=0.010",
                                    facecolor="#fafbfc", edgecolor=LIGHT,
                                    linewidth=1.0))
        ax.text(0.075, yy - 0.010, head, fontsize=11.0, color=NAVY,
                weight="bold", ha="left", va="top")
        ax.text(0.230, yy - 0.012, main, fontsize=10.4, color=DARK,
                ha="left", va="top")
        ax.text(0.075, yy - 0.078, note, fontsize=8.9, color=GRAY, ha="left",
                va="top", linespacing=1.7)

        ax.add_patch(FancyBboxPatch((0.712, yy - 0.062), 0.230, 0.072,
                                    boxstyle="round,pad=0.008",
                                    facecolor="#fbf3f1", edgecolor=RED,
                                    linewidth=1.0))
        ax.text(0.827, yy - 0.026, tag, fontsize=10.0, color=RED, weight="bold",
                ha="center", va="center")
        yy -= 0.180

    ax.plot([0.045, 0.955], [0.265, 0.265], color=LIGHT, linewidth=1.0)

    ax.text(0.050, 0.215, "实际体验", fontsize=10.6, color=RED, weight="bold",
            ha="left", va="center")
    facts = [
        "有用户连续使用不到两小时，就收到了额度耗尽的提示。",
        "也有用户反映，自己的长对话是「超过 72 小时未活跃」就不能继续了，不是 7 天。",
        "官方没有发布统一的限额规则，也没说什么时候解除。",
    ]
    yy = 0.150
    for f in facts:
        ax.plot([0.052], [yy], marker="s", markersize=5.5, color=RED, zorder=3)
        ax.text(0.074, yy, f, fontsize=9.6, color=SLATE, ha="left", va="center")
        yy -= 0.058

    punchline(fig, "同一个功能，不同的人撞上不同的墙。")
    footer(fig, "事实：第一财经（2026-11-16）、21 经济网（11-16）、界面新闻等公开报道｜制图：本文")
    fig.savefig(OUT + "图1_这次到底限了什么.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("2.6 分是怎么来的",
               "小米应用商店：1.3 万条评价，差评占六成以上")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # 左侧大数字
    ax.text(0.060, 0.775, "2.6", fontsize=62, color=RED, weight="bold",
            ha="left", va="center")
    ax.text(0.300, 0.775, "/ 5", fontsize=16, color=GRAY, ha="left",
            va="center")
    ax.text(0.060, 0.660, "小米应用商店评分", fontsize=10.6, color=DARK,
            ha="left", va="center")
    ax.text(0.060, 0.600, "1.3 万条评价中，差评占 63%", fontsize=9.6,
            color=GRAY, ha="left", va="center")

    # 好评/差评比例条
    ax.add_patch(Rectangle((0.060, 0.505), 0.360, 0.052, facecolor="#eef0f3",
                           edgecolor=LIGHT, linewidth=1.0))
    ax.add_patch(Rectangle((0.060, 0.505), 0.360 * 0.63, 0.052,
                           facecolor=RED, edgecolor="none"))
    ax.text(0.060 + 0.360 * 0.63 / 2, 0.531, "差评 63%", fontsize=9.0,
            color="white", weight="bold", ha="center", va="center")
    ax.text(0.436, 0.531, "其余", fontsize=8.6, color=GRAY, ha="left",
            va="center")

    # 右侧：评论区在问什么
    ax.plot([0.520, 0.520], [0.300, 0.800], color=LIGHT, linewidth=1.0,
            linestyle=(0, (4, 4)))
    ax.text(0.560, 0.792, "评论区在说的，其实不是「要收费」", fontsize=11.4,
            color=DARK, weight="bold", ha="left", va="center")

    quotes = [
        ("「不是不愿意付费」", "是想要一个能稳定用的选择，\n但官方没有给付费入口。"),
        ("「长对话断了」", "改了半个月的稿子、聊了几周的设定，\n一夜之间接不上，只能重新开。"),
        ("「不知道规则」", "上限是多少、多久恢复、\n什么时候解除——都没有答案。"),
    ]
    yy = 0.695
    for head, body in quotes:
        ax.text(0.560, yy, head, fontsize=10.2, color=RED, weight="bold",
                ha="left", va="center")
        ax.text(0.560, yy - 0.048, body, fontsize=9.2, color=SLATE, ha="left",
                va="top", linespacing=1.75)
        yy -= 0.175

    punchline(fig, "评分跌下去，不是因为涨价，是因为没人解释。")
    footer(fig, "数据：《正在新闻》2026-11-17 检索小米应用商店；用户反馈引自第一财经等报道｜制图：本文")
    fig.savefig(OUT + "图2_26分是怎么来的.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("算力的账，和规则的账",
               "需求两个月涨了近三倍；规则，一页纸都没有")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # 左：柱状对比
    ax.text(0.060, 0.830, "V4.1 Flash 周调用量（万亿 Token）", fontsize=10.4,
            color=DARK, weight="bold", ha="left", va="center")

    bars = [(0.130, 15.8, "9 月 14 日当周", GRAY),
            (0.320, 59.2, "11 月 9—15 日", NAVY)]
    base_y, max_h, max_v = 0.330, 0.400, 59.2
    for x, val, label, color in bars:
        h = max_h * val / max_v
        ax.add_patch(Rectangle((x, base_y), 0.110, h, facecolor=color,
                               edgecolor="none"))
        ax.text(x + 0.055, base_y + h + 0.040, f"{val}", fontsize=13.6,
                color=color, weight="bold", ha="center", va="center")
        ax.text(x + 0.055, base_y - 0.045, label, fontsize=8.8, color=GRAY,
                ha="center", va="top")
    ax.plot([0.100, 0.470], [base_y, base_y], color=LIGHT, linewidth=1.2)

    ax.text(0.500, 0.500, "近 3 倍", fontsize=15.0, color=RED, weight="bold",
            ha="center", va="center", rotation=0)
    ax.text(0.500, 0.430, "两个月", fontsize=9.0, color=GRAY, ha="center",
            va="center")

    # 右：事实
    ax.plot([0.600, 0.600], [0.190, 0.830], color=LIGHT, linewidth=1.0,
            linestyle=(0, (4, 4)))
    ax.text(0.640, 0.830, "同期发生的", fontsize=10.4, color=DARK,
            weight="bold", ha="left", va="center")

    facts = [
        ("10 月以来", "至少 5 起部分服务中断或异常，\n覆盖对话服务与两款模型的 API"),
        ("10 月 15 日", "服务崩溃 5 小时，\n是今年以来较严重的一次"),
        ("10 月", "完成二轮融资 1055 亿元，\n估值约 6155 亿元，投向算力"),
    ]
    yy = 0.720
    for head, body in facts:
        ax.text(0.640, yy, head, fontsize=10.0, color=RED, weight="bold",
                ha="left", va="center")
        ax.text(0.640, yy - 0.048, body, fontsize=9.0, color=SLATE, ha="left",
                va="top", linespacing=1.75)
        yy -= 0.180

    ax.add_patch(FancyBboxPatch((0.055, 0.055), 0.890, 0.095,
                                boxstyle="round,pad=0.010", facecolor=SAND,
                                edgecolor="#d9cdb6", linewidth=1.0, zorder=2))
    ax.text(0.500, 0.102,
            "限流是理性的选择。不理性的是：限了，却不告诉用户限在哪儿。",
            fontsize=10.6, color="#7a6746", ha="center", va="center", zorder=3)

    punchline(fig, "算力可以买，规则得先说。")
    footer(fig, "数据：OpenRouter 周调用量（第一财经报道）；中断次数据 DeepSeek 官方状态页；融资数据据媒体报道｜制图：本文")
    fig.savefig(OUT + "图3_算力的账和规则的账.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)