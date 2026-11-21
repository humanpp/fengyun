# -*- coding: utf-8 -*-
"""
《智能服务不只是「技术能力」，更要看「产业价值」：三张网各管一段路由》配套图表

事实口径（核到新华网 2026-11-06 刊发的主旨演讲全文）：

一、演讲第三张网的总判断
  · 从模型到智能体、从知识生成到任务执行、从单点智能到规模应用，
    智能服务不只是「技术能力」，更要看「产业价值」。
  · 智能是中国移动高质量发展的坚定方向。致力于打造智能服务的
    「交换机」「路由器」，依托通信基础和算力资源，协同建设网络化智能基础设施，
    创新构建智能互联网，实现模型、数据、智能体的安全可信供给、泛在高效互联，
    支撑从场景到平台、从终端到云端、从应用到模型的全链条智能服务。

二、做大产业价值的三个关键词
  · 需要更加注重连接、协同、普惠，让更多人用得上、用得起、用得好。
  · 依托 MoMA 模型服务平台，全量接入主流模型，降低 Token 成本、提升使用效能，
    帮客户选择最匹配的模型、让客户享用高可信的服务。
  · 构建「移动智能」服务矩阵：推出 MobileWork 智能体赋能工作提效；
    推动咪咕平台升级，做优体育视频、国风音乐、书香阅读体验；
    建强「移动天工」平台，协同行业伙伴加强客户现场洞察，
    推动数智赋能与场景适配，打造更多先进制造标杆应用。
  · 持续做强泛全联盟，共同推动终端功能提升、通信能力升级，
    打造 AI 定制终端，实现端网业高效协同。

三、三张网的路由分工（本篇用作框架，出自同一篇演讲）
  · 通信网贯通流量路由，连接平台与终端，让字节高效传递；
  · 算力网贯通模型路由，连接算力与数据，让词元高效流动；
  · 智能网贯通任务路由，连接模型与场景，让意图高效执行。

风格：克制传媒风，白底、低饱和配色、标题即结论
输出目录 = 脚本所在目录
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

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

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep

Y_TITLE = 0.958
Y_SUB = 0.898
Y_PUNCH = 0.070
Y_FOOT = 0.020

Q_L = "\u300c"
Q_R = "\u300d"


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
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "三张网，各管一段路由",
           "字节、词元、意图，是三种不同的「送达到位」")

    cols = [
        ("通信网", "流量路由", "让字节高效传递", "连接平台与终端", NAVY),
        ("算力网", "模型路由", "让词元高效流动", "连接算力与数据", TEAL),
        ("智能网", "任务路由", "让意图高效执行", "连接模型与场景", RED),
    ]

    w = 0.286
    gap = 0.028
    x = 0.045
    for name, routing, outcome, link, color in cols:
        card(ax, x, 0.372, w, 0.352, color, lw=1.5)
        ax.text(x + 0.024, 0.678, name, fontsize=15.0, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(x + 0.024, 0.634, routing, fontsize=10.4, color=DARK,
                ha="left", va="center", zorder=6)
        ax.plot([x + 0.024, x + w - 0.024], [0.610, 0.610], color=color,
                linewidth=0.9, alpha=0.35, zorder=5)
        ax.text(x + 0.024, 0.578, outcome, fontsize=10.6, color=color,
                weight="bold", ha="left", va="top", zorder=6)
        ax.text(x + 0.024, 0.502, link, fontsize=8.8, color=SLATE,
                ha="left", va="top", zorder=6)
        x += w + gap

    ax.text(0.045, 0.300,
            "越往下，要「送达到位」的东西越抽象：字节有地址，词元有上下文，"
            "意图只有一句话。",
            fontsize=9.4, color=SLATE, ha="left", va="center")

    ax.text(0.045, 0.238,
            "演讲的定位：打造智能服务的" + Q_L + "交换机" + Q_R + Q_L + "路由器" + Q_R +
            "。",
            fontsize=9.4, color=DARK, ha="left", va="center")

    punchline(fig, "第三张网要交付的，不是算力也不是带宽，是「事情办成了」。")
    footer(fig, "事实来源：新华网 2026-11-06《中国移动董事长陈忠岳：网络强基 智能共创》")
    fig.savefig(OUT + "图1_三段路由.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "一句话，拆成三层不同的资产",
           "从模型到智能体、从知识生成到任务执行、从单点智能到规模应用")

    rows = [
        ("模型", "智能体",
         "模型给的是答案，智能体给的是结果\n要能调用工具、承担多步任务"),
        ("知识生成", "任务执行",
         "会写与会做之间，差一整条执行链\n出错时能否回滚、能否追责"),
        ("单点智能", "规模应用",
         "一个场景跑通不等于能复制到一千个\n要靠平台与联盟承接长尾"),
    ]

    top = 0.700
    for i, (left, right, note) in enumerate(rows):
        y = top - i * 0.200

        card(ax, 0.045, y - 0.062, 0.150, 0.098, GRAY, face=PALE, lw=1.0)
        ax.text(0.120, y - 0.013, left, fontsize=11.8, color=SLATE,
                ha="center", va="center", zorder=6)

        ax.annotate("", xy=(0.245, y - 0.013), xytext=(0.208, y - 0.013),
                    arrowprops=dict(arrowstyle="-|>", color=RED,
                                    linewidth=1.6, shrinkA=0, shrinkB=0))

        card(ax, 0.255, y - 0.062, 0.158, 0.098, RED, lw=1.6)
        ax.text(0.334, y - 0.013, right, fontsize=11.8, color=RED,
                weight="bold", ha="center", va="center", zorder=6)

        ax.text(0.446, y + 0.028, note, fontsize=8.9, color=SLATE,
                ha="left", va="top", linespacing=1.62, zorder=6)

    ax.text(0.045, 0.156,
            "演讲原话：智能服务不只是" + Q_L + "技术能力" + Q_R +
            "，更要看" + Q_L + "产业价值" + Q_R + "。",
            fontsize=9.6, color=DARK, ha="left", va="center")

    punchline(fig, "能力回答「能不能」，产业价值回答「值不值」。")
    footer(fig, "事实来源：新华网 2026-11-06《中国移动董事长陈忠岳：网络强基 智能共创》")
    fig.savefig(OUT + "图2_三个转变.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(12, 7.1))
    ax = new_axes(fig)

    header(fig, "服务矩阵的四块拼图，对着四类人",
           "工作提效、数智生活、行业现场、终端入口，各有各的产品线")

    tiles = [
        ("MobileWork 智能体", "对着要提效的人", "赋能工作提效", RED),
        ("咪咕平台升级", "对着要体验的人", "体育视频、国风音乐、书香阅读", TEAL),
        ("移动天工平台", "对着行业现场", "客户现场洞察、先进制造标杆应用", NAVY),
        ("泛全联盟与 AI 定制终端", "对着终端入口", "终端功能提升、通信能力升级、端网业协同", SLATE),
    ]

    x = 0.045
    y = 0.562
    w = 0.443
    h = 0.200
    for i, (name, who, detail, color) in enumerate(tiles):
        col = i % 2
        row = i // 2
        cx = x + col * (w + 0.022)
        cy = y - row * (h + 0.028)

        card(ax, cx, cy, w, h, color, lw=1.4)
        ax.text(cx + 0.022, cy + h - 0.046, name, fontsize=12.2, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(cx + 0.022, cy + h - 0.086, who, fontsize=9.0, color=GRAY,
                ha="left", va="center", zorder=6)
        ax.plot([cx + 0.022, cx + w - 0.022], [cy + h - 0.108] * 2,
                color=color, linewidth=0.9, alpha=0.35, zorder=5)
        ax.text(cx + 0.022, cy + h - 0.134, detail, fontsize=8.8, color=DARK,
                ha="left", va="top", zorder=6)

    # 底部：MoMA
    card(ax, 0.045, 0.200, 0.908, 0.100, NAVY, face=PALE, lw=1.2)
    ax.text(0.068, 0.268, "底座：MoMA 模型服务平台", fontsize=11.4, color=NAVY,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.068, 0.228,
            "全量接入主流模型，降低 Token 成本、提升使用效能，"
            "帮客户选择最匹配的模型。",
            fontsize=9.0, color=SLATE, ha="left", va="center", zorder=6)

    punchline(fig, "四个产品线之上，还压着一个「帮你挑模型」的中间层。")
    footer(fig, "事实来源：新华网 2026-11-06《中国移动董事长陈忠岳：网络强基 智能共创》")
    fig.savefig(OUT + "图3_四块拼图.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)
