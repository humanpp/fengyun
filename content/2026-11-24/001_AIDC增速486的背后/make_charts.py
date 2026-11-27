# -*- coding: utf-8 -*-
"""
《AIDC 收入涨 486%，算力服务只涨 14%：一条增速差说明的事》配套图表

事实口径（2026 年中期业绩，2026-08-13 发布，新华网/上海证券报/经济参考报）：
  · 营运收入 5380 亿元，同比下降 1.1%；主营业务收入 4527 亿元，同比下降 3.1%；
    其他业务收入 854 亿元，同比增长 11.2%；股东应占利润 789 亿元，同比下降 6.3%。
    剔除增值税税目政策调整影响后，同口径均实现正增长。
  · 算力服务收入 529 亿元，同比增长 14.0%。
    其中数据中心收入 190 亿元，同比增长 13.2%；AIDC 收入同比增长 486.1%；
    智算服务收入 53 亿元，增速 130.1%，贡献算力服务收入增量的 46.1%；
    云算应用收入同比增长 5.9%，移动云盘收入同比增长 14.1%。
    移动云公有云收入规模首次进入国内业界前三。
  · 算力基础设施：「4+N+31+X」体系；智算总规模 11.27 万 PFLOPS；
    在网资源使用率超 90%；算间平均时延降至 12 毫秒以下，同比降低 5.5%；
    面向智算卡间互联发布 OISA（全向智感互联）商用 IP 核。

风格：克制传媒风，编辑排版，白底 + 语义色
输出目录 = 脚本所在目录
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["figure.facecolor"] = "white"
plt.rcParams["savefig.facecolor"] = "white"

INK = "#1a2332"
NAVY = "#1b3a5c"
RED = "#b0413e"
TEAL = "#2f6b64"
GOLD = "#9a7b3f"
MUTED = "#7b8494"
HAIR = "#dfe3e8"
WASH = "#f4f6f8"
WHITE = "#ffffff"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep
Q_L, Q_R = "\u300c", "\u300d"


def new_axes(fig):
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return ax


def head(fig, ax, kicker, title, sub, color):
    ax.add_patch(Rectangle((0.042, 0.928), 0.0075, 0.040,
                           facecolor=color, edgecolor="none", zorder=9))
    ax.text(0.058, 0.950, kicker, fontsize=9.2, color=color,
            weight="bold", ha="left", va="center", zorder=9)
    ax.text(0.042, 0.900, title, fontsize=21, color=INK, weight="bold",
            ha="left", va="top", zorder=9)
    ax.text(0.042, 0.848, sub, fontsize=10.4, color=MUTED,
            ha="left", va="top", zorder=9)
    ax.plot([0.042, 0.958], [0.812, 0.812], color=HAIR, linewidth=1.0,
            zorder=5)


def foot(fig, ax, text):
    ax.plot([0.042, 0.958], [0.058, 0.058], color=HAIR, linewidth=0.9,
            zorder=5)
    ax.text(0.042, 0.028, text, fontsize=7.0, color=MUTED,
            ha="left", va="center", zorder=9)


def outro(fig, ax, text, color=INK):
    ax.add_patch(FancyBboxPatch(
        (0.042, 0.082), 0.720, 0.048,
        boxstyle="round,pad=0.002,rounding_size=0.008",
        facecolor=color, edgecolor="none", zorder=6))
    ax.text(0.062, 0.106, text, fontsize=10.2, color=WHITE,
            ha="left", va="center", zorder=9)


def panel(ax, x, y, w, h, accent, face=WHITE, bar=0.0055, shadow=True):
    if shadow:
        ax.add_patch(FancyBboxPatch(
            (x + 0.0035, y - 0.0035), w, h,
            boxstyle="round,pad=0,rounding_size=0.009",
            facecolor="#e9ecf0", edgecolor="none", zorder=2))
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0,rounding_size=0.009",
        facecolor=face, edgecolor="#e6eaee", linewidth=0.9, zorder=3))
    ax.add_patch(FancyBboxPatch(
        (x, y), bar, h,
        boxstyle="round,pad=0,rounding_size=0.0028",
        facecolor=accent, edgecolor="none", zorder=4))


# ---------------------------------------------------------------- 图 1
def fig1():
    fig = plt.figure(figsize=(13.6, 8.0))
    ax = new_axes(fig)

    head(fig, ax, "一条增速差",
         "AIDC 涨 486%，算力服务只涨 14%",
         "同一块业务里，四个层级的增速差了近 90 倍",
         RED)

    # 四条增速条
    ax.text(0.042, 0.762, "2026 年上半年同比增速", fontsize=8.6, color=MUTED,
            ha="left", va="center")
    ax.plot([0.042, 0.958], [0.742, 0.742], color=HAIR, linewidth=1.0)

    bars = [
        ("AIDC 收入", 486.1, RED, "AI 数据中心"),
        ("智算服务收入", 130.1, GOLD, "53 亿元"),
        ("数据中心收入", 13.2, NAVY, "190 亿元"),
        ("算力服务整体", 14.0, TEAL, "529 亿元"),
    ]

    # 对数式刻度，让 486% 和 13% 能同屏
    import math
    base_x = 0.285
    span = 0.280

    def w(v):
        return span * (math.log10(v + 10) - 1.0) / (math.log10(496) - 1.0)

    y = 0.680
    for name, val, color, note in bars:
        ax.text(0.042, y + 0.008, name, fontsize=10.6, color=INK,
                weight="bold", ha="left", va="center", zorder=9)
        ax.text(0.042, y - 0.026, note, fontsize=7.8, color=MUTED,
                ha="left", va="center", zorder=9)

        bw = w(val)
        ax.add_patch(FancyBboxPatch(
            (base_x, y - 0.020), bw, 0.034,
            boxstyle="round,pad=0,rounding_size=0.008",
            facecolor=color, edgecolor="none", zorder=6))
        ax.text(base_x + bw + 0.012, y - 0.003, f"+{val:.1f}%",
                fontsize=12.0, color=color, weight="bold",
                ha="left", va="center", zorder=9)
        y -= 0.108

    ax.plot([base_x, base_x], [0.290, 0.700], color=HAIR, linewidth=1.0,
            zorder=4)
    ax.text(0.042, 0.272,
            "注：为让 486% 与 13% 同屏可比，条形长度按对数刻度绘制，非等比例。",
            fontsize=7.6, color=MUTED, ha="left", va="center", zorder=9)

    # 右侧解读
    panel(ax, 0.688, 0.278, 0.270, 0.424, RED, face=WASH)
    ax.text(0.706, 0.664, "这个差额在说什么", fontsize=9.0, color=MUTED,
            ha="left", va="center", zorder=9)
    ax.text(0.706, 0.624,
            "AIDC 是从很低的\n基数上长出来的，\n"
            "所以增速可以很大。\n\n"
            "但体量还小，\n"
            "拉不动整体。",
            fontsize=8.4, color=INK, ha="left", va="top",
            linespacing=1.75, zorder=9)
    ax.text(0.706, 0.406,
            "真正的增量在\n智算服务：\n贡献 46.1% 的增量。",
            fontsize=8.4, color=RED, weight="bold", ha="left",
            va="top", linespacing=1.75, zorder=9)

    outro(fig, ax, "增速最高的那块，未必是贡献最大的那块。")
    foot(fig, ax, "事实来源：中国移动 2026 年中期业绩（2026-08-13）"
         "；新华网 2026-08-13、上海证券报 2026-08-14")

    fig.savefig(OUT + "图1_增速差.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(13.6, 8.0))
    ax = new_axes(fig)

    head(fig, ax, "增量归属",
         "529 亿元里，哪一块真正在拉动增长",
         "算力服务同比增 14%，增量约 65 亿元——其中近一半来自智算服务",
         NAVY)

    # 左：收入结构（按 529 亿总额等比）
    ax.text(0.042, 0.758, "算力服务收入构成（2026H1，合计 529 亿元）", fontsize=8.6,
            color=MUTED, ha="left", va="center")
    ax.plot([0.042, 0.470], [0.738, 0.738], color=HAIR, linewidth=1.0)

    segs = [
        ("数据中心", 190, NAVY, "同比 +13.2%"),
        ("智算服务", 53, GOLD, "同比 +130.1%"),
        ("其余部分", 286, MUTED, "云算服务、云算应用等"),
    ]
    y = 0.672
    for name, val, color, note in segs:
        ax.text(0.042, y + 0.016, name, fontsize=10.4, color=INK,
                weight="bold", ha="left", va="center", zorder=9)
        ax.text(0.042, y - 0.022, f"{val} 亿元 · {note}", fontsize=8.2,
                color=MUTED, ha="left", va="center", zorder=9)
        bw = 0.428 * (val / 529.0)
        ax.add_patch(FancyBboxPatch(
            (0.042, y - 0.056), bw, 0.026,
            boxstyle="round,pad=0,rounding_size=0.007",
            facecolor=color, edgecolor="none", zorder=6))
        y -= 0.132

    ax.text(0.042, 0.268,
            "注：三类相加为 529 亿元，与算力服务收入总额一致。",
            fontsize=7.8, color=MUTED, ha="left", va="center", zorder=9)

    # 右：增量结构（堆叠条）
    ax.text(0.520, 0.758, "收入增量归属（约 65 亿元）", fontsize=8.6,
            color=MUTED, ha="left", va="center")
    ax.plot([0.520, 0.958], [0.738, 0.738], color=HAIR, linewidth=1.0)

    total_w = 0.438
    part = total_w * 0.461

    ax.add_patch(FancyBboxPatch(
        (0.520, 0.620), part, 0.062,
        boxstyle="round,pad=0,rounding_size=0.008",
        facecolor=GOLD, edgecolor="none", zorder=6))
    ax.add_patch(FancyBboxPatch(
        (0.520 + part, 0.620), total_w - part, 0.062,
        boxstyle="round,pad=0,rounding_size=0.008",
        facecolor="#c9d0d8", edgecolor="none", zorder=6))

    ax.text(0.520 + part / 2, 0.706, "46.1%", fontsize=16.0, color=GOLD,
            weight="bold", ha="center", va="bottom", zorder=9)
    ax.text(0.520 + part / 2, 0.684, "智算服务", fontsize=8.4, color=INK,
            ha="center", va="bottom", zorder=9)
    ax.text(0.520 + part + (total_w - part) / 2, 0.706, "53.9%", fontsize=16.0,
            color=MUTED, weight="bold", ha="center", va="bottom", zorder=9)
    ax.text(0.520 + part + (total_w - part) / 2, 0.684, "其他", fontsize=8.4,
            color=INK, ha="center", va="bottom", zorder=9)

    ax.text(0.520, 0.586,
            "智算服务只占收入约一成，却贡献了近半增量。",
            fontsize=9.0, color=INK, ha="left", va="center", zorder=9)

    # 右下：三个基础指标
    ax.text(0.520, 0.480, "支撑这半壁增量的底座", fontsize=8.6, color=MUTED,
            ha="left", va="center")

    stats = [
        ("11.27 万 PFLOPS", "智算总规模"),
        ("超 90%", "在网资源使用率"),
        ("12 毫秒以下", "算间平均时延，同比降 5.5%"),
    ]
    y = 0.428
    for num, label in stats:
        ax.text(0.520, y, num, fontsize=13.2, color=NAVY, weight="bold",
                ha="left", va="center", zorder=9)
        ax.text(0.520, y - 0.034, label, fontsize=8.0, color=MUTED,
                ha="left", va="center", zorder=9)
        y -= 0.082

    outro(fig, ax, "看算力业务，别只看增速，要看增量落在哪一层。")
    foot(fig, ax, "事实来源：中国移动 2026 年中期业绩；上海证券报 2026-08-14 半年度报告摘要"
         "（算力服务含数据中心、云算服务、云算应用）")

    fig.savefig(OUT + "图2_增量归属.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(13.6, 8.0))
    ax = new_axes(fig)

    head(fig, ax, "从 IDC 到 AIDC",
         "同一台机架，卖的东西换了三次",
         "IDC、AIDC、智算服务——物理载体没变，计价对象在往上走",
         TEAL)

    stages = [
        ("IDC", "卖机位", "按机架、按电、按带宽计费",
         ["客户自己带服务器", "运营商提供空间与电力", "收入随上架率线性增长"], MUTED),
        ("AIDC", "卖算力", "按卡时、按集群计费",
         ["运营商自建 GPU 集群", "客户租用训练/推理能力", "需要算电协同与高阶运维"], NAVY),
        ("智算服务", "卖结果", "按任务、按 Token 计费",
         ["客户提出任务，不必懂硬件", "按调用量与效果付费", "拉动力最强，但最难做"], GOLD),
    ]

    x = 0.042
    w = 0.288
    gap = 0.019
    for i, (name, tag, price, points, color) in enumerate(stages):
        panel(ax, x, 0.230, w, 0.510, color)

        ax.text(x + 0.026, 0.700, name, fontsize=16.0, color=color,
                weight="bold", ha="left", va="center", zorder=9)
        ax.text(x + 0.026, 0.662, tag, fontsize=10.0, color=INK,
                weight="bold", ha="left", va="center", zorder=9)
        ax.text(x + 0.026, 0.622, price, fontsize=8.2, color=MUTED,
                ha="left", va="center", zorder=9)
        ax.plot([x + 0.026, x + w - 0.026], [0.598, 0.598], color=HAIR,
                linewidth=1.0, zorder=5)

        yy = 0.556
        for p in points:
            ax.add_patch(Circle((x + 0.034, yy), 0.0038, facecolor=color,
                                edgecolor="none", zorder=8))
            ax.text(x + 0.048, yy, p, fontsize=8.0, color=INK,
                    ha="left", va="center", zorder=9)
            yy -= 0.062

        if i < 2:
            ax.annotate("", xy=(x + w + gap - 0.001, 0.486),
                        xytext=(x + w + 0.001, 0.486),
                        arrowprops=dict(arrowstyle="-|>", color="#c9d0d8",
                                        linewidth=1.8, shrinkA=0, shrinkB=0))
        x += w + gap

    ax.add_patch(FancyBboxPatch(
        (0.042, 0.140), 0.916, 0.070,
        boxstyle="round,pad=0,rounding_size=0.008",
        facecolor=WASH, edgecolor="none", zorder=3))
    ax.text(0.062, 0.176,
            "往右走一步，运营商承担的环节多一步，收入的天花板也高一层；但能力门槛同步抬高。",
            fontsize=8.6, color=INK, ha="left", va="center", zorder=9)

    outro(fig, ax, "AIDC 的意义不在增速，在于计价对象从「机位」变成了「算力」。")
    foot(fig, ax, "事实来源：中国移动 2026 年中期业绩；算力服务口径含数据中心、"
         "云算服务、云算应用（上海证券报 2026-08-14）")

    fig.savefig(OUT + "图3_三层计价.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)
