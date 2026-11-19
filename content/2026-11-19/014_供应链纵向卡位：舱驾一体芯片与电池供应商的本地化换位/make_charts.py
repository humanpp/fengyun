# -*- coding: utf-8 -*-
"""
《供应链的纵向卡位：舱驾一体芯片与电池供应商的「本地化换位」》配套图表
事实口径（2026-11-19，逐条核对官方通稿与公开报道后）：
  · 2026 年 11 月 12 日，新紫光集团与北汽集团在北京举行联合创新中心揭牌暨深化合作签约仪式；
    新紫光集团董事长李滨与北汽集团党委书记、董事长张建勇共同揭牌；
    今年 5 月 18 日双方已签战略合作协议；仪式上新紫光旗下紫光同芯与北汽旗下北汽研究总院
    签署战略合作协议，围绕先进车规工艺舱驾一体 SoC 芯片开展联合研发；
    单颗算力目标 1000TOPS，计划 2028 年实现量产上车；一颗芯片同时承载智驾、智舱、底盘控制，
    以减少域控制器数量、降本降功耗；合作还覆盖 SoC 芯片、舱驾控域控、智能座舱、智能底盘域控，
    并计划延伸到中央计算平台、下一代座舱芯片与商用车
    （新紫光官网、紫光同芯官网、北汽官方、京报网 11-17、36氪 11-13、NE时代 11-17）；
  · 2026 年 11 月 9 日，宝马集团宣布为第六代（Gen6）高压电池新增电芯供应商：
    【三星SDI 供欧洲、LG 新能源供美国】——不是两家都在两地供货；
    两家从各自在该地区的现有工厂供货，时间从 2020 年代后期（late 2020s）开始；
    欧洲电芯来源为宁德时代、亿纬锂能与三星SDI，美国为 LG 新能源
    （宝马集团新闻室 11-09、electrive 11-09、Korea Herald 11-10、Battery-News 11-10）；
  · 「local for local」原则从供应商网络贯穿到 Gen6 高压电池组装，
    组装在宝马于整车厂附近新建的五座工厂进行：德国 Irlbach-Straßkirchen（下巴伐利亚）、
    匈牙利 Debrecen、中国沈阳、美国 Woodruff、墨西哥 San Luis Potosí；
    采购董事 Nicolai Martin、高压电池采购与质量负责人 Hendrik Lang 的相关表述（宝马集团新闻室 11-09）；
  · 美国 Woodruff 工厂 2026 年 11 月 13 日开业投产，投资约 7 亿美元（2022 年 10 月宣布，
    属 17 亿美元美国电动化投资的一部分），约 100 万平方英尺、300 多名员工、250 台机器人，
    距 Spartanburg 整车厂约 24 公里，首批供应全新 iX5；
    Woodruff 是五座 Gen6 电池厂中第四座量产：匈牙利 Debrecen 2025 年 10 月投产，
    德国 Irlbach-Straßkirchen 与中国沈阳 2026 年 10 月投产，墨西哥 San Luis Potosí 计划 2027 年
    （宝马集团新闻室 11-13、bmwblog 11-13、WSPA 11-13、MoneyDJ 11-18、AutoCN 11-15）。
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
    fig = base("一个往上走，一个摊开铺",
               "同样是供应链动作，方向相反：北汽往设计里走，宝马往供应商里铺")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # 左：纵向
    ax.text(0.048, 0.800, "纵向：往前定义", fontsize=11.6, color=NAVY,
            weight="bold", ha="left", va="center")
    ax.text(0.048, 0.752, "北汽 × 新紫光（2026-11-12）", fontsize=8.8,
            color=GRAY, ha="left", va="center")

    layers = [
        ("整车平台与场景定义", "北汽研究总院", 0.620),
        ("联合研发", "舱驾一体 SoC，1000TOPS", 0.470),
        ("芯片设计", "紫光同芯", 0.320),
    ]
    for name, who, y in layers:
        ax.add_patch(FancyBboxPatch((0.048, y - 0.058), 0.400, 0.116,
                                    boxstyle="round,pad=0.006",
                                    facecolor="white", edgecolor=LIGHT,
                                    linewidth=1.0))
        ax.text(0.070, y + 0.020, name, fontsize=9.6, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(0.070, y - 0.030, who, fontsize=8.2, color=GRAY, ha="left",
                va="center")

    for y in (0.560, 0.410):
        ax.add_patch(FancyArrowPatch((0.248, y), (0.248, y - 0.032),
                                     arrowstyle="-|>", mutation_scale=13,
                                     color=NAVY, linewidth=1.2))

    # 右：横向
    ax.text(0.552, 0.800, "横向：摊开铺", fontsize=11.6, color=RED,
            weight="bold", ha="left", va="center")
    ax.text(0.552, 0.752, "宝马 Gen6 电芯（2026-11-09）", fontsize=8.8,
            color=GRAY, ha="left", va="center")

    groups = [
        ("欧洲", ["宁德时代", "亿纬锂能", "三星SDI"], 0.620),
        ("美国", ["LG 新能源"], 0.430),
    ]
    for region, names, y in groups:
        ax.text(0.552, y + 0.086, region, fontsize=9.4, color=SLATE,
                weight="bold", ha="left", va="center")
        for i, nm in enumerate(names):
            x = 0.552 + i * 0.136
            ax.add_patch(FancyBboxPatch((x, y - 0.030), 0.124, 0.070,
                                        boxstyle="round,pad=0.005",
                                        facecolor=PALE, edgecolor="none"))
            ax.text(x + 0.062, y + 0.005, nm, fontsize=8.6, color=DARK,
                    ha="center", va="center")

    ax.text(0.552, 0.330,
            "同一环节，多家分供；三星SDI 只补欧洲，",
            fontsize=8.6, color=SLATE, ha="left", va="center")
    ax.text(0.552, 0.286,
            "LG 只补美国——补的都是自己那一块。",
            fontsize=8.6, color=SLATE, ha="left", va="center")

    ax.plot([0.504, 0.504], [0.250, 0.840], color=LIGHT, linewidth=0.9,
            linestyle=(0, (3, 4)))

    ax.plot([0.030, 0.960], [0.212, 0.212], color=LIGHT, linewidth=0.9)
    ax.text(0.030, 0.156,
            "一个把供应商拉进设计阶段，一个在同一环节里多找几家——"
            "选择哪条，取决于这个环节还有没有「唯一解」。",
            fontsize=9.2, color=SLATE, ha="left", va="center")

    punchline(fig, "北汽在造一颗还不存在的芯片，宝马在买一批已经存在的电芯。")
    footer(fig, "事实：北汽项目据新紫光官网 11-12、京报网 11-17；宝马供应商据宝马集团新闻室 11-09｜制图：本文")
    fig.savefig(OUT + "图1_一个往上走一个摊开铺.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("宝马的「本地服务本地」，落到五座组装厂",
               "电芯在区域内采购，电池包在整车厂旁边组装")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    plants = [
        ("匈牙利", "Debrecen", "2025 年 10 月", "已投产", SLATE),
        ("德国", "Irlbach-Straßkirchen", "2026 年 10 月", "已投产", SLATE),
        ("中国", "沈阳", "2026 年 10 月", "已投产", SLATE),
        ("美国", "Woodruff", "2026 年 11 月 13 日", "已投产", RED),
        ("墨西哥", "San Luis Potosí", "计划 2027 年", "待投产", LIGHT),
    ]

    ax.text(0.030, 0.800, "五座 Gen6 电池组装厂", fontsize=10.4, color=DARK,
            weight="bold", ha="left", va="center")

    x = 0.030
    w = 0.182
    for i, (country, city, when, status, color) in enumerate(plants):
        xx = x + i * 0.190
        ax.add_patch(FancyBboxPatch((xx, 0.470), w, 0.250,
                                    boxstyle="round,pad=0.006",
                                    facecolor="white", edgecolor=LIGHT,
                                    linewidth=1.0))
        ax.add_patch(Rectangle((xx, 0.714), w, 0.006, facecolor=color,
                               edgecolor="none"))
        ax.text(xx + 0.018, 0.652, country, fontsize=10.4, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(xx + 0.018, 0.594, city, fontsize=7.8, color=GRAY, ha="left",
                va="center")
        ax.plot([xx + 0.018, xx + w - 0.018], [0.558, 0.558], color=LIGHT,
                lw=0.8)
        ax.text(xx + 0.018, 0.518, when, fontsize=8.0, color=color if color is RED else SLATE,
                weight="bold", ha="left", va="center")
        ax.text(xx + 0.018, 0.484, status, fontsize=7.8, color=GRAY,
                ha="left", va="center")

    # 电芯来源
    ax.plot([0.030, 0.960], [0.418, 0.418], color=LIGHT, linewidth=0.9)
    ax.text(0.030, 0.362, "电芯来自哪里", fontsize=9.0, color=GRAY, ha="left",
            va="center")

    ax.text(0.170, 0.310, "欧洲", fontsize=9.4, color=NAVY, weight="bold",
            ha="left", va="center")
    ax.text(0.230, 0.310, "宁德时代　·　亿纬锂能　·　三星SDI", fontsize=9.2,
            color=DARK, ha="left", va="center")
    ax.text(0.170, 0.244, "美国", fontsize=9.4, color=RED, weight="bold",
            ha="left", va="center")
    ax.text(0.230, 0.244, "LG 新能源", fontsize=9.2, color=DARK, ha="left",
            va="center")

    ax.text(0.030, 0.160,
            "两家新供应商从 2020 年代后期起、用各自在该地区的现有工厂供货；"
            "美国 Woodruff 厂投资约 7 亿美元，距 Spartanburg 整车厂约 24 公里，首批供 iX5。",
            fontsize=8.8, color=SLATE, ha="left", va="center")

    punchline(fig, "「本地服务本地」不是口号：电芯、电池包、整车，三段都在同一个区域内完成。")
    footer(fig, "事实：五座工厂与电芯来源据宝马集团新闻室 11-09、11-13；"
                "Woodruff 投资与距离据 bmwblog 11-13、MoneyDJ 11-18｜制图：本文")
    fig.savefig(OUT + "图2_五座组装厂.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("两件事，都不在今年落地",
               "一个是协议，一个是产能；真正的时间点都在后面")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # 左轴：北汽
    ax.text(0.030, 0.792, "北汽 × 新紫光", fontsize=10.6, color=NAVY,
            weight="bold", ha="left", va="center")
    left = [
        ("2026-05-18", "签战略合作协议", 0.700),
        ("2026-11-12", "联合创新中心揭牌", 0.580),
        ("2028 年", "计划量产上车", 0.460),
    ]
    ax.plot([0.078, 0.078], [0.420, 0.740], color=LIGHT, linewidth=1.4)
    for date, note, y in left:
        ax.plot([0.078], [y], marker="o", markersize=7.0,
                color=RED if "2028" in date else NAVY, zorder=3)
        ax.text(0.104, y + 0.026, date, fontsize=9.4, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(0.104, y - 0.026, note, fontsize=8.6, color=GRAY, ha="left",
                va="center")

    # 右轴：宝马
    ax.text(0.530, 0.792, "宝马 Gen6 电芯", fontsize=10.6, color=RED,
            weight="bold", ha="left", va="center")
    right = [
        ("2025-10", "匈牙利厂投产", 0.700),
        ("2026-10", "德国、沈阳厂投产", 0.600),
        ("2026-11-09", "新增两家电芯供应商", 0.500),
        ("2026-11-13", "美国 Woodruff 厂投产", 0.400),
        ("2020 年代后期", "新供应商开始供货", 0.300),
        ("2027 年", "墨西哥厂计划投产", 0.200),
    ]
    ax.plot([0.578, 0.578], [0.170, 0.740], color=LIGHT, linewidth=1.4)
    for date, note, y in right:
        ax.plot([0.578], [y], marker="o", markersize=6.4,
                color=RED if "2026-11" in date else SLATE, zorder=3)
        ax.text(0.604, y + 0.022, date, fontsize=9.0, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(0.750, y + 0.022, note, fontsize=8.4, color=GRAY, ha="left",
                va="center")

    ax.text(0.030, 0.118,
            "一个还在图纸上，一个已经在供货——但它们都要到「后面几年」才见分晓。"
            "2026 年宣布的动作，兑现期都在 2027 到 2029 年之间。",
            fontsize=9.0, color=SLATE, ha="left", va="center")

    punchline(fig, "签字在今年，交货在三到五年后——这两笔都是长期下注。")
    footer(fig, "事实：北汽时间线据新紫光官网 11-12、京报网 11-17；宝马时间线据宝马集团新闻室 "
                "11-09 与 11-13、AutoCN 11-15｜制图：本文")
    fig.savefig(OUT + "图3_两件事都不在今年落地.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)