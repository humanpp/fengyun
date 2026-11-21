# -*- coding: utf-8 -*-
"""
《算力建设不只是「看投入」，更需要「比产出」：三个词的换算》配套图表

事实口径（核到新华网 2026-11-06 刊发的主旨演讲全文、
经济参考报 2026-11-06 关于算力投资的报道、活动征稿文案）：

一、演讲第二张网的总判断
  · 从 IDC 到 AIDC、从 CPU 到 GPU、从云资源池到 Token 工厂，
    算力建设不只是「看投入」，更需要「比产出」。
  · 算力是中国移动高质量发展的重要引擎。今年投资的最大增量在算力，
    在建成多个万卡智算集群的基础上，正在布局建设多个超大规模智算集群，
    未来两年智算能力将连续翻番，建成多个吉瓦级智算园区。

二、连算成网与调度
  · 推进连算成网：拓展 400G OTN 能力，全面贯通国家算力枢纽、各类算力资源，
    加大空芯光纤应用，加快 CDN 扩容升级，让入算连接更顺畅、算间互联更高效、
    边缘分发更敏捷。
  · 升级算网大脑：推动算力并网、一体调度，实现算力供需精准对接。

三、共创与协同
  · 推出 AIDC 全栈解决方案，共建定制化吉瓦级智算园区。
  · 加强卡间、机间互联技术创新，牵引算力产业发展。
  · 创新应用源网荷储、绿电直连、风液同源等技术，推动算电协同、算水协同。
  · 联建算力专网，支撑客户化 Token 工厂部署。
  · 升级「移动云」服务，建强算网一体、安全可信、敏捷高效的智算云，
    拓展更多政务云、工业云等行业标杆，支撑模型训推、算力定制、智能体构建，
    实现算力设施部署在云上、智能应用成长在云上。

四、投资口径（经济参考报 2026-11-06 报道）
  · 2027 年中国移动计划进一步提升采购总量，预计总金额 5000 亿元以上，
    算力投资 1000 亿元以上，终端采销 1000 亿元以上。
  · 双源核对：新华网同日刊发的演讲全文中亦载「2027 年，中国移动计划进一步
    提升采购总量，加大算力投资、确保智算能力倍增」。

风格：克制传媒风，白底、低饱和配色、标题即结论
输出目录 = 脚本所在目录
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

Q_L = "\u300c"
Q_R = "\u300d"


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
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "三个词换了，衡量方式就得跟着换",
           "IDC 到 AIDC、CPU 到 GPU、云资源池到 Token 工厂")

    rows = [
        ("IDC", "AIDC",
         "机房从存数据的仓库，变成产算力的车间\n电、水、散热、卡间互联都成了变量"),
        ("CPU", "GPU",
         "通用算力让位加速算力\n调度对象从进程变成卡与时延"),
        ("云资源池", "Token 工厂",
         "卖的不再是核·小时，是可计量的词元产能\n计价单位直接对应客户拿到的东西"),
    ]

    top = 0.690
    for i, (left, right, note) in enumerate(rows):
        y = top - i * 0.200

        card(ax, 0.045, y - 0.062, 0.168, 0.098, GRAY, face=PALE, lw=1.0)
        ax.text(0.129, y - 0.013, left, fontsize=12.0, color=SLATE,
                ha="center", va="center", zorder=6)

        ax.annotate("", xy=(0.262, y - 0.013), xytext=(0.226, y - 0.013),
                    arrowprops=dict(arrowstyle="-|>", color=RED,
                                    linewidth=1.6, shrinkA=0, shrinkB=0))

        card(ax, 0.272, y - 0.062, 0.176, 0.098, RED, lw=1.6)
        ax.text(0.360, y - 0.013, right, fontsize=12.0, color=RED,
                weight="bold", ha="center", va="center", zorder=6)

        ax.text(0.482, y + 0.028, note, fontsize=8.9, color=SLATE,
                ha="left", va="top", linespacing=1.62, zorder=6)

    ax.text(0.045, 0.152,
            "演讲原话：算力建设不只是" + Q_L + "看投入" + Q_R +
            "，更需要" + Q_L + "比产出" + Q_R + "。",
            fontsize=9.6, color=DARK, ha="left", va="center")

    punchline(fig, "计价单位一换，投入和产出就不再是同一件事。")
    footer(fig, "事实来源：新华网 2026-11-06《中国移动董事长陈忠岳：网络强基 智能共创》")
    fig.savefig(OUT + "图1_三个词.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "投入这一侧，已经有了具体数字",
           "2027 年算力投资 1000 亿元以上；未来两年智算能力连续翻番")

    # 左：三个投资口径
    ax.text(0.048, 0.786, "2027 年三个口径（计划）", fontsize=10.0, color=GRAY,
            ha="left", va="center")
    ax.plot([0.048, 0.512], [0.758, 0.758], color=LIGHT, linewidth=1.0)

    nums = [
        ("5000 亿元以上", "采购总量", NAVY),
        ("1000 亿元以上", "算力投资", RED),
        ("1000 亿元以上", "终端采销", SLATE),
    ]
    y = 0.700
    for num, label, color in nums:
        ax.text(0.048, y, num, fontsize=17.0, color=color, weight="bold",
                ha="left", va="center")
        ax.text(0.048, y - 0.046, label, fontsize=9.4, color=GRAY,
                ha="left", va="center")
        y -= 0.128

    # 右：能力规划
    ax.text(0.570, 0.786, "能力这一侧", fontsize=10.0, color=GRAY,
            ha="left", va="center")
    ax.plot([0.570, 0.952], [0.758, 0.758], color=LIGHT, linewidth=1.0)

    caps = [
        ("已建成", "多个万卡集群", NAVY, 0.45),
        ("正在布局", "超大规模集群", TEAL, 0.58),
        ("两年内", "智算能力翻番", RED, 0.66),
        ("同步推进", "吉瓦级园区", SLATE, 0.74),
    ]
    y = 0.694
    for tag, text, color, ratio in caps:
        ax.text(0.570, y + 0.024, tag, fontsize=8.4, color=GRAY,
                ha="left", va="center", zorder=6)
        ax.add_patch(Rectangle((0.570, y - 0.026), 0.340 * ratio, 0.026,
                               facecolor=color, edgecolor=color,
                               linewidth=0, alpha=0.85, zorder=4))
        y -= 0.100

    # 单列说明：放在右侧条形图下方的空白区（x 起点与条文对齐，右界 0.952）
    ax.text(0.570, 0.300,
            "已建成：多个万卡智算集群\n"
            "正在布局：多个超大规模智算集群\n"
            "两年内：智算能力连续翻番\n"
            "同步推进：建成多个吉瓦级智算园区",
            fontsize=8.8, color=DARK, ha="left", va="top",
            linespacing=1.90, zorder=6)

    ax.text(0.048, 0.300,
            "演讲原话：今年中国移动投资的最大增量在算力。",
            fontsize=9.4, color=SLATE, ha="left", va="top")
    ax.text(0.048, 0.256,
            "紧接着一句：算力建设不只是看投入，更需要比产出。",
            fontsize=9.4, color=DARK, ha="left", va="top")

    card(ax, 0.048, 0.130, 0.478, 0.072, LIGHT, face=PALE, lw=1.0)
    ax.text(0.070, 0.166,
            "考题不在左边的钱，在右边被用掉了多少。",
            fontsize=9.4, color=DARK, ha="left", va="center", zorder=6)

    punchline(fig, "投进去的是钱，交出来的是词元。")
    footer(fig, "事实来源：新华网 2026-11-06 演讲全文；经济参考报 2026-11-06"
                "《中国移动：2027年计划算力投资超1000亿元》")
    fig.savefig(OUT + "图2_两头.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(12, 7.1))
    ax = new_axes(fig)

    header(fig, "从卡到词元，中间隔着四道工序",
           "这四道工序，就是" + Q_L + "比产出" + Q_R + "实际要比的地方")

    layers = [
        ("算力", "卡与集群", "万卡集群、超大规模集群、\n卡间与机间互联技术创新", NAVY),
        ("连接", "连算成网", "400G OTN 贯通国家算力枢纽，\n空芯光纤、CDN 扩容升级", TEAL),
        ("调度", "算网大脑", "算力并网、一体调度，\n供需精准对接", SLATE),
        ("交付", "Token 工厂", "算力专网支撑客户化部署，\n移动云承载训推与智能体", RED),
    ]

    x = 0.045
    w = 0.218
    gap = 0.017
    for i, (name, tag, detail, color) in enumerate(layers):
        card(ax, x, 0.450, w, 0.310, color, lw=1.4)
        ax.text(x + 0.019, 0.716, name, fontsize=14.0, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(x + 0.019, 0.680, tag, fontsize=9.6, color=DARK,
                ha="left", va="center", zorder=6)
        ax.plot([x + 0.019, x + w - 0.019], [0.658, 0.658], color=color,
                linewidth=0.9, alpha=0.35, zorder=5)
        ax.text(x + 0.019, 0.628, detail, fontsize=8.4, color=SLATE,
                ha="left", va="top", linespacing=1.70, zorder=6)

        if i < 3:
            ax.annotate("", xy=(x + w + gap - 0.002, 0.605),
                        xytext=(x + w + 0.002, 0.605),
                        arrowprops=dict(arrowstyle="-|>", color=GRAY,
                                        linewidth=1.4, shrinkA=0, shrinkB=0))
        x += w + gap

    # 底部三个协同项
    ax.text(0.045, 0.372, "贯穿其中的三项协同", fontsize=10.0, color=GRAY,
            ha="left", va="center")
    ax.plot([0.045, 0.952], [0.350, 0.350], color=LIGHT, linewidth=1.0)

    items = [
        ("算电协同", "源网荷储、绿电直连"),
        ("算水协同", "风液同源，降散热成本"),
        ("产业共创", "AIDC 全栈方案、共建吉瓦级园区"),
    ]
    x = 0.045
    for name, detail in items:
        ax.text(x, 0.300, name, fontsize=11.0, color=DARK, weight="bold",
                ha="left", va="center", zorder=6)
        ax.text(x, 0.256, detail, fontsize=8.6, color=SLATE,
                ha="left", va="center", zorder=6)
        x += 0.305

    punchline(fig, "卡只是原料；能不能出词元，看后面三道。")
    footer(fig, "事实来源：新华网 2026-11-06《中国移动董事长陈忠岳：网络强基 智能共创》")
    fig.savefig(OUT + "图3_四道工序.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)
