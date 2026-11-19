# -*- coding: utf-8 -*-
"""
《想蹭一杯免费奶茶，一小时后背了 1.4 万网贷》配套图表
事实口径（2026-11-18 广州黎女士向媒体讲述）：
  · 黎女士在社交平台刷到“订婚请喝奶茶”的帖子，想蹭一杯；
  · 进小程序后客服让她先买 328 元电商平台代金券，称好评后可领
    68 元奶茶钱并全额退款；
  · 扫码后付款页面跳转到另一个平台，扣款方显示为
    “广州网易计算机系统有限公司”，商品说明为“6000 金块”；
  · 她回头查不到订单；客服诱导她添加“退款专员”，在视频监控下
    查看多个账户余额，以“刷流水才能退款”为由让她下载游戏 App 充值；
  · 不到一小时工资见底，背上 1 万多元网贷和信用卡账单，
    总损失超 1.4 万元；
  · 涉事公司成立不足一个月，小程序已被关停；
  · 记者调查：受害者多为大学生等年轻群体，有人被骗走几个月生活费。
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
SAND = "#f7f3ea"
GREEN = "#4f6b58"

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


# ------------------------------------------------------------------ 图 1
def fig1():
    fig = base("一杯奶茶，六步变成 1.4 万网贷",
               "广州黎女士的账单：从 328 元代金券，到 1 万多元网贷")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    steps = [
        ("① 刷到帖子", "“我订婚了，请大家喝奶茶。”她想蹭一杯，沾沾喜气。"),
        ("② 买一张券", "客服：先买 328 元代金券，好评后可领 68 元奶茶钱，全额退款。"),
        ("③ 扫码付款", "页面跳到另一个平台；扣款方“广州网易计算机系统有限公司”，商品“6000 金块”。"),
        ("④ 回头查单", "订单查不到。钱扣了，订单没了。"),
        ("⑤ 加“退款专员”", "对方在视频里看着她，逐个查看她多个账户的余额。"),
        ("⑥ 刷流水充值", "下载游戏 App 充值；工资花完，又开通网贷和信用卡继续充。"),
    ]

    yy = 0.875
    for tag, body in steps:
        ax.text(0.030, yy, tag, fontsize=10.2, color=RED, weight="bold",
                ha="left", va="center")
        ax.text(0.030, yy - 0.052, body, fontsize=8.8, color=SLATE,
                ha="left", va="center")
        ax.plot([0.030, 0.960], [yy - 0.098, yy - 0.098], color=LIGHT,
                linewidth=0.8)
        yy -= 0.128

    punchline(fig, "每一步都像“再试一下就能退回来”。")
    footer(fig, "事实：据 2026-11-18 广州黎女士向媒体讲述｜制图：本文")
    fig.savefig(OUT + "图1_一杯奶茶的六步.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("帖子写的是奶茶，账单写的是“金块”",
               "黎女士的付款页面，跳到了另一个平台")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # 左：她以为
    ax.add_patch(FancyBboxPatch((0.018, 0.160), 0.450, 0.740,
                                boxstyle="round,pad=0.012",
                                facecolor=SAND, edgecolor="#d9cdb6",
                                linewidth=1.0))
    ax.text(0.044, 0.830, "她以为：一杯奶茶", fontsize=10.6, color="#7a6746",
            weight="bold", ha="left", va="center")
    ax.plot([0.044, 0.442], [0.790, 0.790], color="#d9cdb6", linewidth=1.0)
    ax.text(0.044, 0.650, "“我订婚了，\n请大家喝奶茶。”", fontsize=17.0,
            color=DARK, weight="bold", ha="left", va="center",
            linespacing=1.6)
    ax.text(0.044, 0.420,
            "客服：先买 328 元代金券，\n好评后可领 68 元奶茶钱，\n并全额退款。",
            fontsize=9.2, color=SLATE, ha="left", va="center", linespacing=1.9)
    ax.text(0.044, 0.220, "一杯奶茶的门槛，低到不值得多想。",
            fontsize=8.8, color="#8a7a5e", ha="left", va="center")

    # 右：账单显示
    ax.add_patch(FancyBboxPatch((0.532, 0.160), 0.450, 0.740,
                                boxstyle="round,pad=0.012",
                                facecolor="#fbf3f1", edgecolor=LIGHT,
                                linewidth=1.0))
    ax.text(0.558, 0.830, "账单显示：另一个平台", fontsize=10.6, color=RED,
            weight="bold", ha="left", va="center")
    ax.plot([0.558, 0.956], [0.790, 0.790], color=LIGHT, linewidth=1.0)

    rows = [
        ("扣款方", "广州网易计算机系统有限公司"),
        ("商品说明", "6000 金块"),
        ("订单", "查不到"),
    ]
    yy = 0.680
    for label, value in rows:
        ax.text(0.558, yy, label, fontsize=8.8, color=GRAY, ha="left",
                va="center")
        ax.text(0.558, yy - 0.052, value, fontsize=11.4, color=DARK,
                weight="bold", ha="left", va="center")
        ax.plot([0.558, 0.956], [yy - 0.096, yy - 0.096], color=LIGHT,
                linewidth=0.8)
        yy -= 0.150

    ax.text(0.558, 0.240,
            "钱扣了，订单没了。客服还在，\n“退款专员”接着上场。",
            fontsize=9.0, color=SLATE, ha="left", va="center", linespacing=1.9)

    punchline(fig, "从点进帖子那一刻起，对面可能就不是奶茶店。")
    footer(fig, "事实：扣款方与商品说明据黎女士付款页面显示；订单状态据其讲述｜制图：本文")
    fig.savefig(OUT + "图2_帖子写的是奶茶账单写的是金块.png", dpi=150,
                facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("一头是一个月的公司，一头是几个月的饭钱",
               "记者调查：受害者多为大学生等年轻群体；涉事公司成立不足一个月")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    panels = [
        ("受害者", "多为大学生等年轻群体", "有人被骗走几个月生活费",
         ["一杯奶茶的门槛，落在“点一下不心疼”的位置"]),
        ("涉事公司", "成立不足一个月", "小程序已被关停",
         ["发帖、拉人进小程序、收钱、引向网贷"]),
    ]

    xs = [0.018, 0.532]
    for i, (name, line1, line2, notes) in enumerate(panels):
        face = "#fafbfc" if i == 1 else "#fbf6f2"
        ax.add_patch(FancyBboxPatch((xs[i], 0.150), 0.450, 0.740,
                                    boxstyle="round,pad=0.012",
                                    facecolor=face, edgecolor=LIGHT,
                                    linewidth=1.0))
        ax.text(xs[i] + 0.028, 0.830, name, fontsize=11.0, color=NAVY,
                weight="bold", ha="left", va="center")
        ax.plot([xs[i] + 0.028, xs[i] + 0.422], [0.788, 0.788],
                color=LIGHT, linewidth=1.0)

        ax.text(xs[i] + 0.028, 0.700, line1, fontsize=12.0, color=RED,
                weight="bold", ha="left", va="center")
        ax.text(xs[i] + 0.028, 0.610, line2, fontsize=12.0, color=RED,
                weight="bold", ha="left", va="center")

        yy = 0.470
        for n in notes:
            ax.plot([xs[i] + 0.034], [yy + 0.006], marker="s", markersize=4.6,
                    color=SLATE, zorder=3)
            ax.text(xs[i] + 0.056, yy, n, fontsize=8.8, color=SLATE,
                    ha="left", va="top", linespacing=1.8)
            yy -= 0.105

    punchline(fig, "免费的门槛越低，退出的代价越高。")
    footer(fig, "事实：记者调查与涉事公司情况，据 2026-11-18 报道｜制图：本文")
    fig.savefig(OUT + "图3_一头是一个月的公司一头是几个月的饭钱.png", dpi=150,
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)
