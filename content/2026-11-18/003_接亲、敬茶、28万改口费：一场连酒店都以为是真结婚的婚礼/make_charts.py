# -*- coding: utf-8 -*-
"""
《接亲、敬茶、28 万改口费：一场连酒店都以为是真结婚的婚礼》配套图表
事实口径：
  10-30 起，多段"安徽宿州双胞胎姐妹一同出嫁"视频集中发布，发布者多为婚纱、
  摄影、婚庆车队、主持人等从业者，最早流出视频未标注"剧情演绎""工作拍摄"；
  11-14/15 两位"新娘"账号发布婚礼现场照片，仍无标注；
  11-15 当地网友发文指认：并非真实婚礼，是工作拍摄、剧本演绎；
  11-16 宿州市委网信办表示已要求埇桥区委网信办调查核实；提供场地的酒店称，
         婚纱店与婚庆车队定制了场地，"婚礼"当天酒店员工也以为是真结婚，
         事后才知是婚纱店办的一场"沙龙"；
  11-17 宿州警方通报：周某某、张某为引流吸粉、博取关注，编造拍摄虚假场景，
         以剧本演绎形式制作虚构视频发布，扰乱公共秩序，依《治安管理处罚法》
         对两人作出行政处罚。
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
GREEN = "#4f6b58"
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
    fig = base("十八天，从刷屏到处罚",
               "10 月 30 日刷屏送祝福，11 月 17 日警方通报：编造拍摄，行政处罚")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    y = 0.760
    ax.plot([0.040, 0.960], [y, y], color=LIGHT, linewidth=2.6,
            solid_capstyle="round", zorder=1)

    nodes = [
        (0.075, "10-30", "集中发布", "婚纱、摄影、车队、\n司仪等账号齐发\n未标注「演绎」", NAVY),
        (0.238, "10-30 起", "全网送祝福", "接亲、敬茶\n28 万改口费\n评论区一片恭喜", NAVY),
        (0.401, "11-14/15", "仍无标注", "两位「新娘」发\n婚礼现场照片\n问是否真结婚，未回", SLATE),
        (0.564, "11-15", "反转", "当地网友发文：\n这是工作拍摄\n是剧本演绎", RED),
        (0.727, "11-16", "官方回应", "网信办要求调查核实\n酒店：是婚纱店\n办的一场「沙龙」", RED),
        (0.890, "11-17", "警方通报", "周某某、张某\n编造虚假场景\n被行政处罚", RED),
    ]
    for x, date, head, body, color in nodes:
        ax.plot([x], [y], marker="o", markersize=10, color=color,
                markeredgecolor="white", markeredgewidth=1.7, zorder=4)
        ax.text(x, y + 0.062, date, fontsize=10.6, color=color, weight="bold",
                ha="center", va="bottom")
        ax.text(x, y - 0.075, head, fontsize=10.4, color=DARK, weight="bold",
                ha="center", va="top")
        ax.text(x, y - 0.145, body, fontsize=8.8, color=SLATE, ha="center",
                va="top", linespacing=1.65)

    ax.plot([0.040, 0.960], [0.330, 0.330], color=LIGHT, linewidth=1.0)

    marks = [
        ("最开始的 16 天里，没有任何一个发布账号在视频上标注「剧情演绎」或「工作拍摄」。", RED),
        ("18 天里，祝福是真的，婚礼是拍的。这两件事可以同时成立，但不可以同时被隐瞒。", SLATE),
    ]
    yy = 0.245
    for text, color in marks:
        ax.plot([0.048], [yy], marker="s", markersize=6, color=color, zorder=3)
        ax.text(0.072, yy, text, fontsize=10.4, color=DARK, ha="left",
                va="center")
        yy -= 0.095

    punchline(fig, "从「恭喜」到「通报」，中间隔着一句没人写的标注。")
    footer(fig, "事实：纵览新闻、羊城派、中华网、光明网转华商报（宿州警方通报）｜制图：本文")
    fig.savefig(OUT + "图1_十八天从刷屏到处罚.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("一场婚礼，哪些是真的",
               "镜头里每一样都是真的：场地、婚纱、人脸、流程。不真的只有一件")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(0.060, 0.845, "视频里看到的", fontsize=12.4, color=NAVY,
            weight="bold", ha="left", va="center")
    ax.text(0.545, 0.845, "查证后是这样的", fontsize=12.4, color=RED,
            weight="bold", ha="left", va="center")

    ax.plot([0.500, 0.500], [0.120, 0.800], color=LIGHT, linewidth=1.0,
            linestyle=(0, (4, 4)))

    left = [
        ("接亲队伍上门", "队伍、鞭炮、堵门，一样不少"),
        ("给父母敬茶", "跪姿、茶具、长辈受礼"),
        ("28 万改口费", "父母当场递出银行卡"),
        ("新人乘婚车", "车队、路线、跟拍"),
        ("司仪主持", "流程、串词、掌声"),
        ("酒店宴会厅", "真酒店，真场地，真布景"),
    ]
    yy = 0.755
    for name, note in left:
        ax.plot([0.058], [yy], marker="s", markersize=6.5, color=NAVY, zorder=3)
        ax.text(0.085, yy, name, fontsize=10.8, color=DARK, weight="bold",
                ha="left", va="center")
        ax.text(0.085, yy - 0.048, note, fontsize=9.2, color=GRAY, ha="left",
                va="center")
        yy -= 0.105

    right = [
        ("场地是定制的", "婚纱店与婚庆车队\n向酒店定制了婚礼场地"),
        ("当天是「沙龙」", "酒店工作人员也以为\n是真结婚，事后才知"),
        ("「新娘」是模特", "主页写：178 模特双胞胎\n可接拍摄"),
        ("视频没标注", "最早流出的视频\n未标「剧情演绎」「工作拍摄」"),
    ]
    yy = 0.755
    for name, note in right:
        ax.plot([0.543], [yy], marker="s", markersize=6.5, color=RED, zorder=3)
        ax.text(0.570, yy, name, fontsize=10.8, color=DARK, weight="bold",
                ha="left", va="center")
        ax.text(0.570, yy - 0.050, note, fontsize=9.2, color=GRAY, ha="left",
                va="top", linespacing=1.6)
        yy -= 0.155

    ax.add_patch(FancyBboxPatch((0.055, 0.042), 0.890, 0.090,
                                boxstyle="round,pad=0.010", facecolor=SAND,
                                edgecolor="#d9cdb6", linewidth=1.0, zorder=2))
    ax.text(0.500, 0.087,
            "所以它才骗过了所有人：把「演戏」做到了「真办」的规格，只差一句标注。",
            fontsize=10.6, color="#7a6746", ha="center", va="center", zorder=3)

    punchline(fig, "场地是真的，婚纱是真的，只有「结婚」这件事是拍的。")
    footer(fig, "事实：羊城派（纵览新闻）调查报道、宿州警方 11-17 通报｜「28 万改口费」为视频中的说法｜制图：本文")
    fig.savefig(OUT + "图2_一场婚礼哪些是真的.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("被问到时，他们没有沉默",
               "不是「没来得及标注」，是有人问到脸上，答的是另一种说法")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    xs = [0.050, 0.380, 0.690]
    header = ["网友在评论区问", "账号当时这样回", "后来查到的"]
    for x, h in zip(xs, header):
        ax.text(x, 0.845, h, fontsize=10.8, color=GRAY, weight="bold",
                ha="left", va="center")
    ax.plot([0.045, 0.955], [0.812, 0.812], color=LIGHT, linewidth=1.0)

    rows = [
        ("「以为是婚纱店\n在拍广告」", "「是接亲现场」", "现场是婚纱店\n定制场地办的沙龙"),
        ("「两个女婿\n是宿州的吗」", "「是的」", "未获进一步说明"),
        ("「嫁的同一家吗」", "「不是，两个新郎关系\n比较好，选在同一天结婚」", "两位「新娘」为模特\n主页写「可接拍摄」"),
        ("「是不是\n真结婚」（多次）", "未回复", "视频未标注\n「剧情演绎」"),
    ]
    yy = 0.745
    for i, (q, a, fact) in enumerate(rows):
        if i % 2 == 0:
            ax.add_patch(Rectangle((0.040, yy - 0.098), 0.920, 0.148,
                                   facecolor="#fafbfc", edgecolor="none",
                                   zorder=1))
        ax.text(xs[0], yy, q, fontsize=9.6, color=DARK, ha="left", va="center",
                linespacing=1.6, zorder=3)
        ax.text(xs[1], yy, a, fontsize=9.8, color=RED, ha="left", va="center",
                linespacing=1.6, zorder=3)
        ax.text(xs[2], yy, fact, fontsize=9.4, color=SLATE, ha="left",
                va="center", linespacing=1.6, zorder=3)
        yy -= 0.150

    ax.plot([0.045, 0.955], [0.150, 0.150], color=LIGHT, linewidth=1.0)
    ax.text(0.050, 0.098,
            "沉默可以解释成疏忽；但一句「是接亲现场」，解释不了。",
            fontsize=10.6, color=SLATE, ha="left", va="center")

    punchline(fig, "不标注是省略，回一句「是接亲现场」是加固。")
    footer(fig, "事实：羊城派（纵览新闻）11-16 调查报道中记者检索到的评论区截图与回复｜制图：本文")
    fig.savefig(OUT + "图3_被问到时他们没有沉默.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)