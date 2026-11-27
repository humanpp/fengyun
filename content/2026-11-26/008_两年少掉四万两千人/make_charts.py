# -*- coding: utf-8 -*-
"""
《两年少掉 4.2 万人，然后轮到副总裁：光伏周期底部的人才重定价》配套图表

事实口径（逐条可指回）：
  · 新浪财经《BUG》栏目 2026-11-13 报道（记者刘丽丽）：援引消息人士，隆基
    绿能今年以来多次裁员，8—9 月有一次较大规模裁员；14 级以上、总监以上
    员工"裁了一大批"；部分离职管理人员被启动竞业限制；离职管理层人士向
    该栏目确认了此事。有被裁员工称公司给予 N+1 补偿、预留时间，整体合规。
  · 同期报出离职的高管：副总裁兼首席战略与可持续发展官张海濛（2024 年 1 月
    加盟，此前为麦肯锡全球资深董事合伙人，任职不足 3 年）、电力运营中心
    总经理廖宇（2026 年 3 月出任，不足 8 个月；2026 年 11 月 1 日已以原力
    能源总经理身份出席第七届新型电力系统国际论坛）、中国产品策划负责人
    李绍唐（2016 年加入隆基乐叶，效力约 10 年）。信息源为新浪财经 2026-11-13、
    数字新能源 2026-11-05、网易"草根光伏" 2026-11-14、界面新闻 2026-11-17、
    北京商报 2026-11-25 等。截至 2026-11-25，隆基未对上述人事传闻作公开
    回应（北京商报向公司求证未获回应）。
  · 工商信息：2026 年 10 月，西安隆基氢能、无锡隆基氢能两家子公司法定代表人
    由张海濛变更为周国平（界面新闻 2026-11-17、腾讯新闻转《碳见光伏》）。
  · 员工人数（据隆基绿能年报）：2023 年 75,066 人 → 2025 年 32,775 人，
    减少 42,291 人。
  · 业绩：2023 年第四季度起连续 12 个季度净亏损；2024 年净亏 86.18 亿元，
    2025 年净亏 64.20 亿元，2026 年前三季度净亏 47.13 亿元（据《BUG》栏目
    与网易"草根光伏"引述财报；2026 年三季报数据以公司公告为准）。
  · 行业：2026 年前三季度，申万二级"光伏设备"73 家 A 股公司合计营收
    5,618.50 亿元，归母净利润 -204.50 亿元；据国家能源局数据，2026 年
    1—9 月国内光伏新增装机 110.83GW，同比下降 53.9%（新华财经 2026-11-18）。
    同期主要制造企业前三季度均报亏损：通威 -67.59 亿、TCL 中环 -45.56 亿、
    晶澳 -36.4 亿、晶科 -33.67 亿、天合 -19.42 亿、隆基 -47.13 亿
    （据"草根光伏"引述三季报，数字以各公司公告为准）。
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


def header(fig, title, sub):
    fig.text(0.045, Y_TITLE, title, fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, Y_SUB, sub, fontsize=10.6, color=GRAY,
             ha="left", va="top")


def footer(fig, text):
    fig.text(0.045, Y_FOOT, text, fontsize=7.4, color=GRAY,
             ha="left", va="bottom")


def punchline(fig, text):
    fig.text(0.045, Y_PUNCH, text, fontsize=10.4, color=DARK,
             ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


def card(ax, x, y, w, h, edge, face="white", lw=1.0, z=2):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.004,rounding_size=0.012",
        facecolor=face, edgecolor=edge, linewidth=lw, zorder=z))


def new_axes(fig):
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return ax


# ---------------------------------------------------------------- 图 1
def fig1():
    """两年，四万两千人"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "两年少掉 42,291 人，然后轮到副总裁",
           "按公司年报披露的员工人数，2023 到 2025 年减少了 56%")

    base_y = 0.300
    max_h = 0.400

    bars = [
        ("2023 年报", 75066, NAVY, "75,066 人"),
        ("2025 年报", 32775, RED, "32,775 人"),
    ]
    x = 0.130
    for label, val, color, top in bars:
        h = max_h * (val / 75066.0)
        ax.add_patch(Rectangle((x, base_y), 0.150, h, facecolor=color,
                               edgecolor=color, linewidth=1.0, zorder=3))
        ax.text(x + 0.075, base_y + h + 0.018, top, fontsize=12.0,
                color=color, weight="bold", ha="center", va="bottom", zorder=6)
        ax.text(x + 0.075, base_y - 0.032, label, fontsize=8.6, color=DARK,
                ha="center", va="top")
        x += 0.260

    ax.plot([0.110, 0.610], [base_y, base_y], color=SLATE, linewidth=1.2)

    # 右侧：一条时间线上的五个提示
    card(ax, 0.660, 0.250, 0.295, 0.480, LIGHT, lw=1.0)
    ax.text(0.680, 0.694, "这个数字之前发生了什么", fontsize=8.6, color=DARK,
            weight="bold", ha="left", va="center", zorder=7)
    ax.plot([0.680, 0.935], [0.674, 0.674], color=LIGHT, linewidth=0.9, zorder=7)
    items = [
        ("2023 Q4 起", ["连续 12 个季度净亏损"]),
        ("2024 年", ["净亏 86.18 亿元"]),
        ("2025 年", ["净亏 64.20 亿元"]),
        ("2026 年前三季度", ["净亏 47.13 亿元"]),
        ("2026 年 1—9 月", ["国内光伏新增装机 110.83GW，", "同比下降 53.9%"]),
    ]
    ly = 0.638
    for tag, lines in items:
        ax.text(0.680, ly, tag, fontsize=7.4, color=RED, weight="bold",
                ha="left", va="center", zorder=7)
        ty = ly - 0.030
        for t in lines:
            ax.text(0.680, ty, t, fontsize=7.2, color=SLATE,
                    ha="left", va="center", zorder=7)
            ty -= 0.026
        ly -= 0.038 + 0.026 * len(lines)

    # 来源说明单独放在图底部
    fig.text(0.045, 0.150,
             "来源：隆基绿能年报披露的员工人数；2023 年 75,066 人，2025 年 32,775 人，"
             "两年减少 42,291 人，降幅约 56%。",
             fontsize=7.6, color=GRAY, ha="left", va="center")

    punchline(fig, "先说清一件事：这不是一家公司的意外，而是整个行业在收缩。")
    footer(fig, "事实来源：隆基绿能历年年度报告（员工人数）；业绩数字据新浪财经《BUG》栏目 2026-11-13 与网易「草根光伏」2026-11-14 引述财报；"
                "装机数据据国家能源局（经新华财经 2026-11-18 转述）。以公司公告为准。")
    fig.savefig(OUT + "图1_两年四万两千人.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """六家企业，前三季度都亏"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "光伏制造的同一张体检表",
           "六家主要企业 2026 年前三季度净利润，全部为负")

    base_y = 0.700          # 零线
    max_h = 0.400           # 最大亏损对应的柱长
    data = [
        ("通威股份", -67.59),
        ("隆基绿能", -47.13),
        ("TCL 中环", -45.56),
        ("晶澳科技", -36.40),
        ("晶科能源", -33.67),
        ("天合光能", -19.42),
    ]

    bar_w = 0.100
    gap = 0.033
    x = 0.075
    for name, val in data:
        h = max_h * (abs(val) / 70.0)
        color = RED if name == "隆基绿能" else SLATE
        ax.add_patch(Rectangle((x, base_y - h), bar_w, h, facecolor=color,
                               edgecolor=color, linewidth=1.0, zorder=3))
        ax.text(x + bar_w / 2, base_y - h - 0.016, f"{val:.2f}", fontsize=8.8,
                color=color, weight="bold", ha="center", va="top", zorder=6)
        # 企业名放在零线之上，避免与柱体、数值重叠
        ax.text(x + bar_w / 2, base_y + 0.014, name, fontsize=8.0,
                color=DARK, ha="center", va="bottom", zorder=6)
        x += bar_w + gap

    ax.plot([0.060, 0.960], [base_y, base_y], color=SLATE, linewidth=1.2)
    ax.text(0.060, base_y - 0.008, "单位：亿元（归母净利润，2026 年前三季度）",
            fontsize=7.4, color=GRAY, ha="left", va="top")

    # 行业整体：横排三条
    card(ax, 0.060, 0.150, 0.900, 0.086, LIGHT, face=PALE, lw=1.0)
    ax.text(0.080, 0.193, "行业整体", fontsize=7.8, color=DARK,
            weight="bold", ha="left", va="center", zorder=7)
    ax.text(0.185, 0.200, "73 家", fontsize=9.4, color=NAVY, weight="bold",
            ha="left", va="center", zorder=7)
    ax.text(0.250, 0.193, "A 股光伏设备公司", fontsize=7.2, color=SLATE,
            ha="left", va="center", zorder=7)
    ax.text(0.470, 0.200, "5,618.50 亿元", fontsize=9.4, color=NAVY,
            weight="bold", ha="left", va="center", zorder=7)
    ax.text(0.620, 0.193, "前三季度合计营收", fontsize=7.2, color=SLATE,
            ha="left", va="center", zorder=7)
    ax.text(0.775, 0.200, "-204.50 亿元", fontsize=9.4, color=RED,
            weight="bold", ha="left", va="center", zorder=7)
    ax.text(0.895, 0.193, "合计归母净利润", fontsize=7.2, color=SLATE,
            ha="left", va="center", zorder=7)

    punchline(fig, "在这个背景下，人事调整是结果，不是原因。")
    footer(fig, "事实来源：各公司 2026 年三季报（经网易「草根光伏」2026-11-14 引述，数字以公司公告为准）；"
                "行业整体数据据申万二级分类，经新华财经 2026-11-18 转述。")
    fig.savefig(OUT + "图2_六家企业都亏.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """三类人，三种离职"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "同一个下半年，三种离开",
           "路径不同，指向同一个收缩中的组织")

    cols = [
        ("空降型", NAVY,
         "张海濛",
         "副总裁、首席战略与可持续发展官；\n2024 年 1 月加盟，此前为麦肯锡\n全球资深董事合伙人。任期不足 3 年。",
         "先卸任：2026 年 10 月，西安、无锡\n两家氢能子公司法定代表人变更。\n离职时间各版本不一（6/8/9 月）。"),
        ("短周期型", TEAL,
         "廖 宇",
         "电力运营中心总经理；\n2026 年 3 月出任，不足 8 个月。\n此前任天合光能虚拟电厂负责人。",
         "2026 年 11 月 1 日，已以原力能源\n总经理身份出席行业论坛发表演讲。\n业务线本身仍在，人已换场。"),
        ("老兵型", RED,
         "李绍唐",
         "中国产品策划负责人；2016 年加入\n隆基乐叶，效力约 10 年；\n主导 Hi-MO 系列 1—5 代产品策划。",
         "最后一次以该身份公开露面在\n2026 年 7 月。离职消息由\n行业自媒体报道后获交叉印证。"),
    ]

    x = 0.045
    w = 0.288
    for tag, color, name, bio, path in cols:
        card(ax, x, 0.250, w, 0.500, color, lw=1.3)
        ax.text(x + 0.020, 0.712, tag, fontsize=8.6, color=color,
                weight="bold", ha="left", va="center", zorder=7)
        ax.text(x + 0.020, 0.672, name, fontsize=12.0, color=DARK,
                weight="bold", ha="left", va="center", zorder=7)
        ax.plot([x + 0.020, x + w - 0.020], [0.650, 0.650], color=LIGHT,
                linewidth=0.9, zorder=7)
        ax.text(x + 0.020, 0.610, bio, fontsize=7.2, color=SLATE,
                ha="left", va="top", zorder=7, linespacing=1.85)
        ax.text(x + 0.020, 0.430, "此后", fontsize=7.6, color=color,
                weight="bold", ha="left", va="center", zorder=7)
        ax.text(x + 0.020, 0.398, path, fontsize=7.2, color=SLATE,
                ha="left", va="top", zorder=7, linespacing=1.85)
        x += w + 0.017

    punchline(fig, "过去的十年，这三类人都是被抢的对象；现在，他们都在被重新定价。")
    footer(fig, "事实来源：新浪财经《BUG》栏目 2026-11-13、数字新能源 2026-11-05、网易「草根光伏」2026-11-14、"
                "界面新闻 2026-11-17、北京商报 2026-11-25。截至 11 月 25 日公司未公开回应。")
    fig.savefig(OUT + "图3_三类人三种离开.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)
