# -*- coding: utf-8 -*-
"""
《两杯咖啡，三个人，一条"一客一消"》配套图表

事实口径（全部来自公开报道）：
  · 光明网 2026-11-19 17:35《3人同行进咖啡店，2人正常消费，1人因没有喜欢的饮品
    未点单被劝离；店方称并非公益场所，市监局：涉嫌强制最低消费》：
      三人同行、两人点购咖啡、第三人因店内没有喜欢的饮品未消费、仅坐等朋友、
      并未拍照打卡或长时间占座；店家仍要求其单独消费，最终要求离店；
      门店称确实执行"一客一消"，投入二三十万元打造院内景观，并非公益场所；
      南昌市东湖区市场监督管理局：要求"每位进店顾客必须消费才能入座"，
      涉嫌强制最低消费，会核实并向门店劝导。
  · 澎湃新闻（转中国蓝新闻）2026-11-19 22:09 热评《"一客一消"规则引争议
    "消费入座"边界在哪？》：星巴克新规对比；免消费弹性名单；
    另引"在星巴克开会1小时被提醒点单5次"争议。
  · 法治日报-法治网 2026-11-13（司法部智慧普法平台转载），记者张守坤：
      星巴克中国 2026-10-21 宣布自 10-22 起全国门店实行消费入座并发布
    《第三空间倡议》；《餐饮业促进和经营管理办法》第十六条禁止设最低消费；
      律师解读——"消费入座"以是否发生真实消费为条件、不以金额为条件，
      原则上合法；若表述为"每人最低消费××元"或以金额为门槛则仍属设最低消费、
      无效。宜家、霸王茶姬、皮爷咖啡等亦有部分门店明确座位规则。

风格：克制传媒风，白底、低饱和配色、标题即结论
输出目录 = 脚本所在目录
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, FancyArrowPatch

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

Y_TITLE = 0.958
Y_SUB = 0.898
Y_PUNCH = 0.070
Y_FOOT = 0.020


def header(fig, title, sub):
    fig.text(0.045, Y_TITLE, title, fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, Y_SUB, sub, fontsize=10.8, color=GRAY,
             ha="left", va="top")


def footer(fig, text):
    fig.text(0.045, Y_FOOT, text, fontsize=7.8, color=GRAY,
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


def cup(ax, cx, cy, r=0.030, color=NAVY, filled=True):
    """俯视杯形：外圈杯口 + 内圈液面 + 右侧杯柄。filled=False 即空杯。"""
    # 杯柄
    ax.add_patch(Circle((cx + r * 1.06, cy), r * 0.34,
                        facecolor="white", edgecolor=color,
                        linewidth=1.4, zorder=4))
    # 杯口
    ax.add_patch(Circle((cx, cy), r,
                        facecolor="white", edgecolor=color,
                        linewidth=1.5, zorder=5))
    # 液面
    ax.add_patch(Circle((cx, cy), r * 0.66,
                        facecolor=color if filled else "white",
                        edgecolor=color if not filled else "none",
                        linewidth=1.0, zorder=6))


# ---------------------------------------------------------------- 图 1
def fig1():
    fig = plt.figure(figsize=(12, 6.6))
    ax = new_axes(fig)

    header(fig, "三个人，两杯咖啡，一条规则",
           "规则问的不是“这桌有没有消费”，而是“每个人有没有消费”")

    seats = [
        ("点单", "有消费", NAVY, True),
        ("点单", "有消费", NAVY, True),
        ("未点单", "店里没有喜欢的饮品", RED, False),
    ]

    n = 3
    left, right, gap = 0.085, 0.915, 0.055
    w = (right - left - gap * (n - 1)) / n
    top, bot = 0.700, 0.400

    for i, (label, note, color, filled) in enumerate(seats):
        x = left + i * (w + gap)
        cx = x + w / 2
        is_third = (i == 2)
        card(ax, x, bot, w, top - bot,
             RED if is_third else LIGHT,
             face=BLUSH if is_third else "white",
             lw=1.7 if is_third else 1.0)
        cup(ax, cx, top - 0.105, color=color, filled=filled)
        ax.text(cx, bot + 0.120, label, fontsize=13.6, color=color,
                weight="bold", ha="center", va="center", zorder=7)
        ax.text(cx, bot + 0.048, note, fontsize=9.2, color=SLATE,
                ha="center", va="center", zorder=7)

    # 第三人的结果标注
    x3 = left + 2 * (w + gap) + w / 2
    ax.add_patch(FancyArrowPatch((x3, bot - 0.010), (x3, bot - 0.055),
                                 arrowstyle="-|>", mutation_scale=13,
                                 color=RED, linewidth=1.5, zorder=7))
    ax.text(x3, bot - 0.082, "被请离店", fontsize=10.6, color=RED,
            weight="bold", ha="center", va="center")

    # 规则说明
    ax.text(0.500, 0.800, "店家规则：一客一消", fontsize=12.6, color=NAVY,
            weight="bold", ha="center", va="center")
    ax.text(0.500, 0.760,
            "每人各自消费，方可入座", fontsize=10.0, color=SLATE,
            ha="center", va="center")

    ax.text(0.085, 0.250,
            "当事人说法：他与两位朋友同行，两人均已点购；自己未消费，"
            "也并未拍照打卡或长时间占座，只是坐着等朋友。",
            fontsize=9.6, color=SLATE, ha="left", va="center")

    punchline(fig, "两个人付了钱，规则却只盯着第三个人。")
    footer(fig, "事实来源：光明网 2026-11-19；澎湃新闻（转中国蓝新闻）2026-11-19")
    fig.savefig(OUT + "图1_三个人两杯咖啡.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "两条规则，不是一回事",
           "差一个字：一个“这张桌有消费就行”，一个“每个人都要有”")

    # 左：消费入座
    card(ax, 0.045, 0.235, 0.420, 0.560, NAVY, lw=1.5)
    ax.text(0.066, 0.742, "消费入座", fontsize=14.0, color=NAVY,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.066, 0.694, "星巴克中国等（2026 年 10 月起）", fontsize=9.6,
            color=GRAY, ha="left", va="center", zorder=6)
    ax.plot([0.066, 0.444], [0.664, 0.664], color=LIGHT, linewidth=1.0, zorder=4)

    ax.text(0.066, 0.622, "条件", fontsize=9.8, color=SLATE,
            ha="left", va="center", zorder=6)
    ax.text(0.066, 0.562, "这张桌有真实消费即可\n一杯最便宜的也算，不看金额",
            fontsize=10.0, color=DARK, ha="left", va="center",
            linespacing=1.62, zorder=6)

    ax.text(0.066, 0.490, "留了口子", fontsize=9.8, color=SLATE,
            ha="left", va="center", zorder=6)
    ax.text(0.066, 0.408,
            "孕妇、行动不便者、外卖员、\n避雨路人、值班保安等有临时\n休息需求者，可不消费进店，\n照旧提供免费热水",
            fontsize=9.4, color=NAVY, ha="left", va="center",
            linespacing=1.58, zorder=6)

    ax.text(0.066, 0.300, "也挨骂", fontsize=9.8, color=SLATE,
            ha="left", va="center", zorder=6)
    ax.text(0.066, 0.262, "“开会 1 小时被提醒点单 5 次”", fontsize=9.4,
            color=SLATE, ha="left", va="center", zorder=6)

    # 右：一客一消
    card(ax, 0.520, 0.235, 0.435, 0.560, RED, face=BLUSH, lw=1.6)
    ax.text(0.541, 0.742, "一客一消", fontsize=14.0, color=RED,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.541, 0.694, "南昌这家咖啡店", fontsize=9.6,
            color=GRAY, ha="left", va="center", zorder=6)
    ax.plot([0.541, 0.934], [0.664, 0.664], color=RED, linewidth=0.9,
            alpha=0.45, zorder=4)

    ax.text(0.541, 0.612, "条件", fontsize=9.8, color=SLATE,
            ha="left", va="center", zorder=6)
    ax.text(0.541, 0.568, "每位进店顾客各自消费\n三个人，就要三杯",
            fontsize=10.0, color=DARK, ha="left", va="center",
            linespacing=1.62, zorder=6)

    ax.text(0.541, 0.470, "店家的理由", fontsize=9.8, color=SLATE,
            ha="left", va="center", zorder=6)
    ax.text(0.541, 0.424,
            "投入二三十万元打造院内景观，\n“并非公益场所”",
            fontsize=9.4, color=RED, ha="left", va="center",
            linespacing=1.58, zorder=6)

    ax.text(0.541, 0.318, "监管表态", fontsize=9.8, color=SLATE,
            ha="left", va="center", zorder=6)
    ax.text(0.541, 0.272,
            "要求“每位进店顾客必须消费”，\n涉嫌强制最低消费",
            fontsize=9.4, color=RED, ha="left", va="center",
            linespacing=1.58, zorder=6, weight="bold")

    ax.text(0.500, 0.176,
            "同样的三杯椅子，一个允许“有人陪坐”，一个不允许。",
            fontsize=9.8, color=SLATE, ha="center", va="center")

    punchline(fig, "“消费入座”要的是一笔单；“一客一消”要的是每个人一笔单。")
    footer(fig, "事实来源：法治日报-法治网 2026-11-13；澎湃新闻 2026-11-19；光明网 2026-11-19")
    fig.savefig(OUT + "图2_两条规则.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(12, 6.6))
    ax = new_axes(fig)

    header(fig, "法律管的是“有没有拿金额当门槛”",
           "不看要不要坐下，只看入座是否被绑上了价钱")

    tiers = [
        ("原则上合法", NAVY, "white",
         "以“是否发生真实消费”为条件\n不以“消费多少钱”为条件\n买一杯最低价商品即可获得座位"),
        ("仍然无效", RED, BLUSH,
         "表述为“每人最低消费××元”\n或“入座须单笔消费不低于××元”\n或名为消费入座、执行以金额为门槛"),
        ("禁止条款", SLATE, "white",
         "《餐饮业促进和经营管理办法》\n第十六条：禁止餐饮服务经营者\n设置最低消费"),
    ]

    left, right, gap = 0.045, 0.955, 0.028
    w = (right - left - gap * 2) / 3
    top, bot = 0.700, 0.300

    for i, (label, color, face, body) in enumerate(tiers):
        x = left + i * (w + gap)
        card(ax, x, bot, w, top - bot, color, face=face,
             lw=1.6 if i == 1 else 1.2)
        ax.text(x + w / 2, top - 0.062, label, fontsize=13.0, color=color,
                weight="bold", ha="center", va="center", zorder=6)
        ax.plot([x + 0.030, x + w - 0.030], [top - 0.108, top - 0.108],
                color=color, linewidth=0.9, alpha=0.40, zorder=5)
        ax.text(x + w / 2, bot + (top - bot) * 0.40, body, fontsize=9.4,
                color=DARK if i != 1 else RED, ha="center", va="center",
                linespacing=1.72, zorder=6)

    ax.text(0.500, 0.238,
            "“一客一消”没设金额门槛——点最便宜的也行；但它把入座绑到了“每人各自消费”。",
            fontsize=9.6, color=SLATE, ha="center", va="center")

    ax.text(0.500, 0.166,
            "市监局的表态是“涉嫌”，不是“认定”。公开报道里没见到最终处理结果。",
            fontsize=9.6, color=GRAY, ha="center", va="center")

    punchline(fig, "要求每人消费，不等于设了金额门槛——所以它卡在线上。")
    footer(fig, "法条与解读来源：法治日报-法治网 2026-11-13（司法部智慧普法平台转载），记者张守坤")
    fig.savefig(OUT + "图3_法律那条线.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)