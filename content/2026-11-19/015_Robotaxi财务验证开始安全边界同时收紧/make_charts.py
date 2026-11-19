# -*- coding: utf-8 -*-
"""
《Robotaxi：财务验证开始，安全边界同时收紧》配套图表
事实口径（2026-11-19，逐条核对财报原文与公开报道后）：
  · 小马智行（Pony.ai，02026.HK）2026 年 11 月 18 日晚间公布第三季度未经审计业绩：
    总收入 4,460 万美元（约人民币 2.99 亿元），同比 +75.2%，环比 +23.1%，创上市以来单季新高；
    自动驾驶出行服务（Robotaxi）收入 1,780 万美元（约 1.19 亿元），同比 +165.4%、环比 +47.1%，
    占总收入 39.9%（去年同期 26.3%）；Robotruck 收入 1.20 亿元，同比 +76.3%、环比 +34.7%；
    毛利 5,310 万元、同比 +69.5%，毛利率 17.8%；GAAP 经营亏损约 4.61 亿元、同比基本持平，
    Non-GAAP 经营亏损约 3.91 亿元、同比收窄 7.6%；GAAP 净亏损 9.14 亿元、同比扩大逾一倍，
    主要来自交易性金融资产公允价值变动亏损，Non-GAAP 净亏损约 3.28 亿元、同比收窄 13.9%；
    乘客车费收入同比增长接近 400%
    （公司业绩公告与电话会记录、第一财经 11-18、澎湃 11-18、新浪财经 11-18、AutoCN 11-19、OFweek 11-19）；
  · 截至 2026 年 9 月 30 日 Robotaxi 车队 2,768 台（二季度末 1,975 台，单季增 793 台），
    全年目标 3,500 台；广州原市中心城区与南沙区两个独立运营区域已连通为一个覆盖超 1,000 平方公里的
    相连运营区域（公司称接近旧金山市面积九倍）；上海浦东新区新获许可无人驾驶车辆纳入持续示范运营；
    杭州、重庆、珠海横琴启动部署；海外向伦敦、曼彻斯特等欧洲城市扩张，9 月在克罗地亚萨格勒布
    启动欧洲首个全无人驾驶载客服务（业绩公告、电话会记录、新浪财经 11-18）；
  · 港股 11 月 18 日收报 31.78 港元，连续第二个交易日创上市新低（AutoCN 11-19）；
  · 同一周监管动作：加州车辆管理局（DMV）限制令 11 月 11 日生效，禁止 Waymo 在加州任何高速公路
    运营或测试无人车，理由为「对公共安全的紧迫危险」，该命令六天后才被媒体披露；Waymo 随后暂停
    全美高速公路无人载客服务；两起触发事件均未造成碰撞与伤亡，加州方面的处理指向整改失效
    （NBC News 11-17、华盛顿邮报 11-18、OFweek 11-19）；
  · NHTSA 于 11 月 10 日针对 Waymo 2,895 台搭载第五代自动驾驶系统的车辆发起召回查询（RQ26006），
    核查校车避让软件修复是否生效（车联网 11-10）；
  · 新加坡：11 月 5 日两辆自驾车在榜鹅一带分别差点撞上行人和车辆，陆交局 11 月 11 日表示
    正与业者检讨，必要时暂停或撤销运营许可（联合早报 11-11）；
  · 中国：道路交通安全法修订草案提请十四届全国人大常委会第二十四次会议初次审议，
    新增「自动驾驶汽车的特别规定」专章（中国人大网 11-10）。
本文换算（非当事方口径）：GAAP 经营亏损 4.61 亿 ÷ 营收 2.99 亿 ≈ 1.54 倍；
GAAP 净亏损 9.14 亿 ÷ 营收 2.99 亿 ≈ 3.06 倍。
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

REV = 2.99
ROBOTAXI = 1.19
ROBOTRUCK = 1.20
OP_LOSS = 4.61
NET_LOSS = 9.14

OP_RATIO = OP_LOSS / REV
NET_RATIO = NET_LOSS / REV


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
    fig = base("跑得最快的那条线，还不是最大的那条",
               "2026 年第三季度｜单位：亿元人民币")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    x0 = 0.290
    scale = 0.470 / 3.0

    bars = [
        ("Robotaxi", "自动驾驶出行服务", ROBOTAXI, RED,
         "同比 +165.4%　环比 +47.1%", 0.740),
        ("Robotruck", "自动驾驶卡车", ROBOTRUCK, SLATE,
         "同比 +76.3%　环比 +34.7%", 0.550),
        ("总计", "合计收入", REV, NAVY,
         "同比 +75.2%　创单季新高", 0.360),
    ]

    for name, sub, v, color, note, y in bars:
        ax.add_patch(Rectangle((x0, y - 0.044), v * scale, 0.088,
                               facecolor=color, edgecolor="none"))
        ax.text(0.030, y + 0.028, name, fontsize=11.0, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(0.030, y - 0.024, sub, fontsize=8.2, color=GRAY, ha="left",
                va="center")
        ax.text(x0 + v * scale + 0.016, y + 0.016, "%.2f 亿元" % v,
                fontsize=13.4, color=DARK, weight="bold", ha="left",
                va="center")
        ax.text(x0 + v * scale + 0.016, y - 0.030, note, fontsize=8.2,
                color=GRAY, ha="left", va="center")

    ax.add_patch(FancyBboxPatch((0.030, 0.120), 0.940, 0.100,
                                boxstyle="round,pad=0.008",
                                facecolor="white", edgecolor=LIGHT,
                                linewidth=1.0))
    ax.text(0.055, 0.190, "营收占比", fontsize=8.6, color=GRAY, ha="left",
            va="center")
    ax.text(0.055, 0.148,
            "Robotaxi 39.9%（去年同期 26.3%）　｜　"
            "两条业务线金额几乎持平，增速相差一倍以上",
            fontsize=9.4, color=SLATE, ha="left", va="center")

    punchline(fig, "Robotaxi 撑起了四成营收，但卡车的绝对额还略高一点。")
    footer(fig, "事实：小马智行 2026 年第三季度业绩公告及电话会记录；单位换算按公告披露口径｜"
                "制图：本文")
    fig.savefig(OUT + "图1_两条业务线几乎持平.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("收入在涨，亏损还在",
               "2026 年第三季度｜GAAP 口径，单位：亿元人民币")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    x0 = 0.290
    scale = 0.400 / 9.6

    bars = [
        ("营收", "同比 +75.2%", REV, NAVY, 0.790),
        ("经营亏损", "同比基本持平", OP_LOSS, RED, 0.590),
        ("净亏损", "同比扩大逾一倍", NET_LOSS, RED, 0.390),
    ]

    for name, note, v, color, y in bars:
        ax.add_patch(Rectangle((x0, y - 0.044), v * scale, 0.088,
                               facecolor=color, edgecolor="none"))
        ax.text(0.030, y + 0.026, name, fontsize=11.0, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(0.030, y - 0.026, note, fontsize=8.2, color=GRAY, ha="left",
                va="center")
        ax.text(x0 + v * scale + 0.016, y, "%.2f 亿元" % v, fontsize=13.4,
                color=DARK, weight="bold", ha="left", va="center")

    ax.add_patch(FancyBboxPatch((0.030, 0.108), 0.940, 0.104,
                                boxstyle="round,pad=0.008",
                                facecolor="white", edgecolor=LIGHT,
                                linewidth=1.0))
    ax.text(0.055, 0.178,
            "经营亏损约为营收的 %.1f 倍；净亏损约为营收的 %.1f 倍"
            % (OP_RATIO, NET_RATIO),
            fontsize=9.6, color=SLATE, ha="left", va="center")
    ax.text(0.055, 0.134,
            "净亏损扩大主要来自交易性金融资产公允价值变动；Non-GAAP 经营亏损 3.91 亿元，同比收窄 7.6%，"
            "毛利率 17.8%。",
            fontsize=8.6, color=GRAY, ha="left", va="center")

    punchline(fig, "收入端验证了增长，盈利端还没有。")
    footer(fig, "事实：小马智行 2026 年第三季度业绩公告；倍数关系为本文按公告数字换算｜制图：本文")
    fig.savefig(OUT + "图2_收入在涨亏损还在.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("同一周，安全边界在收紧",
               "2026 年 11 月 10—18 日｜全球监管动作与小马财报落在同一周")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    items = [
        ("11 月 10 日", "美国", "NHTSA 对 Waymo 2,895 台车\n发起召回查询", SLATE),
        ("11 月 11 日", "美国 · 加州", "DMV 限制令生效：\n禁止在加州高速运营与测试", RED),
        ("11 月 11 日", "新加坡", "陆交局：正与业者检讨，\n必要时暂停或撤销许可", SLATE),
        ("11 月 17 日", "美国", "禁令被披露，Waymo 暂停\n全美高速无人载客", RED),
        ("11 月 18 日", "中国", "小马智行 Q3 财报：\nRobotaxi 收入 +165.4%", NAVY),
    ]

    ax.plot([0.118, 0.118], [0.170, 0.800], color=LIGHT, linewidth=1.4)

    yy = 0.760
    for date, place, note, color in items:
        ax.plot([0.118], [yy], marker="o", markersize=7.0, color=color, zorder=3)
        ax.text(0.048, yy, date, fontsize=9.2, color=GRAY, weight="bold",
                ha="right", va="center")
        ax.text(0.148, yy + 0.020, place, fontsize=9.6, color=color,
                weight="bold", ha="left", va="center")
        ax.text(0.400, yy + 0.020, note, fontsize=8.8, color=DARK, ha="left",
                va="center", linespacing=1.7)
        yy -= 0.140

    ax.plot([0.030, 0.960], [0.108, 0.108], color=LIGHT, linewidth=0.9)
    ax.text(0.030, 0.062,
            "另：中国《道路交通安全法》修订草案新增「自动驾驶汽车的特别规定」专章，已提请初次审议。",
            fontsize=8.6, color=SLATE, ha="left", va="center")

    punchline(fig, "规模在扩，审查也在跟——这两件事现在同步发生。")
    footer(fig, "事实：NHTSA 查询据车联网 11-10；加州 DMV 限制令据 NBC News 11-17、华盛顿邮报 11-18；"
                "新加坡据联合早报 11-11；财报据公司公告 11-18｜制图：本文")
    fig.savefig(OUT + "图3_同一周安全边界收紧.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)