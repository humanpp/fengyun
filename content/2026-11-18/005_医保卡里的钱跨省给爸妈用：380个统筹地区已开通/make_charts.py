# -*- coding: utf-8 -*-
"""
《医保卡里的钱，跨省也能给爸妈用了》配套图表
政策依据：《国家医保局 财政部关于做好职工基本医疗保险个人账户跨省共济工作的通知》
  （医保发〔2025〕35 号，2025-12-24 成文，2026-01 公开）：
  · 共济对象为职工医保参保人的近亲属，被共济人须为基本医保参保对象；
  · 依托全国统一医保信息平台设立「个人医保钱包」，由共济人设定共济额度；
  · 用途三类：定点机构就医的个人负担费用、定点药店购药械耗材的个人负担费用、
    参加城乡居民基本医保与长期护理保险的个人缴费；
  · 虚拟额度管理，不得将医保基金实际拨入钱包；额度内共济人不得再用；
    关系解除时未使用额度自动恢复；医保关系终止或跨统筹地区转移时关系自动解除；
  · 资金按月全额清算，参照跨省异地就医清算流程。
数据口径：截至 11 月 16 日，全国 380 个统筹地区支持用共济金额缴纳参保费，
  占统筹地区总数 96.45%（国家医保局 11 月 16—17 日披露，据素材方口径）。
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
    fig = base("这笔钱怎么走到爸妈那儿",
               "不是转账，是设一个额度；额度的三个出口，第三个最实用")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # 左：来源
    ax.add_patch(FancyBboxPatch((0.048, 0.560), 0.215, 0.250,
                                boxstyle="round,pad=0.012", facecolor="#fafbfc",
                                edgecolor=NAVY, linewidth=1.3))
    ax.text(0.156, 0.755, "职工医保", fontsize=11.2, color=NAVY, weight="bold",
            ha="center", va="center")
    ax.text(0.156, 0.700, "个人账户", fontsize=11.2, color=NAVY, weight="bold",
            ha="center", va="center")
    ax.text(0.156, 0.630, "你在城里上班\n每月划进来的那笔钱", fontsize=9.0,
            color=GRAY, ha="center", va="center", linespacing=1.7)

    # 中：医保钱包
    ax.add_patch(FancyBboxPatch((0.315, 0.520), 0.215, 0.330,
                                boxstyle="round,pad=0.012", facecolor="#eaf0ea",
                                edgecolor=GREEN, linewidth=1.3))
    ax.text(0.422, 0.795, "医保钱包", fontsize=11.2, color=GREEN, weight="bold",
            ha="center", va="center")
    ax.text(0.422, 0.720, "设一个共济额度", fontsize=9.6, color=DARK,
            ha="center", va="center")
    ax.text(0.422, 0.630, "虚拟额度，不是转账\n基金不会真的打进钱包", fontsize=8.8,
            color=GRAY, ha="center", va="center", linespacing=1.7)
    ax.text(0.422, 0.548, "额度之内，你自己不能再花", fontsize=8.8, color=RED,
            ha="center", va="center")

    # 箭头 1
    ax.add_patch(FancyArrowPatch((0.272, 0.685), (0.305, 0.685),
                                 arrowstyle="-|>", color=GRAY, linewidth=1.4))
    # 箭头 2
    ax.add_patch(FancyArrowPatch((0.540, 0.685), (0.575, 0.685),
                                 arrowstyle="-|>", color=GRAY, linewidth=1.4))

    # 右：三个出口
    outs = [
        (0.815, "① 看病", "定点医院就医的\n个人负担费用", 0),
        (0.615, "② 买药", "定点药店买药、器械\n耗材的个人负担费用", 0),
        (0.415, "③ 缴参保费", "给爸妈缴城乡居民医保\n和长期护理保险的个人缴费", 1),
    ]
    for y, head, body, hot in outs:
        fc = "#fbf3f1" if hot else "#fafbfc"
        ec = RED if hot else LIGHT
        ax.add_patch(FancyBboxPatch((0.585, y - 0.075), 0.360, 0.160,
                                    boxstyle="round,pad=0.012", facecolor=fc,
                                    edgecolor=ec, linewidth=1.3))
        ax.text(0.610, y + 0.035, head, fontsize=10.8,
                color=RED if hot else NAVY, weight="bold", ha="left",
                va="center")
        ax.text(0.610, y - 0.035, body, fontsize=8.8, color=SLATE, ha="left",
                va="center", linespacing=1.7)

    ax.add_patch(FancyArrowPatch((0.540, 0.685), (0.578, 0.760),
                                 arrowstyle="-|>", color=GRAY, linewidth=1.1))
    ax.add_patch(FancyArrowPatch((0.540, 0.685), (0.578, 0.615),
                                 arrowstyle="-|>", color=GRAY, linewidth=1.1))
    ax.add_patch(FancyArrowPatch((0.540, 0.685), (0.578, 0.415),
                                 arrowstyle="-|>", color=RED, linewidth=1.3))

    ax.plot([0.045, 0.955], [0.330, 0.330], color=LIGHT, linewidth=1.0)
    notes = [
        "共济对象是「近亲属」，被共济人必须是基本医保的参保人——爸妈没参保，这条通道就用不上。",
        "额度用完可以再设；解除共济关系，没用掉的那部分自动回到你的账户。",
    ]
    yy = 0.255
    for text in notes:
        ax.plot([0.050], [yy], marker="s", markersize=6, color=GREEN, zorder=3)
        ax.text(0.074, yy, text, fontsize=9.6, color=DARK, ha="left",
                va="center")
        yy -= 0.085

    punchline(fig, "钱还是你卡里的钱，只是现在能花到他们身上。")
    footer(fig, "依据：《国家医保局 财政部关于做好职工基本医疗保险个人账户跨省共济工作的通知》（医保发〔2025〕35 号）｜制图：本文")
    fig.savefig(OUT + "图1_这笔钱怎么走到爸妈那儿.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("96.45% 是什么概念",
               "380 个统筹地区已经能办，也就是说：基本都能用，但不是全都能用")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # 三个数字
    nums = [
        (0.075, "380", "个统筹地区", "支持用共济金额\n缴纳参保费", NAVY),
        (0.395, "96.45%", "占比", "占统筹地区总数", GREEN),
        (0.715, "约 14", "个还没开通", "按 96.45% 反算\n约 394 个的总盘子", RED),
    ]
    for x, big, unit, note, color in nums:
        ax.text(x, 0.800, big, fontsize=34, color=color, weight="bold",
                ha="left", va="center")
        ax.text(x, 0.700, unit, fontsize=10.6, color=DARK, ha="left",
                va="center")
        ax.text(x, 0.615, note, fontsize=9.0, color=GRAY, ha="left", va="top",
                linespacing=1.7)

    # 比例条
    bar_y, bar_h = 0.410, 0.075
    ax.add_patch(Rectangle((0.050, bar_y), 0.900, bar_h, facecolor="#eef0f3",
                           edgecolor=LIGHT, linewidth=1.0))
    ax.add_patch(Rectangle((0.050, bar_y), 0.900 * 0.9645, bar_h,
                           facecolor=GREEN, edgecolor="none"))
    ax.add_patch(Rectangle((0.050 + 0.900 * 0.9645, bar_y), 0.900 * 0.0355,
                           bar_h, facecolor=RED, edgecolor="none"))
    ax.text(0.500, bar_y + 0.108, "已开通 380 个", fontsize=10.4, color=GREEN,
            weight="bold", ha="center", va="center")
    ax.text(0.955, bar_y + 0.108, "还没开", fontsize=9.2, color=RED,
            ha="right", va="center")

    # 三句话
    ax.plot([0.045, 0.955], [0.340, 0.340], color=LIGHT, linewidth=1.0)
    lines = [
        ("基本都能用", "96.45% 的意思是：你随手挑一个城市，很可能已经在名单里。"),
        ("但别默认", "剩下那 3.55% 不是零。爸妈参保的那个县，未必在里面。"),
        ("看两个地方", "你在哪缴职工医保、爸妈在哪缴居民医保——两头都要对得上。"),
    ]
    yy = 0.265
    for head, body in lines:
        ax.text(0.050, yy, head, fontsize=10.4, color=DARK, weight="bold",
                ha="left", va="center")
        ax.text(0.215, yy, body, fontsize=9.6, color=SLATE, ha="left",
                va="center")
        yy -= 0.078

    punchline(fig, "96.45% 是概率，不是承诺；能不能用，要看你家那个县。")
    footer(fig, "数据：截至 11 月 16 日，380 个统筹地区占 96.45%（国家医保局披露口径）；「约 14 个」为按占比反算所得｜制图：本文")
    fig.savefig(OUT + "图2_9645是什么概念.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("今晚就能做的三件事",
               "不用等通知，打开手机就能查到自己家能不能用")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    steps = [
        ("① 查你的城市", "国家医保服务平台 App\n或当地医保小程序",
         "找到「个人账户共济」\n看有没有「跨省」字样"),
        ("② 查爸妈的参保地", "问爸妈今年在哪缴的\n居民医保（县/区一级）",
         "两个地方都在名单里\n这条路才通"),
        ("③ 看钱包升级了没", "App 里搜「医保钱包」",
         "能看到钱包页面\n说明 2.0 已经跑起来了"),
    ]
    xs = [0.060, 0.370, 0.680]
    for (head, where, done), x in zip(steps, xs):
        ax.add_patch(FancyBboxPatch((x, 0.430), 0.270, 0.360,
                                    boxstyle="round,pad=0.012",
                                    facecolor="#fafbfc", edgecolor=NAVY,
                                    linewidth=1.2))
        ax.text(x + 0.135, 0.730, head, fontsize=11.2, color=NAVY,
                weight="bold", ha="center", va="center")
        ax.text(x + 0.135, 0.635, where, fontsize=8.8, color=GRAY,
                ha="center", va="center", linespacing=1.75)
        ax.plot([x + 0.030, x + 0.240], [0.560, 0.560], color=LIGHT,
                linewidth=0.9)
        ax.text(x + 0.135, 0.490, done, fontsize=8.8, color=GREEN,
                ha="center", va="center", linespacing=1.75)

    ax.add_patch(FancyArrowPatch((0.332, 0.610), (0.366, 0.610),
                                 arrowstyle="-|>", color=GRAY, linewidth=1.3))
    ax.add_patch(FancyArrowPatch((0.642, 0.610), (0.676, 0.610),
                                 arrowstyle="-|>", color=GRAY, linewidth=1.3))

    # 三个坑
    ax.plot([0.045, 0.955], [0.375, 0.375], color=LIGHT, linewidth=1.0)
    ax.text(0.050, 0.338, "三个容易踩的坑", fontsize=10.8, color=RED,
            weight="bold", ha="left", va="center")

    pits = [
        ("不是转账", "设的是虚拟额度，基金不会打进钱包。\n所以别指望「把钱取出来」。"),
        ("额度会占用", "额度一旦设出去，这部分钱你自己\n就不能再用来买药了。"),
        ("会自己解除", "医保关系终止、或跨统筹地区转移时，\n共济关系自动解除。"),
    ]
    yy = 0.282
    for head, body in pits:
        ax.text(0.050, yy, head, fontsize=9.8, color=DARK, weight="bold",
                ha="left", va="center")
        ax.text(0.175, yy, body, fontsize=9.2, color=SLATE, ha="left",
                va="center", linespacing=1.75)
        yy -= 0.092

    punchline(fig, "各地经办口径不完全一样，办之前打个 12393 问一句最稳。")
    footer(fig, "操作路径以国家医保服务平台 App 及各地医保小程序实际界面为准；12393 为多数地区医保服务热线｜制图：本文")
    fig.savefig(OUT + "图3_今晚就能做的三件事.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)