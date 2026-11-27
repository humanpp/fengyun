# -*- coding: utf-8 -*-
"""
《160 平方公里低空覆盖、35 平方公里感知区：一张试验网在试什么》配套图表

事实口径（2026-11-18，武汉，2026 中国 5G+工业互联网大会低空经济
技术与创新应用发展平行会议）：
  · 中国移动湖北公司与中信科移动联合发布「中国移动低空试验网（武汉）」
    建设成果，推动低空终端、网络与平台从单项测试迈入端到端联合验证阶段。
  · 该试验网是中国移动全国五大低空技术试验网之一，覆盖武汉、咸宁两地。
  · 规模：累计部署 51 个 5G-A 通感基站、13 套多模态感知设备；
    形成 160 平方公里低空通信覆盖区、35 平方公里低空态势感知区。
  · 联合测试条件：为 3 大主流无人机厂商的机载终端、13 台多模感知设备、
    2 个服务平台提供联合测试。
  · 场景 1（飞行安全）：在鄂州花湖机场部署 11 个 5G-A 通感一体基站，
    通过「中移凌云」平台跟踪无人机位置和飞行轨迹，
    平均支持地面人员及时核查低空安全隐患 20 次/天。
  · 场景 2（公路养护）：在武阳高速通过无线网络和专线将高清巡检画面
    实时传回管理指挥中心，每月平均节省人工成本超 10 万元。
  · 网络底座：湖北移动率先实现全省 17 市州 5G-A 网络商用，
    5G-A 三载波聚合已在全省开通 8800 站，武汉三环内实现全面覆盖；
    在武汉、十堰、荆门等地打造 5G-A 低空经济示范区。
  · 湖北移动副总经理刘建表示，低空智联网建设要以飞行安全和行业作业需求为依据；
    网络覆盖是否连续、感知是否准确需在实际航线上验证。
  · 后续：作为湖北省通信学会低空经济专委会首届主任委员单位，
    将联合产业伙伴制定低空双网的测试与验收标准，
    面向交通、能源、物流等行业开放常态化试点航线。
  据新华网 2026-11-20《中国移动低空试验网（武汉）建成 端到端联合验证启动》。

风格：克制传媒风，编辑排版
输出目录 = 脚本所在目录
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["figure.facecolor"] = "white"
plt.rcParams["savefig.facecolor"] = "white"

INK = "#1a2332"
NAVY = "#1b3a5c"
RED = "#b0413e"
TEAL = "#2f6b64"
GOLD = "#9a7b3f"
MUTED = "#7b8494"
HAIR = "#dfe3e8"
WASH = "#f4f6f8"
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
    ax.add_patch(FancyBboxPatch(
        (0.042, 0.082), 0.740, 0.048,
        boxstyle="round,pad=0.002,rounding_size=0.008",
        facecolor=color, edgecolor="none", zorder=6))
    ax.text(0.062, 0.106, text, fontsize=10.2, color=WHITE,
            ha="left", va="center", zorder=9)


def panel(ax, x, y, w, h, accent, face=WHITE, bar=0.0055, shadow=True):
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


# ---------------------------------------------------------------- 图 1
def fig1():
    fig = plt.figure(figsize=(13.6, 8.0))
    ax = new_axes(fig)

    head(fig, ax, "一张试验网的四个数",
         "160 平方公里覆盖，35 平方公里感知",
         "覆盖和感知是两件事——前者管" + Q_L + "连得上" + Q_R +
         "，后者管" + Q_L + "看得见" + Q_R,
         RED)

    # 左侧四个核心数字
    stats = [
        ("51 个", "5G-A 通感基站", NAVY),
        ("13 套", "多模态感知设备", TEAL),
        ("160 km²", "低空通信覆盖区", NAVY),
        ("35 km²", "低空态势感知区", RED),
    ]
    ax.text(0.042, 0.762, "规模（武汉 + 咸宁两地）", fontsize=8.6, color=MUTED,
            ha="left", va="center")
    ax.plot([0.042, 0.490], [0.742, 0.742], color=HAIR, linewidth=1.0)

    y = 0.686
    for num, label, color in stats:
        ax.text(0.042, y, num, fontsize=21.0, color=color, weight="bold",
                ha="left", va="center", zorder=9)
        ax.text(0.042, y - 0.042, label, fontsize=8.6, color=MUTED,
                ha="left", va="center", zorder=9)
        y -= 0.110

    # 右侧：覆盖 vs 感知的对比
    ax.text(0.545, 0.762, "两个区域大小不一样，是正常的", fontsize=8.6,
            color=MUTED, ha="left", va="center")
    ax.plot([0.545, 0.958], [0.742, 0.742], color=HAIR, linewidth=1.0)

    panel(ax, 0.545, 0.470, 0.413, 0.230, NAVY)
    ax.text(0.567, 0.664, "通信覆盖区 160 km²", fontsize=10.0, color=NAVY,
            weight="bold", ha="left", va="center", zorder=9)
    ax.text(0.567, 0.612,
            "只要信号能覆盖到，无人机就能连上、\n能传回数据、能接受指令。",
            fontsize=8.4, color=INK, ha="left", va="top",
            linespacing=1.7, zorder=9)
    ax.text(0.567, 0.524, "技术门槛：相对低，靠基站密度堆。", fontsize=8.0,
            color=MUTED, ha="left", va="center", zorder=9)

    panel(ax, 0.545, 0.222, 0.413, 0.230, RED)
    ax.text(0.567, 0.416, "态势感知区 35 km²", fontsize=10.0, color=RED,
            weight="bold", ha="left", va="center", zorder=9)
    ax.text(0.567, 0.364,
            "要能测出无人机在哪、多高、往哪飞——\n相当于让基站兼做雷达。",
            fontsize=8.4, color=INK, ha="left", va="top",
            linespacing=1.7, zorder=9)
    ax.text(0.567, 0.276, "技术门槛：高，感知设备贵、算法难。", fontsize=8.0,
            color=MUTED, ha="left", va="center", zorder=9)

    outro(fig, ax, "感知区只有覆盖区的两成——这恰恰说明感知比覆盖难得多。")
    foot(fig, ax, "事实来源：新华网 2026-11-20《中国移动低空试验网（武汉）建成 "
         "端到端联合验证启动》")

    fig.savefig(OUT + "图1_四个数.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(13.6, 8.0))
    ax = new_axes(fig)

    head(fig, ax, "两个已落地的场景",
         "一个管安全，一个管省钱",
         "低空经济的价值不在" + Q_L + "能飞" + Q_R +
         "，在于飞起来之后能干什么",
         TEAL)

    scenes = [
        ("场景一：飞行安全", "鄂州花湖机场", NAVY, [
            ("部署", "11 个 5G-A 通感一体基站"),
            ("平台", Q_L + "中移凌云" + Q_R + "跟踪无人机位置与飞行轨迹"),
            ("效果", "平均支持地面人员核查低空安全隐患 20 次/天"),
        ]),
        ("场景二：公路养护", "武阳高速", RED, [
            ("部署", "无线网络 + 专线，高清巡检画面实时回传"),
            ("方式", "养护人员在指挥中心定位路面隐患"),
            ("效果", "每月平均节省人工成本超 10 万元"),
        ]),
    ]

    x = 0.042
    for name, place, color, items in scenes:
        panel(ax, x, 0.320, 0.438, 0.400, color)

        ax.text(x + 0.026, 0.678, name, fontsize=12.4, color=color,
                weight="bold", ha="left", va="center", zorder=9)
        ax.text(x + 0.026, 0.642, place, fontsize=8.8, color=MUTED,
                ha="left", va="center", zorder=9)
        ax.plot([x + 0.026, x + 0.412], [0.622, 0.622], color=HAIR,
                linewidth=1.0, zorder=5)

        y = 0.580
        for k, v in items:
            ax.text(x + 0.026, y, k, fontsize=7.6, color=MUTED,
                    ha="left", va="center", zorder=9)
            ax.text(x + 0.026, y - 0.030, v, fontsize=8.4, color=INK,
                    weight="bold", ha="left", va="center", zorder=9)
            y -= 0.084

        x += 0.478

    # 底部：联合验证的含义
    ax.text(0.042, 0.286, "试验网真正在验证的东西", fontsize=8.6,
            color=MUTED, ha="left", va="center")
    ax.plot([0.042, 0.958], [0.266, 0.266], color=HAIR, linewidth=1.0)

    ax.text(0.042, 0.228,
            "同一航段内，不同厂商的机载终端 + 网络设备 + 管控平台一起跑通。",
            fontsize=9.2, color=INK, ha="left", va="center", zorder=9)
    ax.text(0.042, 0.186,
            "开放对象：3 大无人机厂商机载终端、13 台多模感知设备、2 个服务平台。",
            fontsize=8.4, color=MUTED, ha="left", va="center", zorder=9)

    outro(fig, ax, "单项测试过关不等于能一起用——端到端联调才是真正的门槛。")
    foot(fig, ax, "事实来源：新华网 2026-11-20；2026 中国 5G+工业互联网大会"
         "低空经济技术与创新应用发展平行会议（2026-11-18，武汉）")

    fig.savefig(OUT + "图2_两个场景.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(13.6, 8.0))
    ax = new_axes(fig)

    head(fig, ax, "网络底座",
         "试验网能建，是因为 5G-A 已经铺到那儿了",
         "全省 17 市州商用、8800 站三载波聚合，才有低空试验的余量",
         GOLD)

    # 三层结构：底座 → 试验区 → 行业场景
    base_y = 0.230

    # 第一层：全省 5G-A 底座
    panel(ax, 0.042, base_y, 0.916, 0.150, GOLD)
    ax.text(0.064, base_y + 0.112, "第一层：全省 5G-A 网络底座", fontsize=9.4,
            color=GOLD, weight="bold", ha="left", va="center", zorder=9)
    bstats = [
        ("17 市州", "率先实现 5G-A 网络商用"),
        ("8800 站", "5G-A 三载波聚合已开通"),
        ("三环内全覆盖", "武汉城区"),
    ]
    x = 0.064
    for num, label in bstats:
        ax.text(x, base_y + 0.058, num, fontsize=13.0, color=INK,
                weight="bold", ha="left", va="center", zorder=9)
        ax.text(x, base_y + 0.024, label, fontsize=7.6, color=MUTED,
                ha="left", va="center", zorder=9)
        x += 0.300

    # 第二层：低空试验区
    panel(ax, 0.042, 0.410, 0.446, 0.150, RED)
    ax.text(0.064, 0.522, "第二层：低空技术试验网", fontsize=9.4, color=RED,
            weight="bold", ha="left", va="center", zorder=9)
    ax.text(0.064, 0.478, "武汉 · 咸宁", fontsize=11.0, color=INK,
            weight="bold", ha="left", va="center", zorder=9)
    ax.text(0.064, 0.442, "全国五大低空技术试验网之一", fontsize=7.8,
            color=MUTED, ha="left", va="center", zorder=9)

    # 第三层：示范区
    panel(ax, 0.512, 0.410, 0.446, 0.150, NAVY)
    ax.text(0.534, 0.522, "第三层：低空经济示范区", fontsize=9.4, color=NAVY,
            weight="bold", ha="left", va="center", zorder=9)
    ax.text(0.534, 0.478, "武汉 · 十堰 · 荆门", fontsize=11.0, color=INK,
            weight="bold", ha="left", va="center", zorder=9)
    ax.text(0.534, 0.442, "联合产业链企业开展通感、探测技术验证", fontsize=7.8,
            color=MUTED, ha="left", va="center", zorder=9)

    # 顶部：行业应用
    panel(ax, 0.042, 0.588, 0.916, 0.190, TEAL, face=WASH)
    ax.text(0.064, 0.740, "第四层：可复制到行业", fontsize=9.4, color=TEAL,
            weight="bold", ha="left", va="center", zorder=9)
    ax.text(0.064, 0.696,
            "低空物流 · 行业巡检 · 低空安防 · 公路养护 · 应急救援",
            fontsize=9.2, color=INK, ha="left", va="center", zorder=9)
    ax.text(0.064, 0.648,
            "下一步：制定低空双网的测试与验收标准，面向交通、能源、物流\n"
            "开放常态化试点航线。",
            fontsize=8.2, color=MUTED, ha="left", va="top",
            linespacing=1.65, zorder=9)

    # 箭头
    for ay in [(0.386, 0.410), (0.564, 0.588)]:
        ax.annotate("", xy=(0.500, ay[1] - 0.002), xytext=(0.500, ay[0] + 0.002),
                    arrowprops=dict(arrowstyle="-|>", color="#c9d0d8",
                                    linewidth=1.6, shrinkA=0, shrinkB=0))

    outro(fig, ax, "低空不是新修一张网，是把已有的网往天上延伸一格。")
    foot(fig, ax, "事实来源：新华网 2026-11-20；湖北移动 5G-A 网络建设进展")

    fig.savefig(OUT + "图3_三层结构.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)
