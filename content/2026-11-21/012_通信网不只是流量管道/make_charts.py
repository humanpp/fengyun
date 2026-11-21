# -*- coding: utf-8 -*-
"""
《通信网不只是「流量管道」：从人人通信到人机交互，底座换了》配套图表

事实口径（核到新华网 2026-11-06 刊发的主旨演讲全文）：
  · 2026 移动网络大会于 2026-11-05 至 11-07 在广州举行；
    中国移动董事长陈忠岳 2026-11-06 上午发表题为《网络强基 智能共创》的主旨演讲。
  · 演讲三特征：AI 驱动移动网络流量加速增长、引发数据传送结构显著变化、
    呼唤网络与算力融合协同。
  · 战略：落实「六张网」建设部署，实施网络强基、全栈创新发展战略，
    坚持智为先、算为要、通为本，一体建强通信网、算力网、智能网。
  · 第一张网总判断：从人人通信到人机交互、从地面覆盖到空天地海、
    从尽力而为到确定保障，通信网不只是「流量管道」，更应成为「数智底座」。
  · 升级基础网络：提升热点区域深度覆盖，建优铁路 5G 专网，
    加快超级上行技术创新、产业协作和现网部署。
  · 深化星地融合：建强天启星座，增强近海、岛屿、边疆网络能力，
    实现无缝覆盖、永远在线。
  · 完善国际网络基础设施布局：畅通「一带一路」等重点方向数字通道，
    增强通达能力和网络韧性。
  · 加强共建共享：推动全频段高效协同，提高全谱系网络品质，
    探索跨行业基础设施能力共建。
  · 巩固 5G 优势、推进 6G 发展，拓展天地一体、通智一体、通感一体。
  · 服务侧：加快「全球通」服务焕新；推出 12580 智能助理，
    让 10 亿多手机客户、3 亿多家庭客户拥有随身智能助手；
    开放移动网络让开发者调用通信能力；汇聚内容资源。

风格：克制传媒风，白底、低饱和配色、标题即结论
输出目录 = 脚本所在目录
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

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

Q_L = "\u300c"   # 「
Q_R = "\u300d"   # 」


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
    fig = plt.figure(figsize=(12, 6.8))
    ax = new_axes(fig)

    header(fig, "三个跨越，把管道的边界重画了一遍",
           "要变的不是速度，是这张网被用来做什么")

    rows = [
        ("人人通信", "人机交互",
         "不再只服务人的通话与上网\n要接住设备、接住智能体的请求"),
        ("地面覆盖", "空天地海",
         "建强天启星座，增强近海、岛屿、边疆\n网络能力，做到无缝覆盖、永远在线"),
        ("尽力而为", "确定保障",
         "从能用就行，到可承诺的时延与可靠性\n铁路 5G 专网、超级上行成为必要项"),
    ]

    top = 0.690
    for i, (left, right, note) in enumerate(rows):
        y = top - i * 0.200

        card(ax, 0.045, y - 0.062, 0.150, 0.098, GRAY, face=PALE, lw=1.0)
        ax.text(0.120, y - 0.013, left, fontsize=12.4, color=SLATE,
                ha="center", va="center", zorder=6)

        ax.annotate("", xy=(0.245, y - 0.013), xytext=(0.208, y - 0.013),
                    arrowprops=dict(arrowstyle="-|>", color=RED,
                                    linewidth=1.6, shrinkA=0, shrinkB=0))

        card(ax, 0.255, y - 0.062, 0.162, 0.098, RED, lw=1.6)
        ax.text(0.336, y - 0.013, right, fontsize=12.4, color=RED,
                weight="bold", ha="center", va="center", zorder=6)

        ax.text(0.452, y + 0.030, note, fontsize=8.9, color=SLATE,
                ha="left", va="top", linespacing=1.62, zorder=6)

    ax.text(0.045, 0.152,
            "演讲原话：通信网不只是" + Q_L + "流量管道" + Q_R +
            "，更应成为" + Q_L + "数智底座" + Q_R + "。",
            fontsize=9.6, color=DARK, ha="left", va="center")

    punchline(fig, "口径一变，考核就从覆盖多广，变成接得住什么。")
    footer(fig, "事实来源：新华网 2026-11-06《中国移动董事长陈忠岳：网络强基 智能共创》；"
                "2026 移动网络大会（2026-11-05 至 07，广州）")
    fig.savefig(OUT + "图1_三个跨越.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "四个动作，补的是网络够不着的地方",
           "热点区域要更深，海岛边疆要更远，出境通道要更韧")

    cols = [
        ("地面", "更密更深", NAVY, [
            "提升热点区域深度覆盖",
            "建优铁路 5G 专网",
            "加快超级上行技术的",
            "创新、协作与现网部署",
        ]),
        ("天上", "无缝在线", RED, [
            "深化星地融合",
            "建强天启星座",
            "增强近海、岛屿、",
            "边疆的网络能力",
        ]),
        ("境外", "通达有韧", TEAL, [
            "完善国际网络布局",
            "畅通" + Q_L + "一带一路" + Q_R + "等",
            "重点方向的数字通道",
            "增强通达与网络韧性",
        ]),
        ("共建", "全频段协同", SLATE, [
            "推动全频段高效协同",
            "提高全谱系网络品质",
            "探索跨行业基础设施",
            "能力的共建共享",
        ]),
    ]

    x = 0.045
    w = 0.218
    gap = 0.017
    for name, tag, color, bullets in cols:
        card(ax, x, 0.290, w, 0.455, color, lw=1.4)
        ax.text(x + 0.019, 0.712, name, fontsize=13.2, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(x + 0.019, 0.678, tag, fontsize=9.2, color=GRAY,
                ha="left", va="center", zorder=6)
        ax.plot([x + 0.019, x + w - 0.019], [0.654, 0.654], color=color,
                linewidth=0.9, alpha=0.35, zorder=5)
        y = 0.612
        for b in bullets:
            ax.text(x + 0.019, y, b, fontsize=8.6, color=DARK,
                    ha="left", va="top", zorder=6)
            y -= 0.070
        x += w + gap

    ax.text(0.045, 0.215,
            "在这之上再展开网络边界：巩固 5G 优势、推进 6G 发展，"
            "拓展天地一体、通智一体、通感一体。",
            fontsize=9.4, color=SLATE, ha="left", va="center")

    punchline(fig, "所谓底座，不是形容词，是四个方向的工程量。")
    footer(fig, "事实来源：新华网 2026-11-06《中国移动董事长陈忠岳：网络强基 智能共创》")
    fig.savefig(OUT + "图2_四个动作.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(12, 6.8))
    ax = new_axes(fig)

    header(fig, "10 亿多手机客户，3 亿多家庭客户",
           "12580 智能助理要做的事，是把助理放进这几个入口里")

    stats = [
        ("10 亿多", "手机客户", NAVY, 0.075, 0.700),
        ("3 亿多", "家庭客户", RED, 0.075, 0.480),
    ]
    for num, label, color, cx, cy in stats:
        ax.text(cx, cy, num, fontsize=30, color=color, weight="bold",
                ha="left", va="center")
        ax.text(cx, cy - 0.064, label, fontsize=10.2, color=GRAY,
                ha="left", va="center")

    ax.plot([0.075, 0.440], [0.372, 0.372], color=LIGHT, linewidth=1.0)
    ax.text(0.075, 0.326,
            "这两个数不是用户规模指标，是" + Q_L + "助理" + Q_R +
            "\n这个产品能触达的物理边界。",
            fontsize=9.4, color=SLATE, ha="left", va="top", linespacing=1.70)

    ax.text(0.520, 0.760, "通信网能力升级之后，三件事跟着变", fontsize=10.0,
            color=GRAY, ha="left", va="center")
    ax.plot([0.520, 0.952], [0.732, 0.732], color=LIGHT, linewidth=1.0)

    items = [
        (Q_L + "全球通" + Q_R + "焕新",
         "服务品牌从办业务的地方\n变成智能服务的入口"),
        ("12580 智能助理",
         "让几亿客户拥有随身助手\n而不是再装一个独立 App"),
        ("开放移动网络",
         "让开发者便捷调用通信能力\n而不是重造一遍"),
    ]
    y = 0.676
    for name, desc in items:
        ax.text(0.520, y, name, fontsize=11.4, color=DARK, weight="bold",
                ha="left", va="center", zorder=6)
        ax.text(0.520, y - 0.054, desc, fontsize=9.0, color=SLATE,
                ha="left", va="top", linespacing=1.62, zorder=6)
        y -= 0.176

    ax.text(0.045, 0.176,
            "配套的一句：汇聚内容资源，让消费者顺畅享用网络服务。",
            fontsize=9.4, color=SLATE, ha="left", va="center")

    punchline(fig, "卖流量和卖用得上，差别在入口。")
    footer(fig, "事实来源：新华网 2026-11-06《中国移动董事长陈忠岳：网络强基 智能共创》")
    fig.savefig(OUT + "图3_一个助理.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)
