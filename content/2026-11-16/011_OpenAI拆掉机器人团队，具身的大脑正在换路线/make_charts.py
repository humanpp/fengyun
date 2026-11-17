# -*- coding: utf-8 -*-
"""
《OpenAI 拆掉机器人团队，华为云把世界模型焊在自家芯片上》配套图表
事实来源：《财富》2026-11-13 报道及 OpenAI 11-14 确认；华为云 2026-11-16 发布会
风格：克制传媒风，白底、低饱和配色、标题即结论
输出目录 = 脚本所在目录
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["figure.facecolor"] = "white"
plt.rcParams["axes.facecolor"] = "white"

NAVY = "#1f3a5f"
RED = "#b5544a"
GRAY = "#8a8f98"
LIGHT = "#d8dbe0"
DARK = "#2b2f36"
PALE = "#eef0f3"
SAND = "#b9a887"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep


def canvas(fig):
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return ax


def footer(fig, text):
    fig.text(0.045, 0.035, text, fontsize=8.4, color=GRAY, ha="left", va="bottom")


def takeaway(fig, y, text, size=10.4):
    fig.text(0.045, y, text, fontsize=size, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


def head(fig, title, sub):
    fig.text(0.045, 0.935, title, fontsize=19, color=DARK, ha="left",
             va="center", weight="bold")
    fig.text(0.045, 0.868, sub, fontsize=10.8, color=GRAY, ha="left", va="center")


# ---------------------------------------------------------------- 图 1
def fig1():
    fig = plt.figure(figsize=(12, 6.8))
    ax = canvas(fig)
    head(fig, "相隔三天，两个方向",
         "11 月 13—14 日 OpenAI 撤团队；11 月 16 日华为云发世界模型")

    cols = [
        (0.055, "OpenAI", "11.13 — 11.14", NAVY, [
            ("撤销独立机器人团队", "第二次撤掉这支队伍，不是退出机器人"),
            ("人员去向", "研究 → Mark Chen；应用与硬件 → Greg Brockman"),
            ("依据", "Astra 在仿真基准上 74.8%，专用模型 51.0%"),
            ("口径", "2027 年首次公开演示人形机器人的目标不变"),
        ]),
        (0.530, "华为云", "11.16", RED, [
            ("发布并开源 CloudRobo-WM1.2", "首款昇腾原生具身世界模型"),
            ("技术路线", "原生一体化，不做“世界模型 + 动作模块”拼接"),
            ("同日披露 openPangu-2.1-Pro", "优化鸿蒙 ArkTS 代码生成与昇腾算子"),
            ("落地", "联合福龙马，新一代智能清扫机器人启动预售"),
        ]),
    ]
    for x, name, date, color, items in cols:
        ax.add_patch(Rectangle((x, 0.300), 0.415, 0.470, facecolor="#fafafb",
                               edgecolor=LIGHT, linewidth=1.0))
        ax.add_patch(Rectangle((x, 0.760), 0.415, 0.010, facecolor=color,
                               edgecolor="none"))
        ax.text(x + 0.025, 0.700, name, fontsize=15, color=color,
                weight="bold", va="center")
        ax.text(x + 0.025, 0.650, date, fontsize=9.6, color=GRAY, va="center")
        ax.plot([x + 0.025, x + 0.390], [0.622, 0.622], color=LIGHT, lw=1.0)
        for i, (t, n) in enumerate(items):
            y = 0.565 - i * 0.068
            ax.text(x + 0.025, y, t, fontsize=9.8, color=DARK, va="center",
                    weight="bold")
            ax.text(x + 0.025, y - 0.030, n, fontsize=8.8, color=GRAY,
                    va="center")

    ax.add_patch(FancyArrowPatch((0.478, 0.535), (0.522, 0.535),
                                 arrowstyle="-|>", mutation_scale=13,
                                 color=GRAY, lw=1.2))
    ax.text(0.500, 0.480, "三天", fontsize=8.8, color=GRAY, ha="center",
            va="center")

    takeaway(fig, 0.150, "一个在收建制，一个在铺栈：撤掉的是团队，不是路线。")
    footer(fig, "据《财富》2026-11-13 报道、OpenAI 11-14 确认，及华为云 2026-11-16 发布会与 IT之家、环球网报道整理。")
    fig.savefig(OUT + "图1_两个方向.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(12, 6.8))
    ax = canvas(fig)
    head(fig, "74.8% 的分量",
         "同一个榜单：通用模型大幅领先专用策略；但这是仿真基准，不是车间")

    # ---- 左：两根柱
    fig.text(0.070, 0.780, "模拟操作基准成功率（%）", fontsize=12.0,
             color=DARK, weight="bold", va="center")
    fig.text(0.070, 0.742, "测试由英伟达开展；口径为暂停式仿真基准，非真机实时控制",
             fontsize=9.0, color=GRAY, va="center")
    axb = fig.add_axes([0.090, 0.330, 0.360, 0.380])
    names = ["GPT-6 Astra\n通用模型", "榜单最佳\n专用机器人模型"]
    vals = [74.8, 51.0]
    bars = axb.bar(names, vals, width=0.46, color=[NAVY, GRAY])
    for b, v in zip(bars, vals):
        axb.text(b.get_x() + b.get_width() / 2, v + 2.2, f"{v}", fontsize=11.5,
                 color=DARK, ha="center", weight="bold")
    axb.set_ylim(0, 90)
    axb.set_xticks([0, 1])
    axb.set_xticklabels(names, fontsize=9.4, color=DARK)
    axb.tick_params(axis="y", labelsize=8.6, colors=GRAY, length=0)
    for s in ("top", "right"):
        axb.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        axb.spines[s].set_color(LIGHT)
    axb.grid(axis="y", color=LIGHT, lw=0.8, alpha=0.7)
    axb.set_axisbelow(True)
    axb.text(0.5, 84.0, "相差 23.8 个百分点", fontsize=9.6, color=RED,
             ha="center", weight="bold")

    # ---- 右：能 / 不能
    blocks = [
        ("能证明", NAVY, 0.720, [
            "看懂场景、直接输出动作，通用模型已越过专用策略的门槛",
            "大脑不必再单独养一个机器人基础模型",
        ]),
        ("不能证明", RED, 0.470, [
            "实时闭环控制：仿真里可以暂停，车间里不能",
            "真机数据与长尾工况，才是真正难的部分",
            "交付工程：CoRL 2026 上那 208 号展位是空的",
        ]),
    ]
    for title, color, ytop, lines in blocks:
        ax.add_patch(Rectangle((0.520, ytop - 0.190), 0.425, 0.190,
                               facecolor="#fafafb", edgecolor=LIGHT,
                               linewidth=1.0))
        ax.text(0.545, ytop - 0.035, title, fontsize=11.5, color=color,
                weight="bold", va="center")
        for i, line in enumerate(lines):
            ax.text(0.545, ytop - 0.085 - i * 0.045, "· " + line, fontsize=8.8,
                    color=DARK if i == 0 else GRAY, va="center")

    takeaway(fig, 0.150, "榜单分数和车间交付之间，隔着整套工程。")
    footer(fig, "据《财富》报道中转述的英伟达测试结果整理；基准口径为模拟操作任务，非真机实时控制。")
    fig.savefig(OUT + "图2_74.8的分量.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(12, 6.8))
    ax = canvas(fig)
    head(fig, "两条路线的栈",
         "左边价值往上游集中，右边价值在栈内分摊")

    def stack(x, title, color, layers):
        ax.text(x + 0.145, 0.790, title, fontsize=12.5, color=color,
                weight="bold", ha="center", va="center")
        for i, (name, note) in enumerate(layers):
            y = 0.665 - i * 0.130
            ax.add_patch(Rectangle((x, y - 0.048), 0.290, 0.096,
                                   facecolor="#fafafb" if i else "#f2f4f7",
                                   edgecolor=LIGHT, linewidth=1.0))
            ax.text(x + 0.145, y + 0.014, name, fontsize=10.0, color=DARK,
                    ha="center", va="center", weight="bold")
            ax.text(x + 0.145, y - 0.024, note, fontsize=8.4, color=GRAY,
                    ha="center", va="center")
        # 价值流向箭头
        ax.add_patch(FancyArrowPatch((x - 0.030, 0.400), (x - 0.030, 0.645),
                                     arrowstyle="-|>", mutation_scale=14,
                                     color=color, lw=1.4))
        ax.text(x - 0.045, 0.522, "价值流向", fontsize=8.6, color=color,
                ha="center", va="center", rotation=90)

    stack(0.080, "OpenAI 的写法", NAVY, [
        ("通用模型（GPT-6 Astra）", "一个大脑适配多种身体"),
        ("应用与硬件（Applied）", "机器人业务并入应用部门"),
        ("本体与场景厂商", "逐渐变成身体供应商"),
        ("终端场景", "议价权被上游拿走"),
    ])
    stack(0.590, "华为云的写法", RED, [
        ("昇腾芯片", "训练与推理都跑在自家算力上"),
        ("CloudRobo-WM1.2", "昇腾原生世界模型，已开源"),
        ("鸿蒙 + openPangu-2.1-Pro", "ArkTS 代码生成、算子开发"),
        ("行业场景", "环卫清扫机器人已启动预售"),
    ])

    takeaway(fig, 0.150, "通用性由谁买单，决定路线怎么分叉。")
    footer(fig, "两条栈为本文据公开信息归纳；OpenAI 侧不涉及具体芯片自研计划，华为云侧以发布会披露为准。")
    fig.savefig(OUT + "图3_两条路线的栈.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")
