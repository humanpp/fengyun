# -*- coding: utf-8 -*-
"""
《蔚来的亏损在缩小，欠供应商的钱在变大》配套图表（共 10 张）。

图表编号 = 正文出现顺序。

事实口径（逐条可核验，仅涉及蔚来自身披露与监管公开文件）：
  · 归母净亏损：2023 年 207.2 亿元、2024 年 226.6 亿元、2025 年 155.7 亿元。
  · 应付账款及票据（Trade and notes payable，SEC 6-K 资产负债表原文）：
    FY2025 末 53,309,727 千元 = 533.1 亿元、2026-06-30 60,385,478 千元 = 604.0 亿元，
    两者均为披露值；2025-06-30 的 349.51 亿元为第三方统计；
    FY2024 末 343.8 亿元由 533.10 ÷ 1.5503 反推，仅用于趋势线。
  · 2025Q4：净利润 2.83 亿元（上市以来首次单季盈利）、交付 12.48 万辆（+71.7%）、
    收入 346.5 亿元、研发 20.26 亿元（−44.3%）、销售及行政 35.37 亿元（−27.5%）。
  · FY2025：营收 874.88 亿元（+33.1%）、研发 106 亿元（−18.7%）、
    经营活动现金流净额 29.93 亿元、年末现金储备 459 亿元；
    员工 4.56 万 → 3.5 万（−23.2%），产品及软件开发 1.15 万 → 6,912 人（−40%）。
  · 2025-12-31：负债总额 1,117 亿元、资产负债率 89.8%、流动比率 0.98、
    速动比率 0.87、流动资产 766.3 亿元、流动负债 785.8 亿元（缺口 19.5 亿元）。
  · 2026-06-30：应付账款及票据 604.00 亿元、非受限现金及短期投资 430.88 亿元、
    含受限现金与长期定期存款的流动性 567 亿元、借款 176.13 亿元、
    可赎回非控股权益 102.23 亿元、股东权益 40.455 亿元、
    流动资产减流动负债 16.31 亿元；上半年应付账款增 70.76 亿元、借款增 36.39 亿元。
  · 2026Q2：营收 321.369 亿元、GAAP 净亏损 5.280 亿元、non-GAAP 净利润 0.261 亿元、
    股权激励 5.541 亿元、加权平均股数 24.967 亿股（上年 22.300 亿股）。
  · 交付：2026Q2 107,658 辆、Q3 109,178 辆、9 月 37,408 辆、10 月 34,246 辆
    （同比 −15.2%、环比 −8.5%）；Q4 目标月均超 4 万辆。
  · 账期口径：中汽协 2026 年 2 月调研平均约 54 天；第三方统计（Wind，经每日经济
    新闻 2026-11-19 引用）2026 年三季度主流车企应付账款周转天数均值 127 天。

注意：本脚本不含任何推算出来的资产负债表科目绝对额。凡未公开披露的科目，
一律只画已披露的差额或比率。
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

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
AMBER = "#a8863f"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep


def newfig(title, sub):
    fig = plt.figure(figsize=(12, 6.8), dpi=150)
    fig.patch.set_facecolor("white")
    fig.text(0.045, 0.958, title, fontsize=18.0, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.895, sub, fontsize=10.3, color=GRAY, ha="left", va="top")
    return fig


def footer(fig, text):
    fig.text(0.045, 0.017, text, fontsize=7.9, color=GRAY, ha="left", va="center")


def note(fig, text, y=0.068):
    fig.text(0.045, y, text, fontsize=9.9, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.55", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


def clean(ax, axis="y"):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.grid(axis=axis, color=LIGHT, lw=0.8)
    ax.set_axisbelow(True)


def save(fig, name):
    fig.savefig(OUT + name, facecolor="white")
    plt.close(fig)
    print("saved", name)


# ================================================== 图 1（正文「两条曲线」）
def chart1():
    fig = newfig("应付账款及票据：18 个月从 343.8 亿涨到 604 亿",
                 "蔚来资产负债表该科目余额（人民币亿元），四个时点")
    data = [("2024 年末", 343.8), ("2025 年 6 月", 349.5),
            ("2025 年末", 533.1), ("2026 年 6 月", 604.0)]
    ax = fig.add_axes([0.085, 0.230, 0.865, 0.560])
    for i, (lab, v) in enumerate(data):
        c = RED if i >= 2 else SLATE
        ax.bar(i, v, color=c, width=0.50)
        ax.text(i, v + 12, "%.1f" % v, ha="center", va="bottom",
                fontsize=14.5, color=c, weight="bold")
    ax.annotate("", xy=(3.0, 645), xytext=(0.0, 645),
                arrowprops=dict(arrowstyle="->", color=GRAY, lw=1.4))
    ax.text(1.5, 660, "+75.6%（+260 亿元）", ha="center", va="bottom",
            fontsize=11.0, color=DARK, weight="bold")
    ax.set_xticks(range(4))
    ax.set_xticklabels([d[0] for d in data], fontsize=10.8)
    ax.set_ylim(0, 760)
    ax.set_ylabel("人民币亿元", fontsize=10, color=SLATE)
    clean(ax)

    note(fig, "2025 年下半年一个半年里净增 184 亿元——同期，蔚来交出了上市以来唯一一个盈利季度。")
    footer(fig, "来源：蔚来 2026 年第二季度业绩公告所附资产负债表（SEC 6-K）Trade and notes payable："
                "53,309,727 千元（2025-12-31）、60,385,478 千元（2026-06-30），均为披露值。"
                "2024 年末为按 2025 年报「较上年末 +55.03%」反推，仅用于趋势线。")
    save(fig, "图1_应付账款四级跳.png")


# ================================================== 图 2（正文「两条曲线」）
def chart2():
    fig = newfig("欠款跑得比营收快：55% 对 33%",
                 "蔚来 2025 年，应付账款及票据增速与营业收入增速")
    ax = fig.add_axes([0.085, 0.215, 0.865, 0.575])
    vals = [("营业收入\n874.88 亿元", 33.1, SLATE),
            ("应付账款及票据\n533.1 亿元", 55.03, RED)]
    for i, (lab, v, c) in enumerate(vals):
        ax.bar(i, v, color=c, width=0.40)
        ax.text(i, v + 1.6, "+%.2f%%" % v, ha="center", va="bottom",
                fontsize=18, color=c, weight="bold")
    ax.set_xticks(range(2))
    ax.set_xticklabels([v[0] for v in vals], fontsize=10.8)
    ax.set_ylim(0, 72)
    ax.set_xlim(-0.65, 1.65)
    ax.set_ylabel("同比增速（%）", fontsize=10, color=SLATE)
    clean(ax)

    note(fig, "生意涨 33%，欠款涨 55%。差额 22 个百分点，就是这一年多出来的时间差。")
    footer(fig, "来源：蔚来 2025 年报（应付票据及应付账款较上年末增加 55.03%；营业收入 874.88 亿元、同比 +33.1%）。")
    save(fig, "图2_欠款跑赢营收.png")


# ================================================== 图 3（正文「两条曲线」）
def chart3():
    fig = newfig("唯一一个盈利季度，供应商同期多垫了 184 亿",
                 "2025 年下半年：净利润与应付账款及票据净增额（人民币亿元）")
    ax = fig.add_axes([0.085, 0.215, 0.865, 0.575])
    vals = [("2025Q4 净利润\n（上市以来首次为正）", 2.83, GREEN),
            ("同期应付账款及票据\n净增加额", 183.7, RED)]
    for i, (lab, v, c) in enumerate(vals):
        ax.bar(i, v, color=c, width=0.42)
        ax.text(i, v + 5.5, "%.1f" % v, ha="center", va="bottom",
                fontsize=17, color=c, weight="bold")
    ax.set_xticks(range(2))
    ax.set_xticklabels([v[0] for v in vals], fontsize=11.0)
    ax.set_ylim(0, 215)
    ax.set_xlim(-0.6, 1.6)
    ax.set_ylabel("人民币亿元", fontsize=10, color=SLATE)
    clean(ax)

    note(fig, "65 倍是量级比喻，不是财务指标。应付账款是负债性占用，不需「赚回」。同口径对比见正文：全年经营现金流 29.93 亿 vs 应付净增约 189 亿。")
    footer(fig, "来源：蔚来 2025 年第四季度及全年业绩公告；应付账款增量由 FY2025 末与 2025-06-30 两期余额相减得出。")
    save(fig, "图3_首次盈利.png")


# ================================================== 图 4（正文「60 天这句话」）
def chart4():
    fig = newfig("公说 60 天，报表说 209 天",
                 "左：蔚来官方表述。右：同期披露的三个数字")
    ax = fig.add_axes([0.040, 0.105, 0.920, 0.720])
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    ax.add_patch(plt.Rectangle((0.05, 4.35), 0.10, 3.35,
                               facecolor=NAVY, edgecolor="none"))
    ax.text(0.45, 7.20, "「将持续贯彻 60 天以内的支付账期」",
            fontsize=12.2, color=DARK, weight="bold", va="center", ha="left")
    ax.text(0.45, 6.55, "蔚来官方微博，2025-06-11", fontsize=9.4,
            color=GRAY, va="center", ha="left")
    ax.text(0.45, 5.55, "这句话说的是合同。\n合同写 60 天，和供应商第 60 天拿到钱，\n是两个概念。",
            fontsize=10.4, color=SLATE, va="center", ha="left", linespacing=1.75)

    nums = [("604.0 亿元", "应付账款及票据，2026-06-30", 7.55),
            ("约 209.5 天", "按该余额与季度销货成本反推", 5.55),
            ("0.98", "2025 年末流动比率，已低于 1", 3.55)]
    for txt, src, y in nums:
        ax.add_patch(plt.Rectangle((5.15, y - 0.75), 0.10, 1.55,
                                   facecolor=RED, edgecolor="none"))
        ax.text(5.55, y + 0.30, txt, fontsize=15.0, color=RED,
                weight="bold", va="center", ha="left")
        ax.text(5.55, y - 0.38, src, fontsize=9.4, color=GRAY,
                va="center", ha="left")

    ax.plot([4.78, 4.78], [2.60, 8.70], color=LIGHT, lw=1.4)
    ax.text(2.30, 9.35, "公司措辞", fontsize=10.4, color=NAVY, weight="bold", ha="center")
    ax.text(6.65, 9.35, "报表事实", fontsize=10.4, color=RED, weight="bold", ha="center")

    note(fig, "两边都不是假的。差别在于：一个说的是条款，一个说的是已经发生的事。")
    footer(fig, "来源：蔚来官方微博经第一财经 2025-06-11 报道；蔚来 2025 年报、2026 年二季度业绩公告。"
                "209.5 天为 604.00 ÷ 262.30 × 91 的折算。")
    save(fig, "图4_措辞与报表.png")


# ================================================== 图 5（正文「60 天这句话」）
def chart5():
    fig = newfig("同一个「账期」，三个口径差了三倍",
                 "行业调研口径、第三方统计口径、按蔚来披露反推的口径")
    ax = fig.add_axes([0.085, 0.250, 0.865, 0.505])
    items = [("行业调研\n2026 年 2 月", 54.0, NAVY),
             ("第三方统计\n2026 年三季度", 127.0, SLATE),
             ("按蔚来披露反推\n2026 年二季度", 209.5, RED)]
    for i, (lab, v, c) in enumerate(items):
        ax.bar(i, v, color=c, width=0.46)
        ax.text(i, v + 7, "%.0f 天" % v, ha="center", va="bottom",
                fontsize=17, color=c, weight="bold")
    ax.axhline(60, color=AMBER, lw=1.7, ls=(0, (6, 3)))
    ax.text(2.45, 66, "承诺线 60 天", ha="right", va="bottom",
            fontsize=10.0, color=AMBER)
    ax.set_xticks(range(3))
    ax.set_xticklabels([i[0] for i in items], fontsize=10.2)
    ax.set_ylim(0, 250)
    ax.set_ylabel("天", fontsize=10, color=SLATE)
    clean(ax)

    note(fig, "三个数量的是三件事：合同怎么写、报表科目怎么转、供应商实际等多久。")
    footer(fig, "来源：中国汽车工业协会 2026 年 2 月调研报告；第三方统计（Wind，经每日经济新闻 2026-11-19 引用）；"
                "反推口径为 604.00 ÷ 262.30 × 91。")
    save(fig, "图5_三个答案.png")


# ================================================== 图 6（正文「60 天这句话」）
def chart6():
    fig = newfig("真压到 60 天，要一次性掏出 431 亿",
                 "以 604.0 亿元应付账款及票据、约 209.5 天周转为基准的静态测算")
    base, pay = 209.5, 604.0
    targets = [180, 150, 120, 90, 60]
    ax = fig.add_axes([0.085, 0.215, 0.865, 0.575])
    for i, t in enumerate(targets):
        v = pay * (base - t) / base
        c = RED if v > 430.9 else SLATE
        ax.bar(i, v, color=c, width=0.52)
        ax.text(i, v + 11, "%.0f 亿" % v, ha="center", va="bottom",
                fontsize=13.5, color=c, weight="bold")
    ax.axhline(430.9, color=GREEN, lw=1.8, ls=(0, (6, 3)))
    ax.text(4.45, 444, "全部非受限现金及短期投资 430.9 亿", ha="right",
            va="bottom", fontsize=9.8, color=GREEN)
    ax.set_xticks(range(len(targets)))
    ax.set_xticklabels(["压到 %d 天" % t for t in targets], fontsize=10.8)
    ax.set_ylim(0, 530)
    ax.set_ylabel("需要挤出的现金（亿元）", fontsize=10, color=SLATE)
    clean(ax)

    note(fig, "不是要求一天完成，也不是全部供应商都压到 60 天。它说明的是量级：这件事等于这家公司全部可动用的钱。")
    footer(fig, "测算：应付账款及票据 ×（当前周转天数 − 目标天数）÷ 当前周转天数。未考虑供应商结构、票据替代与分季执行。")
    save(fig, "图6_四百三十一亿.png")


# ================================================== 图 7（正文「60 天这句话」）
def chart7():
    fig = newfig("Non-GAAP 赚 0.26 亿，靠 5.54 亿不算成本",
                 "蔚来 2026 年第二季度，GAAP 与 non-GAAP 的全部差额（人民币亿元）")
    ax = fig.add_axes([0.095, 0.235, 0.860, 0.530])
    ax.bar(0, 5.280, bottom=-5.280, color=RED, width=0.46)
    ax.bar(1, 5.541, bottom=-5.280, color=GREEN, width=0.46)
    ax.bar(2, 0.261, bottom=0, color=NAVY, width=0.46)
    ax.axhline(0, color=SLATE, lw=1.1)
    ax.plot([0.23, 0.77], [-5.280, -5.280], color=GRAY, lw=1.0, ls=(0, (4, 3)))
    ax.plot([1.23, 1.77], [0.261, 0.261], color=GRAY, lw=1.0, ls=(0, (4, 3)))
    ax.text(0, -5.58, "-5.28", ha="center", va="top", fontsize=15, color=RED, weight="bold")
    ax.text(1, 0.60, "+5.54", ha="center", va="bottom", fontsize=15, color=GREEN, weight="bold")
    ax.text(2, 0.60, "+0.26", ha="center", va="bottom", fontsize=15, color=NAVY, weight="bold")
    for i, lab in enumerate(["GAAP 净亏损", "加回股权激励", "non-GAAP 净利润"]):
        ax.text(i, -6.30, lab, ha="center", va="top", fontsize=10.5, color=DARK)
    ax.set_xticks([])
    ax.set_xlim(-0.55, 2.55)
    ax.set_ylim(-7.4, 2.0)
    ax.set_ylabel("人民币亿元", fontsize=10, color=SLATE)
    clean(ax)

    note(fig, "5.541 亿是净亏损 5.280 亿的 105%。同期加权平均股数从 22.30 亿股增至 24.97 亿股，一年 +12%。")
    footer(fig, "来源：蔚来 2026 年二季度业绩公告「未审计 GAAP 与 non-GAAP 业绩调节表」。")
    save(fig, "图7_盈利质量.png")


# ================================================== 图 9（正文「已经贴着线走了」）
def chart8():
    fig = newfig("净营运资本改善 35.8 亿，负债端同期多拿 107 亿",
                 "流动资产减流动负债（人民币亿元）；右侧为同期两个科目的净增加额")
    ax = fig.add_axes([0.085, 0.215, 0.560, 0.575])
    bars = [("2025 年末", -19.5, RED), ("2026 年 6 月末", 16.31, GREEN)]
    for i, (lab, v, c) in enumerate(bars):
        ax.bar(i, v, color=c, width=0.46)
        ax.text(i, v + (2.4 if v > 0 else -2.4), "%.1f" % v, ha="center",
                va="bottom" if v > 0 else "top", fontsize=15.5,
                color=c, weight="bold")
    ax.axhline(0, color=SLATE, lw=1.1)
    ax.set_xticks(range(2))
    ax.set_xticklabels([b[0] for b in bars], fontsize=10.6)
    ax.set_ylim(-32, 26)
    ax.set_ylabel("人民币亿元", fontsize=10, color=SLATE)
    clean(ax)

    ax2 = fig.add_axes([0.720, 0.215, 0.245, 0.575])
    add = [("应付账款及票据\n净增加", 70.76, RED), ("借款\n净增加", 36.39, AMBER)]
    for i, (lab, v, c) in enumerate(add):
        ax2.barh(1 - i, v, color=c, height=0.42)
        ax2.text(v + 3, 1 - i, "+%.2f" % v, va="center", ha="left",
                 fontsize=12.0, color=c, weight="bold")
    ax2.set_yticks([1, 0])
    ax2.set_yticklabels([a[0] for a in add], fontsize=9.6)
    ax2.set_xlim(0, 118)
    ax2.set_title("同期科目净增加（亿元）", fontsize=9.8, color=SLATE,
                  pad=8, loc="left")
    clean(ax2, axis="x")

    note(fig, "两项不能直接相减：改善幅度 35.8 亿，负债端多拿 107 亿，差额被经营支出与资产端变化吃掉。不是靠留存收益转正的。")
    footer(fig, "来源：蔚来 2025 年报（流动比率 0.98、速动比率 0.87、流动资产 766.3 亿、流动负债 785.8 亿）；"
                "2026 年半年报（流动资产减流动负债 16.31 亿元；上半年应付账款增 70.76 亿、借款增 36.39 亿）。"
                "本图不推算未披露科目的绝对额。")
    save(fig, "图8_净营运资本.png")


# ================================================== 图 9（正文「已经贴着线走了」）
def chart9():
    fig = newfig("股东权益 40 亿，可赎回少数股东权益 102 亿",
                 "2026 年 6 月 30 日，决定清偿顺序的几个数字（人民币亿元）")
    items = [("应付账款及票据", 604.0, RED), ("借款合计", 176.1, SLATE),
             ("可赎回非控股权益", 102.2, AMBER), ("股东权益", 40.5, NAVY),
             ("流动资产减流动负债", 16.3, GRAY)]
    ax = fig.add_axes([0.255, 0.215, 0.590, 0.585])
    ys = list(range(len(items)))[::-1]
    for y, (lab, v, c) in zip(ys, items):
        ax.barh(y, v, color=c, height=0.55)
        ax.text(v + 9, y, "%.1f" % v, va="center", ha="left",
                fontsize=12.5, color=c, weight="bold")
    ax.set_yticks(ys)
    ax.set_yticklabels([i[0] for i in items], fontsize=10.5)
    ax.set_xlim(0, 720)
    clean(ax, axis="x")

    note(fig, "少数股东手里的赎回权，是股东权益的 2.5 倍。真到清算那天，排队顺序写在这张图上。")
    footer(fig, "来源：蔚来 2026 年二季度业绩公告、2026 年半年报。")
    save(fig, "图9_资本结构.png")


# ================================================== 图 10（正文「需求端」）
def chart10():
    fig = newfig("十月交付同比 −15.2%，四季度还差一个台阶",
                 "蔚来月度交付量与四季度目标的距离（辆）")
    vals = [("三季度月均", 36393, SLATE), ("10 月实际", 34246, RED),
            ("四季度目标月均", 40000, NAVY), ("11–12 月所需月均", 42877, GREEN)]
    ax = fig.add_axes([0.085, 0.215, 0.865, 0.575])
    for i, (lab, v, c) in enumerate(vals):
        ax.bar(i, v, color=c, width=0.52)
        ax.text(i, v + 700, "{:,}".format(v), ha="center", va="bottom",
                fontsize=13.5, color=c, weight="bold")
    ax.set_xticks(range(len(vals)))
    ax.set_xticklabels([v[0] for v in vals], fontsize=10.6)
    ax.set_ylim(0, 50000)
    ax.set_ylabel("辆", fontsize=10, color=SLATE)
    clean(ax)

    note(fig, "10 月是 2024 年 2 月以来第一次同比下滑。要做到单季 12 万辆，剩下两个月得月均 42,877 辆。")
    footer(fig, "来源：蔚来 2026 年 10 月交付公告、三季度交付公告；Q4「月均超过 4 万辆」为李斌公开表述；所需月均按 12 万辆倒算。")
    save(fig, "图10_四季度缺口.png")


if __name__ == "__main__":
    chart1()
    chart2()
    chart3()
    chart4()
    chart5()
    chart6()
    chart7()
    chart8()
    chart9()
    chart10()
    print("done ->", OUT)
