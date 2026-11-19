# -*- coding: utf-8 -*-
"""
《谷歌把 AI 代理免费开放六国》配套图表
事实口径（2026-11-19，逐条核对 Google 官方博客与公开报道后）：
  · 2026 年 11 月 17 日，Google 把 Gemini Spark 更名为 Tasks，向美国、日本、韩国、
    加拿大、澳大利亚、印度六国的免费用户开放；此前需订阅 AI Pro / AI Ultra
    （Google 官方博客、9to5Google 11-17、The Verge 11-17、Thurrott 11-18）；
  · 免费档运行 Gemini 4 Hydrogen；AI Pro / Ultra 档运行 11 月 18 日发布的
    Gemini 4 Neon（ITmedia 11-19、ITmedia 同稿）；
  · Tasks 跑在 Google Cloud Agent Compute Engine 上，每账号一台专属、不与他人共享的
    硬件隔离虚拟机；沙盒由安全红队定期测试，带防提示注入保护，浏览网页时启用
    Safe Browsing；敏感操作须用户确认；指令含糊时会追问（9to5Google、Thurrott、Google 博客）；
  · 2026 年 11 月 17 日，OpenAI 发布 GPT-6.2 Astra 与 GPT-6.2 Sol：Astra 面向最难项目，
    Sol 面向日常编码、写作与多步骤工作流且成本更低；进入 ChatGPT Work、Codex 与 API，
    同日上线 Amazon Bedrock（OpenAI 官方公告、9to5Mac 11-17、AWS 11-17）；
  · 2026 年 11 月 18 日，Google 发布 Gemini 4 Neon，定位"Carbon 的质量、Flash 的速度"，
    介于 Carbon（最深长周期）与 Hydrogen（日常快速）之间；API 价 $3 / 百万输入、
    $15 / 百万输出；在 Gemini app 内取代 3.1 Pro（Google 官方博客、9to5Google 11-18、
    The Verge 11-18、VentureBeat 11-18）；
  · Gemini 4 系列此前已有 Argon、Carbon、Hydrogen，Neon 是第四款，多家媒体记为
    "一个月内第四款"（The Verge、the-decoder 11-18）。
注意：图 2 的坐标位置为作者按公开定位所做的示意，不是基准分数。
风格：克制传媒风，白底、低饱和配色、标题即结论。输出目录 = 脚本所在目录。
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch, FancyArrowPatch

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


# ------------------------------------------------------------------ 图 1
def fig1():
    fig = base("同一件事，从订阅墙里搬了出来",
               "2026 年 11 月 17 日起｜原名 Spark，现名 Tasks｜六国免费用户可用")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    cards = [
        (0.030, "改名前", "Spark", SLATE,
         ["只对 AI Pro / AI Ultra 开放",
          "5 月随 Google I/O 发布",
          "10 月并入 Gemini 主 app"]),
        (0.590, "2026 年 11 月 17 日起", "Tasks", RED,
         ["六国免费用户可用，不再需要订阅",
          "美国、日本、韩国、加拿大、澳大利亚、印度",
          "免费档跑 Hydrogen｜付费档跑 Neon"]),
    ]

    for x, tag, name, color, lines in cards:
        ax.add_patch(FancyBboxPatch((x, 0.200), 0.380, 0.590,
                                    boxstyle="round,pad=0.010",
                                    facecolor="white", edgecolor=LIGHT,
                                    linewidth=1.0))
        ax.add_patch(Rectangle((x, 0.784), 0.380, 0.006, facecolor=color,
                               edgecolor="none"))
        ax.text(x + 0.030, 0.722, tag, fontsize=9.0, color=GRAY, ha="left",
                va="center")
        ax.text(x + 0.030, 0.652, name, fontsize=25.0, color=color,
                weight="bold", ha="left", va="center")
        ax.plot([x + 0.030, x + 0.350], [0.592, 0.592], color=LIGHT, lw=0.8)
        yy = 0.522
        for ln in lines:
            ax.text(x + 0.030, yy, ln, fontsize=9.2, color=DARK, ha="left",
                    va="center")
            yy -= 0.106

    ax.add_patch(FancyArrowPatch((0.432, 0.500), (0.570, 0.500),
                                 arrowstyle="-|>", mutation_scale=20,
                                 color=RED, linewidth=1.4))
    ax.text(0.501, 0.556, "免费", fontsize=10.4, color=RED, weight="bold",
            ha="center", va="center")

    ax.text(0.030, 0.140,
            "免费的是「够用」：六国普通用户拿到 Hydrogen；付费档在同一功能上升级到 11 月 18 日发布的 Neon。",
            fontsize=9.2, color=SLATE, ha="left", va="center")

    punchline(fig, "门槛不是降了一点，是对六个国家的所有用户都不再存在。")
    footer(fig, "事实：Google 官方博客 11-17、9to5Google 11-17、The Verge 11-17、"
                "ITmedia 11-19 关于档位与机型的记述｜制图：本文")
    fig.savefig(OUT + "图1_从订阅墙里搬出来.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("不是一条旗舰打天下，是三层同时铺",
               "2026 年 11 月 17—18 日｜OpenAI 发 Astra 与 Sol，Google 发 Neon")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    lanes = [
        (0.760, "最难的一档", "贵，慢，啃硬骨头", SLATE,
         [("Carbon", "Google", "最深、最长周期，复杂工程与科研"),
          ("Astra", "OpenAI", "面向最难的项目与前沿判断")]),
        (0.500, "中间地带", "11 月 18 日才出现的一档", RED,
         [("Neon", "Google｜$3 / $15 每百万 token", "接近 Carbon 的质量，速度更快、更便宜")]),
        (0.240, "日常高频", "便宜，量大，跑得多", NAVY,
         [("Sol", "OpenAI", "日常编码、写作与多步骤工作流"),
          ("Hydrogen", "Google", "日常快速执行，免费档 Tasks 就跑它")]),
    ]

    for y, lane, note, color, cards in lanes:
        ax.text(0.030, y + 0.048, lane, fontsize=11.0, color=color,
                weight="bold", ha="left", va="center")
        ax.text(0.030, y - 0.008, note, fontsize=8.4, color=GRAY, ha="left",
                va="center")
        ax.plot([0.030, 0.960], [y - 0.092, y - 0.092], color=LIGHT,
                linewidth=0.8)
        for i, (name, owner, desc) in enumerate(cards):
            x = 0.255 + i * 0.360
            ax.add_patch(FancyBboxPatch((x, y - 0.080), 0.330, 0.170,
                                        boxstyle="round,pad=0.008",
                                        facecolor="white", edgecolor=LIGHT,
                                        linewidth=1.0))
            ax.add_patch(Rectangle((x, y + 0.084), 0.330, 0.005,
                                   facecolor=color, edgecolor="none"))
            ax.text(x + 0.024, y + 0.036, name, fontsize=12.4, color=DARK,
                    weight="bold", ha="left", va="center")
            ax.text(x + 0.024, y - 0.010, owner, fontsize=8.2, color=GRAY,
                    ha="left", va="center")
            ax.text(x + 0.024, y - 0.048, desc, fontsize=8.4, color=SLATE,
                    ha="left", va="center")

    ax.text(0.030, 0.118,
            "Gemini 4 系列此前已有 Argon、Carbon、Hydrogen，Neon 是第四款，"
            "多家媒体记为“一个月内第四款”。",
            fontsize=9.0, color=SLATE, ha="left", va="center")

    punchline(fig, "四款里有三款不是「最强」，而是「够用且更便宜」——这才是这两天的重点。")
    footer(fig, "事实：三档定位据 OpenAI 11-17 公告、Google 11-18 公告与 The Verge、"
                "the-decoder 11-18 报道｜分层为作者归纳｜制图：本文")
    fig.savefig(OUT + "图3_三层同时铺.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("敢免费，是因为它跑在你的机器里",
               "Tasks 在 Google Cloud Agent Compute Engine 上，为每个账号开一台专属的硬件隔离虚拟机")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    steps = [
        ("① 交办", "用一句话把事交出去"),
        ("② 追问", "指令含糊时先问清"),
        ("③ 执行", "专属隔离虚拟机内跑多步骤"),
        ("④ 确认", "付款等敏感操作须本人点头"),
        ("⑤ 交付", "结果回到对话里"),
    ]

    xs = [0.106, 0.303, 0.500, 0.697, 0.894]
    for (head, note), x in zip(steps, xs):
        color = RED if head.startswith("④") else NAVY
        ax.add_patch(FancyBboxPatch((x - 0.078, 0.605), 0.156, 0.130,
                                    boxstyle="round,pad=0.010",
                                    facecolor="white", edgecolor=color,
                                    linewidth=1.1))
        ax.text(x, 0.670, head, fontsize=10.6, color=color, weight="bold",
                ha="center", va="center")
        ax.text(x, 0.560, note, fontsize=8.6, color=GRAY, ha="center",
                va="center", linespacing=1.6)

    for i in range(4):
        ax.add_patch(FancyArrowPatch((xs[i] + 0.082, 0.670),
                                     (xs[i + 1] - 0.082, 0.670),
                                     arrowstyle="-|>", mutation_scale=13,
                                     color=LIGHT, linewidth=1.4))

    ax.plot([0.030, 0.970], [0.470, 0.470], color=LIGHT, linewidth=0.9)
    ax.text(0.030, 0.404, "隔离与风控", fontsize=8.8, color=GRAY, ha="left",
            va="center")

    guards = [
        ("专属", "每账号一台，不与他人共享"),
        ("沙盒", "安全红队定期测试"),
        ("防注入", "对提示注入有专门保护"),
        ("Safe Browsing", "浏览网页时启用"),
    ]
    gx = 0.150
    for name, note in guards:
        ax.text(gx, 0.340, name, fontsize=9.8, color=NAVY, weight="bold",
                ha="left", va="center")
        ax.text(gx, 0.286, note, fontsize=8.6, color=SLATE, ha="left",
                va="center")
        gx += 0.213

    ax.text(0.030, 0.180,
            "免费不改变风险边界：危险操作仍要用户确认，不确定的指令仍会被追问。"
            "Google 的说法是，这套沙盒只是纵深防御里的一层。",
            fontsize=9.0, color=SLATE, ha="left", va="center")

    punchline(fig, "免费的前提不是大方，是可控——把执行关进一台只属于你的机器。")
    footer(fig, "事实：执行环境与风控据 Google 官方博客 11-17、"
                "9to5Google 11-17、Thurrott 11-18｜制图：本文")
    fig.savefig(OUT + "图2_敢免费的底气.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)
