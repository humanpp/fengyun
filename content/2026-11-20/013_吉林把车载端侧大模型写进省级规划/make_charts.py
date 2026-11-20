# -*- coding: utf-8 -*-
"""
《吉林把"车载端侧大模型"写进省级规划》配套图表
事实口径（均经公开报道交叉核对）：
  · 《吉林省"人工智能+"发展"十五五"规划》由吉林省人民政府办公厅印发，
    发文字号 吉政办发〔2026〕23 号，成文日期 2026-11-12，发布日期 2026-11-19。
    —— 吉林省政府信息公开专栏原文。
  · 汽车方向原文（"培育智能消费新产品"一节）：发展智能网联汽车，支持迭代高阶自动驾驶技术，
    开发智能座舱产品，推进车载端侧大模型部署，支持本地化推理决策与智能服务。
    —— 规划原文，第一财经、界面新闻、观点网 2026-11-19 转述。
  · 2030 年目标："人工智能+"全面深化拓展，新一代智能终端、智能体等应用普及率超 90%。
    —— 规划原文，第一财经 2026-11-19。
  · 规划同时提出：鼓励龙头企业向中小企业开放供应链与创新平台资源；
    引导人工智能领军企业在吉林设立区域总部、研发中心与高端制造基地。
    —— 规划原文，汽车供应商网 2026-11-20 转述。
  · 前置政策：2025-09-16 吉林省《关于加快推进人工智能创新发展的实施意见》提出，
    到 2027 年底全省智能算力规模突破 5000 PFLOPS，形成 10 个左右高质量数据集、
    5 个左右垂直领域大模型，打造 50 个以上高价值示范应用场景，核心产业营业收入达 400 亿元，
    到 2030 年底力争突破 1000 亿元。
    —— 吉林省政府信息公开专栏原文。
  · 行业参照：斑马智能端侧 23B 全模态大模型 AutoOmni 2.0-23B-A3B，端侧推理能力达
    同任务云模型的 80%—100%；英伟达面向车端部署的 Alpamayo 2 Edge 采用约 20 亿参数
    语言模型组件；另有车企在探索自研云端推理芯片，说明算力并非单向全部挪到车端。
    —— InfoQ 2026-09-29、甲子光年 2026-11-16、每日经济新闻 2026-08-17。
说明：素材称"11 月 19 日印发"，经核为 11 月 19 日发布（成文日期 11 月 12 日），图中按"发布"表述。
      素材未提及 2025 年那份实施意见的具体算力与营收目标，本文据原文补入。
风格：克制传媒风，白底、低饱和配色、标题即结论。输出目录 = 脚本所在目录。
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False

NAVY = "#1f3a5f"
RED = "#b5544a"
GRAY = "#8a8f98"
SLATE = "#5f6673"
LIGHT = "#d8dbe0"
DARK = "#2b2f36"
PALE = "#eef0f3"
SAND = "#f7f3ea"
GOLD = "#c9a27a"
GREEN = "#5a7d6f"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep


def base(title, sub):
    fig = plt.figure(figsize=(12, 6.8))
    fig.patch.set_facecolor("white")
    fig.text(0.045, 0.950, title, fontsize=20, color=DARK, weight="bold",
             ha="left", va="top")
    fig.text(0.045, 0.878, sub, fontsize=10.8, color=GRAY, ha="left", va="top")
    return fig


def footer(fig, text):
    fig.text(0.045, 0.014, text, fontsize=8.2, color=GRAY, ha="left", va="center")


def punchline(fig, text, y=0.078):
    fig.text(0.045, y, text, fontsize=10.8, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.6", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


def canvas(fig):
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return ax


# ------------------------------------------------------------------ 图 1
def fig1():
    fig = base("一句话，三条线",
               "规划原文里的汽车方向：智驾、座舱、端侧大模型")
    ax = canvas(fig)

    cards = [
        ("①", "发展智能网联汽车", "支持迭代高阶自动驾驶技术", NAVY),
        ("②", "开发智能座舱产品", "座舱从语音控制走向多模态交互", GOLD),
        ("③", "推进车载端侧大模型部署", "支持本地化推理决策与智能服务", RED),
    ]

    y_top = 0.845
    for i, (num, title, desc, col) in enumerate(cards):
        y = y_top - i * 0.175
        ax.add_patch(FancyBboxPatch((0.070, y - 0.145), 0.860, 0.145,
                                    boxstyle="round,pad=0.008",
                                    facecolor="#fafbfc", edgecolor=col,
                                    linewidth=1.2))
        ax.add_patch(FancyBboxPatch((0.070, y - 0.145), 0.008, 0.145,
                                    boxstyle="square,pad=0",
                                    facecolor=col, edgecolor="none"))
        ax.text(0.100, y - 0.042, num, fontsize=13.0, color=col,
                weight="bold", ha="left", va="center")
        ax.text(0.140, y - 0.042, title, fontsize=12.6, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(0.140, y - 0.104, desc, fontsize=9.4, color=SLATE,
                ha="left", va="center")

    # 底部：目标
    ax.add_patch(FancyBboxPatch((0.070, 0.150), 0.860, 0.110,
                                boxstyle="round,pad=0.010", facecolor=SAND,
                                edgecolor="#d9cdb6", linewidth=1.0))
    ax.text(0.092, 0.222, "到 2030 年", fontsize=9.6, color="#8a7a5e",
            weight="bold", ha="left", va="center")
    ax.text(0.092, 0.180,
            "新一代智能终端、智能体等应用普及率超 90%",
            fontsize=10.4, color=DARK, weight="bold", ha="left", va="center")

    punchline(fig, "第三条是新东西：模型不必都上云，推理可以在车里跑。")
    footer(fig, "事实：吉政办发〔2026〕23 号，成文 2026-11-12、发布 2026-11-19；引文为规划原文｜制图：本文")
    fig.savefig(OUT + "图1_一句话三条线.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("什么留在车里，什么必须上云",
               "端侧前置不等于全部搬到车端")
    ax = canvas(fig)

    # 左：车端
    ax.add_patch(FancyBboxPatch((0.060, 0.310), 0.400, 0.460,
                                boxstyle="round,pad=0.012", facecolor="#eef2f6",
                                edgecolor=NAVY, linewidth=1.3))
    ax.text(0.085, 0.715, "留在车端", fontsize=14.0, color=NAVY, weight="bold",
            ha="left", va="center")
    ax.text(0.085, 0.670, "毫秒级、断网也要能用", fontsize=9.2, color=GRAY,
            ha="left", va="center")
    left_items = [
        "座舱语音与多模态交互",
        "智驾感知与决策",
        "车身与底盘实时控制",
        "数据不出车，隐私风险低",
    ]
    yy = 0.595
    for it in left_items:
        ax.text(0.085, yy, "·  " + it, fontsize=9.6, color=DARK, ha="left",
                va="center")
        yy -= 0.066
    ax.text(0.085, 0.345, "受算力、功耗、成本三重约束", fontsize=9.2,
            color=NAVY, weight="bold", ha="left", va="center")

    # 右：云端
    ax.add_patch(FancyBboxPatch((0.540, 0.310), 0.400, 0.460,
                                boxstyle="round,pad=0.012", facecolor="#f7f3ea",
                                edgecolor=GOLD, linewidth=1.3))
    ax.text(0.565, 0.715, "必须上云", fontsize=14.0, color=GOLD, weight="bold",
            ha="left", va="center")
    ax.text(0.565, 0.670, "重训练、大参数、跨车数据", fontsize=9.2, color=GRAY,
            ha="left", va="center")
    right_items = [
        "基座模型预训练与微调",
        "车队级数据闭环",
        "仿真与场景生成",
        "OTA 版本管理与灰度",
    ]
    yy = 0.595
    for it in right_items:
        ax.text(0.565, yy, "·  " + it, fontsize=9.6, color=DARK, ha="left",
                va="center")
        yy -= 0.066
    ax.text(0.565, 0.345, "单个车端芯片装不下", fontsize=9.2, color=GOLD,
            weight="bold", ha="left", va="center")

    # 中间箭头
    ax.annotate("", xy=(0.535, 0.575), xytext=(0.465, 0.575),
                arrowprops=dict(arrowstyle="-|>", color=NAVY, linewidth=1.8))
    ax.annotate("", xy=(0.465, 0.490), xytext=(0.535, 0.490),
                arrowprops=dict(arrowstyle="-|>", color=GOLD, linewidth=1.8))

    ax.text(0.060, 0.215,
            "行业参照：斑马智能端侧 23B 模型，推理能力达同任务云模型的 80%—100%；",
            fontsize=9.0, color=SLATE, ha="left", va="center")
    ax.text(0.060, 0.172,
            "英伟达车端 Alpamayo 2 Edge 只用约 20 亿参数的语言模型组件。",
            fontsize=9.0, color=SLATE, ha="left", va="center")

    punchline(fig, "“端侧前置”是把该在车里的挪回车里，不是把云拆了。")
    footer(fig, "事实：端侧模型数据据 InfoQ 2026-09-29、甲子光年 2026-11-16；左右分工为本文归纳｜制图：本文")
    fig.savefig(OUT + "图2_端云分工.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("吉林的算力账，早就记过",
               "2025 年的实施意见已定下 2027 与 2030 目标")
    ax = canvas(fig)

    # 左：2027 目标
    ax.add_patch(FancyBboxPatch((0.060, 0.420), 0.400, 0.340,
                                boxstyle="round,pad=0.012", facecolor="#eef2f6",
                                edgecolor=NAVY, linewidth=1.2))
    ax.text(0.085, 0.710, "到 2027 年底", fontsize=12.0, color=NAVY,
            weight="bold", ha="left", va="center")
    rows_2027 = [
        ("智能算力规模", "突破 5000 PFLOPS"),
        ("高质量数据集", "10 个左右"),
        ("垂直领域大模型", "5 个左右"),
        ("示范应用场景", "50 个以上"),
        ("核心产业营收", "400 亿元"),
    ]
    yy = 0.650
    for lab, val in rows_2027:
        ax.text(0.085, yy, lab, fontsize=9.0, color=GRAY, ha="left",
                va="center")
        ax.text(0.245, yy, val, fontsize=9.6, color=DARK, weight="bold",
                ha="left", va="center")
        yy -= 0.048

    # 右：2030 营收目标
    ax.text(0.540, 0.710, "核心产业营业收入", fontsize=10.4, color=DARK,
            weight="bold", ha="left", va="center")

    bars = [
        ("2027", 400, "400 亿元", GOLD),
        ("2030", 1000, "1000 亿元（力争）", RED),
    ]
    x_left = 0.560
    x_scale = 0.00030

    for i, (year, val, label, col) in enumerate(bars):
        y = 0.600 - i * 0.135
        ax.text(x_left - 0.014, y, year, fontsize=9.6, color=DARK,
                ha="right", va="center")
        w = val * x_scale
        ax.add_patch(FancyBboxPatch((x_left, y - 0.030), w, 0.060,
                                    boxstyle="round,pad=0.002",
                                    facecolor=col, edgecolor="none",
                                    alpha=0.92, zorder=3))
        ax.text(x_left + w + 0.014, y, label, fontsize=9.4, color=col,
                weight="bold", ha="left", va="center")

    ax.text(x_left, 0.388, "2030 较 2027 翻 1.5 倍", fontsize=9.6, color=RED,
            weight="bold", ha="left", va="center")

    # 底部：传导链
    ax.add_patch(FancyBboxPatch((0.060, 0.150), 0.880, 0.135,
                                boxstyle="round,pad=0.010", facecolor=SAND,
                                edgecolor="#d9cdb6", linewidth=1.0))
    ax.text(0.082, 0.240, "省级规划不直接给钱，但它决定钱往哪配", fontsize=9.6,
            color="#8a7a5e", weight="bold", ha="left", va="center")
    ax.text(0.082, 0.192,
            "后续可跟踪三件事：是否配套专项资金、一汽系端侧模型的定点节奏、本地零部件能否进入开放供应链名单。",
            fontsize=9.0, color="#7a6746", ha="left", va="center")

    punchline(fig, "端侧大模型写进规划，等于给长春定了一个技术栈锚点。")
    footer(fig, "事实：吉林省《关于加快推进人工智能创新发展的实施意见》2025-09-16；营收目标为该文件原文｜制图：本文")
    fig.savefig(OUT + "图3_吉林的算力账.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)
