# -*- coding: utf-8 -*-
"""
《DDR 从 3 美元涨到 16 美元：一辆车成本多出 2.5 万，存储涨价为何"没得谈"？》配套图表
事实口径：博世智能驾控中国区总裁吴永桥测算，只算 DDR、PCB、MLCC 三项涨价，明年
一辆只配基础 L2、没有 8155 芯片的燃油车成本增加 2000—3000 元；配高阶智驾的纯电车
增加 4000—8000 元；座舱配高通 8397 加高阶智驾增加 1 万—2 万元；智驾和座舱配置
拉满增加 2 万—2.5 万元。车规 DDR 三星、美光、长鑫三家报价全球统一，"没有任何人
能谈判"。地平线余凯：年初每 GB 约 3 美元，现在至少 16 美元，三星说明年涨到 28 美元。
中信证券：供不应求至少持续到 2027 年，实质性缓解要等 2028 年新产能集中释放；建
存储晶圆厂从投入到良率爬坡通常 18—24 个月。新能源零售均价从 2023 年 18.4 万元
降至 2026 年 10 月 15.4 万元。
风格：克制传媒风，白底、低饱和配色、标题即结论
输出目录 = 脚本所在目录
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

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

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep


def footer(fig, text):
    fig.text(0.045, 0.020, text, fontsize=8.4, color=GRAY, ha="left", va="bottom")


def punchline(fig, text):
    fig.text(0.045, 0.072, text, fontsize=10.4, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


# ---------------------------------------------------------------- 图 1
def fig1():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.135, 0.910, 0.690])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "配置越高，涨得越多", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.888, "只算 DDR、PCB、MLCC 三项，明年一辆车的成本增量",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    def xpos(v):
        return 0.180 + v * 0.580 / 26000.0

    rows = [
        (0.700, "基础 L2 燃油车", 2000, 3000, "2000—3000 元", SLATE),
        (0.560, "高阶智驾纯电", 4000, 8000, "4000—8000 元", NAVY),
        (0.420, "座舱 + 高阶智驾", 10000, 20000, "1 万—2 万元", NAVY),
        (0.280, "配置拉满", 20000, 25000, "2 万—2.5 万元", RED),
    ]

    for y, label, lo, hi, text, color in rows:
        ax.text(0.020, y + 0.040, label, fontsize=10.2, color=DARK, va="center")
        x0, x1 = xpos(lo), xpos(hi)
        ax.add_patch(Rectangle((x0, y), x1 - x0, 0.076, facecolor=color,
                               edgecolor="none"))
        ax.text(x1 + 0.014, y + 0.038, text, fontsize=10.6, color=color,
                weight="bold", va="center")

    # 基线
    ax.plot([xpos(0), xpos(0)], [0.230, 0.790], color=LIGHT, linewidth=1.2)
    for v in (0, 10000, 20000):
        ax.plot([xpos(v), xpos(v)], [0.230, 0.240], color=LIGHT, linewidth=1.0)
        ax.text(xpos(v), 0.198, f"{v // 10000} 万元" if v else "0", fontsize=8.8,
                color=GRAY, ha="center", va="center")

    ax.text(0.020, 0.135, "阶梯不是线性的：智驾和座舱都吃存储，配置叠加时涨幅会跳档",
            fontsize=9.4, color=GRAY, va="center")

    punchline(fig, "一辆车多出两万五，等于把一台车的利润整块让出去。")
    footer(fig, "据博世吴永桥测算口径整理；增量仅含 DDR、PCB、MLCC 三项，不含其余零部件。")
    fig.savefig(OUT + "图1_成本阶梯.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.135, 0.910, 0.690])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "一年，5 倍多", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.888, "车规 DDR 每 GB 报价：年初 3 美元，现在 16 美元，明年或 28 美元",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    base_y, max_h = 0.300, 0.400
    bars = [
        (0.230, "年初", 3, "$3", SLATE, "起点"),
        (0.480, "现在", 16, "$16", NAVY, "至少"),
        (0.730, "明年", 28, "$28", RED, "三星口径"),
    ]

    ax.plot([0.150, 0.900], [base_y, base_y], color=LIGHT, linewidth=1.4)

    for x, when, val, shown, color, note in bars:
        h = max_h * val / 28.0
        ax.add_patch(Rectangle((x, base_y), 0.120, h, facecolor=color,
                               edgecolor="none"))
        ax.text(x + 0.060, base_y + h + 0.040, shown, fontsize=19, color=color,
                weight="bold", ha="center", va="center")
        ax.text(x + 0.060, base_y - 0.048, when, fontsize=11, color=DARK,
                weight="bold", ha="center", va="center")
        ax.text(x + 0.060, base_y - 0.092, note, fontsize=9.0, color=GRAY,
                ha="center", va="center")

    ax.text(0.355, 0.368, "×5.3", fontsize=13, color=RED, weight="bold",
            ha="center", va="center")
    ax.text(0.605, 0.640, "×1.75", fontsize=13, color=RED, weight="bold",
            ha="center", va="center")

    ax.text(0.150, 0.158, "车规 DDR 由三星、美光、长鑫三家供应，全球统一报价，没有谈判空间",
            fontsize=9.6, color=DARK, va="center")
    ax.text(0.150, 0.112, "建厂到良率爬坡通常 18—24 个月，新产能集中释放要等到 2028 年",
            fontsize=9.6, color=GRAY, va="center")

    punchline(fig, "这不是周期里的讨价还价，是一张没有商量余地的报价单。")
    footer(fig, "单价据地平线余凯给出的区间（年初约 3 美元/GB、当前至少 16 美元/GB、三星称明年 28 美元/GB）；倍数为换算。")
    fig.savefig(OUT + "图2_单价曲线.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.135, 0.910, 0.690])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "三面一起挤", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.888, "售价往下走，成本往上走，中间的缓冲还在变薄",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    def card(x0, y0, w, h, color, title, rows):
        ax.add_patch(Rectangle((x0, y0), w, h, facecolor=PALE,
                               edgecolor=LIGHT, linewidth=1.0))
        ax.add_patch(Rectangle((x0, y0 + h - 0.012), w, 0.012, facecolor=color,
                               edgecolor="none"))
        ax.text(x0 + 0.025, y0 + h - 0.058, title, fontsize=11.6, color=color,
                weight="bold", va="center")
        for i, line in enumerate(rows):
            ax.text(x0 + 0.025, y0 + h - 0.108 - i * 0.052, line, fontsize=9.2,
                    color=DARK, va="center")

    # 中心
    ax.add_patch(Rectangle((0.360, 0.390), 0.280, 0.180, facecolor="white",
                           edgecolor=NAVY, linewidth=1.4))
    ax.text(0.500, 0.508, "整车利润", fontsize=13.5, color=NAVY,
            weight="bold", ha="center", va="center")
    ax.text(0.500, 0.442, "同一块，三面来挤", fontsize=9.4, color=GRAY,
            ha="center", va="center")

    # 上：成本
    card(0.230, 0.700, 0.540, 0.150, RED, "成本在涨", [
        "存储三项合计 +2000 元 至 +2.5 万元",
    ])
    ax.annotate("", xy=(0.500, 0.578), xytext=(0.500, 0.694),
                arrowprops=dict(arrowstyle="-|>", color=RED, linewidth=1.8,
                                shrinkA=0, shrinkB=0))

    # 左：售价
    card(0.020, 0.380, 0.280, 0.190, SLATE, "售价在降", [
        "新能源零售均价",
        "18.4 万 → 15.4 万元",
    ])
    ax.annotate("", xy=(0.352, 0.480), xytext=(0.306, 0.480),
                arrowprops=dict(arrowstyle="-|>", color=SLATE, linewidth=1.8,
                                shrinkA=0, shrinkB=0))

    # 右：账期
    card(0.700, 0.380, 0.280, 0.190, SLATE, "缓冲在薄", [
        "账期收紧至 60 天",
        "且需现金支付",
    ])
    ax.annotate("", xy=(0.648, 0.480), xytext=(0.694, 0.480),
                arrowprops=dict(arrowstyle="-|>", color=SLATE, linewidth=1.8,
                                shrinkA=0, shrinkB=0))

    ax.text(0.360, 0.290, "每车多 5000 元，年销 30 万辆就是 15 亿元", fontsize=10.4,
            color=RED, weight="bold", va="center")
    ax.text(0.360, 0.240, "这笔钱在 2023 年可以用涨价转嫁，现在转不动", fontsize=9.4,
            color=GRAY, va="center")

    punchline(fig, "以前涨价能转嫁给买车的人，现在两头都堵着。")
    footer(fig, "售价据新能源零售均价 2023 年 18.4 万元、2026 年 10 月 15.4 万元；账期指供应商账期治理中 60 天与现金支付要求，属相邻政策面。")
    fig.savefig(OUT + "图3_三面挤压.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")