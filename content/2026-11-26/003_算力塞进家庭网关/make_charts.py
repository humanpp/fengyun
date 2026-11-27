# -*- coding: utf-8 -*-
"""
《把算力塞进家里的网关：家庭宽带开始按 Token 卖》配套图表

事实口径：
  · 2026 中国移动网络大会（11 月 5-7 日，广州）期间，11 月 6 日中国移动与华为
    联办"数智生活 AI+创新合作论坛"，论坛主题"通信焕新，智启新局"。
    据新华网浙江频道 2026-11-10（来源：中国移动杭州研发中心）与中华网 2026-11-06：
    发布家宽边缘算力网关（BCG）创新方案——以 iBNG 智能网关为底座、
    MPC 算力单板为引擎，把算力下沉到家庭边缘；开启 Token 化经营，
    支持无感鉴权、融合计费和模型路由调度；实现算力、网络与智能体服务
    一体化调度；家庭宽带从"卖流量"的连接通道升级为"家庭算智底座"。
  · 同场发布另含 UE Logo2.0、5G-A 高铁尊享服务体验包、动态切片专属加速、
    大上行赋能 Mobile AI、灵犀屏、新通话 DC 生态共建倡议（据行业媒体报道）。
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch

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
TEAL = "#3f6f6b"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep

Y_TITLE = 0.958
Y_SUB = 0.898
Y_PUNCH = 0.070
Y_FOOT = 0.020


def header(fig, title, sub):
    fig.text(0.045, Y_TITLE, title, fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, Y_SUB, sub, fontsize=10.6, color=GRAY,
             ha="left", va="top")


def footer(fig, text):
    fig.text(0.045, Y_FOOT, text, fontsize=7.6, color=GRAY,
             ha="left", va="bottom")


def punchline(fig, text):
    fig.text(0.045, Y_PUNCH, text, fontsize=10.4, color=DARK,
             ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


def card(ax, x, y, w, h, edge, face="white", lw=1.0, z=2):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.004,rounding_size=0.014",
        facecolor=face, edgecolor=edge, linewidth=lw, zorder=z))


def new_axes(fig):
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return ax


# ---------------------------------------------------------------- 图 1
def fig1():
    """两块拼图"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "一个盒子里，两块拼图",
           "iBNG 是底座，MPC 是引擎")

    # 底部：iBNG 底座
    card(ax, 0.048, 0.300, 0.904, 0.150, NAVY, lw=1.6)
    ax.text(0.072, 0.404, "iBNG 智能网关", fontsize=13.0, color=NAVY,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.072, 0.360, "底座", fontsize=9.4, color=DARK,
            ha="left", va="center", zorder=6)
    ax.text(0.072, 0.326, "连接、拨号、路由、家庭网络管理", fontsize=8.8,
            color=SLATE, ha="left", va="center", zorder=6)
    ax.text(0.560, 0.344, "原有能力的延续与升级", fontsize=8.8,
            color=NAVY, ha="left", va="center", zorder=6)

    # 上方：MPC 引擎
    card(ax, 0.300, 0.520, 0.400, 0.150, RED, lw=1.6)
    ax.text(0.500, 0.624, "MPC 算力单板", fontsize=13.0, color=RED,
            weight="bold", ha="center", va="center", zorder=6)
    ax.text(0.500, 0.580, "引擎", fontsize=9.4, color=DARK,
            ha="center", va="center", zorder=6)
    ax.text(0.500, 0.546, "插进去的计算板卡，负责真正跑推理", fontsize=8.8,
            color=SLATE, ha="center", va="center", zorder=6)

    ax.add_patch(FancyArrowPatch((0.500, 0.518), (0.500, 0.454),
                                 arrowstyle="-|>", mutation_scale=17,
                                 color=GRAY, linewidth=1.5, zorder=5))

    ax.text(0.048, 0.252, "两条路，选了后者", fontsize=10.0, color=GRAY,
            ha="left", va="center")
    ax.plot([0.048, 0.952], [0.234, 0.234], color=LIGHT, linewidth=1.0)

    rows = [
        ("单独做一台家庭算力服务器", "用户要额外买设备、找位置、接电源", GRAY),
        ("把算力塞进已有的网关", "门槛从「添置」降到「升级」", RED),
    ]
    y = 0.202
    for k, v, color in rows:
        ax.text(0.048, y, k, fontsize=9.4, color=DARK,
                ha="left", va="center")
        ax.text(0.470, y, v, fontsize=9.0, color=color,
                ha="left", va="center")
        y -= 0.050

    punchline(fig, "愿意为 AI 再买一台盒子的用户是少数，愿意升级一下套餐的是多数。")
    footer(fig, "事实来源：新华网浙江频道 2026-11-10（来源：中国移动杭州研发中心）；"
                "中华网 2026-11-06 转财讯网")
    fig.savefig(OUT + "图1_两块拼图.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """三个卡点"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "Token 化经营要过三道关",
           "无感鉴权、融合计费、模型路由调度，各解决一个卡点")

    items = [
        ("无感鉴权", "谁在用", "家庭里连着手机、电视、音箱、摄像头\n每台都单独登录体验会很糟\n\n认证在网关这层完成\n设备不用感知", NAVY, 0.048),
        ("融合计费", "怎么收钱", "过去账单只有一笔月租\n叠加算力就有了第二笔\n\n流量与 Token 两种计量单位\n要并到一张账单上", TEAL, 0.368),
        ("模型路由调度", "用哪个", "简单任务本地算，省带宽省时延\n复杂任务上云\n\n网关要知道每个模型的特性\n也要知道当前网络与算力状态", RED, 0.688),
    ]
    for name, tag, desc, color, x in items:
        card(ax, x, 0.330, 0.258, 0.390, color, lw=1.4)
        ax.text(x + 0.018, 0.680, name, fontsize=10.6, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(x + 0.018, 0.638, "解决：" + tag, fontsize=8.8, color=DARK,
                ha="left", va="center", zorder=6)
        ax.plot([x + 0.018, x + 0.240], [0.614, 0.614], color=LIGHT,
                linewidth=1.0, zorder=6)
        ax.text(x + 0.018, 0.540, desc, fontsize=7.8, color=SLATE,
                ha="left", va="center", zorder=6, linespacing=1.7)

    ax.text(0.048, 0.278, "三个词连起来，是一条完整的商业闭环：",
            fontsize=9.6, color=DARK, ha="left", va="center")
    ax.text(0.048, 0.244, "认得出人　·　算得清账　·　分得对活",
            fontsize=11.0, color=RED, weight="bold", ha="left", va="center")

    card(ax, 0.048, 0.140, 0.904, 0.070, LIGHT, face=PALE, lw=1.0)
    ax.text(0.070, 0.175,
            "官方表述是「实现算力、网络与智能体服务一体化调度」——三层都在这一个盒子里被统一调度。",
            fontsize=9.0, color=DARK, ha="left", va="center", zorder=6)

    punchline(fig, "家庭算力卖不卖得动，取决于这三关过得顺不顺。")
    footer(fig, "事实来源：新华网浙江频道 2026-11-10；中华网 2026-11-06"
                "（Token 化经营、无感鉴权、融合计费、模型路由调度）")
    fig.savefig(OUT + "图2_三个卡点.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """什么该在本地算"""
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "什么该在本地算，什么仍然要上云",
           "方案叫「算力下沉」，是下沉不是替代")

    rows = [
        ("调用频次高", "本地算，不用反复占带宽", True),
        ("单次计算量不大", "一块单板扛得住", True),
        ("对时延敏感", "本地往返比上云快", True),
        ("对隐私敏感", "数据不出户", True),
        ("大模型复杂推理", "网关做不了，仍应上云", False),
        ("海量上下文", "仍应上云", False),
        ("长时间连续计算", "仍应上云", False),
    ]

    y = 0.660
    ax.text(0.048, 0.730, "负载特征", fontsize=9.6, color=GRAY,
            ha="left", va="center")
    ax.text(0.400, 0.730, "放在哪", fontsize=9.6, color=GRAY,
            ha="left", va="center")
    ax.text(0.870, 0.730, "判断", fontsize=9.6, color=GRAY,
            ha="left", va="center")
    ax.plot([0.048, 0.952], [0.712, 0.712], color=LIGHT, linewidth=1.0)

    for name, where, local in rows:
        color = TEAL if local else SLATE
        ax.text(0.048, y, name, fontsize=9.2, color=DARK,
                ha="left", va="center")
        ax.text(0.400, y, where, fontsize=8.6, color=SLATE,
                ha="left", va="center")
        ax.text(0.870, y, "本地" if local else "上云", fontsize=8.8,
                color=color, weight="bold", ha="left", va="center")
        y -= 0.058

    ax.text(0.048, 0.220, "同场发布的还有这些，方向一致：", fontsize=9.4,
            color=DARK, ha="left", va="center")

    tags = ["UE Logo2.0", "5G-A 高铁包", "动态切片加速", "大上行",
            "灵犀屏", "新通话 DC"]
    x = 0.048
    for t in tags:
        w = 0.140
        card(ax, x, 0.150, w, 0.042, GRAY, face=PALE, lw=0.9)
        ax.text(x + w / 2, 0.171, t, fontsize=7.8, color=DARK,
                ha="center", va="center", zorder=6)
        x += w + 0.014

    punchline(fig, "多数不是在堆更大的算力，而是在做更匹配 AI 流量的网络能力。")
    footer(fig, "事实来源：新华网浙江频道 2026-11-10；同场成果据行业媒体报道")
    fig.savefig(OUT + "图3_什么该在本地算.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)
