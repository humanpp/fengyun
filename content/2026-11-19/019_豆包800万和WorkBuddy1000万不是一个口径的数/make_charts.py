# -*- coding: utf-8 -*-
"""
《豆包 800 万和 WorkBuddy 1000 万，不是一个口径的数》配套图表
事实口径（2026-11-19，逐条核对财新、第一财经、界面、QuestMobile 与腾讯财报后）：
  · 2026 年 11 月 18 日晚间，腾讯与字节跳动先后披露旗下 AI 智能体数据。
  · 腾讯（00700.HK）在 2026 年第三季度财报中披露：截至 11 月初，WorkBuddy
    日活跃用户数超过 1000 万，日均 Token 消耗量超过 100 万亿；按大模型 Token
    消耗量口径统计，为国内用量最高的 AI 产品（腾讯 Q3 财报、财新 11-18、
    第一财经 11-19、界面 11-19）。
  · 腾讯总裁刘炽平在当晚分析师会上补充：WorkBuddy 最近七天收入按年化折算
    超过 5 亿美元，是腾讯会议的两倍以上；三季度收入是二季度的 5 倍以上；
    中国百强企业已有 60% 成为其客户（新浪科技 11-18、界面 11-19）。
  · 字节跳动随后宣布：豆包工作上线三个月，日活跃用户数（DAU）突破 800 万，
    企业客户年度经常性收入（ARR）突破 20 亿元（每日经济新闻 11-18、
    第一财经 11-18、IT之家 11-18、新华网 08-25 发布稿）。
  · 豆包工作于 2026 年 8 月 25 日正式发布，是豆包面向生产力场景的 Agent 产品；
    11 月 16 日上线「工作台」功能，首批覆盖金融、医疗、教育、创意设计等
    21 个专业场景；此前已接入 Kimi、GLM、DeepSeek 等第三方模型
    （新华网 08-25、环球网 11-18、IT之家 11-18）。
  · 口径差异的关键证据：QuestMobile 2026 年 9 月办公类 Agent 月活数据——
    WorkBuddy 合计月活 3235.3 万（季度环比 +647.1%）、百度搭子 977.0 万、
    千问办公 790.5 万、腾讯 QClaw 317.3 万、豆包工作 204.9 万、TRAE Work 204.2 万；
    该统计将 App、网页端、PC 客户端等不同渠道活跃用户合并计算
    （QuestMobile 2026 年三季度 AI 应用市场报告、199IT 10-20、TechWeb 10-20）。
    即：同为 2026 年 9 月，第三方口径下豆包工作月活 204.9 万，
    与官方 11 月披露的 DAU 800 万不在同一量级，二者不可直接比较。
  · 财新对两家数据的判断："腾讯的 AI 办公智能体用户领先，豆包工作的
    商业化能力强于 WorkBuddy"（财新 11-18 22:45）。
  · 第一财经提示："一时的 DAU 或 ARR 数据仅具备参考意义"；
    并指出月度是最短的合理年化周期，季度更稳定（第一财经 11-19）。
  · 行业盘子：中国企业级 AI 智能体市场 2025 年约 212 亿元，2026 年预计
    增至 449 亿元，2029 年有望突破 3320 亿元（中国通信工业协会数据中心委员会
    《2026 中国企业级 AI 智能体产业白皮书》，经第一财经 06-09、
    界面 06-09、南京软件大会 06-26 转述）。
本文换算（非当事方口径）：20 亿元 ÷ 800 万 DAU ≈ 每 DAU 年化收入 250 元；
5 亿美元按 1 美元≈7.1 元人民币折算约 35.5 亿元；
"7 天年化"与"年度经常性收入"是两种不同算法，不可直接相减。
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


def canvas(fig):
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return ax


# ------------------------------------------------------------------ 图 1
def fig1():
    fig = base("同一晚，两个数，两把尺子",
               "2026 年 11 月 18 日｜两家各自披露的口径并不相同")
    ax = canvas(fig)

    cards = [
        ("腾讯 WorkBuddy", "Q3 财报披露", NAVY,
         "日活跃用户 超 1000 万",
         "日均 Token 消耗 超 100 万亿\n口径：Token 用量，非用户数",
         0.520),
        ("字节 豆包工作", "官方战报", RED,
         "日活跃用户 突破 800 万",
         "企业客户 ARR 突破 20 亿元\n口径：上线三个月，含收入指标",
         0.140),
    ]

    PT = 1.0 / (4.76 * 72.0)
    CARD_H = 0.300

    for name, src, color, main, note, y0 in cards:
        top = y0 + CARD_H
        ax.add_patch(FancyBboxPatch((0.028, y0), 0.944, CARD_H,
                                    boxstyle="round,pad=0.006",
                                    facecolor="white", edgecolor=LIGHT,
                                    linewidth=1.0))
        ax.add_patch(Rectangle((0.028, y0), 0.008, CARD_H,
                               facecolor=color, edgecolor="none"))

        y = top - 8.0 * PT
        ax.text(0.072, y, name, fontsize=10.4, color=color, weight="bold",
                ha="left", va="top")

        y -= (10.4 + 4.0) * PT
        ax.text(0.072, y, src, fontsize=8.4, color=GRAY, ha="left", va="top")

        y -= (8.4 + 11.0) * PT
        ax.text(0.072, y, main, fontsize=15.0, color=DARK, weight="bold",
                ha="left", va="top")

        y -= (15.0 + 8.0) * PT
        ax.text(0.072, y, note, fontsize=8.4, color=SLATE, ha="left",
                va="top", linespacing=1.8)

    ax.text(0.028, 0.080,
            "一个讲用户规模、一个同时讲收入；一个来自财报、一个来自自家战报。",
            fontsize=8.8, color=SLATE, ha="left", va="center")

    punchline(fig, "两个数字都真，但不能直接比大小。")
    footer(fig, "事实：腾讯 2026 年 Q3 财报、财新 11-18、第一财经 11-19、"
                "每日经济新闻 11-18、IT之家 11-18｜制图：本文")
    fig.savefig(OUT + "图1_同一晚两个数.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("官方 800 万，第三方 205 万",
               "同一个产品，两套统计口径｜官方为 11 月 18 日披露，第三方为 9 月数据")
    ax = canvas(fig)

    ax.text(0.028, 0.836, "豆包工作：两个口径下的规模", fontsize=10.4,
            color=DARK, weight="bold", ha="left", va="center")

    x0 = 0.330
    scale = 0.430 / 900.0

    bars = [
        ("官方披露 DAU", "11 月 18 日宣布", 800, NAVY),
        ("第三方月活", "QuestMobile 9 月", 204.9, GRAY),
    ]

    y = 0.700
    for name, note, v, color in bars:
        ax.add_patch(Rectangle((x0, y - 0.042), v * scale, 0.084,
                               facecolor=color, edgecolor="none"))
        ax.text(0.028, y + 0.026, name, fontsize=9.6, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(0.028, y - 0.026, note, fontsize=8.0, color=GRAY,
                ha="left", va="center")
        label = "800 万" if v == 800 else "204.9 万"
        ax.text(x0 + v * scale + 0.014, y, label, fontsize=12.4, color=DARK,
                weight="bold", ha="left", va="center")
        y -= 0.150

    ax.text(0.028, 0.470,
            "差近 4 倍。不是谁造假——官方口径是自家产品后台，第三方只统计能被监测到的渠道。",
            fontsize=8.8, color=SLATE, ha="left", va="center")

    ax.plot([0.028, 0.972], [0.418, 0.418], color=LIGHT, linewidth=0.9)

    ax.text(0.028, 0.360, "同月 QuestMobile 办公类 Agent 月活榜", fontsize=10.0,
            color=DARK, weight="bold", ha="left", va="center")

    rows = [
        ("腾讯 WorkBuddy", "3235.3 万", NAVY),
        ("百度搭子", "977.0 万", SLATE),
        ("阿里千问办公", "790.5 万", SLATE),
        ("腾讯 QClaw", "317.3 万", SLATE),
        ("豆包工作", "204.9 万", RED),
        ("TRAE Work", "204.2 万", SLATE),
    ]

    y = 0.288
    for name, val, color in rows:
        bold = (color == RED)
        ax.text(0.048, y, name, fontsize=9.0, color=(DARK if bold else SLATE),
                weight=("bold" if bold else "normal"), ha="left", va="center")
        ax.text(0.330, y, val, fontsize=9.4, color=color,
                weight="bold", ha="left", va="center")
        y -= 0.046

    punchline(fig, "第三方榜上排第五，和官方说的 800 万，差着量级。")
    footer(fig, "事实：QuestMobile 2026 年三季度 AI 应用市场报告（9 月数据，"
                "多端合计月活）、199IT 10-20、TechWeb 10-20；"
                "官方数据据每日经济新闻 11-18｜制图：本文")
    fig.savefig(OUT + "图2_官方800万第三方205万.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("两家的强项不在同一条线上",
               "用户规模看腾讯，商业化效率看字节｜财新的判断")
    ax = canvas(fig)

    ax.plot([0.500, 0.500], [0.170, 0.800], color=LIGHT, linewidth=1.0)

    ax.text(0.250, 0.800, "用户规模", fontsize=11.0, color=NAVY,
            weight="bold", ha="center", va="center")
    ax.text(0.750, 0.800, "商业化", fontsize=11.0, color=RED,
            weight="bold", ha="center", va="center")

    left = [
        ("DAU 超 1000 万", "腾讯 Q3 财报"),
        ("月活 3235.3 万", "QuestMobile 9 月"),
        ("日均 Token 超 100 万亿", "腾讯口径，国内最高"),
    ]
    right = [
        ("企业 ARR 超 20 亿元", "上线仅三个月"),
        ("每 DAU 年化约 250 元", "本文换算"),
        ("百强企业 60% 是客户", "腾讯 WorkBuddy 口径"),
    ]

    y = 0.690
    for text, note in left:
        ax.text(0.230, y, text, fontsize=9.6, color=DARK, weight="bold",
                ha="right", va="center")
        ax.text(0.230, y - 0.044, note, fontsize=8.0, color=GRAY,
                ha="right", va="center")
        y -= 0.150

    y = 0.690
    for text, note in right:
        ax.text(0.770, y, text, fontsize=9.6, color=DARK, weight="bold",
                ha="left", va="center")
        ax.text(0.770, y - 0.044, note, fontsize=8.0, color=GRAY,
                ha="left", va="center")
        y -= 0.150

    ax.add_patch(FancyBboxPatch((0.028, 0.130), 0.944, 0.086,
                                boxstyle="round,pad=0.008",
                                facecolor="white", edgecolor=LIGHT,
                                linewidth=1.0))
    ax.text(0.052, 0.173,
            "行业盘子：企业级 AI 智能体市场 2025 年约 212 亿元，2026 年预计 449 亿元。",
            fontsize=9.0, color=SLATE, ha="left", va="center")

    punchline(fig, "争的不是谁第一，是两条路哪条先跑通。")
    footer(fig, "事实：财新 11-18（\"腾讯的 AI 办公智能体用户领先，"
                "豆包工作的商业化能力强于 WorkBuddy\"）、腾讯 Q3 财报、"
                "QuestMobile 9 月、CIDC 白皮书｜每 DAU 年化收入为本文换算｜制图：本文")
    fig.savefig(OUT + "图3_两条线各强一头.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)
