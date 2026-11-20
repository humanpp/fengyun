# -*- coding: utf-8 -*-
"""
《河南这场风，“橙色预警”是个误会》配套图表
事实口径（均经公开信息逐条核对）：
  · 河南省气象台 2026-11-19 12 时预报：20 日全省西北风 3 到 4 级，阵风 5 到 6 级，
    中西部同为 3 到 4 级、阵风 5 到 6 级；郑州晴天间多云，白天西北风 3 到 4 级，阵风 5 到 6 级；
    21 日西部、南部晴天到多云，其他县市晴天间多云；22 日西部、南部多云到晴天。
    大部最高气温回升至 12～15℃，最低气温仍在 0 度左右，局地 -1℃，昼夜温差普遍 10℃ 以上。
  · 大风预警分级标准（中国气象局《气象灾害预警信号发布与传播办法》）：
    蓝色 平均 6 级以上或阵风 7 级以上；黄色 平均 8 级以上或阵风 9 级以上；
    橙色 平均 10 级以上或阵风 11 级以上；红色 平均 12 级以上或阵风 13 级以上。
  · 发布记录：
    息县 2026-11-17 19:32 大风蓝色（4～5 级偏北风，阵风 7～8 级）；
    息县 2026-11-19 15:18 大风蓝色（5～6 级偏北风，阵风 7～8 级）；
    息县 2026-11-05 02:36 大雾橙色（不是大风）；
    汝州 2026-11-18 01:54 大风黄色升级；2026-11-19 13:34 大风黄色升级
         （平均风力可达 8 级以上，阵风 9 级以上）；2026-11-20 12:01 大风蓝色。
    平顶山市 2026-11-20 11:53 蓝色；叶县 2026-11-20 12:20 蓝色。
说明：11-20 流传的报道称“息县发布橙色预警，汝州发布黄色预警”，与发布记录不符，
      图中并列呈现，不替报道做圆场。
风格：克制传媒风，白底、低饱和配色、标题即结论。输出目录 = 脚本所在目录。
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False

NAVY = "#1f3a5f"
RED = "#a83f36"
GRAY = "#8a8f98"
SLATE = "#5f6673"
LIGHT = "#d8dbe0"
DARK = "#2b2f36"
PALE = "#eef0f3"
SAND = "#f7f3ea"
GOLD = "#c2a15c"
ZL_BLUE = "#7f97ae"
ZL_YEL = "#c2a15c"
ZL_ORG = "#c07a4e"
ZL_RED = "#a83f36"
ZL_NONE = "#c9ced6"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep


def base(title, sub):
    fig = plt.figure(figsize=(12, 6.8))
    fig.patch.set_facecolor("white")
    fig.text(0.045, 0.950, title, fontsize=20, color=DARK, weight="bold",
             ha="left", va="top")
    fig.text(0.045, 0.878, sub, fontsize=10.8, color=GRAY, ha="left", va="top")
    return fig


def footer(fig, line1, line2):
    fig.text(0.045, 0.042, line1, fontsize=7.6, color=GRAY, ha="left", va="center")
    fig.text(0.045, 0.020, line2, fontsize=7.6, color=GRAY, ha="left", va="center")


def punchline(fig, text, y=0.080):
    fig.text(0.045, y, text, fontsize=10.8, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.6", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


def canvas(fig, bottom=0.135, height=0.700):
    ax = fig.add_axes([0.045, bottom, 0.915, height])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return ax


# ------------------------------------------------------------------ 图 1
def fig1():
    fig = base("颜色的刻度：蓝、黄、橙、红各对应几级风",
               "大风预警按阵风等级分档——橙色意味着平均 10 级、阵风 11 级")
    ax = canvas(fig, bottom=0.115, height=0.730)

    X0, X1 = 0.075, 0.955
    VMIN, VMAX = 4.0, 15.0

    def X(v):
        return X0 + (v - VMIN) / (VMAX - VMIN) * (X1 - X0)

    bands = [
        (4, 7, ZL_NONE, "未达预警门槛", ""),
        (7, 9, ZL_BLUE, "蓝色", "平均 ≥6 级 / 阵风 ≥7 级"),
        (9, 11, ZL_YEL, "黄色", "平均 ≥8 级 / 阵风 ≥9 级"),
        (11, 13, ZL_ORG, "橙色", "平均 ≥10 级 / 阵风 ≥11 级"),
        (13, 15, ZL_RED, "红色", "平均 ≥12 级 / 阵风 ≥13 级"),
    ]

    y_top, y_bot = 0.880, 0.600
    for lo, hi, col, name, rule in bands:
        ax.add_patch(Rectangle((X(lo), y_bot), X(hi) - X(lo), y_top - y_bot,
                               facecolor=col, edgecolor="white", linewidth=2.0,
                               zorder=3))
        cx = (X(lo) + X(hi)) / 2
        tcol = "white" if col != ZL_NONE else SLATE
        ax.text(cx, (y_top + y_bot) / 2, name, fontsize=14.5, color=tcol,
                weight="bold", ha="center", va="center", zorder=4)
        if rule:
            ax.text(cx, y_bot - 0.038, rule, fontsize=8.4, color=SLATE,
                    ha="center", va="top", zorder=4)

    # 坐标轴
    ax.plot([X(VMIN), X(VMAX)], [0.490, 0.490], color=LIGHT, linewidth=1.6,
            zorder=2)
    for v in range(4, 16):
        ax.plot([X(v), X(v)], [0.490, 0.480], color=LIGHT, linewidth=1.2,
                zorder=2)
        ax.text(X(v), 0.452, str(v), fontsize=8.8, color=GRAY, ha="center",
                va="top")
    ax.text(X1, 0.418, "阵风风力（级）", fontsize=8.6, color=GRAY, ha="right",
            va="top")

    facts = [
        (5.5, ZL_NONE, "20 日全省：西北风 3～4 级，阵风 5～6 级 —— 未达蓝色门槛"),
        (7.5, ZL_BLUE, "息县 11-19 15:18：阵风 7～8 级 —— 蓝色（实际发布的就是这一级）"),
        (9.2, ZL_YEL, "汝州 11-19 13:34：平均 8 级以上、阵风 9 级以上 —— 黄色"),
        (11.0, ZL_ORG, "报道所写“息县橙色”：按标准应对应平均 10 级、阵风 11 级"),
    ]

    for v, col, text in facts:
        ax.plot([X(v)], [0.492], marker="v", markersize=9.5, color=col,
                markeredgecolor="white", markeredgewidth=0.8, zorder=6)

    yy = 0.370
    for v, col, text in facts:
        ax.add_patch(Rectangle((0.045, yy - 0.014), 0.016, 0.028, facecolor=col,
                               edgecolor="none", zorder=5))
        ax.text(0.078, yy, text, fontsize=9.4, color=DARK, ha="left",
                va="center", zorder=5)
        yy -= 0.075

    punchline(fig, "蓝到橙隔了三个档，不是“大一点”的差别。")
    footer(fig,
           "事实：分级标准据中国气象局《气象灾害预警信号发布与传播办法》“大风预警信号”条；全省预报据河南省气象台 2026-11-19 12 时预报；",
           "息县、汝州发布记录据中央气象台预警信号页与天气网预警页（来源中国气象局）｜制图：本文")
    fig.savefig(OUT + "图1_颜色的刻度.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("息县这轮发的是蓝色，“橙色”是月初那场雾",
               "把报道说的颜色和发布记录并排放")
    ax = canvas(fig)

    # 顶部对照
    ax.add_patch(FancyBboxPatch((0.070, 0.700), 0.400, 0.170,
                                boxstyle="round,pad=0.012", facecolor="#fdf6f5",
                                edgecolor=RED, linewidth=1.1))
    ax.text(0.096, 0.828, "报道写的", fontsize=9.6, color=RED, weight="bold",
            ha="left", va="center")
    ax.text(0.096, 0.775, "息县　橙色　　汝州　黄色", fontsize=11.0,
            color=DARK, ha="left", va="center", weight="bold")
    ax.text(0.096, 0.730, "11 月 20 日流传的报道原文", fontsize=8.4,
            color="#8a5a52", ha="left", va="center")

    ax.add_patch(FancyBboxPatch((0.530, 0.700), 0.400, 0.170,
                                boxstyle="round,pad=0.012", facecolor="#f4f7f6",
                                edgecolor="#5a7d6f", linewidth=1.1))
    ax.text(0.556, 0.828, "发布记录里的", fontsize=9.6, color="#4a6b5e",
            weight="bold", ha="left", va="center")
    ax.text(0.556, 0.775, "息县　蓝色　　汝州　黄色·20 日转蓝", fontsize=11.0,
            color=DARK, ha="left", va="center", weight="bold")
    ax.text(0.556, 0.730, "中央气象台、天气网预警页", fontsize=8.4,
            color="#5a7d6f", ha="left", va="center")

    # 时间轴
    y0 = 0.440
    ax.plot([0.075, 0.945], [y0, y0], color=LIGHT, linewidth=2.2, zorder=2)

    nodes = [
        (0.110, "11.05 02:36", "息县·大雾橙色", "不是大风", "up", ZL_ORG),
        (0.310, "11.17 19:32", "息县·大风蓝色", "4～5 级，阵风 7～8 级", "down", ZL_BLUE),
        (0.510, "11.19 13:34", "汝州·大风黄色", "平均 8 级以上，阵风 9 级以上", "up", ZL_YEL),
        (0.710, "11.19 15:18", "息县·大风蓝色", "5～6 级，阵风 7～8 级", "down", ZL_BLUE),
        (0.905, "11.20 12:01", "汝州·转回蓝色", "平均 6 级以上，阵风 7 级以上", "up", ZL_BLUE),
    ]
    for x, date, name, desc, where, col in nodes:
        ax.add_patch(Circle((x, y0), 0.0125, facecolor=col, edgecolor="white",
                            linewidth=2.0, zorder=6))
        if where == "up":
            ax.text(x, y0 + 0.042, date, fontsize=9.0, color=col, weight="bold",
                    ha="center", va="bottom")
            ax.text(x, y0 + 0.078, name, fontsize=11.0, color=DARK, weight="bold",
                    ha="center", va="bottom")
            ax.text(x, y0 + 0.118, desc, fontsize=8.2, color=SLATE, ha="center",
                    va="bottom")
        else:
            ax.text(x, y0 - 0.042, date, fontsize=9.0, color=col, weight="bold",
                    ha="center", va="top")
            ax.text(x, y0 - 0.078, name, fontsize=11.0, color=DARK, weight="bold",
                    ha="center", va="top")
            ax.text(x, y0 - 0.118, desc, fontsize=8.2, color=SLATE, ha="center",
                    va="top")

    # 底部结论
    ax.add_patch(FancyBboxPatch((0.070, 0.100), 0.860, 0.135,
                                boxstyle="round,pad=0.012", facecolor=SAND,
                                edgecolor="#d9cdb6", linewidth=1.0))
    ax.text(0.096, 0.196, "一句话", fontsize=9.4, color="#8a7a5e", weight="bold",
            ha="left", va="center")
    ax.text(0.096, 0.158,
            "这轮过程里“橙色”没有落在任何一条大风预警上；息县两次大风都是蓝色，"
            "橙色是 11 月 5 日的大雾。",
            fontsize=8.8, color="#7a6746", ha="left", va="center")
    ax.text(0.096, 0.124,
            "汝州的黄色对得上，但那是 19 日的局地升级，20 日中午已转回蓝色。",
            fontsize=8.8, color=RED, weight="bold", ha="left", va="center")

    punchline(fig, "橙色这个字，是从月初那场雾里挪过来的。")
    footer(fig,
           "事实：息县 11-17 19:32、11-19 15:18 大风蓝色；息县 11-05 02:36 大雾橙色；汝州 11-18 01:54、11-19 13:34 大风黄色，11-20 12:01 蓝色；",
           "据中央气象台预警信号页、天气网预警页（来源中国气象局）、国家应急广播网｜制图：本文")
    fig.savefig(OUT + "图2_息县的记录.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("白天十二到十五度，早晚零度上下",
               "同一天里的两段温度，中间隔着的就是昼夜温差")
    ax = canvas(fig)

    TMIN, TMAX = -4.0, 18.0

    def Y(t):
        return 0.245 + (t - TMIN) / (TMAX - TMIN) * 0.655

    # 冰点虚线先画，落在色块下面
    ax.plot([0.165, 0.775], [Y(0), Y(0)], color=ZL_BLUE, linewidth=1.0,
            linestyle=(0, (4, 3)), zorder=1)
    ax.text(0.788, Y(0), "冰点", fontsize=8.6, color=ZL_BLUE, ha="left",
            va="center")

    # 温度轴
    ax.plot([0.150, 0.150], [Y(TMIN), Y(TMAX)], color=LIGHT, linewidth=1.6,
            zorder=2)
    for t in (-5, 0, 5, 10, 15):
        ax.plot([0.150, 0.138], [Y(t), Y(t)], color=LIGHT, linewidth=1.2,
                zorder=2)
        ax.text(0.126, Y(t), "%d℃" % t, fontsize=8.8, color=GRAY, ha="right",
                va="center")

    # 最高气温带
    ax.add_patch(Rectangle((0.200, Y(12)), 0.520, Y(15) - Y(12),
                           facecolor="#efe3cf", edgecolor=GOLD, linewidth=1.4,
                           zorder=3))
    ax.text(0.232, (Y(12) + Y(15)) / 2, "大部地区最高气温　12～15℃",
            fontsize=11.8, color="#8a6f3e", weight="bold", ha="left",
            va="center", zorder=4)

    # 最低气温带
    ax.add_patch(Rectangle((0.200, Y(-1)), 0.520, Y(1) - Y(-1),
                           facecolor="#dde3ea", edgecolor=ZL_BLUE, linewidth=1.4,
                           zorder=3))
    ax.text(0.232, (Y(-1) + Y(1)) / 2, "最低气温　0℃ 上下，局地 -1℃",
            fontsize=10.8, color="#41586b", weight="bold", ha="left",
            va="center", zorder=4)

    # 温差标注
    ax.annotate("", xy=(0.870, Y(12)), xytext=(0.870, Y(1)),
                arrowprops=dict(arrowstyle="<->", color=RED, linewidth=1.6))
    ax.text(0.892, (Y(12) + Y(1)) / 2, "昼夜温差\n普遍 >10℃", fontsize=10.4,
            color=RED, weight="bold", ha="left", va="center", linespacing=1.8)

    # 底部
    ax.add_patch(FancyBboxPatch((0.070, 0.048), 0.860, 0.130,
                                boxstyle="round,pad=0.012", facecolor=SAND,
                                edgecolor="#d9cdb6", linewidth=1.0))
    ax.text(0.096, 0.140, "再叠上风", fontsize=9.4, color="#8a7a5e",
            weight="bold", ha="left", va="center")
    ax.text(0.096, 0.096,
            "西北风 3～4 级、阵风 5～6 级带来的“风寒效应”，让体感比温度计上的数字更冷。"
            "未来三天晴，21 日西部南部晴到多云。",
            fontsize=8.8, color="#7a6746", ha="left", va="center")

    punchline(fig, "同一天里，出门穿多少要看最低温，不是最高温。")
    footer(fig,
           "事实：河南省气象台 2026-11-19 12 时预报“大部地区最高气温将逐渐回升至 12～15℃，但最低气温仍然在 0 度左右徘徊，整体回暖并不明显，",
           "昼夜温差普遍在 10℃ 以上”；“多地最低气温降至 -1℃”据河南气象经凤凰网大风号 2026-11-20 转述｜制图：本文")
    fig.savefig(OUT + "图3_十二度到零度.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)