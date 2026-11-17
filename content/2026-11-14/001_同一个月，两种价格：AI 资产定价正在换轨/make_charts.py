# -*- coding: utf-8 -*-
"""
生成《同一个月，两种价格：AI 资产定价正在换轨》配套图表
数据来源：文章正文及其脚注所列公开报道
风格：克制传媒风，白底、低饱和配色、标题即结论
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

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

import os

# 图片输出到脚本所在目录，脚本随文章一起归档，换目录无需改代码
OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep


def clean(ax, axis="x"):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(LIGHT)
    ax.tick_params(colors=DARK, labelsize=11, length=0)
    ax.set_axisbelow(True)
    ax.grid(axis=axis, color=LIGHT, linewidth=0.8, alpha=0.55)


def footer(fig, text):
    fig.text(0.045, 0.022, text, fontsize=8.6, color=GRAY, ha="left", va="bottom")


# ---------------------------------------------------------------- 图 1
def fig1():
    fig, (ax1, ax2) = plt.subplots(
        1, 2, figsize=(12, 7.2), gridspec_kw={"width_ratios": [1.12, 1]}
    )
    fig.subplots_adjust(left=0.055, right=0.945, top=0.735, bottom=0.135, wspace=0.55)

    fig.suptitle(
        "一周之内，同一批钱给出两种价格",
        fontsize=19, color=DARK, x=0.045, ha="left", y=0.955, weight="bold",
    )
    fig.text(
        0.045, 0.888,
        "左：Anthropic 成为“AI 第一股”，需求集中在唯一可买标的　|　右：OpenAI 只拿到原计划一半",
        fontsize=11, color=GRAY, ha="left",
    )

    # ---- 左：Anthropic 资金构成
    base = 643.5   # 78 美元上限 × 8.25 亿股
    priv = 260.0   # 基石私募配售
    total = base + priv

    ax1.barh(0, base, height=0.30, color=NAVY)
    ax1.barh(0, priv, left=base, height=0.30, color=RED)
    ax1.text(base / 2, 0, f"{base:.0f}", ha="center", va="center",
             color="white", fontsize=15, weight="bold")
    ax1.text(base + priv / 2, 0, f"{priv:.0f}", ha="center", va="center",
             color="white", fontsize=13, weight="bold")

    ax1.annotate(
        "", xy=(total + 90, 0), xytext=(total + 14, 0),
        arrowprops=dict(arrowstyle="-|>", color=DARK, lw=1.4),
    )
    ax1.text(total + 100, 0, f"合计 ≈ {total:.0f}", ha="left", va="center",
             fontsize=15, color=DARK, weight="bold")

    # 图例式说明，放在柱子下方空白区
    ax1.plot([base / 2], [-0.62], marker="s", ms=8, color=NAVY, clip_on=False)
    ax1.text(base / 2 + 28, -0.62, "基础发行（上限）", va="center", ha="left",
             fontsize=10.2, color=DARK)
    ax1.plot([base + priv / 2], [-0.62], marker="s", ms=8, color=RED, clip_on=False)
    ax1.text(base + priv / 2 + 28, -0.62, "基石私募配售", va="center", ha="left",
             fontsize=10.2, color=DARK)

    ax1.set_yticks([])
    ax1.set_xlim(0, 1180)
    ax1.set_ylim(-1.05, 1.05)
    ax1.set_xlabel("十亿美元", fontsize=11, color=GRAY)
    clean(ax1)

    ax1.set_title("Anthropic IPO", fontsize=13.5, color=DARK,
                  loc="left", pad=36, weight="bold")
    ax1.text(0, 1.020, "发行区间 70–78 美元　·　8.25 亿股　·　代码 ANT　·　11/19 挂牌",
             fontsize=10.2, color=GRAY, transform=ax1.transAxes, va="bottom")

    box = dict(boxstyle="round,pad=0.55", facecolor=PALE, edgecolor=LIGHT, linewidth=0.9)
    ax1.text(0.02, 0.80,
             "认购达可配售股数约 6 倍，承销商已在\n讨论把发行价推至区间之上；估值目标\n被抬到 1.5 万亿美元甚至更高",
             fontsize=10.4, color=DARK, transform=ax1.transAxes, va="center",
             linespacing=1.8, bbox=box)
    ax1.text(0.02, 0.005, "超过 SpaceX，成为史上最大 IPO",
             fontsize=10.4, color=RED, transform=ax1.transAxes,
             va="bottom", weight="bold")

    # ---- 右：OpenAI 目标 vs 实际
    target, actual = 300.0, 150.0
    ax2.barh(0, target, height=0.30, color=LIGHT)
    ax2.barh(0, actual, height=0.30, color=RED)
    ax2.text(actual / 2, 0, f"{actual:.0f}", ha="center", va="center",
             color="white", fontsize=15, weight="bold")

    # 缺口用斜线填充强调
    ax2.barh(0, target - actual, left=actual, height=0.30,
             color="none", edgecolor=RED, hatch="///", linewidth=0)
    ax2.text(target + 8, 0, f"目标 {target:.0f}", ha="left", va="center",
             color=GRAY, fontsize=11.5, weight="bold")
    ax2.annotate(
        "缺口 150 亿（−50%）",
        xy=(actual + (target - actual) / 2, 0.155),
        xytext=(target + 40, 0.66),
        fontsize=11.2, color=RED, ha="center", va="bottom", weight="bold",
        arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.2,
                        connectionstyle="arc3,rad=0.18"),
    )

    ax2.set_yticks([])
    ax2.set_xlim(0, 430)
    ax2.set_ylim(-1.05, 1.05)
    ax2.set_xlabel("十亿美元", fontsize=11, color=GRAY)
    clean(ax2)

    ax2.set_title("OpenAI 私募融资", fontsize=13.5, color=DARK,
                  loc="left", pad=36, weight="bold")
    ax2.text(0, 1.020, "投前估值由 1.4 万亿降至 1.25 万亿美元",
             fontsize=10.2, color=GRAY, transform=ax2.transAxes, va="bottom")

    ax2.text(0.02, 0.80,
             "轮次尚未关闭，被描述为\n“机会性融资”，用于为预计\n2027 年的 IPO 储粮",
             fontsize=10.4, color=DARK, transform=ax2.transAxes, va="center",
             linespacing=1.8, bbox=box)
    ax2.text(0.02, 0.005, "首批交割约 110 亿美元，其余待完成",
             fontsize=10.4, color=GRAY, transform=ax2.transAxes, va="bottom")

    footer(fig, "数据：CNBC、彭博社、《金融时报》、招商证券国际、钜亨网。左图合计为发行上限（643.5）与基石私募配售（260）之和，单位十亿美元。")
    fig.savefig(OUT + "图1_资本侧分化.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    panels = [
        ("SWE-sweep 编程修复", "%",
         [("Hydrogen", 13.5), ("GPT-6.1 Terra", 5.8), ("Sonnet 5.5", 3.1)], 16.5),
        ("AutomationBench-AA", "%",
         [("Hydrogen", 76.1), ("Sonnet 5.5", 71.8), ("GPT-6.1 Terra", 60.2)], 92),
        ("Artificial Analysis 综合指数", "分",
         [("Hydrogen", 54), ("Sonnet 5.5", 55), ("GPT-6.1 Terra", 51)], 66),
    ]

    fig, axes = plt.subplots(1, 3, figsize=(12, 7.2))
    fig.subplots_adjust(left=0.145, right=0.955, top=0.720, bottom=0.255, wspace=1.05)

    fig.suptitle("中端模型的分数追上旗舰，成本却不到三分之一",
                 fontsize=19, color=DARK, x=0.045, ha="left", y=0.955, weight="bold")
    fig.text(0.045, 0.888,
             "Gemini 4 Hydrogen 与两款同代中端/旗舰模型的横向对照（数值越高越好）",
             fontsize=11, color=GRAY, ha="left")

    for ax, (title, unit, rows, xmax) in zip(axes, panels):
        names = [r[0] for r in rows]
        vals = [r[1] for r in rows]
        ypos = range(len(rows))[::-1]
        colors = [NAVY if n == "Hydrogen" else GRAY for n in names]

        ax.barh(list(ypos), vals, height=0.40, color=colors)
        for y, v in zip(ypos, vals):
            ax.text(v + xmax * 0.03, y,
                    f"{v:g}{unit}" if unit == "%" else f"{v:g}",
                    va="center", ha="left", fontsize=12.5, color=DARK, weight="bold")

        ax.set_yticks(list(ypos))
        ax.set_yticklabels(names, fontsize=11.5)
        for lbl in ax.get_yticklabels():
            if lbl.get_text() == "Hydrogen":
                lbl.set_color(NAVY)
                lbl.set_fontweight("bold")
        ax.set_xlim(0, xmax)
        ax.set_ylim(-0.55, len(rows) - 0.45)
        ax.set_xlabel(unit if unit == "%" else "综合得分", fontsize=10, color=GRAY,
                      labelpad=8)
        clean(ax)
        ax.set_title(title, fontsize=12.5, color=DARK, loc="left", pad=14)

    note = (
        "Hydrogen 定价：输入 1.50 美元 / 输出 7.50 美元（每百万 Token），覆盖完整 100 万 Token 上下文，无阶梯计价。\n"
        "平均每任务成本不到 Sonnet 5.5 的三分之一 —— 另两款未披露绝对价格，故此处并列“分数”而非“性能—成本”散点。"
    )
    box = dict(boxstyle="round,pad=0.75", facecolor=PALE, edgecolor=LIGHT, linewidth=0.9)
    fig.text(0.045, 0.088, note, fontsize=10.2, color=DARK, ha="left",
             va="center", linespacing=1.9, bbox=box)

    footer(fig, "数据：谷歌发布材料、Artificial Analysis 第三方评测。SWE-sweep 与 AutomationBench-AA 为百分比，综合指数为独立评分。")
    fig.savefig(OUT + "图2_产品侧成本压力.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig, (ax1, ax2) = plt.subplots(
        1, 2, figsize=(12, 7.2), gridspec_kw={"width_ratios": [1, 1.18]}
    )
    fig.subplots_adjust(left=0.055, right=0.965, top=0.775, bottom=0.145, wspace=0.30)

    fig.suptitle("客户不是换了供应商，是把供应商搬进了机房",
                 fontsize=19, color=DARK, x=0.045, ha="left", y=0.955, weight="bold")
    fig.text(0.045, 0.888,
             "Revolut 将约 2000 名工程师的默认编程模型由 Claude Code / Codex 换为自托管 GLM 5.3，"
             "以 56 张英伟达 B200 支撑",
             fontsize=10.8, color=GRAY, ha="left")

    # ---- 左：单位成本
    labels = ["切换前\nClaude / GPT", "切换后\n自托管 GLM 5.3"]
    costs = [3.00, 0.30]
    ax1.bar([0, 1], costs, width=0.34, color=[LIGHT, NAVY])
    ax1.text(0, costs[0] + 0.10, f"≈ {costs[0]:.2f}", ha="center", va="bottom",
             fontsize=15, color=DARK, weight="bold")
    # 切换后数值放进柱内，避免与箭头冲突
    ax1.text(1, costs[1] / 2, f"≈ {costs[1]:.2f}", ha="center", va="center",
             fontsize=13, color="white", weight="bold")
    ax1.annotate(
        "−90%", xy=(1.20, 0.34), xytext=(0.52, 1.75),
        fontsize=13, color=RED, ha="center", weight="bold",
        arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.3,
                        connectionstyle="arc3,rad=-0.30"),
    )
    ax1.set_xticks([0, 1])
    ax1.set_xticklabels(labels, fontsize=11)
    ax1.set_xlim(-0.6, 1.6)
    ax1.set_ylim(0, 3.7)
    ax1.set_ylabel("美元 / 百万 Token（混合口径）", fontsize=10.5, color=GRAY)
    clean(ax1, axis="y")
    ax1.set_title("推理成本", fontsize=12.5, color=DARK, loc="left", pad=14)

    # ---- 右：效率指标（竖直分组，横轴为指标）
    metrics = ["编码耗时", "需求到合并周期"]
    before = [100, 100]
    after = [40, 30]
    xpos = [0, 1]
    w = 0.30

    ax2.bar([x - w / 2 - 0.01 for x in xpos], before, width=w, color=LIGHT)
    ax2.bar([x + w / 2 + 0.01 for x in xpos], after, width=w, color=NAVY)

    for x, a, label in zip(xpos, after, ["−60%", "−70%"]):
        ax2.text(x + w / 2 + 0.01, a + 2.5, label, ha="center", va="bottom",
                 fontsize=12.5, color=NAVY, weight="bold")
        ax2.text(x - w / 2 - 0.01, 100 + 2.5, "100", ha="center", va="bottom",
                 fontsize=10, color=GRAY)

    ax2.set_xticks(xpos)
    ax2.set_xticklabels(metrics, fontsize=11.5)
    ax2.set_xlim(-0.62, 1.62)
    ax2.set_ylim(0, 122)
    ax2.set_ylabel("相对指数（切换前 = 100）", fontsize=10.5, color=GRAY)
    clean(ax2, axis="y")
    ax2.set_title("交付效率", fontsize=12.5, color=DARK, loc="left", pad=14)

    # 图例
    hs = [plt.Rectangle((0, 0), 1, 1, facecolor=LIGHT),
          plt.Rectangle((0, 0), 1, 1, facecolor=NAVY)]
    ax2.legend(hs, ["切换前", "切换后"], loc="upper right", frameon=False,
               fontsize=10.5, ncol=1, handlelength=1.0, handleheight=1.0,
               labelcolor=DARK, borderpad=0.2)

    footer(fig, "数据：Revolut AI 运营负责人 David Abitbol 于 2026-10-13 AI Engineer NYC 的复盘；新华社 2026-11-13 综述引述。"
                "成本降幅不含 GPU 采购与人力，切换前单位成本由“降至十分之一”反推，故标约数。")
    fig.savefig(OUT + "图3_客户侧替换账单.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")
