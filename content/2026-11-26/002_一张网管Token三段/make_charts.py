# -*- coding: utf-8 -*-
"""
《一张网管 Token 的生产、分发、应用：智能网发布时披露的那套技术栈》配套图表

事实口径（新华网 2026-11-06《聚智成网 创启新章 中国移动智能网正式发布》）：
  · 智能网是与通信网、算力网协同构建的网络化人工智能基础设施，
    充当智能要素的"交换机"和"路由器"；
    打造覆盖 Token 生产、分发、应用的全流程核心能力体系。
  · 生产：芯合异构超融合平台（主流模型在 10 多款主流国产芯片上跨架构迁移
    和部署优化）、OISA（全向智感互联，GPU 卡间互联开放协议）、
    GSE（全调度以太网，机间互联协议）、算网大脑（算网智一体化调度）。
  · 分发：MoMA 模型服务平台与推理算力网络和算力池、AIDN 智能分发网、
    IoA 智能体互联、超级上行、G-SRv6、空芯光纤广域传输。
  · 应用：TraaS 可信服务机制；12580 升级个人智能助理、
    移动天工工业互联网平台焕新、智能体开放服务空间 OAS（四项能力）。
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
TEAL = "#3f6f6b"

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
    """Token 生产四块"""
    fig = plt.figure(figsize=(12, 7.2))
    ax = new_axes(fig)

    header(fig, "生产段：从芯片往上爬的四层",
           "顺序不能颠倒——先单机内适配，再卡间、机间，最后全局调度")

    rows = [
        ("① 芯合异构超融合平台", "屏蔽底层异构硬件差异",
         "主流模型在 10 多款主流国产芯片上跨架构迁移与部署优化", NAVY),
        ("② OISA 全向智感互联", "GPU 卡间互联开放协议",
         "把多张卡连成统一编址的域，推动智算产业向超节点演进", NAVY),
        ("③ GSE 全调度以太网", "机间互联协议",
         "卡连好之后机器之间还要连好，否则集群扩大后通信吃掉新增算力", TEAL),
        ("④ 算网大脑", "全局调度",
         "支持算、网、智一体化调度", RED),
    ]

    y = 0.620
    for name, role, why, color in rows:
        card(ax, 0.048, y - 0.058, 0.904, 0.104, color, lw=1.2)
        ax.text(0.070, y + 0.014, name, fontsize=9.8, color=DARK,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(0.070, y - 0.030, why, fontsize=8.4, color=SLATE,
                ha="left", va="center", zorder=6)
        ax.text(0.560, y - 0.030, role, fontsize=8.4, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        y -= 0.128

    ax.text(0.048, 0.130,
            "注意「10 多款」这个数：没有这一层，模型厂商的适配成本会随芯片型号数量线性上升。",
            fontsize=9.2, color=DARK, ha="left", va="center")

    punchline(fig, "平台的价值，是把适配成本那条曲线压平。")
    footer(fig, "事实来源：新华网 2026-11-06《聚智成网 创启新章 中国移动智能网正式发布》")
    fig.savefig(OUT + "图1_Token生产四块.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """Token 分发四层"""
    fig = plt.figure(figsize=(12, 7.2))
    ax = new_axes(fig)

    header(fig, "分发段：从平台到传输底层",
           "分发对象从「模型」扩展到「智能体」")

    items = [
        ("平台", "MoMA + 推理算力网络与算力池", "考核的是单位算卡产出，不是规模", NAVY, 0.048),
        ("网络", "AIDN 智能分发网 + IoA 智能体互联", "一个送模型与数据，一个送智能体", TEAL, 0.372),
        ("接入", "超级上行无线接入", "传统网络为下行设计，AI 交互要上行", SLATE, 0.048),
        ("传输", "G-SRv6 + 空芯光纤广域传输", "提升网络确定性，支撑多智能体与具身智能", RED, 0.372),
    ]

    coords = [(0.048, 0.520), (0.512, 0.520), (0.048, 0.290), (0.512, 0.290)]
    for (name, what, why, color, _), (x, y) in zip(items, coords):
        card(ax, x, y, 0.440, 0.170, color, lw=1.3)
        ax.text(x + 0.020, y + 0.124, name, fontsize=10.6, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(x + 0.020, y + 0.078, what, fontsize=8.8, color=DARK,
                ha="left", va="center", zorder=6)
        ax.text(x + 0.020, y + 0.032, why, fontsize=8.2, color=SLATE,
                ha="left", va="center", zorder=6)

    ax.text(0.048, 0.250,
            "「网络确定性」在这段出现了——多智能体协同要求时延可预期，具身智能更是等不起抖动。",
            fontsize=9.2, color=SLATE, ha="left", va="center")

    card(ax, 0.048, 0.128, 0.904, 0.066, NAVY, face=PALE, lw=1.2)
    ax.text(0.070, 0.161,
            "从「送模型」到「送智能体」，分发对象的性质变了，对网络的要求也跟着变。",
            fontsize=9.2, color=DARK, ha="left", va="center", zorder=6)

    punchline(fig, "分发段几乎全是通信网的家底。")
    footer(fig, "事实来源：新华网 2026-11-06（MoMA、推理算力网络与算力池、AIDN、IoA、"
                "超级上行、G-SRv6、空芯光纤）")
    fig.savefig(OUT + "图2_Token分发四层.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """应用三段产品"""
    fig = plt.figure(figsize=(12, 7.2))
    ax = new_axes(fig)

    header(fig, "应用段：一个机制，三个产品",
           "TraaS 管可信，产品面向三类对象")

    card(ax, 0.048, 0.560, 0.904, 0.150, RED, lw=1.5)
    ax.text(0.070, 0.664, "TraaS　Trust as a service", fontsize=12.0,
            color=RED, weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.070, 0.612, "可信服务机制：以安全可信，构建开放生态",
            fontsize=9.0, color=DARK, ha="left", va="center", zorder=6)
    ax.text(0.070, 0.580, "应用段公开的机制只有这一个", fontsize=8.4,
            color=GRAY, ha="left", va="center", zorder=6)

    prods = [
        ("12580", "公众客户", "升级为个人智能助理\n增强智能体框架\n电话 + APP 双入口", NAVY),
        ("移动天工", "政企客户", "工业互联网平台焕新\n增强工业制造与供应链知识\n端到端任务能力", TEAL),
        ("OAS", "合作伙伴", "智能体开放服务空间\n四项服务能力\n一站式工作园区", SLATE),
    ]
    x = 0.048
    w = 0.282
    gap = 0.024
    for name, who, desc, color in prods:
        card(ax, x, 0.290, w, 0.230, color, lw=1.3)
        ax.text(x + w / 2, 0.478, name, fontsize=12.4, color=color,
                weight="bold", ha="center", va="center", zorder=6)
        ax.text(x + w / 2, 0.436, who, fontsize=9.0, color=DARK,
                ha="center", va="center", zorder=6)
        ax.plot([x + 0.028, x + w - 0.028], [0.412, 0.412], color=LIGHT,
                linewidth=1.0, zorder=6)
        ax.text(x + w / 2, 0.348, desc, fontsize=8.2, color=SLATE,
                ha="center", va="center", zorder=6, linespacing=1.8)
        x += w + gap

    ax.text(0.048, 0.232, "OAS 的四项能力里，两项属于可信、两项属于能力：",
            fontsize=9.2, color=DARK, ha="left", va="center")
    caps = ["可信身份认证", "安全运行环境", "原生网络能力", "长期记忆框架"]
    x = 0.048
    for c in caps:
        w2 = 0.212
        card(ax, x, 0.166, w2, 0.042, GRAY, face=PALE, lw=0.9)
        ax.text(x + w2 / 2, 0.187, c, fontsize=8.4, color=DARK,
                ha="center", va="center", zorder=6)
        x += w2 + 0.020

    punchline(fig, "这个组合说明 OAS 想同时解决「敢不敢用」和「能不能用」。")
    footer(fig, "事实来源：新华网 2026-11-06（TraaS、12580、移动天工、OAS 四项服务能力）")
    fig.savefig(OUT + "图3_应用三段产品.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)
