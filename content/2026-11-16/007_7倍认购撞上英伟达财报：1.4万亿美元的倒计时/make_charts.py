# -*- coding: utf-8 -*-
"""
《7 倍认购，1.4 万亿美元：倒计时握在英伟达手里》配套图表
事实来源：彭博社/法新社 2026-11-16 关于 7 倍超额认购的报道、
Anthropic 2026-11-10 修订版招股文件、高盛预测模型（经 FT/彭博转述）、
新华财经/TradingKey 关于英伟达 FY27Q3 财报的报道
风格：克制传媒风，白底、低饱和配色、标题即结论
输出目录 = 脚本所在目录
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch
from matplotlib.lines import Line2D

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
SAND = "#b9a887"
ROSE = "#e3c7c3"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep


def canvas(fig):
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return ax


def footer(fig, text):
    fig.text(0.045, 0.035, text, fontsize=8.4, color=GRAY, ha="left", va="bottom")


def takeaway(fig, y, text, size=10.4):
    fig.text(0.045, y, text, fontsize=size, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


def head(fig, title, sub):
    fig.text(0.045, 0.935, title, fontsize=19, color=DARK, ha="left",
             va="center", weight="bold")
    fig.text(0.045, 0.868, sub, fontsize=10.8, color=GRAY, ha="left", va="center")


# ---------------------------------------------------------------- 图 1
def fig1():
    fig = plt.figure(figsize=(12, 6.8))
    ax = canvas(fig)
    head(fig, "7 倍里，只有 260 亿是安排好的",
         "904 亿美元的交易规模；约 6300 亿美元的意向订单为按倍数粗算")

    # ---- 上：一份供给 vs 六份超额需求（同一比例尺）
    fig.text(0.045, 0.780, "一份供给，六份超额需求", fontsize=13, color=DARK,
             weight="bold", va="center")
    fig.text(0.045, 0.735, "同一比例尺：每个方块 = 904 亿美元（可供股份）",
             fontsize=10.2, color=GRAY, va="center")

    x0, w, gap = 0.055, 0.1254, 0.002
    y0, h = 0.600, 0.100
    for i in range(7):
        x = x0 + i * (w + gap)
        face = NAVY if i == 0 else ROSE
        ax.add_patch(Rectangle((x, y0), w, h, facecolor=face,
                               edgecolor="white", linewidth=1.2))
        if i == 0:
            ax.text(x + w / 2, y0 + h / 2, "904 亿", fontsize=11, color="white",
                    ha="center", va="center", weight="bold")
        else:
            ax.text(x + w / 2, y0 + h / 2, f"{i + 1}×", fontsize=10,
                    color=RED, ha="center", va="center")

    ax.text(x0 + w / 2, 0.575, "可供股份", fontsize=9.6, color=NAVY,
            ha="center", va="center", weight="bold")
    ax.text(x0 + w + gap + (6 * w + 5 * gap) / 2, 0.575,
            "超额需求：想买但因配售而拿不到的部分", fontsize=9.6,
            color=RED, ha="center", va="center")

    # ---- 下：904 亿怎么拼
    fig.text(0.045, 0.480, "904 亿怎么拼", fontsize=13, color=DARK,
             weight="bold", va="center")
    fig.text(0.045, 0.435, "70—78 美元的定价区间、8.25 亿股；七家基石承诺 260 亿，上市后立即到位",
             fontsize=10.2, color=GRAY, va="center")

    left, right = 0.055, 0.945
    span = right - left
    yb, hb = 0.330, 0.070
    cut = left + span * 644 / 904
    ax.add_patch(Rectangle((left, yb), cut - left, hb, facecolor=NAVY,
                           edgecolor="none"))
    ax.add_patch(Rectangle((cut, yb), right - cut, hb, facecolor=RED,
                           edgecolor="none"))
    ax.text((left + cut) / 2, yb + hb / 2, "公开募资 最高 644 亿", fontsize=11,
            color="white", ha="center", va="center", weight="bold")
    ax.text((cut + right) / 2, yb + hb / 2, "基石 260 亿", fontsize=10.5,
            color="white", ha="center", va="center", weight="bold")

    # 260 亿内部：谷歌 100 / 英伟达 100 / 其余 60
    ys, hs = 0.245, 0.055
    parts = [("谷歌 100", 100, RED), ("英伟达 100", 100, RED), ("其余五家 60", 60, SAND)]
    cx = cut
    for name, v, color in parts:
        wv = span * v / 904
        ax.add_patch(Rectangle((cx, ys), wv, hs, facecolor="white",
                               edgecolor=color, linewidth=1.2))
        ax.plot([cx + wv / 2, cx + wv / 2], [yb, ys + hs], color=LIGHT, lw=0.9)
        ax.text(cx + wv / 2, ys + hs / 2, name, fontsize=8.6, color=DARK,
                ha="center", va="center")
        cx += wv

    ax.text(left, 0.210, "单位：亿美元；合计最高 904 亿，超过 SpaceX 的 862 亿",
            fontsize=9.2, color=GRAY, ha="left", va="center")

    takeaway(fig, 0.135, "所以 7 倍证明的是发行阶段的热度，证明不了 1.4 万亿的估值。")
    footer(fig, "据彭博社/法新社 2026-11-16 报道、Anthropic 2026-11-10 招股文件整理；6,300 亿为 904 亿乘 7 的粗算，非披露数据。")
    fig.savefig(OUT + "图1_七倍是什么概念.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(12, 6.8))
    head(fig, "904 亿不是利润，是油量",
         "高盛给潜在投资者的模型：营收冲到 6850 亿的那一年，自由现金流才转正")

    # ---- 左：营收路径
    fig.text(0.070, 0.790, "营收路径（亿美元）", fontsize=13, color=DARK,
             weight="bold", va="center")
    fig.text(0.070, 0.752, "高盛估 2027 年现金消耗约 660 亿美元", fontsize=9.6,
             color=GRAY, va="center")
    ax = fig.add_axes([0.075, 0.255, 0.495, 0.480])
    years = ["2026", "2027", "2029", "2030"]
    rev = [520, 1360, 4420, 6850]
    bars = ax.bar(years, rev, width=0.50, color=[NAVY, NAVY, NAVY, RED])
    for b, v in zip(bars, rev):
        ax.text(b.get_x() + b.get_width() / 2, v + 140, f"{v:,}", fontsize=11,
                color=DARK, ha="center", weight="bold")
    ax.set_ylim(0, 7900)
    ax.tick_params(axis="x", labelsize=11.5, colors=DARK)
    ax.tick_params(axis="y", labelsize=9, colors=GRAY, length=0)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(LIGHT)
    ax.grid(axis="y", color=LIGHT, lw=0.8, alpha=0.7)
    ax.set_axisbelow(True)
    ax.annotate("自由现金流转正", xy=(3, 6400), xytext=(1.42, 6300), fontsize=10.2,
                color=RED, weight="bold", va="center",
                arrowprops=dict(arrowstyle="->", color=RED, lw=1.2,
                                connectionstyle="arc3,rad=0"))
    fig.text(0.640, 0.790, "账单 vs 口袋（亿美元）", fontsize=13, color=DARK,
             weight="bold", va="center")
    fig.text(0.640, 0.752, "履约承诺几乎全是算力与数据中心，账期排到 2045 年",
             fontsize=9.6, color=GRAY, va="center")
    ax2 = fig.add_axes([0.640, 0.255, 0.310, 0.440])
    ax2.set_xlim(0, 2)
    ax2.set_ylim(0, 11200)
    ax2.axis("off")
    ax2.add_patch(Rectangle((0.34, 0), 0.32, 9000, facecolor=RED, edgecolor="none"))
    ax2.add_patch(Rectangle((1.24, 0), 0.32, 1320, facecolor=NAVY, edgecolor="none"))
    ax2.text(0.50, 9450, "9,000 亿", fontsize=12, color=RED, ha="center", weight="bold")
    ax2.text(1.40, 1650, "1,320 亿", fontsize=12, color=NAVY, ha="center", weight="bold")
    ax2.text(0.50, -520, "履约承诺", fontsize=10.2, color=DARK, ha="center", va="top")
    ax2.text(1.40, -520, "现金及短期投资", fontsize=10.2, color=DARK, ha="center",
             va="top")
    ax2.text(1.00, 4200, "×6.8", fontsize=13, color=GRAY, ha="center", weight="bold")
    ax2.text(0.50, -1900, "其中约 700 亿一年内到期", fontsize=8.8, color=GRAY,
             ha="center", va="center")

    takeaway(fig, 0.135, "904 亿够撑到下一个融资窗口打开，不够撑到现金流转正。")
    footer(fig, "高盛模型经金融时报、彭博、财讯快报转述；承诺与现金数据见 Anthropic 2026-11-10 招股文件（截至 9 月末）。")
    fig.savefig(OUT + "图2_账单在2030年那头.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(12, 6.8))
    ax = canvas(fig)
    head(fig, "三天，两个窗口",
         "11 月 17 日先由卖铲子的人开口，18 日买铲子的人定价，19 日开盘")

    # 泳道
    ax.add_patch(Rectangle((0.045, 0.600), 0.910, 0.200, facecolor="#f6f3ee",
                           edgecolor=LIGHT, linewidth=1.0))
    ax.add_patch(Rectangle((0.045, 0.300), 0.910, 0.240, facecolor=PALE,
                           edgecolor=LIGHT, linewidth=1.0))
    ax.text(0.075, 0.712, "产业端", fontsize=10.6, color=SAND, weight="bold",
            va="center")
    ax.text(0.075, 0.470, "资本端", fontsize=10.6, color=NAVY, weight="bold",
            va="center")

    # 产业端：一个事件
    ax.plot([0.235, 0.305], [0.712, 0.712], color=GRAY, lw=1.3,
            linestyle=(0, (3, 4)), zorder=1)
    ax.add_patch(plt.Circle((0.320, 0.712), 0.010, facecolor=RED,
                            edgecolor="white", linewidth=1.6, zorder=4))
    ax.text(0.320, 0.772, "11.17 盘后（北京时间 11.18 凌晨）", fontsize=9.8,
            color=RED, ha="left", va="center", weight="bold")
    ax.text(0.352, 0.712, "英伟达 FY27Q3 财报", fontsize=12.4, color=DARK,
            ha="left", va="center", weight="bold")
    ax.text(0.352, 0.662, "指引 1080–1092 亿；市场预期当季约 1090 亿，四季度指引看 1243 亿",
            fontsize=9.6, color=GRAY, ha="left", va="center")
    ax.text(0.352, 0.622, "黄仁勋辞任后的首份财报，电话会由临时 CEO 科莱特·克雷斯主持",
            fontsize=9.6, color=GRAY, ha="left", va="center")

    # 传导箭头
    ax.add_patch(FancyArrowPatch((0.320, 0.595), (0.320, 0.548),
                                 arrowstyle="-|>", mutation_scale=15,
                                 color=RED, lw=1.4, linestyle=(0, (4, 3))))
    ax.text(0.345, 0.572, "先回答“算力需求还在不在”", fontsize=9.6, color=RED,
            ha="left", va="center")

    # 资本端：三个事件
    ax.plot([0.235, 0.870], [0.470, 0.470], color=LIGHT, lw=2.2, zorder=1)
    cap = [
        (0.320, "11.18", "Anthropic 定价", "承销商按订单簿定价，260 亿锁在前面", NAVY),
        (0.565, "11.19", "以 ANT 开盘", "定价权从承销商交回市场", NAVY),
        (0.815, "+6 个月", "解禁", "那 260 亿还锁得住吗", GRAY),
    ]
    for x, date, what, note, color in cap:
        ax.add_patch(plt.Circle((x, 0.470), 0.010, facecolor=color,
                                edgecolor="white", linewidth=1.6, zorder=4))
        ax.text(x, 0.412, date, fontsize=9.8, color=color, weight="bold",
                ha="center", va="center")
        ax.text(x, 0.367, what, fontsize=11.4, color=DARK, weight="bold",
                ha="center", va="center")
        ax.text(x, 0.327, note, fontsize=9.2, color=GRAY, ha="center", va="center")

    takeaway(fig, 0.165, "顺序很别扭：定价前一天，估值叙事的裁判权在别人手上。")
    footer(fig, "财报时间与指引见英伟达 FY27Q2 财报指引（2026-08-26）及新华财经、TradingKey 11-16 报道；定价与挂牌时间见招股文件。")
    fig.savefig(OUT + "图3_三天两个窗口.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")
