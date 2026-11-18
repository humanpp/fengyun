# -*- coding: utf-8 -*-
"""
《5 折代点外卖：他下单，你取餐，然后他说没收到》配套图表
事实口径（中央广播电视总台中国之声 2026-11-17 报道，中新网等转载）：
  今年 8 月，外卖骑手小陈在福建长乐一小区按备注把餐放电梯位置、拍照并点送达，
  随后收到退款通知，下单人称未收到餐品；平台核验后帮骑手申诉免责，
  「备注放电梯」成为风控识别异常订单的重要特征；
  次日同一地址再现高额订单，福州长乐警方蹲守研判，锁定 6 人团伙；
  初步查证作案 1700 余单，涉及全国 21 个省市 700 多名群众，6 人已刑拘；
  手法：网上发布「5 折代点外卖」广告 → 匿名账号接单 → 填大门口、电梯口等
  模糊地址、预留虚假电话 → 顾客取餐后谎称未收到 → 骗取平台退款；
  记者实测：36 元订单卖家报价 20 元代下，称平日多接 150 元上下，
  默认「先下单、后退款」，宣称 200 元以内都可退款，同店还挂出「5 折教程」；
  新变种：利用「爱心商家向骑手打折」政策，以六七折代下单，发骑手凭证骗商家折扣。
风格：克制传媒风，白底、低饱和配色、标题即结论。输出目录 = 脚本所在目录。
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch, FancyArrowPatch

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


def punchline(fig, text, y=0.082):
    fig.text(0.045, y, text, fontsize=10.8, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.6", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


# ------------------------------------------------------------------ 图 1
def fig1():
    fig = base("这条链上，只有一步是假的",
               "前四步完全符合规则，第五步把账单转给了别人")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    steps = [
        ("① 发广告", "二手平台\n「5 折代点外卖」\n「内部链接」", NAVY),
        ("② 匿名下单", "用匿名账号接单\n付款人 ≠ 收货人", NAVY),
        ("③ 填模糊地址", "「大门口」「电梯口」\n预留虚假电话", NAVY),
        ("④ 骑手送达", "按备注放电梯\n拍照、点送达", SLATE),
        ("⑤ 申请退款", "「没收到餐」\n退款到账", RED),
    ]
    xs = [0.075, 0.253, 0.431, 0.609, 0.787]
    w, y0, h = 0.150, 0.585, 0.235
    for (head, body, color), x in zip(steps, xs):
        fc = "#fbf3f1" if color == RED else "#fafbfc"
        ax.add_patch(FancyBboxPatch((x, y0), w, h, boxstyle="round,pad=0.012",
                                    facecolor=fc, edgecolor=color,
                                    linewidth=1.3, zorder=3))
        ax.text(x + w / 2, y0 + h - 0.045, head, fontsize=10.6, color=color,
                weight="bold", ha="center", va="center", zorder=4)
        ax.text(x + w / 2, y0 + 0.078, body, fontsize=8.8, color=SLATE,
                ha="center", va="center", linespacing=1.7, zorder=4)
        if x < xs[-1]:
            ax.add_patch(FancyArrowPatch((x + w + 0.006, y0 + h / 2),
                                         (x + w + 0.020, y0 + h / 2),
                                         arrowstyle="-|>", color=GRAY,
                                         linewidth=1.3, zorder=2))

    ax.text(0.075, 0.520, "规则内", fontsize=9.8, color=NAVY, ha="left",
            va="center")
    ax.plot([0.140, 0.740], [0.520, 0.520], color=NAVY, linewidth=1.0,
            alpha=0.55)
    ax.text(0.787, 0.520, "唯一造假的一步", fontsize=9.8, color=RED,
            ha="left", va="center")
    ax.plot([0.787, 0.940], [0.520, 0.520], color=RED, linewidth=1.0, alpha=0.55)

    # 谁在亏
    ax.plot([0.045, 0.955], [0.445, 0.445], color=LIGHT, linewidth=1.0)
    ax.text(0.050, 0.395, "钱从谁那儿出", fontsize=11.0, color=DARK,
            weight="bold", ha="left", va="center")

    losers = [
        (0.075, "平台", "退了款的订单\n由平台先行垫付"),
        (0.320, "商家", "餐已经做出去\n货款收不回来"),
        (0.565, "骑手", "被投诉「没送到」\n这一次申诉免责了"),
        (0.810, "顾客", "5 折的差价\n其实是别人在付"),
    ]
    for x, head, body in losers:
        ax.plot([x + 0.008], [0.330], marker="s", markersize=6.5, color=RED,
                zorder=3)
        ax.text(x + 0.030, 0.330, head, fontsize=10.4, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(x + 0.030, 0.265, body, fontsize=8.8, color=GRAY, ha="left",
                va="top", linespacing=1.7)

    punchline(fig, "你不是在省钱，是在让别人替你付这顿饭。")
    footer(fig, "事实：中央广播电视总台中国之声（2026-11-17），中新网、京报网转载｜流程为警方通报口径｜制图：本文")
    fig.savefig(OUT + "图1_这条链上只有一步是假的.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("它有报价，也有教程",
               "记者在二手平台实测：这不是偶发的骗，是一门明码标价的生意")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # 左：一次实测对话
    ax.add_patch(FancyBboxPatch((0.050, 0.240), 0.400, 0.570,
                                boxstyle="round,pad=0.012", facecolor="#fafbfc",
                                edgecolor=LIGHT, linewidth=1.1))
    ax.text(0.075, 0.762, "一次实测", fontsize=11.6, color=DARK, weight="bold",
            ha="left", va="center")
    ax.text(0.075, 0.708, "记者发去一单 36 元的外卖", fontsize=9.8,
            color=GRAY, ha="left", va="center")

    dialogue = [
        ("卖家：", "这单太低", GRAY),
        ("卖家：", "平日接的多是 150 元上下", GRAY),
        ("卖家：", "20 元，我帮你下", RED),
    ]
    yy = 0.630
    for who, line, color in dialogue:
        ax.text(0.078, yy, who, fontsize=9.6, color=SLATE, ha="left",
                va="center")
        ax.text(0.135, yy, line, fontsize=9.8, color=color, ha="left",
                va="center")
        yy -= 0.070

    ax.plot([0.078, 0.420], [0.405, 0.405], color=LIGHT, linewidth=0.9)
    ax.text(0.078, 0.352, "默认规则是「先下单、后退款」，", fontsize=9.4,
            color=DARK, ha="left", va="center")
    ax.text(0.078, 0.295, "并称「200 元以内外卖都可以退款」。", fontsize=9.4,
            color=DARK, ha="left", va="center")

    # 右：四条要点
    ax.text(0.520, 0.792, "这几句话说明了什么", fontsize=11.6, color=RED,
            weight="bold", ha="left", va="center")

    points = [
        ("有定价", "36 元的单收 20 元，5 折是幌子，\n真正的价码是「帮你骗一次」。"),
        ("有客单价", "平日多接 150 元上下的单，\n大额订单才是主要目标。"),
        ("有退款上限", "「200 元以内都可以退款」，\n说明他们对风控阈值有经验。"),
        ("有教学", "同一店铺挂着「外卖 5 折教程」，\n套路已经可以复制、可以卖。"),
    ]
    yy = 0.730
    for head, body in points:
        ax.text(0.520, yy, head, fontsize=10.6, color=DARK, weight="bold",
                ha="left", va="center")
        ax.text(0.520, yy - 0.052, body, fontsize=9.4, color=SLATE, ha="left",
                va="top", linespacing=1.7)
        yy -= 0.170

    ax.text(0.050, 0.170,
            "一个人骗一次，是案子；有报价、有上限、有教程，是行业。",
            fontsize=10.4, color=SLATE, ha="left", va="center")

    punchline(fig, "5 折不是他的渠道便宜，是他根本没打算付这笔钱。")
    footer(fig, "事实：中央广播电视总台中国之声（2026-11-17）记者在二手平台的实测与卖家回复｜制图：本文")
    fig.savefig(OUT + "图2_它有报价也有教程.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("已经出到第二个版本",
               "从骗平台退款，转向骗商家折扣——被薅的是给骑手让利的那批店")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # v1
    ax.add_patch(FancyBboxPatch((0.050, 0.470), 0.890, 0.330,
                                boxstyle="round,pad=0.012", facecolor="#fafbfc",
                                edgecolor=NAVY, linewidth=1.2))
    ax.text(0.072, 0.755, "第一版：骗平台的退款", fontsize=11.8, color=NAVY,
            weight="bold", ha="left", va="center")
    ax.text(0.072, 0.690, "下单 → 骑手放餐送达 → 谎称没收到 → 平台退款",
            fontsize=9.6, color=SLATE, ha="left", va="center")
    ax.text(0.072, 0.620, "受损方：平台先行垫付，商家白做一单，骑手背上「没送到」的投诉。",
            fontsize=9.6, color=DARK, ha="left", va="center")
    ax.text(0.072, 0.550, "特征：备注里写「放电梯」「放大门口」。",
            fontsize=9.6, color=RED, ha="left", va="center")
    ax.text(0.072, 0.497, "这是 1700 余单的做法，也是这次被抓的那一版。",
            fontsize=9.2, color=GRAY, ha="left", va="center")

    # v2
    ax.add_patch(FancyBboxPatch((0.050, 0.130), 0.890, 0.300,
                                boxstyle="round,pad=0.012", facecolor="#fbf3f1",
                                edgecolor=RED, linewidth=1.2))
    ax.text(0.072, 0.385, "第二版：骗商家的折扣", fontsize=11.8, color=RED,
            weight="bold", ha="left", va="center")
    ax.text(0.072, 0.322, "利用「爱心商家给骑手打折」的政策 → 六七折代下单 → 发骑手凭证到店核销",
            fontsize=9.6, color=SLATE, ha="left", va="center")
    ax.text(0.072, 0.255, "受损方：主动给骑手让利的那批店——善意成了被利用的漏洞。",
            fontsize=9.6, color=DARK, ha="left", va="center")
    ax.text(0.072, 0.190, "平台方说：灰黑产的源头在「信息发布和交易撮合」环节。",
            fontsize=9.6, color=RED, ha="left", va="center")

    punchline(fig, "版本会更新，识别方法不该只更新一半。")
    footer(fig, "事实：中国之声报道中办案民警与外卖平台权益保障中心负责人的表述｜「六七折」为该负责人所述｜制图：本文")
    fig.savefig(OUT + "图3_已经出到第二个版本.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)