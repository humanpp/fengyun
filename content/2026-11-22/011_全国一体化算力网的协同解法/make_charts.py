# -*- coding: utf-8 -*-
"""
《算力网升格为国家基础设施之后：一张"系统协同"的答卷怎么答》配套图表

事实口径：

一、政策层面
  · 2026 年 4 月 28 日，中共中央政治局会议明确提出加强水网、新型电网、算力网、
    新一代通信网、城市地下管网、物流网等「六张网」规划建设。
  · 2026 年 5 月 22 日国家发展改革委表示，将抓紧出台「六张网」相关规划和实施方案，
    进一步统筹建设内容、明确各领域投资重点、将目标任务分解到年度、明确时间
    和进度安排；新型电网与城市地下管网「十五五」时期投资预计均达 5 万亿元左右。
    （中国政府网 2026-05-22，来源央视网）
  · 2026 年 3 月 6 日十四届全国人大四次会议经济主题记者会上，国家发改委主任
    郑栅洁表示，今年将在「六张网」和重点领域建设上投入超过 7 万亿元。（界面新闻）

二、中国移动的算力网络运营数据（2025 年年度业绩，2026-03-26 公布）
  · 智算总规模 92.5 EFLOPS（FP16，含自建及租赁），实现百卡至超万卡全规格计算能力。
  · 完善城域 1 毫秒、省域 5 毫秒、全国 20 毫秒三级算力时延圈。
  · 省际骨干 400G OTN 网络基本覆盖全国。
  · 对外服务 IDC 标准机架超 150 万架（标准机架按单个机架 2.5KW 折合）。
  · 智算训练全国中心节点和区域中心节点基本覆盖国家八大枢纽。
  · 2025 年算力服务收入 898 亿元，同比增长 11.1%；数据中心收入同比增长 8.7%，
    其中 AIDC 收入同比增长 35.4%；智算服务收入增速 279%，拉动云算服务收入
    同比增长 13.9%。（央广网 2026-03-26）

三、算网调度与协同（2026 年公开披露）
  · 2026-05-08 移动云大会发布「全国一体化算力网技术创新体系」：
    构建「N+31+X」算力布局与智算中心 SPEC 全栈技术体系；
    400G 算力光网与 320+ 城市算力网络；算网智脑实现资源一体化纳管，
    八大算力枢纽端到端时延降至 12 毫秒；网络能力开放超 2900 项。
    （新华网 2026-05-09）
  · 2026-09-12 中国算力大会：AIDC 总签约规模超 7GW；自研「算网大脑」纳管合作算力，
    落地 8 个国家级、枢纽级、区域级平台，承建国家算力互联互通河北区域节点；
    MoMA 平台汇聚超 340 款主流模型、实现 0day 首发接入。（新华网 2026-09-12）
  · 2026-11 移动网络大会：算网大脑 4.0 升级，迈入算、网、智、电一体化调度；
    纳管全网算力资源及 25 万余条网络链路，构建分钟级刷新的算网全景地图；
    首次「算力集群跨时空协同调控」示范验证——南网广州至贵州算力任务跨省迁移
    用时 5 分 44 秒，国网福建到宁夏上百卡任务 15 分钟内完成迁移；
    已支撑长三角、京津冀等 6 个国家枢纽节点和 10 余个省市级算力调度平台建设；
    在工信部「1+M+N」算力互联互通专项中支撑 13 个省份申报并中选。
    （新浪财经 2026-11-10 转载报道，需注明为媒体报道口径）
  · 截至 2026 年 9 月底，我国智能算力规模达 2592 EFLOPS，同比增长 146%
    （工业和信息化部披露，转引自上述报道）。

风格：克制传媒风，白底、低饱和配色、标题即结论
输出目录 = 脚本所在目录
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle

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
AMBER = "#9a7b4f"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep

Y_TITLE = 0.962
Y_SUB = 0.912
Y_PUNCH = 0.052
Y_FOOT = 0.014

Q_L = "\u300c"
Q_R = "\u300d"


def header(fig, title, sub):
    fig.text(0.040, Y_TITLE, title, fontsize=18.5, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.040, Y_SUB, sub, fontsize=10.2, color=GRAY,
             ha="left", va="top")


def footer(fig, text):
    fig.text(0.040, Y_FOOT, text, fontsize=7.2, color=GRAY,
             ha="left", va="bottom")


def punchline(fig, text):
    fig.text(0.040, Y_PUNCH, text, fontsize=10.0, color=DARK,
             ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.65", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


def card(ax, x, y, w, h, edge, face="white", lw=1.0, z=2):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.003,rounding_size=0.012",
        facecolor=face, edgecolor=edge, linewidth=lw, zorder=z))


def new_axes(fig):
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return ax


# ---------------------------------------------------------------- 图 1
def fig1():
    """六张网里的两张"""
    fig = plt.figure(figsize=(13.2, 7.4))
    ax = new_axes(fig)

    header(fig, "六张网里，有两张叫「算力」和「通信」",
           "2026 年 4 月中央政治局会议明确六张网规划建设；两张数字基础设施被纳入国家骨架")

    nets = [
        ("水网", "六大之一", GRAY, False),
        ("新型电网", "六大之一", GRAY, False),
        ("算力网", "本次聚焦", RED, True),
        ("新一代通信网", "本次聚焦", RED, True),
        ("城市地下管网", "六大之一", GRAY, False),
        ("物流网", "六大之一", GRAY, False),
    ]

    x = 0.040
    w = 0.145
    gap = 0.0125
    for name, tag, color, hi in nets:
        h = 0.300 if hi else 0.230
        y = 0.400
        card(ax, x, y, w, h, color if hi else LIGHT,
             face="white" if hi else "#f7f8f9", lw=1.8 if hi else 1.0)
        ax.text(x + w / 2, y + h - 0.062, tag, fontsize=7.6,
                color=color if hi else GRAY, ha="center", va="center",
                zorder=6)
        ax.text(x + w / 2, y + h / 2 - 0.034, name, fontsize=11.2,
                color=color if hi else SLATE,
                weight="bold" if hi else "normal",
                ha="center", va="center", zorder=6)
        x += w + gap

    ax.text(0.040, 0.352,
            "红色两张即自动化基础设施网络；六张网同期统筹、规划一并出台。",
            fontsize=9.2, color=SLATE, ha="left", va="center")

    # 关键数字横排
    stats = [
        ("超 7 万亿", "2026 年六张网及\n重点领域投资规模（元）", NAVY),
        ("5 万亿左右", "新型电网「十五五」\n投资预计（元）", SLATE),
        ("2592 EFLOPS", "截至 2026 年 9 月底\n全国智能算力规模", RED),
    ]
    x = 0.040
    for num, label, color in stats:
        ax.text(x, 0.240, num, fontsize=19.5, color=color, weight="bold",
                ha="left", va="center")
        ax.text(x, 0.170, label, fontsize=8.2, color=GRAY,
                ha="left", va="top", linespacing=1.60)
        x += 0.320

    punchline(fig, "算力网从「信息化项目」变成「国家级基础设施」，这一步的意义不亚于建了多少卡。")
    footer(fig, "事实来源：中共中央政治局会议（2026-04-28）；国家发展改革委（2026-05-22，"
                "中国政府网）；界面新闻 2026-05-27；工业和信息化部披露数据（转引自 2026-11-10 报道）")
    fig.savefig(OUT + "图1_六张网.png", dpi=160)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """三级时延圈 + 三个数字"""
    fig = plt.figure(figsize=(13.2, 7.4))
    # 用等比例坐标系画圆，避免变成椭圆
    ax = fig.add_axes([0.035, 0.10, 0.46, 0.74])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("equal")
    ax.axis("off")

    header(fig, "1 毫秒、5 毫秒、20 毫秒：三级算力时延圈",
           "时延圈是算力网的「站间距」——圈越密，能放进圈里的业务越多")

    cx, cy = 0.500, 0.500
    rings = [
        (0.440, "全国 20 毫秒", NAVY, "#f2f5f7"),
        (0.310, "省域 5 毫秒", TEAL, "#e9eef0"),
        (0.170, "城域 1 毫秒", RED, "#fdf4f3"),
    ]
    for r, label, color, face in rings:
        ax.add_patch(Circle((cx, cy), r, facecolor=face, edgecolor=color,
                            linewidth=1.8, zorder=2))

    ax.text(cx, cy + 0.030, "算力", fontsize=10.5, color=DARK,
            weight="bold", ha="center", va="center", zorder=6)
    ax.text(cx, cy - 0.048, "需求方", fontsize=7.4, color=GRAY,
            ha="center", va="center", zorder=6)

    # 标签放在各环顶部外侧，不压线
    tags = [
        (0.170, "城域 1ms", RED, 0.040),
        (0.310, "省域 5ms", TEAL, 0.040),
        (0.440, "全国 20ms", NAVY, 0.040),
    ]
    for r, txt, color, off in tags:
        ax.text(cx, cy + r + off, txt, fontsize=8.6, color=color,
                weight="bold", ha="center", va="bottom", zorder=7)

    # 右侧：支撑这张圈的三组数字（独立坐标系）
    ax2 = new_axes(fig)

    ax2.text(0.545, 0.760, "支撑这三级时延圈的三组数字", fontsize=10.0,
             color=GRAY, ha="left", va="center")
    ax2.plot([0.545, 0.962], [0.736, 0.736], color=LIGHT, linewidth=1.0)

    rows = [
        ("92.5 EFLOPS", "智算总规模（FP16，含自建及租赁）", NAVY),
        ("超 150 万架", "对外服务 IDC 标准机架（按 2.5KW 折合）", TEAL),
        ("12 毫秒", "八大算力枢纽端到端时延", RED),
    ]
    y = 0.676
    for num, label, color in rows:
        ax2.text(0.545, y, num, fontsize=16.5, color=color, weight="bold",
                 ha="left", va="center")
        ax2.text(0.545, y - 0.048, label, fontsize=8.4, color=GRAY,
                 ha="left", va="center")
        y -= 0.140

    card(ax2, 0.545, 0.168, 0.417, 0.108, LIGHT, face=PALE, lw=1.0)
    ax2.text(0.565, 0.240, "320+ 城市算力网络", fontsize=9.4, color=NAVY,
             weight="bold", ha="left", va="center", zorder=6)
    ax2.text(0.565, 0.198,
             "400G 算力光网 + G-SRv6 智能化互联网，\n省际骨干基本覆盖全国。",
             fontsize=8.0, color=SLATE, ha="left", va="center",
             linespacing=1.55, zorder=6)

    punchline(fig, "时延圈不是技术指标，是「哪些业务能落在哪」的地理边界。")
    footer(fig, "事实来源：中国移动 2025 年年度业绩（2026-03-26，央广网）；"
                "全国一体化算力网技术创新体系发布（2026-05-08，新华网 2026-05-09）")
    fig.savefig(OUT + "图2_三级时延圈.png", dpi=160)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """算网大脑：从内部中枢到社会级底座"""
    fig = plt.figure(figsize=(13.2, 7.4))
    ax = new_axes(fig)

    header(fig, "算网大脑 4.0：把「算、网、智、电」放进同一个调度台",
           "2026 年 11 月升级亮相，定位从内部调度中枢转为社会级算力底座")

    # 四层结构
    layers = [
        ("应用层", "Token 调度", "在基础模型、自有集群、第三方 Token 服务之间\n按成本与性能自动匹配最优解", RED, 0.560),
        ("智能层", "算智协同", "模型与数据就近部署、高效分发；\nMoMA 节点小时级上线", AMBER, 0.440),
        ("调度层", "算网一体", "纳管全网算力资源及 25 万余条网络链路；\n分钟级刷新的算网全景地图", NAVY, 0.320),
        ("能源层", "算电协同", "算力任务跨省迁移：广州至贵州 5 分 44 秒，\n福建至宁夏上百卡 15 分钟内", TEAL, 0.200),
    ]

    for name, tag, detail, color, y in layers:
        card(ax, 0.040, y, 0.600, 0.098, color, lw=1.4)
        ax.text(0.058, y + 0.070, name, fontsize=9.4, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(0.058, y + 0.032, tag, fontsize=8.2, color=DARK,
                ha="left", va="center", zorder=6)
        ax.text(0.230, y + 0.049, detail, fontsize=8.0, color=SLATE,
                ha="left", va="center", linespacing=1.55, zorder=6)

    # 左侧层级箭头
    ax.annotate("", xy=(0.022, 0.610), xytext=(0.022, 0.240),
                arrowprops=dict(arrowstyle="-|>", color=GRAY,
                                linewidth=1.4))

    # 右侧：覆盖范围
    ax.text(0.680, 0.740, "已经铺到哪", fontsize=10.0, color=GRAY,
            ha="left", va="center")
    ax.plot([0.680, 0.960], [0.716, 0.716], color=LIGHT, linewidth=1.0)

    reach = [
        ("6", "个国家枢纽节点\n（长三角、京津冀等）"),
        ("10 余", "个省市级\n算力调度平台"),
        ("13", "个省份在工信部\n「1+M+N」专项中选"),
    ]
    y = 0.650
    for num, label in reach:
        ax.text(0.680, y, num, fontsize=17.0, color=NAVY, weight="bold",
                ha="left", va="center")
        ax.text(0.760, y + 0.014, label, fontsize=8.0, color=SLATE,
                ha="left", va="center", linespacing=1.55)
        y -= 0.115

    card(ax, 0.680, 0.196, 0.280, 0.166, RED, face="white", lw=1.4)
    ax.text(0.698, 0.330, "一句定性", fontsize=9.0, color=GRAY,
            ha="left", va="center", zorder=6)
    ax.text(0.698, 0.292,
            "从企业内部调度中枢，\n到服务全社会的算力底座。",
            fontsize=8.8, color=DARK, ha="left", va="top",
            linespacing=1.80, zorder=6)

    punchline(fig, "单点性能有差距时，能比的只剩系统协同——这正是「一张网」的价值所在。")
    footer(fig, "事实来源：2026 移动网络大会算网大脑 4.0 升级（新浪财经 2026-11-10 转载报道）；"
                "2026 中国算力大会（新华网 2026-09-12）")
    fig.savefig(OUT + "图3_算网大脑.png", dpi=160)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)
