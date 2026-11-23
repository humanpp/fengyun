# -*- coding: utf-8 -*-
"""
《MiMo 拆不拆：一条传闻的两个版本，卡在同一笔预算上》配套图表

事实口径：
  · 2026-11-18 36氪、《TOP华人科创社》等报道：小米讨论 MiMo 是否分拆独立融资，
    多家风投与 CVC 初步接触，集团未拿出明确方案；称雷军与罗福莉存在分歧，
    罗福莉已接触少数投资人和融资顾问，不排除独立创业。
  · 2026-11-23 虎嗅转载《资本不熬夜》独家：摸底发生在 7 月，早于见报四个月；
    知情人士称雷军对 MiMo 有绝对控制权、“不存在分歧”，团队要外部股东分担
    研发投入、罗福莉拿单列预算。
  · 11-24 小米发三季度业绩（未到，作为待验证节点）。
  · 金山云关联交易：小米向金山云采购云服务 2026 年上限 40 亿元、2027 年 60 亿元
    （原上限 31.38 亿元）；金山云向小米采购 MiMo 模型接口，2026-04-23 至年底
    上限 2000 万元、2027 年 5000 万元。
  · 上半年「智能电动汽车及AI等创新业务」下「其他相关业务」收入 19 亿元，
    同比 +62.7%；MiMo 营收未单独披露。
  · 全年 AI 预算年初规划 161 亿元（CFO 林世伟）；雷军 3 月 19 日宣布未来三年
    AI 投入至少 600 亿元；二季报手机毛利率 11.5%→8.5%；上半年汽车和 AI 等
    创新业务经营亏损 57 亿元。
  · 罗福莉：1T 参数是当时算力“比较极限的区间”，预训练/后训练/其他 由 3:5:1
    改为 3:1:1。

输出目录 = 脚本所在目录
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei"]
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
Y_PUNCH = 0.068
Y_FOOT = 0.020


def header(fig, title, sub):
    fig.text(0.045, Y_TITLE, title, fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, Y_SUB, sub, fontsize=10.4, color=GRAY,
             ha="left", va="top")


def footer(fig, text):
    fig.text(0.045, Y_FOOT, text, fontsize=7.6, color=GRAY,
             ha="left", va="bottom")


def punchline(fig, text):
    fig.text(0.045, Y_PUNCH, text, fontsize=10.4, color=DARK,
             ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


def card(ax, x, y, w, h, edge, face="white", lw=1.2, z=2):
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
    """时间线 + 两个版本的要点"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "一条传闻的两个版本",
           "11 月 18 日见报说“有分歧”，11 月 23 日出现“不存在分歧”的版本")

    ax.add_patch(FancyArrowPatch((0.070, 0.665), (0.930, 0.665),
                                 arrowstyle="-|>", mutation_scale=18,
                                 color=LIGHT, lw=2.0))

    nodes = [
        (0.115, "7 月", "罗福莉接触几轮基金\n摸底单独融资的可能", SLATE),
        (0.375, "11 月 18 日", "36 氪等报道：或分拆\n雷军与罗福莉有分歧", RED),
        (0.635, "11 月 20 日", "观察者网联系小米\n截至发稿无回应", GRAY),
        (0.890, "11 月 23 日", "知情人士：不存在分歧\n团队要预算", NAVY),
    ]
    for x, title, note, color in nodes:
        ax.plot([x], [0.665], "o", markersize=9, color=color,
                markeredgecolor="white", markeredgewidth=1.2, zorder=6)
        ax.text(x, 0.705, title, fontsize=11.0, color=DARK,
                weight="bold", ha="center", va="bottom")
        ax.text(x, 0.625, note, fontsize=9.0, color=SLATE,
                ha="center", va="top", linespacing=1.7)

    ax.add_patch(FancyArrowPatch((0.128, 0.735), (0.362, 0.735),
                                 arrowstyle="-|>", mutation_scale=12,
                                 color=GRAY, lw=1.1, linestyle=":"))
    ax.text(0.245, 0.752, "摸底比见报早四个月", fontsize=8.6, color=GRAY,
            ha="center", va="bottom")

    # 版本 A
    card(ax, 0.045, 0.235, 0.435, 0.300, RED, lw=1.4)
    ax.text(0.070, 0.500, "见报版：拆不拆", fontsize=11.0, color=RED,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.070, 0.455,
            "· 正处在是否分拆独立融资的关键阶段\n"
            "· 多家风投与产业资本（CVC）初步接触\n"
            "· 集团层面尚未拿出明确方案\n"
            "· 罗福莉已接触投资人、融资顾问，\n"
            "  不排除独立创业",
            fontsize=9.2, color=SLATE, ha="left", va="top",
            linespacing=1.85, zorder=6)

    # 版本 B
    card(ax, 0.520, 0.235, 0.435, 0.300, NAVY, lw=1.4)
    ax.text(0.545, 0.500, "后续版：不吵，要预算", fontsize=11.0, color=NAVY,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.545, 0.455,
            "· 摸底拿到的反馈并不乐观：\n"
            "  钱在向头部集中\n"
            "· 雷军对 MiMo 有绝对控制权\n"
            "· 团队要的是外部股东分担研发投入\n"
            "  罗福莉拿到单列预算",
            fontsize=9.2, color=SLATE, ha="left", va="top",
            linespacing=1.85, zorder=6)

    ax.text(0.045, 0.175, "两个版本不互相否定，指向同一件事：钱谁出、算力谁批、预算谁定。",
            fontsize=9.6, color=DARK, ha="left", va="center")

    punchline(fig, "“分歧”是最抓眼的部分，预算才是真正的分歧。")
    footer(fig, "事实来源：36氪、《TOP华人科创社》2026-11-18（经 BlockBeats、观点网转述）；"
                "观察者网 2026-11-20；虎嗅转载《资本不熬夜》2026-11-23")
    fig.savefig(OUT + "图1_一条传闻两个版本.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """两笔方向相反的交易，量级差 100 倍以上"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = fig.add_axes([0.075, 0.300, 0.640, 0.450])

    header(fig, "两笔生意的价差",
           "小米买云服务是几十亿，金山云买 MiMo 接口是几千万")

    groups = ["2026 年上限", "2027 年上限"]
    cloud = [40.0, 60.0]       # 小米 → 金山云，亿元
    mimo = [0.20, 0.50]        # 金山云 → 小米，亿元
    ys = [1, 0]

    ax.barh([y + 0.16 for y in ys], cloud, height=0.30, color=NAVY, zorder=3)
    ax.barh([y - 0.16 for y in ys], mimo, height=0.30, color=RED, zorder=3)

    ax.set_yticks(ys)
    ax.set_yticklabels(groups, fontsize=9.8, color=SLATE)
    ax.set_xlim(0, 70)
    ax.set_ylim(-0.55, 1.55)
    ax.set_xlabel("交易金额上限  亿元", fontsize=9.4, color=GRAY)
    ax.tick_params(axis="x", labelsize=8.2, colors=GRAY)
    ax.grid(axis="x", color=LIGHT, linewidth=0.8, alpha=0.7, zorder=0)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    for spine in ("left", "bottom"):
        ax.spines[spine].set_color(LIGHT)

    for y, v in zip(ys, cloud):
        ax.text(v + 1.0, y + 0.16, "%d 亿元" % v, fontsize=11.0,
                color=NAVY, weight="bold", va="center")
    for y, v in zip(ys, mimo):
        ax.text(v + 1.4, y - 0.16, "%d 万元" % (v * 10000), fontsize=11.0,
                color=RED, weight="bold", va="center")

    rows = [
        ("小米 → 金山云", "云服务采购", NAVY,
         "2026 年上限由 31.38 亿元\n调至 40 亿元"),
        ("金山云 → 小米", "MiMo 模型接口", RED,
         "2026-04-23 起至年底\n供平台客户调用"),
    ]
    y = 0.535
    for name, what, color, note in rows:
        fig.text(0.755, y + 0.040, name, fontsize=9.0, color=GRAY,
                 ha="left", va="center")
        fig.text(0.755, y - 0.002, what, fontsize=12.8, color=color,
                 weight="bold", ha="left", va="center")
        fig.text(0.755, y - 0.052, note, fontsize=8.0, color=SLATE,
                 ha="left", va="top", linespacing=1.75)
        y -= 0.190

    fig.text(0.755, 0.180,
             "上半年「其他相关业务」收入 19 亿元、\n"
             "同比 +62.7%，含汽车售后服务与 MiMo\n"
             "相关 AI 业务；MiMo 营收未单独披露。",
             fontsize=8.4, color=SLATE, ha="left", va="top", linespacing=1.85)

    punchline(fig, "投资人现在能看到的 MiMo 订单，主要来自自己人。")
    footer(fig, "事实来源：金山云关联交易公告（2026-04，经《资本不熬夜》引述）；"
                "小米 2026 年中期业绩（经观点网、观察者网转述）")
    fig.savefig(OUT + "图2_两笔生意的价差.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """算力配比 + 四个约束数字"""
    fig = plt.figure(figsize=(12, 6.9))
    axf = new_axes(fig)
    ax = fig.add_axes([0.090, 0.430, 0.385, 0.285])

    header(fig, "约束不在“拆不拆”，在“给多少”",
           "算力配比先被压缩，预算和亏损同时收紧")

    labels = ["业界惯用", "MiMo 团队"]
    pre = [3, 3]
    post = [5, 1]
    other = [1, 1]
    ys = [1, 0]
    total = 9.0

    left = [0, 0]
    bars = []
    for vals, color in ((pre, NAVY), (post, RED), (other, LIGHT)):
        b = ax.barh(ys, [v / total for v in vals],
                    left=[l / total for l in left],
                    height=0.42, color=color, zorder=3)
        bars.append(b)
        left = [a + b2 for a, b2 in zip(left, vals)]

    ax.set_yticks(ys)
    ax.set_yticklabels(labels, fontsize=10.0, color=SLATE)
    ax.set_xlim(0, 1)
    ax.set_ylim(-0.55, 1.55)
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1.0])
    ax.set_xticklabels(["0", "25%", "50%", "75%", "100%"], fontsize=8.4,
                       color=GRAY)
    ax.tick_params(axis="x", colors=GRAY)
    for spine in ("top", "right", "left"):
        ax.spines[spine].set_visible(False)
    ax.spines["bottom"].set_color(LIGHT)

    # 段内只标数字，段名交给图例
    for row, (a, b2, c) in zip(ys, ((3, 5, 1), (3, 1, 1))):
        cx1 = a / total / 2
        cx2 = (a + b2 / 2) / total
        cx3 = (a + b2 + c / 2) / total
        ax.text(cx1, row, "%d" % a, fontsize=10.2, color="white",
                weight="bold", ha="center", va="center", zorder=6)
        ax.text(cx2, row, "%d" % b2, fontsize=10.2, color="white",
                weight="bold", ha="center", va="center", zorder=6)
        ax.text(cx3, row, "%d" % c, fontsize=9.6, color=SLATE,
                weight="bold", ha="center", va="center", zorder=6)

    ax.legend([bars[0], bars[1], bars[2]], ["预训练", "后训练", "其他"],
              loc="lower center", bbox_to_anchor=(0.5, 1.00), ncol=3,
              frameon=False, fontsize=8.8, handlelength=1.2,
              columnspacing=1.8, borderaxespad=0.2)

    ax.set_title("预训练 / 后训练 / 其他 的算力配比", fontsize=10.2,
                 color=SLATE, pad=26)

    cards = [
        ("161 亿元", 13.6, "全年 AI 预算\n年初规划（CFO）", NAVY),
        ("≥600 亿元", 13.6, "未来三年 AI 投入\n雷军 3 月 19 日宣布", TEAL),
        ("11.5% → 8.5%", 10.8, "手机毛利率（二季报）\n零部件涨价所致", RED),
        ("57 亿元", 13.6, "上半年创新业务\n经营亏损", SLATE),
    ]
    for i, (big, fs, note, color) in enumerate(cards):
        col = i % 2
        row = i // 2
        cx = 0.545 + col * 0.213
        cy = 0.585 - row * 0.190
        card(axf, cx, cy, 0.195, 0.165, LIGHT, face="white", lw=1.0)
        axf.text(cx + 0.017, cy + 0.116, big, fontsize=fs, color=color,
                 weight="bold", ha="left", va="center", zorder=6)
        axf.text(cx + 0.017, cy + 0.072, note, fontsize=8.2, color=SLATE,
                 ha="left", va="top", linespacing=1.75, zorder=6)

    axf.text(0.045, 0.330,
             "罗福莉把 1T 参数称为当时团队算力“比较极限的区间”，于是把预训练与后训练的配比\n"
             "从业界惯用的 3:5:1 改成 3:1:1：先保住预训练。",
             fontsize=9.2, color=SLATE, ha="left", va="top", linespacing=1.9)

    punchline(fig, "钱不是没有，是要排队。")
    footer(fig, "事实来源：财报电话会与二季报（经《资本不熬夜》、观察者网引述）；"
                "雷军 2026-03-19 发布会；罗福莉公开表述（经《资本不熬夜》引述）")
    fig.savefig(OUT + "图3_约束在哪.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)
