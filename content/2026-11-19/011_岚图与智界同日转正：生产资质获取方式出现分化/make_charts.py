# -*- coding: utf-8 -*-
"""
《岚图与智界同日「转正」：生产资质获取方式出现分化》配套图表
事实口径（2026-11-19，逐条核对工信部公告与公开报道后）：
  · 工信部 2026 年 11 月 16 日发布 2026 年第 31 号公告，公布《道路机动车辆生产企业及产品》
    （第 412 批）目录：同意东风集团增加成员企业岚图汽车科技股份有限公司，同意奇瑞集团
    增加成员企业安徽智界新能源汽车有限公司（工信部公告、36氪 11-18、观点网 11-17、凤凰网 11-18）；
  · 第 412 批公示期为 10 月 16 日；公示中智界列入「拟发布新准入车辆生产企业」清单，
    同一份文件中奇瑞汽车股份有限公司申请注销该地址的生产资质（虎嗅 10-19）；
  · 岚图生产地址：湖北省武汉市汉阳区永丰环路 1 号、武汉经开区云峰大道 8 号；
    东风汽车有限公司同期注销「武汉经开区军山街云峰大道 8 号」（EET-China 11-18、凤凰网 11-18）；
  · 智界：注册地址芜湖经开区龙山街道华山路与千岛湖路交叉口管委会 15 楼 1507 室，
    生产地址芜湖经开区皖江大道 8 号，备注「奇瑞集团成员企业」；股权为奇瑞股份 85%、
    芜湖瑞启与芜湖瑞联各 7.5%（盖世汽车 11-19、凤凰网 11-18）；
  · 智界是鸿蒙智行「五界」中首个取得独立整车生产资质的品牌；此前 S7、R7 依托奇瑞资质申报，
    车尾铭牌须标「奇瑞汽车」（盖世汽车 11-19、IT之家 11-18）；
  · 岚图 2026 年 3 月 19 日以介绍方式在港交所主板挂牌（07489.HK），为「央国企高端新能源
    汽车第一股」，东风集团股份同步私有化退市（东风汽车集团官网 3-20、新华网 3-19）；
  · 智界品牌 2023 年 11 月发布，S7 于 2023 年 11 月 28 日上市；2026 年 11 月恰逢品牌三周年
    （新华网 2023-11-28、新浪 11-18）；
  · 法律依据：《道路机动车辆生产企业及产品准入管理办法》（工信部令第 50 号，2019 年 6 月 1 日
    施行）第二十五条——鼓励实施企业集团化管理，工业和信息化部可以简化其成员企业的准入审查
    要求；第二十八条允许委托加工生产（中国政府网、人民网 2018-12-09）。
风格：克制传媒风，白底、低饱和配色、标题即结论。输出目录 = 脚本所在目录。
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch, FancyArrowPatch

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


# ------------------------------------------------------------------ 图 1
def fig1():
    fig = base("一个月，四步，从公示到落地",
               "资质不是突然发下来的，它在公示名单里已经挂了一个月")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    steps = [
        ("10 月 16 日", "公示", "第 412 批公示：智界列入\n拟发布新准入企业清单", SLATE),
        ("11 月 16 日", "公告", "工信部 2026 年第 31 号公告\n第 412 批目录正式发布", NAVY),
        ("11 月 17 日", "披露", "岚图在港交所\n发布自愿公告", NAVY),
        ("11 月 18 日", "落地", "报道铺开；智界回应\n恰逢品牌三周年", RED),
    ]

    centers = [0.132, 0.376, 0.620, 0.864]
    for (date, head, body, color), cx in zip(steps, centers):
        ax.text(cx, 0.800, date, fontsize=9.4, color=GRAY, weight="bold",
                ha="center", va="center")
        ax.add_patch(FancyBboxPatch((cx - 0.098, 0.600), 0.196, 0.120,
                                    boxstyle="round,pad=0.008",
                                    facecolor="white", edgecolor=color,
                                    linewidth=1.2))
        ax.text(cx, 0.660, head, fontsize=12.0, color=color, weight="bold",
                ha="center", va="center")
        ax.text(cx, 0.512, body, fontsize=8.4, color=SLATE, ha="center",
                va="center", linespacing=1.9)

    for i in range(3):
        ax.add_patch(FancyArrowPatch((centers[i] + 0.100, 0.660),
                                     (centers[i + 1] - 0.100, 0.660),
                                     arrowstyle="-|>", mutation_scale=14,
                                     color=LIGHT, linewidth=1.6))

    ax.plot([0.030, 0.960], [0.402, 0.402], color=LIGHT, linewidth=0.9)
    ax.text(0.030, 0.344,
            "公示期这一步最容易被漏掉：10 月 16 日那份公示里，奇瑞汽车已同步申请注销"
            "该生产地址的资质。",
            fontsize=9.2, color=SLATE, ha="left", va="center")
    ax.text(0.030, 0.276,
            "也就是说，这条资质不是新造出来的，是从集团另一个主体名下腾出来的。",
            fontsize=9.2, color=DARK, ha="left", va="center")

    punchline(fig, "一个月的公示期，才是这批「准生证」真正的成本。")
    footer(fig, "事实：工信部 2026 年第 31 号公告 11-16、第 412 批公示 10-16（虎嗅 10-19）、"
                "岚图港交所自愿公告 11-17｜制图：本文")
    fig.savefig(OUT + "图1_一个月四步.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("三条路径，本次走的是第三条",
               "《准入管理办法》第二十五条：工信部可以简化企业集团成员企业的准入审查要求")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    paths = [
        ("路径一", "从零申请一张新牌照",
         "完整走一遍企业准入审查，产能、厂房、一致性保证能力逐项核", "周期最长", LIGHT),
        ("路径二", "收购一家已持牌的企业",
         "花钱买主体，资质随股权过来", "一次性现金支出", LIGHT),
        ("路径三", "集团成员企业身份列入目录",
         "依托集团既有资质体系，把子公司单列进准入名单", "本次两家走的路", RED),
    ]

    yy = 0.740
    for tag, name, desc, note, color in paths:
        if color is RED:
            ax.add_patch(FancyBboxPatch((0.030, yy - 0.108), 0.940, 0.186,
                                        boxstyle="round,pad=0.008",
                                        facecolor=PALE, edgecolor="none"))
        ax.text(0.058, yy + 0.036, tag, fontsize=9.0, color=GRAY, ha="left",
                va="center")
        ax.text(0.058, yy - 0.014, name, fontsize=12.4,
                color=RED if color is RED else DARK, weight="bold",
                ha="left", va="center")
        ax.text(0.400, yy + 0.006, desc, fontsize=9.0, color=SLATE,
                ha="left", va="center")
        ax.text(0.790, yy + 0.006, note, fontsize=8.8,
                color=RED if color is RED else GRAY, weight="bold",
                ha="left", va="center")
        yy -= 0.222

    ax.plot([0.030, 0.960], [0.180, 0.180], color=LIGHT, linewidth=0.9)
    ax.text(0.030, 0.120,
            "第三条文义上仍是「准入」，但审查强度被集团背书吸收掉一部分——"
            "拿到的是独立主体资格，不是独立于集团之外的资格。",
            fontsize=9.2, color=SLATE, ha="left", va="center")

    punchline(fig, "资质的分量没变，变的是它从哪个门进来。")
    footer(fig, "事实：《道路机动车辆生产企业及产品准入管理办法》（工信部令第 50 号）第二十五条、"
                "第二十八条；两条路径的说明据公开报道整理｜制图：本文")
    fig.savefig(OUT + "图2_三条路径.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("同一批目录，两种处境",
               "一边是上市八个月的资本平台，一边是刚满三年的品牌")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    heads = [
        (0.235, "岚图汽车", "东风集团", NAVY, "07489.HK"),
        (0.615, "安徽智界", "奇瑞集团", RED, "奇瑞股份持股 85%"),
    ]
    for x, name, group, color, extra in heads:
        ax.add_patch(Rectangle((x, 0.796), 0.345, 0.006, facecolor=color,
                               edgecolor="none"))
        ax.text(x, 0.756, name, fontsize=13.0, color=color, weight="bold",
                ha="left", va="center")
        ax.text(x, 0.706, group, fontsize=9.2, color=GRAY, ha="left",
                va="center")
        ax.text(x, 0.652, extra, fontsize=8.8, color=SLATE, ha="left",
                va="center")

    rows = [
        ("生产地址", "武汉汉阳永丰环路 1 号、\n武汉经开区云峰大道 8 号", "芜湖经开区\n皖江大道 8 号"),
        ("原持牌方同批动作", "东风汽车有限公司注销\n「军山街云峰大道 8 号」", "奇瑞汽车股份注销\n该地址生产资质"),
        ("此前怎么申报", "整车公告依托东风集团资质", "S7、R7 依托奇瑞资质，\n尾标须写「奇瑞汽车」"),
        ("资质落地时点", "2026 年 3 月 19 日已在港交所\n主板上市，资质晚于上市", "品牌 2023 年 11 月发布，\n本批恰逢三周年"),
    ]

    yy = 0.560
    for label, left, right in rows:
        ax.text(0.030, yy, label, fontsize=8.8, color=GRAY, ha="left",
                va="center")
        ax.text(0.235, yy, left, fontsize=8.9, color=DARK, ha="left",
                va="center", linespacing=1.7)
        ax.text(0.615, yy, right, fontsize=8.9, color=DARK, ha="left",
                va="center", linespacing=1.7)
        ax.plot([0.030, 0.960], [yy - 0.078, yy - 0.078], color=LIGHT,
                linewidth=0.8)
        yy -= 0.118

    ax.text(0.030, 0.066,
            "智界是鸿蒙智行「五界」中首个拿到独立整车生产资质的品牌。",
            fontsize=9.0, color=SLATE, ha="left", va="center")

    punchline(fig, "资本先行还是品牌先行都不重要，两家的资质都在替各自的下一个动作开路。")
    footer(fig, "事实：地址与注销动作据工信部公告及凤凰网 11-18、盖世汽车 11-19；"
                "岚图上市据港交所与东风集团官网；智界三周年据新浪 11-18｜制图：本文")
    fig.savefig(OUT + "图3_同一批两种处境.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)
