# -*- coding: utf-8 -*-
"""
《美财长要英伟达去外面找 CEO，还给了 10 天：这不是人事问题》配套图表
事实来源：2026-11-11 深夜英伟达董事会讨论黄仁勋去留、盘后跌超 8%；
11-12 董事会宣布其辞职即时生效、临时负责人接掌；11-15 贝森特在福克斯
《周日早间展望》要求外部 CEO、限 10 天解释出口管制合规；同日 FT 报道
黄仁勋筹谋复职、盟友组建"战情室"、联署超 10 万
风格：克制传媒风，白底、低饱和配色、标题即结论
输出目录 = 脚本所在目录
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch

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

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep


def footer(fig, text):
    fig.text(0.045, 0.020, text, fontsize=8.4, color=GRAY, ha="left", va="bottom")


def punchline(fig, text):
    fig.text(0.045, 0.072, text, fontsize=10.4, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


# ---------------------------------------------------------------- 图 1
def fig1():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.135, 0.930, 0.680])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "十天倒计时：从辞职到施压", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.882, "四天里发生的事，决定了 11 月 25 日要交什么",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    nodes = [
        (0.125, "11 月 11 日 深夜", "董事会连夜开会", SLATE,
         "讨论黄仁勋去留\n消息传出股价\n盘后跌超 8%"),
        (0.370, "11 月 12 日", "辞职即时生效", NAVY,
         "辞去 CEO 与\n共同创办人职务\n临时负责人接掌"),
        (0.615, "11 月 15 日", "施压与回归同天", RED,
         "贝森特要求\n从外部选新 CEO\nFT：其在筹谋复职"),
        (0.860, "11 月 25 日前后", "十天期限到期", NAVY,
         "董事会与外部律所\n须解释出口管制\n合规问题"),
    ]

    ax.plot([0.058, 0.942], [0.720, 0.720], color=LIGHT, linewidth=2.6,
            solid_capstyle="round", zorder=1)

    bw, bh, by = 0.208, 0.262, 0.150
    for x, date, title, color, body in nodes:
        ax.scatter([x], [0.720], s=200, facecolor=color, edgecolor="white",
                   linewidth=2.2, zorder=3)
        ax.text(x, 0.836, title, fontsize=12.5, color=color, weight="bold",
                ha="center", va="center")
        ax.text(x, 0.780, date, fontsize=10, color=GRAY, ha="center", va="center")

        ax.plot([x, x], [0.690, by + bh], color=LIGHT, linewidth=1.4, zorder=1)
        ax.add_patch(Rectangle((x - bw / 2, by), bw, bh, facecolor=PALE,
                               edgecolor=LIGHT, linewidth=1.0, zorder=2))
        ax.add_patch(Rectangle((x - bw / 2, by + bh - 0.013), bw, 0.013,
                               facecolor=color, edgecolor="none", zorder=3))
        ax.text(x, by + bh - 0.042, body, fontsize=9.4, color=DARK,
                ha="center", va="top", linespacing=1.8, zorder=4)

    punchline(fig, "丑闻给了华盛顿一个切口，合规才是期限的内容。")
    footer(fig, "据 BBC 中文、德国之声、路透社、CNBC、《金融时报》（经《每日电讯报》转述）报道整理。")
    fig.savefig(OUT + "图1_时间线.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.135, 0.930, 0.690])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "他要什么，他质疑什么", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.882, "贝森特 11 月 15 日在福克斯《周日早间展望》上的表态",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    panels = [
        (0.012, "他要求的三件事", NAVY, [
            ("01", "新 CEO 从公司外部找", "董事会不应只在内部物色"),
            ("02", "一次「大刀阔斧」的整顿", "原话：dramatic shakeup"),
            ("03", "10 天内解释合规", "董事会与外部法律顾问共同作答"),
        ]),
        (0.508, "他质疑的三个点", RED, [
            ("01", "是否借新加坡绕开管制", "指利用空壳公司向中国输出先进芯片"),
            ("02", "是否牵涉最高管理层", "违规若成立，责任止于哪一层"),
            ("03", "自查结论是否可信", "公司称已清点每一块芯片"),
        ]),
    ]

    for x0, title, color, items in panels:
        ax.add_patch(FancyBboxPatch((x0, 0.135), 0.480, 0.640,
                                    boxstyle="round,pad=0.010,rounding_size=0.012",
                                    facecolor=PALE, edgecolor=LIGHT, linewidth=1.0))
        ax.add_patch(Rectangle((x0, 0.760), 0.480, 0.015, facecolor=color,
                               edgecolor="none"))
        ax.text(x0 + 0.022, 0.700, title, fontsize=14.5, color=color,
                weight="bold", va="center")

        for i, (no, head, sub) in enumerate(items):
            y = 0.592 - i * 0.162
            ax.text(x0 + 0.028, y, no, fontsize=11, color=GRAY, va="center")
            ax.text(x0 + 0.078, y, head, fontsize=12.2, color=DARK,
                    weight="bold", va="center")
            ax.text(x0 + 0.078, y - 0.058, sub, fontsize=9.6, color=GRAY,
                    va="center")

    ax.text(0.012, 0.062,
            "10 天从 11 月 15 日算，期限落在 11 月 25 日前后；这一期限没有法律强制力。",
            fontsize=10.6, color=DARK, ha="left", va="center")

    footer(fig, "据路透社、CNBC、法新社、半岛电视台对贝森特 2026-11-15 采访内容的报道。")
    fig.savefig(OUT + "图2_三问.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.150, 0.930, 0.680])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "三方各有诉求，谁都不肯先让", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.882, "围绕一个 CEO 职位，三种不同的目的",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    heads = [(0.185, "董事会", NAVY), (0.500, "财政部", RED), (0.815, "硅谷盟友", SLATE)]
    for x, name, color in heads:
        ax.text(x, 0.788, name, fontsize=12.5, color=color, weight="bold",
                ha="center")
    ax.plot([0.010, 0.990], [0.752, 0.752], color=LIGHT, linewidth=1.2)

    rows = [
        ("公开诉求", "选出合格的继任者", "外部 CEO + 彻底整顿", "让黄仁勋复职"),
        ("手上筹码", "决定人事与内部调查", "出口管制合规审查", "10 万+ 联署、白宫游说"),
        ("难处", "两头受压，合规待查", "无直接人事权，期限无强制力", "丑闻未清，白宫未松口"),
    ]

    for i, (label, a, b, c) in enumerate(rows):
        y = 0.640 - i * 0.180
        if i % 2 == 0:
            ax.add_patch(Rectangle((0.010, y - 0.070), 0.980, 0.140,
                                   facecolor=PALE, edgecolor="none"))
        ax.text(0.022, y, label, fontsize=10.6, color=GRAY, va="center")
        ax.text(0.185, y, a, fontsize=10.6, color=DARK, va="center", ha="center")
        ax.text(0.500, y, b, fontsize=10.6, color=DARK, va="center", ha="center")
        ax.text(0.815, y, c, fontsize=10.6, color=DARK, va="center", ha="center")

    for x in (0.345, 0.660):
        ax.plot([x, x], [0.185, 0.740], color=LIGHT, linewidth=1.0)

    ax.text(0.010, 0.085, "董事会手里的票，是这场博弈唯一真正的决定权。",
            fontsize=10.8, color=DARK, ha="left", va="center")

    footer(fig, "据路透社、CNBC、法新社、半岛电视台、《金融时报》、《每日电讯报》、BBC 中文公开报道整理。")
    fig.savefig(OUT + "图3_三方博弈.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")