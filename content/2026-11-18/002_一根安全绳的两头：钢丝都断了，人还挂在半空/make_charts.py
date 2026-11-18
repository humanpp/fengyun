# -*- coding: utf-8 -*-
"""
《一根安全绳的两头》配套图表
事实口径：2026-11-16 安徽芜湖通和世纪之光一期小区，总包单位的"蜘蛛人"在 8 楼
外墙维修漏水，5 楼住户因窗外绳子晃动，用钝器切割安全绳，尼龙绳及其内部
钢丝均被切断；工人报警 110、119 后被安全转移，未造成伤亡；律师认为或
涉嫌故意杀人罪（未遂），警方正在侦办。同类案例：2022 无锡、2024 合肥。
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


def note(ax, x, y, text, color=GRAY, fs=9.6, ha="left", va="center"):
    ax.text(x, y, text, fontsize=fs, color=color, ha=ha, va=va, linespacing=1.6)


def box(ax, x, y, w, h, text, fc, ec, tc, fs=10.4):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.012",
                                facecolor=fc, edgecolor=ec, linewidth=1.1,
                                zorder=5))
    ax.text(x + w / 2, y + h / 2, text, fontsize=fs, color=tc, ha="center",
            va="center", zorder=6, linespacing=1.55)


# ------------------------------------------------------------------ 图 1
def fig1():
    fig = base("一根绳子的两头",
               "2026 年 11 月 16 日，安徽芜湖。绳子一头在 8 楼，另一头在 5 楼")
    ax = fig.add_axes([0.045, 0.140, 0.915, 0.690])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # 楼体剖面
    ax.add_patch(Rectangle((0.045, 0.075), 0.300, 0.860, facecolor="#fafbfc",
                           edgecolor=LIGHT, linewidth=1.2, zorder=1))
    levels = [(0.845, "楼顶"), (0.700, "8 楼"), (0.420, "5 楼"), (0.075, "地面")]
    for y, label in levels:
        ax.plot([0.045, 0.345], [y, y], color=LIGHT, linewidth=0.9, zorder=2)
        ax.text(0.038, y, label, fontsize=9.6, color=GRAY, ha="right",
                va="center")

    # 8 楼外墙：待修的漏水点
    ax.add_patch(Rectangle((0.300, 0.640), 0.038, 0.055, facecolor="#f2e6d8",
                           edgecolor="#c9a06a", linewidth=1.0, zorder=3))
    note(ax, 0.372, 0.795, "工人：吊在外墙作业", color=SLATE, fs=9.2)
    note(ax, 0.372, 0.690, "8 楼外墙漏水\n工人是来修的", color="#8a6b3f", fs=9.2)

    # 安全绳：楼顶锚点 → 向下，到 5 楼下方被切断
    ax.plot([0.310, 0.310], [0.845, 0.395], color=NAVY, linewidth=2.6,
            zorder=3, solid_capstyle="round")
    ax.plot([0.310, 0.310], [0.335, 0.075], color=NAVY, linewidth=2.6,
            zorder=3, solid_capstyle="round", alpha=0.45,
            linestyle=(0, (2, 2)))
    ax.plot([0.310], [0.365], marker="X", markersize=13, color=RED,
            markeredgecolor="white", markeredgewidth=1.2, zorder=6)

    # 工人：吊在 8 楼外侧
    ax.plot([0.310, 0.360], [0.700, 0.700], color=SLATE, linewidth=1.4, zorder=4)
    ax.plot([0.360], [0.700], marker="o", markersize=9, color=SLATE,
            markeredgecolor="white", markeredgewidth=1.4, zorder=5)

    # 5 楼住户：窗内，手持钝器
    ax.add_patch(Rectangle((0.160, 0.430), 0.090, 0.060, facecolor="#eef0f3",
                           edgecolor=GRAY, linewidth=1.0, zorder=3))
    note(ax, 0.205, 0.460, "住户", color=SLATE, fs=9.0, ha="center")
    ax.annotate("", xy=(0.300, 0.400), xytext=(0.250, 0.450),
                arrowprops=dict(arrowstyle="-|>", color=RED, linewidth=1.4,
                                shrinkA=0, shrinkB=0))
    note(ax, 0.130, 0.352, "5 楼住户：嫌绳子在窗外晃\n用钝器切割", color=RED, fs=9.4)

    # 切断说明
    note(ax, 0.345, 0.352, "尼龙绳割开，里面的钢丝也断了", color=RED, fs=9.8)
    note(ax, 0.345, 0.300, "不是碰了一下：需要持续用力", color=SLATE, fs=9.2)

    # 地面救援
    ax.plot([0.120, 0.200], [0.100, 0.100], color=RED, linewidth=3.0,
            solid_capstyle="round", zorder=4)
    note(ax, 0.215, 0.100, "公安、消防到场\n工人被安全转移至楼下，未造成伤亡",
         color=DARK, fs=9.4)

    # 右侧：两头对照
    box(ax, 0.555, 0.610, 0.400, 0.150,
        "一头：8 楼\n漏水要修，工人是来解决问题的", "#eaf0ea", GREEN, DARK,
        fs=10.4)
    box(ax, 0.555, 0.400, 0.400, 0.150,
        "另一头：5 楼\n绳子晃眼，住户选择动手", "#f7e9e7", RED, DARK, fs=10.4)
    note(ax, 0.555, 0.330, "同一根绳，两种处理方式：\n一个在修，一个在割",
         color=SLATE, fs=9.8)

    ax.annotate("", xy=(0.545, 0.560), xytext=(0.395, 0.560),
                arrowprops=dict(arrowstyle="-|>", color=GRAY, linewidth=1.2,
                                linestyle=(0, (4, 3)), shrinkA=0, shrinkB=0))
    note(ax, 0.470, 0.588, "同一根绳", color=SLATE, fs=9.2, ha="center")

    punchline(fig, "割断的不是一根绳子，是一个还挂在上面的人。")
    footer(fig, "事实：极目新闻、凤凰网、新浪新闻等公开报道（2026-11-16 起）｜示意图，非现场比例｜制图：本文")
    fig.savefig(OUT + "图1_一根绳子的两头.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("钢丝断了，说明什么",
               "安全绳不是一根绳：尼龙在外，钢丝在内。两样都断，才叫切断")
    ax = fig.add_axes([0.045, 0.140, 0.915, 0.690])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # 左：绳的结构
    ax.add_patch(FancyBboxPatch((0.060, 0.180), 0.360, 0.640,
                                boxstyle="round,pad=0.012", facecolor="#fafbfc",
                                edgecolor=LIGHT, linewidth=1.1))
    note(ax, 0.085, 0.760, "一根安全绳的结构", color=DARK, fs=11.6)
    # 外层尼龙
    ax.add_patch(Rectangle((0.120, 0.300), 0.230, 0.375, facecolor="#e6ece5",
                           edgecolor=GREEN, linewidth=1.2, alpha=0.85, zorder=2))
    # 内层钢丝
    for i in range(6):
        x = 0.148 + i * 0.034
        ax.plot([x, x], [0.315, 0.660], color=GRAY, linewidth=1.6, zorder=3)
    note(ax, 0.100, 0.255, "外层：尼龙编织护套", color=GREEN, fs=9.4)
    note(ax, 0.100, 0.210, "内层：钢丝绳芯", color=SLATE, fs=9.4)
    ax.plot([0.235, 0.235], [0.700, 0.750], color=RED, linewidth=2.4,
            solid_capstyle="round", zorder=5)
    note(ax, 0.250, 0.735, "钝器切割位置", color=RED, fs=9.4)

    # 右：三层判断
    rows = [
        ("① 物理上", "尼龙护套被割开，钢丝绳芯被切断。\n安全绳的承载主体已经失效。"),
        ("② 行为上", "钝器、持续用力、在 5 楼窗口操作——\n这不是「碰了一下」。"),
        ("③ 法律上", "律师意见：或涉嫌故意杀人罪（未遂）。\n警方正在侦办，定性以侦查结论为准。"),
    ]
    yy = 0.765
    for head, body in rows:
        ax.text(0.480, yy, head, fontsize=11.6, color=RED, weight="bold",
                ha="left", va="center")
        ax.text(0.480, yy - 0.075, body, fontsize=10.2, color=DARK, ha="left",
                va="center", linespacing=1.75)
        yy -= 0.195

    ax.plot([0.480, 0.940], [0.245, 0.245], color=LIGHT, linewidth=1.0)
    note(ax, 0.480, 0.155, "绳子那头没有人，只是一根绳；\n绳子这头有一个人，正在上面干活。",
         color=SLATE, fs=10.0)

    punchline(fig, "判定的关键不是「断没断」，是「知不知道会断」。")
    footer(fig, "结构示意见行业通识，非本案物证；法律表述引自公开报道中律师意见｜制图：本文")
    fig.savefig(OUT + "图2_钢丝断了说明什么.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("第三次了",
               "同类事件在公开报道里至少出现过三次，处理结果值得放在一起看")
    ax = fig.add_axes([0.045, 0.140, 0.915, 0.690])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    header = ["时间", "地点", "经过", "结果"]
    xs = [0.050, 0.190, 0.475, 0.790]
    for x, h in zip(xs, header):
        ax.text(x, 0.790, h, fontsize=10.8, color=GRAY, weight="bold",
                ha="left", va="center")
    ax.plot([0.045, 0.955], [0.760, 0.760], color=LIGHT, linewidth=1.0)

    rows = [
        ("2022-06", "江苏无锡", "工人午休，绳子空挂；\n4 楼住户认为有隐患，割断", "工人被消防救下"),
        ("2024-09", "安徽合肥", "9 楼住户不满外墙维修弄脏窗户，\n持刀切割绳索，被制止", "警方立案办理"),
        ("2026-11", "安徽芜湖", "5 楼住户嫌绳子晃动，钝器切割；\n尼龙与钢丝均断", "警方侦办中"),
    ]
    yy = 0.690
    for i, (t, loc, how, res) in enumerate(rows):
        if i == 2:
            ax.add_patch(Rectangle((0.040, yy - 0.085), 0.920, 0.140,
                                   facecolor="#fbf3f1", edgecolor="none",
                                   zorder=1))
        ax.text(xs[0], yy, t, fontsize=10.4, color=DARK, ha="left", va="center")
        ax.text(xs[1], yy, loc, fontsize=10.4, color=DARK, ha="left",
                va="center")
        ax.text(xs[2], yy, how, fontsize=9.8, color=DARK, ha="left",
                va="center", linespacing=1.6)
        ax.text(xs[3], yy, res, fontsize=10.0,
                color=RED if i == 2 else SLATE, ha="left", va="center")
        yy -= 0.145

    ax.plot([0.045, 0.955], [0.330, 0.330], color=LIGHT, linewidth=1.0)
    note(ax, 0.050, 0.235,
         "三次里，绳子都被割断了；两次里，割绳的人都被找到了。\n"
         "真正该被追问的是：为什么还会有人觉得，割一根挂着人的绳子，是个选项？",
         color=SLATE, fs=10.2)

    punchline(fig, "同一件事发生第三次，就不能只当成「奇闻」了。")
    footer(fig, "2022 无锡、2024 合肥案例据公开报道整理；2026 芜湖案警方正在侦办，结果未定｜制图：本文")
    fig.savefig(OUT + "图3_第三次了.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)
