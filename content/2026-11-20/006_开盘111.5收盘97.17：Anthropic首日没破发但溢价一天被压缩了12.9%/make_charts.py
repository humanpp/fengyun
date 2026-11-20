# -*- coding: utf-8 -*-
"""
《开盘 111.5 美元、收盘 97.17 美元：Anthropic 首日没破发，但溢价一天被压缩了 12.9%》配套图表
事实口径（全部经公开报道交叉核对）：
  · 发行价 83.00 美元，发行 9.8 亿股，募资约 813.4 亿美元 —— Anthropic 官方定价公告 2026-11-18；
  · 开盘价 111.50 美元（+34.3%），首笔成交约美东 11:50，此前指示性开盘价数次上调 —— 日经中文网、虎嗅；
  · 盘中最高 115.10 美元（+38.7%），最低 92.72 美元（+11.7%）—— 信报、Unite.AI 引纳斯达克市场记录；
  · 收盘 97.17 美元（+17.07%），较开盘价回落 12.85% —— 纳斯达克行情，澎湃、第一财经、CNBC；
  · 成交量 8.396 亿股（CNBC），Wind 口径 8.46 亿股 —— 澎湃、每经；
  · 开盘前链上合约：币安 98.80、OKX 98.91、Bitget 98.87、Hyperliquid TradeXYZ 98.57 美元
    （北京时间 2026-11-19 09:16）—— AiCoin；
  · 散户配售：英国 3,614,976 股约 3.0 亿美元、欧洲大陆近 970 万股约 8.01 亿美元，
    合计约 11 亿美元、占本次发行约 1.35%；英国认购订单近 10 亿美元约 3 倍，
    63% 英国认购者获全额，Hargreaves Lansdown 客户获配 33.6% —— Retail Book 最终结果、界面新闻、凤凰网。
说明：图 1 只连接已知点位，不是分时走势；素材原称"回落 12.8%"，按 97.17/111.50 计算为 -12.85%，图与文统一取 12.9%。
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
    fig = base("一天之内，四个价格",
               "2026 年 11 月 19 日 ANT 首日：83 → 98.5 → 111.5 → 97.17（美元）")
    ax = canvas(fig)

    # 价格 -> 画布坐标（80—120 美元映射到 0.115—0.800）
    def y_of(p):
        return 0.115 + (p - 80.0) / 40.0 * 0.685

    # 网格与刻度
    for p in (80, 90, 100, 110, 120):
        y = y_of(p)
        ax.plot([0.075, 0.955], [y, y], color="#eceef1", linewidth=0.9, zorder=1)
        ax.text(0.062, y, str(p), fontsize=8.6, color=GRAY, ha="right",
                va="center")
    ax.text(0.078, y_of(120) + 0.030, "美元", fontsize=8.4, color=GRAY,
            ha="left", va="bottom")

    # 发行价参考线
    ax.plot([0.075, 0.955], [y_of(83), y_of(83)], color=RED, linewidth=1.2,
            linestyle=(0, (6, 4)), zorder=2)
    ax.text(0.950, y_of(83) + 0.030, "发行价 83.00", fontsize=9.6, color=RED,
            weight="bold", ha="right", va="bottom")

    # 收盘参考线
    ax.plot([0.075, 0.955], [y_of(97.17), y_of(97.17)], color=NAVY,
            linewidth=1.0, linestyle=(0, (2, 3)), zorder=2, alpha=0.75)

    # 场外到开盘：虚线（不同市场，不是同一段行情）
    ax.plot([0.128, 0.330], [y_of(98.50), y_of(111.50)], color=GOLD,
            linewidth=1.6, linestyle=(0, (4, 3)), zorder=3)
    ax.annotate("", xy=(0.330, y_of(111.50) - 0.006),
                xytext=(0.128, y_of(98.50) + 0.006),
                arrowprops=dict(arrowstyle="-|>", color=GOLD, linewidth=1.4,
                                shrinkA=4, shrinkB=6), zorder=3)
    ax.text(0.196, (y_of(98.50) + y_of(111.50)) / 2 + 0.042, "跳空",
            fontsize=9.4, color=GOLD, weight="bold", ha="center", va="bottom")

    # 开盘之后的日内路径
    xs = [0.330, 0.515, 0.690, 0.885]
    ys = [y_of(111.50), y_of(115.10), y_of(92.72), y_of(97.17)]
    ax.plot(xs, ys, color=NAVY, linewidth=2.4, solid_capstyle="round", zorder=4)

    # 盘前合约：空心点 + 左下角引线标注
    yp = y_of(98.50)
    ax.add_patch(Circle((0.128, yp), 0.011, facecolor="white", edgecolor=GOLD,
                        linewidth=2.0, zorder=6))
    ax.annotate("盘前链上合约　98.57—98.91\n（北京时间 11-19 09:16，链上永续报价）",
                xy=(0.126, yp - 0.010), xytext=(0.098, 0.250),
                fontsize=9.4, color=GOLD, ha="left", va="center",
                linespacing=1.7,
                arrowprops=dict(arrowstyle="-", color=GOLD, linewidth=1.0,
                                connectionstyle="arc3,rad=-0.15"))

    # 开盘价
    y = y_of(111.50)
    ax.add_patch(Circle((0.330, y), 0.011, facecolor=NAVY, edgecolor=NAVY,
                        linewidth=2.0, zorder=6))
    ax.text(0.352, y - 0.032, "开盘（首笔成交约 11:50）", fontsize=9.4,
            color=DARK, ha="left", va="top")
    ax.text(0.352, y - 0.068, "111.50　+34.3%", fontsize=10.4, color=NAVY,
            weight="bold", ha="left", va="top")

    # 盘中最高
    y = y_of(115.10)
    ax.add_patch(Circle((0.515, y), 0.011, facecolor=NAVY, edgecolor=NAVY,
                        linewidth=2.0, zorder=6))
    ax.text(0.515, y + 0.032, "盘中最高", fontsize=9.4, color=DARK,
            ha="center", va="bottom")
    ax.text(0.515, y + 0.066, "115.10　+38.7%", fontsize=10.4, color=NAVY,
            weight="bold", ha="center", va="bottom")

    # 盘中最低
    y = y_of(92.72)
    ax.add_patch(Circle((0.690, y), 0.011, facecolor=SLATE, edgecolor=SLATE,
                        linewidth=2.0, zorder=6))
    ax.text(0.690, y - 0.032, "盘中最低", fontsize=9.4, color=DARK,
            ha="center", va="top")
    ax.text(0.690, y - 0.066, "92.72　+11.7%", fontsize=10.4, color=SLATE,
            weight="bold", ha="center", va="top")

    # 收盘
    y = y_of(97.17)
    ax.add_patch(Circle((0.885, y), 0.011, facecolor=RED, edgecolor=RED,
                        linewidth=2.0, zorder=6))
    ax.text(0.885, y - 0.032, "收盘", fontsize=9.4, color=DARK,
            ha="center", va="top")
    ax.text(0.885, y - 0.066, "97.17　+17.07%", fontsize=10.4, color=RED,
            weight="bold", ha="center", va="top")

    # 开盘到收盘的回落标注
    ax.annotate("", xy=(0.930, y_of(97.17)), xytext=(0.930, y_of(111.50)),
                arrowprops=dict(arrowstyle="<->", color=RED, linewidth=1.4))
    ax.text(0.918, (y_of(97.17) + y_of(111.50)) / 2, "−12.9%", fontsize=12.0,
            color=RED, weight="bold", ha="right", va="center")

    punchline(fig, "首日没有破发，但开盘那 34% 只活了几个小时。")
    footer(fig, "注：仅连接已知点位，非分时走势；盘前为链上永续合约报价，与纳斯达克不同市场｜制图：本文")
    fig.savefig(OUT + "图1_一天四个价格.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("溢价被压缩的 12.9%",
               "同一天里，四个价格各自离发行价多远")
    ax = canvas(fig)

    rows = [
        ("收盘价", 97.17, "+17.07%", RED, 0.0),
        ("开盘价", 111.50, "+34.3%", NAVY, 1.0),
        ("盘前链上合约", 98.50, "+18.7%", GOLD, 2.0),
        ("发行价", 83.00, "基准", SLATE, 3.0),
    ]

    x_left = 0.250
    x_scale = 0.545 / 120.0  # 0—120 美元映射到条长

    for label, price, note, col, i in rows:
        y = 0.805 - i * 0.140
        ax.text(x_left - 0.018, y, label, fontsize=10.6, color=DARK,
                ha="right", va="center")
        w = price * x_scale
        ax.add_patch(FancyBboxPatch((x_left, y - 0.028), w, 0.056,
                                    boxstyle="round,pad=0.002",
                                    facecolor=col, edgecolor="none",
                                    alpha=0.90, zorder=3))
        ax.text(x_left + w + 0.014, y, f"{price:,.2f}", fontsize=11.4,
                color=col, weight="bold", ha="left", va="center")
        ax.text(x_left + w + 0.100, y, note, fontsize=9.4, color=GRAY,
                ha="left", va="center")

    # 发行价基准竖线
    xb = x_left + 83.0 * x_scale
    ax.plot([xb, xb], [0.330, 0.850], color=SLATE, linewidth=1.0,
            linestyle=(0, (4, 3)), zorder=2)

    # 开盘 -> 收盘 回落
    ax.annotate("", xy=(0.930, 0.805), xytext=(0.930, 0.665),
                arrowprops=dict(arrowstyle="<->", color=RED, linewidth=1.6))
    ax.text(0.930, 0.845, "−12.9%", fontsize=12.6, color=RED, weight="bold",
            ha="center", va="bottom")

    # 底部说明
    ax.add_patch(FancyBboxPatch((0.070, 0.160), 0.860, 0.115,
                                boxstyle="round,pad=0.010", facecolor=SAND,
                                edgecolor="#d9cdb6", linewidth=1.0))
    ax.text(0.092, 0.233, "三个锚，一天里收成一个", fontsize=10.2,
            color="#8a7a5e", weight="bold", ha="left", va="center")
    ax.text(0.092, 0.187,
            "一级市场定 83，场外影子价喊到 98.5，二级市场开盘给 111.5 —— 收盘 97.17，落回最保守的那个附近。",
            fontsize=9.6, color="#7a6746", ha="left", va="center")

    punchline(fig, "定价是锚，暗盘是影子，开盘是情绪。一天之后，市场只认最低的那个。")
    footer(fig, "事实：发行价与募资据 Anthropic 定价公告 2026-11-18；其余据纳斯达克行情与公开报道；盘前 98.50 为 98.57—98.91 三家报价的取整示意｜制图：本文")
    fig.savefig(OUT + "图2_溢价压缩.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("首日谁手里有货",
               "英欧散户拿到约 11 亿美元，占本次发行 1.35%")
    ax = canvas(fig)

    # 左：两地配售
    ax.add_patch(FancyBboxPatch((0.060, 0.215), 0.420, 0.500,
                                boxstyle="round,pad=0.012", facecolor="#eef2f6",
                                edgecolor=NAVY, linewidth=1.2))
    ax.text(0.085, 0.668, "散户配售（按 83 美元发行价）", fontsize=11.4,
            color=NAVY, weight="bold", ha="left", va="center")

    blocks = [
        ("英国", "3,614,976 股", "约 3.00 亿美元", 0.588),
        ("欧洲大陆（欧盟＋挪威＋瑞士）", "近 970 万股", "约 8.01 亿美元", 0.418),
    ]
    for name, shares, money, yy in blocks:
        ax.text(0.085, yy, name, fontsize=10.2, color=DARK, weight="bold",
                ha="left", va="center")
        ax.text(0.085, yy - 0.052, shares, fontsize=13.4, color=NAVY,
                weight="bold", ha="left", va="center")
        ax.text(0.085, yy - 0.100, money, fontsize=10.0, color=SLATE,
                ha="left", va="center")

    ax.plot([0.085, 0.455], [0.278, 0.278], color=LIGHT, linewidth=1.0)
    ax.text(0.085, 0.238, "合计约 11 亿美元　≈　本次 IPO 的 1.35%",
            fontsize=10.0, color=RED, weight="bold", ha="left", va="center")

    # 右：认购与获配
    ax.text(0.530, 0.668, "英国散户这一端发生了什么", fontsize=11.4,
            color=DARK, weight="bold", ha="left", va="center")

    cards = [
        ("3 倍", "认购订单近 10 亿美元\n约为可配售金额的三倍", GOLD, 0.625),
        ("63%", "英国认购者拿到\n申请的全部份额", GREEN, 0.470),
        ("33.6%", "Hargreaves Lansdown 的\n45,811 名客户平均获配率", RED, 0.315),
    ]
    for big, desc, col, top in cards:
        ax.add_patch(FancyBboxPatch((0.530, top - 0.130), 0.400, 0.130,
                                    boxstyle="round,pad=0.010",
                                    facecolor="#fafbfc", edgecolor=col,
                                    linewidth=1.1))
        ax.text(0.552, top - 0.065, big, fontsize=16.4, color=col,
                weight="bold", ha="left", va="center")
        ax.text(0.700, top - 0.065, desc, fontsize=9.2, color=SLATE,
                ha="left", va="center", linespacing=1.7)

    ax.text(0.530, 0.140, "散户没有锁定期，也没有减仓要走的风控流程。",
            fontsize=9.8, color=DARK, weight="bold", ha="left", va="center")

    punchline(fig, "手里有货、又能当天决定的人变多，开盘价就更容易只是一天的价格。")
    footer(fig, "事实：配售股数与金额据 Retail Book 最终结果、界面新闻、凤凰网 2026-11-19；获配比例据 Hargreaves Lansdown｜制图：本文")
    fig.savefig(OUT + "图3_谁手里有货.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)
