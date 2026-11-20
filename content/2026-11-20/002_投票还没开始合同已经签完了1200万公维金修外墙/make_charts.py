# -*- coding: utf-8 -*-
"""
《投票还没开始，合同已经签完了》配套图表
事实口径（均据北京日报客户端 2026-11-18 报道，记者鹿艺佳）：
  · 昌平区融泽嘉园中6号院，2014/2015 年陆续入住；
  · 2025-12-02 物业与施工单位签《中标通知书》；
    2025-12-30 签《工程施工承包合同》；
    2026 年二三月份才组织业主投票（物业承认），且投票结果不公示；
    2026-01-30 发布公告，申请外墙大修公维金 1200 余万元；
  · 2025-11 消防改造走应急程序支取 600 余万元，
    2025-11-01 张贴应急使用公告，
    《消防设施维修施工通知》载 2024-09 启动招标、2025-05 选定施工单位、
    2025-08 至 10 完成监理与施工合同签订；
  · 两笔合计近 1900 万元（原报道口径；两数相加为 1800 余万元）。
风格：克制传媒风，白底、低饱和配色、标题即结论。输出目录 = 脚本所在目录。
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch, Circle

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
    fig = base("合同在前，投票在后",
               "2026 年 11 月 18 日北京日报披露：外墙大修 1200 余万元公维金的实际顺序")
    ax = canvas(fig)

    y = 0.620
    ax.plot([0.075, 0.925], [y, y], color=LIGHT, linewidth=2.0)

    # 四个节点按时间顺序横排，标签上下交替，避免重叠
    # (x, 日期, 说明, 颜色, 是否在上方)
    nodes = [
        (0.115, "2025.12.02", "签《中标通知书》", NAVY, True),
        (0.355, "2025.12.30", "签《工程施工承包合同》", NAVY, False),
        (0.605, "2026.01.30", "发布公告，申请 1200 余万元", GOLD, True),
        (0.875, "2026 年二三月份", "才组织业主投票", RED, False),
    ]
    for x, date, desc, color, up in nodes:
        r = 0.019 if color is RED else 0.013
        ax.add_patch(Circle((x, y), r, facecolor=color, edgecolor="white",
                            linewidth=1.8, zorder=6))
        if up:
            ax.text(x, y + 0.048, date, fontsize=11.0, color=color,
                    weight="bold", ha="center", va="bottom")
            ax.text(x, y + 0.014, desc, fontsize=9.0, color=DARK,
                    ha="center", va="bottom")
        else:
            ax.text(x, y - 0.048, date, fontsize=11.0, color=color,
                    weight="bold", ha="center", va="top")
            ax.text(x, y - 0.082, desc, fontsize=9.0, color=DARK,
                    ha="center", va="top")

    # 在时间轴下方标注：投票本应在前
    ax.text(0.875, y - 0.132, "且结果不公示", fontsize=8.6, color=GRAY,
            ha="center", va="top")
    ax.text(0.500, y + 0.155, "投票是法定前置程序，却排在合同之后",
            fontsize=13.0, color=RED, weight="bold", ha="center", va="center")

    # 下方说明块
    ax.add_patch(FancyBboxPatch((0.070, 0.150), 0.860, 0.150,
                                boxstyle="round,pad=0.012", facecolor=SAND,
                                edgecolor="#d9cdb6", linewidth=1.0))
    ax.text(0.095, 0.250, "《民法典》第二百七十八条", fontsize=9.6,
            color="#8a7a5e", ha="left", va="center")
    ax.text(0.095, 0.196,
            "\"使用建筑物及其附属设施的维修资金\"属业主共同决定事项；"
            "第二百八十一条：该资金属于业主共有。",
            fontsize=10.2, color="#7a6746", ha="left", va="center")

    punchline(fig, "合同签完两个月，投票才开始——投的是票，定的是既成事实。")
    footer(fig, "事实：签约与投票时间据 2026-11-18《北京日报》报道（记者鹿艺佳）｜制图：本文")
    fig.savefig(OUT + "图1_合同在前投票在后.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("两套顺序",
               "专家给出的正确流程，与这个小区实际发生的流程")
    ax = canvas(fig)

    left_x, right_x = 0.075, 0.545
    w, h, gap = 0.355, 0.082, 0.023

    # 标题
    ax.text(left_x, 0.925, "应该的顺序", fontsize=12.4, color=NAVY,
            weight="bold", ha="left", va="center")
    ax.text(right_x, 0.925, "实际发生的顺序", fontsize=12.4, color=RED,
            weight="bold", ha="left", va="center")

    correct = ["立项公示", "业主投票", "表决通过", "招投标", "签订合同", "施工"]
    actual = ["招投标", "签订合同", "发布公告", "施工在即", "业主投票"]

    yy = 0.860
    for i, txt in enumerate(correct):
        ax.add_patch(Rectangle((left_x, yy - h), w, h, facecolor="#e8edf3",
                               edgecolor=NAVY, linewidth=1.0))
        ax.text(left_x + 0.020, yy - h / 2, "%d" % (i + 1), fontsize=9.6,
                color=NAVY, weight="bold", ha="left", va="center")
        ax.text(left_x + 0.062, yy - h / 2, txt, fontsize=10.8, color=DARK,
                ha="left", va="center")
        yy -= (h + gap)

    yy = 0.860
    for i, txt in enumerate(actual):
        is_bad = txt in ("签订合同", "业主投票")
        fc = "#f6e4e1" if is_bad else "#f4f5f7"
        ec = RED if is_bad else LIGHT
        ax.add_patch(Rectangle((right_x, yy - h), w, h, facecolor=fc,
                               edgecolor=ec, linewidth=1.0))
        ax.text(right_x + 0.020, yy - h / 2, "%d" % (i + 1), fontsize=9.6,
                color=RED if is_bad else SLATE, weight="bold", ha="left",
                va="center")
        ax.text(right_x + 0.062, yy - h / 2, txt, fontsize=10.8,
                color=DARK if not is_bad else RED, ha="left", va="center")
        yy -= (h + gap)

    # 中间箭头
    ax.annotate("", xy=(0.505, 0.620), xytext=(0.462, 0.620),
                arrowprops=dict(arrowstyle="-|>", color=GRAY, linewidth=1.6))
    ax.text(0.484, 0.575, "顺序颠倒", fontsize=8.6, color=GRAY, ha="center",
            va="center")

    ax.text(0.075, 0.118,
            "注：右侧为报道中可核对的时间点归纳；\"施工在即\"指 2026 年 1 月 30 日公告时大修已进入实施阶段。",
            fontsize=8.6, color=GRAY, ha="left", va="center")

    punchline(fig, "顺序一换，投票就从\"决定\"变成了\"追认\"。")
    footer(fig, "事实：正确流程为北京市社会科学院社会学所副研究员赵小平表述；时间点据 2026-11-18《北京日报》报道｜制图：本文")
    fig.savefig(OUT + "图2_两套顺序.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("同一笔钱，不到 3 个月动了两次",
               "2025 年 11 月至 2026 年 1 月：应急程序 600 余万元，普通流程 1200 余万元")
    ax = canvas(fig)

    base_y = 0.330
    ax.plot([0.070, 0.930], [base_y, base_y], color=LIGHT, linewidth=1.0)

    # 左柱：消防（应急）
    ax.add_patch(Rectangle((0.140, base_y), 0.170, 0.300, facecolor=SLATE,
                           edgecolor="none"))
    ax.text(0.225, base_y + 0.310, "600 余万", fontsize=22.0, color=SLATE,
            weight="bold", ha="center", va="bottom")
    ax.text(0.225, base_y - 0.045, "消防改造", fontsize=11.0, color=DARK,
            ha="center", va="top")
    ax.text(0.225, base_y - 0.098, "应急程序 · 无需业主同意", fontsize=8.8,
            color=GRAY, ha="center", va="top")

    # 右柱：外墙（普通）
    ax.add_patch(Rectangle((0.560, base_y), 0.170, 0.600, facecolor=RED,
                           edgecolor="none"))
    ax.text(0.645, base_y + 0.610, "1200 余万", fontsize=22.0, color=RED,
            weight="bold", ha="center", va="bottom")
    ax.text(0.645, base_y - 0.045, "外墙大修", fontsize=11.0, color=DARK,
            ha="center", va="top")
    ax.text(0.645, base_y - 0.098, "普通流程 · 应先经业主投票", fontsize=8.8,
            color=GRAY, ha="center", va="top")

    # 合计
    ax.add_patch(FancyBboxPatch((0.780, 0.470), 0.150, 0.200,
                                boxstyle="round,pad=0.012", facecolor=SAND,
                                edgecolor="#d9cdb6", linewidth=1.0))
    ax.text(0.855, 0.610, "合计", fontsize=9.4, color="#8a7a5e", ha="center",
            va="center")
    ax.text(0.855, 0.535, "近 1900 万", fontsize=13.6, color="#7a6746",
            weight="bold", ha="center", va="center")

    # 两次之间的时间
    ax.annotate("", xy=(0.560, 0.245), xytext=(0.310, 0.245),
                arrowprops=dict(arrowstyle="<->", color=DARK, linewidth=1.0))
    ax.text(0.435, 0.278, "不到 3 个月", fontsize=10.0, color=DARK,
            weight="bold", ha="center", va="bottom")

    ax.text(0.070, 0.150,
            "注：应急公维金依北京市《关于简化程序方便应急情况下使用住宅专项维修资金有关问题的通知》无需经业主同意；"
            "\"近 1900 万\"为原报道口径，两数相加为 1800 余万元。",
            fontsize=8.4, color=GRAY, ha="left", va="center")

    punchline(fig, "一次是法规允许的例外，一次是本该投票的常规——两次都绕开了业主。")
    footer(fig, "事实：金额与流程据 2026-11-18《北京日报》报道及该报同日评论｜制图：本文")
    fig.savefig(OUT + "图3_两次动用.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)
