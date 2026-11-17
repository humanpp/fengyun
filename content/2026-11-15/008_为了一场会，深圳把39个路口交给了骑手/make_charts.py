# -*- coding: utf-8 -*-
"""
《为了一场会，深圳把 39 个路口交给了骑手》配套图表
事实来源：深圳特区报·读特 2026-11-13 报道；深圳市公安局 APEC 交通管控通告
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
    fig.subplots_adjust(left=0.045, right=0.955, top=0.760, bottom=0.175)

    fig.suptitle("为这 5 天，投下去的东西",
                 fontsize=19, color=DARK, x=0.045, ha="left", y=0.955, weight="bold")
    fig.text(0.045, 0.885,
             "美团在深圳推出的骑手保障十项举措，关键数字一览",
             fontsize=10.8, color=GRAY, ha="left")

    ax.set_xlim(0, 1)
    ax.set_ylim(1.60, 4.72)
    ax.axis("off")

    cards = [
        (0.025, 3.28, "800 万元", "交通安全激励补贴", "专项投入", NAVY),
        (0.345, 3.28, "39 个", "重点路口交通志愿服务", "覆盖 6 个行政区", NAVY),
        (0.665, 3.28, "数百名", "骑手参与早晚高峰劝导", "脱产期间权益不变", RED),
        (0.025, 1.78, "十多个", "团队组建应急保障专班", "技术、调度、安全、客服等", NAVY),
        (0.345, 1.78, "20 次/日", "出餐慢上报上限", "不区分订单品类", RED),
        (0.665, 1.78, "2–3 单", "最高接单负载下调", "按经验与意愿调整", NAVY),
    ]

    for x0, y0, big, mid, small, color in cards:
        ax.add_patch(plt.Rectangle((x0, y0), 0.310, 1.32,
                                   facecolor=PALE, edgecolor=LIGHT, linewidth=1.0))
        ax.add_patch(plt.Rectangle((x0, y0 + 1.24), 0.310, 0.08,
                                   facecolor=color, edgecolor="none"))
        ax.text(x0 + 0.155, y0 + 0.86, big, fontsize=21, color=color,
                weight="bold", ha="center")
        ax.text(x0 + 0.155, y0 + 0.48, mid, fontsize=9.8, color=DARK, ha="center")
        ax.text(x0 + 0.155, y0 + 0.20, small, fontsize=9.0, color=GRAY, ha="center")

    takeaway(fig, 0.080, "清单很长。长到值得问一句：一场会，为什么需要这么多骑手站在路口？")

    footer(fig, "数据：深圳特区报·读特 2026-11-13 报道《美团在深圳推出骑手保障十项举措》。")
    fig.savefig(OUT + "图1_投下去的东西.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig, ax = plt.subplots(figsize=(12, 6.8))
    fig.subplots_adjust(left=0.045, right=0.955, top=0.750, bottom=0.175)

    fig.suptitle("这 5 天，骑手的身份被改写了三次",
                 fontsize=19, color=DARK, x=0.045, ha="left", y=0.955, weight="bold")
    fig.text(0.045, 0.880,
             "三重身份叠在同一个人身上——越往上越是这 5 天才有的，越往下越是本行",
             fontsize=10.6, color=GRAY, ha="left")

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 4.60)
    ax.axis("off")

    # 从上到下：最临时 → 最稳定
    layers = [
        ("第三重｜城市形象", "会期前后", "餐箱贴、定制工装、文明宣导", RED, "最临时"),
        ("第二重｜交通志愿者", "10.22 — 12.31", "39 个路口劝导，脱产权益不变＋现金激励", NAVY, "阶段性"),
        ("第一重｜配送员", "全年", "送餐、接单、面对倒计时", GRAY, "本职"),
    ]

    for i, (title, when, what, color, tag) in enumerate(layers):
        y = 3.78 - i * 1.14
        ax.add_patch(plt.Rectangle((0.030, y - 0.50), 0.940, 1.00,
                                   facecolor=PALE, edgecolor=color, linewidth=1.4))
        ax.add_patch(plt.Rectangle((0.030, y - 0.50), 0.008, 1.00,
                                   facecolor=color, edgecolor="none"))
        ax.text(0.062, y + 0.24, title, fontsize=12.5, color=color,
                weight="bold", va="center")
        ax.text(0.062, y - 0.06, when, fontsize=10.2, color=DARK, va="center")
        ax.text(0.062, y - 0.34, what, fontsize=9.6, color=GRAY, va="center")
        ax.text(0.950, y + 0.10, tag, fontsize=11, color=color,
                weight="bold", ha="right", va="center",
                bbox=dict(boxstyle="round,pad=0.42", facecolor="white",
                          edgecolor=color, linewidth=1.1))

    fig.text(0.045, 0.080,
             "被改写的不只是工作内容，还有“他是谁”；而被收回的，也是这个“他是谁”。",
             fontsize=10.4, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))

    footer(fig, "据美团 2026-11-13 骑手保障十项举措公开内容整理。")
    fig.savefig(OUT + "图2_三重身份.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig, ax = plt.subplots(figsize=(12, 6.8))
    fig.subplots_adjust(left=0.045, right=0.955, top=0.760, bottom=0.170)

    fig.suptitle("一件事铺得很长，另一件只铺了 5 天",
                 fontsize=19, color=DARK, x=0.045, ha="left", y=0.955, weight="bold")
    fig.text(0.045, 0.885,
             "形象类安排与权益类让渡，时间跨度不在同一个量级",
             fontsize=10.8, color=GRAY, ha="left")

    ax.set_xlim(0, 1)
    ax.set_ylim(0.88, 3.80)
    ax.axis("off")

    # 时间轴（10.22 — 12.31）
    ax.plot([0.10, 0.94], [1.28, 1.28], color=LIGHT, lw=2.4)
    for x, label in [(0.10, "10.22"), (0.34, "11.13"), (0.46, "11.16"),
                     (0.62, "11.18"), (0.70, "11.20"), (0.94, "12.31")]:
        ax.plot([x, x], [1.22, 1.34], color=GRAY, lw=1.0)
        ax.text(x, 1.08, label, fontsize=9.4, color=GRAY, ha="center")

    # 长条：形象类（10.22—12.31）
    ax.add_patch(plt.Rectangle((0.10, 2.82), 0.84, 0.46,
                               facecolor=NAVY, edgecolor="none"))
    ax.text(0.52, 3.05, "交通安全志愿服务 · 餐箱贴 · 定制工装  10.22 — 12.31",
            fontsize=10.6, color="white", ha="center", va="center", weight="bold")
    ax.text(0.10, 3.50, "约 70 天", fontsize=11.5, color=NAVY, weight="bold")

    # 短条：权益类（11.16—11.20）
    ax.add_patch(plt.Rectangle((0.46, 1.92), 0.24, 0.46,
                               facecolor=RED, edgecolor="none"))
    ax.text(0.58, 2.15, "超时免责 · 降负载 · 积分保护", fontsize=9.4,
            color="white", ha="center", va="center", weight="bold")
    ax.text(0.58, 2.56, "5 天", fontsize=12, color=RED, weight="bold",
            ha="center")

    # 指引线
    ax.plot([0.10, 0.10], [2.82, 1.36], color=NAVY, lw=1.0, ls=(0, (3, 3)))
    ax.plot([0.94, 0.94], [2.82, 1.36], color=NAVY, lw=1.0, ls=(0, (3, 3)))
    ax.plot([0.46, 0.46], [1.92, 1.36], color=RED, lw=1.0, ls=(0, (3, 3)))
    ax.plot([0.70, 0.70], [1.92, 1.36], color=RED, lw=1.0, ls=(0, (3, 3)))

    takeaway(fig, 0.080, "“让骑手成为城市形象的一部分”是长期项目，“让他少担一点超时风险”是临时措施。")

    footer(fig, "据美团 2026-11-13 骑手保障十项举措：志愿服务 10.22—12.31，免责 11.16—11.20。")
    fig.savefig(OUT + "图3_两条时间跨度.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")