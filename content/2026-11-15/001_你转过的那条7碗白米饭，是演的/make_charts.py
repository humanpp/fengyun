# -*- coding: utf-8 -*-
"""
《你转过的那条"7碗白米饭"，是演的》配套图表
事实来源：梁平区联合调查组 2026-11-12 情况通报、中新网 2026-11-13 评论、
中国青年报客户端 2026-11-12 报道、封面新闻探访、企查查工商信息、
公安部网安局及各地网警公开通报
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
    fig.subplots_adjust(left=0.045, right=0.955, top=0.760, bottom=0.175)

    fig.suptitle("一条爆款暖心视频，是五个节拍排出来的",
                 fontsize=19, color=DARK, x=0.045, ha="left", y=0.955, weight="bold")
    fig.text(0.045, 0.885,
             "6 元炒豆芽 · 7 碗白米饭 · 免费加菜 · 字条与 300 元 · 搂肩落泪",
             fontsize=10.8, color=GRAY, ha="left")

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 5.2)
    ax.axis("off")

    beats = [
        ("1", "母亲把 6 元炒豆芽全推给孩子，自己不动一筷",
         "母爱，不用一句台词", NAVY),
        ("2", "连吃 7 碗白米饭",
         "剂量掐得刚好——够惨，又像真的", RED),
        ("3", "后厨免费加菜",
         "把“旁观”变成“出手”", NAVY),
        ("4", "打包袋里的字条和 300 元现金",
         "不留名、不要还，最难被质疑的一环", NAVY),
        ("5", "两人搂肩落泪",
         "一个镜头收尾，情绪闭环", DARK),
    ]

    box_h = 0.78
    for i, (num, plot, note, color) in enumerate(beats):
        y = 4.55 - i * 1.00
        ax.add_patch(plt.Rectangle((0.015, y - box_h / 2), 0.97, box_h,
                                   facecolor=PALE, edgecolor=LIGHT,
                                   linewidth=1.0, zorder=1))
        ax.add_patch(plt.Rectangle((0.015, y - box_h / 2), 0.006, box_h,
                                   facecolor=color, edgecolor="none", zorder=3))
        ax.text(0.072, y + 0.02, num, fontsize=11.5, color="white",
                weight="bold", ha="center", va="center", zorder=5,
                bbox=dict(boxstyle="circle,pad=0.34", facecolor=color,
                          edgecolor="none"))
        ax.text(0.118, y + 0.155, plot, fontsize=12.2, color=DARK,
                weight="bold", va="center", zorder=4)
        ax.text(0.118, y - 0.155, note, fontsize=10.2, color=color,
                va="center", zorder=4)

    takeaway(fig, 0.085, "菜单是真的，店面是真的，老板娘也是真的——假的只有“这对母女走投无路”这一件事。")

    footer(fig, "情节据媒体公开还原的监控画面与官方通报整理；“五个节拍”为本文归纳。")
    fig.savefig(OUT + "图1_五个泪点节拍.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig, ax = plt.subplots(figsize=(12, 6.8))
    fig.subplots_adjust(left=0.045, right=0.955, top=0.760, bottom=0.170)

    fig.suptitle("三组对不上的说法，偏的方向都一样",
                 fontsize=19, color=DARK, x=0.045, ha="left", y=0.955, weight="bold")
    fig.text(0.045, 0.885,
             "视频里的说法 与 能查到的说法",
             fontsize=10.8, color=GRAY, ha="left")

    ax.set_xlim(0, 1)
    ax.set_ylim(-0.10, 4.15)
    ax.axis("off")

    ax.text(0.245, 3.92, "视频里的说法", fontsize=11, color=RED,
            ha="center", weight="bold")
    ax.text(0.755, 3.92, "能查到的说法", fontsize=11, color=NAVY,
            ha="center", weight="bold")
    ax.plot([0.03, 0.97], [3.68, 3.68], color=DARK, lw=1.3)

    rows = [
        ("投入千万资金救这家老店", "工商登记：资金数额 9 万元"),
        ("经营二十多年的老店", "现经营主体成立于 2016 年 1 月，约 10 年"),
        ("随口生活记录，随手拍下", "被质疑后仍称内容真实，随后通报认定摆拍"),
    ]

    yy = [2.92, 1.92, 0.92]
    for (left, right), y in zip(rows, yy):
        ax.add_patch(plt.Rectangle((0.03, y - 0.40), 0.40, 0.80,
                                   facecolor="#f3eceb", edgecolor=LIGHT,
                                   linewidth=1.0, zorder=1))
        ax.add_patch(plt.Rectangle((0.57, y - 0.40), 0.40, 0.80,
                                   facecolor=PALE, edgecolor=LIGHT,
                                   linewidth=1.0, zorder=1))
        ax.text(0.23, y, left, fontsize=11.2, color=DARK, ha="center",
                va="center", zorder=3)
        ax.text(0.77, y, right, fontsize=11.2, color=DARK, ha="center",
                va="center", zorder=3)
        ax.annotate("", xy=(0.545, y), xytext=(0.455, y),
                    arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=1.4,
                                    shrinkA=0, shrinkB=0))

    note = ("前两项可与工商登记直接对照，第三项据凤凰网、中华网等公开报道。换主体、换执照都是常事，\n"
            "单点出入不等于撒谎——但三处偏差的方向一致：都在往“更惨”“更无辜”那边偏。")
    takeaway(fig, 0.078, note, size=9.9)

    footer(fig, "数据：企查查工商信息、封面新闻与凤凰网实地探访、中国青年报客户端。")
    fig.savefig(OUT + "图2_说法对不上.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig, ax = plt.subplots(figsize=(12, 6.8))
    fig.subplots_adjust(left=0.045, right=0.955, top=0.760, bottom=0.170)

    fig.suptitle("五年，六次：这不是个例，是一条产线",
                 fontsize=19, color=DARK, x=0.045, ha="left", y=0.955, weight="bold")
    fig.text(0.045, 0.885,
             "公开报道中被认定为摆拍的“暖心视频”，2021 年至今",
             fontsize=10.8, color=GRAY, ha="left")

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 6.0)
    ax.axis("off")

    ax.plot([0.088, 0.088], [0.20, 5.55], color=LIGHT, lw=2.2, zorder=1)

    events = [
        ("2021.10", "四川凉山", "“叔叔只能这样了”，孩子被弄脏脸编身世",
         "传唤、公开道歉、删视频", GRAY),
        ("2024.10", "四川凉山", "少年“辍学在家卖苹果”，哥哥考上北大",
         "媒体调查认定摆拍", GRAY),
        ("2026.01", "全国传播", "“小女孩 50 元在学校淘到名酒”",
         "行政处罚", NAVY),
        ("2026.04", "云南丽江", "“深山救助流浪女”，雇佣人员化装",
         "三人被依法处罚", NAVY),
        ("2026.04", "贵州贵阳", "虚构“被骗境外又被解救”的反诈人设",
         "行拘 5 日、账号关停", NAVY),
        ("2026.11", "重庆梁平 / 云南鲁甸", "“7 碗白米饭”与“枕边放钱”同日被打假",
         "立案调查 / 剧本核实", RED),
    ]

    for i, (date, place, what, result, color) in enumerate(events):
        y = 5.18 - i * 0.94
        ax.add_patch(plt.Circle((0.088, y), 0.009, facecolor=color,
                                edgecolor="white", linewidth=1.6, zorder=4))
        ax.text(0.020, y, date, fontsize=11, color=color, weight="bold",
                va="center", ha="left")
        ax.text(0.125, y + 0.150, place, fontsize=11.2, color=DARK,
                weight="bold", va="center")
        ax.text(0.125, y - 0.150, what, fontsize=10.2, color=GRAY, va="center")
        ax.text(0.975, y, result, fontsize=10.2, color=color,
                va="center", ha="right")

    takeaway(fig, 0.078, "套路在升级：从“我很惨”，到“她更惨，而我是个好人”——同一种配方，只是加码。")

    footer(fig, "据公安部网安局、云南丽江网警、贵阳南明公安及央视网、中新网、新京报、中国青年报等公开报道整理。")
    fig.savefig(OUT + "图3_五年产线.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")
