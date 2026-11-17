# -*- coding: utf-8 -*-
"""
《AI 算力叙事分裂：2028 年资本开支预测砍 28%，英伟达谷歌却同日发新硬件》配套图表
事实口径：SemiAnalysis 下修远期 AI 算力预测——2028 年全球 AI 加速器资本开支
下调 28%，2029 年 41%，2030 年 40%；2030 年预测由 1.531 万亿美元降至 9230 亿
美元，减少 6080 亿美元；2026—2030 年加速器逻辑硅片出货面积累计下调 17%。
同日英伟达推出 Vera CPU 机架级平台（能效比 x86 提升一倍）；谷歌云公布第七代
Ironwood TPU 测试结果（640 块 TPU、18 分钟达到目标准确率、训练芯片等待时间
占比低于 3%）。美股费城半导体指数重挫 5.28%，英伟达 −4.12%、英特尔 −7.02%、
台积电 −6.34%、AMD −5.58%。
风格：克制传媒风，白底、低饱和配色、标题即结论
输出目录 = 脚本所在目录
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

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

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep


def footer(fig, text):
    fig.text(0.045, 0.020, text, fontsize=8.4, color=GRAY, ha="left", va="bottom")


def punchline(fig, text):
    fig.text(0.045, 0.072, text, fontsize=10.4, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


# ---------------------------------------------------------------- 图 1
def fig1():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.135, 0.910, 0.690])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "2030 年的账本，被划掉四成", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.888, "SemiAnalysis 下修远期预测：2030 年从 1.531 万亿美元降到 9230 亿美元",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    chips = [("2028 年", "−28%"), ("2029 年", "−41%"), ("2030 年", "−40%")]
    for i, (year, pct) in enumerate(chips):
        x0 = 0.020 + i * 0.327
        ax.add_patch(Rectangle((x0, 0.720), 0.298, 0.200, facecolor=PALE,
                               edgecolor=LIGHT, linewidth=1.0))
        ax.text(x0 + 0.024, 0.872, "资本开支下调", fontsize=9.4, color=GRAY,
                va="center")
        ax.text(x0 + 0.024, 0.800, pct, fontsize=25, color=RED, weight="bold",
                va="center")
        ax.text(x0 + 0.150, 0.786, year, fontsize=10.4, color=SLATE, va="center")

    # 2030 年金额：一条总量条，按比例切成"留下"和"划掉"
    ax.text(0.020, 0.640, "2030 年 AI 加速器资本开支", fontsize=10.4, color=SLATE,
            va="center")
    ax.text(0.020, 0.596, "原预测 1.531 万亿美元", fontsize=9.4, color=GRAY,
            va="center")

    bar_y, bar_h, x_start, total_w = 0.440, 0.120, 0.020, 0.960
    keep = 9230 / 15310.0
    keep_w = total_w * keep

    ax.add_patch(Rectangle((x_start, bar_y), keep_w, bar_h, facecolor=NAVY,
                           edgecolor="none"))
    ax.add_patch(Rectangle((x_start + keep_w, bar_y), total_w - keep_w, bar_h,
                           facecolor=RED, edgecolor="none"))

    ax.text(x_start + keep_w / 2, bar_y + bar_h / 2, "9230 亿　留下",
            fontsize=11.5, color="white", weight="bold", ha="center", va="center")
    ax.text(x_start + keep_w + (total_w - keep_w) / 2, bar_y + bar_h / 2,
            "6080 亿\n划掉", fontsize=11.5, color="white", weight="bold",
            ha="center", va="center", linespacing=1.5)

    ax.text(x_start + keep_w / 2, bar_y - 0.055, "占原预测六成", fontsize=9.4,
            color=NAVY, ha="center", va="center")
    ax.text(x_start + keep_w + (total_w - keep_w) / 2, bar_y - 0.055,
            "相当于留下部分的 66%", fontsize=9.4, color=RED, ha="center",
            va="center")

    ax.plot([x_start, x_start + total_w], [0.290, 0.290], color=LIGHT,
            linewidth=1.2)
    ax.text(x_start, 0.230, "同一份预测里，2026—2030 年加速器逻辑硅片出货面积累计下调 17%",
            fontsize=9.6, color=SLATE, va="center")
    ax.text(x_start, 0.170, "金额砍得比面积狠得多：差额落在单价和结构上，不只是颗数",
            fontsize=9.6, color=GRAY, va="center")

    punchline(fig, "划掉的那一块，比留下的还多三分之二。")
    footer(fig, "据 SemiAnalysis 下修后的远期预测数据整理；66% 与「六成」为据 1.531 万亿、9230 亿两个口径的换算。")
    fig.savefig(OUT + "图1_划掉四成.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.135, 0.910, 0.690])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "一边砍远期，一边发硬件", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.888, "同一天的两组动作，方向相反", fontsize=10.8,
             color=GRAY, ha="left", va="top")

    top, bot = 0.860, 0.190

    # 左：远期预测
    ax.add_patch(Rectangle((0.020, bot), 0.450, top - bot, facecolor=PALE,
                           edgecolor=LIGHT, linewidth=1.0))
    ax.add_patch(Rectangle((0.020, top - 0.013), 0.450, 0.013, facecolor=RED,
                           edgecolor="none"))
    ax.text(0.048, top - 0.075, "远期预测：往下调", fontsize=13.5, color=RED,
            weight="bold", va="center")
    ax.text(0.048, top - 0.130, "SemiAnalysis，2026 年 11 月", fontsize=9.2,
            color=GRAY, va="center")

    left_rows = [
        ("2028 年资本开支", "−28%"),
        ("2029 年资本开支", "−41%"),
        ("2030 年资本开支", "−40%"),
        ("2026—2030 出货面积", "−17%"),
    ]
    for i, (label, val) in enumerate(left_rows):
        y = 0.655 - i * 0.125
        ax.text(0.048, y, label, fontsize=10.4, color=DARK, va="center")
        ax.text(0.442, y, val, fontsize=17, color=RED, weight="bold",
                ha="right", va="center")
        if i < len(left_rows) - 1:
            ax.plot([0.048, 0.442], [y - 0.062, y - 0.062], color=LIGHT,
                    linewidth=0.9)

    # 右：同日新硬件
    ax.add_patch(Rectangle((0.530, bot), 0.450, top - bot, facecolor=PALE,
                           edgecolor=LIGHT, linewidth=1.0))
    ax.add_patch(Rectangle((0.530, top - 0.013), 0.450, 0.013, facecolor=NAVY,
                           edgecolor="none"))
    ax.text(0.558, top - 0.075, "同日新硬件：往前推", fontsize=13.5, color=NAVY,
            weight="bold", va="center")
    ax.text(0.558, top - 0.130, "英伟达 / 谷歌云", fontsize=9.2, color=GRAY,
            va="center")

    right_rows = [
        ("英伟达 Vera CPU", "机架级平台，能效比 x86 提升一倍"),
        ("谷歌 Ironwood TPU（第七代）", "640 块 TPU，18 分钟达到目标准确率"),
        ("训练芯片等待时间", "占比低于 3%，集群几乎不空转"),
    ]
    for i, (title, note) in enumerate(right_rows):
        y = 0.640 - i * 0.160
        ax.text(0.558, y, title, fontsize=11.6, color=NAVY, weight="bold",
                va="center")
        ax.text(0.558, y - 0.062, note, fontsize=9.4, color=SLATE, va="center")
        if i < len(right_rows) - 1:
            ax.plot([0.558, 0.952], [y - 0.100, y - 0.100], color=LIGHT,
                    linewidth=0.9)

    punchline(fig, "预测在降温，动作没减速。")
    footer(fig, "据 SemiAnalysis 下修数据、英伟达 Vera CPU 平台发布信息、谷歌云 Ironwood TPU 测试结果整理；测试结果为厂商公布口径。")
    fig.savefig(OUT + "图2_两边动作.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.250, 0.235, 0.700, 0.540])

    fig.text(0.045, 0.955, "跌得最狠的，不是英伟达", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.888, "费城半导体指数重挫 5.28%，同日个股跌幅排在它前面和后面",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    rows = [
        ("英特尔", 7.02),
        ("台积电", 6.34),
        ("AMD", 5.58),
        ("费城半导体指数", 5.28),
        ("英伟达", 4.12),
    ]

    ys = list(range(len(rows)))[::-1]
    colors = [RED, RED, RED, SLATE, NAVY]
    for y, (name, val), color in zip(ys, rows, colors):
        ax.barh(y, val, height=0.56, color=color, edgecolor="none")
        ax.text(val + 0.12, y, f"−{val:.2f}%", fontsize=12.5, color=color,
                weight="bold", va="center")

    ax.set_yticks(ys)
    ax.set_yticklabels([r[0] for r in rows], fontsize=11, color=DARK)
    ax.set_xlim(0, 8.6)
    ax.set_xticks([0, 2, 4, 6, 8])
    ax.set_xticklabels(["0", "2", "4", "6", "8%"], fontsize=9.5, color=GRAY)
    ax.set_xlabel("当日跌幅", fontsize=9.5, color=GRAY)

    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(LIGHT)
    ax.tick_params(axis="both", length=0)
    ax.grid(axis="x", color=LIGHT, linewidth=0.8, alpha=0.7)
    ax.set_axisbelow(True)

    punchline(fig, "市场没等答案，先把速度差交易掉了。")
    footer(fig, "据当日美股收盘数据整理；跌幅为单日涨跌幅，非区间累计。")
    fig.savefig(OUT + "图3_跌幅榜.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")
