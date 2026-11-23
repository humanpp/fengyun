# -*- coding: utf-8 -*-
"""
《一张算力网要铺到哪：从 1 毫秒圈到 32.7 万家实体企业》配套图表

事实口径：

一、算力怎么算普惠
  · 2026-09-12 中国算力大会：将算力服务明确为公司三大主业之一，
    加快建设全国一体化算力网，着力提供「即取即用、普惠易用」的算力服务。
  · 同一场合：AIDC 总签约规模超 7GW；布局多个万卡智算中心与分布式推理网络；
    自研算网大脑纳管合作算力，落地 8 个国家级、枢纽级、区域级平台，
    承建国家算力互联互通河北区域节点；MoMA 平台汇聚超 340 款主流模型、
    实现 0day 首发接入；打造 Token 工厂。
  · 赋能「天工」工业互联网平台，服务实体企业 32.7 万家。
  · 打造自主可信九天基座大模型，实现从芯片到模型的全栈国产自主可控；
    通过模型微调形成面向能源、农业等重点领域的超 50 款行业模型。
  据新华网 2026-09-12《中国移动参加 2026 中国算力大会》。

二、算力怎么落到具体的地方与行业
  · 2025 年年度业绩：智算训练全国中心节点和区域中心节点基本覆盖国家八大枢纽；
    三级算力时延圈城域 1 毫秒、省域 5 毫秒、全国 20 毫秒。
  · 「N+31+X」算力布局；400G 算力光网与 320+ 城市算力网络；
    算网智脑资源一体化纳管，八大算力枢纽端到端时延降至 12 毫秒。
  据新华网 2026-05-09、央广网 2026-03-26。
  · 2026-07 报道：算网大脑推进「东数西算」与「西电东送」联动。
  · 2026-08-20 移动云（西部）Token 中心发布（C114 通信网）。

三、普惠的另一端：价格与门槛
  · 2026-05-08 移动云大会：围绕 Token 生产、传输、运营全链条构建全栈算力基础设施，
    推动产业链形成「模型迭代—Token 运营—智能应用」飞轮效应；
    在汕头完成 Token 出海全链路验证；网络能力开放超 2900 项。
  据新华网 2026-05-09。

风格：克制传媒风，白底、低饱和配色、标题即结论
输出目录 = 脚本所在目录
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle

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
TEAL = "#3f6f6b"
AMBER = "#9a7b4f"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep

Y_TITLE = 0.962
Y_SUB = 0.912
Y_PUNCH = 0.052
Y_FOOT = 0.014

Q_L = "\u300c"
Q_R = "\u300d"


def header(fig, title, sub):
    fig.text(0.040, Y_TITLE, title, fontsize=18.5, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.040, Y_SUB, sub, fontsize=10.2, color=GRAY,
             ha="left", va="top")


def footer(fig, text):
    fig.text(0.040, Y_FOOT, text, fontsize=7.2, color=GRAY,
             ha="left", va="bottom")


def punchline(fig, text):
    fig.text(0.040, Y_PUNCH, text, fontsize=10.0, color=DARK,
             ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.65", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


def card(ax, x, y, w, h, edge, face="white", lw=1.0, z=2):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.003,rounding_size=0.012",
        facecolor=face, edgecolor=edge, linewidth=lw, zorder=z))


def new_axes(fig):
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return ax


# ---------------------------------------------------------------- 图 1
def fig1():
    """从中心到边缘的四级纵深"""
    fig = plt.figure(figsize=(13.2, 7.4))
    ax = new_axes(fig)

    header(fig, "算力不是一座塔，是一个纵深",
           "从八大枢纽到城域 1 毫秒圈，每一层解决不同的距离问题")

    tiers = [
        ("全国层", "国家八大枢纽", "20 毫秒圈", "长周期训练、数据备份、离线推理", NAVY, 0.720),
        ("区域层", "省域 / 区域中心", "5 毫秒圈", "区域级推理、行业模型微调", TEAL, 0.560),
        ("城市层", "320+ 城市算力网络", "1 毫秒圈", "工业控制、实时交互、边缘推理", RED, 0.400),
        ("边缘层", "分布式推理网络", "现场", "端侧协同、低时延闭环", AMBER, 0.240),
    ]

    for name, node, latency, use, color, y in tiers:
        card(ax, 0.048, y, 0.900, 0.118, color, lw=1.4)
        ax.text(0.070, y + 0.084, name, fontsize=9.6, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(0.070, y + 0.038, node, fontsize=8.6, color=DARK,
                ha="left", va="center", zorder=6)
        ax.text(0.390, y + 0.084, latency, fontsize=10.4, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(0.390, y + 0.038, use, fontsize=8.2, color=SLATE,
                ha="left", va="center", zorder=6)

    # 左侧纵深箭头
    ax.annotate("", xy=(0.026, 0.230), xytext=(0.026, 0.850),
                arrowprops=dict(arrowstyle="-|>", color=GRAY, linewidth=1.3))
    ax.text(0.020, 0.540, "离用户越来越近", fontsize=8.4, color=GRAY,
            rotation=90, ha="center", va="center")

    ax.text(0.048, 0.180,
            "只有全国一层，接不了 1 毫秒的活；只有城市一层，跑不了万卡训练。",
            fontsize=9.2, color=DARK, ha="left", va="center")

    punchline(fig, "「普惠」的前提不是算力总量大，是每一层都有人能接上。")
    footer(fig, "事实来源：2026 中国算力大会（新华网 2026-09-12）；"
                "中国移动 2025 年年度业绩（央广网 2026-03-26）；全国一体化算力网技术创新体系（新华网 2026-05-09）")
    fig.savefig(OUT + "图1_四级纵深.png", dpi=160)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """算力怎么变成产品：三条通道"""
    fig = plt.figure(figsize=(13.2, 7.4))
    ax = new_axes(fig)

    header(fig, "从「有算力」到「能买到」，中间有三条通道",
           "算力、模型、应用，各自有不同的交付形态")

    cols = [
        ("算力通道", "AIDC / 智算中心", RED, [
            ("超 7GW", "AIDC 总签约规模"),
            ("92.5 EFLOPS", "智算总规模（FP16）"),
            ("150 万架+", "对外服务 IDC 机架"),
            ("8 个", "国家级/枢纽级/区域级平台"),
        ]),
        ("模型通道", "MoMA 模型服务平台", NAVY, [
            ("340+ 款", "汇聚主流模型"),
            ("0day", "首发接入"),
            ("50+ 款", "自研行业大模型"),
            ("3,500TB", "自主高质量数据集"),
        ]),
        ("应用通道", "移动天工 / 行业方案", TEAL, [
            ("32.7 万家", "服务实体企业"),
            ("100+ 款", "AI+ 产品及方案"),
            ("29 款", "垂类智能体"),
            ("1 亿+", "灵犀智能体月活"),
        ]),
    ]

    w = 0.288
    gap = 0.018
    x = 0.048
    for name, platform, color, items in cols:
        card(ax, x, 0.268, w, 0.470, color, lw=1.5)
        ax.text(x + 0.020, 0.696, name, fontsize=11.6, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(x + 0.020, 0.658, platform, fontsize=8.4, color=GRAY,
                ha="left", va="center", zorder=6)
        ax.plot([x + 0.020, x + w - 0.020], [0.636, 0.636], color=color,
                linewidth=0.9, alpha=0.35, zorder=5)
        y = 0.588
        for num, label in items:
            ax.text(x + 0.020, y, num, fontsize=12.6, color=color,
                    weight="bold", ha="left", va="center", zorder=6)
            ax.text(x + 0.020, y - 0.040, label, fontsize=7.8, color=GRAY,
                    ha="left", va="center", zorder=6)
            y -= 0.084
        x += w + gap

    ax.text(0.048, 0.204,
            "三条通道里，应用通道的「32.7 万家」最值得注意——它说明算力已经被具体的工厂用上了。",
            fontsize=9.0, color=DARK, ha="left", va="center")

    punchline(fig, "普惠不是一个价格标签，是一条从机房通到车间的路。")
    footer(fig, "事实来源：2026 中国算力大会（新华网 2026-09-12）；"
                "中国移动 2025 年年度业绩（央广网 2026-03-26）")
    fig.savefig(OUT + "图2_三条通道.png", dpi=160)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """算力普惠的三个门槛"""
    fig = plt.figure(figsize=(13.2, 7.4))
    ax = new_axes(fig)

    header(fig, "普惠要过三道门：够得着、买得起、用得对",
           "「即取即用、普惠易用」这八个字，拆开是三件完全不同的工程")

    gates = [
        ("够得着", "覆盖问题", NAVY, [
            "320+ 城市算力网络",
            "AIDC 总签约超 7GW",
            "8 个枢纽级/区域级调度平台",
            "13 个省份入选工信部专项",
        ]),
        ("买得起", "成本问题", RED, [
            "Token 工厂形态交付",
            "MoMA 汇聚 340+ 款模型",
            "在模型、集群、第三方\nToken 之间比价",
            "汕头完成 Token 出海验证",
        ]),
        ("用得对", "适配问题", TEAL, [
            "50+ 款自研行业大模型",
            "九天基座全栈国产可控",
            "服务实体企业 32.7 万家",
            "模型微调贴合行业现场",
        ]),
    ]

    w = 0.288
    gap = 0.018
    x = 0.048
    for name, tag, color, points in gates:
        card(ax, x, 0.320, w, 0.420, color, lw=1.5)
        ax.text(x + 0.020, 0.694, name, fontsize=13.0, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(x + 0.020, 0.652, tag, fontsize=8.8, color=GRAY,
                ha="left", va="center", zorder=6)
        ax.plot([x + 0.020, x + w - 0.020], [0.628, 0.628], color=color,
                linewidth=0.9, alpha=0.35, zorder=5)
        y = 0.582
        for p in points:
            ax.text(x + 0.020, y, "· " + p, fontsize=8.0, color=DARK,
                    ha="left", va="top", linespacing=1.60, zorder=6)
            y -= 0.046 if "\n" not in p else 0.076
        x += w + gap

    ax.text(0.048, 0.252,
            "三道门里，前两道能被数字证明；第三道只能被客户证明。",
            fontsize=9.2, color=DARK, ha="left", va="center")

    punchline(fig, "算力普惠最难的不是降价，是让每一家都找到自己能用的那一款。")
    footer(fig, "事实来源：2026 中国算力大会（新华网 2026-09-12）；全国一体化算力网技术创新体系"
                "（新华网 2026-05-09）；算网大脑 4.0（2026-11 媒体报道）")
    fig.savefig(OUT + "图3_三道门.png", dpi=160)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)
