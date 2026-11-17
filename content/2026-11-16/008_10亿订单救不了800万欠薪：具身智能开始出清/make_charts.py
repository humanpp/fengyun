# -*- coding: utf-8 -*-
"""
《10 亿订单救不了 800 万欠薪：具身智能开始出清》配套图表
事实来源：IT 桔子数据（经每日经济新闻、36 氪、第一财经、中新经纬转述）、
每日经济新闻 2026-10-23 对无境动力的报道、界面新闻 2026-10-28 破产名单报道、
企业公开披露的部署/下线口径
风格：克制传媒风，白底、低饱和配色、标题即结论
输出目录 = 脚本所在目录
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

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
SAND = "#b9a887"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep


def canvas(fig):
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return ax


def footer(fig, text):
    fig.text(0.045, 0.035, text, fontsize=8.4, color=GRAY, ha="left", va="bottom")


def takeaway(fig, y, text, size=10.4):
    fig.text(0.045, y, text, fontsize=size, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


def head(fig, title, sub):
    fig.text(0.045, 0.935, title, fontsize=19, color=DARK, ha="left",
             va="center", weight="bold")
    fig.text(0.045, 0.868, sub, fontsize=10.8, color=GRAY, ha="left", va="center")


# ---------------------------------------------------------------- 图 1
def fig1():
    fig = plt.figure(figsize=(12, 6.8))
    ax = canvas(fig)
    head(fig, "钱没消失，节奏断了",
         "IT 桔子口径：具身智能月度融资额与事件数，2026 年 6 月见顶，10 月回落")

    # ---- 左：柱子
    fig.text(0.070, 0.800, "融资额（亿元）", fontsize=12.5, color=DARK,
             weight="bold", va="center")

    axb = fig.add_axes([0.075, 0.290, 0.520, 0.450])
    labels = ["上半年合计\n（月均 156）", "6 月\n55 起", "8 月\n91 起", "10 月\n33 起"]
    vals = [935, 309, 313, 101]
    colors = [SAND, NAVY, NAVY, RED]
    bars = axb.bar(range(4), vals, width=0.52, color=colors)
    for b, v in zip(bars, vals):
        axb.text(b.get_x() + b.get_width() / 2, v + 22, f"{v}", fontsize=11,
                 color=DARK, ha="center", weight="bold")
    axb.plot([0.5, 0.5], [0, 1030], color=LIGHT, lw=1.2, linestyle=(0, (4, 4)))
    axb.set_ylim(0, 1050)
    axb.set_xticks(range(4))
    axb.set_xticklabels(labels, fontsize=10, color=DARK)
    axb.tick_params(axis="y", labelsize=9, colors=GRAY, length=0)
    for s in ("top", "right"):
        axb.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        axb.spines[s].set_color(LIGHT)
    axb.grid(axis="y", color=LIGHT, lw=0.8, alpha=0.7)
    axb.set_axisbelow(True)

    axb.add_patch(FancyArrowPatch((2.32, 640), (2.72, 640), arrowstyle="-|>",
                                  mutation_scale=14, color=RED, lw=1.3))
    axb.text(2.52, 690, "两个月 −68%", fontsize=10, color=RED, ha="center",
             weight="bold")

    # ---- 右：名单卡
    ax.add_patch(Rectangle((0.630, 0.290), 0.330, 0.510, facecolor="#f7f4ef",
                           edgecolor=LIGHT, linewidth=1.0))
    ax.text(0.660, 0.755, "同时，名单在加长", fontsize=12, color=DARK,
            weight="bold", va="center")
    names = [
        ("无境动力", "10 月停摆，欠薪近 800 万", RED),
        ("深兰机器人", "5 月被裁定受理破产清算", GRAY),
        ("盈合机器人", "两个月前法院受理破产", GRAY),
        ("智橙动力", "9 月进入破产审查", GRAY),
    ]
    for i, (name, note, color) in enumerate(names):
        y = 0.685 - i * 0.098
        ax.text(0.660, y, name, fontsize=10.8, color=color, weight="bold",
                va="center")
        ax.text(0.660, y - 0.042, note, fontsize=9.2, color=GRAY, va="center")

    takeaway(fig, 0.135, "钱没有消失，是出手的方式变了：从抢项目，到挑项目。")
    footer(fig, "据 IT 桔子数据整理（经每日经济新闻、36 氪、第一财经、中新经纬转述）；上半年月均为 935 亿除以 6 个月。")
    fig.savefig(OUT + "图1_钱没消失节奏断了.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(12, 6.8))
    ax = canvas(fig)
    head(fig, "近 10 亿订单，卡在哪一层",
         "一笔生意要走四步，只有最后一步进现金流；无境动力把前两步说满了")

    # ---- 左：漏斗
    fig.text(0.055, 0.800, "订单的四层口径", fontsize=12.5, color=DARK,
             weight="bold", va="center")

    rows = [
        ("签约（框架 + 储备）", "近 10 亿：不锁交付时间、不锁付款", 1.00, NAVY),
        ("锁定交付", "有验收排期才算数，要验收单", 0.64, NAVY),
        ("开票", "形成应收账款，账期通常 60—180 天", 0.40, SAND),
        ("回款", "进现金流，才叫收入", 0.20, RED),
    ]
    x0, full = 0.055, 0.400
    ytop, hh, pitch = 0.690, 0.070, 0.122
    for i, (name, note, wfrac, color) in enumerate(rows):
        top = ytop - i * pitch
        ax.add_patch(Rectangle((x0, top - hh), full * wfrac, hh, facecolor=color,
                               edgecolor="none"))
        ax.text(x0 + 0.014, top - hh / 2, name, fontsize=10.2, color="white",
                va="center", weight="bold")
        ax.text(x0, top - hh - 0.028, note, fontsize=9.2, color=GRAY, va="center")

    ax.text(0.055, 0.190, "前两层可以开发布会；后两层才进现金流。",
            fontsize=10.2, color=DARK, va="center", weight="bold")

    # ---- 右：无境动力时间线
    fig.text(0.560, 0.800, "无境动力：九个月", fontsize=12.5, color=DARK,
             weight="bold", va="center")
    ax.plot([0.575, 0.575], [0.215, 0.740], color=LIGHT, lw=2.0, zorder=1)

    events = [
        ("2026.02", "成立，注册资本 1000 万元", GRAY),
        ("06", "官宣近 10 亿元订单（框架 5 亿 + 储备 5 亿）", NAVY),
        ("07", "1.1 亿元融资到账，天使轮估值 10 亿元", NAVY),
        ("08", "开始拖欠工资", RED),
        ("09", "停缴住房公积金", RED),
        ("10", "停工，三四十人欠薪近 800 万；实控人失联", RED),
    ]
    for i, (date, what, color) in enumerate(events):
        y = 0.715 - i * 0.096
        ax.add_patch(plt.Circle((0.575, y), 0.008, facecolor=color,
                                edgecolor="white", linewidth=1.4, zorder=4))
        ax.text(0.500, y, date, fontsize=9.4, color=color, weight="bold",
                va="center", ha="left")
        ax.text(0.598, y, what, fontsize=9.6, color=DARK, va="center")

    takeaway(fig, 0.135, "“框架”“储备”这两个词，不承诺交付时间，也不承诺付款。")
    footer(fig, "据每日经济新闻 2026-10-23 报道及界面新闻、新浪财经、虎嗅后续报道整理；账期区间为行业常见区间，非该公司披露。")
    fig.savefig(OUT + "图2_订单卡在哪一层.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(12, 6.8))
    ax = canvas(fig)
    head(fig, "资本换了一支标尺",
         "旧标尺看技术想象力，新标尺只问三件事：有场景、有订单、有回款")

    # 列头
    ax.text(0.055, 0.790, "维度", fontsize=9.6, color=GRAY, va="center")
    ax.text(0.175, 0.790, "旧标尺", fontsize=9.6, color=GRAY, va="center")
    ax.text(0.470, 0.790, "新标尺", fontsize=9.6, color=RED, va="center")
    ax.text(0.775, 0.790, "要看的东西", fontsize=9.6, color=GRAY, va="center")

    rows = [
        ("场景", "机器人能做多少事", "谁在付钱，会不会付第二次", "客户名单、复购率"),
        ("订单", "签约额、框架协议", "锁量锁价、验收与违约条款", "验收单、开票记录"),
        ("回款", "过去基本不看", "账期、回款率、应收账龄", "经营性现金流"),
    ]
    for i, (dim, old, new, ev) in enumerate(rows):
        y = 0.665 - i * 0.170
        ax.add_patch(Rectangle((0.055, y - 0.075), 0.890, 0.150,
                               facecolor=PALE if i % 2 == 0 else "#f8f8f9",
                               edgecolor=LIGHT, linewidth=1.0))
        ax.text(0.085, y, dim, fontsize=13, color=NAVY, weight="bold",
                va="center")
        ax.text(0.175, y, old, fontsize=10.4, color=GRAY, va="center")
        ax.add_patch(FancyArrowPatch((0.430, y), (0.458, y), arrowstyle="-|>",
                                     mutation_scale=12, color=GRAY, lw=1.1))
        ax.text(0.470, y, new, fontsize=11, color=DARK, va="center",
                weight="bold")
        ax.text(0.775, y, ev, fontsize=9.2, color=GRAY, va="center")

    # 底部提示
    ax.add_patch(Rectangle((0.055, 0.163), 0.890, 0.078, facecolor="#f7f4ef",
                           edgecolor=LIGHT, linewidth=1.0))
    ax.text(0.075, 0.202, "下线 ≠ 卖出", fontsize=10.4, color=RED,
            weight="bold", va="center")
    ax.text(0.250, 0.202,
            "银河通用称超千台商业部署；启元称 Q1/T1 累计下线破万台，后 5000 台只用 14 天——均为企业口径",
            fontsize=9.2, color=DARK, va="center")

    takeaway(fig, 0.105, "万台下线可以是好消息，也可以是库存。")
    footer(fig, "标尺为本文据多份投资机构访谈与报道归纳；部署与下线数字均为企业公开披露口径，未经第三方核验。")
    fig.savefig(OUT + "图3_资本换了一支标尺.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")
