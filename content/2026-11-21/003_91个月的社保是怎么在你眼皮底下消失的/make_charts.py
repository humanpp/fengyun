# -*- coding: utf-8 -*-
"""
《91 个月的社保，是怎么在你眼皮底下消失的》配套图表

事实口径（全部来自公开报道）：
  · 芦玉菲，2000 年 3 月生，河南郑州人，2014 年入选国家体操队，
    2021 年东京奥运会高低杠第四名，后转型裁判。
  · 她晒出的《河南省机关事业单位基本养老保险个人账户查询单》：
    参加工作 2011-01-01；参保缴费 2016-09-01；缴费状态"暂停缴费（中断）"；
    2016-09 至 2024-03 共 91 个月欠费；
    单位欠费 102,260.32 元，个人欠费本金 47,686.24 元，合计 149,946.56 元。
  · 11-18 下午发文求助；当晚称官方已介入；11-19 上午称欠缴部分已全部缴纳。
  · 原博文此后在其主页无法查看。

来源：澎湃新闻（转观察者网）2026-11-19、凤凰网体育 2026-11-19 等。
风格：克制传媒风，白底、低饱和配色、标题即结论。
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

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
BLUSH = "#fbf1ef"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep

Y_TITLE = 0.958
Y_SUB = 0.898
Y_PUNCH = 0.072
Y_FOOT = 0.020


def header(fig, title, sub):
    fig.text(0.045, Y_TITLE, title, fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, Y_SUB, sub, fontsize=10.8, color=GRAY,
             ha="left", va="top")


def footer(fig, text):
    fig.text(0.045, Y_FOOT, text, fontsize=8.0, color=GRAY,
             ha="left", va="bottom")


def punchline(fig, text):
    fig.text(0.045, Y_PUNCH, text, fontsize=10.4, color=DARK,
             ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


def card(ax, x, y, w, h, edge, face="white", lw=1.0):
    # 底 zorder=2：卡内色块画在 3 层，文字在 4 层
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.004,rounding_size=0.014",
        facecolor=face, edgecolor=edge, linewidth=lw, zorder=2))


def new_axes(fig):
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return ax


# ---------------------------------------------------------------- 图 1
def fig1():
    fig = plt.figure(figsize=(12, 7.2))
    ax = new_axes(fig)

    header(fig, "91 个格子，就是 91 个月",
           "2011 年 1 月到 2024 年 3 月，159 个月里，缴费记录是空的")

    # 月格矩阵：2011-01 起共 159 个月（含首含尾）
    cols, cell_w, cell_h = 16, 0.0455, 0.0232
    x0, y_top = 0.078, 0.735
    gapx = 0.0088
    gapy = 0.0090

    for m in range(159):
        r, c = divmod(m, cols)
        x = x0 + c * (cell_w + gapx)
        y = y_top - r * (cell_h + gapy)
        if m < 68:          # 2011-01 .. 2016-08：无缴费记录 68 个月
            face, edge = "#e9ebef", "none"
        else:               # 2016-09 .. 2024-03：欠费 91 个月
            face, edge = NAVY, "none"
        ax.add_patch(Rectangle((x, y), cell_w, cell_h, facecolor=face,
                               edgecolor=edge, linewidth=0.5, zorder=3))

    # 图例
    ly = y_top - 10 * (cell_h + gapy) - 0.035
    ax.add_patch(Rectangle((x0, ly), 0.022, cell_h, facecolor="#e9ebef",
                           edgecolor="none", zorder=3))
    ax.text(x0 + 0.030, ly + cell_h / 2, "68 个月：无缴费记录 (2011.01–2016.08)",
            fontsize=9.6, color=SLATE, ha="left", va="center")

    ly2 = ly - 0.040
    ax.add_patch(Rectangle((x0, ly2), 0.022, cell_h, facecolor=NAVY,
                           edgecolor="none", zorder=3))
    ax.text(x0 + 0.030, ly2 + cell_h / 2, "91 个月：欠费 (2016.09–2024.03)",
            fontsize=9.6, color=NAVY, ha="left", va="center", weight="bold")

    # 右侧：两个日期
    ax.text(0.640, ly + 0.004, "参加工作：2011-01-01", fontsize=10.6,
            color=SLATE, ha="left", va="center")
    ax.text(0.640, ly2 + 0.004, "参保缴费：2016-09-01", fontsize=10.6,
            color=NAVY, ha="left", va="center", weight="bold")

    # 下方：补齐的速度
    yb = 0.170
    ax.add_patch(Rectangle((0.078, yb), 0.580, 0.060, facecolor=BLUSH,
                           edgecolor=RED, linewidth=1.2, zorder=3))
    ax.text(0.092, yb + 0.030, "11-18 下午发文", fontsize=9.8, color=RED,
            ha="left", va="center", weight="bold", zorder=4)
    ax.text(0.644, yb + 0.030, "11-19 上午补齐", fontsize=9.8, color=RED,
            ha="right", va="center", weight="bold", zorder=4)
    ax.text(0.700, yb + 0.030, "← 分开算，这段不到一天", fontsize=10.0,
            color=RED, ha="left", va="center")

    punchline(fig, "91 个月没人发现；公开发文后，一天之内补完。")
    footer(fig, "数据来源：澎湃新闻（转观察者网）2026-11-19；查询单为《河南省机关事业单位基本养老保险个人账户查询单》")
    fig.savefig(OUT + "图1_91个格子.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(12, 6.8))
    ax = new_axes(fig)

    header(fig, "近 15 万，是谁欠的",
           "单位欠费 102,260.32 元，个人欠费本金 47,686.24 元")

    # 堆叠条：单位 68.2%，个人 31.8%
    total = 149946.56
    unit = 102260.32
    own = 47686.24
    w_total, x0, y0, h = 0.880, 0.060, 0.520, 0.075

    w_unit = w_total * (unit / total)
    w_own = w_total * (own / total)

    ax.add_patch(Rectangle((x0, y0), w_unit, h, facecolor=NAVY,
                           edgecolor="none", zorder=3))
    ax.add_patch(Rectangle((x0 + w_unit, y0), w_own, h, facecolor=RED,
                           edgecolor="none", zorder=3))

    ax.text(x0 + 0.012, y0 + h + 0.040, "单位", fontsize=11.0, color=NAVY,
            weight="bold", ha="left", va="center")
    ax.text(x0 + 0.012, y0 + h + 0.012, "102,260.32 元 · 约 68%", fontsize=10.0,
            color=NAVY, ha="left", va="center")

    ax.text(x0 + w_total - 0.012, y0 + h + 0.040, "个人（本金）", fontsize=11.0,
            color=RED, weight="bold", ha="right", va="center")
    ax.text(x0 + w_total - 0.012, y0 + h + 0.012, "47,686.24 元 · 约 32%",
            fontsize=10.0, color=RED, ha="right", va="center")

    ax.text(0.500, 0.432, "合计 149,946.56 元", fontsize=17.0, color=DARK,
            weight="bold", ha="center", va="center")

    # 三个说明块
    notes = [
        ("这不是罚款", "是本来该缴没缴的部分——\n补上，只是回到原位。"),
        ("个人那部分也从没缴", "所以不是单位垫了钱、\n个人不出，而是两边都空着。"),
        ("查询单上的状态", "写的是“暂停缴费（中断）”，\n不是“欠费”两个字。"),
    ]
    card_top, card_bot = 0.372, 0.196
    gap = 0.020
    left, right = 0.060, 0.940
    w = (right - left - gap * 2) / 3
    for i, (t, b) in enumerate(notes):
        x = left + i * (w + gap)
        card(ax, x, card_bot, w, card_top - card_bot, LIGHT, lw=1.0)
        ax.text(x + w / 2, card_top - 0.052, t, fontsize=10.6, color=NAVY,
                weight="bold", ha="center", va="center", zorder=4)
        ax.text(x + w / 2, card_bot + (card_top - card_bot) * 0.40, b,
                fontsize=9.4, color=SLATE, ha="center", va="center",
                linespacing=1.60, zorder=4)

    punchline(fig, "十五万里，有近五万是她自己那份——也从没交过。")
    footer(fig, "数据来源：《河南省机关事业单位基本养老保险个人账户查询单》，据澎湃新闻 2026-11-19 引述")
    fig.savefig(OUT + "图2_近15万是谁欠的.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(12, 6.6))
    ax = new_axes(fig)

    header(fig, "今晚看一眼：两个日期，一个状态",
           "不用等出事才查，三分钟能看完")

    items = [
        ("找到缴费记录", "掌上 12333、支付宝或微信的社保查询，\n看最近 12 个月有没有“断”。"),
        ("看两个日期", "“参加工作（参保）日期”和“参保缴费日期”。\n两个日期之间那段，就是可能空着的。"),
        ("看一个状态", "缴费状态写的是“正常”“暂停”\n还是“中断”。"),
        ("分清险种和体系", "企业职工养老、机关事业单位养老是两套；\n单位属机关事业的，要去对应渠道单独查。"),
    ]

    top, h, gap = 0.760, 0.132, 0.024
    for i, (title, body) in enumerate(items):
        y = top - i * (h + gap) - h
        card(ax, 0.060, y, 0.880, h, LIGHT, lw=1.0)
        ax.text(0.088, y + h / 2, f"{i + 1}", fontsize=17, color=LIGHT,
                weight="bold", ha="center", va="center", zorder=4)
        ax.text(0.120, y + h * 0.700, title, fontsize=12.4, color=NAVY,
                weight="bold", ha="left", va="center", zorder=4)
        ax.text(0.120, y + h * 0.300, body, fontsize=9.6, color=SLATE,
                ha="left", va="center", linespacing=1.55, zorder=4)

    punchline(fig, "她查得太晚，但还是查到了；多数人是压根没打开过。")
    footer(fig, "查询入口以各地人社部门公布为准；图示为通用路径，非官方界面截图")
    fig.savefig(OUT + "图3_两个日期一个状态.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)
