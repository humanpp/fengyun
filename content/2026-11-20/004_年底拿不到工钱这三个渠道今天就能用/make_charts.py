# -*- coding: utf-8 -*-
"""
《年底拿不到工钱，这三个渠道今天就能用》配套图表
事实口径：
  · 2026-11-18 国务院就业促进和劳动保护工作领导小组办公室召开
    2026 年治理欠薪冬季行动动员部署视频会（中国组织人事报 11-19）；
  · 2026-11-15 新华社：北京部署 2026 年"安薪北京"冬季行动，
    20 多个部门联动，聚焦工程建设、环卫、保安等劳动密集型行业
    与政府、国企项目，查实欠薪案件 2027 年春节前实质性化解、动态清零；
  · 渠道：12333（人社劳动保障热线）、12345（政务服务便民热线）、
    "全国根治欠薪线索反映平台"（人社部公众号"服务互动—根治欠薪"为
    主入口，国务院客户端等同步加载）。
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
    fig = base("三个渠道",
               "都是公开、免费、当天就能用的入口")
    ax = canvas(fig)

    cards = [
        ("12333", "人社劳动保障热线",
         "欠薪投诉举报与政策咨询\n北京 12333 提供 24 小时政策解读", NAVY),
        ("12345", "政务服务便民热线",
         "覆盖广、有办理时限与回访\n不知道该找谁时，它会转办", SLATE),
        ("线上平台", "全国根治欠薪线索反映平台",
         "人社部公众号「服务互动—根治欠薪」\n也可从国务院客户端等进入", GREEN),
    ]

    y_top = 0.855
    h = 0.170
    gap = 0.045
    for i, (num, name, desc, color) in enumerate(cards):
        y = y_top - i * (h + gap)
        ax.add_patch(FancyBboxPatch((0.065, y - h), 0.870, h,
                                    boxstyle="round,pad=0.012",
                                    facecolor="#f7f8fa", edgecolor=color,
                                    linewidth=1.2))
        # 左侧色块 + 编号
        ax.add_patch(Rectangle((0.065, y - h), 0.012, h, facecolor=color,
                               edgecolor="none"))
        ax.text(0.110, y - h / 2, num, fontsize=20.0, color=color,
                weight="bold", ha="left", va="center")
        ax.text(0.335, y - 0.048, name, fontsize=12.2, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(0.335, y - 0.112, desc, fontsize=9.4, color=SLATE, ha="left",
                va="center", linespacing=1.5)

    ax.text(0.065, 0.128,
            "注：三个渠道可同时使用，不冲突；建议先打 12333，同时线上提交线索，留下时间记录。",
            fontsize=8.8, color=GRAY, ha="left", va="center")

    punchline(fig, "工钱没到手，先别急着回家——今天就打。")
    footer(fig, "事实：渠道信息据人力资源和社会保障部公开说明、北京市人社局公开信息｜制图：本文")
    fig.savefig(OUT + "图1_三个渠道.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("平台怎么用",
               "全国根治欠薪线索反映平台：从入口到分办")
    ax = canvas(fig)

    steps = [
        ("1", "找入口", "人社部公众号「服务互动—根治欠薪」\n或国务院客户端、电子社保卡等"),
        ("2", "实名登录", "平台需实名认证；\n网络不稳时换个网络再试"),
        ("3", "选领域", "工程建设领域 / 非工程建设领域"),
        ("4", "勾选地区", "下拉菜单选到用工所在地的县（区）\n这一步决定线索分给谁"),
        ("5", "提交", "填拖欠单位等必填项\n提交后可用「补充说明」更正"),
    ]

    x0 = 0.075
    y = 0.870
    row_h = 0.132
    for i, (n, title, desc) in enumerate(steps):
        yy = y - i * row_h
        ax.add_patch(plt.Circle((x0 + 0.022, yy - 0.028), 0.021,
                                facecolor=NAVY, edgecolor="none", zorder=5))
        ax.text(x0 + 0.022, yy - 0.028, n, fontsize=10.4, color="white",
                weight="bold", ha="center", va="center", zorder=6)
        ax.text(x0 + 0.062, yy - 0.028, title, fontsize=12.0, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(x0 + 0.230, yy - 0.028, desc, fontsize=9.6, color=SLATE,
                ha="left", va="center", linespacing=1.5)
        if i < len(steps) - 1:
            ax.plot([x0 + 0.022, x0 + 0.022], [yy - 0.055, yy - row_h + 0.020],
                    color=LIGHT, linewidth=1.6, zorder=1)

    # 底部说明块（放在步骤列表下方，留出间距）
    ax.add_patch(FancyBboxPatch((0.075, 0.150), 0.860, 0.088,
                                boxstyle="round,pad=0.010", facecolor=SAND,
                                edgecolor="#d9cdb6", linewidth=1.0))
    ax.text(0.098, 0.194,
            "提交后：平台自动分发至用工所在地地市级人社部门，由其直接办理或交县（区）办理。",
            fontsize=9.8, color="#7a6746", ha="left", va="center")

    punchline(fig, "地区那一栏填错，线索就分不到对的人手上。")
    footer(fig, "事实：平台流程据人力资源和社会保障部、安康市人社局公开答疑（根治欠薪线索反映平台）｜制图：本文")
    fig.savefig(OUT + "图2_平台怎么用.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("提交前先备好这些",
               "有就带上，没有也不妨碍提交——但越全越省事")
    ax = canvas(fig)

    items = [
        ("身份信息", "本人身份证（平台需实名认证）", True),
        ("干活的地方", "工地/单位名称、地址，具体到区县", True),
        ("给谁干的", "总包单位、分包单位、包工头姓名电话", True),
        ("欠多少、欠多久", "金额、起止月份", True),
        ("干过活的证据", "合同、工资条、考勤、工牌、微信记录、转账截图", False),
    ]

    y = 0.880
    for i, (head, body, must) in enumerate(items):
        yy = y - i * 0.115
        color = NAVY if must else GOLD
        ax.add_patch(Rectangle((0.075, yy - 0.040), 0.006, 0.062,
                               facecolor=color, edgecolor="none"))
        ax.text(0.098, yy - 0.009, head, fontsize=11.2, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(0.300, yy - 0.009, body, fontsize=9.8, color=SLATE, ha="left",
                va="center")

    # 两个常见疑问（置于列表下方，留足间距）
    ax.add_patch(FancyBboxPatch((0.075, 0.150), 0.860, 0.175,
                                boxstyle="round,pad=0.012", facecolor=PALE,
                                edgecolor=LIGHT, linewidth=1.0))
    ax.text(0.098, 0.288, "两个最常问的", fontsize=9.6, color=SLATE,
            weight="bold", ha="left", va="center")
    ax.text(0.098, 0.236,
            "没合同、没工资条 → 不妨碍提交，监察机构会依法核实；但证据越全越省事。",
            fontsize=9.8, color=DARK, ha="left", va="center")
    ax.text(0.098, 0.184,
            "不是农民工 → 属于劳动保障监察范围的欠薪都能反映，处理方式没有区别。",
            fontsize=9.8, color=DARK, ha="left", va="center")

    punchline(fig, "证据不用完美，先让线索进队列。")
    footer(fig, "事实：材料与口径据人力资源和社会保障部公开答疑；《劳动保障监察条例》第二十条为 2 年查处时效｜制图：本文")
    fig.savefig(OUT + "图3_提交前先备好这些.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)
