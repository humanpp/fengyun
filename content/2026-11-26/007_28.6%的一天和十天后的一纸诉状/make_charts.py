# -*- coding: utf-8 -*-
"""
《28.6% 的一天，和十天后的一纸诉状》配套图表

事实口径（逐条可指回）：
  · 英特尔 2026 财年第三季度财报（2026-10-29 美股盘后发布，Intel 官网
    新闻稿）：季度营收 165.1 亿美元，同比增长 21%，略高于市场预期的
    160 亿美元；但对第四季度给出营收 150 亿—160 亿美元、调整后每股
    收益 0.25 美元的指引，低于华尔街预期（CNBC 2026-10-30、Reuters、
    Yonhap Infomax 转述）。
  · 管理层同时披露：以色列一座工厂发生爆炸（部分报道称"爆炸"，亦有
    表述为"工厂事故/停产"），停产约两周，预计在两个季度内造成约
    6 亿美元收入损失；公司还警告今年将出现现金净流出（Reuters、
    CNA、Calcalist 2026-10-29）。
  · 股价：10 月 30 日单日下跌 29%（CNBC 口径，为 1970 年代以来最差
    单日表现）；Ars Technica 与诉状表述为 28.6%；Yahoo Finance 盘中
    报道为"超过五分之一"；盘后一度跌 21%—23%。不同时点、不同口径，
    本文并列。
  · 证券集体诉讼：2026-11-13（周五）向美国加州北区联邦地区法院圣何塞
    分院提起，案号 5:26-cv-13758（City of Southfield Fire and Police
    Retirement System v. Intel Corporation et al.），由 Robbins Geller
    Rudman & Dowd LLP 代理；被告为英特尔公司、CEO 陈立武（Lip-Bu Tan）
    与 CFO 大卫·津斯纳（David Zinsner）；集体诉讼期 2026-07-23 至
    2026-10-29；指控核心为未及时披露 PC 需求疲软与渠道库存积压对
    客户端业务（CCPG）的实质影响，涉嫌证券欺诈；索赔金额未定。
    法院尚未对指控作出任何认定（Reuters 2026-11-15、BBC 2026-11-16、
    Ars Technica 2026-11-16、财新 2026-11-16、凤凰网 2026-11-17 等）。
  · 陈立武 2025-03-12 被英特尔董事会任命为 CEO，2025-03-18 到任，
    为公司史上第九任 CEO（Intel 官网新闻稿、Reuters 2025-03-12、
    AP 2025-03-12）。
  · 行业背景：2026 年 10 月前后内存价格大幅上涨，PC 整机成本上升，
    压制 PC 需求（Yahoo Finance 2026-10-30 等）。本条为公开报道口径，
    非英特尔公司表述。
  · 同期另一事件（仅作时间参照，与本案无因果关系）：英伟达 2026-11-12
    宣布黄仁勋辞去全部职务，CFO 科莱特·克雷斯任临时 CEO（新华网、
    财新、纽约时报中文网 2026-11-12 至 13）。
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
    """一周之内，两次「下跌」和一次「起立」"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "10 月 29 日到 11 月 13 日：十五天",
           "这份诉状不是芯片业「信任危机」的下集，它只是另一条线")

    rows = [
        ("10.29", "英特尔发布 Q3 财报",
         "营收 165.1 亿美元，超预期；Q4 指引 150 亿—160 亿美元，低于预期",
         "同步披露：以色列工厂停产约两周，预计两季度损失约 6 亿美元收入", NAVY),
        ("10.30", "英特尔股价单日跌约 29%",
         "为 1970 年代以来最差单日表现；诉状表述为 28.6%",
         "同一天，内存涨价压制 PC 需求的消息也在影响整条 PC 产业链", RED),
        ("11.12", "英伟达宣布黄仁勋辞职",
         "即刻卸任 CEO、总裁与董事，CFO 科莱特·克雷斯任临时 CEO",
         "起因是英伟达董事会就其它事项启动的独立调查，与英特尔无关", GRAY),
        ("11.13", "英特尔股东提起集体诉讼",
         "案号 5:26-cv-13758，被告为英特尔、CEO 陈立武、CFO 津斯纳",
         "集体诉讼期 7 月 23 日至 10 月 29 日，指控未披露 PC 疲软与库存", TEAL),
    ]

    y = 0.780
    for date, who, quote, note, color in rows:
        card(ax, 0.045, y - 0.150, 0.910, 0.132, color, lw=1.2)
        ax.text(0.065, y - 0.040, date, fontsize=9.0, color=color,
                weight="bold", ha="left", va="center", zorder=7)
        ax.text(0.175, y - 0.040, who, fontsize=9.0, color=DARK,
                weight="bold", ha="left", va="center", zorder=7)
        ax.text(0.065, y - 0.080, quote, fontsize=8.0, color=DARK,
                ha="left", va="center", zorder=7)
        ax.text(0.065, y - 0.117, note, fontsize=7.3, color=SLATE,
                ha="left", va="center", zorder=7)
        y -= 0.155

    punchline(fig, "两件事在同一周发生，但只有一件和黄仁勋有关。")
    footer(fig, "事实来源：英特尔 2026Q3 财报与 Q4 指引（Intel 官网 2026-10-29，经 CNBC、Reuters 转述）；"
                "股价跌幅据 CNBC 2026-10-30（29%）与诉状表述（28.6%）；集体诉讼信息据 Reuters 2026-11-15、BBC 2026-11-16；"
                "英伟达公告据新华网、财新 2026-11-12。")
    fig.savefig(OUT + "图1_十五天四件事.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """英特尔做对了什么，市场为什么不认"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "业绩超预期，股价跌 29%",
           "这两件事同时成立，才是一场集体诉讼的起点")

    base_y = 0.330
    max_h = 0.330

    # 左：Q3 实际 vs 预期
    ax.text(0.045, 0.740, "Q3 实际营收（超预期）", fontsize=8.8, color=NAVY,
            weight="bold", ha="left", va="center")
    vals = [("实际", 165.1, NAVY), ("市场预期", 160.0, GRAY)]
    x = 0.070
    for label, v, color in vals:
        h = max_h * (v / 180.0)
        ax.add_patch(Rectangle((x, base_y), 0.085, h, facecolor=color,
                               edgecolor=color, linewidth=1.0, zorder=3))
        ax.text(x + 0.0425, base_y + h + 0.014, f"{v:g}", fontsize=10.5,
                color=color, weight="bold", ha="center", va="bottom", zorder=6)
        ax.text(x + 0.0425, base_y - 0.030, label, fontsize=8.0, color=DARK,
                ha="center", va="top")
        x += 0.115

    # 右：Q4 指引区间
    ax.text(0.340, 0.740, "Q4 营收指引（低于预期）", fontsize=8.8, color=RED,
            weight="bold", ha="left", va="center")
    lo_h = max_h * (150.0 / 180.0)
    hi_h = max_h * (160.0 / 180.0)
    ax.add_patch(Rectangle((0.365, base_y), 0.110, lo_h, facecolor=RED,
                           alpha=0.35, edgecolor=RED, linewidth=1.0, zorder=3))
    ax.text(0.420, base_y + lo_h / 2, "150 亿\n—160 亿", fontsize=9.0,
            color=DARK, weight="bold", ha="center", va="center", zorder=6,
            linespacing=1.7)
    ax.plot([0.345, 0.495], [base_y, base_y], color=SLATE, linewidth=1.1)
    ax.text(0.420, base_y - 0.030, "指引区间", fontsize=8.0, color=DARK,
            ha="center", va="top")
    ax.text(0.420, base_y + hi_h + 0.014, "0.25 美元", fontsize=8.4,
            color=RED, ha="center", va="bottom")
    ax.text(0.420, base_y + hi_h + 0.040, "调整后每股收益", fontsize=6.8,
            color=GRAY, ha="center", va="bottom")

    # 右卡：三件拖累
    card(ax, 0.545, 0.300, 0.410, 0.430, LIGHT, lw=1.0)
    ax.text(0.565, 0.700, "指引里写明的三件事", fontsize=8.8, color=DARK,
            weight="bold", ha="left", va="center", zorder=7)
    ax.plot([0.565, 0.935], [0.680, 0.680], color=LIGHT, linewidth=0.9, zorder=7)
    items = [
        ("其一", "以色列工厂停产约两周，\n两个季度预计损失约 6 亿美元收入"),
        ("其二", "PC 需求走弱，\n内存涨价推高整机成本"),
        ("其三", "公司警告今年将出现现金净流出，\n扩产投入仍在继续"),
    ]
    ly = 0.640
    for tag, text in items:
        ax.text(0.565, ly, tag, fontsize=7.6, color=RED, weight="bold",
                ha="left", va="top", zorder=7)
        ax.text(0.625, ly, text, fontsize=7.4, color=SLATE, ha="left",
                va="top", zorder=7, linespacing=1.85)
        ly -= 0.105

    punchline(fig, "业绩是「过去三个月」的答案，股价买的是「下个季度」的确定性。")
    footer(fig, "事实来源：英特尔 2026Q3 财报与 Q4 指引（Intel 官网 2026-10-29）；"
                "以色列工厂停产及损失、现金净流出风险据 Reuters、CNA、Calcalist 2026-10-29；"
                "PC 需求与内存涨价的关系据 Yahoo Finance 2026-10-30。")
    fig.savefig(OUT + "图2_业绩与指引.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """诉状里写了什么，没写什么"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "一纸诉状里有什么，没有什么",
           "把它读成一个法律事件，而不是一场道德审判")

    # 左列：诉状载明
    card(ax, 0.045, 0.240, 0.440, 0.500, NAVY, lw=1.3)
    ax.text(0.068, 0.708, "诉状载明的（可查证）", fontsize=9.2, color=NAVY,
            weight="bold", ha="left", va="center", zorder=7)
    ax.plot([0.068, 0.462], [0.688, 0.688], color=LIGHT, linewidth=0.9, zorder=7)
    left = [
        "受理法院：加州北区联邦地区法院",
        "圣何塞分院；案号 5:26-cv-13758",
        "原告：南菲尔德市消防与警察退休基金",
        "被告：英特尔公司、CEO 陈立武、",
        "　　CFO 大卫·津斯纳",
        "诉讼性质：拟议证券欺诈集体诉讼",
        "集体诉讼期：2026-07-23 至 10-29",
        "指控核心：未及时披露 PC 需求疲软",
        "　　与渠道库存积压对客户端业务的影响",
        "索赔金额：未确定",
        "代理律所：Robbins Geller Rudman & Dowd",
    ]
    ly = 0.652
    for t in left:
        ax.text(0.068, ly, t, fontsize=7.6, color=SLATE, ha="left",
                va="center", zorder=7)
        ly -= 0.037

    # 右列：诉状没有的
    card(ax, 0.515, 0.240, 0.440, 0.500, GRAY, lw=1.3)
    ax.text(0.538, 0.708, "诉状没有、也不该有的（尚待法庭）", fontsize=9.2,
            color=GRAY, weight="bold", ha="left", va="center", zorder=7)
    ax.plot([0.538, 0.932], [0.688, 0.688], color=LIGHT, linewidth=0.9, zorder=7)
    right = [
        "没有认定「陈立武有主观故意」——",
        "　集体诉讼的标准环节，法院尚未裁定",
        "没有认定「披露行为构成欺诈」——",
        "　需要证明明知与因果关系",
        "没有认定「陈立武个人决策失误」",
        "没有认定任何高管个人获利",
        "没有与「华裔 CEO」这一身份相关的",
        "　任何法律主张——诉状未涉及族裔",
        "没有与其他公司的事件建立关联",
    ]
    ly = 0.652
    for t in right:
        color = DARK if not t.startswith("　") else SLATE
        ax.text(0.538, ly, t, fontsize=7.6, color=color, ha="left",
                va="center", zorder=7)
        ly -= 0.045

    punchline(fig, "一份起诉书能说明的，只是有人提出了质疑，不是质疑已经成立。")
    footer(fig, "事实来源：诉状 No. 5:26-cv-13758（N.D. Cal.）；Reuters 2026-11-15、BBC 2026-11-16、"
                "Ars Technica 2026-11-16、财新 2026-11-16、凤凰网 2026-11-17。")
    fig.savefig(OUT + "图3_诉状载明与未定.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)
