# -*- coding: utf-8 -*-
"""
《吉利借雷诺卖车，小米去阿联酋卖高价：中国车企出海不再只靠建厂》配套图表
事实口径（均已核对原始来源）：
  · 2026-11-17，雷诺集团与吉利汽车宣布签署战略合作协议，雷诺阿根廷公司成为吉利
    新能源车型在阿根廷的官方经销商，雷诺开放其在阿根廷现有的经销网络、运营基础设施
    与售后服务能力。该协议非排他性，阿根廷现有吉利经销商表示合作关系仍然有效，
    短期将出现「雷诺渠道＋原有进口代理」双轨销售。协议未披露投放车型、时间表与
    销量目标。来源：雷诺阿根廷媒体室（2026-11-17）、LA NACION、Clarín、界面新闻、
    AutoCN（2026-11-18）。
  · 吉利与雷诺此前合作：韩国——吉利持雷诺韩国 34.02% 股份，共研 Grand Koleos
    累计销量约 2.2 万辆；巴西——2025 年 11 月吉利收购雷诺巴西公司 26.4% 股份，
    雷诺保持控股并合并报表，合资公司计划投入 38 亿雷亚尔推进本地化生产，2026 年 9 月
    首台巴西本地制造 Geely EX5 EM-i 在巴拉那州埃尔顿·塞纳工业园区下线，纯电 EX2
    计划 12 月投产。阿根廷这一步落在渠道层面。来源：AutoCN（2026-11-18）。
  · 阿根廷政策：第 49/2025 号与第 50/2025 号法令，离岸价不超过 1.6 万美元的电动及
    混合动力汽车可免缴 35% 南方共同市场对外关税，每年配额 5 万辆、有效期五年；
    2026 年配额分配向进口商倾斜，进口商 30720 辆、终端企业 19280 辆。市场：2025 年
    阿根廷新车登记 61.2 万辆、同比 +47.8%；电气化车型 2.6 万辆、同比 +88%，其中纯电
    1279 辆、同比 +130%，中国品牌在纯电细分约占 55%。来源：AutoCN（2026-11-18）。
  · 吉利出口：2026 年前 10 个月累计出口 90.5 万辆、同比 +168%；10 月单月 10.7 万辆，
    连续第五个月超 10 万辆；前三季度新能源出口 48.4 万辆、占出口总量 61%；拉美及非洲
    出口超 18 万辆、同比 +236%。来源：AutoCN（2026-11-18），素材方口径。
  · 小米汽车阿联酋：经销商为 Gargash Prime Automotive（Gargash 集团新设高端业务部，
    该集团 1918 年起在阿联酋经营，历史上代理奔驰、阿尔法·罗密欧、GAC 等），2026 年
    10 月中旬正式开售，共 13 个配置；质保 5 年或 15 万公里、保养至 6 万公里。
    售价：SU7 标准版 169,900 迪拉姆、YU7 标准版 184,900、澎程 SkyNomad N70 Pro
    209,900、澎程 N90 Max 249,900、SU7 Ultra 375,900。首批交付 2026 年 12 月，
    其余配置排至 2027 年 2 月。来源：tbreak（2026-10-19／20 更新）、
    gargashprimeautomotive.ae。
  · 澎程（SkyNomad）为小米汽车增程 SUV 序列的中文名，2026-07-08 官宣，与 SU7、YU7
    并列；N70 国内 20.99 万元起、N90 Max 国内 26.99 万元起（小米汽车官网）。
  · 国内售价：SU7 标准版 21.59 万元、YU7 标准版 25.35 万元（上市发布会口径）。
  · 汇率：2026-11-18 迪拉姆兑人民币约 1.815（金投网、convertworld 等），折算为
    粗略对比，未计物流、认证、关税与增值税口径差异。
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
SAND = "#f7f3ea"

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


def punchline(fig, text, y=0.078):
    fig.text(0.045, y, text, fontsize=10.8, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.6", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


# ------------------------------------------------------------------ 图 1
def fig1():
    fig = base("两件事都是「借渠道」，借的东西不一样",
               "吉利借同行的产业资产，小米借豪华车总代的零售资产")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # 左
    ax.add_patch(Rectangle((0.045, 0.255), 0.440, 0.655, facecolor="white",
                           edgecolor=LIGHT, linewidth=1.1, zorder=2))
    ax.text(0.068, 0.852, "吉利 × 雷诺", fontsize=13.0, color=NAVY,
            weight="bold", ha="left", va="center", zorder=3)
    ax.text(0.068, 0.802, "阿根廷｜借同行的产业资产", fontsize=9.4, color=GRAY,
            ha="left", va="center", zorder=3)
    left = [
        ("借什么", "经销网络、运营基础设施、\n售后与备件体系"),
        ("为什么", "不建厂、不建网点，\n用最低固定投入换覆盖面"),
        ("代价", "非排他协议，双轨并行，\n定价与售后口径待统一"),
    ]
    yy = 0.720
    for tag, body in left:
        ax.text(0.068, yy, tag, fontsize=9.0, color=RED, weight="bold",
                ha="left", va="center", zorder=3)
        ax.text(0.068, yy - 0.062, body, fontsize=8.8, color=SLATE, ha="left",
                va="center", linespacing=1.7, zorder=3)
        yy -= 0.155

    # 右
    ax.add_patch(Rectangle((0.515, 0.255), 0.440, 0.655, facecolor="white",
                           edgecolor=RED, linewidth=1.1, zorder=2))
    ax.text(0.538, 0.852, "小米 × Gargash", fontsize=13.0, color=RED,
            weight="bold", ha="left", va="center", zorder=3)
    ax.text(0.538, 0.802, "阿联酋｜借豪华车总代的零售资产", fontsize=9.4,
            color=GRAY, ha="left", va="center", zorder=3)
    right = [
        ("借什么", "高端门店、本地质保承诺、\n交付与售后服务"),
        ("为什么", "把零售与售后整体交出去，\n自己只管产品与品牌"),
        ("代价", "交付排到 2027 年 2 月，\n溢价能否守住待验证"),
    ]
    yy = 0.720
    for tag, body in right:
        ax.text(0.538, yy, tag, fontsize=9.0, color=RED, weight="bold",
                ha="left", va="center", zorder=3)
        ax.text(0.538, yy - 0.062, body, fontsize=8.8, color=SLATE, ha="left",
                va="center", linespacing=1.7, zorder=3)
        yy -= 0.155

    ax.plot([0.500, 0.500], [0.255, 0.910], color=LIGHT, linewidth=1.0,
            linestyle=(0, (4, 4)))

    ax.add_patch(FancyBboxPatch((0.045, 0.120), 0.910, 0.108,
                                boxstyle="round,pad=0.012", facecolor=SAND,
                                edgecolor="#d9cdb6", linewidth=1.0, zorder=2))
    ax.text(0.500, 0.174,
            "一个借「能不能把车修好」，一个借「能不能把车卖贵」。",
            fontsize=10.6, color="#7a6746", ha="center", va="center", zorder=3)

    punchline(fig, "都不建厂，但一个补服务短板，一个补品牌溢价。")
    footer(fig, "依据：雷诺阿根廷媒体室与吉利公告（2026-11-17）、Gargash Prime Automotive 官方渠道｜制图：本文")
    fig.savefig(OUT + "图1_借渠道但借的东西不一样.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("从股权到渠道：同一对伙伴，第三次合作",
               "介入越来越轻，复制越来越快")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    panels = [
        ("韩国", "股权", "吉利持雷诺韩国 34.02% 股份",
         "双方共研 Grand Koleos\n累计销量约 2.2 万辆", NAVY),
        ("巴西", "股权＋产能", "吉利收购雷诺巴西 26.4% 股份",
         "合资计划投入 38 亿雷亚尔\n2026 年 9 月首台本地车下线", NAVY),
        ("阿根廷", "仅渠道", "雷诺阿根廷成官方经销商",
         "借经销网络与售后体系\n协议非排他，双轨并行", RED),
    ]

    xs = [0.045, 0.355, 0.665]
    for (country, mode, line1, line2, color), x in zip(panels, xs):
        ax.add_patch(Rectangle((x, 0.360), 0.290, 0.520, facecolor="white",
                               edgecolor=color, linewidth=1.2, zorder=2))
        ax.text(x + 0.022, 0.800, country, fontsize=13.0, color=color,
                weight="bold", ha="left", va="center", zorder=3)
        ax.add_patch(FancyBboxPatch((x + 0.022, 0.706), 0.150, 0.058,
                                    boxstyle="round,pad=0.008",
                                    facecolor=PALE, edgecolor="none",
                                    zorder=3))
        ax.text(x + 0.097, 0.735, mode, fontsize=8.8, color=color,
                weight="bold", ha="center", va="center", zorder=4)
        ax.plot([x + 0.022, x + 0.268], [0.672, 0.672], color=LIGHT,
                linewidth=0.9, zorder=3)
        ax.text(x + 0.022, 0.612, line1, fontsize=8.8, color=DARK, ha="left",
                va="center", zorder=3)
        ax.text(x + 0.022, 0.510, line2, fontsize=8.6, color=SLATE, ha="left",
                va="center", linespacing=1.75, zorder=3)

    # 方向箭头
    for x0 in (0.040, 0.350):
        ax.annotate("", xy=(x0 + 0.310, 0.240), xytext=(x0 + 0.288, 0.240),
                    arrowprops=dict(arrowstyle="->", color=GRAY, lw=1.2))
    ax.plot([0.045, 0.955], [0.240, 0.240], color=LIGHT, linewidth=1.0)
    ax.text(0.045, 0.196, "重资产", fontsize=9.0, color=GRAY, ha="left",
            va="center")
    ax.text(0.955, 0.196, "轻资产", fontsize=9.0, color=RED, ha="right",
            va="center")
    ax.text(0.500, 0.286, "介入深度递减", fontsize=9.0, color=SLATE,
            ha="center", va="center")

    punchline(fig, "同一个伙伴，从买股权、建产能，一路走到只借一张网。")
    footer(fig, "依据：AutoCN（2026-11-18）、雷诺阿根廷媒体室、吉利与雷诺合作公告｜制图：本文")
    fig.savefig(OUT + "图2_从股权到渠道.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("阿联酋卖得比国内贵，而且越贵越多",
               "同一配置、两端起售价对比（万元人民币，迪拉姆按 1:1.815 折算）")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    rows = [
        ("SU7 标准版", 21.59, 30.84, 9.25),
        ("YU7 标准版", 25.35, 33.56, 8.21),
        ("澎程 N90 Max", 26.99, 45.36, 18.37),
    ]

    ax.plot([0.160, 0.160], [0.230, 0.880], color=LIGHT, linewidth=1.1)
    ax.text(0.160, 0.912, "0", fontsize=8.6, color=GRAY, ha="center",
            va="center")

    scale = 0.0108  # 每万元对应的横向宽度
    ys = [0.760, 0.550, 0.340]

    for (name, cn, ae, gap), y in zip(rows, ys):
        ax.text(0.135, y + 0.058, name, fontsize=10.6, color=DARK,
                weight="bold", ha="right", va="center")
        # 国内
        w1 = cn * scale
        ax.add_patch(Rectangle((0.170, y + 0.006), w1, 0.048,
                               facecolor=GRAY, edgecolor="none", zorder=3))
        ax.text(0.170 + w1 + 0.012, y + 0.030, f"国内 {cn:.2f}", fontsize=9.0,
                color=SLATE, ha="left", va="center", zorder=4)
        # 阿联酋
        w2 = ae * scale
        ax.add_patch(Rectangle((0.170, y - 0.062), w2, 0.048,
                               facecolor=NAVY, edgecolor="none", zorder=3))
        ax.text(0.170 + w2 + 0.012, y - 0.038, f"阿联酋 {ae:.2f}", fontsize=9.0,
                color=NAVY, weight="bold", ha="left", va="center", zorder=4)
        # 差价
        ax.text(0.170 + w2 + 0.115, y - 0.038, f"+{gap:.1f}", fontsize=10.4,
                color=RED, weight="bold", ha="left", va="center", zorder=4)

    ax.plot([0.045, 0.955], [0.230, 0.230], color=LIGHT, linewidth=1.1)
    ax.text(0.955, 0.196, "单位：万元人民币　｜　右端红色为折算差价",
            fontsize=8.4, color=GRAY, ha="right", va="center")

    punchline(fig, "旧的印象是中国车在海外只能卖便宜，这份价目表正好相反。")
    footer(fig, "售价：Gargash Prime Automotive 官网（2026-10）；国内价据上市发布会与小米汽车官网；汇率为 2026-11-18 中间价，口径差异见文末｜制图：本文")
    fig.savefig(OUT + "图3_阿联酋售价比国内贵多少.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)
