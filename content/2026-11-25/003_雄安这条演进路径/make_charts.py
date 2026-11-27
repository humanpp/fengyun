# -*- coding: utf-8 -*-
"""
《雄安这条路径：5G-A 先用起来，6G 在后面等着》配套图表

事实口径（2026-11-25，河北日报；中国雄安官网转载）：
  · 中国移动在雄安率先完成 5G-A 技术的规模组网部署，为 6G 演进探路。
  · 京雄快线航站楼地下空间已部署 5G-A 网络：列车穿行隧道时，
    手机视频通话、高清直播等仍能保持信号稳定；航站楼客流高峰期，
    5G-A 网络可自动识别乘客的网络需求（微信聊天、网页浏览、短视频等），
    按不同业务需要分配带宽和时延资源。
  · 6G 研发：自 2018 年起中国移动率先启动 6G 研发，构建通、感、算、智融合的
    6G 技术体系，研制业界领先的 6G 原型样机，不少技术验证在雄安开展。
  · 中国工程院院士、中国移动总工程师王晓云：6G 将成为智能时代的新型网络底座，
    将提供更强的连接服务以及超越连接服务。
  · 中国移动已牵头建立信息产业协同创新基地和高校联合研发载体，
    研制 6G 研发试验装置，开放 6G 关键技术验证能力。
  · 雄安新区正在为 6G 创新发展部省协同试点做首批核心节点部署准备
    （中国移动（雄安）智慧城市科创中心）。
  · 相关对照（2026-11-16 经济参考报）：6G 新引入通信与 AI 融合、通信与感知融合、
    星地融合等新技术新场景；服务对象从人机物扩展到智能体；
    2026 年 11 月中国移动披露 6G 实验在 U6GHz 特定波段实现单载波 18Gbps 下载速率；
    2026 年 9 月高通与中国移动完成 U6G 频段基站原型与 6G 终端原型对接测试。

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
        (0.042, 0.082), 0.740, 0.048,
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

    head(fig, ax, "代际演进的时间轴",
         "5G-A 先用起来，6G 在后面等着",
         "同一张网的两代技术，在同一个城市里同时推进",
         NAVY)

    # 时间轴
    ty = 0.620
    ax.plot([0.070, 0.930], [ty, ty], color="#e6eaf0", linewidth=4.0,
            zorder=2, solid_capstyle="round")

    nodes = [
        (0.110, "2018", "启动 6G 研发", "比 5G 商用还早一年", MUTED),
        (0.360, "2024 前后", "5G-A 规模部署", "雄安率先完成", NAVY),
        (0.610, "2026", "6G 原型样机", "通、感、算、智融合", GOLD),
        (0.880, "标准冻结前", "部省协同试点", "雄安部署首批核心节点", RED),
    ]
    for cx, top, title, note, color in nodes:
        ax.add_patch(Circle((cx, ty), 0.0115, facecolor=color,
                            edgecolor=WHITE, linewidth=2.2, zorder=7))
        ax.text(cx, ty + 0.058, top, fontsize=10.6, color=color,
                weight="bold", ha="center", va="bottom", zorder=9)
        ax.text(cx, ty + 0.026, title, fontsize=8.8, color=INK,
                ha="center", va="bottom", zorder=9)
        ax.text(cx, ty - 0.048, note, fontsize=7.6, color=MUTED,
                ha="center", va="top", zorder=9, linespacing=1.5)

    # 下方两块
    ax.text(0.042, 0.400, "两代技术在同一张网上的分工", fontsize=8.6,
            color=MUTED, ha="left", va="center")

    halves = [
        ("5G-A：现在就要能用", NAVY, [
            ("京雄快线地下空间", "列车穿隧道时，视频通话、高清直播保持稳定"),
            ("航站楼高峰期", "自动识别聊天、浏览、短视频需求，分配带宽与时延"),
        ]),
        ("6G：把能力先做出来", GOLD, [
            ("技术体系", "通、感、算、智融合，已研制原型样机"),
            ("验证环境", "6G 研发试验装置，开放关键技术验证能力"),
        ]),
    ]
    x = 0.042
    for name, color, items in halves:
        panel(ax, x, 0.180, 0.438, 0.196, color)
        ax.text(x + 0.024, 0.342, name, fontsize=10.2, color=color,
                weight="bold", ha="left", va="center", zorder=9)
        y = 0.296
        for k, v in items:
            ax.text(x + 0.024, y, k, fontsize=7.8, color=INK,
                    weight="bold", ha="left", va="center", zorder=9)
            ax.text(x + 0.024, y - 0.028, v, fontsize=7.4, color=MUTED,
                    ha="left", va="center", zorder=9)
            y -= 0.058
        x += 0.478

    outro(fig, ax, "先进技术不是等出来的，是在用起来的过程中逼出来的。")
    foot(fig, ax, "事实来源：河北日报 2026-11-25（中国雄安官网转载）；经济参考报 2026-11-16")

    fig.savefig(OUT + "图1_两代同框.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(13.6, 8.0))
    ax = new_axes(fig)

    head(fig, ax, "一个隧道场景",
         "地铁里能打电话，背后是三件不同的事",
         "京雄快线地下空间这个案例，把 5G-A 的三种能力同时用上了",
         TEAL)

    cols = [
        ("连接不中断", "覆盖能力", NAVY, [
            ("难点", "隧道内信号无法靠室外基站穿透"),
            ("解法", "沿线路部署室内分布系统与漏缆"),
            ("效果", "列车穿行时视频通话、直播保持稳定"),
            ("属于", "传统通信能力，5G 时代已有，5G-A 做得更稳"),
        ]),
        ("容量够用", "带宽分配", RED, [
            ("难点", "航站楼高峰，几千人同时上网"),
            ("解法", "三载波聚合，把多个频段捆起来用"),
            ("效果", "总容量上去，人均体验不下滑"),
            ("属于", "5G-A 的核心升级之一"),
        ]),
        ("按需分配", "AI 调度", GOLD, [
            ("难点", "聊天要低时延，视频要大带宽，需求不同"),
            ("解法", "自动识别业务类型，按需分配资源"),
            ("效果", "不同应用各得其所，而不是平均分"),
            ("属于", "5G-A 新引入的智能化能力"),
        ]),
    ]

    x = 0.042
    w = 0.288
    gap = 0.019
    for i, (name, tag, color, items) in enumerate(cols):
        panel(ax, x, 0.220, w, 0.510, color)

        ax.text(x + 0.026, 0.690, name, fontsize=13.5, color=color,
                weight="bold", ha="left", va="center", zorder=9)
        ax.text(x + 0.026, 0.654, tag, fontsize=9.2, color=MUTED,
                ha="left", va="center", zorder=9)
        ax.plot([x + 0.026, x + w - 0.026], [0.632, 0.632], color=HAIR,
                linewidth=1.0, zorder=5)

        yy = 0.588
        for k, v in items:
            ax.text(x + 0.026, yy, k, fontsize=7.4, color=MUTED,
                    ha="left", va="center", zorder=9)
            ax.text(x + 0.026, yy - 0.030, v, fontsize=8.2, color=INK,
                    weight="bold" if k != "属于" else "normal",
                    ha="left", va="center", zorder=9)
            yy -= 0.086

        x += w + gap

    outro(fig, ax, "看似一个场景，实际是覆盖、容量、调度三种能力叠出来的。")
    foot(fig, ax, "事实来源：河北日报 2026-11-25；5G-A 三载波聚合、AI 调度为"
         "公开技术口径说明")

    fig.savefig(OUT + "图2_隧道三件事.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(13.6, 8.0))
    ax = new_axes(fig)

    head(fig, ax, "为什么选雄安",
         "新区的好处：没有旧包袱",
         "一张白纸上建网，可以按未来十年的需求来规划",
         GOLD)

    # 左：旧城 vs 新区
    panel(ax, 0.042, 0.380, 0.438, 0.350, MUTED)
    ax.text(0.066, 0.690, "成熟城区建网", fontsize=10.4, color=MUTED,
            weight="bold", ha="left", va="center", zorder=9)
    old = [
        "站址难找，楼顶资源紧张",
        "管线已定型，改动成本高",
        "存量设备多代并存，升级要兼容",
        "频谱与业务已分配完，腾挪空间小",
    ]
    y = 0.636
    for t in old:
        ax.add_patch(Circle((0.074, y), 0.0038, facecolor=MUTED,
                            edgecolor="none", zorder=8))
        ax.text(0.088, y, t, fontsize=8.2, color=INK, ha="left",
                va="center", zorder=9)
        y -= 0.058

    panel(ax, 0.520, 0.380, 0.438, 0.350, GOLD)
    ax.text(0.544, 0.690, "雄安这类新区", fontsize=10.4, color=GOLD,
            weight="bold", ha="left", va="center", zorder=9)
    new = [
        "楼宇、管廊、机房一次性规划",
        "5G-A 可与市政同步建设",
        "6G 试验装置有独立部署空间",
        "新业务没有存量用户负担",
    ]
    y = 0.636
    for t in new:
        ax.add_patch(Circle((0.552, y), 0.0038, facecolor=GOLD,
                            edgecolor="none", zorder=8))
        ax.text(0.566, y, t, fontsize=8.2, color=INK, ha="left",
                va="center", zorder=9)
        y -= 0.058

    # 底部：雄安承担的四件事
    ax.text(0.042, 0.336, "雄安正在承担的四件事", fontsize=8.6, color=MUTED,
            ha="left", va="center")
    ax.plot([0.042, 0.958], [0.316, 0.316], color=HAIR, linewidth=1.0)

    tasks = [
        ("5G-A 规模组网", "率先完成部署"),
        ("6G 技术验证", "不少验证在此开展"),
        ("部省协同试点", "首批核心节点"),
        ("试验装置研制", "开放验证能力"),
    ]
    x = 0.042
    w = 0.222
    gap = 0.017
    for name, note in tasks:
        panel(ax, x, 0.180, w, 0.116, NAVY)
        ax.text(x + 0.020, 0.256, name, fontsize=9.0, color=INK,
                weight="bold", ha="left", va="center", zorder=9)
        ax.text(x + 0.020, 0.220, note, fontsize=7.6, color=MUTED,
                ha="left", va="center", zorder=9)
        x += w + gap

    outro(fig, ax, "试验最怕的不是失败，是环境不干净——新区恰好把干扰项去掉了。")
    foot(fig, ax, "事实来源：河北日报 2026-11-25；成熟城区的约束为一般性工程经验描述")

    fig.savefig(OUT + "图3_为什么是雄安.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)
