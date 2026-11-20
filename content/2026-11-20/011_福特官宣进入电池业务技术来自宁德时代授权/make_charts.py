# -*- coding: utf-8 -*-
"""
《福特官宣进入电池业务，技术却来自宁德时代授权》配套图表
事实口径（均经公开报道交叉核对）：
  · 2026-11-18（周三）福特宣布：密歇根州马歇尔 BlueOval Battery Park Michigan 首批
    磷酸铁锂（LFP）方形电芯下线并发运肯塔基州路易斯维尔装配厂，用于 Fathom 电动皮卡原型车
    与验证车。工厂运营经理 Tracy Church 宣布；福特称这是美国车企首次为主流消费车型
    供应本土生产的 LFP 电芯。电池包工厂要到 2027 年春季才全面投产。
    —— MLive 2026-11-18、Electrek、UPI、Automotive World、CNBC。
  · 技术来自宁德时代授权：福特向宁德时代支付未披露比例的按颗专利费（royalty），
    宁德时代在该工厂与电动车产线零股权；宁德时代提供技术、设备与培训，
    但所有电芯均在马歇尔生产。—— MLive 2026-11-18 引 Tracy Church。
  · 工厂数据：投资约 30 亿美元（原 35 亿）、200 万平方英尺、规划年产能约 20GWh
    （原 35GWh，削减约 43%）、1,700 名员工（原 2,500 名）、
    产线速度每分钟 40 颗电芯，每个电池包约需 100 颗。
  · 沿革：2023-02 宣布建厂（35 亿美元、35GWh、2,500 人）；2023-09 因电动车销量放缓
    暂停建设近两个月；2023-11 缩减规模后复工（产能降 43% 至 20GWh、员工降至 1,700、
    投资降至约 30 亿美元）；曾遭美国国会议员质疑其使用中国技术。
    —— 福特 2023-02-14 新闻稿、路透社/CNBC/TechCrunch 2023-11-21、MLive 2026-11-18。
  · Fathom：UEV 平台首款车，计划 2027 年四季度推出；起售价 28,350 美元（标准续航版），
    2027 年初开启预订；方形电芯直接融入底盘布局，让电池包承担部分车身结构功能以压缩成本。
    —— MLive、Electrek 2026-11-18 引福特及 CEO 吉姆·法利三季度财报电话会。
说明：素材称"产能规划较早些时候少了一半"，经核为削减约 43%（35→20GWh），图中按实际比例；
      素材称"起售价目标低于 3 万美元"，经核福特已公布具体起售价 28,350 美元；
      素材未提及宁德时代零股权、按颗收专利费、电池包工厂 2027 年春季才全面投产、
      2023 年曾暂停建设，本文据公开信源补入。
风格：克制传媒风，白底、低饱和配色、标题即结论。输出目录 = 脚本所在目录。
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False

NAVY = "#1f3a5f"
RED = "#b5544a"
GRAY = "#8a8f98"
SLATE = "#5f6673"
LIGHT = "#d8dbe0"
DARK = "#2b2f36"
PALE = "#eef0f3"
SAND = "#f7f3ea"
GOLD = "#c9a27a"
GREEN = "#5a7d6f"

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


def canvas(fig):
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return ax


# ------------------------------------------------------------------ 图 1
def fig1():
    fig = base("三年半，从宣布到下线",
               "福特马歇尔电池厂：一条走得不顺的路")
    ax = canvas(fig)

    y_line = 0.540
    ax.plot([0.070, 0.935], [y_line, y_line], color=LIGHT, linewidth=2.0,
            zorder=2)

    nodes = [
        ("2023.02", "宣布建厂", "35 亿美元\n35GWh　2,500 人", "below", SLATE),
        ("2023.09", "暂停建设", "电动车销量放缓\n停工近两个月", "above", RED),
        ("2023.11", "缩减后复工", "产能降至 20GWh\n投资降至约 30 亿", "below", GOLD),
        ("2026.11.18", "首批电芯下线", "发运路易斯维尔\n用于 Fathom 原型车", "above", NAVY),
        ("2027", "计划节点", "春季电池包厂全面投产\n四季度 Fathom 上市", "below", GREEN),
    ]
    xs = [0.100, 0.300, 0.500, 0.720, 0.900]

    for x, (date, name, desc, where, col) in zip(xs, nodes):
        ax.add_patch(Circle((x, y_line), 0.013, facecolor=col,
                            edgecolor="white", linewidth=2.0, zorder=6))
        if where == "above":
            ax.text(x, y_line + 0.048, date, fontsize=9.6, color=col,
                    weight="bold", ha="center", va="bottom")
            ax.text(x, y_line + 0.084, name, fontsize=11.6, color=DARK,
                    weight="bold", ha="center", va="bottom")
            ax.text(x, y_line + 0.124, desc, fontsize=8.6, color=SLATE,
                    ha="center", va="bottom", linespacing=1.7)
        else:
            ax.text(x, y_line - 0.048, date, fontsize=9.6, color=col,
                    weight="bold", ha="center", va="top")
            ax.text(x, y_line - 0.084, name, fontsize=11.6, color=DARK,
                    weight="bold", ha="center", va="top")
            ax.text(x, y_line - 0.124, desc, fontsize=8.6, color=SLATE,
                    ha="center", va="top", linespacing=1.7)

    ax.text(0.070, 0.165,
            "2023 年 2 月宣布时是 35GWh、2,500 人、35 亿美元；十个月后砍到 20GWh、1,700 人、约 30 亿。",
            fontsize=9.2, color=SLATE, ha="left", va="center")
    ax.text(0.070, 0.128,
            "中间还停过一次工，理由是电动车销量增长低于预期。",
            fontsize=9.2, color=RED, weight="bold", ha="left", va="center")

    punchline(fig, "“正式进入电池业务”这句话，前面压着三年半的反复。")
    footer(fig, "事实：福特 2023-02-14 新闻稿、路透社/CNBC 2023-11-21、MLive 与 Electrek 2026-11-18｜制图：本文")
    fig.savefig(OUT + "图1_三年半.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("缩水的不只是产能",
               "原规划 vs 最终落地：三项同时下调")
    ax = canvas(fig)

    groups = [
        ("规划年产能", "35 GWh", "20 GWh", 35, 20, "−43%", NAVY),
        ("员工人数", "2,500 人", "1,700 人", 25, 17, "−32%", GOLD),
        ("投资额", "35 亿美元", "约 30 亿美元", 35, 30, "−14%", SLATE),
    ]

    x_left = 0.235
    x_scale = 0.0195  # 1 单位 ≈ 0.0195（最大 35 单位 → 0.68）

    for i, (label, before, after, v1, v2, pct, col) in enumerate(groups):
        y_top = 0.830 - i * 0.205

        ax.text(x_left - 0.020, y_top - 0.010, label, fontsize=10.6, color=DARK,
                ha="right", va="center")

        # 原规划（浅色）
        w1 = v1 * x_scale
        ax.add_patch(FancyBboxPatch((x_left, y_top - 0.060), w1, 0.040,
                                    boxstyle="round,pad=0.002",
                                    facecolor="#e4e7ec", edgecolor="none",
                                    zorder=3))
        ax.text(x_left + w1 + 0.012, y_top - 0.040, before, fontsize=9.0,
                color=GRAY, ha="left", va="center")

        # 最终（实色）
        w2 = v2 * x_scale
        ax.add_patch(FancyBboxPatch((x_left, y_top - 0.112), w2, 0.040,
                                    boxstyle="round,pad=0.002",
                                    facecolor=col, edgecolor="none",
                                    alpha=0.92, zorder=3))
        ax.text(x_left + w2 + 0.012, y_top - 0.092, after, fontsize=9.6,
                color=col, weight="bold", ha="left", va="center")
        ax.text(x_left + w2 + 0.105, y_top - 0.092, pct, fontsize=9.6,
                color=RED, weight="bold", ha="left", va="center")

    # 产线速度
    ax.add_patch(FancyBboxPatch((0.070, 0.150), 0.860, 0.115,
                                boxstyle="round,pad=0.010", facecolor=SAND,
                                edgecolor="#d9cdb6", linewidth=1.0))
    ax.text(0.092, 0.226, "但产线本身不慢", fontsize=9.8, color="#8a7a5e",
            weight="bold", ha="left", va="center")
    ax.text(0.092, 0.182,
            "每分钟 40 颗电芯，每个电池包约需 100 颗——福特称这是中国以外最快的 LFP 方形电芯装配线之一。",
            fontsize=9.2, color="#7a6746", ha="left", va="center")

    punchline(fig, "厂是新的，速度是快的，规划是砍过的。")
    footer(fig, "事实：产能/人数/投资数据据路透社、CNBC、TechCrunch 2023-11-21 及 MLive 2026-11-18；百分比为本文计算｜制图：本文")
    fig.savefig(OUT + "图2_三项下调.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("授权，不是合资",
               "钱、厂、股权在福特这边；技术、设备、培训在宁德时代那边")
    ax = canvas(fig)

    # 左：福特
    ax.add_patch(FancyBboxPatch((0.055, 0.290), 0.360, 0.450,
                                boxstyle="round,pad=0.012", facecolor="#eef2f6",
                                edgecolor=NAVY, linewidth=1.3))
    ax.text(0.080, 0.690, "福特", fontsize=15.0, color=NAVY, weight="bold",
            ha="left", va="center")
    ax.text(0.080, 0.645, "出钱、建厂、招人", fontsize=9.2, color=GRAY,
            ha="left", va="center")
    ford_items = [
        "投资约 30 亿美元",
        "100% 持有工厂与产线",
        "1,700 名员工，两班制",
        "所有电芯在密歇根生产",
    ]
    yy = 0.565
    for it in ford_items:
        ax.text(0.080, yy, "·  " + it, fontsize=9.4, color=DARK, ha="left",
                va="center")
        yy -= 0.070

    # 右：宁德时代
    ax.add_patch(FancyBboxPatch((0.585, 0.290), 0.360, 0.450,
                                boxstyle="round,pad=0.012", facecolor="#f7eae8",
                                edgecolor=RED, linewidth=1.3))
    ax.text(0.610, 0.690, "宁德时代", fontsize=15.0, color=RED, weight="bold",
            ha="left", va="center")
    ax.text(0.610, 0.645, "出技术、出设备、出培训", fontsize=9.2, color=GRAY,
            ha="left", va="center")
    catl_items = [
        "LFP 电芯专利授权",
        "产线设备与工艺",
        "人员培训",
        "零股权，按每颗电芯收专利费",
    ]
    yy = 0.565
    for i, it in enumerate(catl_items):
        col = RED if i == 3 else DARK
        w = "bold" if i == 3 else "normal"
        ax.text(0.610, yy, "·  " + it, fontsize=9.4, color=col, weight=w,
                ha="left", va="center")
        yy -= 0.070

    # 中间箭头
    ax.annotate("", xy=(0.575, 0.515), xytext=(0.425, 0.515),
                arrowprops=dict(arrowstyle="-|>", color=GOLD, linewidth=2.0))
    ax.text(0.500, 0.545, "技术", fontsize=9.6, color=GOLD, weight="bold",
            ha="center", va="bottom")
    ax.annotate("", xy=(0.425, 0.435), xytext=(0.575, 0.435),
                arrowprops=dict(arrowstyle="-|>", color=RED, linewidth=2.0))
    ax.text(0.500, 0.405, "专利费", fontsize=9.6, color=RED, weight="bold",
            ha="center", va="top")

    ax.text(0.055, 0.200,
            "这跟“合资建厂”是两回事：宁德时代不占股、不分红，只按产量收费。",
            fontsize=9.4, color=DARK, weight="bold", ha="left", va="center")
    ax.text(0.055, 0.160,
            "对福特来说，好处是不必自己从零摸索配方与工艺；代价是每颗电芯都要付一次钱。",
            fontsize=9.0, color=SLATE, ha="left", va="center")

    punchline(fig, "买的是“怎么做”，不是“谁来管”。")
    footer(fig, "事实：授权结构、零股权、按颗收专利费据 MLive 2026-11-18 引工厂运营经理 Tracy Church｜制图：本文")
    fig.savefig(OUT + "图3_授权不是合资.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)
