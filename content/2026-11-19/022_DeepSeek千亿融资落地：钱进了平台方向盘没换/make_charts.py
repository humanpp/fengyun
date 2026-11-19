# -*- coding: utf-8 -*-
"""
《DeepSeek 千亿融资落地：钱进了平台，方向盘没换》配套图表
事实口径（2026-11-19，逐条核对财新、科创板日报、The Information 转述稿后）：
  · 2026 年 11 月 17 日，杭州深度求索人工智能基础技术研究有限公司完成工商
    变更：注册资本由 1644.75 万元增至 1991.87 万元（+21.1%），新增股东杭州
    程砚企业管理咨询合伙企业（有限合伙），持股约 17.27%（财新 11-19）。
  · 同日，杭州程砚完成工商变更：注册资本由 0.6 万元增至约 34.39 亿元，
    新增 31 家有限合伙人，变更后共 32 名合伙人；执行事务合伙人仍为杭州程策
    商务咨询有限公司（财新 11-19、科创板日报 11-19）。
  · 梁文锋退出杭州程砚直接合伙人名单，但持有杭州程策 99% 股权（财新 11-19）。
  · 出资比例（科创板日报 11-19）：腾讯旗下上海珩岫 9.5653%；宁德时代三只
    基金合计 9.5653%（4.9198%+4.4410%+0.2045%）；中移投资 7.6522%；中信
    证券投资 7.6522%；砺思星深 7.1740%；国寿股权相关青岛城鑫致达 4.7826%；
    CPE 源峰、正心谷、博裕、拾象各 3.3479%；IDG 3.3236%；美团龙珠、中国
    电信、vivo、美的、高榕、君联各 2.8696%；立臻精密 2.7739%；网易 2.3913%；
    中芯聚源 1.5974%；兆易创新、上海科慧（携程关联）、横店、弘卓、中金河钢
    各 1.4348%；小红书、吉利产投各 0.9565%；中金浦成 0.4783%。
  · 融资规模 1055 亿元、投后估值 6155 亿元、近 30 家投资方、国资占比 27%
    （首轮 2%）出自 The Information 10-30 报道，经新浪财经、CNMO、观点网、
    通信世界网等转述；DeepSeek 未发布官方公告，财新 11-19 只确认工商变更。
  · 首轮：2026 年 6 月 16 日完成，约 510 亿元，投后估值近 4000 亿元；梁文锋
    个人出资约 200 亿元（投中网/投资界 06-16、企查查、凤凰网 06-18）。
  · 二轮：7 月中旬启动，初始目标 500 亿元，10 月中旬两度上调至约 1000 亿元，
    投前估值约 5000 亿元（财联社 10-13、WSJ/彭博 10-22）。
  · IPO：中信证券 9 月 9 日已进场尽调、尚未签订正式辅导协议，当时浙江证监局
    官网查不到辅导备案；辅导期不少于三个月（21 世纪经济报道 09-09）。严文韬
    9 月 21 日到岗任 CFO（路透 09-14、华尔街见闻 09-22）。
本文换算（非当事方口径）：510+1055≈1565 亿元；17.27%×6155 亿元≈1063 亿元，
与 1055 亿元互为交叉验证；投前 5000 亿+1055 亿=6055 亿，与报道的投后 6155 亿
差 100 亿元；84%×(1644.75/1991.87)≈69%，为梁文锋二轮后持股的粗略推算。
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

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep


def base(title, sub):
    fig = plt.figure(figsize=(12, 6.8))
    fig.patch.set_facecolor("white")
    fig.text(0.045, 0.950, title, fontsize=20, color=DARK, weight="bold",
             ha="left", va="top")
    fig.text(0.045, 0.876, sub, fontsize=10.4, color=GRAY, ha="left", va="top")
    return fig


def footer(fig, text):
    fig.text(0.045, 0.014, text, fontsize=8.2, color=GRAY, ha="left", va="center")


def punchline(fig, text, y=0.078):
    fig.text(0.045, y, text, fontsize=10.8, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.6", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


def canvas(fig):
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return ax


# ------------------------------------------------------------------ 图 1
def fig1():
    fig = base("四个月，一千五百亿",
               "两轮融资的时间线｜规模、估值与工商落地节点")
    ax = canvas(fig)

    ax.plot([0.055, 0.965], [0.545, 0.545], color=LIGHT, linewidth=2.0,
            solid_capstyle="round")

    nodes = [
        (0.100, "2026.04", "启动首轮", "首次引入外部资本", True),
        (0.305, "06.16", "510 亿", "首轮交割\n投后近 4000 亿", False),
        (0.510, "2026.07", "二轮启动", "目标 500 亿\n投前 5000 亿", True),
        (0.715, "10.30", "1055 亿", "报道口径\n投后 6155 亿", False),
        (0.920, "2026.11", "工商变更", "31 家入伙\n持股 17.27%", True),
    ]

    for x, date, head, note, above in nodes:
        ax.plot([x], [0.545], marker="o", markersize=8.0, color=NAVY,
                markeredgecolor="white", markeredgewidth=1.4, zorder=5)
        if above:
            ax.plot([x, x], [0.565, 0.635], color=LIGHT, linewidth=1.2)
            ax.text(x, 0.655, date, fontsize=8.4, color=GRAY, ha="center",
                    va="bottom")
            ax.text(x, 0.713, head, fontsize=11.2, color=NAVY, weight="bold",
                    ha="center", va="bottom")
            ax.text(x, 0.781, note, fontsize=8.2, color=SLATE, ha="center",
                    va="bottom", linespacing=1.5)
        else:
            ax.plot([x, x], [0.455, 0.525], color=LIGHT, linewidth=1.2)
            ax.text(x, 0.437, date, fontsize=8.4, color=GRAY, ha="center",
                    va="top")
            ax.text(x, 0.377, head, fontsize=11.2, color=NAVY, weight="bold",
                    ha="center", va="top")
            ax.text(x, 0.309, note, fontsize=8.2, color=SLATE, ha="center",
                    va="top", linespacing=1.5)

    ax.add_patch(FancyBboxPatch((0.055, 0.088), 0.910, 0.082,
                                boxstyle="round,pad=0.006",
                                facecolor="white", edgecolor=LIGHT,
                                linewidth=1.0))
    ax.text(0.080, 0.129,
            "两轮合计约 1565 亿元｜首轮 510 亿，二轮 1055 亿；"
            "从 500 亿目标到 1055 亿落地，约四个月。",
            fontsize=9.0, color=SLATE, ha="left", va="center")

    punchline(fig, "目标喊了两倍，落地的只有工商登记那一格。")
    footer(fig, "事实：财新 11-19、科创板日报 11-19、投中网 06-16、"
                "财联社 10-13、The Information 10-30（经新浪财经等转述）｜制图：本文")
    fig.savefig(OUT + "图1_四个月一千五百亿.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("31 家进了同一个平台",
               "杭州程砚出资比例｜11 月 17 日工商变更，变更后共 32 名合伙人（31 家 LP + 1 名 GP）")
    ax = canvas(fig)

    rows = [
        ("腾讯（上海珩岫）", 9.5653, NAVY),
        ("宁德时代（三只基金）", 9.5653, NAVY),
        ("中移投资", 7.6522, RED),
        ("中信证券投资", 7.6522, RED),
        ("砺思星深", 7.1740, SLATE),
        ("国寿股权（青岛城鑫）", 4.7826, RED),
        ("CPE 源峰", 3.3479, SLATE),
        ("正心谷", 3.3479, SLATE),
        ("博裕资本", 3.3479, SLATE),
        ("拾象尚势", 3.3479, SLATE),
        ("IDG 资本", 3.3236, SLATE),
        ("美团龙珠", 2.8696, SLATE),
    ]

    x0 = 0.335
    scale = 0.430 / 12.0

    y = 0.792
    for name, pct, color in rows:
        ax.text(0.028, y, name, fontsize=9.0, color=DARK, ha="left", va="center")
        ax.add_patch(Rectangle((x0, y - 0.017), pct * scale, 0.034,
                               facecolor=color, edgecolor="none"))
        ax.text(x0 + pct * scale + 0.012, y, "%.2f%%" % pct, fontsize=9.2,
                color=color, weight="bold", ha="left", va="center")
        y -= 0.0555

    ax.text(0.028, 0.128,
            "其余 19 家：中国电信、vivo、美的、高榕、君联各 2.87%；立臻精密 2.77%；"
            "网易 2.39%；中芯聚源 1.60%；",
            fontsize=8.4, color=SLATE, ha="left", va="center")
    ax.text(0.028, 0.092,
            "兆易创新、携程关联方、横店、弘卓、中金河钢各 1.43%；小红书、吉利产投各 0.96%；"
            "中金浦成 0.48%。",
            fontsize=8.4, color=SLATE, ha="left", va="center")

    ax.text(0.760, 0.822, "深蓝＝产业巨头　红＝国资与券商　灰＝市场化机构",
            fontsize=7.4, color=GRAY, ha="right", va="center")

    punchline(fig, "两家并列第一，各 9.57%；31 家加起来才凑满 100%。")
    footer(fig, "事实：科创板日报 11-19《DeepSeek 千亿融资落地：31 家出资主体现身》"
                "披露的杭州程砚出资结构；财新 11-19 确认工商变更｜制图：本文")
    fig.savefig(OUT + "图2_31家进了同一个平台.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("钱进来了，方向盘没换",
               "控制权链条｜11 月 17 日工商登记，31 家以 LP 身份出资，不参与管理")
    ax = canvas(fig)

    boxes = [
        (0.020, "梁文锋", "创始人"),
        (0.275, "杭州程策", "执行事务合伙人（GP）"),
        (0.530, "杭州程砚", "32 名合伙人：31 LP + 1 GP"),
        (0.785, "杭州深度求索", "DeepSeek 工商主体"),
    ]
    w, top, h = 0.195, 0.720, 0.190

    for x, name, role in boxes:
        ax.add_patch(FancyBboxPatch((x, top), w, h,
                                    boxstyle="round,pad=0.006",
                                    facecolor="white", edgecolor=LIGHT,
                                    linewidth=1.1))
        ax.text(x + w / 2, top + h * 0.66, name, fontsize=10.2, color=DARK,
                weight="bold", ha="center", va="center")
        ax.text(x + w / 2, top + h * 0.28, role, fontsize=7.6, color=GRAY,
                ha="center", va="center")

    arrows = [
        (0.215, 0.275, "持 99%"),
        (0.470, 0.530, "GP 控制"),
        (0.725, 0.785, "持股 17.27%"),
    ]
    for xa, xb, label in arrows:
        ax.annotate("", xy=(xb - 0.004, top + h / 2), xytext=(xa + 0.004, top + h / 2),
                    arrowprops=dict(arrowstyle="-|>", color=NAVY, linewidth=1.4,
                                    shrinkA=0, shrinkB=0))
        ax.text((xa + xb) / 2, top + h / 2 + 0.045, label, fontsize=7.6,
                color=NAVY, ha="center", va="bottom")

    ax.text(0.020, 0.610, "两条线同时变化", fontsize=10.0, color=DARK,
            weight="bold", ha="left", va="center")

    stats = [
        ("梁文锋持股", "首轮后 84%　→　二轮后约 69%", "按注册资本 1644.75 万增至 1991.87 万测算，本文推算"),
        ("国资出资占比", "首轮 2%　→　本轮 27%", "按单轮出资额占比，The Information 报道口径"),
    ]
    y = 0.540
    for label, value, note in stats:
        ax.text(0.020, y, label, fontsize=9.4, color=SLATE, ha="left", va="center")
        ax.text(0.230, y, value, fontsize=11.0, color=DARK, weight="bold",
                ha="left", va="center")
        ax.text(0.020, y - 0.052, note, fontsize=7.8, color=GRAY, ha="left",
                va="center")
        y -= 0.165

    ax.add_patch(FancyBboxPatch((0.020, 0.175), 0.960, 0.078,
                                boxstyle="round,pad=0.006",
                                facecolor="white", edgecolor=LIGHT,
                                linewidth=1.0))
    ax.text(0.044, 0.214,
            "31 家外部股东以 LP 身份进入，出资但不参与管理；"
            "梁文锋退出直接合伙人名单，仍以 GP 控制平台。",
            fontsize=8.8, color=SLATE, ha="left", va="center")

    punchline(fig, "31 家出钱，一个人签字。")
    footer(fig, "事实：财新 11-19（持股 17.27%、程策持 99%、31 家 LP）、"
                "科创板日报 11-19；84% 为首轮后持股（红星资本局 07-15）；"
                "69% 与国资占比为本文换算/引用报道｜制图：本文")
    fig.savefig(OUT + "图3_钱进来方向盘没换.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)
