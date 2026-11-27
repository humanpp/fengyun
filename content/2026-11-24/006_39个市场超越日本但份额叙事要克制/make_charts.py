# -*- coding: utf-8 -*-
"""
《39 个市场的新车份额超过日本品牌》配套图表

事实口径：
  · 《日本经济新闻》2026-11-23：美国研究机构"全球汽车咨询公司"分析 1—9 月新车销售数据，
    中国品牌在 39 个国家和地区份额超过日本品牌，14 个为今年实现超越、8 个在欧洲；
    德国份额同比 +2 个百分点、意大利 +6、巴西 +10（新华社东京 11-23 电）。
  · 乘联分会 2026-11-18：11 月 1—15 日乘用车零售 61.1 万辆（同比 -25%、环比 -6）；
    新能源零售 44.7 万辆（同比 -13%、环比 +7）；零售渗透率 73.2%；
    年内累计零售 1558.9 万辆（同比 -22%）。
  · 中汽协 2026-11-11：10 月汽车出口 106.6 万辆（同比 +60.2%、环比 +1.3%），
    月度出口连续 5 个月保持 100 万辆以上；新能源出口 60.6 万辆（同比 +1.4 倍）；
    国内销量同比降幅连续 7 个月超 20%。
  · 三个落点：捷途巴西追加 4 亿雷亚尔（约 6900 万美元）、2027 年本地生产 T1/T2；
    零跑与欧宝联合开发 C 级纯电 SUV、对价 1 亿欧元、2028 年上市；
    千台岚图梦想家 9 右舵版 11-20 发运、10 亿级订单、泰国上市。

风格：克制传媒风，编辑排版
输出目录 = 脚本所在目录
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["figure.facecolor"] = "white"
plt.rcParams["savefig.facecolor"] = "white"

INK = "#1a2332"
NAVY = "#1b3a5c"
RED = "#b0413e"
TEAL = "#2f6b64"
GOLD = "#9a7b3f"
MUTED = "#7b8494"
HAIR = "#dfe3e8"
WASH = "#f4f6f8"
WHITE = "#ffffff"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep


def new_axes(fig):
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return ax


def head(fig, ax, kicker, title, sub, color):
    ax.add_patch(Rectangle((0.042, 0.928), 0.0075, 0.040,
                           facecolor=color, edgecolor="none", zorder=9))
    ax.text(0.058, 0.950, kicker, fontsize=9.2, color=color,
            weight="bold", ha="left", va="center", zorder=9)
    ax.text(0.042, 0.900, title, fontsize=21, color=INK, weight="bold",
            ha="left", va="top", zorder=9)
    ax.text(0.042, 0.848, sub, fontsize=10.4, color=MUTED,
            ha="left", va="top", zorder=9)
    ax.plot([0.042, 0.958], [0.812, 0.812], color=HAIR, linewidth=1.0,
            zorder=5)


def foot(fig, ax, text):
    ax.plot([0.042, 0.958], [0.058, 0.058], color=HAIR, linewidth=0.9,
            zorder=5)
    ax.text(0.042, 0.032, text, fontsize=7.0, color=MUTED,
            ha="left", va="center", zorder=9)


def outro(fig, ax, text, color=INK, width=0.780):
    ax.add_patch(FancyBboxPatch(
        (0.042, 0.082), width, 0.048,
        boxstyle="round,pad=0.002,rounding_size=0.008",
        facecolor=color, edgecolor="none", zorder=6))
    ax.text(0.062, 0.106, text, fontsize=10.2, color=WHITE,
            ha="left", va="center", zorder=9)


def note(fig, ax, y, h, text, size=8.8):
    ax.add_patch(FancyBboxPatch(
        (0.042, y), 0.916, h,
        boxstyle="round,pad=0,rounding_size=0.008",
        facecolor=WASH, edgecolor="none", zorder=3))
    ax.text(0.062, y + h / 2, text, fontsize=size, color=INK,
            ha="left", va="center", zorder=9, linespacing=1.6)


# ---------------------------------------------------------------- 图 1
def fig1():
    fig = plt.figure(figsize=(13.6, 8.0))
    ax = new_axes(fig)

    head(fig, ax,
         "2026.11.23  日经 / 新华社",
         "39 个市场，14 个是今年才拿下的",
         "中国品牌新车份额超过日本品牌的市场数（1—9 月）",
         NAVY)

    rows = [
        ("全部超越日本品牌的市场", "39 个国家和地区", 39, NAVY),
        ("其中今年才实现超越的", "比 2025 年新增", 14, TEAL),
        ("其中位于欧洲的", "欧洲是全球法规最严的市场之一", 8, GOLD),
    ]
    x0, span, vmax = 0.420, 0.400, 39.0
    ys = [0.752, 0.660, 0.568]
    h = 0.044

    for (name, tag, val, color), y in zip(rows, ys):
        ax.text(x0 - 0.020, y + 0.008, name, fontsize=10.4, color=INK,
                ha="right", va="center", zorder=9)
        ax.text(x0 - 0.020, y - 0.026, tag, fontsize=8.2, color=MUTED,
                ha="right", va="center", zorder=9)
        ax.add_patch(Rectangle((x0, y - h / 2), val / vmax * span, h,
                               facecolor=color, edgecolor="none", zorder=6))
        ax.text(x0 + val / vmax * span + 0.014, y, "%d" % val, fontsize=15.0,
                color=color, weight="bold", ha="left", va="center", zorder=9)

    ax.plot([0.042, 0.958], [0.508, 0.508], color=HAIR, linewidth=1.0,
            zorder=5)
    ax.text(0.042, 0.478,
            "三个市场的份额同比提升（百分点；刻度 0—10，与上组市场数不可比长短）",
            fontsize=10.0, color=INK, weight="bold", ha="left", va="center",
            zorder=9)

    mini = [("巴西", 10, NAVY), ("意大利", 6, TEAL), ("德国", 2, GOLD)]
    mys = [0.414, 0.332, 0.250]
    for (name, val, color), y in zip(mini, mys):
        ax.text(x0 - 0.020, y, name, fontsize=10.0, color=INK, ha="right",
                va="center", zorder=9)
        px = x0 + val / 10.0 * span
        ax.plot([x0, px], [y, y], color=HAIR, linewidth=1.0, zorder=4)
        ax.add_patch(Circle((px, y), 0.0085, facecolor=color,
                            edgecolor="none", zorder=8))
        ax.text(px + 0.016, y, "+%d" % val, fontsize=10.4, color=color,
                weight="bold", ha="left", va="center", zorder=9)
    ax.plot([x0, x0], [0.436, 0.226], color=HAIR, linewidth=1.0, zorder=4)

    note(fig, ax, 0.148, 0.052,
         "报道只给「份额超过日本品牌」，没给排名与绝对份额；德国那 2 个百分点也没有基数，"
         "可能是 1% 到 3%，也可能是 5% 到 7%。")

    outro(fig, ax, "超过日本品牌，不等于拿下这个市场。")
    foot(fig, ax, "数据来源：《日本经济新闻》2026-11-23，经新华社东京 11-23 电转述；"
                  "该数据由美国研究机构「全球汽车咨询公司」分析 1—9 月新车销售得出，"
                  "本文未独立复算原始数据。")
    fig.savefig(OUT + "图1_39个14个8个.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(13.6, 8.0))
    ax = new_axes(fig)

    head(fig, ax,
         "同一周，两个方向",
         "国内在缩，海外在冲",
         "同比增速（%），口径与时间窗口各按发布方",
         RED)

    items = [
        ("新能源出口", "10 月", 140.0, NAVY),
        ("汽车出口", "10 月，106.6 万辆", 60.2, NAVY),
        ("乘用车零售", "11 月 1—15 日，61.1 万辆", -25.0, RED),
        ("年内累计零售", "1—11 月上半月，1558.9 万辆", -22.0, RED),
        ("新能源零售", "11 月 1—15 日，44.7 万辆", -13.0, RED),
    ]

    zero, span, vmax = 0.420, 0.330, 150.0
    ys = [0.722, 0.638, 0.526, 0.442, 0.358]
    h = 0.038

    ax.plot([zero, zero], [0.766, 0.312], color="#9aa3ad", linewidth=1.2,
            zorder=5)

    for (name, tag, val, color), y in zip(items, ys):
        ax.text(zero - 0.162, y + 0.008, name, fontsize=10.2, color=INK,
                ha="right", va="center", zorder=9)
        ax.text(zero - 0.162, y - 0.026, tag, fontsize=7.6, color=MUTED,
                ha="right", va="center", zorder=9)
        w = abs(val) / vmax * span
        if val > 0:
            ax.add_patch(Rectangle((zero, y - h / 2), w, h, facecolor=color,
                                   edgecolor="none", zorder=6))
            ax.text(zero + w + 0.012, y, "+%.1f%%" % val, fontsize=10.2,
                    color=color, weight="bold", ha="left", va="center",
                    zorder=9)
        else:
            ax.add_patch(Rectangle((zero - w, y - h / 2), w, h,
                                   facecolor=color, edgecolor="none", zorder=6))
            ax.text(zero - w - 0.012, y, "%.0f%%" % val, fontsize=10.2,
                    color=color, weight="bold", ha="right", va="center",
                    zorder=9)

    ax.text(zero - 0.012, 0.788, "国内：零售", fontsize=8.6, color=RED,
            ha="right", va="center", zorder=9)
    ax.text(zero + 0.012, 0.788, "海外：出口", fontsize=8.6, color=NAVY,
            ha="left", va="center", zorder=9)

    ax.plot([zero + (-25) / vmax * span, zero + 1.0 * span], [0.300, 0.300],
            color=HAIR, linewidth=1.0, zorder=4)
    for tick in (-25, 0, 50, 100, 150):
        tx = zero + tick / vmax * span
        ax.plot([tx, tx], [0.300, 0.290], color=HAIR, linewidth=1.0, zorder=4)
        ax.text(tx, 0.272, "%d%%" % tick, fontsize=8.0, color=MUTED,
                ha="center", va="center", zorder=9)

    note(fig, ax, 0.150, 0.070,
         "月度出口已连续 5 个月保持在 100 万辆以上；国内销量同比降幅连续 7 个月超过 20%。\n"
         "零售为乘用车口径、11 月 1—15 日；出口为全口径（含商用车）、10 月。两者不可相减。")

    outro(fig, ax, "引擎换了：国内增量没了，全球替代顶上。")
    foot(fig, ax, "数据来源：乘联分会 2026-11-18 发布；中国汽车工业协会 2026-11-11 发布"
                  "（经济观察网 11-11、新浪财经 11-18 转述）。")
    fig.savefig(OUT + "图2_两个方向.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    cards = [
        ("① 产能", "捷途 · 巴西", NAVY,
         "4 亿雷亚尔", "约 6900 万美元，追加投入",
         "2027 年起在巴西本地生产\n先落地 T1、T2 两款 SUV"),
        ("② 渠道与授权", "零跑 × 欧宝", TEAL,
         "1 亿欧元", "含项目开发费与授权使用费",
         "共研 C 级纯电 SUV\n2028 年上市，核心零部件零跑供"),
        ("③ 法规与右舵", "岚图 · 梦想家 9", GOLD,
         "千台发运", "随车落地 10 亿级海外订单",
         "泰国已上市，12 月中进香港\n再到新加坡、马来西亚、印尼"),
    ]

    fig = plt.figure(figsize=(13.6, 8.0))
    ax = new_axes(fig)

    head(fig, ax,
         "2026 年 11 月，三个落点",
         "全球替代能不能持续，看三件事",
         "本地产能 · 渠道嵌入 · 法规适配",
         GOLD)

    w = 0.2853
    gap = 0.030
    x = 0.042
    top, h_card = 0.676, 0.442

    for name, who, color, big, unit, desc in cards:
        ax.add_patch(FancyBboxPatch(
            (x, top - h_card), w, h_card,
            boxstyle="round,pad=0,rounding_size=0.010",
            facecolor=WHITE, edgecolor=HAIR, linewidth=1.2, zorder=4))
        ax.add_patch(Rectangle((x, top - 0.060), w, 0.060, facecolor=color,
                               edgecolor="none", zorder=6))
        ax.text(x + 0.020, top - 0.030, name, fontsize=11.0, color=WHITE,
                weight="bold", ha="left", va="center", zorder=9)
        ax.text(x + 0.020, top - 0.104, who, fontsize=12.4, color=INK,
                weight="bold", ha="left", va="center", zorder=9)
        ax.plot([x + 0.020, x + w - 0.020], [top - 0.140, top - 0.140],
                color=HAIR, linewidth=1.0, zorder=5)
        ax.text(x + 0.020, top - 0.198, big, fontsize=17.0, color=color,
                weight="bold", ha="left", va="center", zorder=9)
        ax.text(x + 0.020, top - 0.244, unit, fontsize=8.4, color=MUTED,
                ha="left", va="center", zorder=9)
        ax.text(x + 0.020, top - 0.340, desc, fontsize=9.0, color=INK,
                ha="left", va="center", zorder=9, linespacing=1.7)
        x += w + gap

    outro(fig, ax, "钱、技术、合规：三条路任何一条掉链子，39 明年就会往回走。",
          width=0.800)
    foot(fig, ax, "数据来源：路透社 2026-11-18、观点网 11-19（捷途）；"
                  "零跑 2026 年 Q3 业绩电话会、新浪科技 11-22、NE 时代 11-24（零跑与欧宝）；"
                  "新华网湖北 11-20、经济观察网 11-21、澎湃新闻 11-21（岚图）。")
    fig.savefig(OUT + "图3_三个落点.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)