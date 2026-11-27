# -*- coding: utf-8 -*-
"""
《5.2 万卡、257.88 亿、1323 亿美元：算力的瓶颈换了地方》配套图表

事实口径：

一、中国移动第二批超节点集采（2026-11-20 发布招标公告）
  · 采购人工智能超节点合计 52160 卡，不划分标包，计划选取 6—7 家中标人，
    投标截止 2026-12-14。
  · 公告未披露金额，但设最高投标限价；每家须对每个配置承诺至少 30% 的供货量。
  · 第一批（2026-09-29 发标，10-28 公示）：20480 卡，5 家中标
    （华鲲振宇、宝德、华启智慧、百信、神州鲲泰），投标报价集中在不含税
    115.99 亿—117.02 亿元，平均单卡约 57 万元，份额 30%/25%/20%/15%/10%，
    交货期 30 天。第一批配 448 台 RoCE 交换机、82 套存储
    （其中 72 套智算、10 套分布式）。
  · 两批累计 72640 卡（20480 + 52160）。按第一批不含税均价静态测算，
    第二批对应约 297 亿元，接近 300 亿元（非公告金额）。

二、中国电信智算超节点（N 系列）集采（2026-11-16 公告）
  · 最高投标限价 257.88 亿元（含税），合同有效期至 2027 年底。
  · 采购智算服务器 5248 台，另配 110 台高性能存储、374 台 RoCE 交换机；
    集成、调优、测试验证打包在内；最多 5 家中标，投标截止 2026-12-07。
  · 份额规则：有效投标人 6 家以上，5 名中标人按 30%/25%/20%/15%/10%；
    有效投标人 2—3 家，按 70%/30%。
  · 约束条款：第二名评标价低于第一名九折时，份额改为 60%/40%；
    中标产品须通过中国电信组织的集群联调性能测试，不达标不予供货。
  · 机型：一套撑 1024 卡集群，一套撑 256 卡；统一冷板液冷；网络侧要求 800G RoCE。
  · 口径提示：中国移动第一批披露为不含税报价，中国电信本次为含税限价，
    两者不可直接相加或比较。

三、戴尔 2027 财年第三季度（2026-11-24 发布，季度截至 2026-10-30）
  · 净营收 549.37 亿美元（同比 +103%）；摊薄每股收益 8.82 美元（+287%）。
  · ISG（基础设施解决方案集团）营收 419.74 亿美元（+198%）；
    其中 AI 优化服务器营收 220.31 亿美元（+291%）；
    传统服务器与网络 150.13 亿美元（+235%）；存储 49.30 亿美元（+24%）。
  · 本季新增 AI 服务器订单 602 亿美元；期末 AI 订单积压达 1323 亿美元（历史纪录）。
  · 全年 FY27 营收指引 2020 亿美元（+78%）；AI 优化服务器全年指引 780 亿美元（+216%）。
  · 副董事长兼 COO Jeff Clarke 表述：订单「每一项都严格审核客户质量以及获得
    资金、土地和电力的能力」；「我们在发货前测试完整机架，交付后六小时内完成上线，
    从而缩短首次出词时间」；超过 7500 家客户在部署 Dell AI Factory。
  据戴尔科技官方新闻稿（2026-11-24）。

风格：克制传媒风，编辑排版
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
plt.rcParams["savefig.facecolor"] = "white"

INK = "#1a2332"
NAVY = "#1b3a5c"
RED = "#b0413e"
TEAL = "#2f6b64"
GOLD = "#9a7b3f"
MUTED = "#7b8494"
HAIR = "#dfe3e8"
WASH = "#f4f6f8"
WHITE = "#ffffff"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep
Q_L, Q_R = "\u300c", "\u300d"


def new_axes(fig):
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return ax


def head(fig, ax, kicker, title, sub, color):
    ax.add_patch(Rectangle((0.042, 0.928), 0.0075, 0.040,
                           facecolor=color, edgecolor="none", zorder=9))
    ax.text(0.058, 0.950, kicker, fontsize=9.2, color=color,
            weight="bold", ha="left", va="center", zorder=9)
    ax.text(0.042, 0.900, title, fontsize=21, color=INK, weight="bold",
            ha="left", va="top", zorder=9)
    ax.text(0.042, 0.848, sub, fontsize=10.4, color=MUTED,
            ha="left", va="top", zorder=9)
    ax.plot([0.042, 0.958], [0.812, 0.812], color=HAIR, linewidth=1.0,
            zorder=5)


def foot(fig, ax, text):
    ax.plot([0.042, 0.958], [0.058, 0.058], color=HAIR, linewidth=0.9,
            zorder=5)
    ax.text(0.042, 0.028, text, fontsize=7.0, color=MUTED,
            ha="left", va="center", zorder=9)


def outro(fig, ax, text, color=INK):
    ax.add_patch(FancyBboxPatch(
        (0.042, 0.082), 0.760, 0.048,
        boxstyle="round,pad=0.002,rounding_size=0.008",
        facecolor=color, edgecolor="none", zorder=6))
    ax.text(0.062, 0.106, text, fontsize=10.2, color=WHITE,
            ha="left", va="center", zorder=9)


def panel(ax, x, y, w, h, accent, face=WHITE, bar=0.0055, shadow=True):
    if shadow:
        ax.add_patch(FancyBboxPatch(
            (x + 0.0035, y - 0.0035), w, h,
            boxstyle="round,pad=0,rounding_size=0.009",
            facecolor="#e9ecf0", edgecolor="none", zorder=2))
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0,rounding_size=0.009",
        facecolor=face, edgecolor="#e6eaee", linewidth=0.9, zorder=3))
    ax.add_patch(FancyBboxPatch(
        (x, y), bar, h,
        boxstyle="round,pad=0,rounding_size=0.0028",
        facecolor=accent, edgecolor="none", zorder=4))


# ---------------------------------------------------------------- 图 1
def fig1():
    fig = plt.figure(figsize=(13.6, 8.0))
    ax = new_axes(fig)

    head(fig, ax, "两家运营商，两种买法",
         "一个按卡买，一个按台买",
         "5.2 万卡与 257.88 亿元之间，差的不是规模，是规则",
         NAVY)

    # 左：中国移动
    panel(ax, 0.042, 0.220, 0.438, 0.540, NAVY)
    ax.text(0.066, 0.712, "中国移动", fontsize=13.0, color=NAVY,
            weight="bold", ha="left", va="center", zorder=9)
    ax.text(0.066, 0.674, "第二批超节点集采 · 2026-11-20 发标", fontsize=8.4,
            color=MUTED, ha="left", va="center", zorder=9)
    ax.plot([0.066, 0.456], [0.652, 0.652], color=HAIR, linewidth=1.0)

    mi = [
        ("52160 卡", "本批采购量"),
        ("6—7 家", "计划中标人数（第一批 5 家）"),
        ("7.26 万卡", "两批累计"),
        ("约 300 亿元", "按第一批均价静态测算（非公告金额）"),
        ("12 月 14 日", "投标截止"),
    ]
    y = 0.618
    for num, label in mi:
        ax.text(0.066, y, num, fontsize=13.0, color=NAVY, weight="bold",
                ha="left", va="center", zorder=9)
        ax.text(0.066, y - 0.029, label, fontsize=7.4, color=MUTED,
                ha="left", va="center", zorder=9)
        y -= 0.066

    ax.add_patch(FancyBboxPatch(
        (0.066, 0.234), 0.390, 0.058,
        boxstyle="round,pad=0,rounding_size=0.007",
        facecolor=WASH, edgecolor="none", zorder=6))
    ax.text(0.086, 0.278, "约束：设最高限价 · 每配置承诺 ≥30% 供货",
            fontsize=7.8, color=INK, weight="bold", ha="left",
            va="center", zorder=9)
    ax.text(0.086, 0.250, "第一批交货期 30 天", fontsize=7.4, color=MUTED,
            ha="left", va="center", zorder=9)

    # 右：中国电信
    panel(ax, 0.520, 0.220, 0.438, 0.540, RED)
    ax.text(0.544, 0.712, "中国电信", fontsize=13.0, color=RED,
            weight="bold", ha="left", va="center", zorder=9)
    ax.text(0.544, 0.674, "智算超节点（N 系列）· 2026-11-16 发标", fontsize=8.4,
            color=MUTED, ha="left", va="center", zorder=9)
    ax.plot([0.544, 0.934], [0.652, 0.652], color=HAIR, linewidth=1.0)

    ct = [
        ("257.88 亿元", "最高投标限价（含税）"),
        ("5248 台", "智算服务器"),
        ("110 台 / 374 台", "高性能存储 / RoCE 交换机"),
        ("合同至 2027 年底", "有效期"),
        ("12 月 7 日", "投标截止"),
    ]
    y = 0.618
    for num, label in ct:
        ax.text(0.544, y, num, fontsize=13.0, color=RED, weight="bold",
                ha="left", va="center", zorder=9)
        ax.text(0.544, y - 0.029, label, fontsize=7.4, color=MUTED,
                ha="left", va="center", zorder=9)
        y -= 0.066

    ax.add_patch(FancyBboxPatch(
        (0.544, 0.234), 0.390, 0.058,
        boxstyle="round,pad=0,rounding_size=0.007",
        facecolor=WASH, edgecolor="none", zorder=6))
    ax.text(0.564, 0.278, "约束：九折线 · 集群联调不过不予供货",
            fontsize=7.8, color=INK, weight="bold", ha="left",
            va="center", zorder=9)
    ax.text(0.564, 0.250, "集成、调优、测试验证打包在内", fontsize=7.4,
            color=MUTED, ha="left", va="center", zorder=9)

    outro(fig, ax, "一个压产能，一个压性能——但都在把系统交付的风险推给厂商。")
    foot(fig, ax, "事实来源：中国移动第二批集采招标公告（2026-11-20）、中国电信 N 系列集采公告"
         "（2026-11-16）；通信产业网 2026-11-25、C114 通信网 2026-11-21")

    fig.savefig(OUT + "图1_两种买法.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(13.6, 8.0))
    ax = new_axes(fig)

    head(fig, ax, "供给侧的对照",
         "1323 亿美元积压：缺口在扩大，不在收窄",
         "戴尔 2027 财年第三季度：单季新增订单 602 亿美元，期末积压 1323 亿美元",
         GOLD)

    # 三个数字
    ax.text(0.042, 0.762, "戴尔 AI 服务器（2027 财年 Q3，截至 2026-10-30）",
            fontsize=8.6, color=MUTED, ha="left", va="center")
    ax.plot([0.042, 0.958], [0.742, 0.742], color=HAIR, linewidth=1.0)

    stats = [
        ("602 亿美元", "本季新增 AI 服务器订单", RED),
        ("220 亿美元", "本季 AI 服务器确认收入", NAVY),
        ("1323 亿美元", "期末 AI 订单积压（历史纪录）", GOLD),
    ]
    x = 0.042
    w = 0.288
    gap = 0.019
    for num, label, color in stats:
        panel(ax, x, 0.560, w, 0.150, color)
        ax.text(x + 0.024, 0.672, num, fontsize=17.0, color=color,
                weight="bold", ha="left", va="center", zorder=9)
        ax.text(x + 0.024, 0.606, label, fontsize=8.0, color=INK,
                ha="left", va="center", zorder=9)
        x += w + gap

    # 订单 vs 收入 的对比条
    ax.text(0.042, 0.520, "单季新增订单与确认收入的比例", fontsize=8.6,
            color=MUTED, ha="left", va="center")

    total_w = 0.916
    unit = total_w / 602.0
    bar_y = 0.430

    ax.add_patch(FancyBboxPatch(
        (0.042, bar_y), 602 * unit * 0.365, 0.048,
        boxstyle="round,pad=0,rounding_size=0.007",
        facecolor=NAVY, edgecolor="none", zorder=6))
    ax.add_patch(FancyBboxPatch(
        (0.042 + 602 * unit * 0.365, bar_y), 602 * unit * 0.635, 0.048,
        boxstyle="round,pad=0,rounding_size=0.007",
        facecolor="#e3c9a0", edgecolor="none", zorder=6))

    ax.text(0.542, bar_y + 0.070, "本季确认收入 220 亿（37%）", fontsize=8.6,
            color=NAVY, weight="bold", ha="center", va="bottom", zorder=9)
    ax.text(0.800, bar_y + 0.070, "未交付 382 亿（63%）", fontsize=8.6,
            color=GOLD, weight="bold", ha="center", va="bottom", zorder=9)
    ax.text(0.042, bar_y - 0.032,
            "602 亿美元订单中，当季只确认了约 37%。剩下的进入积压。",
            fontsize=8.4, color=INK, ha="left", va="top", zorder=9)

    # 底部：COO 的两句话
    ax.text(0.042, 0.372, "官方表述里最关键的两句", fontsize=8.6,
            color=MUTED, ha="left", va="center")
    ax.plot([0.042, 0.958], [0.354, 0.354], color=HAIR, linewidth=1.0)

    quotes = [
        ("订单审核", "每一项都严格审核客户质量，以及获得资金、土地和电力的能力"),
        ("交付方式", "发货前测试完整机架，交付后六小时内完成上线，缩短首次出词时间"),
    ]
    y = 0.312
    for k, v in quotes:
        ax.add_patch(Circle((0.050, y), 0.0040, facecolor=GOLD,
                            edgecolor="none", zorder=8))
        ax.text(0.064, y, k, fontsize=8.4, color=INK, weight="bold",
                ha="left", va="center", zorder=9)
        ax.text(0.150, y, v, fontsize=8.2, color=MUTED,
                ha="left", va="center", zorder=9)
        y -= 0.056

    ax.text(0.042, 0.196,
            "「审核资金、土地、电力」——这三样恰恰是系统交付的前置条件，不是芯片。",
            fontsize=8.4, color=INK, ha="left", va="center", zorder=9)

    outro(fig, ax, "瓶颈不在有没有 GPU，在能不能把电力、土建、机架和交付一起搞定。")
    foot(fig, ax, "事实来源：Dell Technologies 2027 财年第三季度业绩新闻稿（2026-11-24）")

    fig.savefig(OUT + "图2_供给缺口.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(13.6, 8.0))
    ax = new_axes(fig)

    head(fig, ax, "超节点是什么",
         "买的不再是一台服务器，是一个「域」",
         "几百上千张卡统一编址，远端内存像本地内存一样访问",
         TEAL)

    # 左：传统集群 vs 超节点
    ax.text(0.042, 0.756, "两种组网思路", fontsize=8.6, color=MUTED,
            ha="left", va="center")
    ax.plot([0.042, 0.958], [0.736, 0.736], color=HAIR, linewidth=1.0)

    # 传统：多台服务器 + 网络互联
    panel(ax, 0.042, 0.470, 0.438, 0.230, MUTED)
    ax.text(0.066, 0.664, "传统集群：加法", fontsize=10.4, color=MUTED,
            weight="bold", ha="left", va="center", zorder=9)
    for i in range(4):
        bx = 0.070 + i * 0.088
        ax.add_patch(FancyBboxPatch(
            (bx, 0.594), 0.066, 0.044,
            boxstyle="round,pad=0,rounding_size=0.005",
            facecolor="#c9d0d8", edgecolor="none", zorder=6))
        ax.text(bx + 0.033, 0.616, "8 卡", fontsize=6.8, color="white",
                ha="center", va="center", zorder=9)
    ax.plot([0.070, 0.400], [0.578, 0.578], color=MUTED, linewidth=1.4,
            zorder=5)
    ax.text(0.066, 0.552, "机间用网络连，跨机通信频繁", fontsize=8.0,
            color=INK, ha="left", va="center", zorder=9)
    ax.text(0.066, 0.518, "通信可吃掉训练四成以上时间（第三方测算）", fontsize=7.6,
            color=MUTED, ha="left", va="center", zorder=9)
    ax.text(0.066, 0.488, "思路：修更宽的路", fontsize=7.8, color=MUTED,
            weight="bold", ha="left", va="center", zorder=9)

    # 超节点：统一编址
    panel(ax, 0.520, 0.470, 0.438, 0.230, TEAL)
    ax.text(0.544, 0.664, "超节点：统一编址", fontsize=10.4, color=TEAL,
            weight="bold", ha="left", va="center", zorder=9)
    ax.add_patch(FancyBboxPatch(
        (0.544, 0.578), 0.390, 0.062,
        boxstyle="round,pad=0,rounding_size=0.008",
        facecolor="#e4eeec", edgecolor=TEAL, linewidth=1.2, zorder=6))
    ax.text(0.739, 0.609, "统一编址的内存域", fontsize=8.6, color=TEAL,
            weight="bold", ha="center", va="center", zorder=9)
    ax.text(0.544, 0.552, "几百上千张卡连成一个域，远端像本地", fontsize=8.0,
            color=INK, ha="left", va="center", zorder=9)
    ax.text(0.544, 0.518, "中国电信两套机型：1024 卡 / 256 卡", fontsize=7.6,
            color=MUTED, ha="left", va="center", zorder=9)
    ax.text(0.544, 0.488, "思路：整个车队在一个仓库里调度", fontsize=7.8,
            color=TEAL, weight="bold", ha="left", va="center", zorder=9)

    # 底部：一个超节点包含什么
    ax.text(0.042, 0.418, "所以集采单里，为什么要把这些东西单列", fontsize=8.6,
            color=MUTED, ha="left", va="center")
    ax.plot([0.042, 0.958], [0.398, 0.398], color=HAIR, linewidth=1.0)

    parts = [
        ("计算", "GPU / 加速卡", "核心但只是其一"),
        ("网络", "RoCE 交换机", "移动 448 台 / 电信 374 台"),
        ("存储", "高性能存储", "电信 110 台 / 移动 82 套"),
        ("散热", "冷板液冷", "电信统一要求"),
        ("集成", "调优与测试", "认知门槛最高"),
    ]
    x = 0.042
    w = 0.174
    gap = 0.0165
    for name, item, note in parts:
        panel(ax, x, 0.180, w, 0.190, TEAL if name == "集成" else NAVY)
        ax.text(x + 0.018, 0.328, name, fontsize=10.0, color=INK,
                weight="bold", ha="left", va="center", zorder=9)
        ax.text(x + 0.018, 0.290, item, fontsize=7.8, color=MUTED,
                ha="left", va="center", zorder=9)
        ax.text(x + 0.018, 0.238, note, fontsize=7.2, color=MUTED,
                ha="left", va="top", linespacing=1.6, zorder=9)
        x += w + gap

    outro(fig, ax, "卡是零件；系统才是交付物——这是这轮采购真正的变化。")
    foot(fig, ax, "事实来源：中国移动/中国电信集采公告；超节点技术特征与通信占比引自"
         "通信产业网 2026-11-25（第三方测算口径）")

    fig.savefig(OUT + "图3_超节点.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)
