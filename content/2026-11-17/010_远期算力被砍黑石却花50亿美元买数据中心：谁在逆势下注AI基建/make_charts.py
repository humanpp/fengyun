# -*- coding: utf-8 -*-
"""
《远期算力被砍，黑石却花 50 亿美元买数据中心：谁在逆势下注 AI 基建？》配套图表
事实口径：SemiAnalysis 大幅下修远期算力预测的同时，算力基础设施资产化交易仍在
推进——黑石数字基础设施信托以约 50 亿美元收购亚马逊一处数据中心资产包 75% 股权，
AWS 将全部资产回租、初始租期 12 年；诺基亚、Telia 等五家企业组建 AI 超级工厂
联盟，拟竞标欧盟 AI 算力项目。
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


def box(ax, x0, y0, w, h, color=NAVY, facecolor=PALE):
    ax.add_patch(Rectangle((x0, y0), w, h, facecolor=facecolor,
                           edgecolor=LIGHT, linewidth=1.0))
    ax.add_patch(Rectangle((x0, y0 + h - 0.012), w, 0.012, facecolor=color,
                           edgecolor="none"))


# ---------------------------------------------------------------- 图 1
def fig1():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.135, 0.910, 0.690])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "50 亿美元，买的是租约", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.888, "黑石数字基础设施信托收购亚马逊一处数据中心资产包 75% 股权",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    # 上层两个主体
    box(ax, 0.070, 0.620, 0.360, 0.170, NAVY)
    ax.text(0.250, 0.735, "黑石数字基础设施信托", fontsize=12.5, color=NAVY,
            weight="bold", ha="center", va="center")
    ax.text(0.250, 0.668, "出资方 · 买方", fontsize=9.4, color=GRAY,
            ha="center", va="center")

    box(ax, 0.570, 0.620, 0.360, 0.170, SLATE)
    ax.text(0.750, 0.735, "AWS 亚马逊云科技", fontsize=12.5, color=SLATE,
            weight="bold", ha="center", va="center")
    ax.text(0.750, 0.668, "原业主 · 承租人", fontsize=9.4, color=GRAY,
            ha="center", va="center")

    # 中间资产包
    box(ax, 0.250, 0.330, 0.500, 0.150, RED)
    ax.text(0.500, 0.435, "数据中心资产包", fontsize=13, color=DARK,
            weight="bold", ha="center", va="center")
    ax.text(0.500, 0.372, "实体设施，不是芯片", fontsize=9.4, color=GRAY,
            ha="center", va="center")

    # 箭头
    ax.annotate("", xy=(0.250, 0.487), xytext=(0.250, 0.612),
                arrowprops=dict(arrowstyle="-|>", color=NAVY, linewidth=1.6,
                                shrinkA=0, shrinkB=0))
    ax.text(0.270, 0.550, "出资约 50 亿美元\n购入 75% 股权", fontsize=9.4,
            color=NAVY, ha="left", va="center", linespacing=1.8)

    ax.annotate("", xy=(0.750, 0.487), xytext=(0.750, 0.612),
                arrowprops=dict(arrowstyle="-|>", color=RED, linewidth=1.6,
                                shrinkA=0, shrinkB=0))
    ax.text(0.730, 0.550, "保留 25% 股权\n全部资产回租", fontsize=9.4,
            color=RED, ha="right", va="center", linespacing=1.8)

    # 底部三条
    ax.plot([0.070, 0.930], [0.262, 0.262], color=LIGHT, linewidth=1.1)
    notes = [
        ("初始租期", "12 年"),
        ("现金流", "租金可预期"),
        ("标的价格", "与算力斜率无关"),
    ]
    for i, (label, value) in enumerate(notes):
        x = 0.070 + i * 0.300
        ax.text(x, 0.185, label, fontsize=9.2, color=GRAY, va="center")
        ax.text(x, 0.130, value, fontsize=12.5, color=DARK, weight="bold",
                va="center")

    punchline(fig, "买的是未来十二年的租金，不是明年的算力需求。")
    footer(fig, "据黑石数字基础设施信托收购交易公开口径整理；「与算力斜率无关」为作者判断。")
    fig.savefig(OUT + "图1_交易结构.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.135, 0.910, 0.690])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "被砍的年份，全在租期里面", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.888, "租约覆盖 2026—2038，被下修的三年落在里面",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    def xpos(year):
        return 0.080 + (year - 2026) / 12.0 * 0.880

    # 租期条
    ax.add_patch(Rectangle((xpos(2026), 0.680), xpos(2038) - xpos(2026), 0.085,
                           facecolor=NAVY, edgecolor="none"))
    ax.text(xpos(2026) + 0.020, 0.722, "初始租期 12 年", fontsize=10.6,
            color="white", weight="bold", va="center")

    # 时间轴
    ax.plot([xpos(2026), xpos(2038)], [0.620, 0.620], color=LIGHT,
            linewidth=1.6)
    for yr in (2026, 2034, 2038):
        x = xpos(yr)
        ax.plot([x, x], [0.620, 0.605], color=LIGHT, linewidth=1.2)
        ax.text(x, 0.572, str(yr), fontsize=9.4, color=GRAY, ha="center",
                va="center")

    # 下修年份
    marks = [(2028, "−28%"), (2029, "−41%"), (2030, "−40%")]
    for yr, pct in marks:
        x = xpos(yr)
        ax.plot([x, x], [0.680, 0.430], color=RED, linewidth=1.2,
                linestyle=(0, (3, 3)))
        ax.scatter([x], [0.680], s=110, facecolor=RED, edgecolor="white",
                   linewidth=1.6, zorder=4)
        ax.text(x, 0.390, pct, fontsize=11.5, color=RED, weight="bold",
                ha="center", va="center")

    ax.text(xpos(2026), 0.335, "SemiAnalysis 下修的三年", fontsize=9.4,
            color=RED, va="center")

    # 分隔与结论
    ax.plot([0.070, 0.930], [0.285, 0.285], color=LIGHT, linewidth=1.1)
    ax.text(0.070, 0.225, "下修改的是预测曲线；租约是已经签好的合同", fontsize=10.4,
            color=DARK, va="center")

    punchline(fig, "预测可以改，合同不能。")
    footer(fig, "租期为交易披露的初始 12 年，按 2026 年起算示意；下修幅度为 SemiAnalysis 2028—2030 年资本开支口径。")
    fig.savefig(OUT + "图2_租期覆盖.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.135, 0.910, 0.690])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "一边买存量，一边赌增量", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.888, "同一周里，两笔性质不同的钱", fontsize=10.8,
             color=GRAY, ha="left", va="top")

    top, bot = 0.840, 0.250

    panels = [
        (0.020, "存量：已建成的资产", NAVY, [
            ("主体", "黑石数字基础设施信托"),
            ("动作", "收购 75% 股权，约 50 亿美元"),
            ("收益", "AWS 全额回租，租期 12 年"),
            ("性质", "买现金流，确定性优先"),
        ]),
        (0.530, "增量：还没建的项目", RED, [
            ("主体", "诺基亚、Telia 等五家企业"),
            ("动作", "组建 AI 超级工厂联盟"),
            ("目标", "竞标欧盟 AI 算力项目"),
            ("性质", "赌建设，方向性下注"),
        ]),
    ]

    for x0, title, color, rows in panels:
        ax.add_patch(Rectangle((x0, bot), 0.450, top - bot, facecolor=PALE,
                               edgecolor=LIGHT, linewidth=1.0))
        ax.add_patch(Rectangle((x0, top - 0.013), 0.450, 0.013, facecolor=color,
                               edgecolor="none"))
        ax.text(x0 + 0.030, top - 0.062, title, fontsize=13.5, color=color,
                weight="bold", va="center")
        for i, (label, value) in enumerate(rows):
            y = 0.700 - i * 0.120
            ax.text(x0 + 0.030, y, label, fontsize=9.4, color=GRAY,
                    va="center")
            ax.text(x0 + 0.030, y - 0.052, value, fontsize=11.0, color=DARK,
                    weight="bold", va="center")
            if i < len(rows) - 1:
                ax.plot([x0 + 0.030, x0 + 0.420], [y - 0.086, y - 0.086],
                        color=LIGHT, linewidth=0.9)

    punchline(fig, "一个买已经建好的，一个赌还没建的。")
    footer(fig, "据黑石收购交易与五家企业联盟公开口径整理；「存量／增量」与性质判断为作者归纳，非当事方表述。")
    fig.savefig(OUT + "图3_存量与增量.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")