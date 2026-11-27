# -*- coding: utf-8 -*-
"""
《一场召回 11 亿，2.9 万台交付，和每天 3 封催款邮件》配套图表

事实口径（逐条可指回）：
  · 宁德时代官网 2025-09-19《理想汽车与宁德时代达成全面战略合作》：
    9 月 18 日双方在宁德签署五年全面战略合作协议并完成授牌仪式；宁德时代
    将为理想汽车全系产品提供三元锂电池、M3P 电池、磷酸铁锂电池和钠离子
    电池等；"截至目前，搭载宁德时代电池的理想汽车累计交付量突破 100 万辆"。
  · 《21 汽车·一见 Auto》2026-11-18《理想宁德，后会友期》（原文现已全网
    不可见，内容经凤凰网科技、搜狐等多家媒体转述）：i6 电池包指标 8000 个、
    实到 4000 个；2025 年内 i6 交付 2.9 万台；宁德产能利用率 96.9%；
    MEGA 召回 11411 辆、财报口径 11 亿元、内部人士称实际超 20 亿元；
    "一天至少 3 封催款邮件"；溧阳提货冲突；复盘结论"自己的命运，不能掌握
    在别人手里"。行业口径："偏差 15% 以内可接受，超过 50% 属于巨大供应失误"。
  · 乘联分会数据（经财经生活帮 2026-11-21 转述）：2026 年 6 月理想占宁德
    装机 6.8%、占欣旺达 6.4%；8 月退出宁德前五大客户，占欣旺达 39%。
  · 甲子光年 2026-02-10：2025 年上半年宁德产能利用率爬升至 90% 以上；
    理想为 i6 预备的 2025 年四季度产能 4.5 万—5 万辆，后上调至 6.8 万辆。
  · 宁德时代委托汇业律师事务所律师函（2026-11-21 经媒体转述）：催款邮件
    系"依约进行对账与到期付款提醒"；召回原因是冷却液防腐性能不足，并非
    电芯或电池包本身缺陷，冷却液由整车厂选定。

版式约定：画布 12 × 7 英寸（2040 × 1190 像素 @170dpi）。
  标题 y=0.958，副标题 y=0.898；正文区 0.190 ~ 0.860；
  结论条 y=0.070；来源脚注 y=0.020。
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch

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

BODY_TOP = 0.860
BODY_BOTTOM = 0.190


def header(fig, title, sub):
    fig.text(0.045, Y_TITLE, title, fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, Y_SUB, sub, fontsize=10.6, color=GRAY,
             ha="left", va="top")


def footer(fig, text):
    fig.text(0.045, Y_FOOT, text, fontsize=7.4, color=GRAY,
             ha="left", va="bottom")


def punchline(fig, text):
    fig.text(0.045, Y_PUNCH, text, fontsize=10.4, color=DARK,
             ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


def card(ax, x, y, w, h, edge, face="white", lw=1.0, z=2):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.004,rounding_size=0.012",
        facecolor=face, edgecolor=edge, linewidth=lw, zorder=z))


def new_axes(fig):
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return ax


# ---------------------------------------------------------------- 图 1
def fig1():
    """十三个月，两段关系（竖直时间轴）"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "十三个月，两段关系",
           "上半段是给不够，下半段是分不清")

    ax.plot([0.100, 0.100], [0.775, 0.245], color=LIGHT, linewidth=1.4, zorder=1)
    ax.text(0.100, 0.800, "时间向下", fontsize=7.6, color=GRAY,
            ha="center", va="center")

    # (纵坐标, 日期, 事件, 说明, 颜色)
    rows = [
        (0.750, "2025.09.18—19", "五年全面战略合作协议签署",
         "宁德时代将为理想全系产品提供三元锂、M3P、磷酸铁锂、钠离子电池四项", NAVY),
        (0.670, "2025.09.26", "i6 上市，宁德为四季度电池独供方",
         "理想对 2025 年交付的 i6 承诺「均为宁德时代电池」", SLATE),
        (0.580, "2025.10", "电池包指标 8000 个，实到 4000 个",
         "宁德解释为「产能不够」；同期其产能利用率 96.9%", RED),
        (0.500, "2025.11.14", "就 MEGA 质量事故内部问责 14 人",
         "10 月一辆 MEGA 起火，调查指向冷却液防腐不足或致热失控", RED),
        (0.415, "2025.10.31 / 11", "备案召回 11411 辆，并启动召回",
         "召回前沟通会上宁德建议「单点解决」；财报口径损失 11 亿元", RED),
        (0.330, "2026.03 / 08", "双电池路线：理想品牌与宁德并行",
         "8 月明确下半年起自研电池陆续搭载全系车型", TEAL),
        (0.250, "2026.09", "26.5 亿元增资欣旺达，官宣全系自研",
         "电芯由代工方生产、电池包自制；官宣次日宁德 A 股市值缩水 540 亿元", NAVY),
    ]

    for y, date, head, note, color in rows:
        ax.add_patch(plt.Circle((0.100, y), 0.0075, color=color, zorder=6))
        ax.plot([0.100, 0.128], [y, y], color=color, linewidth=1.2, zorder=2)
        ax.text(0.145, y + 0.015, date, fontsize=7.4, color=GRAY,
                ha="left", va="center")
        ax.text(0.145, y - 0.012, head, fontsize=9.6, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(0.145, y - 0.038, note, fontsize=7.6, color=SLATE,
                ha="left", va="center")

    # 右侧三条阶段带（右沿与正文右边界 0.955 对齐）
    bands = [
        (0.625, 0.180, "阶段一　绑定", NAVY,
         ["协议写明供什么电池，",
          "没写供不上时怎么算。",
          "绑定之后先到的，是缺口。"]),
        (0.400, 0.200, "阶段二　给不够", RED,
         ["指标与实到差了 50%，",
          "行业能接受的偏差是 15%。",
          "同期宁德产能利用率 96.9%。"]),
        (0.235, 0.140, "阶段三　分不清", TEAL,
         ["自研解决「谁排产」，",
          "没解决「谁定召回、谁付账」。"]),
    ]
    for by, bh, name, color, lines in bands:
        card(ax, 0.765, by, 0.190, bh, color, face="white", lw=1.2)
        ax.text(0.787, by + bh - 0.030, name, fontsize=9.4, color=color,
                weight="bold", ha="left", va="center", zorder=7)
        ly = by + bh - 0.068
        for t in lines:
            ax.text(0.787, ly, t, fontsize=7.2, color=SLATE,
                    ha="left", va="center", zorder=7)
            ly -= 0.032

    punchline(fig, "协议解决的是「供什么」，没有解决「供不上怎么办、出了事谁定」。")
    footer(fig, "事实来源：宁德时代官网 2025-09-19；《21 汽车·一见 Auto》2026-11-18（经凤凰网科技、搜狐等转述）；"
                "甲子光年 2026-02-10；财经生活帮 2026-11-21。时点按公开报道归位，同一月份内事件的先后顺序未逐日核对。")
    fig.savefig(OUT + "图1_十三个月两段关系.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """同一场召回，三个数字，一个没法回答的问题"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "同一场召回，三个数字，一个没法回答的问题",
           "召回范围定了，分摊比例没人定")

    # 左：三个数字，每组占 0.150，落在 0.215 ~ 0.675
    nums = [
        ("11411", "辆", "备案召回数量",
         "2024 款 MEGA，免费更换冷却液、动力电池、前电机控制器", NAVY),
        ("11", "亿元", "财报口径损失",
         "理想汽车披露的召回相关损失", RED),
        ("20", "亿元+", "内部人士称实际花费",
         "报道口径，非公司披露", RED),
    ]
    y = 0.675
    for v, unit, label, note, color in nums:
        ax.text(0.045, y, v, fontsize=21.0, color=color, weight="bold",
                ha="left", va="center")
        ax.text(0.290, y + 0.010, unit, fontsize=9.4, color=color,
                ha="left", va="center")
        ax.text(0.045, y - 0.048, label, fontsize=9.2, color=DARK,
                ha="left", va="center")
        ax.text(0.045, y - 0.080, note, fontsize=7.4, color=SLATE,
                ha="left", va="center")
        y -= 0.150

    # 右：分歧卡（0.330 ~ 0.730）
    card(ax, 0.452, 0.330, 0.503, 0.400, LIGHT, lw=1.0)
    ax.text(0.476, 0.700, "召回前的沟通会上，两句话", fontsize=9.4,
            color=DARK, weight="bold", ha="left", va="center", zorder=6)
    ax.plot([0.476, 0.931], [0.678, 0.678], color=LIGHT, linewidth=0.9, zorder=6)

    card(ax, 0.476, 0.578, 0.455, 0.070, GRAY, face="white", lw=1.0)
    ax.text(0.494, 0.629, "宁德方面（据《一见 Auto》报道）", fontsize=7.4,
            color=GRAY, ha="left", va="center", zorder=7)
    ax.text(0.494, 0.601, "建议「单点解决，不做大规模召回」", fontsize=9.0,
            color=DARK, ha="left", va="center", zorder=7)

    card(ax, 0.476, 0.455, 0.455, 0.100, RED, face="white", lw=1.3)
    ax.text(0.494, 0.532, "理想高管当场反问", fontsize=7.4,
            color=RED, ha="left", va="center", zorder=7)
    ax.text(0.494, 0.500, "「如果再出现一台车辆自燃，", fontsize=9.0,
            color=DARK, ha="left", va="center", zorder=7)
    ax.text(0.494, 0.472, "你们能跟我们一起承担责任吗？」", fontsize=9.0,
            color=DARK, ha="left", va="center", zorder=7)

    ax.text(0.476, 0.420, "报道记述：对此没有答复，会议不了了之。",
            fontsize=8.0, color=SLATE, ha="left", va="center", zorder=7)
    ax.text(0.476, 0.385, "最终由理想独自完成 11411 辆的召回。", fontsize=8.0,
            color=NAVY, ha="left", va="center", zorder=7)
    ax.text(0.476, 0.348, "宁德律师函否认干预召回，称缺陷源于整车厂选定的冷却液。",
            fontsize=7.2, color=GRAY, ha="left", va="center", zorder=7)

    # 中间一句判断
    ax.plot([0.045, 0.432], [0.238, 0.238], color=LIGHT, linewidth=1.0)
    ax.text(0.045, 0.205, "分歧不在「有没有缺陷」，而在「多大的缺陷\n要多大范围的召回」，以及决定错了谁付账。",
            fontsize=8.6, color=DARK, ha="left", va="center", linespacing=1.8)

    punchline(fig, "能被追问的是责任，没有答案的是机制。")
    footer(fig, "事实来源：《21 汽车·一见 Auto》2026-11-18（经凤凰网科技、搜狐等转述）；理想汽车召回备案（2025-10-31）；"
                "宁德时代委托汇业律师事务所律师函（2026-11-21 经媒体转述）。")
    fig.savefig(OUT + "图2_召回分歧.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """i6 交付缺口：指标 8000，实到 4000"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "一个月的电池包：指标 8000，实到 4000",
           "缺口 50%，行业里能接受的偏差是 15% 以内")

    base_y = 0.320
    bar_w = 0.115
    max_h = 0.330

    bars = [
        (0.070, 8000, "指标", "理想下发（《一见 Auto》）", NAVY),
        (0.320, 4000, "实到", "宁德交付（《一见 Auto》）", RED),
    ]
    for x, val, tag, who, color in bars:
        h = max_h * (val / 8000.0)
        ax.add_patch(Rectangle((x, base_y), bar_w, h, facecolor=color,
                               edgecolor=color, linewidth=1.0, zorder=3))
        ax.text(x + bar_w / 2, base_y + h + 0.018, f"{val:,}", fontsize=14.0,
                color=color, weight="bold", ha="center", va="bottom", zorder=6)
        ax.text(x + bar_w / 2, base_y - 0.034, tag, fontsize=9.2, color=DARK,
                ha="center", va="top")
        ax.text(x + bar_w / 2, base_y - 0.066, who, fontsize=7.2, color=GRAY,
                ha="center", va="top")

    ax.plot([0.055, 0.465], [base_y, base_y], color=SLATE, linewidth=1.2)

    # 缺口标注：从实到柱顶画到指标柱顶
    ax.add_patch(FancyArrowPatch(
        (0.380, base_y + max_h), (0.380, base_y + max_h * 0.5),
        arrowstyle="<|-|>", mutation_scale=11, color=RED, linewidth=1.3,
        connectionstyle="arc3,rad=0", zorder=5))
    ax.text(0.398, base_y + max_h * 0.78, "缺口 4000 个\n即 50%", fontsize=9.2,
            color=RED, weight="bold", ha="left", va="center", linespacing=1.7)

    # 15% 容忍带：以指标 8000 为基准，下限画在 6800 处
    tol_y = base_y + max_h * 0.85
    ax.plot([0.055, 0.500], [tol_y, tol_y], color=TEAL, linewidth=1.2,
            linestyle=(0, (5, 3)), zorder=4)
    ax.add_patch(Rectangle((0.055, tol_y), 0.410, base_y + max_h - tol_y,
                           facecolor=TEAL, alpha=0.06, edgecolor="none",
                           zorder=2))
    ax.text(0.058, base_y + max_h + 0.052, "偏差 15% 的容忍下限（约 6800 个）", fontsize=7.4,
            color=TEAL, ha="left", va="bottom", zorder=5)

    # 右侧：两套解释 + 后果
    card(ax, 0.520, 0.310, 0.435, 0.385, LIGHT, lw=1.0)
    ax.text(0.544, 0.668, "缺口为什么出现，公开报道有两套解释", fontsize=8.8,
            color=DARK, weight="bold", ha="left", va="center", zorder=7)
    ax.plot([0.544, 0.931], [0.648, 0.648], color=LIGHT, linewidth=0.9, zorder=7)

    ax.text(0.544, 0.618, "一说：产能真的不够", fontsize=8.4, color=RED,
            weight="bold", ha="left", va="center", zorder=7)
    ax.text(0.544, 0.575, "宁德 2025 年上半年产能利用率已升至 90% 以上，\n"
                          "10 月自述满负荷；产能优先保障有资本绑定的车企。",
            fontsize=7.4, color=SLATE, ha="left", va="center", zorder=7,
            linespacing=1.75)

    ax.text(0.544, 0.498, "一说：节奏与定制", fontsize=8.4, color=NAVY,
            weight="bold", ha="left", va="center", zorder=7)
    ax.text(0.544, 0.443, "i6 上市提前至 9 月 26 日，理想对电池定制与极端工况\n"
                          "要求高于国标，生产耗时更长；四季度产能规划原为\n"
                          "4.5 万至 5 万辆，订单火爆后上调至 6.8 万辆。",
            fontsize=7.4, color=SLATE, ha="left", va="center", zorder=7,
            linespacing=1.75)

    ax.plot([0.544, 0.931], [0.396, 0.396], color=LIGHT, linewidth=0.9, zorder=7)
    ax.text(0.544, 0.374, "后果", fontsize=8.0, color=DARK, weight="bold",
            ha="left", va="center", zorder=7)
    ax.text(0.544, 0.336, "i6 全年只交付 2.9 万台，约 1 万台推迟到 2026 年；\n"
                          "11 月起启用双供应商，改配欣旺达电池可加快提车。",
            fontsize=7.4, color=SLATE, ha="left", va="center", zorder=7,
            linespacing=1.6)

    punchline(fig, "缺口是事实；缺口为什么出现，公开报道里至少有两套解释。")
    footer(fig, "事实来源：《21 汽车·一见 Auto》2026-11-18（8000/4000 个、96.9%、15% 口径）；"
                "甲子光年 2026-02-10（利用率 90% 以上、产能规划上调）；财经生活帮 2026-11-21（双供应商）。")
    fig.savefig(OUT + "图3_i6交付缺口.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)
