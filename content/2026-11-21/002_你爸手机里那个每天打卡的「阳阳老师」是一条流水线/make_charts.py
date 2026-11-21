# -*- coding: utf-8 -*-
"""
《你爸手机里那个每天打卡领红包的「阳阳老师」，可能是一条流水线》配套图表

事实口径（全部来自大众日报 2026-11-18 卧底调查，记者贾涵宇）：
  · AI 生成"名医"短剧 + 蓝大褂"导师" + 加微信领资料
  · 小鹅通链接单日有效、观看进度后台监测、40 分钟 + 选择题领 0.38 元红包
  · 连续打卡 14 天送藏红花
  · 前五天讲经历；第六天转"为什么医院总看不好"并推七十味珍珠丸、四味石榴丸
  · 第七天进"VIP班"微信群；后续新药号称治三高、偏瘫、脑梗
  · 客服从"阳阳老师"轮换到"惠惠老师"
  · 代运营：演员费 500–1000 元 / 30 分钟；AI 内容约 200 元 / 分钟；一周投放
  · 深圳机构：30 分钟访谈含演员、拍摄、剪辑 6000 元一条，并建议虚构栏目名

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
BLUSH = "#fbf1ef"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep

# 统一的纵向分区，避免标题与正文互相压字
Y_TITLE = 0.958
Y_SUB = 0.898
Y_BODY_TOP = 0.800
Y_PUNCH = 0.072
Y_FOOT = 0.020


def header(fig, title, sub):
    fig.text(0.045, Y_TITLE, title, fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, Y_SUB, sub, fontsize=10.8, color=GRAY,
             ha="left", va="top")


def footer(fig, text):
    fig.text(0.045, Y_FOOT, text, fontsize=8.4, color=GRAY,
             ha="left", va="bottom")


def punchline(fig, text):
    fig.text(0.045, Y_PUNCH, text, fontsize=10.4, color=DARK,
             ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


def card(ax, x, y, w, h, edge, face="white", lw=1.0):
    # 底 zorder=2：卡内的柱子、色块画在 3 层，文字画在 4 层，保证不被卡片盖住
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.004,rounding_size=0.014",
        facecolor=face, edgecolor=edge, linewidth=lw, zorder=2))

# ---------------------------------------------------------------- 图 1
def fig1():
    fig = plt.figure(figsize=(12, 7.4))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    header(fig, "七天剧本：每天只往前挪一步",
           "老人走完的每一步，都是他自愿点的")

    steps = [
        ("直播", "蓝大褂“导师”\n做手势拉经脉\n右下角弹卡片：\n加微信领资料"),
        ("加人", "“阳阳老师”\n头像 AI 生成\n发穴位图\n约好打卡送礼"),
        ("打卡", "清晨六点发链接\n单日有效，\n进度被后台监测\n红包 0.38 元"),
        ("看剧", "AI 短剧讲\n“名医”传奇经历\n前五天只讲故事\n不提一个药字"),
        ("转向", "第六天：\n为什么小病\n去医院总不见好？\n“秘方”登场"),
        ("进群", "第七天：VIP班\n群里在抢\n七十味珍珠丸\n四味石榴丸"),
        ("收割", "新药号称治\n三高、偏瘫、脑梗\n老人晒 B 超单\n求药、备货"),
    ]

    n = len(steps)
    left, right, gap = 0.042, 0.958, 0.013
    w = (right - left - gap * (n - 1)) / n
    card_top, card_bot = 0.690, 0.250
    y_line = 0.780

    ax.plot([left, right], [y_line, y_line], color=LIGHT, linewidth=2.6,
            solid_capstyle="round", zorder=1)

    for i, (title, body) in enumerate(steps):
        x = left + i * (w + gap)
        cx = x + w / 2
        hot = i >= 5
        edge = RED if hot else LIGHT
        card(ax, x, card_bot, w, card_top - card_bot, edge,
             face=BLUSH if hot else "white", lw=1.6 if hot else 0.9)

        ax.text(cx, card_top - 0.048, f"{i + 1}", fontsize=11.5,
                color=RED if hot else GRAY, ha="center", va="center",
                weight="bold", zorder=4)
        ax.text(cx, card_top - 0.115, title, fontsize=15.0,
                color=RED if hot else NAVY, ha="center", va="center",
                weight="bold", zorder=4)
        ax.text(cx, card_bot + (card_top - card_bot) * 0.42, body,
                fontsize=9.8, color=DARK if hot else SLATE,
                ha="center", va="center", linespacing=1.62, zorder=4)

        ax.plot([cx, cx], [y_line - 0.004, card_top],
                color=RED if hot else LIGHT, linewidth=1.1,
                linestyle=(0, (2.2, 2.2)), zorder=2)
        ax.add_patch(plt.Circle((cx, y_line), 0.0155,
                                facecolor=RED if hot else "white",
                                edgecolor=RED if hot else NAVY,
                                linewidth=1.8, zorder=4))

    ax.text(left, 0.828, "最后两天是拐点：前面全是铺垫，第六天才出现“卖”的动作",
            fontsize=9.8, color=RED, ha="left", va="center", weight="bold")

    punchline(fig, "前五天只让老人相信一个人；等信了，第六天才开始卖药。")
    footer(fig, "数据来源：大众日报《党报帮办丨“AI名医”，盯上老年人钱包》，记者贾涵宇，2026-11-18")
    fig.savefig(OUT + "图1_七天剧本.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(12, 6.6))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    header(fig, "六千块一条：钱花在哪，省在哪",
           "同一段 30 分钟“访谈”，两种买法——差别在有没有真人")

    # ---- 左卡：深圳机构 6000 元 / 条
    card(ax, 0.042, 0.230, 0.410, 0.570, NAVY, lw=1.5)
    ax.text(0.068, 0.752, "深圳某机构：30 分钟访谈", fontsize=12.8,
            color=NAVY, weight="bold", ha="left", va="center")
    ax.text(0.068, 0.700, "找演员 + 拍摄 + 剪辑，全包", fontsize=10.2,
            color=SLATE, ha="left", va="center")
    ax.plot([0.068, 0.428], [0.665, 0.665], color=LIGHT, linewidth=1.0)

    ax.add_patch(Rectangle((0.068, 0.560), 0.240, 0.052,
                           facecolor=NAVY, edgecolor="none", zorder=3))
    ax.text(0.068, 0.632, "一条成片", fontsize=9.8, color=SLATE,
            ha="left", va="center")
    ax.text(0.320, 0.586, "6,000 元", fontsize=14.0, color=NAVY,
            weight="bold", ha="left", va="center")

    ax.text(0.068, 0.400,
            "深圳机构另外给了一个主意：\n自己虚构一个栏目名称，\n"
            "“看起来有官方背书，更有可信度”。",
            fontsize=10.0, color=RED, ha="left", va="center", linespacing=1.70)

    ax.text(0.068, 0.268, "所谓“官方栏目”就是这么来的——不是买来的资质，是起了个名字。",
            fontsize=9.0, color=GRAY, ha="left", va="center")

    # ---- 右卡：代运营机构报价
    card(ax, 0.512, 0.230, 0.446, 0.570, RED, lw=1.5)
    ax.text(0.538, 0.752, "代运营机构：可以换更便宜的零件", fontsize=12.8,
            color=RED, weight="bold", ha="left", va="center")
    ax.text(0.538, 0.700, "负责人小孙：直播间里的导师就是请的演员",
            fontsize=10.2, color=SLATE, ha="left", va="center")
    ax.plot([0.538, 0.932], [0.665, 0.665], color=LIGHT, linewidth=1.0)

    rows = [
        (0.606, "演员费", "500 – 1000 元 / 30 分钟", NAVY, 11.4),
        (0.522, "制作周期", "一周即可投放", NAVY, 11.4),
        (0.438, "要 AI 生成的内容", "约 200 元 / 分钟", RED, 12.2),
    ]
    for y, label, value, color, fs in rows:
        ax.text(0.538, y, label, fontsize=10.0, color=SLATE,
                ha="left", va="center")
        ax.text(0.932, y, value, fontsize=fs, color=color,
                weight="bold", ha="right", va="center")

    ax.text(0.538, 0.330,
            "还能给演员生成数字人形象，批量产出其他视频；\n账号一触发风控，就弃号换壳。",
            fontsize=9.4, color=SLATE, ha="left", va="center", linespacing=1.70)

    ax.text(0.538, 0.268, "演员、拍摄、剪辑、数字人，每一环都能外包。",
            fontsize=9.0, color=GRAY, ha="left", va="center")

    punchline(fig, "六千块买到的不是资质，是一个能随时换掉的人。")
    footer(fig, "数据来源：大众日报，2026-11-18；报价为受访机构当场给出，非行业均价")
    fig.savefig(OUT + "图2_六千块.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(12, 6.4))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    header(fig, "今晚四件事，和一句话",
           "不用跟爸妈吵，先看清他手机里有什么")

    items = [
        ("通讯录搜三个词", "搜“老师”“健康管家”“VIP班”，带这些字样的\n联系人，逐个问一句是谁。"),
        ("翻群聊列表", "有没有“先进学员”“优秀学员”“养生”“秘方”\n这类群名。"),
        ("看转账和快递", "有没有来历不明的药丸、药酒、护腕，\n和对应的转账记录。"),
        ("查填过的信息", "有没有在“领礼品”链接里填过姓名、手机号、\n身份证号、病史。"),
    ]

    top, h, gap = 0.760, 0.140, 0.026
    for i, (title, body) in enumerate(items):
        y = top - i * (h + gap) - h
        card(ax, 0.042, y, 0.610, h, LIGHT, lw=1.0)
        ax.text(0.070, y + h / 2, f"{i + 1}", fontsize=17, color=LIGHT,
                weight="bold", ha="center", va="center")
        ax.text(0.104, y + h * 0.680, title, fontsize=12.6, color=NAVY,
                weight="bold", ha="left", va="center")
        ax.text(0.104, y + h * 0.290, body, fontsize=9.8, color=SLATE,
                ha="left", va="center", linespacing=1.55)

    card(ax, 0.686, 0.180, 0.272, 0.580, RED, face=BLUSH, lw=1.5)
    ax.text(0.822, 0.700, "教一句话", fontsize=11.0, color=RED,
            ha="center", va="center", weight="bold")
    ax.plot([0.722, 0.922], [0.666, 0.666], color=RED, linewidth=0.9, alpha=0.5)
    ax.text(0.822, 0.418,
            "说不清医院名字、\n也查不到这个人\n的视频，\n别信他是名医。",
            fontsize=13.2, color=DARK, ha="center", va="center",
            linespacing=1.90, weight="bold")
    ax.text(0.822, 0.232,
            "话不用多，\n能打断就好。",
            fontsize=9.2, color=GRAY, ha="center", va="center",
            linespacing=1.70)

    punchline(fig, "短剧里那句“拉通经脉”，换成谁的脸都能拍——成本 6000 元。")
    footer(fig, "核对依据：大众日报 2026-11-18 卧底调查披露的引流话术与打卡机制")
    fig.savefig(OUT + "图3_今晚四件事.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)
