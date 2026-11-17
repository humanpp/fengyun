# -*- coding: utf-8 -*-
"""
《微软蒸发 6000 亿，跌的不是业绩》配套图表
事实来源：The Verge 2026-11-10；Investing.com / IBD / 潮新闻 / 智东西；
财联社 2026-11-13（Stifel 观点）；TradingKey（M365 收入占比估算）
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
    fig.subplots_adjust(left=0.045, right=0.955, top=0.750, bottom=0.175)

    fig.suptitle("2026 年 11 月 10 日，周二，同一天的两件事",
                 fontsize=19, color=DARK, x=0.045, ha="left", y=0.955, weight="bold")
    fig.text(0.045, 0.878,
             "原文所称“11 月 14 日”是周六、非交易日——按一手报道应为 11 月 10 日",
             fontsize=10.4, color=GRAY, ha="left")

    ax.set_xlim(0, 1)
    ax.set_ylim(1.30, 4.55)
    ax.axis("off")

    # 左侧两件事
    events = [
        (3.78, "Anthropic 启动 IPO 路演", "计划最高募资 644 亿美元，冲击史上最大规模上市", NAVY),
        (2.32, "同日发布办公套件", "Claude Meetings / Sheets / Whiteboards 三款新品\nClaude Data 从测试转为正式可用", RED),
    ]

    for y, title, note, color in events:
        ax.add_patch(plt.Rectangle((0.025, y - 0.58), 0.520, 1.16,
                                   facecolor=PALE, edgecolor=color, linewidth=1.4))
        ax.add_patch(plt.Rectangle((0.025, y - 0.58), 0.007, 1.16,
                                   facecolor=color, edgecolor="none"))
        ax.text(0.055, y + 0.32, title, fontsize=12.5, color=color,
                weight="bold", va="center")
        ax.text(0.055, y - 0.18, note, fontsize=9.4, color=GRAY,
                va="center", linespacing=1.7)

    # 中间箭头
    ax.annotate("", xy=(0.635, 3.05), xytext=(0.558, 3.05),
                arrowprops=dict(arrowstyle="-|>", color=DARK, lw=2.0))

    # 右侧结果
    ax.add_patch(plt.Rectangle((0.660, 2.24), 0.315, 1.62,
                               facecolor="white", edgecolor=DARK, linewidth=1.5))
    ax.text(0.818, 3.56, "微软 MSFT", fontsize=11.5, color=DARK,
            weight="bold", ha="center")
    ax.text(0.818, 3.02, "−2.2%", fontsize=30, color=RED,
            weight="bold", ha="center", va="center")
    ax.text(0.818, 2.58, "盘中一度跌超 3.5%\n市值蒸发约 893 亿美元", fontsize=9.4,
            color=GRAY, ha="center", va="center", linespacing=1.7)

    # 折算说明
    ax.text(0.818, 1.90, "≈ 6000 亿元人民币", fontsize=11, color=DARK,
            ha="center", va="center", weight="bold")

    takeaway(fig, 0.082, "数字是真的，但“蒸发 6000 亿”遮住了真正值得看的东西。")

    footer(fig, "数据：The Verge 2026-11-10；Investing.com、Investor's Business Daily、潮新闻、智东西 11-10 至 11-11。")
    fig.savefig(OUT + "图1_同一天的两件事.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig, ax = plt.subplots(figsize=(12, 6.8))
    fig.subplots_adjust(left=0.045, right=0.955, top=0.750, bottom=0.175)

    fig.suptitle("四个新产品，四个靶子",
                 fontsize=19, color=DARK, x=0.045, ha="left", y=0.955, weight="bold")
    fig.text(0.045, 0.878,
             "前三个为本次新推（beta），Claude Data 由测试转为正式可用",
             fontsize=10.6, color=GRAY, ha="left")

    ax.set_xlim(0, 1)
    ax.set_ylim(0.25, 4.60)
    ax.axis("off")

    # 表头
    ax.text(0.265, 4.30, "Anthropic", fontsize=12.5, color=RED,
            ha="center", weight="bold")
    ax.text(0.735, 4.30, "微软对应产品", fontsize=12.5, color=NAVY,
            ha="center", weight="bold")
    ax.plot([0.040, 0.960], [4.10, 4.10], color=DARK, lw=1.3)

    rows = [
        ("Claude Meetings", "Teams", "进会议、记笔记、跟进任务"),
        ("Claude Sheets", "Excel / Google Sheets", "AI 长在表里，而非贴在表上"),
        ("Claude Whiteboards", "Whiteboard", "团队与 Claude 共同头脑风暴"),
        ("Claude Data", "Power BI", "数据看板与解说"),
    ]

    for i, (left, right, note) in enumerate(rows):
        y = 3.45 - i * 0.74
        ax.add_patch(plt.Rectangle((0.040, y - 0.29), 0.450, 0.58,
                                   facecolor="#f4ecea", edgecolor=LIGHT, linewidth=1.0))
        ax.add_patch(plt.Rectangle((0.510, y - 0.29), 0.450, 0.58,
                                   facecolor=PALE, edgecolor=LIGHT, linewidth=1.0))
        ax.text(0.265, y + 0.07, left, fontsize=11, color=DARK,
                ha="center", weight="bold")
        ax.text(0.265, y - 0.14, note, fontsize=8.6, color=GRAY, ha="center")
        ax.text(0.735, y, right, fontsize=11.2, color=NAVY, ha="center",
                weight="bold")
        ax.annotate("", xy=(0.498, y), xytext=(0.492, y),
                    arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=1.6))

    # 结论
    ax.add_patch(plt.Rectangle((0.115, 0.30), 0.770, 0.46,
                               facecolor="white", edgecolor=RED, linewidth=1.4))
    ax.text(0.500, 0.53, "从“嵌进 Office”到“把 Office 变成可选项”",
            fontsize=12, color=RED, ha="center", va="center", weight="bold")

    footer(fig, "产品与对应关系据 The Verge 2026-11-10 及智东西、Investing.com 同日报道整理。")
    fig.savefig(OUT + "图2_四个靶子.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig, ax = plt.subplots(figsize=(12, 6.8))
    fig.subplots_adjust(left=0.045, right=0.955, top=0.750, bottom=0.175)

    fig.suptitle("微软同时是三个身份，而它们互相冲突",
                 fontsize=19, color=DARK, x=0.045, ha="left", y=0.955, weight="bold")
    fig.text(0.045, 0.878,
             "“合作”这个词，装不下这三种关系同时成立",
             fontsize=10.8, color=GRAY, ha="left")

    ax.set_xlim(0, 1)
    ax.set_ylim(0.50, 4.60)
    ax.axis("off")

    roles = [
        ("股东", "260 亿美元非公开配售的七家之一", "投了钱，希望它涨", NAVY),
        ("客户", "“Claude for Microsoft 365”，2026 年 5 月起", "在用它的能力", NAVY),
        ("被替代对象", "Microsoft 365 约占微软总收入三成", "被它打的那块收入", RED),
    ]

    for i, (role, fact, note, color) in enumerate(roles):
        x0 = 0.030 + i * 0.325
        ax.add_patch(plt.Rectangle((x0, 1.90), 0.290, 2.42,
                                   facecolor=PALE, edgecolor=color, linewidth=1.5))
        ax.add_patch(plt.Rectangle((x0, 4.20), 0.290, 0.12,
                                   facecolor=color, edgecolor="none"))
        ax.text(x0 + 0.145, 3.88, role, fontsize=15, color=color,
                weight="bold", ha="center")
        ax.text(x0 + 0.145, 3.10, fact, fontsize=9.6, color=DARK,
                ha="center", va="center", linespacing=1.8,
                wrap=True)
        ax.text(x0 + 0.145, 2.28, note, fontsize=10, color=GRAY,
                ha="center", va="center", style="italic")

    # 冲突说明（三个身份之间的张力）
    ax.text(0.500, 1.56, "同一家公司，既要它好，又要打它",
            fontsize=12, color=RED, ha="center", weight="bold")

    # 底部结论
    ax.add_patch(plt.Rectangle((0.115, 0.62), 0.770, 0.72,
                               facecolor="white", edgecolor=DARK, linewidth=1.4))
    ax.text(0.500, 1.16, "结构无解：这笔 2.2% 只会在下次发布会再被定价一次",
            fontsize=11.6, color=DARK, ha="center", va="center", weight="bold")
    ax.text(0.500, 0.84, "它跌的不是本季业绩，是护城河的估值",
            fontsize=10.6, color=RED, ha="center", va="center")

    footer(fig, "据 Anthropic 招股与配售公开信息、Claude for Microsoft 365 产品页、TradingKey 收入占比估算整理。")
    fig.savefig(OUT + "图3_三个身份.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")