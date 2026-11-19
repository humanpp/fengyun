# -*- coding: utf-8 -*-
"""
《一句"他是谁"之后，四十分钟谈的是乌克兰》配套图表
事实口径（2026-11-19，核对财新现场稿、新华社/央视、SBS、lenta 等后）：
  · 2026 年 11 月 19 日，来华出席 APEC 第三十三次领导人非正式会议的美国总统
    特朗普与俄罗斯总统普京在深圳举行会晤。现场视频：身着蓝色领带的特朗普步入
    布置着美俄两国国旗的房间，伸出右手指向身着深红色领带的普京，笑着说"他是谁？
    他是我的朋友"；随后握手，普京同时伸左手轻拍特朗普右臂，特朗普说"很高兴见到
    你"并靠近普京右耳耳语（财新网 11-19 16:25 现场稿）。
  · 会谈时长各方口径不一：韩国 SBS 称约 40 分钟；lenta 等称约 40 分钟；俄媒
    转述称 48 分钟；乌克兰 UA.NEWS 称近一小时，并称因美俄会谈，特朗普与习近平
    的双边会晤推迟。会后未对媒体发表联合声明（open.kg）。
  · 议题：乌克兰问题为主要议题（财新网标题）。特朗普称两人"相识已久"，此次
    会晤"或许能促成许多美好的事物，或者至少是一个良好的开端"（凤凰网，经新浪
    转载）；并称双方关系很好。普京"心情很好"（SBS）。美方随行包括国务卿鲁比奥、
    财长贝森特（lenta）。
  · 当日下午，国家主席习近平在深圳同普京、特朗普举行中俄美元首会晤，就大国
    如何正确相处、共同为世界和平托底提出 4 点看法；第一点为"坚持相互尊重"：
    三国国情不同，谁也改变不了谁；要尊重彼此主权和领土完整、尊重各自选择的
    社会制度和发展道路、尊重彼此核心利益和重大关切；坚持不干涉别国内政，
    在涉及对方的重大敏感问题上提前沟通、换位思考、谨慎行事，特别是不能触碰
    对方的底线（新华社，经财新网 11-19 17:53 转述）。
  · 同日，习近平会见特朗普，主题之一为"中美应确保人工智能始终处于人类控制
    之下"（财新网 11-19 16:18）。日本首相高市早苗亦在深圳会见普京，为俄日
    领导人时隔 7 年再次面对面（财新网 11-19）。
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
    fig = base("一天三场会，从一句玩笑开始",
               "2026 年 11 月 19 日｜深圳，APEC 第三十三次领导人非正式会议期间")
    ax = canvas(fig)

    cards = [
        ("美俄双边", "约 40 分钟", "乌克兰问题为主要议题\n会后未发表联合声明", NAVY, 0.020),
        ("中美双边", "会晤推迟", "主题之一：AI 须处于\n人类控制之下", SLATE, 0.350),
        ("中俄美三方", "当日下午", "习近平主持\n提出四点看法", RED, 0.680),
    ]

    y, h, w = 0.520, 0.250, 0.290

    for i, (title, meta, note, color, x) in enumerate(cards):
        ax.add_patch(FancyBboxPatch((x, y), w, h,
                                    boxstyle="round,pad=0.006",
                                    facecolor="white", edgecolor=LIGHT,
                                    linewidth=1.1))
        ax.add_patch(Rectangle((x, y + h - 0.012), w, 0.012, facecolor=color,
                               edgecolor="none"))
        ax.text(x + 0.024, y + h - 0.048, title, fontsize=11.6, color=color,
                weight="bold", ha="left", va="center")
        ax.text(x + 0.024, y + h - 0.100, meta, fontsize=8.6, color=GRAY,
                ha="left", va="center")
        ax.text(x + 0.024, y + 0.052, note, fontsize=8.6, color=SLATE,
                ha="left", va="center", linespacing=1.8)

        if i < 2:
            ax.annotate("", xy=(x + w + 0.034, y + h / 2), xytext=(x + w + 0.008, y + h / 2),
                        arrowprops=dict(arrowstyle="-|>", color=LIGHT,
                                        linewidth=1.6, shrinkA=0, shrinkB=0))

    ax.text(0.020, 0.400,
            "顺序：先美俄场边双边，再中美双边，最后是三国元首同席。"
            "据外媒，因美俄会谈，中美双边被推迟。",
            fontsize=9.0, color=SLATE, ha="left", va="center")
    ax.text(0.020, 0.345,
            "同日还有一场：日本首相高市早苗在深圳会见普京，为俄日领导人时隔 7 年"
            "再次面对面。",
            fontsize=9.0, color=SLATE, ha="left", va="center")

    ax.add_patch(FancyBboxPatch((0.020, 0.190), 0.950, 0.100,
                                boxstyle="round,pad=0.006",
                                facecolor="white", edgecolor=LIGHT,
                                linewidth=1.0))
    ax.text(0.044, 0.240,
            "进门那一幕：特朗普指着普京说“他是谁？他是我的朋友”，随后握手，"
            "普京伸左手轻拍其右臂。",
            fontsize=9.0, color=SLATE, ha="left", va="center")

    punchline(fig, "玩笑是开场，乌克兰才是议程。")
    footer(fig, "事实：财新网 11-19（现场、中美、三方会晤）、新华社经财新转述的"
                "四点看法、UA.NEWS 11-19（推迟）、SBS 11-19｜制图：本文")
    fig.savefig(OUT + "图1_一天三场会.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("这场会谈开了多久，说法对不上",
               "美俄深圳场边会晤｜时长口径与对外发布情况")
    ax = canvas(fig)

    rows = [
        ("SBS、lenta 等", "约 40 分钟", 40, NAVY),
        ("俄媒转述", "48 分钟", 48, SLATE),
        ("乌克兰 UA.NEWS", "近 1 小时", 60, SLATE),
    ]

    x0 = 0.330
    scale = 0.480 / 70.0

    y = 0.755
    for name, label, minutes, color in rows:
        ax.text(0.028, y, name, fontsize=9.6, color=DARK, ha="left",
                va="center")
        ax.add_patch(Rectangle((x0, y - 0.032), minutes * scale, 0.064,
                               facecolor=color, edgecolor="none"))
        ax.text(x0 + minutes * scale + 0.014, y, label, fontsize=10.0,
                color=color, weight="bold", ha="left", va="center")
        y -= 0.125

    ax.text(0.028, 0.330,
            "同一场会，从 40 分钟到近 1 小时，差出二十分钟。差别不在事实，在谁在数："
            "有的算正式会谈，有的把开场寒暄一起算进去。",
            fontsize=9.0, color=SLATE, ha="left", va="center")
    ax.text(0.028, 0.275,
            "比时长更确定的是发布：会谈结束后，双方没有对媒体发表联合声明，"
            "也没有共同记者会。",
            fontsize=9.0, color=SLATE, ha="left", va="center")

    ax.add_patch(FancyBboxPatch((0.028, 0.150), 0.940, 0.080,
                                boxstyle="round,pad=0.006",
                                facecolor="white", edgecolor=LIGHT,
                                linewidth=1.0))
    ax.text(0.052, 0.190,
            "唯一被双方同时确认的，是这场会开了；至于谈成什么，公开信息里只有各自的转述。",
            fontsize=9.0, color=SLATE, ha="left", va="center")

    punchline(fig, "时长对不上，说明公开的只有画面。")
    footer(fig, "事实：SBS 11-19（约 40 分钟）、lenta 11-19（约 40 分钟）、"
                "俄媒转述（48 分钟）、UA.NEWS 11-19（近 1 小时）、open.kg 11-19"
                "（未对媒体发表联合声明）｜时长与口径为原报道表述｜制图：本文")
    fig.savefig(OUT + "图2_时长四种口径.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("公开可见的实质内容，只有这一段",
               "中俄美元首会晤｜习近平四点看法中的第一点：坚持相互尊重")
    ax = canvas(fig)

    ax.text(0.028, 0.800,
            "“中俄美三国国情不同，谁也改变不了谁，这是历史形成的，"
            "也是各自人民的自主选择。”",
            fontsize=11.0, color=DARK, ha="left", va="center")

    items = [
        ("尊重主权和领土完整", "原文：要尊重彼此主权和领土完整"),
        ("尊重社会制度和发展道路", "各自选择的路，别人改不了"),
        ("尊重核心利益和重大关切", "敏感问题上提前沟通、换位思考"),
        ("不干涉内政，不触碰底线", "谨慎行事，特别是不能碰对方的底线"),
    ]

    y = 0.660
    for i, (head, note) in enumerate(items):
        ax.add_patch(FancyBboxPatch((0.028, y - 0.070), 0.940, 0.100,
                                    boxstyle="round,pad=0.004",
                                    facecolor="white", edgecolor=LIGHT,
                                    linewidth=1.0))
        ax.text(0.056, y - 0.006, "0%d" % (i + 1), fontsize=9.0, color=GRAY,
                ha="left", va="center")
        ax.text(0.110, y + 0.014, head, fontsize=9.8, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(0.110, y - 0.032, note, fontsize=8.6, color=SLATE,
                ha="left", va="center")
        y -= 0.125

    ax.text(0.028, 0.170,
            "四点看法中的后三点，新华社通稿未在首屏公开全文；本文只引第一点。",
            fontsize=8.6, color=GRAY, ha="left", va="center")

    punchline(fig, "玩笑可以剪成短视频，这一段只能读原文。")
    footer(fig, "事实：新华社通稿“习近平就大国如何正确相处、共同为世界和平托底"
                "提出 4 点看法”，经财新网 11-19 17:53 转述；引文为第一点原文｜制图：本文")
    fig.savefig(OUT + "图3_四点看法第一点.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)
