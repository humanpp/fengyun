# -*- coding: utf-8 -*-
"""
《净利降 7.9%，折旧却少提 12 亿：中国移动三季报里的两个方向》
配套图表

事实口径（核到公司定期报告与会计估计变更公告）：

一、2026 年第三季度报告（2026-10-20 披露，按中国企业会计准则、未经审计）
  · 前三季度营业收入 7803 亿元，同比下降 1.8%；
    其中主营业务收入 6577 亿元，同比下降 3.7%；
    其他业务收入 1226 亿元，同比增长 9.9%。
  · 前三季度股东应占利润 1062 亿元，同比下降 7.9%；股东应占利润率 13.6%；
    归属于母公司股东的扣除非经常性损益的净利润 984 亿元，同比下降 8.1%。
  · EBITDA 2475 亿元，同比下降 6.7%；EBITDA 率由上年同期 33.4% 降至 31.7%；
    EBITDA 占主营业务收入比 37.6%。
  · 单看第三季度：营业收入 2423 亿元，同比下降 3.4%；
    主营业务收入 2051 亿元，同比下降 5.1%；
    其他业务收入 372 亿元，同比增长 7.2%；
    归属于母公司股东的净利润 273 亿元，同比下降 12.2%；
    扣非归母净利润 287 亿元，同比下降 0.2%。
  · 运营数据（截至 2026-09-30）：移动客户 10.14 亿户，三季度净增 300.9 万户，
    本年累计净增 888.6 万户；5G 网络客户 7.02 亿户；
    宽带联网客户 3.42 亿户，本季度净增 534.5 万户，本年累计净增 1304.9 万户；
    物联网卡连接数 14.97 亿户，三季度净减 1454.6 万户，
    本年累计净增 1503.2 万户。

二、会计估计变更公告（2026-11-20 披露，董事会 2026-11-19 审议通过
   《关于部分资产折旧年限调整的议案》，自议案生效之日起执行）
  · 部分动力配套设备折旧年限由 5-10 年调整至 6-15 年；
    钢筋混凝土、钢结构房屋折旧年限由 30 年调整至 50 年。
  · 按现有资料初步测算，预计使公司 2026 年度固定资产折旧额减少约 12 亿元。
  · 本次会计估计变更无需提交股东大会审议。
  · 原因表述：2026 年 4 月国家明确提出加强算力网、新一代通信网等「六张网」
    统筹建设、多网协同的长期战略；集团加快向科技服务企业提能升级；
    2026 年以来算力服务规模快速增长，算力网相关数据中心业务的经营模式
    向较长期服务合同转变，对动力配套及建筑物等数据中心相关基础设施的
    长期运营安排及持续使用需求预期更为明确。
  据证券日报网 2026-11-20、同花顺 2026-11-20、香港交易所披露易海外监管公告
  （2026-11-20，会计估计变更）。

风格：克制传媒风，白底、低饱和配色、标题即结论
输出目录 = 脚本所在目录
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
TEAL = "#3f6f6b"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep

Y_TITLE = 0.958
Y_SUB = 0.898
Y_PUNCH = 0.070
Y_FOOT = 0.020

Q_L = "\u300c"
Q_R = "\u300d"


def header(fig, title, sub):
    fig.text(0.045, Y_TITLE, title, fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, Y_SUB, sub, fontsize=10.6, color=GRAY,
             ha="left", va="top")


def footer(fig, text):
    fig.text(0.045, Y_FOOT, text, fontsize=7.6, color=GRAY,
             ha="left", va="bottom")


def punchline(fig, text):
    fig.text(0.045, Y_PUNCH, text, fontsize=10.4, color=DARK,
             ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


def card(ax, x, y, w, h, edge, face="white", lw=1.0, z=2):
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
    """前三季度 vs 第三季度 四个降幅"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "四个数字都是负的，但负得不一样",
           "前三季度与第三季度单季，营收降幅差了一倍，利润降幅差了四倍")

    groups = [
        ("前三季度", [
            ("营业收入 7803 亿元", -1.8),
            ("主营业务收入 6577 亿元", -3.7),
            ("股东应占利润 1062 亿元", -7.9),
            ("扣非净利润 984 亿元", -8.1),
        ], NAVY),
        ("第三季度单季", [
            ("营业收入 2423 亿元", -3.4),
            ("主营业务收入 2051 亿元", -5.1),
            ("归母净利润 273 亿元", -12.2),
            ("扣非净利润 287 亿元", -0.2),
        ], RED),
    ]

    scale = 0.220 / 13.0

    for gi, (gname, rows, color) in enumerate(groups):
        gx = 0.048 + gi * 0.470
        ax.text(gx, 0.782, gname, fontsize=11.4, color=color,
                weight="bold", ha="left", va="center")
        ax.plot([gx, gx + 0.400], [0.756, 0.756], color=LIGHT,
                linewidth=1.0)

        y = 0.690
        for label, val in rows:
            ax.text(gx, y, label, fontsize=8.8, color=SLATE,
                    ha="left", va="center", zorder=6)
            w = abs(val) * scale
            ax.add_patch(Rectangle((gx, y - 0.048), w, 0.026,
                                   facecolor=color, edgecolor=color,
                                   linewidth=0, alpha=0.88, zorder=4))
            ax.text(gx + w + 0.010, y - 0.035, f"{val:.1f}%",
                    fontsize=9.4, color=color, weight="bold",
                    ha="left", va="center", zorder=6)
            y -= 0.128

    ax.text(0.048, 0.196,
            "最值得看的是最后一行：三季度单季扣非净利润只降 0.2%，",
            fontsize=9.4, color=DARK, ha="left", va="center")
    ax.text(0.048, 0.152,
            "而归母净利润降 12.2%——两个数之间的那 12 个点，不在经营里。",
            fontsize=9.4, color=DARK, ha="left", va="center")

    punchline(fig, "营收的降幅已经收窄，利润的降幅还在扩大。")
    footer(fig, "事实来源：中国移动 2026 年第三季度报告（2026-10-20 披露）；"
                "澎湃新闻 2026-10-20 对三季报的报道")
    fig.savefig(OUT + "图1_四个降幅.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """折旧年限调整 前后对比"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "两类资产，折旧年限一起拉长",
           "动力配套 5-10 年改为 6-15 年；房屋 30 年改为 50 年")

    # 左：动力配套设备
    ax.text(0.052, 0.770, "动力配套设备", fontsize=12.0, color=DARK,
            weight="bold", ha="left", va="center")
    ax.text(0.052, 0.726, "机房的电源、UPS、空调这类设备", fontsize=8.8,
            color=GRAY, ha="left", va="center")

    unit = 0.0200  # 每年对应的横向长度
    rows_a = [
        ("原口径", 5, 10, SLATE),
        ("调整后", 6, 15, RED),
    ]
    y = 0.646
    for label, lo, hi, color in rows_a:
        ax.text(0.052, y, label, fontsize=9.4, color=GRAY,
                ha="left", va="center", zorder=6)
        x_start = 0.150
        ax.add_patch(Rectangle((x_start + lo * unit, y - 0.020),
                               (hi - lo) * unit, 0.040,
                               facecolor=color, edgecolor=color,
                               linewidth=0, alpha=0.88, zorder=4))
        ax.text(x_start + hi * unit + 0.012, y, f"{lo}—{hi} 年",
                fontsize=9.6, color=color, weight="bold",
                ha="left", va="center", zorder=6)
        y -= 0.098

    # 右：房屋
    ax.text(0.052, 0.456, "钢筋混凝土、钢结构房屋", fontsize=12.0, color=DARK,
            weight="bold", ha="left", va="center")
    ax.text(0.052, 0.412, "数据中心的主体建筑", fontsize=8.8,
            color=GRAY, ha="left", va="center")

    unit2 = 0.0105

    rows_b = [
        ("原口径", 30, SLATE),
        ("调整后", 50, RED),
    ]
    y = 0.310
    for label, yrs, color in rows_b:
        ax.text(0.052, y, label, fontsize=9.4, color=GRAY,
                ha="left", va="center", zorder=6)
        x_start = 0.150
        ax.add_patch(Rectangle((x_start, y - 0.020), yrs * unit2, 0.040,
                               facecolor=color, edgecolor=color,
                               linewidth=0, alpha=0.88, zorder=4))
        ax.text(x_start + yrs * unit2 + 0.012, y, f"{yrs} 年",
                fontsize=9.6, color=color, weight="bold",
                ha="left", va="center", zorder=6)
        y -= 0.078

    card(ax, 0.052, 0.118, 0.898, 0.076, LIGHT, face=PALE, lw=1.0)
    ax.text(0.076, 0.156,
            "公司初步测算：本次变更将使 2026 年度固定资产折旧额减少约 12 亿元。",
            fontsize=9.6, color=DARK, ha="left", va="center", zorder=6)

    punchline(fig, "折旧少提一年，利润就多一年；这不是多赚了钱。")
    footer(fig, "事实来源：中国移动《关于会计估计变更的公告》（2026-11-20）；"
                "董事会 2026-11-19 审议通过")
    fig.savefig(OUT + "图2_折旧年限.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """公告自己给的理由"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "公司给的理由，和折旧本身没关系",
           "公告把原因指向了业务模式的变化，不是资产变新了")

    steps = [
        ("2026 年 4 月", "国家明确提出加强算力网、\n新一代通信网等六张网统筹建设"),
        ("业务模式", "算力网相关数据中心业务，\n向较长期服务合同转变"),
        ("判断依据", "对动力配套及建筑物的长期运营安排、\n持续使用需求的预期更为明确"),
        ("会计结果", "重新评估使用寿命，\n折旧年限拉长"),
    ]

    y = 0.700
    for i, (tag, text) in enumerate(steps):
        card(ax, 0.052, y - 0.086, 0.560, 0.100, NAVY if i < 3 else RED,
             face="white", lw=1.2)
        ax.text(0.074, y - 0.036, tag, fontsize=10.4,
                color=NAVY if i < 3 else RED, weight="bold",
                ha="left", va="center", zorder=6)
        ax.text(0.230, y - 0.036, text, fontsize=8.6, color=DARK,
                ha="left", va="center", linespacing=1.55, zorder=6)
        if i < 3:
            ax.annotate("", xy=(0.332, y - 0.100), xytext=(0.332, y - 0.084),
                        arrowprops=dict(arrowstyle="-|>", color=GRAY,
                                        linewidth=1.3, shrinkA=0,
                                        shrinkB=0))
        y -= 0.130

    # 右侧说明
    card(ax, 0.648, 0.300, 0.304, 0.400, LIGHT, face=PALE, lw=1.0)
    ax.text(0.670, 0.664, "这句话在说什么", fontsize=10.0, color=GRAY,
            ha="left", va="center", zorder=6)
    ax.text(0.670, 0.618,
            "资产本身没变，\n变的是公司对\n"
            "「它会用多久」\n的判断。\n\n"
            "合同越长、用途越确定，\n"
            "可分摊的年限就可以越长。",
            fontsize=9.0, color=DARK, ha="left", va="top",
            linespacing=1.80, zorder=6)

    punchline(fig, "折旧是一次判断，不是一次收入。")
    footer(fig, "事实来源：中国移动《关于会计估计变更的公告》（2026-11-20）原文表述")
    fig.savefig(OUT + "图3_理由.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)
