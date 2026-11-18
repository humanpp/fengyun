# -*- coding: utf-8 -*-
"""
《两杯咖啡，一个被取消的面试》配套图表
事实口径：2026-11-13 江苏昆山，求职者跨城面试，到场后 HR 要求其点两杯饮品
（一杯不含咖啡因）并明确不报销；求职者拒绝后 HR 改口可报销，随即以
"公司不招斤斤计较的员工"取消面试；11-14 平台回应暂停该招聘账号权限；
11-16 记者向平台客服求证确认，该公司在平台已无法搜索。
风格：克制传媒风，白底、低饱和配色、标题即结论。输出目录 = 脚本所在目录。
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False

NAVY = "#1f3a5f"
RED = "#b5544a"
GRAY = "#8a8f98"
SLATE = "#5f6673"
LIGHT = "#d8dbe0"
DARK = "#2b2f36"
PALE = "#eef0f3"

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


def box(ax, x, y, w, h, text, fc, ec, tc, fs=10.4, bold=False):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.012",
                                facecolor=fc, edgecolor=ec, linewidth=1.1,
                                zorder=2))
    ax.text(x + w / 2, y + h / 2, text, fontsize=fs, color=tc,
            weight="bold" if bold else "normal", ha="center", va="center",
            zorder=3, linespacing=1.55)


# ------------------------------------------------------------------ 图 1
def fig1():
    fig = base("从跨城到取消：一条时间线",
               "2026 年 11 月 13 日，江苏昆山。见面之前，面试就结束了")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    y = 0.745
    ax.plot([0.030, 0.970], [y, y], color=LIGHT, linewidth=2.8,
            solid_capstyle="round", zorder=1)

    nodes = [
        (0.080, "① 出发", "跨城赴约\n路费自理、时间自担", NAVY),
        (0.300, "② 到场", "人还没见到\n消息先到了", SLATE),
        (0.520, "③ 被要求", "点两杯喝的，一杯不含咖啡因\n且「不报销」", RED),
        (0.740, "④ 拒绝", "拒绝垫钱后 HR 改口\n「可以报销」，随即倒打一耙", RED),
        (0.930, "⑤ 取消", "面试当场取消\n没见到面试官", RED),
    ]
    for x, head, body, color in nodes:
        ax.plot([x], [y], marker="o", markersize=11, color=color,
                markeredgecolor="white", markeredgewidth=1.8, zorder=4)
        ax.text(x, y + 0.085, head, fontsize=12.6, color=color, weight="bold",
                ha="center", va="bottom")
        ax.text(x, y - 0.100, "13 日", fontsize=9.2, color=GRAY, ha="center",
                va="top")
        ax.text(x, y - 0.195, body, fontsize=9.8, color=DARK, ha="center",
                va="top", linespacing=1.6)

    ax.plot([0.030, 0.970], [0.355, 0.355], color=LIGHT, linewidth=1.0)
    ax.text(0.500, 0.290,
            "顺序是关键：先拒绝，后改口，再取消——不是不肯报销，是不肯被拒绝",
            fontsize=10.6, color=SLATE, ha="center", va="center")

    ax.text(0.030, 0.200, "11-14　平台回应：暂停该招聘账号权限，要求其学习规则",
            fontsize=10.6, color=DARK, ha="left", va="center")
    ax.text(0.030, 0.125, "11-16　记者求证确认：该公司在平台已无法搜索",
            fontsize=10.6, color=DARK, ha="left", va="center")

    punchline(fig, "一杯咖啡没买成，一个人的面试资格被取消了。")
    footer(fig, "事实：素材与公开报道（澎湃、扬子晚报、新浪财经、界面新闻）｜制图：本文")
    fig.savefig(OUT + "图1_从跨城到取消.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("这笔账，谁在付",
               "两杯饮品的价钱很小，先付钱的那一方不是求职者的义务")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(0.060, 0.865, "求职者：已经付了的", fontsize=12.5, color=NAVY,
            weight="bold", ha="left", va="center")
    ax.text(0.545, 0.865, "招聘方：被要求付的", fontsize=12.5, color=RED,
            weight="bold", ha="left", va="center")

    rows_left = [
        ("跨城往返路费", "自付；按常见跨城面试估算 100–300 元"),
        ("路上的时间", "单程 1–3 小时，请假或调休另计"),
        ("被要求的饮品", "约 30–60 元（两杯，实际未付）"),
        ("给不给的答复", "拒绝——这是她的权利"),
    ]
    yy = 0.755
    for name, note in rows_left:
        ax.plot([0.058], [yy], marker="s", markersize=7, color=NAVY, zorder=3)
        ax.text(0.085, yy, name, fontsize=11.2, color=DARK, weight="bold",
                ha="left", va="center")
        ax.text(0.085, yy - 0.058, note, fontsize=9.4, color=GRAY,
                ha="left", va="center")
        yy -= 0.152

    box(ax, 0.545, 0.615, 0.400, 0.210,
        "0 元\n\n出了一条消息：\n「你先点两杯喝的，我要不带咖啡因的」",
        "#f7e9e7", RED, DARK, fs=10.4)
    box(ax, 0.545, 0.370, 0.400, 0.200,
        "0 元\n\n面试取消，没有补偿\n路费、时间，一概不认",
        "#f7e9e7", RED, DARK, fs=10.4)
    ax.text(0.545, 0.285, "11-14 平台暂停其招聘权限　｜　11-16 该公司在平台已搜不到",
            fontsize=9.6, color=GRAY, ha="left", va="center")

    ax.annotate("", xy=(0.535, 0.700), xytext=(0.420, 0.700),
                arrowprops=dict(arrowstyle="-|>", color=GRAY, linewidth=1.2,
                                linestyle=(0, (4, 3)), shrinkA=0, shrinkB=0))
    ax.text(0.478, 0.728, "成本转移", fontsize=9.6, color=SLATE,
            ha="center", va="center")

    punchline(fig, "要求垫钱的那一刻，风险就从公司挪到了求职者身上。")
    footer(fig, "路费与饮品价为本市常见区间的估算，非当事人披露数字｜制图：本文")
    fig.savefig(OUT + "图2_这笔账谁在付.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("一道服从性测试",
               "「不招斤斤计较的员工」这句话，翻译过来是什么")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    box(ax, 0.150, 0.815, 0.700, 0.115,
        "见面之前，先来一个与岗位无关的私人要求",
        PALE, LIGHT, DARK, fs=11.8)

    ax.plot([0.500, 0.500], [0.800, 0.740], color=GRAY, linewidth=1.2)
    ax.plot([0.215, 0.785], [0.740, 0.740], color=GRAY, linewidth=1.2)
    ax.annotate("", xy=(0.215, 0.690), xytext=(0.215, 0.740),
                arrowprops=dict(arrowstyle="-|>", color=NAVY, linewidth=1.2))
    ax.annotate("", xy=(0.785, 0.690), xytext=(0.785, 0.740),
                arrowprops=dict(arrowstyle="-|>", color=RED, linewidth=1.2))

    box(ax, 0.060, 0.560, 0.310, 0.120, "答应了\n面试继续", "#eaf0ea", NAVY,
        DARK, fs=11.4)
    box(ax, 0.630, 0.560, 0.310, 0.120, "拒绝了\n「斤斤计较」", "#f7e9e7", RED,
        DARK, fs=11.4)

    ax.text(0.215, 0.500, "被要求的是配合度，不是专业能力", fontsize=9.8,
            color=SLATE, ha="center", va="top")
    ax.text(0.785, 0.500, "拒绝被重新命名为「态度问题」", fontsize=9.8,
            color=SLATE, ha="center", va="top")

    ax.plot([0.045, 0.955], [0.430, 0.430], color=LIGHT, linewidth=1.0)

    items = [
        ("于情", "路费自理、时间自担，跨城赶来本身就是诚意；被拒后当场翻脸，凉的是人心。"),
        ("于理", "招聘考的是能力与岗位的匹配度。用一杯咖啡定去留，是把考察换成了服从。"),
        ("于法", "《劳动合同法》第九条：招用劳动者，不得以其他名义向劳动者收取财物。金额小，性质不变。"),
    ]
    yy = 0.355
    for head, body in items:
        ax.text(0.055, yy, head, fontsize=10.8, color=RED, weight="bold",
                ha="left", va="center")
        ax.text(0.145, yy, body, fontsize=10.2, color=DARK, ha="left",
                va="center")
        yy -= 0.075

    ax.text(0.055, 0.120,
            "面试是双向打分：企业看能力，求职者也在看这家公司怎么对待人。",
            fontsize=10.6, color=SLATE, ha="left", va="center")

    punchline(fig, "一杯咖啡不报销叫「不计较」，那什么才叫计较？")
    footer(fig, "法条：《劳动合同法》第九条（界面新闻快评亦援引）；「于情/于理/于法」框架借自该快评，表述为本刊重写｜制图：本文")
    fig.savefig(OUT + "图3_一道服从性测试.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)
