# -*- coding: utf-8 -*-
"""
《中国归零了，新加坡那一行却先消失：一份做空报告的推演与边界》配套图表
事实口径（均已核对原始披露）：
  · Culper Research《The China Problem》，2026-05-13 发布，40 页，开篇明示
    「We are short Nvidia」，即持有英伟达空头仓位（存在自身利益立场）。
    PDF: culperresearch.com/wp-content/uploads/2026/05/Culper_NVDA_5-13-2026.pdf
  · Megaspeed（新加坡）资产负债表：2023 年底 3300 万美元 → 2024 年底 30 亿美元
    总负债及权益，主要由 29 亿美元「refundable deposits received」（来源未具名）
    推动；同期「amounts due from subsidiaries」亦为 29 亿美元。
  · Speedmatrix（马来西亚）：2024 年 6 月、开业前两个月，将全部业务质押给
    Apex Enterprise Solutions（新加坡）；新加坡工商信息显示 Apex 母公司为阿里
    巴巴，唯一业务为「providing procurement activities」；截至 2025-03-31，
    Apex 报表列 41 亿美元预付款、42 亿美元对阿里借款。
  · 贸易记录：2024-12 至 2026-01，Speedmatrix 进口 46 亿美元货物，其中
    40 亿美元来自 Aivres Systems（前身 Inspur Systems，浪潮信息关联，改名后
    仍由中方国资持有约三分之一）。
  · Giga Computing（技嘉）向 Speedmatrix 与 Novagate 合计出口逾 5 亿美元
    H200／Blackwell 服务器；Novagate 马来西亚子公司 2025-04-11 注册，
    即管制宣布后两天。
  · 英伟达地域收入口径：2025-11（2026 财年第三季度）起由「客户账单地址」
    改为「直接客户总部所在地」，新加坡不再单列。
    FY2025（截至 2025-01-26）按账单地址，新加坡 236.84 亿美元、占 18%；
    2026 财年 Q2（截至 2025-07-27）新加坡 101.56 亿美元、占 22%、同比 +81%，
    该季为最后一次单列（WSJ／Fortune 2026-11）。
    FY2025 中国收入：旧口径 171.08 亿美元 → 新口径 250.48 亿美元（+79.4 亿）。
    2027 财年 Q3（2026-11-17 公布）：美国 62.93%、中国台湾 26.15%、
    中国（含香港）9.54%（110.50 亿美元）、其他 1.38%。
  · 金融时报（2026-11-17）：英伟达新加坡子公司截至 2026-01 的 12 个月
    对外营收约 1040 亿美元、同比 +72%，全年利润仅 5300 万美元。
  · 纽约时报（2026-11-09）：英伟达总法律顾问 Tim Teter 2025-08 电邮商务部
    调查人员询问 Megaspeed 案，案件随后移交司法部，商务部调查中止。
  · 美国司法部与商务部联合声明（2026-11-17）：对 Megaspeed 展开刑事调查。
  · 新加坡内政部（2026-11-12）：2025-02 起调查 Megaspeed 与黄乐（Alice Huang），
    未发现间谍活动充分证据，但禁止黄乐再入境。
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
SAND = "#f7f3ea"
GREEN = "#4f6b58"
AMBER = "#a8863f"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep


def base(title, sub):
    fig = plt.figure(figsize=(12, 6.8))
    fig.patch.set_facecolor("white")
    fig.text(0.045, 0.950, title, fontsize=19.5, color=DARK, weight="bold",
             ha="left", va="top")
    fig.text(0.045, 0.880, sub, fontsize=10.6, color=GRAY, ha="left", va="top")
    return fig


def footer(fig, text):
    fig.text(0.045, 0.014, text, fontsize=8.0, color=GRAY, ha="left", va="center")


def punchline(fig, text, y=0.075):
    fig.text(0.045, y, text, fontsize=10.6, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.6", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


def arrow(ax, x1, y1, x2, y2, color=LIGHT):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>",
                                 mutation_scale=14, linewidth=1.2,
                                 color=color, shrinkA=2, shrinkB=2, zorder=1))


# ------------------------------------------------------------------ 图 1
def fig1():
    fig = base("一条链的三层：设备出海、公司过桥、钱隐身",
               "做空报告把这条链拆成三段，每一段各自解决一个管制问题")
    ax = fig.add_axes([0.045, 0.130, 0.915, 0.705])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    nodes = [
        (0.020, "上游 · 合规外壳", "Aivres Systems", NAVY,
         "美国加州注册\n前身浪潮信息的美国子公司\n中方国资持股约三分之一\n卡在 50% 门槛之下"),
        (0.265, "中游 · 过桥公司", "Megaspeed\nSpeedmatrix", GREEN,
         "新加坡接单、马来西亚进口\n2024-12 至 2026-01\n进口 46 亿美元服务器"),
        (0.510, "中游 · 换壳备份", "Novagate Cloud", AMBER,
         "官网与 Megaspeed 近乎同版\n马来西亚子公司 2025-04-11 注册\n管制宣布后两天"),
        (0.755, "下游 · 真实需求", "中国境内算力", RED,
         "报告称 FY2026 逾 20%\n算力收入仍由中国驱动\n（此为报告估算，非公司口径）"),
    ]

    for x, tag, name, color, body in nodes:
        ax.add_patch(Rectangle((x, 0.395), 0.205, 0.470, facecolor="white",
                               edgecolor=color, linewidth=1.1, zorder=2))
        ax.text(x + 0.017, 0.820, tag, fontsize=8.6, color=GRAY,
                ha="left", va="center", zorder=3)
        ax.text(x + 0.017, 0.748, name, fontsize=10.6, color=color,
                weight="bold", ha="left", va="center", linespacing=1.45,
                zorder=3)
        ax.plot([x + 0.017, x + 0.188], [0.700, 0.700], color=LIGHT,
                linewidth=0.9, zorder=3)
        ax.text(x + 0.017, 0.560, body, fontsize=8.5, color=SLATE, ha="left",
                va="center", linespacing=1.95, zorder=3)

    for x in (0.228, 0.473, 0.718):
        arrow(ax, x, 0.630, x + 0.034, 0.630, GRAY)

    # 下半部分：钱的路径
    ax.plot([0.020, 0.960], [0.345, 0.345], color=LIGHT, linewidth=0.9)

    ax.text(0.020, 0.300, "另一种解法：钱不从股权走", fontsize=10.2, color=DARK,
            weight="bold", ha="left", va="center")

    money = [
        ("29 亿美元「可退还押金」", "Megaspeed 账面，来源未具名\n不计股本、不公示股东"),
        ("29 亿美元「应收子公司」", "同一笔钱转手给\n马来西亚子公司"),
        ("全部资产质押给 Apex", "Apex 母公司为阿里巴巴\n唯一业务：采购服务"),
    ]
    xx = 0.020
    for i, (head, body) in enumerate(money):
        ax.add_patch(FancyBboxPatch((xx, 0.105), 0.290, 0.160,
                                    boxstyle="round,pad=0.012",
                                    facecolor=SAND, edgecolor="#d9cdb6",
                                    linewidth=1.0, zorder=2))
        ax.text(xx + 0.020, 0.218, head, fontsize=9.8, color="#7a6746",
                weight="bold", ha="left", va="center", zorder=3)
        ax.text(xx + 0.020, 0.155, body, fontsize=8.4, color="#7a6746",
                ha="left", va="center", linespacing=1.9, zorder=3)
        if i < 2:
            arrow(ax, xx + 0.296, 0.185, xx + 0.330, 0.185, "#b9a882")
        xx += 0.335

    punchline(fig, "三段各解一题：设备出境、公司身份、钱的主人。")
    footer(fig, "依据：Culper Research《The China Problem》（2026-05-13）｜制图：本文")
    fig.savefig(OUT + "图1_一条链的三层.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("新加坡那一行：先占 22%，然后整行消失",
               "口径一变，最异常的那一项就从财报里找不到了")
    ax = fig.add_axes([0.045, 0.130, 0.915, 0.705])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    cards = [
        (0.020, 0.510, "236.84 亿美元", "FY2025 全年 · 按账单地址", "占当年总营收 18%，仅次于美国", NAVY),
        (0.510, 0.510, "101.56 亿美元", "2026 财年 Q2 · 单季", "占当季 22%，同比 +81%，最后一次单列", RED),
        (0.020, 0.130, "1040 亿美元", "新加坡子公司 · 对外营收", "截至 2026-01 的 12 个月，同比 +72%", GREEN),
        (0.510, 0.130, "5300 万美元", "同一主体 · 全年利润", "千亿美元流水，利润不到一个零头", AMBER),
    ]
    for x, y, big, note, sub, color in cards:
        ax.add_patch(Rectangle((x, y), 0.450, 0.315, facecolor="white",
                               edgecolor=color, linewidth=1.1, zorder=2))
        ax.text(x + 0.024, y + 0.240, note, fontsize=8.8, color=GRAY,
                ha="left", va="center", zorder=3)
        ax.text(x + 0.024, y + 0.165, big, fontsize=17.0, color=color,
                weight="bold", ha="left", va="center", zorder=3)
        ax.text(x + 0.024, y + 0.075, sub, fontsize=8.6, color=SLATE,
                ha="left", va="center", zorder=3)

    punchline(fig, "2025 年 11 月起，这一行不再出现——公司说，因为改按客户总部统计。")
    footer(fig, "数据：英伟达 FY2025 10-K、2026 财年 Q2 10-Q；金融时报（2026-11-17）｜制图：本文")
    fig.savefig(OUT + "图2_新加坡那一行.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("同一财年，换个口径中国多出 79 亿美元",
               "左边是重述前后的差额，右边是改口径之后的最新一季")
    ax = fig.add_axes([0.045, 0.130, 0.915, 0.705])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(0.030, 0.845, "FY2025 中国收入：两种统计方法", fontsize=10.6,
            color=DARK, weight="bold", ha="left", va="center")
    ax.text(0.030, 0.800, "同一财年、同一批客户，只是换了个「算在谁头上」", fontsize=8.6,
            color=GRAY, ha="left", va="center")

    bars = [
        (0.615, "171.08 亿美元", "按客户账单地址（旧口径）", 0.300, LIGHT, SLATE),
        (0.405, "250.48 亿美元", "按客户总部所在地（新口径）", 0.440, NAVY, NAVY),
    ]
    for y, label, note, w, color, tcolor in bars:
        ax.text(0.030, y + 0.125, note, fontsize=8.8, color=SLATE,
                ha="left", va="center", zorder=3)
        ax.add_patch(Rectangle((0.030, y), w, 0.078, facecolor=color,
                               edgecolor="none", zorder=2))
        ax.text(0.030 + w + 0.018, y + 0.039, label, fontsize=10.4,
                color=tcolor, weight="bold", ha="left", va="center", zorder=3)

    ax.text(0.030, 0.330, "差额 +79.4 亿美元：同一年，凭空多出一块中国收入", fontsize=8.8,
            color=RED, ha="left", va="center")
    ax.text(0.030, 0.285, "也就是说：旧口径把总部在中国的采购，记到了开票地（多在新加坡）名下。", fontsize=8.6,
            color=SLATE, ha="left", va="center")

    ax.plot([0.700, 0.700], [0.180, 0.860], color=LIGHT, linewidth=1.0,
            linestyle=(0, (4, 4)))

    ax.text(0.735, 0.845, "2027 财年 Q3 地域结构", fontsize=10.6, color=DARK,
            weight="bold", ha="left", va="center")
    ax.text(0.735, 0.800, "新口径下，中国仍是 9.54%", fontsize=8.6, color=GRAY,
            ha="left", va="center")

    regions = [
        ("美国", 62.93, "728.99 亿美元", NAVY),
        ("中国台湾", 26.15, "302.95 亿美元", GREEN),
        ("中国（含香港）", 9.54, "110.50 亿美元", RED),
        ("其他", 1.38, "16 亿美元", GRAY),
    ]
    yy = 0.700
    for name, pct, amount, color in regions:
        ax.text(0.735, yy, name, fontsize=9.2, color=SLATE, ha="left",
                va="center")
        ax.add_patch(Rectangle((0.850, yy - 0.020), 0.130 * pct / 62.93, 0.040,
                               facecolor=color, edgecolor="none", zorder=2))
        ax.text(0.850 + 0.130 * pct / 62.93 + 0.010, yy,
                "%.2f%%" % pct, fontsize=9.0, color=color, weight="bold",
                ha="left", va="center", zorder=3)
        ax.text(0.735, yy - 0.052, amount, fontsize=8.0, color=GRAY,
                ha="left", va="center")
        yy -= 0.135

    ax.text(0.735, 0.190, "注：新口径下中国仍有单季 110 亿美元收入，", fontsize=8.4,
            color=SLATE, ha="left", va="center")
    ax.text(0.735, 0.152, "与「对华高端算力归零」并不矛盾——归零的是受管制型号。", fontsize=8.4,
            color=SLATE, ha="left", va="center")

    punchline(fig, "口径改的不是事实，是事实归谁。")
    footer(fig, "数据：英伟达 FY2025／FY2026 10-K、2027 财年 Q3 财报（2026-11-17）｜制图：本文")
    fig.savefig(OUT + "图3_换个口径中国多出79亿.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 4
def fig4():
    fig = base("钱怎么进去，又不留名字",
               "报告复原的三步：押金代替入股、应收代替转账、质押代替控股")
    ax = fig.add_axes([0.045, 0.130, 0.915, 0.705])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    steps = [
        ("第 1 步", "钱以押金进来", "29 亿美元「可退还押金」", NAVY,
         "押金不是股本：不进股东名册、不需公示股东身份。\nMegaspeed 总资产从 3300 万涨到 30 亿美元，几乎全靠它。"),
        ("第 2 步", "钱变成内部应收", "29 亿美元「应收子公司」", GREEN,
         "同一笔钱以内部往来形式转给 Speedmatrix。\n报表上看是关联方往来，不是外部注资。"),
        ("第 3 步", "资产全额质押", "Speedmatrix 质押全部业务", AMBER,
         "2024 年 6 月、开业前两个月，把全部业务押给 Apex。\nApex 母公司为阿里巴巴，唯一业务是采购。"),
    ]
    yy = 0.845
    for tag, head, big, color, body in steps:
        ax.add_patch(Rectangle((0.030, yy - 0.175), 0.930, 0.175,
                               facecolor="white", edgecolor=color,
                               linewidth=1.1, zorder=2))
        ax.text(0.050, yy - 0.030, tag, fontsize=8.4, color=GRAY, ha="left",
                va="center", zorder=3)
        ax.text(0.050, yy - 0.075, head, fontsize=11.6, color=color,
                weight="bold", ha="left", va="center", zorder=3)
        ax.text(0.050, yy - 0.140, body, fontsize=8.4, color=SLATE, ha="left",
                va="center", linespacing=1.75, zorder=3)
        ax.text(0.610, yy - 0.075, big, fontsize=9.8, color=DARK,
                ha="left", va="center", zorder=3)
        yy -= 0.215

    ax.add_patch(FancyBboxPatch((0.030, 0.030), 0.930, 0.150,
                                boxstyle="round,pad=0.008", facecolor=PALE,
                                edgecolor=LIGHT, linewidth=1.0, zorder=2))
    ax.text(0.050, 0.128, "结果：出资方拿到了资产处置权（质押），但没有出现在任何股东名单上。",
            fontsize=9.0, color=DARK, ha="left", va="center", zorder=3)
    ax.text(0.050, 0.075, "报告能拿到的只是两端各一半的线索：押金来源未具名，Apex 母公司是阿里。直接对应关系没有证据。",
            fontsize=8.4, color=SLATE, ha="left", va="center", zorder=3)

    punchline(fig, "不持股、只出资、全质押：链条上最精巧的一环，也是最缺实锤的一环。")
    footer(fig, "依据：Culper Research《The China Problem》（2026-05-13）引 Megaspeed 财报、马来西亚与新加坡工商登记｜制图：本文")
    fig.savefig(OUT + "图4_钱怎么进去又不留名字.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 5
def fig5():
    fig = base("两年时间线：管制、调查、做空，三条线互相追着走",
               "每一个节点都有公开出处，判断留给读者")
    ax = fig.add_axes([0.045, 0.130, 0.915, 0.705])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.plot([0.140, 0.140], [0.185, 0.865], color=LIGHT, linewidth=1.6)

    events = [
        ("2024-06", "Speedmatrix 将全部业务质押给 Apex（阿里）", "开业前两个月", NAVY),
        ("2025-04", "美国收紧管制，对华 AI 芯片销售基本关闭", "英伟达计提 55 亿美元 H20 减值", RED),
        ("2025-06", "英伟达把 Megaspeed 列入内部禁售名单", "据《华尔街日报》", AMBER),
        ("2025-08", "英伟达总法律顾问电邮商务部，询问 Megaspeed 案", "案件随后移交司法部，商务部调查中止（NYT）", RED),
        ("2025-11", "英伟达改地域收入口径，新加坡不再单列", "同日季度财报口径变更", NAVY),
        ("2026-03", "WSJ：Aivres 向马来西亚运营商供 25 亿美元 Blackwell", "同一月，超微关联三人被起诉，涉 25 亿美元转运", GREEN),
        ("2026-05-13", "Culper Research 发布 40 页报告《The China Problem》", "开篇明示持有英伟达空头仓位", SLATE),
        ("2026-11-17", "司法部与商务部联合声明：对 Megaspeed 刑事调查", "新加坡内政部 11-12：未发现间谍证据，禁止黄乐入境", RED),
    ]
    yy = 0.855
    for date, text, note, color in events:
        ax.add_patch(plt.Circle((0.140, yy), 0.0085, facecolor=color,
                                edgecolor="white", linewidth=1.2, zorder=4))
        ax.text(0.030, yy, date, fontsize=9.2, color=color, weight="bold",
                ha="left", va="center", zorder=3)
        ax.text(0.168, yy + 0.017, text, fontsize=9.4, color=DARK, ha="left",
                va="center", zorder=3)
        ax.text(0.168, yy - 0.023, note, fontsize=8.2, color=GRAY, ha="left",
                va="center", zorder=3)
        yy -= 0.092

    punchline(fig, "管制在前，调查在中，做空在后——时间顺序本身不是证据。")
    footer(fig, "依据：纽约时报（2026-11-09）、华尔街日报（2026-11）、金融时报（2026-11-17）、美司法部与商务部联合声明（2026-11-17）、Culper Research（2026-05-13）｜制图：本文")
    fig.savefig(OUT + "图5_两年时间线.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 6
def fig6():
    fig = base("把报告拆开：哪一句是文件，哪一句是推断",
               "同一份报告里，证据强度差四个量级")
    ax = fig.add_axes([0.045, 0.130, 0.915, 0.705])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    ax.text(0.030, 0.858, "结论", fontsize=9.0, color=GRAY, ha="left",
            va="center")
    ax.text(0.530, 0.858, "支撑它的东西", fontsize=9.0, color=GRAY, ha="left",
            va="center")
    ax.text(0.818, 0.858, "强度", fontsize=9.0, color=GRAY, ha="left",
            va="center")
    ax.plot([0.030, 0.960], [0.838, 0.838], color=LIGHT, linewidth=1.0)

    rows = [
        ("Speedmatrix 把全部业务质押给 Apex；\nApex 母公司是阿里巴巴",
         "马来西亚、新加坡工商登记\n与公司财务报表", "文件实证", GREEN),
        ("Speedmatrix 进口 46 亿美元设备，\n其中 40 亿来自 Aivres",
         "贸易记录（第三方数据商口径）\n报告未公开原始单据", "文件实证\n原件待核", NAVY),
        ("29 亿美元押金与阿里出资是同一笔钱",
         "押金来源未具名；\nApex 母公司是阿里巴巴", "推断", AMBER),
        ("英伟达「放任」转运，并对监管施压",
         "离职员工访谈；NYT 关于电邮\n与案件移交的报道；公司否认", "立场推定", RED),
    ]

    yy = 0.790
    for claim, basis, level, color in rows:
        ax.add_patch(Rectangle((0.030, yy - 0.160), 0.930, 0.155,
                               facecolor="white", edgecolor=LIGHT,
                               linewidth=0.9, zorder=2))
        ax.text(0.048, yy - 0.080, claim, fontsize=8.8, color=DARK,
                ha="left", va="center", linespacing=1.8, zorder=3)
        ax.text(0.530, yy - 0.080, basis, fontsize=8.2, color=SLATE,
                ha="left", va="center", linespacing=1.8, zorder=3)
        ax.add_patch(FancyBboxPatch((0.818, yy - 0.118), 0.130, 0.076,
                                    boxstyle="round,pad=0.008",
                                    facecolor="white", edgecolor=color,
                                    linewidth=1.2, zorder=3))
        ax.text(0.883, yy - 0.080, level, fontsize=8.2, color=color,
                weight="bold", ha="center", va="center", linespacing=1.6,
                zorder=4)
        yy -= 0.178

    ax.text(0.030, 0.058, "注：Culper Research 在报告开篇写明「We are short Nvidia」，即持有英伟达空头仓位，结论与自身盈亏同向。",
            fontsize=8.4, color=RED, ha="left", va="center")

    punchline(fig, "前三行能当事实读，第四行只能当指控读。")
    footer(fig, "依据：Culper Research《The China Problem》（2026-05-13）；分级为本文判断｜制图：本文")
    fig.savefig(OUT + "图6_证据分四级.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    fig4()
    fig5()
    fig6()
    print("done:", OUT)
