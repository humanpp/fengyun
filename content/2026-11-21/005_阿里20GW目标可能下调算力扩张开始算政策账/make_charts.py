# -*- coding: utf-8 -*-
"""
《阿里可能下调20GW数据中心目标：不是AI需求没了，是算力扩张开始算"政策账"》配套图表

事实口径（全部来自公开披露）：
  · 阿里巴巴集团 2026 年 9 月季度业绩（2026-11-19 发布）及同日业绩电话会：
      - 资本性支出 504.77 亿元（75.29 亿美元），2025 年同期 315.01 亿元，同比 +60%；
        环比低于上季度 676.8 亿元。自由现金流净流出 344.72 亿元（上年同期 218.4 亿元）。
      - 云收入 610 亿元、同比 +53%。
      - 吴泳铭：全球各区域算力政策出现非常大的变化，将影响阿里云数据中心建设；
        初步评估下，到 2032 年全球数据中心规模超 20GW 的目标"有可能下调"，
        资本开支"可能有一定程度降低"。
      - 平头哥路线图：M890 已放量商用；V900 2027Q1 量产、算力为 M890 的 3 倍；
        V900 超节点集群 2027Q2 大规模商用；J900 2028 年。
      - Qwen 已在平头哥芯片上训练下一代模型；2027 年后新增 AI 芯片产能主要为自研。
      - 2027、2028 上半年为最集中投资期；集团自由现金流 2028 下半年整体转正。
      - 云增速指引：2027 自然年 30%–45%，2028 年回到 50%+。
  · BIS《解决先进半导体远程访问问题》临时最终规则（RIN 0694-AK50）：
      2026-11-16 发布，2026-11-19 刊载《联邦公报》（91 FR 74970）并当日生效；
      向总部设在中国或澳门的企业提供超 1200 万"总处理性能"算力（约合 334 张 B200）
      须申请许可，第三国数据中心一并受限。
  · 美光 CEO Sanjay Mehrotra，2026-11-18 TomorrowX Summit（奥斯汀）：
      2027 年约 75% 产能已售出；客户谈判转向 2028 年；2027 与 2028 比 2026 更紧；
      26 份战略客户协议合计 320 亿美元预付现金与承诺，多数五年期、含照付不议条款；
      "The SCA volume requirements over the course of next 5 years were higher
      than what we were able to commit to them."
  · 全球电子协会（Global Electronics Association）2026-11-18 行业警报：
      截至 2026 年 9 月的一年，PCB 订单 +56.1%、出货 +13.3%；
      高多层板交期 16—20 周或更长；AI 服务器板 40—60+ 层，PC 板约 12 层；
      亚洲产量占全球 90%+；瓶颈在玻纤布、树脂、铜箔、覆铜板；
      短缺至少持续至 2027 年上半年，2028 年年中前难有实质缓解。

风格：克制传媒风，白底、低饱和配色、标题即结论
输出目录 = 脚本所在目录
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
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
BLUSH = "#fbf1ef"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep

Y_TITLE = 0.958
Y_SUB = 0.898
Y_PUNCH = 0.070
Y_FOOT = 0.020


def header(fig, title, sub):
    fig.text(0.045, Y_TITLE, title, fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, Y_SUB, sub, fontsize=10.6, color=GRAY,
             ha="left", va="top")


def footer(fig, text):
    fig.text(0.045, Y_FOOT, text, fontsize=7.6, color=GRAY,
             ha="left", va="bottom")


def punchline(fig, text):
    fig.text(0.045, Y_PUNCH, text, fontsize=10.4, color=DARK,
             ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


def card(ax, x, y, w, h, edge, face="white", lw=1.0, z=2):
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
    fig = plt.figure(figsize=(12, 6.6))
    ax = new_axes(fig)

    header(fig, "钱还在花，目标却可能往回收",
           "2026 年 9 月季度资本开支同比增 60%；同一场电话会上，"
           "到 2032 年超 20GW 的目标被挂上了“可能下调”")

    base = 0.300
    scale = 0.400 / 504.77
    bars = [
        ("2025 年 9 月季度", 315.01, LIGHT, SLATE),
        ("2026 年 9 月季度", 504.77, NAVY, NAVY),
    ]
    bw = 0.092
    for i, (label, val, face, edge) in enumerate(bars):
        x = 0.105 + i * 0.165
        h = val * scale
        ax.add_patch(Rectangle((x, base), bw, h, facecolor=face,
                               edgecolor=edge, linewidth=1.2, zorder=4))
        ax.text(x + bw / 2, base + h + 0.026, f"{val:.2f} 亿元",
                fontsize=12.6, color=edge, weight="bold",
                ha="center", va="bottom", zorder=5)
        ax.text(x + bw / 2, base - 0.040, label, fontsize=9.4, color=GRAY,
                ha="center", va="top", zorder=5)

    ax.plot([0.085, 0.400], [base, base], color=SLATE, linewidth=1.1, zorder=3)

    # 同比标注：贴在较高那根柱子的数值正上方
    ax.text(0.316, base + 0.400 + 0.100, "同比 +60%", fontsize=12.0,
            color=RED, weight="bold", ha="center", va="bottom", zorder=7)

    ax.text(0.085, 0.196, "资本开支仍在高位：本季度 504.77 亿元，"
                          "环比低于上季度的 676.8 亿元；\n自由现金流净流出 344.72 亿元，"
                          "上年同期为 218.4 亿元。",
            fontsize=9.4, color=SLATE, ha="left", va="top", linespacing=1.7)

    # 右：20GW 目标卡
    card(ax, 0.500, 0.250, 0.455, 0.560, RED, face=BLUSH, lw=1.6)
    ax.text(0.525, 0.748, "远期产能规划", fontsize=9.6, color=GRAY,
            ha="left", va="center", zorder=6)
    ax.text(0.525, 0.668, "到 2032 年", fontsize=11.0, color=SLATE,
            ha="left", va="center", zorder=6)
    ax.text(0.525, 0.578, "全球数据中心规模", fontsize=13.2, color=DARK,
            ha="left", va="center", zorder=6)
    ax.text(0.525, 0.470, "超过 20GW", fontsize=26.0, color=NAVY,
            weight="bold", ha="left", va="center", zorder=6)

    ax.plot([0.525, 0.930], [0.418, 0.418], color=RED, linewidth=0.9,
            alpha=0.45, zorder=5)

    ax.text(0.525, 0.372, "初步评估：", fontsize=9.6, color=SLATE,
            ha="left", va="center", zorder=6)
    ax.text(0.525, 0.300, "目标“有可能下调”，资本开支“可能有一定程度降低”",
            fontsize=10.4, color=RED, weight="bold",
            ha="left", va="center", zorder=6)

    ax.add_patch(FancyArrowPatch((0.888, 0.470), (0.888, 0.372),
                                 arrowstyle="-|>", mutation_scale=16,
                                 color=RED, linewidth=1.8, zorder=7))

    punchline(fig, "资本开支的斜率还在，产能规划的斜率开始不确定。")
    footer(fig, "事实来源：阿里巴巴集团 2026 年 9 月季度业绩及同日电话会（2026-11-19）；财联社 2026-11-19")
    fig.savefig(OUT + "图1_钱还在花目标却要收.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "算力扩张开始算三本账",
           "过去只要规模；现在要先过政策、材料、自研三道关")

    books = [
        ("政策账", NAVY, "white",
         "BIS《解决先进半导体\n远程访问问题》临时最终规则",
         "2026-11-16 发布\n11-19 刊载并生效",
         "超 1200 万 TPP 须许可\n第三国数据中心一并受限"),
        ("供应链账", SLATE, "white",
         "美光：2027 年约 75% 产能\n已售出，客户谈的是 2028 年",
         "26 份战略客户协议\n320 亿美元预付与承诺",
         "客户五年要货量\n高于美光可承诺规模"),
        ("自研账", RED, BLUSH,
         "Qwen 已在平头哥芯片上\n训练下一代模型",
         "V900 2027Q1 量产\n算力为 M890 的 3 倍",
         "2027 年后新增 AI 芯片\n产能主要来自自研"),
    ]

    left, right, gap = 0.045, 0.955, 0.026
    w = (right - left - gap * 2) / 3
    top, bot = 0.720, 0.215

    for i, (name, color, face, l1, l2, l3) in enumerate(books):
        x = left + i * (w + gap)
        card(ax, x, bot, w, top - bot, color, face=face,
             lw=1.6 if i == 2 else 1.2)
        cx = x + 0.026
        ax.text(cx, top - 0.062, name, fontsize=14.2, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        ax.plot([cx, x + w - 0.026], [top - 0.106, top - 0.106],
                color=color, linewidth=0.9, alpha=0.40, zorder=5)
        ax.text(cx, top - 0.165, l1, fontsize=9.5, color=DARK,
                ha="left", va="top", linespacing=1.70, zorder=6)
        ax.text(cx, top - 0.278, l2, fontsize=9.5, color=SLATE,
                ha="left", va="top", linespacing=1.70, zorder=6)
        ax.text(cx, top - 0.390, l3, fontsize=9.5, color=color,
                weight="bold", ha="left", va="top", linespacing=1.70,
                zorder=6)

    ax.text(0.045, 0.160,
            "路线图是 4 个时间点；而供应链的缓解，排到了 2028 年年中之后。",
            fontsize=9.4, color=SLATE, ha="left", va="center")

    punchline(fig, "三道减法题：能不能建、能不能到、能不能顶上。")
    footer(fig, "事实来源：BIS 2026-11-16；美光 TomorrowX 对话 2026-11-18；"
                "全球电子协会 2026-11-18；阿里巴巴电话会 2026-11-19")
    fig.savefig(OUT + "图2_三本账.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(12, 6.8))
    ax = new_axes(fig)

    header(fig, "自研芯片被排进了时间表",
           "阿里把国产算力的验证节点写成了日期，云增速也押在它上面")

    y_line = 0.590
    nodes = [
        ("M890", "现在", "已放量商用"),
        ("V900", "2027 年一季度", "量产，算力为 M890 的 3 倍"),
        ("V900 超节点集群", "2027 年二季度", "大规模商用"),
        ("J900", "2028 年", "计划量产"),
    ]
    xs = [0.115, 0.360, 0.605, 0.860]

    ax.plot([0.060, 0.945], [y_line, y_line], color=LIGHT, linewidth=2.0,
            zorder=3, solid_capstyle="round")

    for i, (name, date, desc) in enumerate(nodes):
        x = xs[i]
        color = SLATE if i == 0 else NAVY
        ax.plot([x], [y_line], marker="o", markersize=9.0, color=color,
                markeredgecolor="white", markeredgewidth=1.4, zorder=6)
        ax.text(x, y_line + 0.048, date, fontsize=10.2, color=color,
                weight="bold", ha="center", va="bottom", zorder=6)
        ax.text(x, y_line - 0.052, name, fontsize=11.6, color=DARK,
                weight="bold", ha="center", va="top", zorder=6)
        ax.text(x, y_line - 0.108, desc, fontsize=9.2, color=SLATE,
                ha="center", va="top", zorder=6)

    # 左卡：财务承诺
    card(ax, 0.045, 0.250, 0.445, 0.185, NAVY, lw=1.1)
    ax.text(0.068, 0.395, "同一份路线图上的财务安排", fontsize=9.6,
            color=GRAY, ha="left", va="center", zorder=6)
    ax.text(0.068, 0.336,
            "2027 年与 2028 年上半年为最集中投资期",
            fontsize=10.0, color=DARK, ha="left", va="center", zorder=6)
    ax.text(0.068, 0.286,
            "集团自由现金流 2028 年下半年才整体转正",
            fontsize=10.0, color=NAVY, weight="bold",
            ha="left", va="center", zorder=6)

    # 右卡：云增速
    card(ax, 0.510, 0.250, 0.445, 0.185, RED, face=BLUSH, lw=1.3)
    ax.text(0.533, 0.395, "云收入增速：本季 53%，明年目标下调", fontsize=9.6,
            color=GRAY, ha="left", va="center", zorder=6)
    ax.text(0.533, 0.336, "2027 自然年  30%—45%", fontsize=10.6,
            color=RED, weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.533, 0.286, "2028 年国产算力放量后  回到 50% 以上",
            fontsize=10.0, color=SLATE, ha="left", va="center", zorder=6)

    punchline(fig, "这几个日期兑现不了，2028 年的回升就不成立。")
    footer(fig, "事实来源：阿里巴巴 2027 财年第二季度业绩电话会（2026-11-19）")
    fig.savefig(OUT + "图3_平头哥时间表.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)