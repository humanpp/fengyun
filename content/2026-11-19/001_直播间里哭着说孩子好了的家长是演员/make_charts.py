# -*- coding: utf-8 -*-
"""
《直播间里哭着说“孩子好了”的家长，是演员》配套图表
事实口径（2026-11-18 多家媒体暗访曝光）：
  · 直播间里哭着称“我娃以前也这样，学了课就好了”的“家长”为同一批演员，
    衣服不换，在几个直播间来回演；
  · 演员演完焦虑后主播上场，以“有你这样的父母，神仙也救不了你孩子”
    等话术放大愧疚，再行报价；
  · 低价课只是钩子，拉进私域群后，线下“父母觉醒营”逐个推销
    3.98 万元“私密课堂”；
  · 机构合同写明：不许对外说，不许投诉，不许曝光，否则赔违约金；
  · 江苏邓女士：丈夫车祸去世后儿子受打击不再出门，她先后在 3 家机构
    花费近 10 万元，孩子无好转；发视频讲述后，两家机构以“侵害名誉、
    违反合同”申请仲裁，她被裁定赔偿（金额未披露）；
  · 湖北残疾母亲胡女士：交费 2.7 万元，孩子抑郁症复发；发帖维权后
    被机构仲裁，判赔 9000 元。
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
    fig = base("一场直播，四步把你推到报价前",
               "演员连麦 · 主播定罪 · 低价课引流 · 3.98 万私密课堂")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    steps = [
        ("① 连麦", "家长讲自己的崩溃",
         "厌学、不出门、不说话。\n这份焦虑是真的，也正是\n他们要找的入口。"),
        ("② 接话", "另一个“家长”哭着说",
         "“我娃以前也这样，\n学了课就好了。”同一批\n演员，衣服都不换。"),
        ("③ 定罪", "主播上场，先骂家长",
         "“有你这样的父母，\n神仙也救不了你孩子。”\n不给答案，只给愧疚。"),
        ("④ 报价", "低价课引流，3.98 万收口",
         "低价课拉进私域群，\n线下“父母觉醒营”烧热\n气氛，逐个推销。"),
    ]

    xs = [0.016, 0.250, 0.484, 0.718]
    w, top, h = 0.210, 0.860, 0.480
    for i, (tag, head, body) in enumerate(steps):
        ax.add_patch(FancyBboxPatch((xs[i], top - h), w, h,
                                    boxstyle="round,pad=0.010",
                                    facecolor="#fafbfc", edgecolor=LIGHT,
                                    linewidth=1.0))
        ax.text(xs[i] + 0.016, top - 0.052, tag, fontsize=10.2, color=RED,
                weight="bold", ha="left", va="top")
        ax.text(xs[i] + 0.016, top - 0.118, head, fontsize=10.6, color=DARK,
                weight="bold", ha="left", va="top")
        ax.text(xs[i] + 0.016, top - 0.190, body, fontsize=8.7, color=SLATE,
                ha="left", va="top", linespacing=1.85)

        if i < len(steps) - 1:
            ax.annotate("",
                        xy=(xs[i + 1] - 0.004, top - h / 2),
                        xytext=(xs[i] + w + 0.004, top - h / 2),
                        arrowprops=dict(arrowstyle="-|>", color=GRAY,
                                        lw=1.2, shrinkA=0, shrinkB=0))

    ax.plot([0.016, 0.958], [0.300, 0.300], color=LIGHT, linewidth=1.0)
    ax.text(0.500, 0.234,
            "“演员”不是失误，是流程的一部分。",
            fontsize=10.2, color=NAVY, ha="center", va="center")
    ax.text(0.500, 0.170,
            "一句“有你这样的父母”，把家长从“来听课的人”变成“欠孩子的人”。",
            fontsize=9.2, color=SLATE, ha="center", va="center")

    punchline(fig, "真正被卖掉的不是课，是家长最无助的那一分钟。")
    footer(fig, "事实：据 2026-11-18 多家媒体暗访报道；价格与合同条款均引自报道｜制图：本文")
    fig.savefig(OUT + "图1_一场直播的四步剧本.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("合同里最贵的一行字：不许喊疼",
               "3.98 万元的“私密课堂”，附一份封口协议")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # 左：合同节选
    ax.add_patch(FancyBboxPatch((0.020, 0.120), 0.500, 0.780,
                                boxstyle="round,pad=0.012",
                                facecolor=SAND, edgecolor="#d9cdb6",
                                linewidth=1.0))
    ax.text(0.046, 0.860, "家庭教育服务合同（节选）", fontsize=10.6,
            color="#7a6746", weight="bold", ha="left", va="center")
    ax.plot([0.046, 0.494], [0.820, 0.820], color="#d9cdb6", linewidth=1.0)

    clauses = [
        ("一", "不得对外披露课程内容、服务细节"),
        ("二", "不得向任何平台投诉、举报"),
        ("三", "不得公开曝光机构及其服务"),
    ]
    yy = 0.700
    for num, text in clauses:
        ax.text(0.046, yy, num, fontsize=10.0, color=RED, weight="bold",
                ha="left", va="center")
        ax.text(0.086, yy, text, fontsize=9.6, color=DARK, ha="left",
                va="center")
        ax.text(0.474, yy, "违约即赔", fontsize=9.0, color=RED, weight="bold",
                ha="right", va="center")
        ax.plot([0.046, 0.494], [yy - 0.058, yy - 0.058], color="#e2d7c4",
                linewidth=0.8)
        yy -= 0.130

    ax.text(0.046, 0.350, "合同由机构单方提供，签字前不看这一页的人很多。",
            fontsize=8.8, color="#8a7a5e", ha="left", va="center")
    ax.text(0.046, 0.286,
            "出事之后，条款反过来成了索赔依据。",
            fontsize=8.8, color="#8a7a5e", ha="left", va="center")

    # 右：报价与链条
    ax.plot([0.560, 0.560], [0.160, 0.860], color=LIGHT, linewidth=1.0,
            linestyle=(0, (4, 4)))

    ax.text(0.610, 0.760, "3.98 万", fontsize=42, color=RED, weight="bold",
            ha="left", va="center")
    ax.text(0.612, 0.682, "“私密课堂”报价", fontsize=10.4, color=DARK,
            ha="left", va="center")

    ax.text(0.610, 0.600, "低价课 → 私域群 → 线下营 → 3.98 万",
            fontsize=9.4, color=SLATE, ha="left", va="center")

    ax.text(0.610, 0.495, "低价课只是钩子。", fontsize=9.4, color=DARK,
            weight="bold", ha="left", va="center")
    ax.text(0.610, 0.440,
            "把人拉进私域群，线下的“父母觉醒营”\n"
            "把气氛烧到最热，结尾再逐个推销。",
            fontsize=9.0, color=SLATE, ha="left", va="top", linespacing=1.85)

    punchline(fig, "你掏钱买课，也买走了自己说话的权利。")
    footer(fig, "事实：据 2026-11-18 多家媒体暗访报道及受访家长提供的合同；条款为合同原文意思｜制图：本文")
    fig.savefig(OUT + "图2_合同里的三个不许.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("钱花出去了，孩子没好，人先成了被告",
               "两位家长的账：近 10 万元，和 2.7 万元")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    cards = [
        ("江苏 · 邓女士", "近 10 万", "先后走进 3 家机构",
         ["丈夫车祸去世，儿子不再出门",
          "孩子没有好转",
          "她发视频讲述经历",
          "两家机构以“侵害名誉、\n违反合同”申请仲裁，她被裁定赔偿"]),
        ("湖北 · 胡女士（残疾母亲）", "2.7 万", "交费金额",
         ["孩子抑郁症复发",
          "她发帖维权",
          "被机构申请仲裁",
          "判赔 9000 元"]),
    ]

    xs = [0.020, 0.510]
    w, top, h = 0.470, 0.860, 0.780
    for i, (name, amount, amount_note, rows) in enumerate(cards):
        face = "#fbf3f1" if i == 0 else "#fafbfc"
        ax.add_patch(FancyBboxPatch((xs[i], top - h), w, h,
                                    boxstyle="round,pad=0.012",
                                    facecolor=face, edgecolor=LIGHT,
                                    linewidth=1.0))
        ax.text(xs[i] + 0.028, top - 0.048, name, fontsize=10.6, color=NAVY,
                weight="bold", ha="left", va="top")
        ax.text(xs[i] + 0.028, top - 0.155, amount, fontsize=32, color=RED,
                weight="bold", ha="left", va="center")
        ax.text(xs[i] + 0.028, top - 0.232, amount_note, fontsize=8.8,
                color=GRAY, ha="left", va="center")
        ax.plot([xs[i] + 0.028, xs[i] + w - 0.028],
                [top - 0.270, top - 0.270], color=LIGHT, linewidth=0.9)

        yy = top - 0.330
        for row in rows:
            ax.plot([xs[i] + 0.034], [yy + 0.006], marker="s", markersize=4.6,
                    color=RED if i == 0 else SLATE, zorder=3)
            ax.text(xs[i] + 0.056, yy, row, fontsize=9.0, color=SLATE,
                    ha="left", va="top", linespacing=1.75)
            yy -= 0.125 if "\n" in row else 0.085

    ax.plot([0.500, 0.500], [0.080, 0.860], color=LIGHT, linewidth=1.0,
            linestyle=(0, (4, 4)))
    punchline(fig, "交钱时是为了孩子，开口时成了违约。")
    footer(fig, "事实：据 2026-11-18 多家媒体报道中两位受访家长的遭遇；邓女士被裁定赔偿金额未披露｜制图：本文")
    fig.savefig(OUT + "图3_两个花过钱的人.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)
