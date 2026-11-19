# -*- coding: utf-8 -*-
"""
《肺癌靶向药难逃"两年之困"？这半句是真的》配套图表
事实口径（2026-11-19，逐条核对原始报道、国家癌症中心数据与 MARIPOSA 试验原文后）：
  · 国家癌症中心 2024 年中国恶性肿瘤流行情况：全年新发癌症约 515.06 万例，
    肺癌为发病首位，年新发约 117—118 万例（《中华肿瘤杂志》2026 年发布；
    Cancer incidence and mortality in China, 2024，PMC13731668）。
  · 中山大学肿瘤防治中心胸外科主任医师龙浩接受南方+采访时表示：
    一代 EGFR-TKI 中位耐药时间约 8—10 个月；三代 EGFR-TKI 一线使用后，
    中位耐药时间大多在 18—22 个月；"单靠靶向药，能维持的时间很难超过两年"
    （南方+ 经中华网转载 2026-11-19 16:10，原文标题《肺癌靶向药难逃"两年之困"？
    双抗联合靶向瞄准耐药旁路》）。
  · 同篇报道：非小细胞肺癌中腺癌占比 50%—60%，肺腺癌患者 EGFR 突变阳性比例超过 50%；
    EGFR 靶向治疗自 2003 年一代药物起步；低剂量螺旋 CT 筛查已证实可降低 20% 肺癌死亡率；
    门诊晚期患者占比由约三分之二降至约三分之一。
  · 耐药机制：MET 扩增是发生率最高的旁路耐药类型，三代 EGFR-TKI 耐药后约 8%，
    一代耐药后约 10%—15%；另有小细胞转化、其他旁路突变等（同篇报道引龙浩）。
  · 脑转移：初诊晚期肺癌患者约 20% 伴脑转移；初诊无脑转移者，一代 EGFR-TKI 治疗后
    三年内脑转移发生率约 25%，三代可降至约 10%（同篇报道）。
  · 该报道称 EGFR/MET 双抗联合三代 EGFR-TKI 一线方案"三年总生存率超过 71%，
    较三代 EGFR-TKI 单药提升约 20%，较三代 EGFR-TKI 联合化疗提升约 10%"。
    经核 MARIPOSA Ⅲ 期试验最终总生存分析（Yang 等，NEJM 2025；
    2025-09-23 ASCO Post 报道）：中位随访 37.8 个月，
    3 年总生存率 amivantamab+lazertinib 组 60%、奥希替尼组 51%
    （HR=0.75，95%CI 0.61—0.92，P=0.005），中位 OS 未达到 vs 36.7 个月。
    即"71%"与"提升约 20%"两个数字与试验原文不符；
    按百分点计，两组相差 9 个百分点，相对降幅约 15%。
    本文据此标注为"报道口径与试验原文不一致"，不做推断。
  · 安全性（同一试验）：≥3 级不良事件发生率 80% vs 52%。
  · 报道同时载明：上述数据来自临床研究，真实世界长期生存仍需更多随访验证；
    EGFR/MET 双抗皮下剂型已在国内获批约 4 个月。
本文换算（非当事方口径）："两年"= 24 个月，落在三代药 18—22 个月中位耐药时间之上、
一代药 8—10 个月的两倍以上；60% − 51% = 9 个百分点。
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
    fig = base("两年不是药的极限，是单药一线的时间",
               "EGFR-TKI 一线治疗的中位耐药时间｜单位：个月")
    ax = canvas(fig)

    x0 = 0.300
    scale = 0.400 / 24.0

    bars = [
        ("一代 EGFR-TKI", "如吉非替尼、厄洛替尼", 8, 10, GRAY, 0.740),
        ("三代 EGFR-TKI", "如奥希替尼，一线使用", 18, 22, NAVY, 0.540),
    ]

    for name, note, lo, hi, color, y in bars:
        ax.add_patch(Rectangle((x0, y - 0.048), hi * scale, 0.096,
                               facecolor=color, edgecolor="none", alpha=0.28))
        ax.add_patch(Rectangle((x0 + lo * scale, y - 0.048),
                               (hi - lo) * scale, 0.096,
                               facecolor=color, edgecolor="none"))
        ax.text(0.028, y + 0.030, name, fontsize=11.0, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(0.028, y - 0.028, note, fontsize=8.2, color=GRAY,
                ha="left", va="center")
        ax.text(x0 + hi * scale + 0.016, y, "%d—%d 个月" % (lo, hi),
                fontsize=12.6, color=DARK, weight="bold", ha="left",
                va="center")

    # 底部刻度尺：把「两年」标在轴上，避开条形与数值标签
    ry = 0.410
    ax.plot([x0, x0 + 24 * scale], [ry, ry], color=LIGHT, linewidth=1.2)
    for m in (0, 6, 12, 18, 24):
        tx = x0 + m * scale
        ax.plot([tx, tx], [ry - 0.014, ry + 0.014], color=LIGHT, linewidth=1.2)
        ax.text(tx, ry - 0.052, "%d" % m, fontsize=8.6, color=GRAY,
                ha="center", va="center")
    ax.text(x0 + 24 * scale, ry + 0.030, "两年", fontsize=9.6, color=RED,
            weight="bold", ha="center", va="bottom")
    ax.text(x0 - 0.014, ry - 0.052, "个月", fontsize=8.6, color=GRAY,
            ha="right", va="center")

    ax.text(0.028, 0.300,
            "浅色为区间下沿到上沿的跨度；一代药的中位耐药时间不到三代的一半。",
            fontsize=8.8, color=SLATE, ha="left", va="center")

    ax.add_patch(FancyBboxPatch((0.028, 0.150), 0.944, 0.118,
                                boxstyle="round,pad=0.008",
                                facecolor="white", edgecolor=LIGHT,
                                linewidth=1.0))
    ax.text(0.055, 0.222,
            "两年 = 24 个月，比三代药的中位耐药上限（22 个月）还多两个月。",
            fontsize=9.6, color=NAVY, weight="bold", ha="left", va="center")
    ax.text(0.055, 0.178,
            "所以「单靠靶向药很难超过两年」说的是单药一线的天花板，不是治疗的终点。",
            fontsize=8.8, color=SLATE, ha="left", va="center")

    punchline(fig, "「两年」是真的，但它说的是一个方案能撑多久，不是人能活多久。")
    footer(fig, "事实：中山大学肿瘤防治中心龙浩教授接受南方+采访，"
                "经中华网转载 2026-11-19｜区间为报道所述中位值范围｜制图：本文")
    fig.savefig(OUT + "图1_两年是怎么来的.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("71% 和 60%，差的不只是 11 个百分点",
               "同一个联合方案，报道口径与 Ⅲ 期试验原文的对照")
    ax = canvas(fig)

    # 左：报道口径
    ax.text(0.028, 0.828, "报道口径", fontsize=10.4, color=SLATE, weight="bold",
            ha="left", va="center")
    ax.text(0.028, 0.760, "三年总生存率超过 71%", fontsize=15.0, color=RED,
            weight="bold", ha="left", va="center")
    ax.text(0.028, 0.700, "称较单药提升约 20%，较联合化疗提升约 10%",
            fontsize=8.8, color=GRAY, ha="left", va="center")

    # 右：试验原文
    ax.text(0.560, 0.828, "MARIPOSA Ⅲ 期试验原文", fontsize=10.4, color=SLATE,
            weight="bold", ha="left", va="center")

    yy = 0.700
    for label, val, color in [("双抗 + 三代 TKI", "60%", NAVY),
                              ("三代 TKI 单药", "51%", GRAY)]:
        ax.add_patch(Rectangle((0.560, yy - 0.030), val and float(val.strip('%')) * 0.0040,
                               0.060, facecolor=color, edgecolor="none"))
        ax.text(0.560, yy + 0.052, label, fontsize=9.0, color=SLATE,
                ha="left", va="center")
        ax.text(0.560 + float(val.strip('%')) * 0.0040 + 0.014, yy,
                val, fontsize=13.0, color=DARK, weight="bold", ha="left",
                va="center")
        yy -= 0.130

    ax.plot([0.028, 0.972], [0.492, 0.492], color=LIGHT, linewidth=0.9)

    ax.text(0.028, 0.432, "差在哪", fontsize=10.0, color=DARK, weight="bold",
            ha="left", va="center")

    rows = [
        ("三年生存率", "超过 71%", "60%", "差 11 个百分点"),
        ("相对单药的提升", "约 20%", "9 个百分点（相对降幅约 18%）", "口径不同"),
    ]

    y = 0.352
    for a, b, c, d in rows:
        ax.text(0.028, y, a, fontsize=9.0, color=SLATE, ha="left", va="center")
        ax.text(0.300, y, b, fontsize=9.4, color=RED, ha="left", va="center")
        ax.text(0.470, y, c, fontsize=9.4, color=NAVY, ha="left", va="center")
        ax.text(0.800, y, d, fontsize=8.6, color=GRAY, ha="left", va="center")
        y -= 0.078

    ax.text(0.028, 0.150,
            "试验同时显示：≥3 级不良事件发生率 80%（双抗联合组）对 52%（单药组）。",
            fontsize=8.8, color=SLATE, ha="left", va="center")
    ax.text(0.028, 0.104,
            "报道本身也注明：数据来自临床研究，真实世界长期生存仍需更多随访验证。",
            fontsize=8.8, color=SLATE, ha="left", va="center")

    punchline(fig, "疗效是真的，但那个 71%，在试验原文里找不到。")
    footer(fig, "事实：MARIPOSA 最终总生存分析（Yang 等，NEJM 2025；"
                "ASCO Post 2025-09-23）｜报道口径据中华网转载南方+ 2026-11-19｜制图：本文")
    fig.savefig(OUT + "图2_71%和60%.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("耐药之后，肿瘤换一条路走",
               "EGFR-TKI 耐药后的常见旁路机制与脑转移风险")
    ax = canvas(fig)

    ax.text(0.028, 0.840, "MET 扩增：发生率最高的旁路耐药类型", fontsize=10.4,
            color=DARK, weight="bold", ha="left", va="center")

    x0 = 0.330
    scale = 0.420 / 16.0

    bars = [
        ("三代 TKI 耐药后", "约 8%", 8, NAVY),
        ("一代 TKI 耐药后", "约 10%—15%", 12.5, SLATE),
    ]

    y = 0.735
    for name, note, v, color in bars:
        ax.add_patch(Rectangle((x0, y - 0.038), v * scale, 0.076,
                               facecolor=color, edgecolor="none"))
        ax.text(0.028, y + 0.024, name, fontsize=9.6, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(0.028, y - 0.026, "占该线耐药的比例", fontsize=8.0, color=GRAY,
                ha="left", va="center")
        ax.text(x0 + v * scale + 0.014, y, note, fontsize=11.6, color=DARK,
                weight="bold", ha="left", va="center")
        y -= 0.120

    ax.text(0.028, 0.530,
            "另有小细胞转化、其他旁路突变等。龙浩的比喻：道路被封堵，肿瘤会不断寻找其他旁路。",
            fontsize=8.8, color=SLATE, ha="left", va="center")

    ax.plot([0.028, 0.972], [0.470, 0.470], color=LIGHT, linewidth=0.9)

    ax.text(0.028, 0.412, "脑转移：另一个必须一起看的问题", fontsize=10.4,
            color=DARK, weight="bold", ha="left", va="center")

    rows = [
        ("初诊晚期患者伴脑转移", "约 20%", GRAY),
        ("一代 TKI 治疗后三年内", "约 25%", RED),
        ("三代 TKI 治疗后三年内", "约 10%", NAVY),
    ]

    y = 0.330
    for name, val, color in rows:
        ax.text(0.028, y, name, fontsize=9.4, color=SLATE, ha="left",
                va="center")
        ax.text(0.560, y, val, fontsize=11.4, color=color, weight="bold",
                ha="left", va="center")
        y -= 0.076

    ax.text(0.028, 0.062,
            "后两行指初诊无脑转移者。数字来自报道引述，非本文推算。",
            fontsize=8.6, color=GRAY, ha="left", va="center")

    punchline(fig, "耐药不是终点，是换方案的信号。")
    footer(fig, "事实：中山大学肿瘤防治中心龙浩教授接受南方+采访，"
                "经中华网转载 2026-11-19｜制图：本文")
    fig.savefig(OUT + "图3_耐药之后换哪条路.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)
