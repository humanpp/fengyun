# -*- coding: utf-8 -*-
"""
《出海路径：从「宣布计划」到「落地产能与运力」》配套图表
事实口径（2026-11-19，逐条核对厂商公告、路透与公开报道后）：
  · 腾势（DENZA，比亚迪集团旗下）于当地时间 2026 年 11 月 13 日在孟买举行品牌发布活动，
    正式进入印度市场，首批推出 D9（七座纯电 MPV）与 Z9 GT（纯电猎装）两款车型，
    均以整车进口方式进入；D9 起售价 900 万印度卢比（约合人民币 64.2 万元），
    Z9 GT 起售价 1,568 万印度卢比（约合人民币 111.8 万元）；11 月 17 日对外宣布，
    11 月 18 日为媒体集中报道日（BAR 印度官网、盖世汽车 11-17、IT之家 11-17、观察者网 11-18）；
  · 捷途（Jetour，奇瑞集团旗下）2026 年 11 月 18 日（周三）宣布，明年将在巴西启动本地生产，
    从 T1 与 T2 两款 SUV 开始；投资 4 亿雷亚尔（约 6,860 万—6,900 万美元），
    为在此前已宣布的同等规模投资之外的追加投入；厂址选在里约热内卢州，具体地址尚未确认；
    捷途今年刚进入巴西市场，已售出超 8,000 辆、推出六款车型
    （路透 11-18、工商时报 11-19、观点网 11-19、AASTOCKS 11-18、Folha 11-18）；
  · 长安汽车、长安民生物流与中远海运特运于 2026 年 11 月 16 日在重庆签署合资合作意向协议，
    计划研究设立合资公司、打造汽车滚装运力平台，打通整车海外运输、航线运营、海外码头配套；
    签约在中远海运集团西南区域总部揭牌仪式上完成，属重庆推进西部陆海新通道、
    支持渝车出海的重点项目；需注意为「意向协议」，合资主体尚待设立；
    中远海运特运与长安民生物流早在 2023 年 7 月 17 日已在江苏太仓成立汽车供应链合资公司
    （界面新闻 11-19、东方财富 11-19、中华航运网 2023-07-18、汽车殿堂网 11-19）；
  · 滚装运力背景：2026 年上半年中国汽车出口 509.6 万辆、同比增 65.3%；
    1—7 月累计 639.9 万辆、同比增 53.7%，6 月单月首破百万辆、7 月 109.2 万辆；
    6500 车位（CEU）滚装船一年期期租租金 2026 年 9 月约 9.5 万美元 / 天，
    较当年均值高 43%、较五年均值高 21%；市场平均日租金约 6.7 万美元，
    部分新船成交逼近 9 万美元；主流船厂排产已到 2030 年以后；
    2028 年起新船集中交付，供需格局可能改变（中汽协数据经多家转述、Intermodal 周报经华球通 10-27、
    海事服务网 8-05、中新网 9-11）。
本文换算（非当事方口径）：9.5 万美元 / 天 × 365 ≈ 3,468 万美元 / 年 / 艘；
6,860 万美元 ÷ 3,468 万美元 ≈ 1.98 年，即一艘 6500CEU 船约两年的租金，
与捷途巴西建厂投资相当；4 亿雷亚尔按 6,860 万美元口径折算。
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
SAND_EDGE = "#d9cdb6"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep

RATE_DAY = 9.5            # 万美元/天
RATE_YEAR = RATE_DAY * 365
FACTORY = 6860.0          # 万美元
YEARS = FACTORY / RATE_YEAR


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
    fig = base("三种出海，三种下注的厚度",
               "同一周的三条消息，落在出海链条的不同位置")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    rows = [
        ("轻", "卖品牌", "腾势 · 印度", NAVY,
         "整车进口，两款旗舰直接切入",
         "D9 约 64.2 万元｜Z9 GT 约 111.8 万元", 0.784),
        ("中", "建产能", "捷途 · 巴西", SLATE,
         "本地生产，从 T1、T2 两款 SUV 起",
         "4 亿雷亚尔（约 6,860 万美元），2027 年投产", 0.536),
        ("重", "持运力", "长安 × 中远海运特运", RED,
         "设合资公司，持有滚装运力平台",
         "意向协议阶段，合资主体尚待设立", 0.288),
    ]

    for tag, head, name, color, desc, detail, y in rows:
        ax.add_patch(Rectangle((0.030, y - 0.086), 0.940, 0.172,
                               facecolor="white", edgecolor=LIGHT,
                               linewidth=1.0))
        ax.add_patch(Rectangle((0.030, y - 0.086), 0.006, 0.172,
                               facecolor=color, edgecolor="none"))
        ax.text(0.062, y + 0.058, tag, fontsize=15.0, color=color,
                weight="bold", ha="left", va="center")
        ax.text(0.062, y + 0.004, head, fontsize=10.0, color=GRAY,
                ha="left", va="center")
        ax.text(0.150, y + 0.038, name, fontsize=12.0, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(0.150, y - 0.016, desc, fontsize=8.8, color=SLATE, ha="left",
                va="center")
        ax.text(0.150, y - 0.056, detail, fontsize=8.8, color=color,
                ha="left", va="center")

    ax.text(0.030, 0.128,
            "越往下，投进去的钱离「卖一台车」越远：一层是产品定价权，一层是产能，"
            "一层是整条链路能不能按自己的节奏走。",
            fontsize=9.2, color=SLATE, ha="left", va="center")

    punchline(fig, "出海这件事，已经从「进不进得去」变成「进去了靠什么站着」。")
    footer(fig, "事实：腾势据其印度官网与盖世汽车 11-17；捷途据路透 11-18、观点网 11-19；"
                "长安三方据界面新闻、东方财富 11-19｜制图：本文")
    fig.savefig(OUT + "图1_三种出海三种厚度.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("一艘船跑两年，等于一座厂的投资",
               "6500 车位滚装船 2026 年 9 月一年期期租约 9.5 万美元 / 天")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    x0 = 0.330
    scale = 0.400 / 7600.0

    bars = [
        ("一艘船 · 一年租金", "9.5 万美元 / 天 × 365", RATE_YEAR, SLATE, 0.720),
        ("一艘船 · 两年租金", "同上 × 2", RATE_YEAR * 2, RED, 0.500),
        ("捷途巴西 · 建厂投资", "4 亿雷亚尔", FACTORY, NAVY, 0.280),
    ]

    for name, note, v, color, y in bars:
        ax.add_patch(Rectangle((x0, y - 0.042), v * scale, 0.084,
                               facecolor=color, edgecolor="none"))
        ax.text(0.030, y + 0.030, name, fontsize=10.2, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(0.030, y - 0.016, note, fontsize=8.4, color=GRAY, ha="left",
                va="center")
        ax.text(x0 + v * scale + 0.016, y, "约 %.0f 万美元" % v, fontsize=13.0,
                color=DARK, weight="bold", ha="left", va="center")

    ax.add_patch(FancyBboxPatch((0.030, 0.112), 0.940, 0.062,
                                boxstyle="round,pad=0.006",
                                facecolor=SAND, edgecolor=SAND_EDGE,
                                linewidth=0.9))
    ax.text(0.055, 0.143,
            "按 9.5 万美元 / 天算，两年租金约 6,935 万美元，"
            "与捷途在巴西的 6,860 万美元建厂投入基本相当（约 %.2f 年追平）。"
            % YEARS,
            fontsize=9.2, color="#7a6746", ha="left", va="center")

    punchline(fig, "这就是为什么车企开始算运力的账：它已经不是一笔运输费，是一笔资本开支。")
    footer(fig, "事实：租金据 Intermodal 周报（2026 年 9 月 6500CEU 一年期期租约 9.5 万美元 / 天，"
                "经华球通 10-27 转述）；建厂投资据路透 11-18｜换算为本文所作，非当事方口径｜制图：本文")
    fig.savefig(OUT + "图2_一艘船两年等于一座厂.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("为什么运力突然成了瓶颈",
               "出口在涨，船在紧，新船要等")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    cards = [
        (0.030, 0.760, "出口", "509.6 万辆", "2026 年上半年，同比 +65.3%", NAVY),
        (0.515, 0.760, "月度", "109.2 万辆", "7 月单月，6 月首破百万", NAVY),
        (0.030, 0.500, "租金", "9.5 万美元 / 天", "6500CEU 一年期，较五年均值 +21%", RED),
        (0.515, 0.500, "交付", "2030 年以后", "主流船厂排产，新船短期补不上", RED),
    ]

    for x, y, tag, big, note, color in cards:
        ax.add_patch(FancyBboxPatch((x, y - 0.150), 0.455, 0.216,
                                    boxstyle="round,pad=0.008",
                                    facecolor="white", edgecolor=LIGHT,
                                    linewidth=1.0))
        ax.text(x + 0.026, y + 0.022, tag, fontsize=8.8, color=GRAY,
                ha="left", va="center")
        ax.text(x + 0.026, y - 0.036, big, fontsize=17.0, color=color,
                weight="bold", ha="left", va="center")
        ax.text(x + 0.026, y - 0.096, note, fontsize=8.2, color=SLATE,
                ha="left", va="center")

    ax.plot([0.030, 0.960], [0.292, 0.292], color=LIGHT, linewidth=0.9)
    ax.text(0.030, 0.244, "变量", fontsize=8.8, color=GRAY, ha="left",
            va="center")
    ax.text(0.030, 0.192,
            "2028 年起新船集中交付，当前偏紧的供需格局可能改变；"
            "另有大量整车被迫分流到集装箱船。",
            fontsize=9.0, color=SLATE, ha="left", va="center")

    punchline(fig, "瓶颈不在造车，在运车——而船，不是一年能买到的。")
    footer(fig, "事实：出口数据据中汽协（经多家转述）；租金与排产据 Intermodal 周报（经华球通 10-27）、"
                "海事服务网 8-05、中新网 9-11｜制图：本文")
    fig.savefig(OUT + "图3_为什么运力成了瓶颈.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)