# -*- coding: utf-8 -*-
"""
《Anthropic 上市当天，前研究员在总部外呼吁禁止 AI"递归自我改进"》配套图表
事实口径（均经公开报道交叉核对）：
  · 2026-11-19（美东）Anthropic 上市首日，旧金山 Howard Street 总部外 100 余人抗议，
    要求限制 AI 递归自我改进；下午 2:30 前至少 4 人因堵塞大堂正门被捕，
    其中一人为 Stop AI 联合创始人 Guido Reichstadter，警方称将开罚单并给开庭日期后释放。
    —— Mission Local 2026-11-19、KQED、KRON4、The Guardian。
  · 同日纽约纳斯达克交易所外（时报广场）亦有反 AI 团体集会，亦有人被捕。—— The Guardian 2026-11-19。
  · 雅各布·考克森（Jacob Coxon）：曾在 OpenAI 与 Anthropic 做预训练研究，在 Anthropic 约四个月，
    2026-09-08 宣布离职，公开警告 AI 竞速危及人类；9-12 接受 BBC 访问。
    2026-11-13 称 Anthropic IPO 路演中一张算力需求图表是促使他离职的重要原因。
    2026-11-19 在总部外对抗议者说："他们应该禁止 RSI，关掉它。"
    以及："这里每来一个人，就有数十万人如果知道正在发生什么，也会来到这里。而这样的人有数百万。"
    —— 凤凰网科技引《旧金山标准报》2026-11-20、Business Insider、WSJ、TechCrunch、BBC、IT之家。
  · 三星电子 2026-11-18 在新加坡摩根士丹利会议上：
    DS 部门经营战略总裁金容宽称 Neocloud 在整体市场占比约 8%，"不认为这些疑虑会对 AI 整体成长
    趋势构成重大威胁"；晶圆代工销售与营销负责人康锡采称当前 AI 投资由实际需求驱动而非投机，
    长期合同提高了供需可见度，预计芯片短缺在可预见未来持续。—— 路透社 2026-11-18，多家转载。
  · SemiAnalysis 2026-11-13 模型更新：2028 年全球 AI 加速器资本开支预测由约 1.054 万亿美元
    下调至 7580 亿美元（−28%）；2029 年由 1.352 万亿降至 7960 亿（−41%）；2030 年由 1.531 万亿
    降至 9230 亿（−40%）；2026—2030 加速器逻辑硅片出货面积累计下调 17%，英伟达占其中 66%。
    —— 财联社、中国金融信息网、工商时报 2026-11-16/17。
说明：素材写"雅各布·科克森"，公开报道中文译名为"雅各布·考克森"，图中按后者。
      素材称"今年 9 月离开 Anthropic"经核属实（9 月 8 日宣布）。
      素材未提及抗议规模、被捕人数、纽约同步集会，本文据公开信源补入。
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
    fig = base("从辞职到喊话，七十二天",
               "雅各布·考克森（Jacob Coxon）：一个前研究员的路线")
    ax = canvas(fig)

    y_line = 0.575
    ax.plot([0.070, 0.935], [y_line, y_line], color=LIGHT, linewidth=2.0,
            zorder=2)

    nodes = [
        ("9·08", "宣布离职", "在 Anthropic 约四个月\n此前在 OpenAI 做预训练", "below", SLATE),
        ("9·12", "接受 BBC 访问", "称同行“真诚地恐惧”", "above", SLATE),
        ("11·13", "说出离职原因", "IPO 路演的一张\n算力需求图“太惊人了”", "below", GOLD),
        ("11·19", "总部外喊话", "“他们应该禁止 RSI\n关掉它”", "above", RED),
    ]
    xs = [0.115, 0.380, 0.640, 0.890]

    for x, (date, name, desc, where, col) in zip(xs, nodes):
        ax.add_patch(Circle((x, y_line), 0.013, facecolor=col,
                            edgecolor="white", linewidth=2.0, zorder=6))
        if where == "above":
            ax.text(x, y_line + 0.050, date, fontsize=10.0, color=col,
                    weight="bold", ha="center", va="bottom")
            ax.text(x, y_line + 0.088, name, fontsize=12.2, color=DARK,
                    weight="bold", ha="center", va="bottom")
            ax.text(x, y_line + 0.130, desc, fontsize=8.8, color=SLATE,
                    ha="center", va="bottom", linespacing=1.7)
        else:
            ax.text(x, y_line - 0.050, date, fontsize=10.0, color=col,
                    weight="bold", ha="center", va="top")
            ax.text(x, y_line - 0.088, name, fontsize=12.2, color=DARK,
                    weight="bold", ha="center", va="top")
            ax.text(x, y_line - 0.130, desc, fontsize=8.8, color=SLATE,
                    ha="center", va="top", linespacing=1.7)

    # 现场数字
    ax.add_patch(FancyBboxPatch((0.070, 0.135), 0.860, 0.110,
                                boxstyle="round,pad=0.010", facecolor=SAND,
                                edgecolor="#d9cdb6", linewidth=1.0))
    ax.text(0.092, 0.203, "11 月 19 日当天，旧金山总部外：", fontsize=9.6,
            color="#8a7a5e", weight="bold", ha="left", va="center")
    ax.text(0.092, 0.163,
            "100 余人集会　·　至少 4 人因堵塞大堂正门被捕　·　纽约纳斯达克门外同步集会",
            fontsize=9.6, color="#7a6746", ha="left", va="center")

    punchline(fig, "他在公司最值钱的那天，说了公司最不想听的话。")
    footer(fig, "事实：时间线与引语据《旧金山标准报》、Business Insider、WSJ、TechCrunch、BBC、凤凰网科技 2026-11-20；抗议规模与被捕人数据 Mission Local、KQED、The Guardian 2026-11-19｜制图：本文")
    fig.savefig(OUT + "图1_七十二天.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("“禁掉 RSI”不是一道是非题",
               "真正的分歧在三个关口：谁批准、谁检验、谁叫停")
    ax = canvas(fig)

    steps = [
        ("①", "谁批准", "这一轮用 AI 改 AI，\n开跑之前谁签字？",
         "实验室内部伦理委员会\n（现在的位置）", NAVY, 0.820),
        ("②", "谁检验", "改完的模型是不是\n真的更安全，谁验？",
         "第三方评估机构\n（尚不成体系）", GOLD, 0.600),
        ("③", "谁叫停", "发现异常时，\n谁有权按下停止键？",
         "监管机构\n（目前几乎空白）", RED, 0.380),
    ]

    for num, name, question, who, col, y in steps:
        ax.add_patch(FancyBboxPatch((0.070, y - 0.082), 0.400, 0.164,
                                    boxstyle="round,pad=0.010",
                                    facecolor="#fafbfc", edgecolor=col,
                                    linewidth=1.2))
        ax.text(0.092, y + 0.044, num + "  " + name, fontsize=12.4, color=col,
                weight="bold", ha="left", va="center")
        ax.text(0.092, y - 0.018, question, fontsize=9.2, color=SLATE,
                ha="left", va="center", linespacing=1.7)

        ax.annotate("", xy=(0.500, y), xytext=(0.478, y),
                    arrowprops=dict(arrowstyle="-|>", color=GRAY, linewidth=1.4))
        ax.text(0.520, y + 0.020, who, fontsize=9.0, color=col, weight="bold",
                ha="left", va="center", linespacing=1.7)

    ax.text(0.070, 0.198,
            "考克森的主张是第一步就停：不批准，就不用管后面两道。",
            fontsize=9.6, color=DARK, weight="bold", ha="left", va="center")
    ax.text(0.070, 0.155,
            "但只要有一家实验室不配合，单方面叫停就等于把位置让出去——这是争议真正的难点。",
            fontsize=9.0, color=GRAY, ha="left", va="center")

    punchline(fig, "喊“禁止”很容易，难的是回答：凭什么、由谁、怎么执行。")
    footer(fig, "说明：本图为分析框架，非当事方表述；“现在的位置/尚不成体系/几乎空白”为作者判断｜制图：本文")
    fig.savefig(OUT + "图2_三个关口.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("同一天，两种判断",
               "一边在喊停，一边在下调预测，还有一边说“短缺会持续”")
    ax = canvas(fig)

    # 左：SemiAnalysis 下修
    ax.text(0.075, 0.820, "SemiAnalysis：把远期算力砍了一刀", fontsize=11.4,
            color=NAVY, weight="bold", ha="left", va="center")

    bars = [
        ("2028", -28, "1.054 万亿 → 7580 亿"),
        ("2029", -41, "1.352 万亿 → 7960 亿"),
        ("2030", -40, "1.531 万亿 → 9230 亿"),
    ]
    x_left = 0.180
    x_scale = 0.0085

    for i, (year, pct, detail) in enumerate(bars):
        y = 0.720 - i * 0.110
        ax.text(x_left - 0.016, y, year, fontsize=10.4, color=DARK,
                ha="right", va="center")
        w = abs(pct) * x_scale
        ax.add_patch(FancyBboxPatch((x_left, y - 0.026), w, 0.052,
                                    boxstyle="round,pad=0.002",
                                    facecolor=NAVY, edgecolor="none",
                                    alpha=0.90, zorder=3))
        ax.text(x_left + w - 0.010, y, f"{pct}%", fontsize=10.6, color="white",
                weight="bold", ha="right", va="center", zorder=5)
        ax.text(0.930, y, detail, fontsize=8.8, color=GRAY,
                ha="right", va="center")

    # 右：三星表态
    ax.add_patch(FancyBboxPatch((0.075, 0.215), 0.860, 0.190,
                                boxstyle="round,pad=0.010", facecolor="#edf2f0",
                                edgecolor=GREEN, linewidth=1.2))
    ax.text(0.098, 0.365, "三星电子（11·18，新加坡摩根士丹利会议）", fontsize=10.6,
            color=GREEN, weight="bold", ha="left", va="center")
    ax.text(0.098, 0.320,
            "Neocloud 在整体市场约占 8%，“不认为会构成重大威胁”",
            fontsize=9.6, color=DARK, ha="left", va="center")
    ax.text(0.098, 0.272,
            "当前投资由实际需求驱动而非投机；芯片短缺将在可预见未来持续",
            fontsize=9.6, color=DARK, ha="left", va="center")

    ax.text(0.075, 0.168,
            "同一天，三条线各说各话：安全侧要叫停，研究侧砍远期，产业侧说紧缺没变。",
            fontsize=9.2, color=SLATE, ha="left", va="center")

    punchline(fig, "分歧不在“AI 会不会出事”，在“用哪个时间尺度算这笔账”。")
    footer(fig, "事实：SemiAnalysis 2026-11-13 模型更新（财联社、中国金融信息网、工商时报）；三星据路透社 2026-11-18｜制图：本文")
    fig.savefig(OUT + "图3_同一天两种判断.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)
