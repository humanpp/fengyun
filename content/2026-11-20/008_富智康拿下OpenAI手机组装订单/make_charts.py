# -*- coding: utf-8 -*-
"""
《富智康拿下 OpenAI 手机组装订单：模型公司不做 App 了，开始抢手机入口？》配套图表
事实口径（均经公开报道交叉核对）：
  · 2026-11-19 证券时报从供应链获悉：富士康旗下富智康集团（02038.HK）获 OpenAI 手机项目订单，
    参与整机组装；富士康同时是苹果 iPhone 主要组装商；产品方案、订单规模、量产安排均待确认。
  · 富智康当日行情：低开 12.88 港元，早盘最低 12.56（−3.90%），午后最高 14.65（+12.09%），
    收 13.59 港元（+3.98%），成交 4473 万港元，振幅 15.99%，换手 0.42%，市值约 106.3 亿港元；
    同日恒指 −1.95%、恒生科技 −2.33%、消费性电讯设备及零件板块 −2.37%（逆市走强）。
    —— 智通财经、财华社、老虎社区 2026-11-19；前收 13.07 港元由 13.59 − 0.52 推得。
  · 富智康未在港交所披露易就该订单刊发公告或澄清；OpenAI 与鸿海方面均无官方确认。
  · OpenAI 首款 AI 端侧硬件：2026 年底启动出货，立讯精密独家承担整机制造并供应核心零部件；
    形态为甜甜圈状无屏设备（Jony Ive / LoveFrom），含麦克风、扬声器、摄像头及环境传感器，
    以语音交互为主；定价传闻 300—400 美元。—— 每日经济新闻 2026-11-19。
  · 立讯精密与 OpenAI 有多个产品全面合作，"或因资源配置的统筹考量未承接手机组装业务"。
    —— 每日经济新闻 2026-11-18 引供应链人士。
  · 郭明錤：OpenAI AI 智能体手机量产目标由 2028 年提前至 2027 年上半年，联发科有望独家供应
    基于天玑 9600 的定制芯片（台积电 N2P），2027—2028 合计出货约 3000 万部；
    做手机三条理由：掌控 OS 与硬件才能提供完整 AI 智能体服务、手机可持续获取用户实时状态、
    智能手机仍是出货规模最大的个人智能终端之一。—— 天风国际 2026-05，每日经济新闻 2026-11-18 转述。
  · 富智康 2026 前三季度营收 56.36 亿美元（+7.8%）、期内利润 6698.5 万美元（+59.1%）；
    Q3 单季营收 33.65 亿美元（+6.2%）、利润 5480.9 万美元（+52.6%）。—— 公司 2026-11-06 公告。
说明：素材称"午后港股一度涨超 9%"，经核为盘中最高 +12.09%、收盘 +3.98%，图中按实际区间呈现。
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
    fig = base("盘中涨 12%，收盘剩 4%",
               "富智康集团 02038.HK · 2026 年 11 月 19 日")
    ax = canvas(fig)

    def y_of(p):
        return 0.330 + (p - 12.40) / 2.40 * 0.500

    # 网格
    for p in (12.5, 13.0, 13.5, 14.0, 14.5):
        y = y_of(p)
        ax.plot([0.085, 0.930], [y, y], color="#eceef1", linewidth=0.9, zorder=1)
        ax.text(0.072, y, f"{p:.1f}", fontsize=8.6, color=GRAY, ha="right",
                va="center")
    ax.text(0.072, 0.862, "港元", fontsize=8.4, color=GRAY, ha="right",
            va="center")

    # 前收基准线
    ax.plot([0.085, 0.930], [y_of(13.07), y_of(13.07)], color=GRAY,
            linewidth=1.1, linestyle=(0, (6, 4)), zorder=2)
    ax.text(0.927, y_of(13.07) + 0.020, "前收 13.07", fontsize=8.8,
            color=GRAY, ha="right", va="bottom")

    xs = [0.150, 0.370, 0.560, 0.760]
    labels = ["开盘", "早盘最低", "午后最高", "收盘"]
    pts = [
        ("12.88", "−1.45%", 12.88, "down"),
        ("12.56", "−3.90%", 12.56, "down"),
        ("14.65", "+12.09%", 14.65, "up"),
        ("13.59", "+3.98%", 13.59, "up"),
    ]

    ys = [y_of(p[2]) for p in pts]
    ax.plot(xs, ys, color=NAVY, linewidth=2.4, solid_capstyle="round", zorder=4)

    for x, y, lab, (val, note, price, where) in zip(xs, ys, labels, pts):
        col = RED if price == 14.65 else NAVY
        ax.add_patch(Circle((x, y), 0.011, facecolor=col, edgecolor=col,
                            linewidth=2.0, zorder=6))
        ax.text(x, 0.232, lab, fontsize=9.4, color=SLATE, ha="center",
                va="center")
        if where == "up":
            ax.text(x, y + 0.032, val, fontsize=11.0, color=col, weight="bold",
                    ha="center", va="bottom")
            ax.text(x, y + 0.070, note, fontsize=9.6, color=col, weight="bold",
                    ha="center", va="bottom")
        else:
            ax.text(x, y - 0.032, val, fontsize=11.0, color=col, weight="bold",
                    ha="center", va="top")
            ax.text(x, y - 0.068, note, fontsize=9.6, color=col, weight="bold",
                    ha="center", va="top")

    # 高点到收盘的回落
    ax.annotate("", xy=(0.845, y_of(13.59)), xytext=(0.845, y_of(14.65)),
                arrowprops=dict(arrowstyle="<->", color=RED, linewidth=1.4))
    ax.text(0.836, (y_of(13.59) + y_of(14.65)) / 2, "−7.2%", fontsize=10.6,
            color=RED, weight="bold", ha="right", va="center")

    ax.text(0.085, 0.198,
            "同日：恒生指数 −1.95%、恒生科技指数 −2.33%、消费性电讯设备及零件板块 −2.37%。",
            fontsize=9.0, color=SLATE, ha="left", va="center")
    ax.text(0.085, 0.155,
            "振幅 15.99%，成交 4473 万港元，换手 0.42%，市值约 106.3 亿港元。",
            fontsize=9.0, color=SLATE, ha="left", va="center")

    punchline(fig, "消息值 12%，收盘只认 4%——中间那 8% 是“还没确认”。")
    footer(fig, "事实：行情据智通财经、财华社、老虎社区 2026-11-19；前收 13.07 港元由 13.59 − 0.52 推得｜制图：本文")
    fig.savefig(OUT + "图1_盘中12收盘4.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("OpenAI 的硬件不止一款",
               "三条产品线，三家不同的代工方")
    ax = canvas(fig)

    cards = [
        ("无屏 AI 设备", "甜甜圈状，冰球大小\n麦克风 / 扬声器 / 摄像头 / 环境传感器\n以语音交互为主",
         "立讯精密", "独家整机制造\n2026 年底启动出货", NAVY),
        ("AI 手机", "定制天玑 9600（台积电 N2P）\n双 NPU 架构\n主打 AI 智能体",
         "富智康", "获整机组装订单\n2027 上半年量产", RED),
        ("眼镜 / 耳机", "早期规划阶段\n形态与时间均未确定",
         "—", "尚未定点", SLATE),
    ]

    y_top = 0.822
    h = 0.180
    step = 0.216
    for i, (name, desc, maker, when, col) in enumerate(cards):
        y = y_top - i * step
        ax.add_patch(FancyBboxPatch((0.070, y - h), 0.860, h,
                                    boxstyle="round,pad=0.010",
                                    facecolor="#fafbfc", edgecolor=col,
                                    linewidth=1.2))
        # 左侧色条
        ax.add_patch(FancyBboxPatch((0.070, y - h), 0.008, h,
                                    boxstyle="square,pad=0",
                                    facecolor=col, edgecolor="none"))
        ax.text(0.098, y - 0.034, name, fontsize=12.8, color=col,
                weight="bold", ha="left", va="center")
        ax.text(0.098, y - 0.074, desc, fontsize=8.8, color=SLATE,
                ha="left", va="top", linespacing=1.75)

        ax.plot([0.560, 0.560], [y - h + 0.024, y - 0.024], color=LIGHT,
                linewidth=1.0)
        ax.text(0.585, y - 0.048, maker, fontsize=11.2, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(0.585, y - 0.086, when, fontsize=8.8, color=SLATE,
                ha="left", va="top", linespacing=1.75)

    ax.text(0.070, 0.170,
            "同一家公司，三条线，三家代工方：设备交给立讯，手机交给富智康。",
            fontsize=9.6, color=DARK, weight="bold", ha="left", va="center")
    ax.text(0.070, 0.128,
            "立讯与 OpenAI 有多个产品全面合作，“或因资源配置的统筹考量未承接手机组装业务”。",
            fontsize=8.8, color=GRAY, ha="left", va="center")

    punchline(fig, "不是一款设备，是一排入口。")
    footer(fig, "事实：无屏设备据每日经济新闻 2026-11-19；手机规格与量产节奏据郭明錤（天风国际）2026-05 及每日经济新闻 2026-11-18；眼镜/耳机据彭博社等公开报道｜制图：本文")
    fig.savefig(OUT + "图2_三条产品线.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("从 App 到设备",
               "模型公司往下走一层，拿到的不是渠道，是入口")
    ax = canvas(fig)

    layers = [
        ("设备层", "谁决定这台机器长什么样、什么时候开机、麦克风什么时候听",
         "手机厂商 / 硬件公司", 0.720, RED),
        ("系统层", "谁决定默认助手是谁、权限怎么给、通知怎么弹",
         "操作系统厂商", 0.500, GOLD),
        ("应用层", "谁决定用户点开哪个图标、每次多问一句",
         "模型公司（过去的位置）", 0.280, NAVY),
    ]

    for name, desc, who, y, col in layers:
        ax.add_patch(FancyBboxPatch((0.110, y - 0.062), 0.520, 0.124,
                                    boxstyle="round,pad=0.008",
                                    facecolor="#fafbfc", edgecolor=col,
                                    linewidth=1.2))
        ax.text(0.132, y + 0.022, name, fontsize=12.4, color=col,
                weight="bold", ha="left", va="center")
        ax.text(0.132, y - 0.030, desc, fontsize=8.6, color=SLATE,
                ha="left", va="center")
        ax.text(0.660, y, who, fontsize=9.4, color=DARK, ha="left",
                va="center")

    # 向上的箭头：模型公司正在往上走
    ax.annotate("", xy=(0.062, 0.720), xytext=(0.062, 0.280),
                arrowprops=dict(arrowstyle="-|>", color=RED, linewidth=2.2,
                                shrinkA=2, shrinkB=2))
    ax.text(0.040, 0.500, "模型公司正在往上走", fontsize=9.6, color=RED,
            weight="bold", ha="center", va="center", rotation=90)

    ax.text(0.110, 0.168,
            "过去：模型公司做 App，手机厂商预装，双方是合作关系。",
            fontsize=9.4, color=SLATE, ha="left", va="center")
    ax.text(0.110, 0.120,
            "现在：模型公司自己做设备，预装变成竞争——默认入口只有一个。",
            fontsize=9.4, color=RED, weight="bold", ha="left", va="center")

    punchline(fig, "App 是租来的位置，设备是自己的门。")
    footer(fig, "说明：本图为分析框架，非当事方表述；分层参考郭明錤关于“掌控 OS 与硬件才能提供完整 AI 智能体服务”的判断｜制图：本文")
    fig.savefig(OUT + "图3_从App到设备.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)
