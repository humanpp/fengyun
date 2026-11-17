# -*- coding: utf-8 -*-
"""
《17 家车企被抽查账期：60 天现金支付，蔚来盘中跌超 5%》配套图表
事实口径：2026 年 11 月 16 日中汽协发布通知，对 17 家重点车企供应商账款支付
启动年度调研评估，采取"车企定期报送 + 样本供应商抽查"，每家随机抽取样本供应商
不少于 15 家。硬指标：中小企业账期不超过 60 天、全部采用现金支付；非中小企业
账期符合 60 天要求，现金和银行承兑汇票支付比例不低于 80%。工信部同日明确，对
应付账款规模大、故意拉长账期、供应商投诉集中的车企，联合约谈、督促整改。
市场端：蔚来-SW 11 月 17 日早盘盘中跌超 5%，蔚来在首批纳入评估车企之列。
背景数据：前三季度整车利润率 3.3%，上半年整车制造环节利润率 1.5%。
风格：克制传媒风，白底、低饱和配色、标题即结论
输出目录 = 脚本所在目录
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

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

    fig.text(0.045, 0.955, "两类供应商，两套付款标准", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.888, "账期都卡在 60 天，区别在拿什么结算",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    panels = [
        (0.020, "中小企业供应商", NAVY, "全部现金", "不接受票据替代"),
        (0.520, "非中小企业供应商", RED, "≥ 80%", "现金与银行承兑汇票合计"),
    ]

    for x0, title, color, big, big_note in panels:
        ax.add_patch(Rectangle((x0, 0.240), 0.460, 0.540, facecolor=PALE,
                               edgecolor=LIGHT, linewidth=1.0))
        ax.add_patch(Rectangle((x0, 0.767), 0.460, 0.013, facecolor=color,
                               edgecolor="none"))
        ax.text(x0 + 0.038, 0.720, title, fontsize=13, color=color,
                weight="bold", va="center")

        # 账期
        ax.text(x0 + 0.038, 0.638, "账期上限", fontsize=9.4, color=GRAY,
                va="center")
        ax.text(x0 + 0.038, 0.556, "≤60", fontsize=42, color=DARK,
                weight="bold", va="center", ha="left")
        ax.text(x0 + 0.238, 0.536, "天", fontsize=17, color=DARK,
                weight="bold", va="center")

        ax.plot([x0 + 0.038, x0 + 0.422], [0.480, 0.480], color=LIGHT,
                linewidth=1.0)

        # 支付方式
        ax.text(x0 + 0.038, 0.424, "支付方式", fontsize=9.4, color=GRAY,
                va="center")
        ax.text(x0 + 0.038, 0.348, big, fontsize=24, color=color,
                weight="bold", va="center")
        ax.text(x0 + 0.038, 0.282, big_note, fontsize=9.2, color=SLATE,
                va="center")

    punchline(fig, "账期只是形式，真正收紧的是「能不能用票据拖」。")
    footer(fig, "据 2026 年 11 月 16 日中汽协通知的评估指标整理；承兑汇票折价成本未在指标中体现。")
    fig.savefig(OUT + "图1_两套标准.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.135, 0.910, 0.690])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "从倡议，到可以核查", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.888, "17 家重点车企的账期，进入年度评估流程",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    steps = [
        ("01", "车企定期报送", "账期与支付方式自报", SLATE),
        ("02", "样本供应商抽查", "每家随机抽取不少于 15 家", NAVY),
        ("03", "评估与公示", "报送与抽查结果对账", SLATE),
        ("04", "约谈与整改", "工信部对问题车企督促", RED),
    ]

    w, gap = 0.215, 0.037
    y0, h = 0.400, 0.300
    for i, (no, title, note, color) in enumerate(steps):
        x0 = 0.015 + i * (w + gap)
        ax.add_patch(Rectangle((x0, y0), w, h, facecolor=PALE,
                               edgecolor=LIGHT, linewidth=1.0))
        ax.add_patch(Rectangle((x0, y0 + h - 0.012), w, 0.012, facecolor=color,
                               edgecolor="none"))
        ax.text(x0 + 0.022, y0 + h - 0.062, no, fontsize=12, color=GRAY,
                weight="bold", va="center")
        ax.text(x0 + 0.022, y0 + h - 0.135, title, fontsize=12.2, color=color,
                weight="bold", va="center")
        ax.text(x0 + 0.022, y0 + 0.070, note, fontsize=9.2, color=DARK,
                va="center")

        if i < len(steps) - 1:
            ax.annotate("", xy=(x0 + w + gap - 0.004, y0 + h / 2),
                        xytext=(x0 + w + 0.004, y0 + h / 2),
                        arrowprops=dict(arrowstyle="-|>", color=GRAY,
                                        linewidth=1.4, shrinkA=0, shrinkB=0))

    ax.text(0.015, 0.300, "此前是行业倡议，现在是可被抽查、可被对账的材料",
            fontsize=10.2, color=DARK, va="center")

    ax.plot([0.015, 0.985], [0.245, 0.245], color=LIGHT, linewidth=1.1)
    ax.text(0.015, 0.190, "随机抽取的意义：车企知道会被查，但不知道查谁",
            fontsize=9.6, color=GRAY, va="center")

    punchline(fig, "倡议靠自觉，抽查靠证据。")
    footer(fig, "据 2026 年 11 月 16 日中汽协通知与工信部同日表态整理；评估与公示的具体形式尚未披露。")
    fig.savefig(OUT + "图2_评估闭环.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.135, 0.910, 0.690])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "利润薄到 1.5%，账期就成了钱", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.888, "利润率与占用供应商资金之间，是替代关系",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    rows = [
        (0.560, "前三季度 · 整车利润率", 3.3, NAVY),
        (0.360, "上半年 · 整车制造环节利润率", 1.5, RED),
    ]
    scale, base_x = 0.400 / 4.0, 0.140

    for y, label, val, color in rows:
        ax.text(base_x, y + 0.135, label, fontsize=9.8, color=SLATE,
                va="center")
        ax.add_patch(Rectangle((base_x, y), scale * val, 0.105,
                               facecolor=color, edgecolor="none"))
        ax.text(base_x + scale * val + 0.018, y + 0.052, f"{val}%",
                fontsize=15, color=color, weight="bold", va="center")

    # 右侧：股价反应
    ax.add_patch(Rectangle((0.600, 0.340), 0.375, 0.380, facecolor=PALE,
                           edgecolor=LIGHT, linewidth=1.0))
    ax.add_patch(Rectangle((0.600, 0.707), 0.375, 0.013, facecolor=RED,
                           edgecolor="none"))
    ax.text(0.628, 0.658, "蔚来-SW", fontsize=12, color=RED, weight="bold",
            va="center")
    ax.text(0.628, 0.560, "盘中跌超 5%", fontsize=19, color=RED,
            weight="bold", va="center")
    ax.text(0.628, 0.470, "11 月 17 日早盘", fontsize=9.4, color=GRAY,
            va="center")
    ax.text(0.628, 0.408, "首批纳入评估车企之列", fontsize=9.6, color=DARK,
            va="center")

    ax.text(0.140, 0.240, "账期曾是无需付息的短期资金；规范化之后，这部分要另外找",
            fontsize=9.6, color=GRAY, va="center")

    punchline(fig, "利润率越薄，账期越像一笔不用付息的贷款。")
    footer(fig, "利润率据前三季度整车 3.3%、上半年整车制造环节 1.5% 的公开口径；蔚来跌幅为 11 月 17 日早盘盘中数据。")
    fig.savefig(OUT + "图3_利润与跌幅.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")