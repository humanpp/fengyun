# -*- coding: utf-8 -*-
"""
《45 亿美元买推理平台，AMD 再补推理芯片》配套图表
事实口径（2026-11-19，逐条核对公开报道与公司公告后）：
  · AMD 完成收购 World Labs：9 月 28 日签约，11 月 16 日交割，82 亿美元【全股票】；
    李飞飞出任执行副总裁兼首席科学家（AMD 新闻稿、Yahoo Finance 11-16、WSJ/CNBC 9-28）；
  · AMD 完成收购 Taalas：8 月 6 日签约，11 月 17 日交割；多伦多，2023 年成立；
    把训练好的模型权重烧进硅片，即"模型专用"推理芯片；
    11 月 4 日季报估值约 29 亿美元（【现金加股票】，含或有对价）；
    技术并入加速器路线图，与 Instinct GPU 配套（AMD 新闻稿、Unite.AI、CNBC 8-6）；
  · Palo Alto Networks 11 月 18 日宣布以 45 亿美元【全股票】收购 Applied Compute，
    预计 FY2027 第三财季交割；Applied Compute 2025 年由三位前 OpenAI 研究员创立，
    做开放权重模型的后训练与推理，含自动扩缩推理引擎与 Shift-1 模型路由；
    客户含微软、DoorDash；11 月初以 32.5 亿美元估值融资 3.5 亿美元，ARR 逾 1 亿美元。
本文换算（非当事方口径）：45 / 29 ≈ 1.55（平台比芯片贵约 55%）；
45 / 32.5 ≈ 1.38（两周溢价约 38%）；45 亿 / 1 亿 ARR ≈ 45 倍。
风格：克制传媒风，白底、低饱和配色、标题即结论。输出目录 = 脚本所在目录。
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False

NAVY = "#1f3a5f"
RED = "#b5544a"
GRAY = "#8a8f98"
SLATE = "#5f6673"
LIGHT = "#d8dbe0"
DARK = "#2b2f36"
PALE = "#eef0f3"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep

V_WORLDLABS = 82.0
V_TAALAS = 29.0
V_APPLIED = 45.0
PRE_APPLIED = 32.5
ARR = 1.0

PREM_PLATFORM = (V_APPLIED / V_TAALAS - 1) * 100
PREM_ROUND = (V_APPLIED / PRE_APPLIED - 1) * 100
PS = V_APPLIED / ARR


def base(title, sub):
    fig = plt.figure(figsize=(12, 6.8))
    fig.patch.set_facecolor("white")
    fig.text(0.045, 0.950, title, fontsize=20, color=DARK, weight="bold",
             ha="left", va="top")
    fig.text(0.045, 0.876, sub, fontsize=10.4, color=GRAY, ha="left", va="top")
    return fig


def footer(fig, text):
    fig.text(0.045, 0.014, text, fontsize=8.2, color=GRAY, ha="left", va="center")


def punchline(fig, text, y=0.078):
    fig.text(0.045, y, text, fontsize=10.8, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.6", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


# ------------------------------------------------------------------ 图 1
def fig1():
    fig = base("三天，三笔，三个不同的层",
               "2026 年 11 月 16—18 日｜金额为公告口径：World Labs 与 Applied Compute 为全股票，"
               "Taalas 为现金加股票")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    x0 = 0.330
    scale = 0.360 / V_WORLDLABS

    rows = [
        ("11 月 16 日", "AMD ｜ World Labs", "模型研究 · 空间智能",
         V_WORLDLABS, NAVY, 0.745),
        ("11 月 17 日", "AMD ｜ Taalas", "推理芯片 · 模型专用硅片",
         V_TAALAS, RED, 0.505),
        ("11 月 18 日", "Palo Alto ｜ Applied Compute", "推理平台 · 后训练与部署",
         V_APPLIED, RED, 0.265),
    ]

    for date, name, layer, val, color, y in rows:
        ax.add_patch(Rectangle((x0, y - 0.047), val * scale, 0.094,
                               facecolor=color, edgecolor="none"))
        ax.text(0.030, y + 0.046, date, fontsize=8.6, color=GRAY, ha="left",
                va="center")
        ax.text(0.030, y + 0.002, name, fontsize=10.6, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(0.030, y - 0.044, layer, fontsize=8.6, color=GRAY, ha="left",
                va="center")
        ax.text(0.730, y, "%.0f 亿美元" % val, fontsize=15.0, color=DARK,
                weight="bold", ha="left", va="center")

    ax.plot([0.030, 0.960], [0.178, 0.178], color=LIGHT, linewidth=0.9)
    ax.text(0.030, 0.136,
            "两笔买在推理上：一笔是硅片，一笔是平台。中间那层——从模型到部署之间的工程层——"
            "由第三笔买下，买方不是芯片厂。",
            fontsize=9.2, color=SLATE, ha="left", va="center")

    punchline(fig, "同一周，推理在两个方向被同时买走：一层在硅片里，一层在平台里。")
    footer(fig, "事实：AMD 新闻稿 11-16 与 11-17、Palo Alto Networks 公告与 8-K 11-18、"
                "Bloomberg Law 11-18｜金额为公告口径，未经价格调整｜制图：本文")
    fig.savefig(OUT + "图1_三天三笔三个层.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("同样是买推理，平台比芯片贵一半",
               "左边是 8 月签约、11 月交割的芯片交易；右边是 11 月 18 日宣布的平台交易")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    headers = [
        (0.235, "Taalas　推理芯片", SLATE, "29 亿美元"),
        (0.615, "Applied Compute　推理平台", RED, "45 亿美元"),
    ]
    for x, name, color, money in headers:
        ax.add_patch(Rectangle((x, 0.818), 0.345, 0.006, facecolor=color,
                               edgecolor="none"))
        ax.text(x, 0.778, name, fontsize=10.4, color=color, weight="bold",
                ha="left", va="center")
        ax.text(x, 0.706, money, fontsize=19.0, color=DARK, weight="bold",
                ha="left", va="center")

    rows = [
        ("交易结构", "现金 + 股票，含或有对价", "全股票，可作价格调整"),
        ("时间", "8 月 6 日签约，11 月 17 日交割", "11 月 18 日宣布，FY27Q3 交割"),
        ("买的是什么", "把模型权重烧进硅片，\n模型专用的推理芯片",
         "后训练 + 推理 + 模型路由，\n打包成企业能直接用的层"),
        ("接到哪里", "并入 AMD 加速器路线图，\n与 Instinct GPU 配套",
         "并入安全业务，\n公有云与自有环境都能部署"),
    ]

    yy = 0.612
    for label, left, right in rows:
        ax.text(0.030, yy, label, fontsize=8.8, color=GRAY, ha="left",
                va="center")
        ax.text(0.235, yy, left, fontsize=8.9, color=DARK, ha="left",
                va="center", linespacing=1.7)
        ax.text(0.615, yy, right, fontsize=8.9, color=DARK, ha="left",
                va="center", linespacing=1.7)
        ax.plot([0.030, 0.960], [yy - 0.074, yy - 0.074], color=LIGHT,
                linewidth=0.8)
        yy -= 0.114

    ax.text(0.030, 0.128, "价差与重定价", fontsize=8.8, color=GRAY, ha="left",
            va="center")
    ax.text(0.235, 0.128,
            "平台比芯片贵约 %.0f%%　｜　两周前私募轮估值 32.5 亿美元，本次溢价约 %.0f%%"
            % (PREM_PLATFORM, PREM_ROUND),
            fontsize=9.2, color=SLATE, ha="left", va="center")
    ax.text(0.235, 0.088,
            "按 ARR 逾 1 亿美元算，约 %.0f 倍　｜　以上溢价与倍数为本文换算，非当事方口径"
            % PS,
            fontsize=9.2, color=SLATE, ha="left", va="center")

    punchline(fig, "差价不在技术高低，在稀缺性的位置：能烧硅片的团队少，能把部署打包好的更少。")
    footer(fig, "事实：Taalas 估值据 AMD 11-4 季报（含或有对价）；Applied Compute 私募轮与 ARR "
                "据 SiliconANGLE 11-18｜制图：本文")
    fig.savefig(OUT + "图2_平台比芯片贵一半.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("训练和部署，问的不是同一个问题",
               "训练是一次性的攻坚，部署是每天的账本")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    panels = [
        (0.030, "训练", "模型厂的主场", SLATE,
         ["峰值算力：几万张卡堆上去", "模型分数：榜单上的排名", "一次性：跑完这轮，下一轮重来"]),
        (0.515, "部署", "企业的主场", RED,
         ["单位成本：每百万 token 多少钱", "数据边界：权重留在自己机房",
          "长周期：跑三年，天天在账上"]),
    ]

    for x, title, sub, color, items in panels:
        ax.add_patch(FancyBboxPatch((x, 0.185), 0.455, 0.680,
                                    boxstyle="round,pad=0.010",
                                    facecolor="white", edgecolor=LIGHT,
                                    linewidth=1.0))
        ax.add_patch(Rectangle((x, 0.859), 0.455, 0.006, facecolor=color,
                               edgecolor="none"))
        ax.text(x + 0.032, 0.792, title, fontsize=15.0, color=color,
                weight="bold", ha="left", va="center")
        ax.text(x + 0.032, 0.736, sub, fontsize=9.0, color=GRAY, ha="left",
                va="center")
        ax.plot([x + 0.032, x + 0.423], [0.694, 0.694], color=LIGHT, lw=0.8)

        yy = 0.612
        for it in items:
            ax.plot([x + 0.034], [yy], marker="o", markersize=4.0, color=color)
            ax.text(x + 0.058, yy, it, fontsize=10.0, color=DARK, ha="left",
                    va="center")
            yy -= 0.152

    ax.text(0.030, 0.120,
            "Palo Alto 董事长兼 CEO Nikesh Arora：每家企业都会混跑开源和闭源模型，"
            "而每一个都需要被保护。开放权重把数据留在自己机房，也把部署的活留给了自己。",
            fontsize=9.0, color=SLATE, ha="left", va="center")

    punchline(fig, "训练决定能不能上榜，部署决定能不能上账。")
    footer(fig, "事实：Arora 表述据 Palo Alto Networks 11-18 公告；"
                "两类诉求的归纳为作者判断｜制图：本文")
    fig.savefig(OUT + "图3_训练与部署.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)
