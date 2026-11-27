# -*- coding: utf-8 -*-
"""
《21 个场景全网推广、17 个试点突破：自智网络的 L4 是怎么爬上去的》配套图表

事实口径（2026-11-06 广州，2026 移动网络大会「网络强基论坛」）：
  · 《中国移动自智网络白皮书（2026版）》发布，阐释「四要素一闭环」总体规划、
    「五个以」落地方法与「三化」技术发展策略，倡议产业向
    「人工智能+信息通信」深度延伸、向新一代通信网演进延伸、向海外自智网络市场延伸。
  · 「三化」：业务本体化、应用智能化、演进自主化（中国移动副总经理李慧镝提出）。
  · 规模底座：每天超过 3 亿台设备在网运行，服务超 10 亿移动用户、
    宽带联网用户和 5 亿物联网用户，日均产生 14PB 运维数据；
    手机上网流量中 AI 流量占比已较年初增长五倍。
  · 进度：21 个 L4 高价值自智场景完成全网规模推广，17 个场景实现 L4 试点突破；
    重点业务开通效率提升 72%；今年底目标推动 38 个场景达到 L4。
  · 标准与评测：累计主导行业及国际标准 230 项，标准贡献量居全球运营商第一；
    TM Forum 全部 13 个自智网络场景评估中，12 个场景位列全球第一；
    获 ITU WSIS、ITU AI4G、GSMA GLOMO、TM Forum Excellence 等国际及行业奖项超 20 项。
  · 案例数据：A2A-T 通信智能体交互协议全球首发、多地试点；跨域故障管理场景
    智能体交互准确率提升至 95% 以上，故障处理从周级缩短至天级，每年挽回流量损失 880TB；
    SPN 专线投诉处理自动化诊断成功率 90%，投诉平均处理时长下降 26%；
    远程调优支撑家庭宽带质量主动修复年均超 400 万次，网络质量满意度同比提升约 11%；
    面向生成式 AI 用户突破 7 亿户，借数字孪生与 GSRv6 使业务访问时延降低 15%、
    丢包率减少 41%。
  · 行业参照（TM Forum）：自智网络产业参与者从 2019 年 7 家增至 2026 年近百家；
    对 80 家运营商调研，20% 预计 2027 年前达到 AN L4 或以上，81% 将 2030 年设为目标节点。
  据 C114 通信网 2026-11-08/09（蒋均牧）、人民邮电报 2026-11-07、光互连 2026-11。

风格：克制传媒风，编辑排版
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
Q_L, Q_R = "\u300c", "\u300d"


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
    ax.text(0.042, 0.028, text, fontsize=7.0, color=MUTED,
            ha="left", va="center", zorder=9)


def outro(fig, ax, text, color=INK):
    ax.add_patch(FancyBboxPatch(
        (0.042, 0.082), 0.720, 0.048,
        boxstyle="round,pad=0.002,rounding_size=0.008",
        facecolor=color, edgecolor="none", zorder=6))
    ax.text(0.062, 0.106, text, fontsize=10.2, color=WHITE,
            ha="left", va="center", zorder=9)


def panel(ax, x, y, w, h, accent, face=WHITE, bar=0.0055, shadow=True):
    if shadow:
        ax.add_patch(FancyBboxPatch(
            (x + 0.0035, y - 0.0035), w, h,
            boxstyle="round,pad=0,rounding_size=0.009",
            facecolor="#e9ecf0", edgecolor="none", zorder=2))
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0,rounding_size=0.009",
        facecolor=face, edgecolor="#e6eaee", linewidth=0.9, zorder=3))
    ax.add_patch(FancyBboxPatch(
        (x, y), bar, h,
        boxstyle="round,pad=0,rounding_size=0.0028",
        facecolor=accent, edgecolor="none", zorder=4))


# ---------------------------------------------------------------- 图 1
def fig1():
    fig = plt.figure(figsize=(13.6, 8.0))
    ax = new_axes(fig)

    head(fig, ax, "L4 的爬坡路线",
         "21 个场景全网推广，17 个还在试点",
         "年底目标 38 个场景达到 L4——这意味着剩下的 17 个要在几个月内转正",
         RED)

    # 三段进度条（漏斗式）
    ax.text(0.042, 0.762, "自智能力推进的三个梯队（单位：场景数）", fontsize=8.6,
            color=MUTED, ha="left", va="center")
    ax.plot([0.042, 0.958], [0.742, 0.742], color=HAIR, linewidth=1.0)

    tiers = [
        ("已全网规模推广", 21, NAVY, "已经跑在所有省公司"),
        ("已试点突破", 17, GOLD, "部分地区验证通过"),
        ("年底目标", 38, RED, "两者合计，须全部达到 L4"),
    ]

    maxv = 38.0
    y = 0.672
    for name, val, color, note in tiers:
        ax.text(0.042, y + 0.014, name, fontsize=10.2, color=INK,
                weight="bold", ha="left", va="center", zorder=9)
        ax.text(0.042, y - 0.022, note, fontsize=7.8, color=MUTED,
                ha="left", va="center", zorder=9)

        bw = 0.290 * (val / maxv)
        ax.add_patch(FancyBboxPatch(
            (0.330, y - 0.024), bw, 0.042,
            boxstyle="round,pad=0,rounding_size=0.008",
            facecolor=color, edgecolor="none", zorder=6))
        ax.text(0.330 + bw + 0.014, y - 0.003, str(val), fontsize=17.0,
                color=color, weight="bold", ha="left", va="center",
                zorder=9)
        y -= 0.122

    ax.text(0.042, 0.290,
            "21 + 17 = 38。这个加法不是凑数——它说明 L4 的门槛不是"
            "\u300c能不能做到\u300d,而是\u300c能不能全网复制\u300d。",
            fontsize=8.8, color=INK, ha="left", va="center")

    # 右侧：三个"看得见"的结果
    panel(ax, 0.660, 0.150, 0.298, 0.548, RED, face=WHITE)
    ax.text(0.682, 0.672, "已兑现的效果", fontsize=9.0, color=MUTED,
            ha="left", va="center", zorder=9)

    stats = [
        ("72%", "重点业务开通效率提升"),
        ("95% 以上", "跨域故障智能体交互准确率"),
        ("880TB", "每年挽回的流量损失"),
        ("26%", "SPN 投诉处理时长下降"),
    ]
    y = 0.616
    for num, label in stats:
        ax.text(0.682, y, num, fontsize=15.0, color=RED, weight="bold",
                ha="left", va="center", zorder=9)
        ax.text(0.682, y - 0.038, label, fontsize=7.6, color=INK,
                ha="left", va="top", zorder=9)
        y -= 0.108

    outro(fig, ax, "自智网络的价值不在演示，在把周级的事变成天级。")
    foot(fig, ax, "事实来源：2026 移动网络大会网络强基论坛（2026-11-06，广州）；"
         "C114 通信网 2026-11-08、人民邮电报 2026-11-07")

    fig.savefig(OUT + "图1_三个梯队.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(13.6, 8.0))
    ax = new_axes(fig)

    head(fig, ax, "三化方法论",
         "AI 要真正进网络，先得让网络能被读懂",
         "业务本体化、应用智能化、演进自主化——三件事解决三个不同层面的问题",
         NAVY)

    cols = [
        ("业务本体化", "让 AI 看得懂", NAVY, [
            ("解决的问题", "网络对象与规则分散、名称标识不一"),
            ("做什么", "构建统一的业务语义体系"),
            ("类比", "给 AI 一本网络词典与语法"),
            ("判断标准", "AI 能否自主判断操作条件"),
        ]),
        ("应用智能化", "让 AI 能协同", RED, [
            ("解决的问题", "应用靠预设流程，遇变化需人工介入"),
            ("做什么", "环节智能 → 流程智能 → 体系智能"),
            ("类比", "从一个人干活到一条流水线"),
            ("判断标准", "能否跨域跨系统闭环"),
        ]),
        ("演进自主化", "让 AI 会进化", TEAL, [
            ("解决的问题", "经验沉淀不下来，下次还得重来"),
            ("做什么", "把运行经验沉淀为知识、策略、技能"),
            ("类比", "老员工的直觉变成可复制的规则"),
            ("判断标准", "模型与智能体能否持续自改进"),
        ]),
    ]

    x = 0.042
    w = 0.288
    gap = 0.019
    for i, (name, tag, color, items) in enumerate(cols):
        panel(ax, x, 0.226, w, 0.504, color)

        ax.text(x + 0.026, 0.694, name, fontsize=14.5, color=color,
                weight="bold", ha="left", va="center", zorder=9)
        ax.text(x + 0.026, 0.658, tag, fontsize=9.4, color=MUTED,
                ha="left", va="center", zorder=9)
        ax.plot([x + 0.026, x + w - 0.026], [0.636, 0.636], color=HAIR,
                linewidth=1.0, zorder=5)

        yy = 0.592
        for k, v in items:
            ax.text(x + 0.026, yy, k, fontsize=7.4, color=MUTED,
                    ha="left", va="center", zorder=9)
            ax.text(x + 0.026, yy - 0.028, v, fontsize=8.4, color=INK,
                    weight="bold", ha="left", va="center", zorder=9)
            yy -= 0.078

        if i < 2:
            ax.annotate("", xy=(x + w + gap - 0.001, 0.478),
                        xytext=(x + w + 0.001, 0.478),
                        arrowprops=dict(arrowstyle="-|>", color="#c9d0d8",
                                        linewidth=1.8, shrinkA=0, shrinkB=0))
        x += w + gap

    ax.add_patch(FancyBboxPatch(
        (0.042, 0.140), 0.916, 0.068,
        boxstyle="round,pad=0,rounding_size=0.008",
        facecolor=WASH, edgecolor="none", zorder=3))
    ax.text(0.062, 0.174,
            "三化是递进的：没有本体，AI 读不懂；读不懂，就谈不上跨域协同；不能协同，经验沉淀不下来。",
            fontsize=8.6, color=INK, ha="left", va="center", zorder=9)

    outro(fig, ax, "L3 到 L4 之间隔的不是算法，是一套让 AI 读懂业务的方法。")
    foot(fig, ax, "事实来源：中国移动副总经理李慧镝在 2026 移动网络大会网络强基论坛的发言；"
         "C114 通信网 2026-11-08 对「三化」的解读")

    fig.savefig(OUT + "图2_三化.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(13.6, 8.0))
    ax = new_axes(fig)

    head(fig, ax, "为什么必须自智",
         "3 亿台设备、14PB 数据：人工已经管不过来了",
         "规模本身，就是自智网络最硬的驱动力",
         GOLD)

    # 左侧四个规模数字
    stats = [
        ("3 亿+", "台设备在网运行", NAVY),
        ("10 亿+", "移动用户", TEAL),
        ("5 亿", "物联网用户", GOLD),
        ("14 PB", "日均运维数据", RED),
    ]

    ax.text(0.042, 0.760, "每天要面对的规模", fontsize=8.6, color=MUTED,
            ha="left", va="center")
    ax.plot([0.042, 0.500], [0.740, 0.740], color=HAIR, linewidth=1.0)

    y = 0.678
    for num, label, color in stats:
        ax.text(0.042, y, num, fontsize=22.0, color=color, weight="bold",
                ha="left", va="center", zorder=9)
        ax.text(0.230, y - 0.004, label, fontsize=8.8, color=INK,
                ha="left", va="center", zorder=9)
        y -= 0.114

    ax.text(0.042, 0.240,
            "这些数字每年还在涨。靠加人解决不了，只能靠网络自己管自己。",
            fontsize=8.6, color=MUTED, ha="left", va="center")

    # 右侧：AI 流量带来的新压力
    ax.text(0.560, 0.760, "AI 流量带来的三种新压力", fontsize=8.6, color=MUTED,
            ha="left", va="center")
    ax.plot([0.560, 0.958], [0.740, 0.740], color=HAIR, linewidth=1.0)

    panel(ax, 0.560, 0.500, 0.398, 0.212, RED, face=WHITE)
    ax.text(0.582, 0.676, "AI 流量占比", fontsize=8.8, color=MUTED,
            ha="left", va="center", zorder=9)
    ax.text(0.582, 0.622, "较年初增长 5 倍", fontsize=17.0, color=RED,
            weight="bold", ha="left", va="center", zorder=9)
    ax.text(0.582, 0.570, "手机上网流量中 AI 流量的占比", fontsize=7.8,
            color=INK, ha="left", va="center", zorder=9)
    ax.text(0.582, 0.534, "生成式 AI 用户已突破 7 亿户", fontsize=7.8,
            color=INK, ha="left", va="center", zorder=9)

    pressures = [
        ("老鼠流与大象流交织", "小流量连接多、大流量突发猛，调度颗粒度不够"),
        ("多轮推理要求极低抖动", "时延抖一下，推理链就断"),
        ("首 Token 时延要卡死", "端侧交互对首包时间极度敏感"),
    ]
    y = 0.442
    for name, note in pressures:
        ax.add_patch(Circle((0.568, y), 0.0040, facecolor=RED,
                            edgecolor="none", zorder=8))
        ax.text(0.582, y, name, fontsize=8.8, color=INK, weight="bold",
                ha="left", va="center", zorder=9)
        ax.text(0.582, y - 0.030, note, fontsize=7.6, color=MUTED,
                ha="left", va="center", zorder=9)
        y -= 0.076

    ax.add_patch(FancyBboxPatch(
        (0.042, 0.140), 0.916, 0.070,
        boxstyle="round,pad=0,rounding_size=0.008",
        facecolor=WASH, edgecolor="none", zorder=3))
    ax.text(0.062, 0.176,
            "面对这些，传统人工经验和外挂式 AI 都难以有效管理——这句话是公司自己说的。",
            fontsize=8.6, color=INK, ha="left", va="center", zorder=9)

    outro(fig, ax, "自智网络不是锦上添花，是规模涨到某个点后的唯一解。")
    foot(fig, ax, "事实来源：2026 移动网络大会网络强基论坛；C114 通信网 2026-11-08")

    fig.savefig(OUT + "图3_为什么必须自智.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)
