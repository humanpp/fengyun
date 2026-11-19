# -*- coding: utf-8 -*-
"""
《特朗普说"不支持台独"，这五个字中方要了两年》配套图表
事实口径（2026-11-19，逐条核对外交部通稿、新华社原文与多家外媒后）：
  · 2026 年 11 月 19 日下午，国家主席习近平在深圳会见来华出席亚太经合组织
    第三十三次领导人非正式会议的美国总统特朗普。这是两人今年第三次双边会晤
    （5 月北京、9 月华盛顿、11 月深圳）（外交部通稿 11-19 16:16、新华社 11-19、
    联合早报 11-19）。
  · 特朗普在会晤中表示："建交 40 多年来，美中关系取得显著进展……美国不支持'台独'。
    祝贺中方成功举办亚太经合组织领导人非正式会议。"（外交部通稿 11-19、
    央视新闻 11-19、第一财经 11-19）
  · 习近平就台湾问题表示："美方要坚持做正确的事，避免中美关系出现大的波折。"
    （外交部通稿 11-19）
  · 双方同意制定建设性战略稳定关系行动计划（外交部通稿 11-19）。
  · 会晤当天上午，习近平在深圳国际交流中心主持亚太经合组织第三十三次领导人
    非正式会议并发表题为《建设亚太共同体，续写"亚太奇迹"新篇章》的讲话；
    会议一致通过 2026 年亚太经合组织领导人宣言，就亚太共同体建设提出"深圳展望"
    及贸易、联通、创新领域三项成果文件（新华社 11-19、外交部 11-19、
    香港电台 11-19、金十数据 11-19 引外交部发言人郭嘉昆）。
  · 措辞沿革（本文用于对照的关键背景）：
    - 美方长期官方表述为"不支持台独"（does not support Taiwan independence）。
    - 2024 年 11 月旧金山会晤，中方要求美方将"不支持台独"改为"反对台独"，美方未接受
      （路透社 2024-10-29 独家，多家转述）。
    - 2026 年 5 月北京会晤，习近平要求美方"坚持反对'台独'的正确立场"；
      特朗普会后接受福克斯新闻采访时称"不希望看到有人走向独立"，未作承诺；
      美国驻华大使庞德伟 5 月 18 日称特朗普当面向习近平表明美国不支持台湾独立
      （新华社 2026-05-14、联合早报 2026-05-19、BBC 中文 2026-05-17）。
    - 2026 年 9 月华盛顿会晤，习近平再次要求美方"坚持反对'台独'的正确立场"；
      美方公布内容未采用"反对"表述，国务院重申对台立场未变
      （新华社 2026-09-24、中央社 2025-09-30 相关表态、中国时报 2026-09-28 分析）。
    - 2026 年 11 月 19 日深圳会晤，通稿表述仍为"不支持'台独'"。
  · 美方反应：截至本文写作时（2026-11-19 17 时前后），未见白宫就"不支持台独"
    一句单独发布确认文本；台湾《自由时报》11-19 16:52 报道称"美国方面未证实"。
    本文据此标注"美方未单独确认"，不据此推断美方立场变化。
本文换算（非当事方口径）：5 月、9 月、11 月三次会晤，跨度为 2026 年 5 月至 11 月，
约 6 个月；"两年"指中方自 2024 年 11 月起持续提出"反对台独"要求至今，
按 2024 年 11 月至 2026 年 11 月计约两年。
风格：克制传媒风，白底、低饱和配色、标题即结论。输出目录 = 脚本所在目录。
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False

NAVY = "#1f3a5f"
RED = "#b5544a"
GRAY = "#8a8f98"
SLATE = "#5f6673"
LIGHT = "#d8dbe0"
DARK = "#2b2f36"
PALE = "#eef0f3"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep


def base(title, sub):
    fig = plt.figure(figsize=(12, 6.8))
    fig.patch.set_facecolor("white")
    fig.text(0.045, 0.950, title, fontsize=20, color=DARK, weight="bold",
             ha="left", va="top")
    fig.text(0.045, 0.876, sub, fontsize=10.4, color=GRAY, ha="left", va="top")
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
    fig = base("一天之内，两场会",
               "2026 年 11 月 19 日，深圳｜上午主持 APEC，下午会见特朗普")
    ax = canvas(fig)

    # 画布高 4.76 英寸 = 342.7 磅，1 磅 ≈ 0.002918 轴单位。
    # 卡片内所有文字统一 va="top" 自上而下排，间距按磅数给定，不靠试凑。
    PT = 1.0 / (4.76 * 72.0)
    CARD_H = 0.300

    cards = [
        ("上午", "深圳国际交流中心", NAVY,
         "习近平主持亚太经合组织第三十三次领导人非正式会议并发表讲话",
         "会议一致通过领导人宣言，就亚太共同体建设提出「深圳展望」，\n以及贸易、联通、创新领域三项成果文件",
         0.520),
        ("下午", "深圳", RED,
         "习近平会见美国总统特朗普",
         "这是两人今年第三次双边会晤（5 月北京、9 月华盛顿、11 月深圳）；\n双方同意制定建设性战略稳定关系行动计划",
         0.140),
    ]

    for when, where, color, what, note, y0 in cards:
        top = y0 + CARD_H
        ax.add_patch(FancyBboxPatch((0.028, y0), 0.944, CARD_H,
                                    boxstyle="round,pad=0.006",
                                    facecolor="white", edgecolor=LIGHT,
                                    linewidth=1.0))
        ax.add_patch(Rectangle((0.028, y0), 0.008, CARD_H,
                               facecolor=color, edgecolor="none"))

        y = top - 8.0 * PT
        ax.text(0.072, y, when, fontsize=10.0, color=color, weight="bold",
                ha="left", va="top")

        y -= (10.0 + 5.0) * PT
        ax.text(0.072, y, where, fontsize=8.8, color=GRAY,
                ha="left", va="top")

        y -= (8.8 + 12.0) * PT
        ax.text(0.072, y, what, fontsize=10.4, color=DARK, weight="bold",
                ha="left", va="top")

        y -= (10.4 + 9.0) * PT
        ax.text(0.072, y, note, fontsize=8.4, color=SLATE,
                ha="left", va="top", linespacing=1.75)

    ax.text(0.028, 0.078,
            "同一天还举行了中俄美三方会晤——这是三国领导人首次同席。",
            fontsize=8.8, color=SLATE, ha="left", va="center")

    punchline(fig, "台湾问题是下午那场里的一个段落，不是全部。")
    footer(fig, "事实：外交部通稿 11-19、新华社 11-19、香港电台 11-19、"
                "路透 11-18、美联社 11-19｜制图：本文")
    fig.savefig(OUT + "图1_一天之内两场会.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("中方要的是「反对」，拿到的是「不支持」",
               "同一个议题，两年里四次上桌｜措辞没有变，位置在往前挪")
    ax = canvas(fig)

    rows = [
        ("2024.11", "旧金山", "中方要求改为「反对台独」", "美方未接受", GRAY, "white"),
        ("2026.05", "北京", "中方要求「坚持反对台独」", "特朗普称「不希望有人走向独立」，未作承诺",
         SLATE, "white"),
        ("2026.09", "华盛顿", "中方再次要求「坚持反对台独」", "美方公布内容未采用「反对」",
         SLATE, "white"),
        ("2026.11", "深圳", "中方要求「坚持做正确的事」", "通稿表述：美国不支持「台独」",
         NAVY, NAVY),
    ]

    y = 0.800
    for date, place, ask, got, color, face in rows:
        ax.add_patch(FancyBboxPatch((0.028, y - 0.086), 0.944, 0.172,
                                    boxstyle="round,pad=0.005",
                                    facecolor="white", edgecolor=LIGHT,
                                    linewidth=1.0))
        ax.text(0.058, y + 0.030, date, fontsize=11.0, color=color,
                weight="bold", ha="left", va="center")
        ax.text(0.058, y - 0.030, place, fontsize=8.4, color=GRAY,
                ha="left", va="center")
        ax.text(0.200, y + 0.034, ask, fontsize=10.2, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(0.200, y - 0.036, got, fontsize=8.6, color=SLATE,
                ha="left", va="center")
        y -= 0.196

    ax.text(0.028, 0.052,
            "四个时间点里，「反对」两个字一次也没有出现在美方表述中。11 月这次仍是「不支持」。",
            fontsize=9.0, color=SLATE, ha="left", va="center")

    punchline(fig, "措辞没变，但这句话第一次进了元首会晤的通稿。")
    footer(fig, "事实：路透 2024-10-29、新华社 2026-05-14／09-24／11-19、"
                "外交部通稿 11-19、联合早报 05-19、中国时报 09-28｜制图：本文")
    fig.savefig(OUT + "图2_反对与不支持.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("这句话，谁确认了",
               "同一条表述，三种来源状态｜越往下，可信度越低")
    ax = canvas(fig)

    rows = [
        ("中方通稿", "外交部 11-19 16:16、新华社 11-19、央视新闻 11-19",
         "直接引用特朗普原话", NAVY, NAVY, "已确认"),
        ("第三方通讯社", "路透、美联社、韩联社等当日报道，均引新华社",
         "转述中方通稿，非独立信源", SLATE, "white", "转述"),
        ("美方自身文本", "截至 11-19 17 时，未见白宫就该句单独发布确认",
         "台湾《自由时报》16:52 称「美国方面未证实」", RED, "white", "未确认"),
    ]

    y = 0.740
    for name, src, note, color, face, badge in rows:
        ax.add_patch(FancyBboxPatch((0.028, y - 0.104), 0.944, 0.208,
                                    boxstyle="round,pad=0.005",
                                    facecolor="white", edgecolor=LIGHT,
                                    linewidth=1.0))
        ax.add_patch(Rectangle((0.028, y - 0.104), 0.008, 0.208,
                               facecolor=color, edgecolor="none"))
        ax.text(0.070, y + 0.046, name, fontsize=11.4, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(0.070, y - 0.010, src, fontsize=8.6, color=SLATE,
                ha="left", va="center")
        ax.text(0.070, y - 0.062, note, fontsize=8.6, color=GRAY,
                ha="left", va="center")

        bx = 0.800
        ax.add_patch(FancyBboxPatch((bx, y - 0.030), 0.146, 0.060,
                                    boxstyle="round,pad=0.004",
                                    facecolor=face, edgecolor=color,
                                    linewidth=1.2))
        ax.text(bx + 0.073, y, badge, fontsize=9.0,
                color=("white" if face == NAVY else color),
                weight="bold", ha="center", va="center")
        y -= 0.244

    ax.text(0.028, 0.048,
            "这不等于美方否认。但在拿到美方文本之前，「美方证实」这四个字不能用。",
            fontsize=9.0, color=SLATE, ha="left", va="center")

    punchline(fig, "一句话的可信度，取决于谁把它写下来。")
    footer(fig, "事实：外交部通稿 11-19 16:16、新华社 11-19、自由时报 11-19 16:52、"
                "路透／美联社 11-19｜「未见白宫单独确认」为本文检索时点状态｜制图：本文")
    fig.savefig(OUT + "图3_谁确认了这句话.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)
