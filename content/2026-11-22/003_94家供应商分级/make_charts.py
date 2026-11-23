# -*- coding: utf-8 -*-
"""
《94 家供应商、28 个 A 级：中国移动这份名单，评的不是企业》配套图表

事实口径（核到中国移动采购与招标网公示及行业报道）：
  · 2026 年 11 月，中国移动采购与招标网发布「关于中国移动 2026 年一级集采
    供应商分级结果的公示」。
  · 分级工作的原则为「面向产品、循序渐进、动态评估、公正公开、合作共赢」。
  · 公示包含 94 家供应商；其中 28 家获评 A 级产品及服务，102 家获评
    B 级产品及服务。
  · 关键口径：分级对象是「产品及服务」，不是企业本身；因此同一家企业
    可能在不同产品线上分属不同等级，故 94 家企业对应 28 + 102 = 130 个
    产品及服务条目。公示未披露具体企业名单与产品对应关系。
  据 C114 通信网 2026-11-10、通信世界网 2026-11-12、光电通信 2026-11-10、
  通信产业网 2026-11-16。

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
TEAL = "#3f6f6b"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep

Y_TITLE = 0.958
Y_SUB = 0.898
Y_PUNCH = 0.070
Y_FOOT = 0.020

Q_L = "\u300c"
Q_R = "\u300d"


def header(fig, title, sub):
    fig.text(0.045, Y_TITLE, title, fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, Y_SUB, sub, fontsize=10.6, color=GRAY,
             ha="left", va="top")


def footer(fig, text):
    fig.text(0.045, Y_FOOT, text, fontsize=7.6, color=GRAY,
             ha="left", va="bottom")


def punchline(fig, text):
    fig.text(0.045, Y_PUNCH, text, fontsize=10.4, color=DARK,
             ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


def card(ax, x, y, w, h, edge, face="white", lw=1.0, z=2):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.004,rounding_size=0.014",
        facecolor=face, edgecolor=edge, linewidth=lw, zorder=z))


def new_axes(fig):
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return ax


# ---------------------------------------------------------------- 图 1
def fig1():
    """94 / 28 / 102 三个数"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "94 家企业，130 个产品与服务条目",
           "28 个 A 级、102 个 B 级，加起来比企业数多 36")

    # 左：三个数字
    stats = [
        ("94", "家企业入选", "本次一级集采供应商分级", NAVY),
        ("28", "个 A 级", "产品及服务", RED),
        ("102", "个 B 级", "产品及服务", TEAL),
    ]
    y = 0.720
    for num, label, note, color in stats:
        ax.text(0.052, y, num, fontsize=34, color=color, weight="bold",
                ha="left", va="center")
        ax.text(0.170, y + 0.010, label, fontsize=11.4, color=DARK,
                ha="left", va="center")
        ax.text(0.170, y - 0.032, note, fontsize=8.8, color=GRAY,
                ha="left", va="center")
        y -= 0.180

    # 右：为什么加起来不等
    card(ax, 0.560, 0.330, 0.392, 0.400, NAVY, face="white", lw=1.4)
    ax.text(0.582, 0.684, "为什么 28 + 102 ≠ 94", fontsize=11.6, color=NAVY,
            weight="bold", ha="left", va="center", zorder=6)
    ax.plot([0.582, 0.930], [0.658, 0.658], color=NAVY, linewidth=0.9,
            alpha=0.35, zorder=5)
    ax.text(0.582, 0.620,
            "因为评的不是公司，\n是「产品及服务」。\n\n"
            "一家企业供三类产品，\n就可能在三个条目里各得\n"
            "一次 A 或 B 的评价。\n\n"
            "所以 130 是条目数，\n94 是主体数。",
            fontsize=9.2, color=DARK, ha="left", va="top",
            linespacing=1.75, zorder=6)

    ax.text(0.052, 0.196,
            "公示未披露具体企业名单，也未公布产品与等级的对应关系。",
            fontsize=9.2, color=SLATE, ha="left", va="center")

    punchline(fig, "把公司当单位看，这份名单会读不懂。")
    footer(fig, "事实来源：中国移动采购与招标网《关于中国移动 2026 年一级集采供应商"
                "分级结果的公示》；C114 通信网 2026-11-10")
    fig.savefig(OUT + "图1_三个数.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """A/B 的差别：从一次评级到一次激励"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "A 和 B 之间，差的不只是一个字母",
           "分级的目的写在原则第一句：建立合理的供应商激励机制")

    cols = [
        ("A 级产品及服务", "28 个", RED, [
            "公示已给出的：",
            "评为最高一档",
            "",
            "公示未给出的：",
            "该等级对应何种采购安排、",
            "何种加分或份额",
            "",
        ]),
        ("B 级产品及服务", "102 个", SLATE, [
            "公示已给出的：",
            "列入分级体系，",
            "但不在最高一档",
            "",
            "公示未给出的：",
            "与 A 级在采购中的",
            "具体差异",
            "",
        ]),
    ]

    w = 0.430
    gap = 0.042
    x = 0.045
    for name, count, color, bullets in cols:
        card(ax, x, 0.300, w, 0.440, color, lw=1.5)
        ax.text(x + 0.024, 0.694, count, fontsize=26, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(x + 0.024, 0.640, name, fontsize=11.0, color=DARK,
                ha="left", va="center", zorder=6)
        ax.plot([x + 0.024, x + w - 0.024], [0.616, 0.616], color=color,
                linewidth=0.9, alpha=0.35, zorder=5)
        y = 0.584
        for b in bullets:
            if b:
                is_label = b.startswith("公示已") or b.startswith("公示未")
                is_note = b.startswith("本图不作")
                ax.text(x + 0.024, y, b,
                        fontsize=8.4 if is_label else (7.8 if is_note else 8.8),
                        color=GRAY if (is_label or is_note) else DARK,
                        weight="bold" if is_label else "normal",
                        ha="left", va="top", zorder=6)
            y -= 0.036
        x += w + gap

    ax.text(0.045, 0.248,
            "左侧两栏只复述公示内容；等级对应的采购安排与份额差异，公示未披露，本图不作推测。",
            fontsize=8.8, color=SLATE, ha="left", va="center")

    punchline(fig, "评级是名词，激励才是动词——而后者还没公开。")
    footer(fig, "事实来源：中国移动采购与招标网公示（2026-11）；"
                "分级原则「面向产品、循序渐进、动态评估、公正公开、合作共赢」")
    fig.savefig(OUT + "图2_AB差别.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """五个原则，五个动作"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "五个词，其实是五道门槛",
           "面向产品、循序渐进、动态评估、公正公开、合作共赢")

    items = [
        ("面向产品", "评的是产品线，不是公司", "一家公司可以有多条线、多个等级", NAVY),
        ("循序渐进", "不是一次性定终身", "分级每年做，标准逐年调", NAVY),
        ("动态评估", "等级会变", "上一年 A 不代表今年 A", RED),
        ("公正公开", "结果公示", "谁进了名单、谁没进，都看得见", RED),
        ("合作共赢", "目的是激励", "分级要能影响后续采购安排", TEAL),
    ]

    y = 0.712
    for i, (name, meaning, effect, color) in enumerate(items):
        card(ax, 0.045, y - 0.074, 0.908, 0.088, color, lw=1.1)
        ax.text(0.068, y - 0.030, name, fontsize=11.0, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(0.228, y - 0.030, meaning, fontsize=9.2, color=DARK,
                ha="left", va="center", zorder=6)
        ax.text(0.560, y - 0.030, effect, fontsize=8.6, color=SLATE,
                ha="left", va="center", zorder=6)
        y -= 0.103

    ax.text(0.045, 0.170,
            "前两个词约束方法，中间两个约束过程，最后一个说明目的。",
            fontsize=9.4, color=DARK, ha="left", va="center")

    punchline(fig, "五个词连起来看，这是一套机制，不是一次评奖。")
    footer(fig, "事实来源：中国移动采购与招标网《关于中国移动 2026 年一级集采供应商"
                "分级结果的公示》所列分级原则；通信世界网 2026-11-12")
    fig.savefig(OUT + "图3_五个原则.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)
