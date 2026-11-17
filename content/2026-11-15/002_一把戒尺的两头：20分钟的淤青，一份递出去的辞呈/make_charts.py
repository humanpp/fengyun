# -*- coding: utf-8 -*-
"""
《一把戒尺，两头都是伤口》配套图表
事实来源：《中小学教育惩戒规则（试行）》（教育部令第 49 号，2021-03-01 施行）
第十二条原文（中国政府网）；贵州仁怀、湖南两起事件的公开报道
风格：克制传媒风，白底、低饱和配色、标题即结论
输出目录 = 脚本所在目录
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["figure.facecolor"] = "white"
plt.rcParams["axes.facecolor"] = "white"

NAVY = "#1f3a5f"
RED = "#b5544a"
GRAY = "#8a8f98"
LIGHT = "#d8dbe0"
DARK = "#2b2f36"
PALE = "#eef0f3"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep


def footer(fig, text):
    fig.text(0.045, 0.020, text, fontsize=8.4, color=GRAY, ha="left", va="bottom")


def takeaway(fig, y, text, size=10.4):
    fig.text(0.045, y, text, fontsize=size, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


# ---------------------------------------------------------------- 图 1
def fig1():
    fig, ax = plt.subplots(figsize=(12, 6.8))
    fig.subplots_adjust(left=0.045, right=0.955, top=0.765, bottom=0.170)

    fig.suptitle("规则早就写清了：能做什么，不能做什么",
                 fontsize=19, color=DARK, x=0.045, ha="left", y=0.955, weight="bold")
    fig.text(0.045, 0.888,
             "《中小学教育惩戒规则（试行）》第八条 与 第十二条第一项（2021 年 3 月 1 日施行）",
             fontsize=10.6, color=GRAY, ha="left")

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 5.05)
    ax.axis("off")

    ax.text(0.020, 4.82, "规则允许的惩戒（第八条）", fontsize=12.2, color=NAVY,
            weight="bold", va="center")
    allowed = ["点名批评", "责令赔礼道歉、做口头或书面检讨",
               "适当增加公益服务任务", "一节课堂教学时间内的教室内站立",
               "课后教导", "校规校纪规定的其他适当措施"]
    for i, item in enumerate(allowed):
        y = 4.18 - i * 0.66
        ax.add_patch(plt.Rectangle((0.020, y - 0.235), 0.020, 0.47,
                                   facecolor=NAVY, edgecolor="none", alpha=0.85))
        ax.text(0.058, y, item, fontsize=11, color=DARK, va="center")

    ax.text(0.545, 4.82, "明令禁止（第十二条第一项）", fontsize=12.2, color=RED,
            weight="bold", va="center")
    ax.add_patch(plt.Rectangle((0.545, 3.05), 0.430, 1.36,
                               facecolor="#f6ecea", edgecolor=RED, linewidth=1.4))
    ax.text(0.760, 4.00, "以击打、刺扎等方式", fontsize=13.5, color=RED,
            weight="bold", ha="center", va="center")
    ax.text(0.760, 3.62, "直接造成身体痛苦的体罚", fontsize=13.5, color=RED,
            weight="bold", ha="center", va="center")
    ax.text(0.760, 3.24, "——不设例外，不设“情节严重才禁止”",
            fontsize=10.2, color=GRAY, ha="center", va="center")

    ax.text(0.545, 2.62, "同一部规则第十二条，还一并禁止：", fontsize=10.6,
            color=DARK, va="center")
    others = ["超过正常限度的罚站、反复抄写", "辱骂或侮辱学生人格尊严",
              "因学业成绩而惩戒学生", "因个人情绪、好恶实施惩戒"]
    for i, item in enumerate(others):
        y = 2.28 - i * 0.42
        ax.text(0.560, y, "· " + item, fontsize=10, color=GRAY, va="center")

    takeaway(fig, 0.080, "仁怀这起事件里，尺子落下的第一下就已经在线外——与打了多久无关。")

    footer(fig, "原文：中国政府网《中小学教育惩戒规则（试行）》（教育部令第 49 号）。")
    fig.savefig(OUT + "图1_规则清单.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig, ax = plt.subplots(figsize=(12, 6.8))
    fig.subplots_adjust(left=0.045, right=0.955, top=0.790, bottom=0.115)

    fig.suptitle("同一把尺子，两头各自走向极端",
                 fontsize=19, color=DARK, x=0.045, ha="left", y=0.955, weight="bold")
    fig.text(0.045, 0.888,
             "一头是 8 岁女孩的淤青，一头是 50 多岁班主任递出的辞呈",
             fontsize=10.8, color=GRAY, ha="left")

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 4.20)
    ax.axis("off")

    ax.plot([0.5, 0.5], [0.42, 4.12], color=LIGHT, lw=2.0, zorder=1)

    panels = [
        (0.030, "极少数：打服", RED, [
            "把“管教”理解成“压住”",
            "不信规则管得住，就拿起尺子",
            "尺子一拿，20 分钟和 2 分钟没有界线",
            "最后只剩情绪",
        ]),
        (0.530, "大多数：少管一点", NAVY, [
            "怕投诉、怕被认定成体罚",
            "怕一次冲突变成一场舆情",
            "“把戒尺还给老师”喊了几年",
            "纸面权利 ≠ 现实底气",
        ]),
    ]

    for x0, title, color, lines in panels:
        ax.add_patch(plt.Rectangle((x0, 1.95), 0.440, 2.15,
                                   facecolor=PALE, edgecolor=LIGHT, linewidth=1.0))
        ax.add_patch(plt.Rectangle((x0, 3.98), 0.440, 0.12,
                                   facecolor=color, edgecolor="none"))
        ax.text(x0 + 0.030, 3.66, title, fontsize=13.5, color=color,
                weight="bold", va="center")
        for i, ln in enumerate(lines):
            ax.text(x0 + 0.030, 3.20 - i * 0.36, ln, fontsize=10.6,
                    color=DARK, va="center")

    ax.add_patch(plt.Rectangle((0.115, 0.35), 0.770, 1.35,
                               facecolor="white", edgecolor=DARK, linewidth=1.2))
    ax.text(0.500, 1.28, "禁止的部分很清楚，允许的部分很单薄，支撑的部分几乎没有",
            fontsize=13, color=DARK, ha="center", va="center", weight="bold")
    ax.text(0.500, 0.72, "于是“管”与“不管”之间，没有中间档位可站",
            fontsize=11, color=GRAY, ha="center", va="center")

    footer(fig, "据《中小学教育惩戒规则（试行）》及仁怀、湖南两起事件的公开报道整理。")
    fig.savefig(OUT + "图2_两头.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig, ax = plt.subplots(figsize=(12, 6.8))
    fig.subplots_adjust(left=0.045, right=0.955, top=0.790, bottom=0.100)

    fig.suptitle("三段边界，缺的是最后一段",
                 fontsize=19, color=DARK, x=0.045, ha="left", y=0.955, weight="bold")
    fig.text(0.045, 0.888,
             "戒尺该不该存在不是真问题；物理、程序、兜底，三处都得有人兜住",
             fontsize=10.8, color=GRAY, ha="left")

    ax.set_xlim(0, 1)
    ax.set_ylim(-0.28, 4.45)
    ax.axis("off")

    rows = [
        ("物理边界", "打，不行", NAVY,
         "手、尺子、教鞭、书本——任何落到身上的东西都在线外。这条规则已写死，无需再议。",
         "有"),
        ("程序边界", "惩戒要发生在能被看见的地方", NAVY,
         "仁怀最刺人的不是“20 分钟”，是“办公室没有监控”：无第三方、无记录，事后只能靠三方说法互相印证。",
         "缺"),
        ("兜底边界", "老师被投诉，谁来查、谁来还他清白", RED,
         "规则第十五条写了“教师无过错的不得给予处分”，但落到一所具体学校、一位具体班主任，能不能兑现是另一回事。",
         "最缺"),
    ]

    for i, (title, core, color, body, status) in enumerate(rows):
        y = 3.95 - i * 1.50
        ax.add_patch(plt.Rectangle((0.020, y - 1.15), 0.960, 1.45,
                                   facecolor=PALE, edgecolor=LIGHT, linewidth=1.0))
        ax.add_patch(plt.Rectangle((0.020, y - 1.15), 0.008, 1.45,
                                   facecolor=color, edgecolor="none"))
        ax.text(0.052, y + 0.10, title, fontsize=13.5, color=color,
                weight="bold", va="center")
        ax.text(0.052, y - 0.30, core, fontsize=11, color=DARK, va="center")
        ax.text(0.052, y - 0.76, body, fontsize=9.6, color=GRAY, va="center")
        ax.text(0.950, y + 0.10, status, fontsize=13, color=color,
                weight="bold", ha="right", va="center",
                bbox=dict(boxstyle="round,pad=0.45", facecolor="white",
                          edgecolor=color, linewidth=1.2))

    footer(fig, "据《中小学教育惩戒规则（试行）》第十二条、第十五条，及仁怀、湖南两起事件公开报道。")
    fig.savefig(OUT + "图3_三条边界.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")
