# -*- coding: utf-8 -*-
"""
《10 个月登顶 22 级，然后呢》配套图表

事实口径：
  · 罗福莉 1995 年生于四川宜宾，北大计算语言学硕士，参与 DeepSeek-V2 研发；
    2024 年底被曝获雷军千万年薪邀约，2025 年 11 月正式加入小米任 MiMo 大模型负责人；
    2026 年 9 月 22 日小米内部晋升名单显示其升至 22 级，接近小米人士称
    这已是职级体系最高级别，从入职到登顶 10 个月。
  · 2026 年 7 月组织调整，MiMo 团队负责小爱同学基础模型；8 月超级小爱 2.0 接入 MiMo。
  · 团队管理：相对放权、研究氛围开放自由、不过度强调内部竞争与高强度节奏，
    更多依靠自我驱动，重视技术探索而非单纯榜单排名（华尔街见闻·全天候科技 2026-11-18）。
  · 薪酬参照：清华计算机系教授刘知远称组内大模型方向博士毕业生可拿 600 万元以上年薪，
    硕士百万元以上（《中国新闻周刊》2026-07-07）；字节 Top Seed 校招薪资
    2024 年约 150 万元 → 2025 年 300–500 万元 → 2026 年部分核心岗位突破 600 万元
    （据《晚点LatePost》，同上转述）。
  · 林俊旸（前阿里通义千问技术负责人）2026-08-12 宣布创办语用科技，
    产品未出即获 2.2 亿美元天使轮，投后估值 20 亿美元（约合人民币 133 亿元）。
  · 分拆传闻：2026-11-18 见报；11-23《资本不熬夜》称金山系等关联主体联合持股
    可能是方向之一。

输出目录 = 脚本所在目录
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei"]
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
TEAL = "#3f6f6b"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep

Y_TITLE = 0.958
Y_SUB = 0.898
Y_PUNCH = 0.068
Y_FOOT = 0.020


def header(fig, title, sub):
    fig.text(0.045, Y_TITLE, title, fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, Y_SUB, sub, fontsize=10.4, color=GRAY,
             ha="left", va="top")


def footer(fig, text):
    fig.text(0.045, Y_FOOT, text, fontsize=7.6, color=GRAY,
             ha="left", va="bottom")


def punchline(fig, text):
    fig.text(0.045, Y_PUNCH, text, fontsize=10.4, color=DARK,
             ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


def card(ax, x, y, w, h, edge, face="white", lw=1.2, z=2):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.004,rounding_size=0.014",
        facecolor=face, edgecolor=edge, linewidth=lw, zorder=z))


def new_axes(fig):
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return ax


# ---------------------------------------------------------------- 图 1
def fig1():
    """入职到 22 级，12 个月"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "10 个月，走到职级尽头",
           "2025 年 11 月加入，2026 年 9 月 22 日升至小米最高职级")

    ax.add_patch(FancyArrowPatch((0.070, 0.640), (0.940, 0.640),
                                 arrowstyle="-|>", mutation_scale=18,
                                 color=LIGHT, lw=2.0))

    nodes = [
        (0.105, "2025.11", "正式加入小米\n任 MiMo 负责人", GRAY),
        (0.320, "2026.07", "小爱同学基础模型\n交由 MiMo 团队", SLATE),
        (0.535, "2026.08", "超级小爱 2.0\n接入 MiMo", SLATE),
        (0.750, "2026.09.22", "升至 22 级\n入职满 10 个月", NAVY),
        (0.915, "2026.11.18", "分拆传闻见报", RED),
    ]
    for x, title, note, color in nodes:
        ax.plot([x], [0.640], "o", markersize=9, color=color,
                markeredgecolor="white", markeredgewidth=1.2, zorder=6)
        ax.text(x, 0.685, title, fontsize=10.4, color=DARK,
                weight="bold", ha="center", va="bottom")
        ax.text(x, 0.600, note, fontsize=8.8, color=SLATE,
                ha="center", va="top", linespacing=1.7)

    ax.add_patch(FancyArrowPatch((0.150, 0.760), (0.705, 0.760),
                                 arrowstyle="<|-|>", mutation_scale=13,
                                 color=NAVY, lw=1.2, linestyle=":"))
    ax.text(0.428, 0.775, "10 个月", fontsize=10.0, color=NAVY,
            weight="bold", ha="center", va="bottom")

    card(ax, 0.045, 0.290, 0.910, 0.215, NAVY, lw=1.4)
    ax.text(0.070, 0.455, "22 级意味着什么", fontsize=11.0, color=NAVY,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.070, 0.410,
            "小米职级体系的最高一级。组织地位这一项，到 2026 年 9 月已经给到顶了——"
            "此后集团还能往上加的，只剩股权和预算两样。",
            fontsize=9.6, color=SLATE, ha="left", va="top", zorder=6)
    ax.text(0.070, 0.330,
            "入职前，她已被曝获雷军千万年薪邀约；入职十个月，职级封顶。",
            fontsize=9.0, color=GRAY, ha="left", va="top", zorder=6)

    punchline(fig, "职级给到顶之后，能给的只剩两样：股权和预算。")
    footer(fig, "事实来源：观察者网 2026-11-20；华尔街见闻·全天候科技 2026-11-18；"
                "观点网 2026-11-19（22 级与 10 个月、千万年薪邀约）")
    fig.savefig(OUT + "图1_十个月走到职级尽头.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """现金的天花板与股权的想象空间"""
    fig = plt.figure(figsize=(12, 6.9))

    header(fig, "现金有天花板，股权没有",
           "同样是顶尖 AI 人才，拿年薪和拿股权是两个数量级的账")

    ax = fig.add_axes([0.105, 0.375, 0.375, 0.375])
    labels = ["清华大模型方向\n博士毕业生", "字节 Top Seed\n部分核心岗", "罗福莉\n（据报道）"]
    vals = [600, 600, 1000]
    colors = [LIGHT, LIGHT, NAVY]
    bars = ax.bar([0, 1, 2], vals, width=0.52, color=colors, zorder=3)
    ax.set_xticks([0, 1, 2])
    ax.set_xticklabels(labels, fontsize=9.0, color=SLATE)
    ax.set_ylim(0, 1250)
    ax.set_yticks([])
    ax.set_title("年薪口径  万元", fontsize=10.2, color=SLATE, pad=12)
    for spine in ("top", "right", "left"):
        ax.spines[spine].set_visible(False)
    ax.spines["bottom"].set_color(LIGHT)
    ax.tick_params(colors=GRAY)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + 40, "%d 万" % v,
                fontsize=10.4, color=DARK, ha="center", va="bottom")
    ax.text(0.02, 0.95, "600 万已是国内 AI 行业顶级待遇",
            transform=ax.transAxes, fontsize=8.2, color=GRAY,
            ha="left", va="top")

    axf = new_axes(fig)
    card(axf, 0.520, 0.365, 0.435, 0.385, TEAL, lw=1.5)
    axf.text(0.545, 0.700, "另一个参照：一次天使轮", fontsize=11.0, color=TEAL,
             weight="bold", ha="left", va="center", zorder=6)
    axf.text(0.545, 0.620, "20 亿美元", fontsize=20.0, color=DARK,
             weight="bold", ha="left", va="center", zorder=6)
    axf.text(0.545, 0.582, "投后估值 ≈ 人民币 133 亿元", fontsize=9.2,
             color=SLATE, ha="left", va="center", zorder=6)
    axf.text(0.545, 0.545,
             "林俊旸 8 月 12 日宣布创办语用科技，\n"
             "产品还没发，天使轮就拿到 2.2 亿美元。\n"
             "这笔钱在团队手里是股权，在小米体系里\n"
             "是工资和期权——两种东西不能换算。",
             fontsize=9.2, color=SLATE, ha="left", va="top",
             linespacing=1.85, zorder=6)

    axf.text(0.045, 0.300,
             "一个人的定价，一旦从“年薪”换成“公司估值占比”，量级就变了。",
             fontsize=9.8, color=DARK, ha="left", va="center")

    punchline(fig, "钱可以给到位，位置给不到位。")
    footer(fig, "事实来源：《中国新闻周刊》2026-07-07（清华刘知远、字节 Top Seed，"
                "经新浪财经转述）；观点网 2026-11-19（语用科技融资与估值）")
    fig.savefig(OUT + "图2_现金与股权.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """四件激励工具，给了三样"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "四件工具，给了三样",
           "职级、现金、研发自主权都已到位，卡在长期股权与独立预算")

    rows = [
        ("职级", "已给 —— 22 级，小米职级体系最高一级", TEAL, "已给"),
        ("现金", "已给 —— 千万年薪级邀约、行业顶格待遇", TEAL, "已给"),
        ("研发自主权", "已给 —— 相对放权，氛围开放，重视技术探索本身", TEAL, "已给"),
        ("长期股权与独立预算", "未给 —— 分拆传闻指向的正是这一项", RED, "未给"),
    ]

    y = 0.660
    for name, note, color, chip in rows:
        card(ax, 0.045, y, 0.910, 0.105, color, lw=1.3)
        ax.text(0.070, y + 0.072, name, fontsize=11.0, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(0.070, y + 0.033, note, fontsize=9.0, color=SLATE,
                ha="left", va="center", zorder=6)
        chip_w = 0.085
        card(ax, 0.845, y + 0.030, chip_w, 0.045, color, face=color, lw=1.0)
        ax.text(0.845 + chip_w / 2, y + 0.0525, chip, fontsize=8.6,
                color="white", weight="bold", ha="center", va="center",
                zorder=8)
        y -= 0.128

    ax.text(0.045, 0.175,
            "前三样解决的是“在这里做得好不好”；第四样解决的是“做得好的东西值钱之后，我分多少”。",
            fontsize=9.6, color=DARK, ha="left", va="center")

    punchline(fig, "顶尖人才要的不是更高的工资，是自己做出来的东西的所有权。")
    footer(fig, "事实来源：华尔街见闻·全天候科技 2026-11-18（团队管理方式）；"
                "观察者网 2026-11-20（22 级）；《资本不熬夜》2026-11-23（单列预算诉求）")
    fig.savefig(OUT + "图3_四件工具.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)