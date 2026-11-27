# -*- coding: utf-8 -*-
"""
《5% 的利用率，和一条被 AI 抽紧的供给曲线》配套图表

事实口径（逐条可指回）：
  · Cheeky Pint 播客（主播 John Collison，Stripe 联合创始人）2026-10-29
    发布，第 39 期《Why Sam Altman is against a single superintelligence》，
    约 29 分 30 秒处，奥特曼谈本地推理："But from a global allocation
    perspective, actually, it's quite terrible to have everybody have a
    bunch of the world's limited supply of DRAM sitting in their own
    computer." 随后："And be used 5% of the time." / "You want maximum
    utilization in the cloud if you're trying to deal with this very
    constrained environment." / "Given that the world is going to be
    limited in its silicon capacity, we all have a shared interest."
    同一段落中他还提到 DRAM 厂商"投 200 亿美元只赚回 190 亿"的历史，
    以及"看不见的手正在失灵"。
  · 马斯克 2026-11-01 前后在 X 发帖"民众也有权拥有自己的 RAM"，并配
    改编自电影《无耻混蛋》的梗图（据 TechNews 科技新报 2026-11-03、
    IT之家 2026-11-02 等转述）。
  · 奥特曼 2026-11-03 起在 X 回应，称言论被断章取义，表示"我想让你们
    拥有海量的内存，咱们多造点"，并把账号名短暂改为 "Ram Altman"
    （据新智元 2026-11-08、虎嗅 2026-11-05 等转述）。
  · 美光执行副总裁兼首席商务官 Sumit Sadana：HBM3E 与 DDR5 的"置换
    比"约为 1:3，即生产 100 bit HBM 会使 DDR 产出减少约 300 bit；
    HBM4E 时该比例可能接近 1:4（据 Yahoo Finance、BigGo Finance 等
    转述其公开表述，及美光高盛半导体会议纪要）。
  · 东吴证券测算：HBM 占 DRAM 总产能比重 2024 年 12.3%、2025 年 17.1%、
    2026 年 20.8%、2027 年 22.5%（经爱集微 2026-09-29 转述）；
    三星高管称 2026 年约 20%、2027 年接近 30%（路透 2026-09-29，
    TrendForce 转述）。两组口径不同，本文并列。
  · Akiba PC Hotline 2026-10-29 发布秋叶原采样（10 月 17—24 日）：
    海盗船 DDR5-6000 128GB（64GB×2）套装报 514,800 日元，一年前
    追踪起点（2025-10-04）为 59,800 日元，累计涨幅约 761%。
  · OpenAI 与三星、SK 海力士 2025-10-01 签署意向书，为"星际之门"供应
    存储芯片，OpenAI 总需求可能达每月 90 万片晶圆（路透、华尔街见闻）。
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
    """一句话，七天"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "一句话，七天，四步",
           "从播客里的资源分配，到账号名里的一个字母")

    stages = [
        ("10.29", "播客原话", "“it's quite terrible”",
         "全球分配视角下，把有限 DRAM 放在\n个人电脑里、只有 5% 的时间在用。\n他主张云端最大化利用率。", NAVY, 0.120,
         "Cheeky Pint 第 39 期，第 29 分前后"),
        ("11.01", "马斯克回应", "“民众也有权拥有自己的 RAM”",
         "配图改编自电影《无耻混蛋》：\n军官挨家挨户搜查私藏的内存条。", RED, 0.375,
         "在 X 发帖，未点名"),
        ("11.03", "奥特曼回应", "“我想让你们拥有海量的内存”",
         "称自己被断章取义；舆论并未平息，\n社区笔记贴回了原话。", TEAL, 0.630,
         "在 X 回应，措辞明显带火气"),
        ("11.04—05", "改名", "Ram Altman",
         "把 X 账号名里的 Sam 改成 Ram，\n以自嘲方式收场。", SLATE, 0.885,
         "账号仍是 @sama"),
    ]

    # 时间轴
    ax.plot([0.075, 0.960], [0.745, 0.745], color=LIGHT, linewidth=1.4, zorder=1)

    for i, (date, name, quote, note, color, cx, foot) in enumerate(stages):
        ax.add_patch(plt.Circle((cx, 0.745), 0.0085, color=color, zorder=6))
        ax.text(cx, 0.782, date, fontsize=9.0, color=color, weight="bold",
                ha="center", va="center")
        ax.plot([cx, cx], [0.745, 0.700], color=color, linewidth=1.1, zorder=2)

        w = 0.200
        bx = cx - w / 2
        bx = min(max(bx, 0.030), 0.965 - w)
        card(ax, bx, 0.360, w, 0.330, color, lw=1.3)
        ax.text(bx + 0.014, 0.658, name, fontsize=9.6, color=color,
                weight="bold", ha="left", va="center", zorder=7)
        ax.plot([bx + 0.014, bx + w - 0.014], [0.638, 0.638], color=LIGHT,
                linewidth=0.9, zorder=7)
        ax.text(bx + 0.014, 0.596, quote, fontsize=8.2, color=DARK,
                weight="bold", ha="left", va="center", zorder=7,
                linespacing=1.6)
        ax.text(bx + 0.014, 0.500, note, fontsize=7.4, color=SLATE,
                ha="left", va="center", zorder=7, linespacing=1.9)
        ax.text(bx + 0.014, 0.392, foot, fontsize=6.9, color=GRAY,
                ha="left", va="center", zorder=7)

    # 下方一句收口
    ax.plot([0.045, 0.955], [0.300, 0.300], color=LIGHT, linewidth=1.0)
    ax.text(0.045, 0.248,
            "前两步说的是「谁该拥有内存」，后两步说的是「我说的是什么意思」。\n"
            "四步之间，没有人谈过供给：为什么这一年的内存会紧张到这个地步。",
            fontsize=8.8, color=DARK, ha="left", va="center", linespacing=1.9)

    punchline(fig, "一场七天的争论，三句话都成立，也都不是重点。")
    footer(fig, "事实来源：Cheeky Pint 第 39 期（2026-10-29，第 29 分钟前后）；马斯克 X 帖（2026-11-01 前后）；"
                "奥特曼 X 回应与改名（2026-11-03 至 11-05）。日期据 IT之家、TechNews、新智元等媒体转述。")
    fig.savefig(OUT + "图1_一句话七天四步.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """HBM 挤占通用 DRAM 的两组口径"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "HBM 吃掉的那部分产能",
           "两家机构给出两组口径，趋势一致，刻度不同")

    base_y = 0.290
    max_h = 0.380

    def bar(x, h_ratio, color, top_label, series_label):
        h = max_h * h_ratio
        ax.add_patch(Rectangle((x, base_y), 0.062, h, facecolor=color,
                               edgecolor=color, linewidth=1.0, zorder=3))
        ax.text(x + 0.031, base_y + h + 0.014, top_label, fontsize=8.4,
                color=color, weight="bold", ha="center", va="bottom",
                zorder=6)
        ax.text(x + 0.031, base_y - 0.030, series_label, fontsize=7.4,
                color=GRAY, ha="center", va="top")

    # 左组：东吴证券
    grp_a = [("2024", 0.123, "12.3%"), ("2025", 0.171, "17.1%"),
             ("2026E", 0.208, "20.8%"), ("2027E", 0.225, "22.5%")]
    ax.text(0.070, 0.712, "东吴证券测算", fontsize=9.2, color=NAVY,
            weight="bold", ha="left", va="center")
    x = 0.070
    for year, ratio, label in grp_a:
        bar(x, ratio / 0.40, NAVY, label, year)
        x += 0.086

    # 右组：三星口径
    grp_b = [("2026", 0.200, "约 20%"), ("2027E", 0.300, "近 30%")]
    ax.text(0.520, 0.712, "三星高管表述（路透，2026-09-29）", fontsize=9.2,
            color=RED, weight="bold", ha="left", va="center")
    x = 0.520
    for year, ratio, label in grp_b:
        bar(x, ratio / 0.40, RED, label, year)
        x += 0.086

    ax.plot([0.055, 0.960], [base_y, base_y], color=SLATE, linewidth=1.2)

    # 右侧说明卡（与柱状图区分离，避免遮挡）
    card(ax, 0.700, 0.150, 0.258, 0.520, LIGHT, lw=1.0)
    ax.text(0.718, 0.640, "换算关系", fontsize=8.6, color=DARK,
            weight="bold", ha="left", va="center", zorder=7)
    ax.plot([0.718, 0.940], [0.620, 0.620], color=LIGHT, linewidth=0.9, zorder=7)
    ax.text(0.718, 0.575,
            "美光首席商务官萨达纳：\n"
            "HBM3E 与 DDR5 的置换比约 1:3；\n"
            "每产出 100 bit HBM，\n"
            "DDR 产出减少约 300 bit，\n"
            "HBM4E 时可能接近 1:4。",
            fontsize=7.2, color=SLATE, ha="left", va="top", zorder=7,
            linespacing=1.9)
    ax.text(0.718, 0.440,
            "换算下来，产能占比每升 1 个点，\n"
            "通用 DRAM 有效供给少约 3 个点。",
            fontsize=7.2, color=DARK, ha="left", va="top", zorder=7,
            linespacing=1.9)
    ax.text(0.718, 0.340,
            "注：置换比为厂商口径，非精确\n"
            "会计等式；两组产能占比的统计\n"
            "口径不同，不宜直接相减。",
            fontsize=6.6, color=GRAY, ha="left", va="top", zorder=7,
            linespacing=1.9)

    punchline(fig, "个人电脑里那根内存，不是被谁占着，是被造出来的总量里少了一块。")
    footer(fig, "事实来源：东吴证券测算（经爱集微 2026-09-29 转述）；三星电子高管表述（路透 2026-09-29）；"
                "美光 Sumit Sadana 公开表述（Yahoo Finance、美光高盛半导体会议纪要等）。")
    fig.savefig(OUT + "图2_HBM挤占产能.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """价格落在零售端"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "同一套内存，一年前 59,800 日元",
           "日本秋叶原零售价，东京一家渠道的公开采样")

    base_y = 0.300
    max_h = 0.360

    # 三个时点
    pts = [
        ("2025.10.04", 59800, "59,800 日元", GRAY),
        ("2026.09.12", 316980, "316,980 日元", RED),
        ("2026.10.17", 514800, "514,800 日元", RED),
    ]
    x = 0.085
    for date, val, label, color in pts:
        h = max_h * (val / 520000.0)
        ax.add_patch(Rectangle((x, base_y), 0.105, h, facecolor=color,
                               edgecolor=color, linewidth=1.0, zorder=3))
        ax.text(x + 0.0525, base_y + h + 0.016, label, fontsize=10.2,
                color=color, weight="bold", ha="center", va="bottom",
                zorder=6)
        ax.text(x + 0.0525, base_y - 0.030, date, fontsize=8.2, color=DARK,
                ha="center", va="top")
        x += 0.145

    ax.plot([0.070, 0.560], [base_y, base_y], color=SLATE, linewidth=1.2)

    # 涨幅标注：放在柱子右侧，不压柱身
    ax.add_patch(FancyArrowPatch((0.578, base_y + max_h),
                                (0.578, base_y + max_h * (59800 / 520000.0)),
                                arrowstyle="<|-|>", mutation_scale=11,
                                color=NAVY, linewidth=1.3, zorder=5))
    ax.text(0.596, base_y + max_h * 0.80, "一年累计\n约 +761%", fontsize=9.0,
            color=NAVY, weight="bold", ha="left", va="center", linespacing=1.7)
    ax.text(0.596, base_y + max_h * 0.30, "9 月 12 日到\n10 月 17 日\n单月 +62.4%",
            fontsize=7.8, color=RED, ha="left", va="center", linespacing=1.7)

    # 右侧：涨价是谁造成的
    card(ax, 0.700, 0.150, 0.258, 0.520, LIGHT, lw=1.0)
    ax.text(0.718, 0.628, "这一年里发生了什么", fontsize=8.6, color=DARK,
            weight="bold", ha="left", va="center", zorder=7)
    ax.plot([0.718, 0.940], [0.608, 0.608], color=LIGHT, linewidth=0.9, zorder=7)
    rows = [
        ("三星、SK 海力士、美光把先进产能", SLATE),
        ("优先投向 HBM 与服务器 DDR5，", SLATE),
        ("PC 级常规 DRAM 供给被压缩。", SLATE),
        ("", SLATE),
        ("TrendForce：2026 年三季度", SLATE),
        ("PC DRAM 合约价涨 18%—23%，", SLATE),
        ("四季度预计再涨 13%—18%。", SLATE),
        ("", SLATE),
        ("OpenAI 与两家韩企 2025 年 10 月", SLATE),
        ("签意向书，星际之门的内存需求", SLATE),
        ("最高每月 90 万片晶圆。", SLATE),
        ("", SLATE),
        ("个人用户手里的内存，", DARK),
        ("在总量里只是一小块。", DARK),
    ]
    ly = 0.580
    for t, color in rows:
        if t:
            ax.text(0.718, ly, t, fontsize=7.2, color=color, ha="left",
                    va="center", zorder=7)
        ly -= 0.030

    punchline(fig, "消费者不是在囤积，是在一条被抽紧的供给曲线末端排队。")
    footer(fig, "事实来源：Akiba PC Hotline 2026-10-29 秋叶原采样（10 月 17—24 日），产品为海盗船 DDR5-6000 128GB（64GB×2）套装；"
                "TrendForce 经 Chosun Biz 2026-10-30 转述；OpenAI 与三星、SK 海力士意向书（2025-10-01，路透）。")
    fig.savefig(OUT + "图3_零售端价格.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)
