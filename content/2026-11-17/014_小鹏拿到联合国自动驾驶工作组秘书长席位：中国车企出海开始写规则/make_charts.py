# -*- coding: utf-8 -*-
"""
《小鹏拿到联合国自动驾驶工作组秘书长席位：中国车企出海，不只卖车，开始写规则》配套图表
事实口径：小鹏集团近日当选联合国欧洲经济委员会（UNECE）自动驾驶工作组（GRVA）
新设"自动驾驶场景相关信息交换工作组"（TF-ESRI）秘书长，成为首家在联合国自动
驾驶法规核心框架下担任相关工作组秘书长的中国企业；小鹏通过麦格纳斯泰尔在奥地利
格拉茨的柔性生产线以委托生产模式进行 G6、G9 本地化生产，计划 2027 年起逐步向
全球客户交付 NGP。另一条规则线：中国—东盟自贸区 3.0 版升级议定书确认 2026 年
12 月 1 日正式生效，双方将在绿色经济框架下推动新能源汽车、光伏等重点领域合作，
绿色贸易等 8 大优先领域贯穿研发、融资、生产、消费、回收全链条，并与中泰备忘录衔接。
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

    fig.text(0.045, 0.955, "同一时间，三条线一起动", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.888, "规则、产能、市场，三件事不是各自为战",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    cards = [
        (0.020, NAVY, "规则", "UNECE · GRVA",
         ["TF-ESRI 工作组秘书长", "首家中国企业", "自动驾驶场景信息交换"]),
        (0.345, SLATE, "产能", "奥地利 · 格拉茨",
         ["麦格纳斯泰尔柔性线", "委托生产 G6、G9", "不用自建工厂"]),
        (0.670, RED, "市场", "中国—东盟 3.0",
         ["2026 年 12 月 1 日生效", "新能源汽车、光伏", "8 大优先领域全链条"]),
    ]

    for x0, color, tag, sub, rows in cards:
        ax.add_patch(Rectangle((x0, 0.260), 0.310, 0.520, facecolor=PALE,
                               edgecolor=LIGHT, linewidth=1.0))
        ax.add_patch(Rectangle((x0, 0.767), 0.310, 0.013, facecolor=color,
                               edgecolor="none"))
        ax.text(x0 + 0.026, 0.715, tag, fontsize=15, color=color,
                weight="bold", va="center")
        ax.text(x0 + 0.026, 0.660, sub, fontsize=9.2, color=GRAY, va="center")
        ax.plot([x0 + 0.026, x0 + 0.284], [0.618, 0.618], color=LIGHT,
                linewidth=1.0)
        for i, line in enumerate(rows):
            ax.text(x0 + 0.026, 0.560 - i * 0.085, line, fontsize=9.8,
                    color=DARK, va="center")

    ax.text(0.020, 0.185, "规则决定准入成本，产能决定响应速度，市场决定规模上限",
            fontsize=10.2, color=DARK, va="center")

    punchline(fig, "这三件事拼起来，才是「出海」和「卖车」的区别。")
    footer(fig, "据 UNECE 任命、奥地利委托生产安排与中国—东盟自贸区 3.0 生效时间公开口径整理。")
    fig.savefig(OUT + "图1_三条线.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.135, 0.910, 0.690])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "写规则，省的是兼容成本", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.888, "同样一套高阶智驾，两种进入海外市场的方式",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    top, bot = 0.760, 0.360

    # 左：被动适配
    ax.add_patch(Rectangle((0.020, bot), 0.450, top - bot, facecolor=PALE,
                           edgecolor=LIGHT, linewidth=1.0))
    ax.add_patch(Rectangle((0.020, top - 0.013), 0.450, 0.013, facecolor=SLATE,
                           edgecolor="none"))
    ax.text(0.048, top - 0.062, "被动适配", fontsize=13, color=SLATE,
            weight="bold", va="center")
    ax.text(0.048, top - 0.108, "每进一个市场，重做一遍", fontsize=9.4,
            color=GRAY, va="center")
    left = ["按当地法规重做验证", "场景、数据、测试逐项对表", "每家车企各付一次"]
    for i, line in enumerate(left):
        ax.text(0.048, 0.585 - i * 0.075, line, fontsize=10.2, color=DARK,
                va="center")

    # 右：参与制定
    ax.add_patch(Rectangle((0.530, bot), 0.450, top - bot, facecolor=PALE,
                           edgecolor=LIGHT, linewidth=1.0))
    ax.add_patch(Rectangle((0.530, top - 0.013), 0.450, 0.013, facecolor=NAVY,
                           edgecolor="none"))
    ax.text(0.558, top - 0.062, "参与制定", fontsize=13, color=NAVY,
            weight="bold", va="center")
    ax.text(0.558, top - 0.108, "在框架层面推动", fontsize=9.4, color=GRAY,
            va="center")
    right = ["场景信息如何交换、比对", "一次投入，多处复用", "全行业按同一套来"]
    for i, line in enumerate(right):
        ax.text(0.558, 0.585 - i * 0.075, line, fontsize=10.2, color=DARK,
                va="center")

    # 中间箭头
    ax.annotate("", xy=(0.512, 0.560), xytext=(0.478, 0.560),
                arrowprops=dict(arrowstyle="-|>", color=GRAY, linewidth=1.6,
                                shrinkA=0, shrinkB=0))

    # 底部结论条
    ax.add_patch(Rectangle((0.020, 0.180), 0.960, 0.085, facecolor="white",
                           edgecolor=NAVY, linewidth=1.2))
    ax.text(0.500, 0.222, "TF-ESRI 管的就是「场景信息怎么交换」——这正是每家车企都要重复付的那笔钱",
            fontsize=10.0, color=NAVY, ha="center", va="center")

    punchline(fig, "改产品是一次性的，改标准是所有人的。")
    footer(fig, "TF-ESRI 全称「自动驾驶场景相关信息交换工作组」；两种路径的对比为作者据工作组职能所作的归纳。")
    fig.savefig(OUT + "图2_两种进入方式.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.135, 0.910, 0.690])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "出海的三个台阶", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.888, "从把车卖过去，到把规则和产能一起带过去",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    stages = [
        (0.020, "阶段一", "产品出口", ["整车运过去卖", "关税与认证由对方定", "价格战是主要手段"], SLATE),
        (0.365, "阶段二", "本地组装", ["建厂或找代工", "换取配额与关税优惠", "重资产，回本周期长"], SLATE),
        (0.710, "阶段三", "规则 + 轻资产", ["参与法规框架制定", "借用现有闲置产线", "技术、品牌、服务同步"], RED),
    ]

    for x0, tag, title, rows, color in stages:
        ax.add_patch(Rectangle((x0, 0.380), 0.270, 0.310, facecolor=PALE,
                               edgecolor=LIGHT, linewidth=1.0))
        ax.add_patch(Rectangle((x0, 0.677), 0.270, 0.013, facecolor=color,
                               edgecolor="none"))
        ax.text(x0 + 0.024, 0.652, tag, fontsize=9.2, color=GRAY, va="center")
        ax.text(x0 + 0.024, 0.600, title, fontsize=13.2, color=color,
                weight="bold", va="center")
        for i, line in enumerate(rows):
            ax.text(x0 + 0.024, 0.525 - i * 0.057, line, fontsize=9.0,
                    color=DARK, va="center")

    for x in (0.294, 0.639):
        ax.annotate("", xy=(x + 0.066, 0.535), xytext=(x + 0.004, 0.535),
                    arrowprops=dict(arrowstyle="-|>", color=GRAY, linewidth=1.6,
                                    shrinkA=0, shrinkB=0))

    ax.plot([0.020, 0.980], [0.320, 0.320], color=LIGHT, linewidth=1.1)
    ax.text(0.020, 0.255, "越往后，输出的东西越不是「一辆车」，而是一套能落地的能力",
            fontsize=10.0, color=DARK, va="center")
    ax.text(0.020, 0.200, "第三阶段才刚开头：2027 年起，NGP 计划逐步向全球客户交付",
            fontsize=9.4, color=GRAY, va="center")

    punchline(fig, "卖车赚的是一次差价，写规则收的是长期过路费。")
    footer(fig, "三阶段划分为作者为说明演进路径所作归纳，非行业标准表述；NGP 全球交付为计划安排。")
    fig.savefig(OUT + "图3_三个台阶.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")