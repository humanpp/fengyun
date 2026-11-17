# -*- coding: utf-8 -*-
"""
《召回是真的，短信是假的：80 万辆车的公告发出后，有人点了链接，27 万没了》配套图表
事实口径：2026-11-04 市场监管总局一次发布多起召回公告、涉及大众/丰田/路特斯/Jeep
等品牌、合计超 80 万辆；随后出现伪造"召回通知"短信（姓名、车型、车牌、车架号
全对，附伪造红头文件与公章，话术"气囊隐患""2 小时内办理""逾期取消质保"）；
北京警方通报有事主被骗 27 万元；被冒充车企 20 余家相继辟谣；正规召回经官方 App、
400 客服、挂号信或授权 4S 店发出，完全免费，不索要密码与验证码，不要求转账。
风格：克制传媒风，白底、低饱和配色、标题即结论
输出目录 = 脚本所在目录
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch

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

    fig.text(0.045, 0.955, "同一个起点，两条路", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.882, "11 月 4 日之后，车主手机上出现了两种「召回通知」",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    # 起点
    ax.add_patch(FancyBboxPatch((0.012, 0.330), 0.138, 0.340,
                                boxstyle="round,pad=0.008,rounding_size=0.010",
                                facecolor=PALE, edgecolor=LIGHT, linewidth=1.0))
    ax.add_patch(Rectangle((0.012, 0.658), 0.138, 0.012, facecolor=SLATE,
                           edgecolor="none"))
    ax.text(0.024, 0.610, "11 月 4 日", fontsize=10.4, color=SLATE, va="center")
    ax.text(0.024, 0.556, "召回公告", fontsize=12.4, color=DARK, weight="bold",
            va="center")
    ax.text(0.024, 0.486, "80 万辆", fontsize=16, color=NAVY, weight="bold",
            va="center")
    ax.text(0.024, 0.428, "多品牌同时发布", fontsize=8.8, color=GRAY, va="center")
    ax.text(0.024, 0.384, "公告公开，谁都能查", fontsize=8.8, color=GRAY,
            va="center")

    lanes = [
        (0.850, "真的", NAVY, [
            ("官方渠道", "App · 400 电话\n挂号信 · 4S 店"),
            ("免费处理", "不收费，不索要\n密码和验证码"),
            ("车修好了", "公告编号可查\n到店预约即可"),
        ]),
        (0.360, "假的", RED, [
            ("伪造短信", "姓名、车型、车牌\n甚至车架号全对"),
            ("钓鱼链接", "「气囊隐患 ·\n2 小时内办理」"),
            ("27 万没了", "北京警方通报\n有事主点了链接"),
        ]),
    ]

    bw, bh = 0.225, 0.210
    for top, lane_name, color, boxes in lanes:
        bot = top - bh
        ax.text(0.175, top + 0.040, lane_name, fontsize=11, color=color,
                weight="bold", va="center")
        for i, (head, body) in enumerate(boxes):
            x0 = 0.175 + i * 0.2875
            ax.add_patch(Rectangle((x0, bot), bw, bh, facecolor=PALE,
                                   edgecolor=LIGHT, linewidth=1.0))
            ax.add_patch(Rectangle((x0, top - 0.011), bw, 0.011, facecolor=color,
                                   edgecolor="none"))
            ax.text(x0 + 0.016, top - 0.048, head, fontsize=11.2, color=color,
                    weight="bold", va="center")
            ax.text(x0 + 0.016, top - 0.088, body, fontsize=8.8, color=DARK,
                    va="top", linespacing=1.65)
            if i < 2:
                ax.annotate("", xy=(x0 + bw + 0.048, top - 0.105),
                            xytext=(x0 + bw + 0.008, top - 0.105),
                            arrowprops=dict(arrowstyle="-|>", color=GRAY,
                                            linewidth=1.2, shrinkA=0, shrinkB=0))

    # 起点 → 两条道
    ax.annotate("", xy=(0.172, 0.720), xytext=(0.152, 0.545),
                arrowprops=dict(arrowstyle="-|>", color=NAVY, linewidth=1.4,
                                shrinkA=0, shrinkB=0,
                                connectionstyle="arc3,rad=-0.15"))
    ax.annotate("", xy=(0.172, 0.250), xytext=(0.152, 0.455),
                arrowprops=dict(arrowstyle="-|>", color=RED, linewidth=1.4,
                                shrinkA=0, shrinkB=0,
                                connectionstyle="arc3,rad=0.15"))

    punchline(fig, "公告是真的，所以「说得对」的部分全是真的——除了那个链接。")
    footer(fig, "据 2026 年 11 月 4 日市场监管总局召回公告及警方通报整理；被冒名车企达 20 余家。")
    fig.savefig(OUT + "图1_两条路.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.135, 0.910, 0.690])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "四行就能分开", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.882, "同一条召回，两种通知：看谁发的、写了什么、让你做什么、要不要钱",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    ax.text(0.030, 0.800, "看什么", fontsize=10.2, color=GRAY, weight="bold",
            va="center")
    ax.text(0.300, 0.800, "真召回", fontsize=11.4, color=NAVY, weight="bold",
            va="center")
    ax.text(0.690, 0.800, "假短信", fontsize=11.4, color=RED, weight="bold",
            va="center")
    ax.plot([0.012, 0.988], [0.772, 0.772], color=LIGHT, linewidth=1.4)

    rows = [
        ("谁发的", "车企官方 App、400 客服、\n挂号信、授权 4S 店",
         "陌生号码，或仿冒的「客服」\n（20 余家车企已辟谣）"),
        ("写了什么", "车型、召回原因、\n预约方式",
         "姓名、车牌、车架号，\n外加伪造的「红头文件」"),
        ("让你做什么", "到店预约，\n免费检修",
         "「2 小时内点链接办理」\n「逾期取消质保」"),
        ("要不要钱", "一分不要。\n不索要密码和验证码",
         "要你转账——\n任何名义的转账"),
    ]

    for i, (label, real, fake) in enumerate(rows):
        y = 0.640 - i * 0.163
        if i % 2 == 0:
            ax.add_patch(Rectangle((0.012, y - 0.072), 0.976, 0.144,
                                   facecolor=PALE, edgecolor="none"))
        ax.text(0.030, y, label, fontsize=10.4, color=GRAY, va="center")
        ax.text(0.300, y, real, fontsize=9.8, color=DARK, va="center",
                linespacing=1.65)
        ax.text(0.690, y, fake, fontsize=9.8, color=DARK, va="center",
                linespacing=1.65)

    for x in (0.278, 0.668):
        ax.plot([x, x], [0.180, 0.766], color=LIGHT, linewidth=1.0)

    punchline(fig, "改一个字都不行：召回是要给你修车，不是要你掏钱。")
    footer(fig, "据 2026 年 11 月 4 日召回公告、警方通报及车企辟谣信息整理。")
    fig.savefig(OUT + "图2_四行.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(12, 6.8))
    ax = fig.add_axes([0.045, 0.135, 0.910, 0.690])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    fig.text(0.045, 0.955, "三十秒，三条路", fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, 0.882, "收到召回短信，先别点——任选一条，问一句就清楚",
             fontsize=10.8, color=GRAY, ha="left", va="top")

    ax.add_patch(Rectangle((0.012, 0.755), 0.976, 0.085, facecolor=RED,
                           edgecolor="none"))
    ax.text(0.030, 0.797, "第一步：不点那条链接", fontsize=14, color="white",
            weight="bold", va="center")
    ax.text(0.735, 0.797, "下面的三件事，30 秒内能做到", fontsize=10, color="white",
            va="center")

    cards = [
        ("01", "打开 App", "你买车那家车企的官方 App，\n找「召回」或「服务」入口，\n输车架号查一下。"),
        ("02", "打个电话", "车企 400 客服，或者你常去的\n授权 4S 店，报车牌问一句\n「我这车在召回名单里吗」。"),
        ("03", "打 96110", "已经点了链接、已经转了账，\n或者就是拿不准——\n打这个号码。"),
    ]

    for i, (no, title, body) in enumerate(cards):
        x0 = 0.012 + i * 0.337
        ax.add_patch(FancyBboxPatch((x0, 0.240), 0.310, 0.470,
                                    boxstyle="round,pad=0.010,rounding_size=0.012",
                                    facecolor=PALE, edgecolor=LIGHT, linewidth=1.0))
        ax.text(x0 + 0.026, 0.650, no, fontsize=15, color=GRAY, weight="bold",
                va="center")
        ax.text(x0 + 0.026, 0.570, title, fontsize=14.5, color=NAVY,
                weight="bold", va="center")
        ax.text(x0 + 0.026, 0.500, body, fontsize=9.6, color=DARK, va="top",
                linespacing=1.8)

    ax.text(0.012, 0.150, "真的召回不会因为晚点一个链接就取消质保。",
            fontsize=11, color=DARK, va="center")
    ax.text(0.012, 0.080, "30 秒，比 27 万便宜。", fontsize=15, color=RED,
            weight="bold", va="center")

    footer(fig, "正规召回渠道：车企官方 App、400 客服、挂号信、授权 4S 店；服务完全免费。96110 为全国反诈专线。")
    fig.savefig(OUT + "图3_三十秒.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")
