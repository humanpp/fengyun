# -*- coding: utf-8 -*-
"""
《说 AI 危险的人，卖的是闭源 API；推开放权重的人，靠的不再是开源》配套图表

事实口径（逐条可指回）：
  · 2026-11-16，@vikktorrrre 在 X 发一段视频（1,943,202 次浏览）；11-22
    07:57 UTC，@huxlab 引用该视频发文，称阿莫代在国会听证上说开放模型
    走向"非常危险的道路"。同日 17:06 UTC，杨立昆（Yann LeCun）回复：
    "Dario's spiel since GPT-2 has always been about hyping the dangers
    so that open models would be made illegal and he would stay in
    control." / "He left OpenAI because he wasn't going to have control."
    / "It's like the Ottoman Empire banning the printing press for Arabic
    so they would keep in control of the dogma." / "It's a new form of
    medieval obscurantism."（据 CellCog 2026-11-23 逐字记录与截图、
    IT之家 2026-11-25、TechNews 2026-11-25 等转述）
  · 该视频出自 2023-07-25 美国参议院司法委员会"隐私、技术与法律"小组
    委员会听证《Oversight of A.I.: Principles for Regulation》
    （GovInfo 编号 CHRG-118shrg53503）。原答复比片段更完整：阿莫代说
    "in most scientific fields, open source is a good thing"，并称当时
    已发布的开放模型"风险相对有限"，他担心的是未来更大的模型。
    该答复中他并未主张禁止开放模型。
  · 2026-11-25，阿莫代在 X 发长文（约千词）回应"应把人类自由意志交给
    AI"的说法："No, I do not believe that we should 'surrender human
    free will' to AI systems, and it's absurd to suggest that I do."
    文中称"turning over governance to AI is a terrible idea"，并批评
    部分同行"vibes-based commercial and political positioning"，只重复
    "human control and agency"、"AI should be just a tool"等口号。
  · 《华尔街日报》2026-11-21 刊出阿莫代兄妹（Dario 与 Daniela）人物
    特写，其中提到他在 OpenAI 任职期间，曾在内部讨论中提出沉浸式电子
    游戏或许能缓解"AI 导致失业所引发的政治冲突"。该说法出自内部 Slack
    讨论，非正式政策提案（The Verge 2026-11-22、India Today、
    GamesRadar+、IBTimes 等转述）。
  · Anthropic 2026 年上市（纳斯达克，代码 ANT），IPO 募资 810 亿美元、
    估值 1.5 万亿美元（路透，经 Investing.com 转述）。修订后的招股书
    显示：2026 年前九个月营收 332.4 亿美元（上年同期 25 亿美元），
    第三季度营收约 170 亿美元；截至 10 月 31 日的年化收入约 810 亿
    美元（CNBC 2026-11-02、Reuters/Investing.com 2026-11-18）。
    据 Investopedia 对招股书的口径，其收入近五分之四来自按用量计费的
    API 消费，其余为订阅（Pro / Max / Team / 企业席位）。
  · 杨立昆现为 AMI Labs 创始人兼主席，纽约大学教授，曾任 Meta 首席
    AI 科学家（据其 X 个人简介与公开报道）；Meta 于 2026-08 发布开放
    权重模型 Muse Glimmer（纽约时报中文网 2026-08-11）。
  · 2026-11-21 Novara Media 播出、迈克尔·沃克发布的访谈中，物理学家
    马克斯·泰格马克称"和 Anthropic 的员工喝几杯之后，话题常会转向
    推翻美国政府"；该说法无具名、无文件、Anthropic 未确认。同周末
    Anthropic 另有一份 92 人联署的声明称其"不是一家安全的 AI 公司"。
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

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
    fig.text(0.045, Y_FOOT, text, fontsize=7.4, color=GRAY,
             ha="left", va="bottom")


def punchline(fig, text):
    fig.text(0.045, Y_PUNCH, text, fontsize=10.4, color=DARK,
             ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


def card(ax, x, y, w, h, edge, face="white", lw=1.0, z=2):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.004,rounding_size=0.012",
        facecolor=face, edgecolor=edge, linewidth=lw, zorder=z))


def new_axes(fig):
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return ax


# ---------------------------------------------------------------- 图 1
def fig1():
    """三个年份，四句话，一场错位"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "三个年份，四句话，一场错位",
           "被反驳的那句话是 2023 年说的，反驳发在 2026 年")

    rows = [
        ("2023.07.25", "阿莫代 参议院听证",
         "「开放模型正走向一条非常危险的道路」",
         "完整答复里他说：多数科学领域里开源是好事，当时的开放模型风险相对有限。", NAVY),
        ("2026.11.16", "旧视频被重新上传",
         "3 年后的这条发言，被剪成 15 秒",
         "该片段在 X 上获得 194 万次浏览，多数转发未标注日期。", GRAY),
        ("2026.11.22", "杨立昆 回复（17:06 UTC）",
         "「从 GPT-2 起他就在炒作危险，好让开放模型被定为非法」",
         "他补了两句：此人离开 OpenAI 是因为拿不到控制权；这是「一种新的中世纪蒙昧主义」。", RED),
        ("2026.11.25", "阿莫代 千字长文回应",
         "「说我要把自由意志交给 AI，既荒谬也不符合我的文字」",
         "他同时批评部分同行「靠氛围做商业和政治定位」，只喊口号不改产品。", TEAL),
    ]

    y = 0.780
    for date, who, quote, note, color in rows:
        card(ax, 0.045, y - 0.150, 0.910, 0.132, color, lw=1.2)
        ax.text(0.065, y - 0.042, date, fontsize=8.4, color=color,
                weight="bold", ha="left", va="center", zorder=7)
        ax.text(0.165, y - 0.042, who, fontsize=8.8, color=DARK,
                weight="bold", ha="left", va="center", zorder=7)
        ax.text(0.065, y - 0.080, quote, fontsize=8.4, color=DARK,
                ha="left", va="center", zorder=7)
        ax.text(0.065, y - 0.118, note, fontsize=7.3, color=SLATE,
                ha="left", va="center", zorder=7)
        y -= 0.155

    punchline(fig, "争论的每个字都能查到原文，唯独时间对不上。")
    footer(fig, "事实来源：美参议院司法委员会 2023-07-25 听证记录（GovInfo CHRG-118shrg53503）；"
                "@vikktorrrre 2026-11-16、@huxlab 2026-11-22、杨立昆 2026-11-22 17:06 UTC 的 X 帖；"
                "阿莫代 2026-11-25 X 长文。")
    fig.savefig(OUT + "图1_三个年份四句话.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """同一周的两条指控，证据强度不同"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "两条指控，两种证据强度",
           "一条可查原文与完整答复，一条只有转述")

    # 表头
    ax.text(0.045, 0.812, "指控", fontsize=9.0, color=GRAY,
            ha="left", va="center")
    ax.text(0.300, 0.812, "证据形态", fontsize=9.0, color=GRAY,
            ha="left", va="center")
    ax.text(0.640, 0.812, "可核实到什么程度", fontsize=9.0, color=GRAY,
            ha="left", va="center")
    ax.text(0.885, 0.812, "判定", fontsize=9.0, color=GRAY,
            ha="left", va="center")
    ax.plot([0.045, 0.955], [0.795, 0.795], color=LIGHT, linewidth=1.0)

    rows = [
        ("杨立昆：阿莫代\n炒作危险以压制开源",
         "公开发言原文\n+ 完整听证记录",
         "视频确有其事；但完整答复中\n他说开源在多数领域是好事，\n并未主张禁止",
         "动机不可证", RED),
        ("泰格马克：Anthropic 员工\n酒后谈论推翻政府",
         "播客转述的\n私下对话",
         "无具名、无日期、无文件；\nAnthropic 未确认；\n该访谈属媒体访谈",
         "不可核实", GRAY),
        ("阿莫代：同行只喊\n「人类控制」口号",
         "各家公开产品\n与招股书",
         "他自家产品同样在\n推进任务自动化；\n批评与自辩指向同一处",
         "双向适用", NAVY),
    ]

    y = 0.720
    for claim, evid, verify, verdict, color in rows:
        ax.text(0.045, y, claim, fontsize=8.0, color=DARK, ha="left",
                va="top", linespacing=1.8)
        ax.text(0.300, y, evid, fontsize=7.6, color=SLATE, ha="left",
                va="top", linespacing=1.8)
        ax.text(0.640, y, verify, fontsize=7.6, color=SLATE, ha="left",
                va="top", linespacing=1.8)
        ax.text(0.890, y, verdict, fontsize=8.0, color=color, weight="bold",
                ha="left", va="top")
        y -= 0.150
        ax.plot([0.045, 0.955], [y + 0.030, y + 0.030], color=LIGHT,
                linewidth=0.8)

    # 底部提醒（放在表格线之下，不压内容）
    card(ax, 0.045, 0.168, 0.910, 0.078, LIGHT, face=PALE, lw=1.0)
    ax.text(0.065, 0.220,
            "同一周里，前两条被当成「AI 圈的互撕」传播，第三条被当成「阿莫代的反击」传播；",
            fontsize=8.0, color=DARK, ha="left", va="center", zorder=7)
    ax.text(0.065, 0.188,
            "但它们的证据强度并不一样，能核实到的层次也不一样。",
            fontsize=8.0, color=DARK, ha="left", va="center", zorder=7)

    punchline(fig, "在判断一句话对不对之前，先看它能被核实到什么程度。")
    footer(fig, "事实来源：CellCog 2026-11-23（逐条标注「已显示」与「仅有主张」）；Novara Media 2026-11-21 访谈；"
                "阿莫代 2026-11-25 X 长文；Anthropic 2026 年招股书（经 CNBC、Investopedia 转述）。")
    fig.savefig(OUT + "图2_指控与证据强度.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """Anthropic 的钱从哪来"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "Anthropic 的钱，主要来自按用量计费的 API",
           "招股书口径：近五分之四收入属于消费型计费")

    base_y = 0.340
    total_h = 0.300

    # 左侧份数示意
    api_w = 0.560 * 0.79
    sub_w = 0.560 - api_w
    ax.add_patch(Rectangle((0.045, base_y), api_w, total_h,
                           facecolor=NAVY, edgecolor=NAVY, linewidth=1.0,
                           zorder=3))
    ax.add_patch(Rectangle((0.045 + api_w, base_y), sub_w, total_h,
                           facecolor=GRAY, edgecolor=GRAY, linewidth=1.0,
                           zorder=3))
    ax.text(0.045 + api_w / 2, base_y + total_h / 2, "API 按用量计费\n约 79%",
            fontsize=10.0, color="white", weight="bold", ha="center",
            va="center", zorder=6, linespacing=1.7)
    ax.text(0.045 + api_w + sub_w / 2, base_y + total_h / 2, "订阅\n约 21%",
            fontsize=8.6, color="white", weight="bold", ha="center",
            va="center", zorder=6, linespacing=1.7)

    ax.plot([0.045, 0.605], [base_y, base_y], color=SLATE, linewidth=1.2)
    ax.text(0.045, base_y - 0.034,
            "来源：Anthropic 修订版招股书，2026 年前九个月口径；比例为约数。",
            fontsize=7.4, color=GRAY, ha="left", va="top")

    # 右侧数字
    stats = [
        ("332.4", "亿美元", "2026 年前九个月营收（上年同期 25 亿）", NAVY),
        ("810", "亿美元", "截至 2026-10-31 的年化收入", NAVY),
        ("810", "亿美元", "IPO 募资额，估值 1.5 万亿美元", RED),
    ]
    y = 0.700
    for val, unit, label, color in stats:
        ax.text(0.640, y, val, fontsize=17.0, color=color, weight="bold",
                ha="left", va="center")
        ax.text(0.790, y + 0.006, unit, fontsize=8.4, color=color,
                ha="left", va="center")
        ax.text(0.640, y - 0.036, label, fontsize=7.6, color=SLATE,
                ha="left", va="center")
        y -= 0.115

    # 说明
    card(ax, 0.640, 0.150, 0.315, 0.240, LIGHT, lw=1.0)
    ax.text(0.658, 0.360, "为什么这组数字重要", fontsize=8.2, color=DARK,
            weight="bold", ha="left", va="center", zorder=7)
    ax.plot([0.658, 0.936], [0.342, 0.342], color=LIGHT, linewidth=0.9, zorder=7)
    ax.text(0.658, 0.318,
            "按用量计费意味着，每一次\n"
            "推理都在别人的服务器上跑。\n"
            "而本地可运行的开放权重\n"
            "模型，不产生这笔计量。",
            fontsize=7.4, color=SLATE, ha="left", va="top", zorder=7,
            linespacing=1.9)

    punchline(fig, "一个靠「计量」收钱的公司，和一个靠「许可」收钱的公司，对开放的态度不会一样。")
    footer(fig, "事实来源：Anthropic 修订版招股书（2026-11-02，经 CNBC 转述；收入结构经 Investopedia 转述）；"
                "IPO 募资与估值据路透（经 Investing.com 2026-11-18 转述）。")
    fig.savefig(OUT + "图3_Anthropic收入结构.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)
