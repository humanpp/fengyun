# -*- coding: utf-8 -*-
"""
《30 毫升水，占掉了半个胃》配套图表
事实口径（均经公开信息逐条核对）：
  · 2026-11-19 报道，2026-11-20 澎湃新闻转载：河南一名出生 20 多天的新生儿，
    就诊时“精神状态很差，双手、双脚和阴囊都出现了水肿”，诊断“肾功能异常、
    电解质紊乱、肾脏负荷过重”；起因是“黄疸退得慢，还出现了便秘、舌苔厚的情况，
    家长以为是‘上火’，就在两顿奶之间加喂 30-50 毫升的白开水”。
    医生说法：“母乳的水分含量约 87%”“0–3个月宝宝肾脏过滤、排泄功能不到成人的一半”
    “宝宝胃容量极小，喝完奶再灌水，水占了位置，奶量自然下降”；
    判断标准“24 小时尿片数量……大于等于 6 片”。
  · 胃容量与奶量：第1-2天 5-13ml、第3-6天 22-27ml、1周之后约 60ml、满月约 120ml；
    15天—满月每次奶量 90-120ml，一天 8-10 次；胃排空 水 1-2 小时、母乳 2-3 小时、
    牛奶 3-4 小时。—— 中华医学会围产医学分会 2021-09-13 科普。
  · “一日喝水量若超过每公斤 50ml 才有可能达到急性低钠血症的程度”
    —— 台大医院健康教育《嬰兒可以喝水嗎？》。
  · 水中毒＝高容量性低钠血症，细胞外液稀释致细胞肿胀，脑细胞反应最快。
换算说明：“4 公斤 × 50ml/kg ＝ 200ml”“30～50ml × 6 次 ＝ 180～300ml”
     均为公开数字的直接相乘；报道未披露患儿体重与每日喂水次数，
     4 公斤与每天 6 次是为换算成立所设的估算前提。
风格：克制传媒风，白底、低饱和配色、标题即结论。输出目录 = 脚本所在目录。
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False

NAVY = "#1f3a5f"
RED = "#a83f36"
GRAY = "#8a8f98"
SLATE = "#5f6673"
LIGHT = "#d8dbe0"
DARK = "#2b2f36"
PALE = "#eef0f3"
SAND = "#f7f3ea"
GOLD = "#c2a15c"
GREEN = "#5a7d6f"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep


def base(title, sub):
    fig = plt.figure(figsize=(12, 6.8))
    fig.patch.set_facecolor("white")
    fig.text(0.045, 0.950, title, fontsize=20, color=DARK, weight="bold",
             ha="left", va="top")
    fig.text(0.045, 0.878, sub, fontsize=10.8, color=GRAY, ha="left", va="top")
    return fig


def footer(fig, line1, line2):
    fig.text(0.045, 0.042, line1, fontsize=7.6, color=GRAY, ha="left", va="center")
    fig.text(0.045, 0.020, line2, fontsize=7.6, color=GRAY, ha="left", va="center")


def punchline(fig, text, y=0.080):
    fig.text(0.045, y, text, fontsize=10.8, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.6", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


def canvas(fig, bottom=0.135, height=0.700):
    ax = fig.add_axes([0.045, bottom, 0.915, height])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return ax


# ------------------------------------------------------------------ 图 1
def fig1():
    fig = base("30 毫升水，半个胃",
               "新生儿的胃容量，和这一勺水比一比")
    ax = canvas(fig)

    VMAX = 140.0

    def X(v):
        return 0.215 + v / VMAX * 0.725

    # 网格
    for v in range(0, 141, 20):
        ax.plot([X(v), X(v)], [0.150, 0.820], color="#f1f3f6", linewidth=0.9,
                zorder=1)
        ax.text(X(v), 0.118, "%d" % v, fontsize=8.4, color=GRAY, ha="center",
                va="top")
    ax.text(X(70), 0.075, "毫升（mL）", fontsize=8.6, color=GRAY, ha="center",
            va="top")

    rows = [
        (0.760, "出生第 1–2 天", 5, 13, SLATE),
        (0.634, "出生第 3–6 天", 22, 27, SLATE),
        (0.508, "1 周后", 60, None, SLATE),
        (0.382, "满月", 120, None, SLATE),
        (0.230, "一次奶量（15 天—满月）", 90, 120, NAVY),
    ]

    for y, name, lo, hi, col in rows:
        ax.text(0.196, y, name, fontsize=10.6, color=DARK, ha="right",
                va="center")
        ax.barh(y, X(hi if hi else lo) - X(0), left=X(0), height=0.078,
                color=col, alpha=0.18, edgecolor="none", zorder=3)
        ax.barh(y, X(lo) - X(0), left=X(0), height=0.078, color=col,
                edgecolor="none", zorder=4)
        label = ("%d–%d" % (lo, hi)) if hi else ("约 %d" % lo)
        ax.text(X(hi if hi else lo) + 0.010, y, label, fontsize=10.0,
                color=col, weight="bold", ha="left", va="center", zorder=7,
                bbox=dict(boxstyle="square,pad=0.25", facecolor="white",
                          edgecolor="none"))

    # 这一勺水
    ax.add_patch(Rectangle((X(30), 0.150), X(50) - X(30), 0.670,
                           facecolor=RED, alpha=0.13, edgecolor="none",
                           zorder=2))
    ax.plot([X(30), X(30)], [0.150, 0.820], color=RED, linewidth=1.2,
            linestyle=(0, (4, 3)), zorder=5)
    ax.plot([X(50), X(50)], [0.150, 0.820], color=RED, linewidth=1.2,
            linestyle=(0, (4, 3)), zorder=5)
    ax.text((X(30) + X(50)) / 2, 0.856, "这次喂的水 30–50", fontsize=10.0,
            color=RED, weight="bold", ha="center", va="bottom")

    punchline(fig, "满月的胃装满也就 120 毫升，这一勺水占掉三到四成。")
    footer(fig,
           "事实：胃容量“第1-2天 5-13ml、第3-6天 22-27ml、1周之后可达60ml、满月时能达到120ml”，奶量“15天—满月 每次90-120ml”，",
           "据中华医学会围产医学分会 2021-09-13 科普；一次加喂 30-50 毫升白开水据 2026-11-19 报道（澎湃新闻 2026-11-20）｜制图：本文")
    fig.savefig(OUT + "图1_三十毫升水半个胃.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("一天的 200 毫升，是条什么线",
               "按体重算的急性低钠门槛，和这个宝宝一天可能喝下去的水")
    ax = canvas(fig)

    VMAX = 320.0

    def X(v):
        return 0.115 + v / VMAX * 0.825

    # 两段底色
    ax.add_patch(Rectangle((X(0), 0.330), X(200) - X(0), 0.400,
                           facecolor="#f2f6f3", edgecolor="none", zorder=1))
    ax.add_patch(Rectangle((X(200), 0.330), X(320) - X(200), 0.400,
                           facecolor="#fdf4f3", edgecolor="none", zorder=1))
    ax.text(X(100), 0.395, "未越过门槛", fontsize=9.0, color="#6b8574",
            ha="center", va="center")
    ax.text(X(260), 0.395, "越过门槛", fontsize=9.0, color="#a8756c",
            ha="center", va="center")

    # 门槛线
    ax.plot([X(200), X(200)], [0.300, 0.790], color=RED, linewidth=1.8,
            linestyle=(0, (5, 3)), zorder=4)
    ax.text(X(200) + 0.010, 0.800, "4 公斤 × 每公斤 50 毫升 ＝ 200 毫升",
            fontsize=10.0, color=RED, weight="bold", ha="left", va="bottom")

    # 一天的水量区间
    ax.add_patch(Rectangle((X(180), 0.500), X(300) - X(180), 0.085,
                           facecolor=GOLD, edgecolor="none", zorder=5))
    ax.plot([X(180), X(180)], [0.470, 0.615], color=GOLD, linewidth=1.4,
            zorder=6)
    ax.plot([X(300), X(300)], [0.470, 0.615], color=GOLD, linewidth=1.4,
            zorder=6)
    ax.text(X(240), 0.660, "一天 6 次 × 30–50 毫升 ＝ 180–300 毫升",
            fontsize=10.0, color="#8a6f3e", weight="bold", ha="center",
            va="bottom", zorder=7,
            bbox=dict(boxstyle="square,pad=0.3", facecolor="white",
                      edgecolor="none"))

    # 刻度
    ax.plot([X(0), X(VMAX)], [0.300, 0.300], color=LIGHT, linewidth=1.4,
            zorder=3)
    for v in range(0, 321, 40):
        ax.plot([X(v), X(v)], [0.300, 0.288], color=LIGHT, linewidth=1.1,
                zorder=3)
        ax.text(X(v), 0.262, "%d" % v, fontsize=8.4, color=GRAY, ha="center",
                va="top")
    ax.text(X(VMAX), 0.222, "毫升 / 天", fontsize=8.6, color=GRAY, ha="right",
            va="top")

    punchline(fig, "同一件事，换个体重算，结果就跨过了那条线。")
    footer(fig,
           "事实：“一日喝水量若超过每公斤 50ml 才有可能达到急性低钠血症的程度”，据台大医院健康教育《嬰兒可以喝水嗎？》；",
           "一次加喂 30-50 毫升据 2026-11-19 报道；体重与每日次数为本文换算所设估算前提，报道未披露｜制图：本文")
    fig.savefig(OUT + "图2_两百毫升这条线.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("一个闭环", "从“黄疸退得慢”出发，回到“退得更慢”")
    ax = canvas(fig)

    boxes = [
        (0.790, "黄疸退得慢 · 便秘 · 舌苔厚", PALE, LIGHT, DARK),
        (0.575, "家长判断：这是“上火”", PALE, LIGHT, DARK),
        (0.360, "两顿奶之间加喂 30–50 毫升白开水", "#fdf4f3", RED, DARK),
        (0.145, "吃奶少 → 排便少 → 胆红素排出减少", "#fdf4f3", RED, DARK),
    ]

    for y, text, bg, ec, tc in boxes:
        ax.add_patch(FancyBboxPatch((0.230, y), 0.550, 0.110,
                                    boxstyle="round,pad=0.010", facecolor=bg,
                                    edgecolor=ec, linewidth=1.2))
        ax.text(0.505, y + 0.055, text, fontsize=11.4, color=tc,
                weight="bold", ha="center", va="center")

    for y0, y1 in ((0.786, 0.690), (0.571, 0.475), (0.356, 0.260)):
        ax.annotate("", xy=(0.505, y1), xytext=(0.505, y0),
                    arrowprops=dict(arrowstyle="-|>", color=SLATE, linewidth=1.5,
                                    mutation_scale=14))

    # 回路
    ax.plot([0.230, 0.120], [0.200, 0.200], color=RED, linewidth=1.4,
            zorder=4)
    ax.plot([0.120, 0.120], [0.200, 0.845], color=RED, linewidth=1.4,
            zorder=4)
    ax.annotate("", xy=(0.228, 0.845), xytext=(0.120, 0.845),
                arrowprops=dict(arrowstyle="-|>", color=RED, linewidth=1.4,
                                mutation_scale=14))
    ax.text(0.086, 0.520, "于是喂水这件事，看起来是对的", fontsize=9.4,
            color=RED, weight="bold", ha="center", va="center", rotation=90)

    punchline(fig, "越喂越慢，越慢越喂——问题出在第一步的判断上。")
    footer(fig,
           "事实：黄疸退得慢、便秘、舌苔厚被家长判为“上火”并加喂 30-50 毫升白开水，据 2026-11-19 报道（澎湃新闻 2026-11-20）；",
           "“喝完奶再灌水，水占了位置，奶量自然下降，长期下去体重增长缓慢、营养不良”据该报道医生表述；吃奶少致排便少、胆红素排出减少为新生儿黄疸的常见机制｜制图：本文")
    fig.savefig(OUT + "图3_一个闭环.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)