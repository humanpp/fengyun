# -*- coding: utf-8 -*-
"""
《V2X 安全预警、充电信息安全国标报批，外文版同步公示》配套图表
事实口径（均经公开信息交叉核对）：
  · 2026-11-19 14:21 工信部科技司发布公示：相关标准化技术组织已完成
    《智能网联汽车 基于直连通信技术的安全预警系统技术规范》等 2 项推荐性国家标准、
    《电动汽车充电系统信息安全技术要求及试验方法》等 2 项推荐性国家标准外文版的编制工作，
    公开征求报批意见。公示时间 2026-11-20 至 2026-11-26。
    —— 工信部官网科技司公示原文。
  · 重要区分：充电信息安全标准本身为现行国标 GB/T 41578-2022
    《电动汽车充电系统信息安全技术要求及试验方法》，此次公示的是其英文版
    （Technical requirements and test methods for cybersecurity of electric vehicle
    charging system），不是新制定标准。—— 全国标准信息公共服务平台。
  · V2X 标准：计划号 20250933-T-339，由 TC114（全国汽车标准化技术委员会）归口、
    TC114/SC34（智能网联汽车分会）执行，主管部门工信部，主要起草单位含中国汽车技术研究中心、
    安徽江淮汽车集团等；2024-08 在中汽股份盐城试验场完成标准验证试验，验证了
    交叉路口碰撞预警、左转辅助、闯红灯预警、前方车辆切出、前方侧向车道异常车辆等
    V2I 与 V2V 场景；2026 年 6 月通过审查。
    —— 全国标准信息公共服务平台、中汽股份 2024-08-12、星云互联 2024-08、与非网 2026-10-14。
  · L2 强标：GB 47955—2026《智能网联汽车 组合驾驶辅助系统安全要求》，
    2026-06-27 由国家市场监督管理总局、国家标准化管理委员会批准发布，
    拟于 2027-01-01 起实施；针对基础单车道、基础多车道、领航驾驶辅助三类系统分别提出要求，
    从功能要求、数据记录、车辆制造商安全保障等维度提出基线要求；
    2026 年以来我国搭载组合驾驶辅助功能的乘用车新车渗透率达 70%。
    —— 工信部 2026-07-02、新华社 2026-07-02。
  · 已实施的配套推荐性国标：GB/T 45315-2025《基于 LTE-V2X 直连通信的车载信息交互系统
    技术要求及试验方法》，2025-02-28 实施。—— 全国标准信息公共服务平台、与非网。
说明：素材称"《电动汽车充电系统信息安全技术要求及试验方法》外文版"与 V2X 标准并列报批，
      易被误读为两者都是新标准；实为一新一译（V2X 为新制定、充电信息安全为现行标准的外文版），
      图中明确区分。
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
    fig = base("四项里，两项是新标准，两项是翻译",
               "2026-11-19 工信部科技司公示的实际构成")
    ax = canvas(fig)

    # 左列：新制定
    ax.text(0.070, 0.845, "2 项推荐性国家标准", fontsize=11.4, color=NAVY,
            weight="bold", ha="left", va="center")
    ax.text(0.070, 0.808, "新制定", fontsize=9.4, color=NAVY,
            ha="left", va="center")

    left = [
        ("智能网联汽车\n基于直连通信技术的\n安全预警系统技术规范",
         "计划号 20250933-T-339", 0.760),
        ("另一项推荐性国家标准", "公示未在标题中列明", 0.520),
    ]
    for name, note, y in left:
        ax.add_patch(FancyBboxPatch((0.070, y - 0.190), 0.400, 0.190,
                                    boxstyle="round,pad=0.008",
                                    facecolor="#fafbfc", edgecolor=NAVY,
                                    linewidth=1.1))
        ax.text(0.092, y - 0.026, name, fontsize=8.8, color=DARK,
                ha="left", va="top", linespacing=1.75)
        ax.text(0.092, y - 0.166, note, fontsize=8.2, color=NAVY,
                ha="left", va="center")

    # 右列：外文版
    ax.text(0.545, 0.845, "2 项推荐性国家标准外文版", fontsize=11.4,
            color=GOLD, weight="bold", ha="left", va="center")
    ax.text(0.545, 0.808, "翻译", fontsize=9.4, color=GOLD,
            ha="left", va="center")

    right = [
        ("电动汽车充电系统信息安全\n技术要求及试验方法\n（英文版）",
         "现行国标 GB/T 41578-2022", 0.760),
        ("另一项标准外文版", "公示未在标题中列明", 0.520),
    ]
    for name, note, y in right:
        ax.add_patch(FancyBboxPatch((0.545, y - 0.190), 0.400, 0.190,
                                    boxstyle="round,pad=0.008",
                                    facecolor="#fafbfc", edgecolor=GOLD,
                                    linewidth=1.1))
        ax.text(0.567, y - 0.026, name, fontsize=8.8, color=DARK,
                ha="left", va="top", linespacing=1.75)
        ax.text(0.567, y - 0.166, note, fontsize=8.2, color=GOLD,
                ha="left", va="center")

    # 底部说明
    ax.add_patch(FancyBboxPatch((0.070, 0.150), 0.875, 0.115,
                                boxstyle="round,pad=0.010", facecolor=SAND,
                                edgecolor="#d9cdb6", linewidth=1.0))
    ax.text(0.092, 0.228, "关键区别", fontsize=9.4, color="#8a7a5e",
            weight="bold", ha="left", va="center")
    ax.text(0.092, 0.190,
            "V2X 标准是新制定的；充电信息安全标准 2022 年就已发布执行，这次公示的是它的英文版。",
            fontsize=8.6, color="#7a6746", ha="left", va="center")
    ax.text(0.092, 0.162,
            "一个从零起草，一个把跑通的标准翻译出去——两种不同的动作。",
            fontsize=8.6, color=RED, weight="bold", ha="left", va="center")

    punchline(fig, "“新标准”和“标准的英文版”，分量不一样。")
    footer(fig, "事实：工信部科技司 2026-11-19 公示；GB/T 41578-2022 与计划号 20250933-T-339 据全国标准信息公共服务平台｜制图：本文")
    fig.savefig(OUT + "图1_四项构成.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("三项标准，三层安全",
               "L2 强标定底线，V2X 管协同，充电标准管补能")
    ax = canvas(fig)

    layers = [
        ("GB 47955—2026（强制）", "组合驾驶辅助系统安全要求",
         "单车智能的安全底线\n2027-01-01 实施", NAVY, 0.735),
        ("20250933-T-339（推荐）", "基于直连通信的安全预警系统",
         "车—车、车—路之间的预警接口\n跨厂商、跨区域互通", GREEN, 0.505),
        ("GB/T 41578-2022（推荐）", "充电系统信息安全",
         "车—桩之间的数据交互与身份认证\n补能环节的数据入口", GOLD, 0.275),
    ]

    for name, title, desc, col, y in layers:
        ax.add_patch(FancyBboxPatch((0.090, y - 0.090), 0.830, 0.180,
                                    boxstyle="round,pad=0.010",
                                    facecolor="#fafbfc", edgecolor=col,
                                    linewidth=1.3))
        ax.add_patch(FancyBboxPatch((0.090, y - 0.090), 0.008, 0.180,
                                    boxstyle="square,pad=0",
                                    facecolor=col, edgecolor="none"))
        ax.text(0.118, y + 0.058, title, fontsize=12.4, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(0.118, y - 0.008, name, fontsize=8.8, color=col,
                weight="bold", ha="left", va="center")
        ax.text(0.118, y - 0.062, desc, fontsize=9.0, color=SLATE,
                ha="left", va="center", linespacing=1.7)

    # 左侧括号：三层指向同一件事
    ax.annotate("", xy=(0.068, 0.735), xytext=(0.068, 0.275),
                arrowprops=dict(arrowstyle="<->", color=RED, linewidth=1.6))
    ax.text(0.046, 0.505, "同一条安全链", fontsize=9.2, color=RED,
            weight="bold", ha="center", va="center", rotation=90)

    punchline(fig, "强标管单车，推荐标管路和桩——三层叠起来才叫体系。")
    footer(fig, "事实：GB 47955—2026 据工信部 2026-07-02、新华社；V2X 标准据全国标准信息公共服务平台；GB/T 41578-2022 据该标准文本｜制图：本文")
    fig.savefig(OUT + "图2_三层安全.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("两年，从验证到报批",
               "V2X 安全预警标准的推进节奏")
    ax = canvas(fig)

    y_line = 0.560
    ax.plot([0.080, 0.930], [y_line, y_line], color=LIGHT, linewidth=2.0,
            zorder=2)

    nodes = [
        ("2024.08", "验证试验", "盐城中汽股份试验场\n20 余家单位参与", "above", SLATE),
        ("2025.03", "计划下达", "计划号 20250933-T-339\nTC114/SC34 执行", "below", SLATE),
        ("2026.06", "通过审查", "进入报批程序", "above", GOLD),
        ("2026.11.19", "报批公示", "公示期 11/20—11/26", "below", RED),
    ]
    xs = [0.130, 0.400, 0.660, 0.880]

    for x, (date, name, desc, where, col) in zip(xs, nodes):
        ax.add_patch(Circle((x, y_line), 0.013, facecolor=col,
                            edgecolor="white", linewidth=2.0, zorder=6))
        if where == "above":
            ax.text(x, y_line + 0.048, date, fontsize=9.4, color=col,
                    weight="bold", ha="center", va="bottom")
            ax.text(x, y_line + 0.084, name, fontsize=11.4, color=DARK,
                    weight="bold", ha="center", va="bottom")
            ax.text(x, y_line + 0.124, desc, fontsize=8.2, color=SLATE,
                    ha="center", va="bottom", linespacing=1.7)
        else:
            ax.text(x, y_line - 0.048, date, fontsize=9.4, color=col,
                    weight="bold", ha="center", va="top")
            ax.text(x, y_line - 0.084, name, fontsize=11.4, color=DARK,
                    weight="bold", ha="center", va="top")
            ax.text(x, y_line - 0.124, desc, fontsize=8.2, color=SLATE,
                    ha="center", va="top", linespacing=1.7)

    # 底部：已实施的同类标准
    ax.add_patch(FancyBboxPatch((0.080, 0.150), 0.850, 0.130,
                                boxstyle="round,pad=0.010", facecolor=SAND,
                                edgecolor="#d9cdb6", linewidth=1.0))
    ax.text(0.104, 0.240, "已有一项同类推荐性国标在跑", fontsize=9.6,
            color="#8a7a5e", weight="bold", ha="left", va="center")
    ax.text(0.104, 0.196,
            "GB/T 45315-2025《基于 LTE-V2X 直连通信的车载信息交互系统技术要求及试验方法》，2025-02-28 实施",
            fontsize=8.8, color="#7a6746", ha="left", va="center")

    punchline(fig, "标准不是一年攒出来的，验证、审查、公示各占一段。")
    footer(fig, "事实：验证试验据中汽股份 2024-08-12、星云互联 2024-08；计划号与归口据全国标准信息公共服务平台；通过审查据与非网 2026-10-14｜制图：本文")
    fig.savefig(OUT + "图3_两年推进.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)
