# -*- coding: utf-8 -*-
"""
《34 家领航级智能工厂公布，汽车占 4 席》配套图表
事实口径（均经公开报道交叉核对）：
  · 2026-11-18 工业和信息化部等六部门印发《2026 年度领航级智能工厂培育名单》
    （工信厅联通装函〔2026〕562 号），共 34 家；11-19 在 2026 世界智能制造大会上正式公布。
    领航级为智能工厂梯度培育体系最高层级，其下依次为基础级、先进级、卓越级。
    —— 工信部官网、经济参考报、IT之家 2026-11-19。
  · 名单中汽车相关 4 家（IT之家所附官方名单序号）：
    1 小米汽车科技有限公司「AI 驱动的敏捷制造高端新能源汽车超级智能工厂」（北京）
    4 中信戴卡股份有限公司「全球价值共创的极致韧性铝制轻量化汽车零部件智能工厂」（河北）
    7 一汽—大众汽车有限公司「油电混共融的多车型混流敏捷智造母工厂」（吉林）
    29 赛力斯汽车有限公司「产业大脑驱动的全域融合新能源汽车智能工厂」（重庆）
    —— IT之家 2026-11-19 附官方名单；汽车之家 2026-10-28。
  · 34 家整体数据：全员劳动生产率平均提升 34.4%、生产效率平均提升 19.3%，
    累计带动近 4000 家企业协同升级；覆盖 20 个省区市；首次纳入医药（天士力）、
    服装（海澜之家）企业。—— 经济参考报、IT之家 2026-11-19。
  · 赛力斯超级工厂：超 3000 台机器人协同作业、关键工序 100% 自动化、
    质量检测 100% 自动化、AI 视觉检测；万吨级超级智能压铸单元把数百个零部件一次集成；
    "厂中厂"模式引入宁德时代，2025-06-30 两条 CTP 2.0 电池包产线投产，
    2026-10-10 签长期协议扩建二期（年规划 10—12GWh，一二期合计超 20GWh）；
    "工厂自动驾驶测试"新模式（车辆从下线检测到入库全程无人化）于 2026-05-27 发布会宣布。
    —— 赛力斯官网、宁德时代官网、新华网、汽车之家/希鸥网 2026-11-19、一页电车 2026-06。
  · 一汽-大众：2026-08 批售 6.9 万辆同比降 48%，前 8 个月累计批售 65.11 万辆同比降近 34%；
    大众在华前三季度交付 137.9 万辆同比降 30.2%。佛山工厂焊装车间实现 8 款产品混线、
    19 种制造工艺并行；天津分公司 2026-10 启动改造，完成后具备"油电混全品类"生产能力。
    —— 新浪财经 2026-09-21、钛媒体 2026-10-13、新华网 2026-10-16、天津日报 2026-10-27。
  · 中信戴卡：全球最大铝车轮和铝制底盘零部件供应商，2026 全球汽车零部件供应商百强第 36 位；
    此前已以"轻量化铝制汽车零部件柔性化生产智能工厂"入选首批卓越级智能工厂。
    —— 中信戴卡招聘资料、长城网 2026-04-23、世铝网 2026-11-19。
说明：素材称"汽车及相关领域占 4 席"经核属实（含零部件企业中信戴卡）；
      多数媒体报道只提"3 家车企入选"，因中信戴卡为零部件企业，两者口径不同。
风格：克制传媒风，白底、低饱和配色、标题即结论。输出目录 = 脚本所在目录。
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle

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
GOLD = "#c9a27a"
GREEN = "#5a7d6f"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep


def base(title, sub):
    fig = plt.figure(figsize=(12, 6.8))
    fig.patch.set_facecolor("white")
    fig.text(0.045, 0.950, title, fontsize=20, color=DARK, weight="bold",
             ha="left", va="top")
    fig.text(0.045, 0.878, sub, fontsize=10.8, color=GRAY, ha="left", va="top")
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
    fig = base("34 家，汽车占 4 席",
               "2026 年度领航级智能工厂培育名单里的汽车样本")
    ax = canvas(fig)

    # 左侧：总数
    ax.text(0.075, 0.780, "全国入选", fontsize=9.6, color=GRAY, ha="left",
            va="center")
    ax.text(0.075, 0.690, "34", fontsize=52, color=NAVY, weight="bold",
            ha="left", va="center")
    ax.text(0.205, 0.665, "家", fontsize=13.0, color=NAVY, ha="left",
            va="center")

    ax.text(0.075, 0.560, "其中汽车相关", fontsize=9.6, color=GRAY, ha="left",
            va="center")
    ax.text(0.075, 0.470, "4", fontsize=52, color=RED, weight="bold",
            ha="left", va="center")
    ax.text(0.135, 0.445, "席", fontsize=13.0, color=RED, ha="left",
            va="center")
    ax.text(0.075, 0.375, "3 家整车 + 1 家零部件", fontsize=9.4, color=SLATE,
            ha="left", va="center")

    # 右侧：四家卡片
    cards = [
        ("小米汽车", "AI 驱动的敏捷制造\n高端新能源汽车超级智能工厂", "北京", "1", NAVY),
        ("一汽-大众", "油电混共融的多车型\n混流敏捷智造母工厂", "吉林", "7", GOLD),
        ("赛力斯", "产业大脑驱动的\n全域融合新能源汽车智能工厂", "重庆", "29", GREEN),
        ("中信戴卡", "全球价值共创的极致韧性\n铝制轻量化汽车零部件智能工厂", "河北", "4", RED),
    ]

    y_top = 0.815
    for i, (name, proj, loc, num, col) in enumerate(cards):
        y = y_top - i * 0.190
        ax.add_patch(FancyBboxPatch((0.400, y - 0.160), 0.530, 0.160,
                                    boxstyle="round,pad=0.008",
                                    facecolor="#fafbfc", edgecolor=col,
                                    linewidth=1.1))
        ax.text(0.418, y - 0.040, name, fontsize=11.6, color=col,
                weight="bold", ha="left", va="center")
        ax.text(0.418, y - 0.098, proj, fontsize=8.4, color=SLATE,
                ha="left", va="center", linespacing=1.6)
        ax.text(0.912, y - 0.040, loc, fontsize=8.8, color=GRAY, ha="right",
                va="center")
        ax.text(0.912, y - 0.098, f"名单序号 {num}", fontsize=8.2, color=GRAY,
                ha="right", va="center")

    punchline(fig, "四家里三家造整车，一家造轮子——都是车企，只是站位不同。")
    footer(fig, "事实：工信部等六部门 2026-11-18 印发名单，序号据 IT之家 2026-11-19 所附官方名单｜制图：本文")
    fig.savefig(OUT + "图1_34家占4席.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("四种样本，四种解法",
               "同是“智能工厂”，解决的问题并不一样")
    ax = canvas(fig)

    rows = [
        ("小米汽车", "AI 驱动敏捷制造", "新车企，一款车要快速爬产", NAVY),
        ("赛力斯", "产业大脑 + 厂中厂", "供应链距离要压到最短", GREEN),
        ("一汽-大众", "油电混线柔性共融", "燃油与纯电都要在同一厂摊成本", GOLD),
        ("中信戴卡", "极致韧性 + 轻量化", "多品种小批量，还要属地化配套", RED),
    ]

    y_top = 0.845
    for i, (name, method, problem, col) in enumerate(rows):
        y = y_top - i * 0.168
        ax.add_patch(FancyBboxPatch((0.070, y - 0.140), 0.860, 0.140,
                                    boxstyle="round,pad=0.008",
                                    facecolor="#fafbfc", edgecolor=col,
                                    linewidth=1.1))
        ax.add_patch(FancyBboxPatch((0.070, y - 0.140), 0.008, 0.140,
                                    boxstyle="square,pad=0",
                                    facecolor=col, edgecolor="none"))
        ax.text(0.098, y - 0.038, name, fontsize=12.4, color=col,
                weight="bold", ha="left", va="center")
        ax.text(0.098, y - 0.098, method, fontsize=9.2, color=DARK,
                ha="left", va="center")

        ax.plot([0.500, 0.500], [y - 0.122, y - 0.018], color=LIGHT,
                linewidth=1.0)
        ax.text(0.525, y - 0.066, problem, fontsize=9.4, color=SLATE,
                ha="left", va="center")

    ax.text(0.070, 0.155,
            "共同点：都不是“买几台机器人”，而是拿制造体系去换成本、换响应速度。",
            fontsize=9.4, color=DARK, weight="bold", ha="left", va="center")

    punchline(fig, "自动化只是入场券，真正的考题是柔性、嵌入和摊薄。")
    footer(fig, "说明：右栏为本文据各企业项目名称与公开报道归纳，非企业自述｜制图：本文")
    fig.savefig(OUT + "图2_四种样本.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("一汽-大众的账",
               "批售腰斩的同一时期，它拿了个“混线”的奖")
    ax = canvas(fig)

    # 左：销量下滑
    ax.text(0.075, 0.800, "2026 年批售（万辆）", fontsize=10.4, color=NAVY,
            weight="bold", ha="left", va="center")

    bars = [
        ("2026 年 8 月", 6.9, "同比 −48%"),
        ("2026 年前 8 月累计", 65.11, "同比 −34%"),
    ]
    x_left = 0.230
    x_scale = 0.0088

    for i, (label, val, chg) in enumerate(bars):
        y = 0.700 - i * 0.135
        ax.text(x_left - 0.016, y, label, fontsize=9.4, color=DARK,
                ha="right", va="center")
        w = val * x_scale
        ax.add_patch(FancyBboxPatch((x_left, y - 0.030), w, 0.060,
                                    boxstyle="round,pad=0.002",
                                    facecolor=NAVY, edgecolor="none",
                                    alpha=0.90, zorder=3))
        ax.text(x_left + w + 0.014, y, f"{val}", fontsize=10.0, color=NAVY,
                weight="bold", ha="left", va="center")
        ax.text(x_left + w + 0.070, y, chg, fontsize=9.0, color=RED,
                weight="bold", ha="left", va="center")

    # 右：混线能力
    ax.add_patch(FancyBboxPatch((0.075, 0.240), 0.860, 0.240,
                                boxstyle="round,pad=0.010", facecolor="#edf2f0",
                                edgecolor=GREEN, linewidth=1.2))
    ax.text(0.098, 0.440, "同一时期的制造侧动作", fontsize=10.4,
            color=GREEN, weight="bold", ha="left", va="center")
    ax.text(0.098, 0.385,
            "佛山工厂焊装车间：8 款产品混线生产、19 种制造工艺并行",
            fontsize=9.4, color=DARK, ha="left", va="center")
    ax.text(0.098, 0.335,
            "天津分公司 2026 年 10 月启动改造，完成后具备“油电混全品类”产能",
            fontsize=9.4, color=DARK, ha="left", va="center")
    ax.text(0.098, 0.285,
            "入选项目名：油电混共融的多车型混流敏捷智造母工厂",
            fontsize=9.4, color=GREEN, weight="bold", ha="left", va="center")

    ax.text(0.075, 0.190,
            "销量掉得越狠，把燃油和纯电塞进同一条线摊固定成本就越急。",
            fontsize=9.4, color=RED, weight="bold", ha="left", va="center")

    punchline(fig, "“混线”不是技术炫技，是产能利用率下滑时的止血方案。")
    footer(fig, "事实：批售数据据乘联分会、新浪财经 2026-09-21；佛山/天津产线据新华网 2026-10-16、天津日报 2026-10-27｜制图：本文")
    fig.savefig(OUT + "图3_一汽大众的账.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)
