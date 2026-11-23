# -*- coding: utf-8 -*-
"""
《国产大模型先解决的不是"能不能"，是"敢不敢用"》配套图表 —— 视觉增强版
设计规范同 013，统一视觉语言。
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, Polygon

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
WASH2 = "#ebeff3"
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
        (0.042, 0.082), 0.700, 0.048,
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

    head(fig, ax, "工业客户的真实门槛",
         "从「能用」到「敢用」，中间有四道门",
         "看得懂、信得过、说得清、用得起——顺序不能颠倒",
         RED)

    gates = [
        ("第一道", "看得懂", "多模态理解", NAVY,
         ["文本、图像、视频联合理解", "工业图纸、巡检照片、仪表读数"]),
        ("第二道", "信得过", "防得住攻击", RED,
         ["指令藏进图像纹理、照片角落", "传统文本安全机制难以察觉"]),
        ("第三道", "说得清", "可解释可追溯", GOLD,
         ["数据来源可追溯：时间、地点、路径", "推理过程可解释：深度思维链"]),
        ("第四道", "用得起", "成本可控", TEAL,
         ["单位 Token 成本压降", "资源占用率下降，同投入更多调用"]),
    ]

    x = 0.042
    w = 0.222
    gap = 0.0145
    for i, (num, name, sub, color, points) in enumerate(gates):
        panel(ax, x, 0.300, w, 0.400, color)

        # 序号底块
        ax.add_patch(Circle((x + 0.040, 0.658), 0.0185, facecolor=color,
                            edgecolor="none", zorder=8))
        ax.text(x + 0.040, 0.658, str(i + 1), fontsize=11.0, color=WHITE,
                weight="bold", ha="center", va="center", zorder=9)

        ax.text(x + 0.070, 0.658, num, fontsize=8.4, color=MUTED,
                ha="left", va="center", zorder=9)
        ax.text(x + 0.032, 0.610, name, fontsize=15.5, color=color,
                weight="bold", ha="left", va="center", zorder=9)
        ax.text(x + 0.032, 0.572, sub, fontsize=8.8, color=MUTED,
                ha="left", va="center", zorder=9)
        ax.plot([x + 0.032, x + w - 0.032], [0.548, 0.548], color=HAIR,
                linewidth=1.0, zorder=5)

        yy = 0.508
        for p in points:
            ax.add_patch(Circle((x + 0.038, yy), 0.0038, facecolor=color,
                                edgecolor="none", zorder=8))
            ax.text(x + 0.052, yy, p, fontsize=8.0, color=INK,
                    ha="left", va="center", zorder=9)
            yy -= 0.052

        if i < 3:
            ax.annotate("", xy=(x + w + gap - 0.001, 0.500),
                        xytext=(x + w + 0.001, 0.500),
                        arrowprops=dict(arrowstyle="-|>", color="#c9d0d8",
                                        linewidth=1.6, shrinkA=0,
                                        shrinkB=0))
        x += w + gap

    # 底部两段说明
    ax.text(0.042, 0.252, "前两道门决定" + Q_L + "能不能用" + Q_R +
            "，后两道门决定" + Q_L + "敢不敢大规模铺" + Q_R + "。",
            fontsize=9.6, color=INK, ha="left", va="center")

    outro(fig, ax, "工业客户不缺模型，缺的是一个敢签字的理由。")
    foot(fig, ax, "事实来源：新华网 2026-07-19《中国移动九天多模态大模型+MoMA 多模型服务引擎"
         "打造安全可控智能中枢》")

    fig.savefig(OUT + "图1_四道门.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(13.6, 8.0))
    ax = new_axes(fig)

    head(fig, ax, "一个系列，两条能力线",
         "一个系列，两个规格，两条能力线",
         "JT4.0 起，通用能力与安全可信同向推进；JT4.1 补上多模态",
         GOLD)

    # 左：两个规格
    ax.text(0.042, 0.762, "两个规格（JT4.0 起）", fontsize=8.6, color=MUTED,
            ha="left", va="center")
    ax.plot([0.042, 0.400], [0.742, 0.742], color=HAIR, linewidth=1.0)

    vers = [
        ("236B", "MoE 架构", "稀疏激活\n适合大规模在线服务", NAVY),
        ("35B", "稠密架构", "单机部署\n适合行业定制与私有化", TEAL),
    ]
    y = 0.660
    for num, arch, note, color in vers:
        panel(ax, 0.042, y - 0.058, 0.358, 0.118, color)
        ax.text(0.062, y + 0.012, num, fontsize=26, color=color,
                weight="bold", ha="left", va="center", zorder=9)
        ax.text(0.172, y + 0.020, arch, fontsize=10.6, color=INK,
                weight="bold", ha="left", va="center", zorder=9)
        ax.text(0.172, y - 0.022, note, fontsize=7.8, color=MUTED,
                ha="left", va="top", linespacing=1.55, zorder=9)
        y -= 0.148

    ax.add_patch(FancyBboxPatch(
        (0.042, 0.330), 0.358, 0.078,
        boxstyle="round,pad=0,rounding_size=0.008",
        facecolor=WASH, edgecolor="none", zorder=3))
    ax.text(0.062, 0.394, "共用同一套安全可信能力", fontsize=9.0,
            color=INK, weight="bold", ha="left", va="center", zorder=9)
    ax.text(0.062, 0.360, "区别在部署形态，不在安全等级", fontsize=8.2,
            color=MUTED, ha="left", va="center", zorder=9)

    # 右：两条能力线
    ax.text(0.470, 0.762, "两条能力线同时推进", fontsize=8.6, color=MUTED,
            ha="left", va="center")
    ax.plot([0.470, 0.958], [0.742, 0.742], color=HAIR, linewidth=1.0)

    lines = [
        ("安全", "防的是攻击", RED, [
            ("视觉 DWC 全信数据体系", "给图片补时间、地点、传播路径"),
            ("隐蔽攻击专项增强", "指令藏进纹理或角落也能识别"),
            ("从源头拦截", "风险在数据构建阶段就被识别"),
        ]),
        ("可信", "求的是内生", GOLD, [
            ("九天价值罗盘", "从外部约束转向内生价值观"),
            ("12 个维度评估", "系统提升安全可信能力"),
            ("深度思维链", "让推理过程可解释"),
        ]),
    ]

    y0 = 0.700
    for tag, sub, color, items in lines:
        ax.add_patch(Rectangle((0.470, y0 - 0.016), 0.006, 0.032,
                               facecolor=color, edgecolor="none", zorder=8))
        ax.text(0.490, y0, tag, fontsize=13.0, color=color, weight="bold",
                ha="left", va="center", zorder=9)
        ax.text(0.545, y0 - 0.002, sub, fontsize=8.4, color=MUTED,
                ha="left", va="center", zorder=9)

        y = y0 - 0.058
        for name, note in items:
            ax.text(0.490, y, name, fontsize=9.4, color=INK,
                    weight="bold", ha="left", va="center", zorder=9)
            ax.text(0.490, y - 0.032, note, fontsize=8.0, color=MUTED,
                    ha="left", va="center", zorder=9)
            y -= 0.074
        y0 = y - 0.030

    outro(fig, ax, "安全不是一个补丁，是一条和参数一起长的能力线。")
    foot(fig, ax, "事实来源：九天安全可信大模型 JT4.0（2026-04-29）、JT4.1（2026-07-17）；"
         "新华网 2026-07-19")

    fig.savefig(OUT + "图2_两个规格.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(13.6, 8.0))
    ax = new_axes(fig)

    head(fig, ax, "多模型时代的选型难题",
         "模型多了之后，难题不是" + Q_L + "有没有" + Q_R + "，是" + Q_L + "选哪个" + Q_R,
         "MoMA 2.0 把选型、编排、控成本三件事做成了一层服务",
         TEAL)

    steps = [
        ("用户提交任务", "一句话，不必说明用哪个模型", NAVY),
        ("自动选模", "按业务场景匹配最优模型", RED),
        ("动态编排", "复杂任务自动拆解，多模型协同", GOLD),
        ("成本压降", "单位 Token 成本与资源占用率下降", TEAL),
        ("全链路防护", "请求接入到结果返回，全程可控", NAVY),
    ]

    y = 0.690
    for i, (name, detail, color) in enumerate(steps):
        panel(ax, 0.042, y - 0.062, 0.520, 0.076, color)
        ax.add_patch(Circle((0.072, y - 0.024), 0.0135, facecolor=color,
                            edgecolor="none", zorder=8))
        ax.text(0.072, y - 0.024, str(i + 1), fontsize=8.6, color=WHITE,
                weight="bold", ha="center", va="center", zorder=9)
        ax.text(0.100, y - 0.024, name, fontsize=9.8, color=color,
                weight="bold", ha="left", va="center", zorder=9)
        ax.text(0.268, y - 0.024, detail, fontsize=8.2, color=MUTED,
                ha="left", va="center", zorder=9)
        y -= 0.098

    # 右侧：落地情况
    ax.text(0.610, 0.762, "已经跑在哪", fontsize=8.6, color=MUTED,
            ha="left", va="center")
    ax.plot([0.610, 0.958], [0.742, 0.742], color=HAIR, linewidth=1.0)

    ax.text(0.610, 0.680, "20 余个", fontsize=30, color=TEAL, weight="bold",
            ha="left", va="center", zorder=9)
    ax.text(0.610, 0.628, "业务场景已接入", fontsize=8.8, color=MUTED,
            ha="left", va="center", zorder=9)

    scopes = [
        ("灵犀智能体 2.0", "月活超 1 亿（2025 年报口径）"),
        ("5G 消息", "通信场景"),
        ("家庭泛屏", "家庭场景"),
        ("办公 · 出行 · 生活", "多类日常使用"),
    ]
    y = 0.570
    for a, b in scopes:
        ax.add_patch(Circle((0.618, y), 0.0038, facecolor=TEAL,
                            edgecolor="none", zorder=8))
        ax.text(0.632, y, a, fontsize=9.0, color=INK, weight="bold",
                ha="left", va="center", zorder=9)
        ax.text(0.632, y - 0.030, b, fontsize=7.8, color=MUTED,
                ha="left", va="center", zorder=9)
        y -= 0.074

    ax.add_patch(FancyBboxPatch(
        (0.610, 0.210), 0.348, 0.086,
        boxstyle="round,pad=0,rounding_size=0.008",
        facecolor=WASH, edgecolor="none", zorder=3))
    ax.text(0.628, 0.264, "模型数量解决" + Q_L + "有没有" + Q_R + "，",
            fontsize=8.6, color=INK, ha="left", va="center", zorder=9)
    ax.text(0.628, 0.232, "引擎解决" + Q_L + "用得对不对" + Q_R + "。",
            fontsize=8.6, color=INK, ha="left", va="center", zorder=9)

    outro(fig, ax, "选型能力本身，正在变成一种可交付的产品。")
    foot(fig, ax, "事实来源：新华网 2026-07-19；MoMA 于 2025 年世界人工智能大会首发；"
         "灵犀智能体月活数据据中国移动 2025 年年度业绩")

    fig.savefig(OUT + "图3_MoMA引擎.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)
