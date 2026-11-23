# -*- coding: utf-8 -*-
"""
《AI 代理帮你比价，谁来为它的选择负责》配套图表

事实口径：
  · 2026-11-21，澳大利亚助理部长（生产力、竞争、慈善与财政部）Andrew Leigh
    在堪培拉对记者表示，政府正在做大量工作确保竞争法在 AI 时代跟上；随着更多
    消费者用个人 AI 代理购物，相关法律是否需要更新正在研究；"监控定价"
    （surveillance pricing）同样在审查之列；尚未公布具体方案。
  · 2026-06-17 Leigh 在澳大利亚经济学会（NSW）"The Invisible Mind"会议演讲，
    提出"隐形代理"概念，列出四类代理不当行为：隐藏引导（hidden steering）、
    个性化榨取（personalised extraction，"从'价格是多少'到'我的价格是多少'"）、
    代理互斗（agent gaming）、机器合谋（machine coordination），并提出四项测试：
    忠诚、可竞争、可验证、可归责。
  · 同一演讲引用：2024 年加拿大航空因聊天机器人提供错误的丧亲票价信息被判赔，
    其"聊天机器人是独立法律实体"的抗辩被法庭驳回。
  · Treasury《Review of AI and the Australian Consumer Law》（2025）结论：
    ACL 大体能应对 AI 相关损害，包括代理系统；执法挑战在于观察。
  · 2025-12 ACCC 发布 AI 行业快照；2026-10-16 参议院联合委员会听证提到
    监控定价、串联的机器人等风险。
  · 对照：中国工信部办公厅《关于加强智能体终端设备进网管理的通知》
    （成文 2026-10-24，发布 2026-11-06）。

输出目录 = 脚本所在目录
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei"]
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
Y_PUNCH = 0.068
Y_FOOT = 0.020


def header(fig, title, sub):
    fig.text(0.045, Y_TITLE, title, fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, Y_SUB, sub, fontsize=10.4, color=GRAY,
             ha="left", va="top")


def footer(fig, text):
    fig.text(0.045, Y_FOOT, text, fontsize=7.6, color=GRAY,
             ha="left", va="bottom")


def punchline(fig, text):
    fig.text(0.045, Y_PUNCH, text, fontsize=10.4, color=DARK,
             ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


def card(ax, x, y, w, h, edge, face="white", lw=1.2, z=2):
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
    """一年时间线"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "澳大利亚这条线，走了将近一年",
           "从监管机构发快照，到部长表态要改法")

    ax.add_patch(FancyArrowPatch((0.070, 0.610), (0.945, 0.610),
                                 arrowstyle="-|>", mutation_scale=18,
                                 color=LIGHT, lw=2.0))

    nodes = [
        (0.110, "2025.12", "ACCC 发布 AI\n行业快照", GRAY),
        (0.330, "2026.06.17", "部长演讲：\n四类代理不当行为", SLATE),
        (0.550, "2026.09.11", "ACCC 向议会\n联合委员会提交意见", SLATE),
        (0.765, "2026.10.16", "参议院听证：\n监控定价、串联机器人", SLATE),
        (0.915, "2026.11.21", "部长：竞争法\n要跟上 AI 时代", RED),
    ]
    for x, title, note, color in nodes:
        ax.plot([x], [0.610], "o", markersize=9, color=color,
                markeredgecolor="white", markeredgewidth=1.2, zorder=6)
        ax.text(x, 0.652, title, fontsize=10.0, color=DARK,
                weight="bold", ha="center", va="bottom")
        ax.text(x, 0.572, note, fontsize=8.6, color=SLATE,
                ha="center", va="top", linespacing=1.7)

    card(ax, 0.045, 0.300, 0.910, 0.190, NAVY, lw=1.4)
    ax.text(0.070, 0.445, "现在到哪一步", fontsize=10.6, color=NAVY,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.070, 0.400,
            "11 月 21 日的表态只到“正在研究、确保法律跟上”，没有草案、没有时间表。\n"
            "按程序，接下来要看财政部或竞争监管机构是否发布征求意见稿。",
            fontsize=9.4, color=SLATE, ha="left", va="top",
            linespacing=1.9, zorder=6)

    punchline(fig, "法律还没改，先把问题说清楚了。")
    footer(fig, "事实来源：ACCC 2025-12-16；Treasury 部长演讲 2026-06-17；ACCC 提交意见 2026-09-11；"
                "彭博社/海峡时报 2026-11-21")
    fig.savefig(OUT + "图1_时间线.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """四种代理行为"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "四种“看不见”的做法",
           "都不是新罪名，是旧问题换了执行者")

    items = [
        ("隐藏引导", "推荐里藏了返点。它排前面\n不是因为好，是因为结账更顺。", "误导性陈述"),
        ("个性化榨取", "从“价格是多少”变成\n“我的价格是多少”。", "不公平交易行为"),
        ("代理互斗", "卖方代理研究买方代理的偏好，\n改写商品页去迎合它。", "误导 / 虚假评价"),
        ("机器合谋", "两个定价代理从同一批数据里\n学会“别打价格战”。", "反竞争协议"),
    ]
    y = 0.680
    for name, note, tool in items:
        card(ax, 0.045, y, 0.620, 0.115, LIGHT, lw=1.1)
        ax.text(0.068, y + 0.082, name, fontsize=10.6, color=DARK,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(0.240, y + 0.078, note, fontsize=8.8, color=SLATE,
                ha="left", va="top", linespacing=1.7, zorder=6)
        card(ax, 0.690, y + 0.032, 0.265, 0.052, NAVY, face=PALE, lw=1.0)
        ax.text(0.8225, y + 0.058, tool, fontsize=8.8, color=NAVY,
                ha="center", va="center", zorder=8)
        y -= 0.135

    ax.text(0.045, 0.170,
            "右侧是澳大利亚现行法里已经能用的工具，不是新立法。",
            fontsize=9.2, color=GRAY, ha="left", va="center")

    punchline(fig, "手段没变，执行者从人换成了代理。")
    footer(fig, "事实来源：Treasury 部长 2026-06-17 演讲（四类行为）；Treasury《Review of AI and the "
                "Australian Consumer Law》2025（现行法适用性）")
    fig.savefig(OUT + "图2_四种做法.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """监管要变成机器购物者"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "监管得学会当“机器购物者”",
           "个性化之后，同样的商品在不同人那里价格不同，旧办法查不出来")

    card(ax, 0.045, 0.560, 0.290, 0.220, SLATE, lw=1.3)
    ax.text(0.068, 0.735, "旧办法", fontsize=10.4, color=SLATE,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.068, 0.690,
            "比对公开价目、\n查合同条款、\n调阅文件",
            fontsize=9.4, color=SLATE, ha="left", va="top",
            linespacing=1.95, zorder=6)

    card(ax, 0.375, 0.560, 0.290, 0.220, NAVY, lw=1.3)
    ax.text(0.398, 0.735, "现在的做法", fontsize=10.4, color=NAVY,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.398, 0.690,
            "用合成消费者做受控实验：\n同一时间、同一商品，\n只改变买家特征",
            fontsize=9.4, color=SLATE, ha="left", va="top",
            linespacing=1.95, zorder=6)

    card(ax, 0.705, 0.560, 0.250, 0.220, RED, lw=1.3)
    ax.text(0.728, 0.735, "要建的能力", fontsize=10.4, color=RED,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.728, 0.690,
            "审计留痕：指令、\n数据输入、模型变更、\n定价结果",
            fontsize=9.4, color=SLATE, ha="left", va="top",
            linespacing=1.95, zorder=6)

    ax.add_patch(FancyArrowPatch((0.340, 0.670), (0.370, 0.670),
                                 arrowstyle="-|>", mutation_scale=14,
                                 color=GRAY, lw=1.4))
    ax.add_patch(FancyArrowPatch((0.670, 0.670), (0.700, 0.670),
                                 arrowstyle="-|>", mutation_scale=14,
                                 color=GRAY, lw=1.4))

    card(ax, 0.045, 0.255, 0.910, 0.215, TEAL, lw=1.4)
    ax.text(0.070, 0.430, "一条现成的判例", fontsize=10.4, color=TEAL,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.070, 0.385,
            "2024 年，加拿大航空因聊天机器人给出错误的丧亲票价信息被判赔。它辩称聊天机器人是"
            "“独立法律实体”，\n被法庭驳回。对代理同样适用：企业应为它部署的系统负责。",
            fontsize=9.2, color=SLATE, ha="left", va="top",
            linespacing=1.95, zorder=6)

    punchline(fig, "归责不难，难的是先看见它做了什么。")
    footer(fig, "事实来源：Treasury 部长 2026-06-17 演讲（合成消费者、审计留痕、加航判例）")
    fig.savefig(OUT + "图3_机器购物者.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)