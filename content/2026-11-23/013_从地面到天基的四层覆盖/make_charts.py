# -*- coding: utf-8 -*-
"""
《从地面到天基：一张通信网要盖住四层空间》配套图表 —— 视觉增强版

设计规范（统一视觉语言）
  · 顶部：左侧色块 + 大标题 + 副标题，标题下一条同色细线
  · 数字：粗体 + 色块底；标签小字灰
  · 卡片：微阴影 + 左侧竖色条（不用整圈描边）
  · 结论条：深色底白字，横贯右下
  · 页脚：极细灰线 + 来源小字
输出目录 = 脚本所在目录
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, Polygon

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["figure.facecolor"] = "white"
plt.rcParams["savefig.facecolor"] = "white"

# 主色板
INK = "#1a2332"        # 主文字，近黑带蓝
NAVY = "#1b3a5c"
RED = "#b0413e"
TEAL = "#2f6b64"
GOLD = "#9a7b3f"
MUTED = "#7b8494"
HAIR = "#dfe3e8"
WASH = "#f4f6f8"
WASH2 = "#ebeff3"
WHITE = "#ffffff"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep
Q_L, Q_R = "\u300c", "\u300d"


def new_axes(fig):
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return ax


def head(fig, ax, kicker, title, sub, color):
    """顶部标题区：左侧色块 + 标题 + 副标题 + 分隔线"""
    # 左上角色块
    ax.add_patch(Rectangle((0.042, 0.928), 0.0075, 0.040,
                           facecolor=color, edgecolor="none", zorder=9))
    ax.text(0.058, 0.950, kicker, fontsize=9.2, color=color,
            weight="bold", ha="left", va="center", zorder=9)
    ax.text(0.042, 0.900, title, fontsize=21, color=INK, weight="bold",
            ha="left", va="top", zorder=9)
    ax.text(0.042, 0.848, sub, fontsize=10.4, color=MUTED,
            ha="left", va="top", zorder=9)
    ax.plot([0.042, 0.958], [0.812, 0.812], color=HAIR, linewidth=1.0,
            zorder=5)


def foot(fig, ax, text):
    ax.plot([0.042, 0.958], [0.058, 0.058], color=HAIR, linewidth=0.9,
            zorder=5)
    ax.text(0.042, 0.028, text, fontsize=7.0, color=MUTED,
            ha="left", va="center", zorder=9)


def outro(fig, ax, text, color=INK):
    """底部结论条：深色底白字"""
    ax.add_patch(FancyBboxPatch(
        (0.042, 0.082), 0.700, 0.048,
        boxstyle="round,pad=0.002,rounding_size=0.008",
        facecolor=color, edgecolor="none", zorder=6))
    ax.text(0.062, 0.106, text, fontsize=10.2, color=WHITE,
            ha="left", va="center", zorder=9)


def panel(ax, x, y, w, h, accent, face=WHITE, bar=0.0055, shadow=True):
    """卡片：微阴影 + 左侧竖色条"""
    if shadow:
        ax.add_patch(FancyBboxPatch(
            (x + 0.0035, y - 0.0035), w, h,
            boxstyle="round,pad=0,rounding_size=0.009",
            facecolor="#e9ecf0", edgecolor="none", zorder=2))
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0,rounding_size=0.009",
        facecolor=face, edgecolor="#e6eaee", linewidth=0.9, zorder=3))
    ax.add_patch(FancyBboxPatch(
        (x, y), bar, h,
        boxstyle="round,pad=0,rounding_size=0.0028",
        facecolor=accent, edgecolor="none", zorder=4))


def big_num(ax, x, y, num, label, color, size=26, unit=""):
    """大数字 + 底部标签"""
    ax.text(x, y, num, fontsize=size, color=color, weight="bold",
            ha="left", va="center", zorder=8)
    ax.text(x, y - size * 0.0023 - 0.020, label, fontsize=8.6,
            color=MUTED, ha="left", va="center", zorder=8)
    if unit:
        ax.text(x, y - size * 0.0023 - 0.042, unit, fontsize=7.6,
                color=MUTED, ha="left", va="center", zorder=8)


# ---------------------------------------------------------------- 图 1
def fig1():
    fig = plt.figure(figsize=(13.6, 8.0))
    ax = new_axes(fig)

    head(fig, ax, "覆盖的物理边界",
         "一张网要盖住四层空间",
         "地面、近海、低空、天基，四层的物理约束完全不同，解法也不同",
         GOLD)

    layers = [
        ("天空", "天基层", "卫星 · 全域兜底", GOLD, 0.632, [
            (Q_L + "天通+北斗" + Q_R + "双星协同，天通卫星通话已上线", ""),
            ("01 星（5G-A NTN 再生）、02 星（手机直连 NTN）在轨验证", ""),
            ("全球首颗 6G 架构验证星" + Q_L + "星核" + Q_R + "完成在轨验证", ""),
        ]),
        ("低空", "低空层", "300—1000 米 · 无人机", NAVY, 0.486, [
            ("5G-A 通感一体：一个基站既通信又感知", ""),
            ("杭州、绍兴等地已布局低空智联基础设施", ""),
            ("支撑低空物流、急救转运、工业巡检、农林植保", ""),
        ]),
        ("近海", "近海层", "0—60 公里海域", TEAL, 0.340, [
            ("江苏" + Q_L + "陆地+岛屿+风电平台" + Q_R + "组网，近海 40 公里", ""),
            ("辽宁无人海岛低碳 5G 基站，环渤海 60 公里全域覆盖", ""),
            ("福建 700M / 2.6G / 4.9G 多频协同超远覆盖", ""),
        ]),
        ("地面", "地面层", "乡镇以上连续覆盖", RED, 0.194, [
            ("5G 基站超 277 万站", "关键数字"),
            ("5G-A 三载波聚合、RedCap、网络智能化规模部署", ""),
            ("重点区域下行近 800Mbps、上行超 120Mbps", ""),
        ]),
    ]

    for tag, name, span, color, y, items in layers:
        panel(ax, 0.042, y, 0.916, 0.128, color)

        # 左侧：层级标签
        ax.text(0.062, y + 0.094, tag, fontsize=9.0, color=color,
                weight="bold", ha="left", va="center", zorder=9)
        ax.text(0.062, y + 0.056, name, fontsize=13.0, color=INK,
                weight="bold", ha="left", va="center", zorder=9)
        ax.text(0.062, y + 0.024, span, fontsize=8.2, color=MUTED,
                ha="left", va="center", zorder=9)

        # 细分隔
        ax.plot([0.252, 0.252], [y + 0.016, y + 0.112], color="#e6eaee",
                linewidth=1.0, zorder=5)

        yy = y + 0.098
        for txt, mark in items:
            is_key = (mark == "关键数字")
            ax.add_patch(Circle((0.272, yy), 0.0045, facecolor=color,
                                edgecolor="none", zorder=8))
            ax.text(0.288, yy, txt, fontsize=8.8,
                    color=INK if not is_key else color,
                    weight="bold" if is_key else "normal",
                    ha="left", va="center", zorder=9)
            yy -= 0.040

    # 右侧纵深箭头
    ax.annotate("", xy=(0.026, 0.186), xytext=(0.026, 0.766),
                arrowprops=dict(arrowstyle="-|>", color=HAIR,
                                linewidth=2.2, shrinkA=0, shrinkB=0))

    outro(fig, ax, "补上垂直方向的覆盖，比在平面上再堆基站难得多。")
    foot(fig, ax, "事实来源：通信世界网 2026-06-11《中国移动这张" + Q_L + "立体网" + Q_R +
         "，真的有点东西》；2025 年移动网络质量评测结果")

    fig.savefig(OUT + "图1_四层空间.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(13.6, 8.0))
    ax = new_axes(fig)

    head(fig, ax, "星地融合的三条线",
         "星地融合不是把基站搬上天，是三条线同时铺",
         "存量卫星资源、自研技术体系、国际标准——缺一条都成不了一张网",
         RED)

    cols = [
        ("存量资源", "借现成的", NAVY, "01", [
            ("亚太 6D", "高轨宽带容量"),
            ("北斗", "短报文定位"),
            ("天通", "卫星通话"),
            ("天启 / 星网", "低轨星座"),
        ], "盘活高轨存量，再联合低轨补容量"),
        ("技术体系", "自己做标准", RED, "02", [
            ("STCN", "星地深度协同组网"),
            ("3GPP NTN", "国际标准推进"),
            ("" + Q_L + "星核" + Q_R + "", "6G 架构验证星"),
            ("01 星 / 02 星", "在轨技术验证"),
        ], "先上天验证，再回标准里确认"),
        ("终端侧", "让手机能用", TEAL, "03", [
            ("天通卫星通话", "已上线"),
            ("北斗卫星短信", "同时可用"),
            ("文字 + 语音", "双重保障"),
            ("不改手机形态", "靠芯片与协议打通"),
        ], "手机不必换外形也能发消息"),
    ]

    w = 0.288
    gap = 0.019
    x = 0.042
    for name, tag, color, num, items, note in cols:
        panel(ax, x, 0.210, w, 0.560, color)

        ax.text(x + 0.024, 0.716, num, fontsize=11.0, color=color,
                weight="bold", ha="left", va="center", zorder=9)
        ax.text(x + 0.024, 0.678, name, fontsize=14.0, color=INK,
                weight="bold", ha="left", va="center", zorder=9)
        ax.text(x + 0.024, 0.642, tag, fontsize=8.6, color=MUTED,
                ha="left", va="center", zorder=9)
        ax.plot([x + 0.024, x + w - 0.024], [0.620, 0.620], color=HAIR,
                linewidth=1.0, zorder=5)

        yy = 0.580
        for k, v in items:
            ax.text(x + 0.024, yy, k, fontsize=9.2, color=INK,
                    weight="bold", ha="left", va="center", zorder=9)
            ax.text(x + 0.024, yy - 0.030, v, fontsize=8.0, color=MUTED,
                    ha="left", va="center", zorder=9)
            yy -= 0.072

        # 卡片内结论
        ax.add_patch(FancyBboxPatch(
            (x + 0.024, 0.232), w - 0.048, 0.050,
            boxstyle="round,pad=0,rounding_size=0.006",
            facecolor=WASH, edgecolor="none", zorder=6))
        ax.text(x + 0.038, 0.257, note, fontsize=8.0, color=color,
                weight="bold", ha="left", va="center", zorder=9)

        x += w + gap

    outro(fig, ax, "卫星互联网的竞争，最后落在标准、芯片和终端协议上。")
    foot(fig, ax, "事实来源：通信世界网 2026-06-11；2026 移动网络大会星地融合表述"
         "（新华网 2026-11-07）")

    fig.savefig(OUT + "图2_三条技术线.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(13.6, 8.0))
    ax = new_axes(fig)

    head(fig, ax, "覆盖的经济学",
         "覆盖边界每往外推一格，成本结构和用户数都在变",
         "同一个" + Q_L + "覆盖" + Q_R + "，在五种场景里是五门不同的生意",
         NAVY)

    rows = [
        ("城市", "人口密集", "高", "基站密度决定容量，成本可分摊", RED, 5),
        ("乡镇", "连片覆盖", "中", "277 万站打底，规模换低成本", NAVY, 4),
        ("近海", "线性延伸", "中高", "岸基 + 海基 + 船载，单站覆盖几十公里", TEAL, 3),
        ("低空", "立体空域", "高", "要感知能力，成本高于普通覆盖", GOLD, 2),
        ("天基", "全域兜底", "极高", "卫星造价与发射成本，靠稀缺场景回收", MUTED, 1),
    ]

    ax.text(0.042, 0.762, "单位覆盖成本（圆点数即成本档位，5 档越高）", fontsize=8.6,
            color=MUTED, ha="left", va="center")
    ax.plot([0.042, 0.958], [0.742, 0.742], color=HAIR, linewidth=1.0)

    y = 0.688
    for name, tag, cost, note, color, level in rows:
        # 左侧场景名
        ax.text(0.042, y, name, fontsize=12.4, color=INK, weight="bold",
                ha="left", va="center", zorder=9)
        ax.text(0.042, y - 0.032, tag, fontsize=7.8, color=MUTED,
                ha="left", va="center", zorder=9)

        # 成本刻度（五个点，点亮 level 个）
        for i in range(5):
            cx = 0.190 + i * 0.026
            filled = i < level
            ax.add_patch(Circle((cx, y), 0.0072,
                                facecolor=color if filled else WHITE,
                                edgecolor=color if filled else "#d6dbe1",
                                linewidth=1.2, zorder=8))

        ax.text(0.352, y, cost, fontsize=10.6, color=color, weight="bold",
                ha="left", va="center", zorder=9)

        # 分隔线
        ax.plot([0.430, 0.430], [y - 0.024, y + 0.024], color="#e6eaee",
                linewidth=1.0, zorder=5)
        ax.text(0.452, y, note, fontsize=8.8, color=INK,
                ha="left", va="center", zorder=9)

        y -= 0.096

    # 底部说明面板
    ax.add_patch(FancyBboxPatch(
        (0.042, 0.140), 0.916, 0.086,
        boxstyle="round,pad=0,rounding_size=0.009",
        facecolor=WASH, edgecolor="none", zorder=3))
    ax.add_patch(FancyBboxPatch(
        (0.042, 0.140), 0.0055, 0.086,
        boxstyle="round,pad=0,rounding_size=0.0028",
        facecolor=NAVY, edgecolor="none", zorder=4))
    ax.text(0.064, 0.196, "这张表的用处：判断一件事该用什么手段覆盖",
            fontsize=9.8, color=INK, weight="bold", ha="left",
            va="center", zorder=9)
    ax.text(0.064, 0.164,
            "人口密集区堆基站最划算；远洋和荒漠堆基站永远收不回成本，只能靠卫星。",
            fontsize=8.4, color=MUTED, ha="left", va="center", zorder=9)

    outro(fig, ax, "全覆盖不是技术问题，是多少场景愿意为" + Q_L + "永远在线" + Q_R + "付钱。")
    foot(fig, ax, "事实来源：通信世界网 2026-06-11；成本分级为作者据公开材料所作的定性归纳")

    fig.savefig(OUT + "图3_覆盖经济账.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)
