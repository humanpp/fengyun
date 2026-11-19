# -*- coding: utf-8 -*-
"""
《OpenAI 手机的三个日期，和一条查不到的产线》配套图表
事实口径（2026-11-19，逐条核对财联社、证券时报、每经、郭明錤产业调查后）：
  · 2026 年 11 月 19 日，财联社记者王碧微从消费电子核心供应链人士处获悉：
    OpenAI 即将进军手机市场，首款产品有望在 2027 年底或 2028 年面市；
    富士康旗下富智康（FIH，02038.HK）已获得 OpenAI 手机项目订单，
    将参与相关产品的整机组装；零部件等其他环节亦有立讯精密、领益智造、
    瑞声科技等多家传统果链厂商参与。财联社已向富士康求证，截至发稿未获回复
    （财联社 11-19 12:56）。
  · 同日证券时报/人民财讯亦独家报道同一消息，表述一致：
    「相关产品方案、订单规模及量产安排，仍有待进一步获悉」（证券时报 11-19）。
  · 2026 年 11 月 18 日晚间，每日经济新闻记者从供应链人士处获悉：
    立讯精密目前与 OpenAI 有多个产品的全面合作，或因资源配置的统筹考量
    未承接手机组装业务（每经 11-18）。
  · 时间线沿革（本文用于对照的关键背景）：
    - 2026 年 4 月 27 日，天风国际分析师郭明錤发布产业调查：OpenAI 计划自研手机，
      正与联发科、高通合作开发手机处理器，立讯精密为独家系统协同设计与制造商，
      预计 2028 年量产；规格与供应商最终拍板预计在 2026 年底至 2027 年一季度完成
      （郭明錤 X 帖文；界面新闻 4-27、IT之家 4-27、科创板日报 4-27、工商时报 4-28）。
      消息当日立讯精密股价一度涨停、收涨逾 9% 至 71.97 元/股。
    - 2026 年 5 月 5 日，郭明錤更新调查：量产目标提前至 2027 年上半年，
      处理器供应可能由联发科独家取得（基于天玑 9600 客制化版本，台积电 N2P），
      2027 与 2028 两年合计出货量目标约 3000 万支
      （郭明錤 X 帖文；鉅亨網 5-6、TechNews 5-5、NOWnews 5-5、环球网 5-6）。
    - 2026 年 11 月 19 日，财联社口径：2027 年底或 2028 年面市。
  · 未获证实的三项（本文标注为「查不到出处」）：
    - 「Project Chimera」为 OpenAI 手机项目内部代号：检索未见任何权威来源支持；
      该代号在公开信息中指向其他项目，与手机项目无可靠关联。
    - 「富士康深圳宝安基地已开始调试首条 AI 手机 SMT 生产线」：
      财联社、证券时报原文均无此表述。
    - 「模型即系统」「统一语义总线」「取消应用抽屉」等产品架构描述：
      原始报道未披露，OpenAI 官方亦未公布产品形态。
  · 股价反应：11 月 19 日富智康（02038.HK）盘中一度涨超 12%，
    午后涨幅收窄；智通财经 13:33 报道时涨 2.75% 报 13.43 港元
    （新浪财经 11-19、智通财经 11-19、经济观察网 11-19、第一财经 11-19）。
  · 参照系：OpenAI 首款 AI 端侧硬件（非手机）据每经 11-19 报道或于 2026 年底
    启动出货，立讯精密独家承担整机制造；产品形态 OpenAI 尚未正式公布
    （每经 11-19）。
本文换算（非当事方口径）：2026 年 4 月 27 日至 11 月 19 日约 7 个月；
三个时间点（2028 年、2027 上半年、2027 年底或 2028 年）跨度约 12 个月。
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
PT = 1.0 / (4.76 * 72.0)


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
    fig = base("同一个项目，三个量产时间",
               "2026 年 4 月—11 月｜郭明錤两次调查，财联社一次求证")
    ax = canvas(fig)

    rows = [
        ("4 月 27 日", "郭明錤", "2028 年量产",
         "立讯精密为独家系统协同设计与制造商\n处理器与联发科、高通共同开发", GRAY, 0.700),
        ("5 月 5 日", "郭明錤（更新）", "2027 年上半年量产",
         "时间提前约一年；处理器或由联发科独家\n两年出货目标约 3000 万支", SLATE, 0.470),
        ("11 月 19 日", "财联社求证", "2027 年底或 2028 年面市",
         "富智康获整机组装订单；立讯精密未承接组装\n富士康截至发稿未回复", NAVY, 0.240),
    ]

    for date, who, when, note, color, y in rows:
        ax.add_patch(FancyBboxPatch((0.028, y - 0.090), 0.944, 0.180,
                                    boxstyle="round,pad=0.005",
                                    facecolor="white", edgecolor=LIGHT,
                                    linewidth=1.0))
        ax.add_patch(Rectangle((0.028, y - 0.090), 0.007, 0.180,
                               facecolor=color, edgecolor="none"))

        ax.text(0.066, y + 0.052, date, fontsize=9.4, color=GRAY,
                weight="bold", ha="left", va="center")
        ax.text(0.190, y + 0.052, who, fontsize=8.6, color=color,
                ha="left", va="center")
        ax.text(0.400, y + 0.052, when, fontsize=12.0, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(0.066, y - 0.036, note, fontsize=8.2, color=SLATE,
                ha="left", va="center", linespacing=1.8)

    ax.text(0.028, 0.104,
            "七个月里，同一个项目的量产时间被推前、又推后。差别在于口径：分析师调查 vs 供应链求证。",
            fontsize=8.8, color=SLATE, ha="left", va="center")

    punchline(fig, "时间表还没定，订单先被看见了。")
    footer(fig, "事实：郭明錤 X 帖文 4-27／5-5、界面新闻 4-27、鉅亨網 5-6、"
                "财联社 11-19、证券时报 11-19｜制图：本文")
    fig.savefig(OUT + "图1_三个量产时间.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("谁接组装，谁供零件",
               "2026 年 11 月｜供应链分工与已确认程度")
    ax = canvas(fig)

    ax.text(0.028, 0.842, "整机组装", fontsize=10.4, color=DARK, weight="bold",
            ha="left", va="center")

    # 富智康：已获订单
    ax.add_patch(FancyBboxPatch((0.028, 0.648), 0.452, 0.166,
                                boxstyle="round,pad=0.006",
                                facecolor="white", edgecolor=NAVY,
                                linewidth=1.4))
    ax.text(0.056, 0.772, "富智康 FIH（02038.HK）", fontsize=10.0, color=NAVY,
            weight="bold", ha="left", va="center")
    ax.text(0.056, 0.720, "已获 OpenAI 手机项目订单", fontsize=8.8, color=DARK,
            ha="left", va="center")
    ax.text(0.056, 0.680, "富士康旗下，同时是 iPhone 主要组装商", fontsize=7.8,
            color=GRAY, ha="left", va="center")

    # 立讯：未承接
    ax.add_patch(FancyBboxPatch((0.520, 0.648), 0.452, 0.166,
                                boxstyle="round,pad=0.006",
                                facecolor="white", edgecolor=RED,
                                linewidth=1.4))
    ax.text(0.548, 0.772, "立讯精密", fontsize=10.0, color=RED,
            weight="bold", ha="left", va="center")
    ax.text(0.548, 0.720, "未承接手机组装业务", fontsize=8.8, color=DARK,
            ha="left", va="center")
    ax.text(0.548, 0.680, "或因资源配置统筹考量；仍参与零部件环节", fontsize=7.8,
            color=GRAY, ha="left", va="center")

    ax.plot([0.028, 0.972], [0.596, 0.596], color=LIGHT, linewidth=0.9)

    ax.text(0.028, 0.540, "零部件环节", fontsize=10.4, color=DARK,
            weight="bold", ha="left", va="center")

    parts = ["立讯精密", "领益智造", "瑞声科技"]
    x = 0.028
    for p in parts:
        ax.add_patch(FancyBboxPatch((x, 0.432), 0.290, 0.072,
                                    boxstyle="round,pad=0.005",
                                    facecolor=PALE, edgecolor=LIGHT,
                                    linewidth=1.0))
        ax.text(x + 0.145, 0.468, p, fontsize=9.6, color=DARK, weight="bold",
                ha="center", va="center")
        x += 0.327

    ax.text(0.028, 0.364,
            "三家均为传统苹果供应链厂商。财联社称其「参与」，未披露具体料号与份额。",
            fontsize=8.6, color=SLATE, ha="left", va="center")

    ax.plot([0.028, 0.972], [0.312, 0.312], color=LIGHT, linewidth=0.9)

    ax.text(0.028, 0.254, "市场反应", fontsize=10.4, color=DARK, weight="bold",
            ha="left", va="center")
    ax.text(0.028, 0.190,
            "11 月 19 日富智康盘中一度涨超 12%，午后涨幅收窄；智通财经 13:33 报道时涨 2.75%，报 13.43 港元。",
            fontsize=8.8, color=SLATE, ha="left", va="center")
    ax.text(0.028, 0.136,
            "消息面驱动，且截至发稿富士康未回复求证。",
            fontsize=8.8, color=GRAY, ha="left", va="center")

    punchline(fig, "订单能查证，产线不能。")
    footer(fig, "事实：财联社 11-19、证券时报 11-19、每经 11-18、"
                "智通财经 11-19、第一财经 11-19｜制图：本文")
    fig.savefig(OUT + "图2_谁接组装谁供零件.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("素材里的六句话，查得到出处吗",
               "逐条核对原始报道后的状态")
    ax = canvas(fig)

    rows = [
        ("富智康获整机组装订单", "财联社、证券时报同日报道",
         "有出处", NAVY, NAVY),
        ("立讯精密未承接组装", "每经 11-18 引供应链人士",
         "有出处", NAVY, NAVY),
        ("首款 2027 年底或 2028 年面市", "财联社引供应链人士",
         "有出处", NAVY, NAVY),
        ("代号「Project Chimera」", "检索未见权威来源支持",
         "查不到", RED, "white"),
        ("深圳宝安调试首条 SMT 产线", "原始报道无此表述",
         "查不到", RED, "white"),
        ("「模型即系统」「统一语义总线」", "OpenAI 未公布产品形态",
         "查不到", RED, "white"),
    ]

    y = 0.800
    for claim, src, badge, color, face in rows:
        ax.text(0.028, y + 0.014, claim, fontsize=9.2, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(0.028, y - 0.026, src, fontsize=7.8, color=GRAY,
                ha="left", va="center")

        bx = 0.790
        ax.add_patch(FancyBboxPatch((bx, y - 0.026), 0.150, 0.052,
                                    boxstyle="round,pad=0.004",
                                    facecolor=face, edgecolor=color,
                                    linewidth=1.1))
        ax.text(bx + 0.075, y, badge, fontsize=8.4,
                color=("white" if face == NAVY else color),
                weight="bold", ha="center", va="center")
        y -= 0.116

    ax.text(0.028, 0.086,
            "前三条可以写进报道，后三条不能——它们不是错误，是没有证据。",
            fontsize=8.8, color=SLATE, ha="left", va="center")

    punchline(fig, "一半有出处，一半查不到。")
    footer(fig, "事实：财联社 11-19、证券时报 11-19、每经 11-18｜"
                "「查不到」为本文检索时点状态｜制图：本文")
    fig.savefig(OUT + "图3_哪句话查得到出处.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)
