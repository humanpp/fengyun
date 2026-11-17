# -*- coding: utf-8 -*-
"""
《AI「馆长」喊了声爸妈：上千位老人，为一句天价估价掏了上千万》配套图表
事实口径：2026-11-13 警方披露的"免费鉴宝、高价回收"诈骗案——涉案超千万元、
受害者上千人、多为老年人；AI 鉴宝视频引流 → 填信息 → 私密直播间 → 伪装
"博物馆馆长"虚估天价、认"爸妈" → 收"插队鉴定费""门槛费""保证金" →
"砸金蛋"奖品与中奖记录伪造 → 老人只拿到廉价假藏品。
风格：克制传媒风，白底、低饱和配色、标题即结论
输出目录 = 脚本所在目录
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch, Circle

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
    ax = fig.add_axes([0.045, 0.105, 0.910, 0.720])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "一条视频，到一件假货", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.885,
             "上千位老人走完的六步——每一步都是他自愿点的",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    steps = [
        ("刷到视频", "AI 生成的「专家」\n说高价回收钱币、\n字画、文玩，\n可先打钱再上门"),
        ("填信息", "电话、地址、\n藏品照片\n全都留下，\n然后被人加了微信"),
        ("进直播间", "私密直播间，\n外人刷不到，\n只对筛过的\n「客户」开放"),
        ("喊一声爸妈", "主播自称\n「博物馆馆长」，\n先认亲，\n再许诺养老金"),
        ("开始收费", "插队鉴定费、\n门槛费、\n保证金，\n一笔几百到几千"),
        ("拿到假货", "砸金蛋的奖品\n和中奖记录\n都是伪造的，\n藏品是廉价货"),
    ]

    y_line = 0.780
    ax.plot([0.02, 0.98], [y_line, y_line], color=LIGHT, linewidth=2.4,
            solid_capstyle="round", zorder=1)

    card_top, card_bot = 0.660, 0.200
    bw = 0.152
    for i, (title, body) in enumerate(steps):
        x = 0.085 + i * 0.163
        color = NAVY if i < 4 else RED

        ax.scatter([x], [y_line], s=560, facecolor=color, edgecolor="white",
                   linewidth=2.0, zorder=3)
        ax.text(x, y_line, str(i + 1), fontsize=10.5, color="white",
                ha="center", va="center", zorder=4)

        ax.plot([x, x], [y_line - 0.024, card_top], color=LIGHT, linewidth=1.3,
                zorder=1, linestyle=(0, (3, 2)))
        ax.add_patch(Rectangle((x - bw / 2, card_bot), bw, card_top - card_bot,
                               facecolor=PALE, edgecolor=LIGHT, linewidth=1.0,
                               zorder=2))
        ax.add_patch(Rectangle((x - bw / 2, card_top - 0.011), bw, 0.011,
                               facecolor=color, edgecolor="none", zorder=3))
        ax.text(x - bw / 2 + 0.014, card_top - 0.115, title, fontsize=11,
                color=color, weight="bold", ha="left", va="top", zorder=4)
        ax.text(x - bw / 2 + 0.014, card_top - 0.171, body, fontsize=8.8,
                color=DARK, ha="left", va="top", zorder=4, linespacing=1.75)

    punchline(fig, "六步里没有一步是强迫的——这正是它难防的原因。")
    footer(fig, "据 2026 年 11 月 13 日警方披露的案情整理；平台名称、单笔金额未在公开信息中披露。")
    fig.savefig(OUT + "图1_一条链.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.135, 0.910, 0.690])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "三个名目，一个方向：钱只往外走", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.882, "他说得越像行规，老人越不好意思问「这钱退不退」",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    cards = [
        (0.005, "插队鉴定费",
         "「排队的人太多，\n交钱就能往前排」",
         "钱交了，队列不存在，\n鉴定也从来没做过。"),
        (0.350, "门槛费",
         "「够这个数，\n你的藏品才够格被回收」",
         "门槛是他随口定的，\n交完还有下一个门槛。"),
        (0.695, "保证金",
         "「怕你临时反悔，\n先押一笔，成交就退」",
         "押金从没有退过，\n这是整条链里最贵的一步。"),
    ]

    for x0, name, quote, fact in cards:
        ax.add_patch(FancyBboxPatch((x0, 0.360), 0.300, 0.440,
                                    boxstyle="round,pad=0.010,rounding_size=0.012",
                                    facecolor=PALE, edgecolor=LIGHT, linewidth=1.0))
        ax.add_patch(Rectangle((x0, 0.789), 0.300, 0.011, facecolor=RED,
                               edgecolor="none"))
        ax.text(x0 + 0.022, 0.742, name, fontsize=13.5, color=RED, weight="bold",
                va="center")
        ax.text(x0 + 0.022, 0.688, "他说", fontsize=8.8, color=GRAY, va="center")
        ax.text(x0 + 0.022, 0.642, quote, fontsize=9.8, color=DARK, va="top",
                linespacing=1.7)
        ax.text(x0 + 0.022, 0.520, "实际", fontsize=8.8, color=GRAY, va="center")
        ax.text(x0 + 0.022, 0.474, fact, fontsize=9.8, color=SLATE, va="top",
                linespacing=1.7)

    # 警方三条线
    ax.add_patch(Rectangle((0.005, 0.075), 0.990, 0.225, facecolor=PALE,
                           edgecolor=LIGHT, linewidth=1.0))
    ax.text(0.028, 0.245, "警方划的三条线", fontsize=11.2, color=NAVY,
            weight="bold", va="center")

    marks = [
        (0.028, "宣称藏品远超市场价回收"),
        (0.360, "承诺高额收益、稳赚不赔"),
        (0.692, "以任何名目先收你的钱"),
    ]
    for x, text in marks:
        ax.text(x, 0.165, "×", fontsize=13, color=RED, va="center")
        ax.text(x + 0.026, 0.165, text, fontsize=10.4, color=DARK, va="center")
    ax.text(0.028, 0.108, "三条里沾上任何一条，就不是生意，是陷阱。",
            fontsize=9.4, color=GRAY, va="center")

    footer(fig, "名目据 2026 年 11 月 13 日警方披露的案情；三条线为警方提示原意转述。")
    fig.savefig(OUT + "图2_收费清单.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.135, 0.910, 0.690])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "今晚十分钟，看三个地方", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.882, "不用懂技术，会翻手机就行——趁爸妈还愿意让你翻",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    rows = [
        ("关注列表", "短视频 App 里，有没有带「鉴宝」「收藏」「回收」「古玩」字样的账号"),
        ("群聊和好友", "有没有「XX 馆长」「XX 老师」，有没有群名带「内部」「VIP」「藏友」的私域群"),
        ("转账记录", "近三个月有没有转给个人账户的「鉴定费」「保证金」「门槛费」"),
    ]

    for i, (title, detail) in enumerate(rows):
        y = 0.720 - i * 0.195
        ax.add_patch(Rectangle((0.005, y - 0.082), 0.990, 0.164,
                               facecolor=PALE, edgecolor=LIGHT, linewidth=1.0))
        ax.scatter([0.048], [y], s=1100, facecolor=NAVY, edgecolor="none",
                   zorder=3)
        ax.text(0.048, y, str(i + 1), fontsize=11, color="white",
                ha="center", va="center", zorder=4)
        ax.text(0.092, y + 0.042, title, fontsize=12.6, color=NAVY,
                weight="bold", va="center")
        ax.text(0.092, y - 0.032, detail, fontsize=9.8, color=DARK, va="center")

    ax.add_patch(Rectangle((0.010, 0.030), 0.980, 0.148,
                           facecolor="white", edgecolor=RED, linewidth=1.4))
    ax.text(0.030, 0.132, "教爸妈一句，比讲一小时道理管用：",
            fontsize=9.6, color=GRAY, va="center")
    ax.text(0.030, 0.072, "「真正收东西的人，不会先让我掏钱。」",
            fontsize=14, color=RED, weight="bold", va="center")

    footer(fig, "自查项据警方提示与本案作案手法整理；若已转账，保存聊天与转账记录后立即报警。")
    fig.savefig(OUT + "图3_看三个地方.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")
