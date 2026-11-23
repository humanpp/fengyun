# -*- coding: utf-8 -*-
"""
《6G 还有三十个月：标准冻结前的窗口期，比的是什么》配套图表 —— 视觉增强版
设计规范同 013/014，统一视觉语言。
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

    head(fig, ax, "5G 到 6G 的能力边界",
         "5G 到 6G，最大的变化是" + Q_L + "三个一体" + Q_R,
         "天地一体、通感一体、通智一体——每一项都在改写基站的定义",
         GOLD)

    cols = [
        ("天地一体", "把覆盖从地面推到三维", GOLD, [
            ("组网方式", "地面基站 + 低轨卫星 + 高空平台"),
            ("落地载体", "02 星、天启星座"),
            ("终端侧", "手机直连天通 + 北斗"),
        ], "5G：以地面为主，卫星补盲", "6G：天地统一组网"),
        ("通感一体", "让基站兼做雷达", NAVY, [
            ("核心能力", "同一套设备同时通信与感知"),
            ("关键用途", "低空飞行器定位与轨迹跟踪"),
            ("延伸价值", "为低空经济提供监管能力"),
        ], "5G：通信为主，感知是附加", "6G：感知成为内生能力"),
        ("通智一体", "把 AI 放进网络里", RED, [
            ("网络侧", "AI 内生进 RAN（无线接入网）"),
            ("终端侧", "AI 内生进终端"),
            ("效果", "网络自己优化自己"),
        ], "5G：AI 外挂，做运维辅助", "6G：AI 成为网络组成"),
    ]

    w = 0.288
    gap = 0.019
    x = 0.042
    for name, tag, color, items, g5, g6 in cols:
        panel(ax, x, 0.200, w, 0.578, color)

        ax.text(x + 0.026, 0.736, name, fontsize=15.0, color=color,
                weight="bold", ha="left", va="center", zorder=9)
        ax.text(x + 0.026, 0.700, tag, fontsize=8.6, color=MUTED,
                ha="left", va="center", zorder=9)
        ax.plot([x + 0.026, x + w - 0.026], [0.678, 0.678], color=HAIR,
                linewidth=1.0, zorder=5)

        yy = 0.632
        for k, v in items:
            ax.text(x + 0.026, yy, k, fontsize=8.0, color=MUTED,
                    ha="left", va="center", zorder=9)
            ax.text(x + 0.026, yy - 0.028, v, fontsize=8.8, color=INK,
                    weight="bold", ha="left", va="center", zorder=9)
            yy -= 0.072

        # 5G vs 6G 对照
        ax.add_patch(FancyBboxPatch(
            (x + 0.026, 0.216), w - 0.052, 0.094,
            boxstyle="round,pad=0,rounding_size=0.008",
            facecolor=WASH, edgecolor="none", zorder=6))
        ax.text(x + 0.042, 0.284, g5, fontsize=8.0, color=MUTED,
                ha="left", va="center", zorder=9)
        ax.text(x + 0.042, 0.244, g6, fontsize=8.6, color=color,
                weight="bold", ha="left", va="center", zorder=9)

        x += w + gap

    outro(fig, ax, "6G 争的不是网速，是基站还能干多少别的事。")
    foot(fig, ax, "事实来源：2026 移动网络大会（2026-11-05 至 07，广州）中国移动"
         + Q_L + "三个一体" + Q_R + "表述（SatNet News 2026-11-21 转述）；经济参考报 2026-11-16")

    fig.savefig(OUT + "图1_三个一体.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(13.6, 8.0))
    ax = new_axes(fig)

    head(fig, ax, "标准冻结前的窗口期",
         "距离标准冻结不到 30 个月",
         "这段时间决定 6G 将来的频谱、场景和话语权",
         RED)

    # 时间轴
    ty = 0.660
    ax.plot([0.070, 0.930], [ty, ty], color="#e6eaf0", linewidth=4.0,
            zorder=2, solid_capstyle="round")

    nodes = [
        (0.110, "2024", "5G-A 商用启动", "5G 的能力延长线", MUTED),
        (0.370, "2026 年 9 月", "系统化验证", "U6G 基站与终端原型对接", NAVY),
        (0.630, "2026 年 11 月", "不到 30 个月", "需求牵引网络设计", RED),
        (0.890, "2029 年 5 月", "倒推的落点", "据「不到 30 个月」推算", GOLD),
    ]
    for cx, top, title, note, color in nodes:
        ax.add_patch(Circle((cx, ty), 0.0115, facecolor=color,
                            edgecolor=WHITE, linewidth=2.2, zorder=7))
        ax.text(cx, ty + 0.058, top, fontsize=11.0, color=color,
                weight="bold", ha="center", va="bottom", zorder=9)
        ax.text(cx, ty + 0.026, title, fontsize=9.0, color=INK,
                ha="center", va="bottom", zorder=9)
        ax.text(cx, ty - 0.048, note, fontsize=7.8, color=MUTED,
                ha="center", va="top", zorder=9, linespacing=1.5)

    # 三块：要定的事 / 要投的钱 / 要养的人
    ax.text(0.042, 0.530, "这三十个月要落定的三件事", fontsize=8.6,
            color=MUTED, ha="left", va="center")

    blocks = [
        ("要定的事", "频谱 · 场景 · 架构", "标准冻结前定不下来，后面全是返工", NAVY),
        ("要投的钱", "十亿元级", "研发合作资金，支持关键技术攻关与应用创新", RED),
        ("要养的人", "百亿元级", "产业投资基金，培育专精特新企业与成果转化", TEAL),
    ]
    x = 0.042
    w = 0.288
    gap = 0.019
    for name, num, note, color in blocks:
        panel(ax, x, 0.300, w, 0.196, color)
        ax.text(x + 0.026, 0.452, name, fontsize=9.0, color=MUTED,
                ha="left", va="center", zorder=9)
        ax.text(x + 0.026, 0.404, num, fontsize=17.0, color=color,
                weight="bold", ha="left", va="center", zorder=9)
        ax.text(x + 0.026, 0.348, note, fontsize=8.0, color=INK,
                ha="left", va="top", linespacing=1.55, zorder=9)
        x += w + gap

    ax.add_patch(FancyBboxPatch(
        (0.042, 0.196), 0.916, 0.072,
        boxstyle="round,pad=0,rounding_size=0.008",
        facecolor=WASH, edgecolor="none", zorder=3))
    ax.text(0.062, 0.232,
            "三十个月里要同时完成：频谱协调、场景验证、架构定型、样机测试、标准文本多轮投票。",
            fontsize=8.6, color=INK, ha="left", va="center", zorder=9)

    outro(fig, ax, "标准是提前写好的规则，谁参与写，谁就少走弯路。")
    foot(fig, ax, "事实来源：经济参考报 2026-11-16（王晓云" + Q_L +
         "距离 6G 标准冻结已不到 30 个月" + Q_R + "）；2026 年 9 月 U6G 频段原型对接测试")

    fig.savefig(OUT + "图2_三十个月.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(13.6, 8.0))
    ax = new_axes(fig)

    head(fig, ax, "先定场景，再定网络",
         "先想清楚用在哪儿，再决定网络怎么建",
         "6G 智能应用共创行动圈定十大高价值场景，牵引网络技术创新",
         TEAL)

    scenes = [
        ("网联机器人", "工厂与园区", NAVY, True),
        ("AI 终端", "端侧推理", NAVY, True),
        ("沉浸式通信", "全息与空间视频", RED, True),
        ("空天地海一体", "全域覆盖", RED, True),
        ("智能体群智协作", "多智能体协同", RED, True),
        ("工业实时控制", "确定性时延", TEAL, False),
        ("低空经济", "通感一体", TEAL, False),
        ("车路云一体", "高可靠低时延", TEAL, False),
        ("数字孪生", "大上行与大带宽", GOLD, False),
        ("应急与公共安全", "无网时可用", GOLD, False),
    ]

    x0, y0 = 0.042, 0.566
    w, h = 0.170, 0.106
    gx, gy = 0.0145, 0.020
    for i, (name, note, color, core) in enumerate(scenes):
        col = i % 5
        row = i // 5
        cx = x0 + col * (w + gx)
        cy = y0 - row * (h + gy)
        panel(ax, cx, cy, w, h, color)
        ax.text(cx + 0.016, cy + h - 0.034, name, fontsize=8.6,
                color=color, weight="bold", ha="left", va="center",
                zorder=9)
        ax.text(cx + 0.016, cy + h - 0.072, note, fontsize=7.4,
                color=MUTED, ha="left", va="center", zorder=9)

    ax.text(0.042, 0.336,
            "前五项为公开材料明确列出的场景；后五项为同类高价值场景的归纳，仅供参考。",
            fontsize=7.6, color=MUTED, ha="left", va="center")

    # 5G → 6G 定性
    ax.add_patch(FancyBboxPatch(
        (0.042, 0.180), 0.916, 0.116,
        boxstyle="round,pad=0,rounding_size=0.009",
        facecolor=WHITE, edgecolor="#e6eaee", linewidth=0.9, zorder=3))
    ax.add_patch(FancyBboxPatch(
        (0.042, 0.180), 0.0055, 0.116,
        boxstyle="round,pad=0,rounding_size=0.0028",
        facecolor=NAVY, edgecolor="none", zorder=4))

    ax.text(0.066, 0.262, "5G 万物互联", fontsize=12.0, color=MUTED,
            weight="bold", ha="left", va="center", zorder=9)
    ax.annotate("", xy=(0.352, 0.262), xytext=(0.258, 0.262),
                arrowprops=dict(arrowstyle="-|>", color=NAVY,
                                linewidth=2.0, shrinkA=0, shrinkB=0))
    ax.text(0.378, 0.262, "6G 万物智联", fontsize=12.0, color=NAVY,
            weight="bold", ha="left", va="center", zorder=9)
    ax.text(0.066, 0.212,
            "服务对象从人机物扩展到智能体；服务空间从地面拓展到空天地。",
            fontsize=8.4, color=INK, ha="left", va="center", zorder=9)

    outro(fig, ax, "6G 的设计起点，从「网能跑多快」变成了「谁要用、用来干什么」。")
    foot(fig, ax, "事实来源：经济参考报 2026-11-16；中国信息通信研究院杜滢对 6G 新场景的表述"
         "（转引自该报道）")

    fig.savefig(OUT + "图3_十大场景.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)
