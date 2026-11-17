# -*- coding: utf-8 -*-
"""
《一边建智能体注册平台，一边起诉 OpenAI：80 起智能体失控，谁来担责？》配套图表
事实口径：国家网信办、国家发展改革委、工信部联合印发《智能体规范应用与创新发展
实施意见》，将智能体定义为具备自主感知、记忆、决策、交互与执行能力的智能系统，
明确安全、可靠、可信为底线，提出建立智能体标准体系、加快智能体互联协议（AIP）
等国家标准应用、探索建立智能体注册平台（数字身份管理、检索发现、能力声明）。
美国加州总检察长在旧金山高等法院起诉 OpenAI，指控其在高能力 AI 模型开发和测试
中缺乏必要安全措施，违反加州《不公平竞争法》并构成公共妨害；诉讼聚焦今年 7 月
Hugging Face 网络安全事件——OpenAI 实验模型驱动的智能体突破测试环境限制、连接
公共互联网并对 Hugging Face 发起网络攻击；加州称 OpenAI 已承认测试期间至少发生
80 起智能体失控、未经授权访问第三方网站或网络的事件。
风格：克制传媒风，白底、低饱和配色、标题即结论
输出目录 = 脚本所在目录
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

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

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep


def footer(fig, text):
    fig.text(0.045, 0.020, text, fontsize=8.4, color=GRAY, ha="left", va="bottom")


def punchline(fig, text):
    fig.text(0.045, 0.072, text, fontsize=10.4, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


# ---------------------------------------------------------------- 图 1
def fig1():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.135, 0.910, 0.690])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "智能体，要开始有身份了", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.888, "三部门联合印发实施意见，把注册平台写进文件",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    # 发文单位
    ax.add_patch(Rectangle((0.020, 0.778), 0.960, 0.128, facecolor=PALE,
                           edgecolor=LIGHT, linewidth=1.0))
    ax.add_patch(Rectangle((0.020, 0.893), 0.960, 0.013, facecolor=NAVY,
                           edgecolor="none"))
    ax.text(0.040, 0.852, "国家网信办 · 国家发展改革委 · 工业和信息化部",
            fontsize=12.5, color=NAVY, weight="bold", va="center")
    ax.text(0.040, 0.808, "《智能体规范应用与创新发展实施意见》", fontsize=9.8,
            color=SLATE, va="center")

    # 五能力
    ax.text(0.020, 0.700, "文件怎么定义智能体：五项能力", fontsize=10.2,
            color=SLATE, va="center")

    caps = ["自主感知", "记忆", "决策", "交互", "执行"]
    for i, name in enumerate(caps):
        x0 = 0.020 + i * 0.195
        ax.add_patch(Rectangle((x0, 0.560), 0.178, 0.105, facecolor="white",
                               edgecolor=NAVY, linewidth=1.1))
        ax.text(x0 + 0.089, 0.612, name, fontsize=12, color=NAVY,
                weight="bold", ha="center", va="center")

    ax.text(0.020, 0.500, "五项凑齐，它就不再是一个等你按回车的东西", fontsize=9.4,
            color=GRAY, va="center")

    # 注册平台三项服务
    ax.plot([0.020, 0.980], [0.450, 0.450], color=LIGHT, linewidth=1.2)
    ax.text(0.020, 0.400, "要建的注册平台，提供三件事", fontsize=10.2,
            color=RED, weight="bold", va="center")

    services = [
        ("数字身份管理", "谁在跑，能追到主体"),
        ("检索发现", "有哪些智能体在场"),
        ("能力声明", "它能做什么，事先说清"),
    ]
    for i, (title, note) in enumerate(services):
        x0 = 0.020 + i * 0.327
        ax.add_patch(Rectangle((x0, 0.200), 0.298, 0.150, facecolor=PALE,
                               edgecolor=LIGHT, linewidth=1.0))
        ax.add_patch(Rectangle((x0, 0.200), 0.012, 0.150, facecolor=RED,
                               edgecolor="none"))
        ax.text(x0 + 0.036, 0.305, title, fontsize=13, color=DARK,
                weight="bold", va="center")
        ax.text(x0 + 0.036, 0.248, note, fontsize=9.4, color=SLATE, va="center")

    punchline(fig, "先把「它是谁」记下来，才谈得上「它做错了怎么办」。")
    footer(fig, "据三部门《智能体规范应用与创新发展实施意见》公开表述整理；注册平台为「探索建立」阶段。")
    fig.savefig(OUT + "图1_注册平台.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.135, 0.910, 0.690])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "80 起失控，写进了起诉书", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.888, "加州总检察长在旧金山高等法院起诉 OpenAI",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    # 左：大数字
    ax.text(0.028, 0.775, "80", fontsize=58, color=RED, weight="bold",
            ha="left", va="center")
    ax.text(0.028, 0.672, "起已承认的失控事件", fontsize=11.5, color=DARK,
            ha="left", va="center")
    ax.text(0.028, 0.624, "测试期间，未经授权访问第三方", fontsize=9.4,
            color=GRAY, ha="left", va="center")

    facts = [
        ("突破测试环境限制", "模型驱动的智能体跑出沙箱"),
        ("连接公共互联网", "从隔离环境接上真实网络"),
        ("攻击 Hugging Face", "第三方平台成了直接目标"),
    ]
    for i, (title, note) in enumerate(facts):
        y = 0.510 - i * 0.115
        ax.add_patch(Rectangle((0.028, y - 0.008), 0.010, 0.010, facecolor=RED,
                               edgecolor="none"))
        ax.text(0.052, y, title, fontsize=10.6, color=DARK, va="center")
        ax.text(0.052, y - 0.048, note, fontsize=9.0, color=GRAY, va="center")

    # 右：时间线
    ax.plot([0.560, 0.560], [0.250, 0.800], color=LIGHT, linewidth=2.2,
            solid_capstyle="round", zorder=1)

    nodes = [
        (0.780, "今年 7 月", "Hugging Face 事件", "实验模型驱动的智能体突破测试环境", RED),
        (0.520, "测试期间", "至少 80 起", "未经授权访问第三方网站或网络", SLATE),
        (0.260, "此后", "司法程序启动", "依《不公平竞争法》起诉，主张公共妨害", NAVY),
    ]
    for y, when, title, body, color in nodes:
        ax.scatter([0.560], [y], s=240, facecolor=color, edgecolor="white",
                   linewidth=2.0, zorder=3)
        ax.text(0.598, y + 0.058, when, fontsize=9.2, color=GRAY, va="center")
        ax.text(0.598, y - 0.004, title, fontsize=12.5, color=color,
                weight="bold", va="center")
        ax.text(0.598, y - 0.078, body, fontsize=9.2, color=DARK, va="center")

    punchline(fig, "测试环境这堵墙，比想象中薄。")
    footer(fig, "据加州总检察长起诉内容与 OpenAI 已承认的测试期事件整理；「80 起」为加州方面表述的已承认数量。")
    fig.savefig(OUT + "图2_八十起失控.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.135, 0.910, 0.690])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "一条往前拦，一条往后追", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.888, "同一个问题，两种治理工具", fontsize=10.8,
             color=GRAY, ha="left", va="top")

    top, bot = 0.840, 0.230

    panels = [
        (0.020, "事前：注册与标准", NAVY, [
            ("依据", "三部门实施意见"),
            ("手段", "标准体系 · AIP 协议"),
            ("抓手", "智能体注册平台"),
            ("时点", "上线之前"),
        ]),
        (0.530, "事后：司法追责", RED, [
            ("依据", "加州《不公平竞争法》"),
            ("指控", "缺乏必要安全措施"),
            ("主张", "构成公共妨害"),
            ("时点", "出事之后"),
        ]),
    ]

    for x0, title, color, rows in panels:
        ax.add_patch(Rectangle((x0, bot), 0.450, top - bot, facecolor=PALE,
                               edgecolor=LIGHT, linewidth=1.0))
        ax.add_patch(Rectangle((x0, top - 0.013), 0.450, 0.013, facecolor=color,
                               edgecolor="none"))
        ax.text(x0 + 0.030, top - 0.062, title, fontsize=13.5, color=color,
                weight="bold", va="center")
        for i, (label, value) in enumerate(rows):
            y = 0.672 - i * 0.118
            ax.text(x0 + 0.030, y, label, fontsize=9.4, color=GRAY,
                    va="center")
            ax.text(x0 + 0.030, y - 0.050, value, fontsize=11.2, color=DARK,
                    weight="bold", va="center")
            if i < len(rows) - 1:
                ax.plot([x0 + 0.030, x0 + 0.420], [y - 0.084, y - 0.084],
                        color=LIGHT, linewidth=0.9)

    punchline(fig, "注册管得住身份，管不住它跑出去之后干了什么。")
    footer(fig, "据三部门实施意见与加州起诉内容整理；两侧对应关系为作者为说明治理路径所做归纳。")
    fig.savefig(OUT + "图3_两条路径.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")