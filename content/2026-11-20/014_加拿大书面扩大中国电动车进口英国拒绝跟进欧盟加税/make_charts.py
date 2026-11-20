# -*- coding: utf-8 -*-
"""
《加拿大书面扩大中国电动车进口，英国拒绝跟进欧盟加税》配套图表
事实口径（均经公开报道交叉核对）：
  · 2026-11-17 深圳 APEC 期间，习近平会见加拿大总理卡尼（Mark Carney），系一年内第三次会面。
    加拿大总理办公室同日发布公告：双方就进一步扩大贸易的新措施达成一致。
    —— 联合早报 2026-11-17、香港01 2026-11-17、中国商务部 2026-11-17。
  · 加方承诺：将部分中国钢铝产品现有关税减免措施延长两年，并将减免范围扩大至另外 32 个关税税目；
    不对中国太阳能产品和半导体加征关税；扩大中国电动汽车进口。
    —— 加拿大总理办公室公告，中国产业经济信息网 2026-11-20 转述。
  · 中方对应：对约 4 亿加元的加拿大对华出口商品提供额外关税减免，
    含冷冻猪肉约 1.16 亿美元、鱼类与海产品约 2.85 亿美元；
    商务部表述为"进一步调整对加方部分农水产品采取的反歧视措施"。
    —— 香港01 2026-11-17 引加拿大总理办公室、中国商务部 2026-11-17。
  · 背景：加拿大前政府曾效仿美国对中国电动汽车征收 100% 关税，中方对油菜籽等加方产品反制；
    2026 年 1 月卡尼访华后，加方以低关税税率允许少量中国电动车进入，中方取消油菜籽关税。
    —— 纽约时报中文网 2026-11-18。
  · 2026-11-20 英欧峰会在布鲁塞尔举行，计划签署经济伙伴关系协议。
    欧盟要求英国在脱欧后新协议框架下对中国商品征收与欧盟同等水平关税，英国计划拒绝。
    若拒绝，"欧洲制造"（Made in Europe）准入将受影响。一名欧盟外交消息人士称峰会前气氛"相当冷淡"。
    —— 英国《金融时报》，参考消息/澎湃 2026-11-19、俄罗斯卫星通讯社 2026-11-19。
  · 英国商贸大臣雷诺兹（Jonathan Reynolds）此前多次表态：英国贸易防御关税决定依据本国利益，
    不因他国要求而改变（2026-10-14 中央社、10-21 联合早报）。
  · 福特欧洲总裁 Jim Baumbick（2026-11-17）：若欧盟将英国、土耳其、摩洛哥排除在
    "欧洲制造"模式之外，非但无法强化本土产业以对抗中国竞争，反而会损害欧盟自身汽车工业；
    并以在土耳其组装的 Ford Transit 为例。法国《汽车杂志》称其用词为"自残"（automutilation）。
    —— 路透社 2026-11-17、Daily Sabah 2026-11-18、journalauto 2026-11-18。
  · 行业侧：ACEA 与 SMMT 2026-11-17 联合声明，英欧汽车年贸易额约 800 亿欧元；
    2027-01-01 起 TCA 更严原产地规则生效，业内调查称明年跨境电动车不足四分之一合规，
    将面临 10% 关税，2027 年一年账单约 UK→EU 4 亿欧元、EU→UK 14 亿欧元；
    "欧洲制造"拟议的 Industrial Accelerator Act 若排除英国产整车/零部件/电池，
    将使其无法获得补贴与政府采购资格。英国汽车生产支撑欧盟 240 亿欧元经济活动、25 万个岗位。
    —— ACEA/SMMT 联合新闻稿 2026-11-17。
说明：素材称"中方新增对每年价值 4 亿加元的加拿大农产品出口给予关税减免"作为"对等安排"，
      经核 4 亿加元为中方减免所覆盖的加方对华出口规模（含冷冻猪肉与鱼类海产品），
      加方对应动作是延长钢铝豁免并扩围，二者并非等额对价，图中按双向安排并列呈现。
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
    fig = base("一份书面安排，两个方向",
               "2026-11-17 中加经贸磋商成果：加方给什么，中方给什么")
    ax = canvas(fig)

    # 左：加方
    ax.add_patch(FancyBboxPatch((0.055, 0.320), 0.400, 0.450,
                                boxstyle="round,pad=0.012", facecolor="#eef2f6",
                                edgecolor=NAVY, linewidth=1.3))
    ax.text(0.080, 0.725, "加方承诺", fontsize=14.0, color=NAVY, weight="bold",
            ha="left", va="center")
    ax.text(0.080, 0.680, "总理办公室公告，书面", fontsize=9.2, color=GRAY,
            ha="left", va="center")
    left_items = [
        "扩大中国电动汽车进口",
        "不对中国太阳能产品加税",
        "不对中国半导体加税",
        "钢铝豁免延长 2 年",
        "钢铝豁免扩至另 32 个税目",
    ]
    yy = 0.610
    for it in left_items:
        ax.text(0.080, yy, "·  " + it, fontsize=9.4, color=DARK, ha="left",
                va="center")
        yy -= 0.054
    ax.text(0.080, 0.352, "北美关税框架的外溢边界，在这里松了",
            fontsize=9.0, color=NAVY, weight="bold", ha="left", va="center")

    # 右：中方
    ax.add_patch(FancyBboxPatch((0.545, 0.320), 0.400, 0.450,
                                boxstyle="round,pad=0.012", facecolor="#f7f3ea",
                                edgecolor=GOLD, linewidth=1.3))
    ax.text(0.570, 0.725, "中方对应", fontsize=14.0, color=GOLD, weight="bold",
            ha="left", va="center")
    ax.text(0.570, 0.680, "商务部：调整部分农水产品反歧视措施", fontsize=9.0,
            color=GRAY, ha="left", va="center")

    ax.text(0.570, 0.615, "约 4 亿加元", fontsize=19.0, color=GOLD,
            weight="bold", ha="left", va="center")
    ax.text(0.570, 0.572, "加拿大对华出口商品获额外关税减免", fontsize=9.2,
            color=SLATE, ha="left", va="center")

    sub_items = [
        "冷冻猪肉　约 1.16 亿美元",
        "鱼类与海产品　约 2.85 亿美元",
    ]
    yy = 0.512
    for it in sub_items:
        ax.text(0.570, yy, "·  " + it, fontsize=9.2, color=DARK, ha="left",
                va="center")
        yy -= 0.052
    ax.text(0.570, 0.395, "油菜籽关税此前已取消", fontsize=9.0, color=GRAY,
            ha="left", va="center")
    ax.text(0.570, 0.355, "不是等额对价，是双向各让一步",
            fontsize=9.0, color=RED, weight="bold", ha="left", va="center")

    # 中间双向箭头
    ax.annotate("", xy=(0.540, 0.595), xytext=(0.470, 0.595),
                arrowprops=dict(arrowstyle="-|>", color=NAVY, linewidth=1.8))
    ax.annotate("", xy=(0.470, 0.490), xytext=(0.540, 0.490),
                arrowprops=dict(arrowstyle="-|>", color=GOLD, linewidth=1.8))

    ax.text(0.055, 0.215,
            "从口头表态到书面安排：上一轮是“可能转向与中国车企合作”，这一轮是可执行的关税条目。",
            fontsize=9.0, color=SLATE, ha="left", va="center")

    punchline(fig, "增量不在“态度变好”，在于它写进了公告。")
    footer(fig, "事实：加拿大总理办公室 2026-11-17 公告、中国商务部 2026-11-17 答记者问、香港01 与联合早报 2026-11-17｜制图：本文")
    fig.savefig(OUT + "图1_一份书面安排.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("英国这次没跟",
               "欧盟要的是“关税对齐”，英国要的是“欧洲制造”准入")
    ax = canvas(fig)

    # 上：欧盟的要求与筹码
    ax.add_patch(FancyBboxPatch((0.070, 0.640), 0.860, 0.170,
                                boxstyle="round,pad=0.010", facecolor="#eef2f6",
                                edgecolor=NAVY, linewidth=1.2))
    ax.text(0.094, 0.770, "欧盟的要求", fontsize=11.0, color=NAVY,
            weight="bold", ha="left", va="center")
    ax.text(0.094, 0.718,
            "在脱欧后新协议框架下，对中国商品征收与欧盟同等水平关税",
            fontsize=9.4, color=DARK, ha="left", va="center")
    ax.text(0.094, 0.672,
            "交换条件：英国汽车可进入“欧洲制造”计划，享受补贴与政府采购优先",
            fontsize=9.4, color=SLATE, ha="left", va="center")

    # 中：英国的选择
    ax.add_patch(FancyBboxPatch((0.070, 0.370), 0.860, 0.220,
                                boxstyle="round,pad=0.010", facecolor="#f7eae8",
                                edgecolor=RED, linewidth=1.2))
    ax.text(0.094, 0.530, "英国的计划：拒绝", fontsize=11.0, color=RED,
            weight="bold", ha="left", va="center")
    ax.text(0.094, 0.478,
            "商贸大臣雷诺兹：贸易防御关税决定依据英国自身利益，不因他国要求而改变",
            fontsize=9.2, color=DARK, ha="left", va="center")
    ax.text(0.094, 0.432,
            "代价：若拒绝，“欧洲制造”准入将受影响",
            fontsize=9.2, color=RED, weight="bold", ha="left", va="center")
    ax.text(0.094, 0.390,
            "一名欧盟外交消息人士：峰会前气氛“相当冷淡”",
            fontsize=9.0, color=SLATE, ha="left", va="center")

    # 下：为什么难
    ax.add_patch(FancyBboxPatch((0.070, 0.155), 0.860, 0.170,
                                boxstyle="round,pad=0.010", facecolor=SAND,
                                edgecolor="#d9cdb6", linewidth=1.0))
    ax.text(0.094, 0.285, "两难在哪", fontsize=10.0, color="#8a7a5e",
            weight="bold", ha="left", va="center")
    ax.text(0.094, 0.235,
            "跟着加税：怕招来中方反制；不加税：怕被排除在“欧洲制造”之外",
            fontsize=9.2, color="#7a6746", ha="left", va="center")
    ax.text(0.094, 0.190,
            "英国汽车生产支撑欧盟约 240 亿欧元经济活动、25 万个岗位",
            fontsize=9.2, color="#7a6746", ha="left", va="center")

    punchline(fig, "“统一加税”变成了“规则准入”，武器从税率换成了资格。")
    footer(fig, "事实：英国《金融时报》2026-11-19（参考消息/澎湃、卫星社转述）；雷诺兹表态据中央社 2026-10-14；岗位数据据 ACEA/SMMT 2026-11-17｜制图：本文")
    fig.savefig(OUT + "图2_英国这次没跟.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("排除三个国家，谁受损",
               "福特欧洲总裁：这会“自残”，不是强化")
    ax = canvas(fig)

    # 左：被排除的三国
    ax.text(0.070, 0.810, "“欧洲制造”若排除", fontsize=11.0, color=DARK,
            weight="bold", ha="left", va="center")

    countries = [
        ("英国", "欧盟最大汽车出口市场，也是其最大汽车贸易伙伴", NAVY),
        ("土耳其", "Ford Transit 在此组装", GOLD),
        ("摩洛哥", "欧洲整车厂的近岸配套基地", GREEN),
    ]
    for i, (name, note, col) in enumerate(countries):
        y = 0.740 - i * 0.145
        ax.add_patch(FancyBboxPatch((0.070, y - 0.110), 0.380, 0.110,
                                    boxstyle="round,pad=0.008",
                                    facecolor="#fafbfc", edgecolor=col,
                                    linewidth=1.1))
        ax.text(0.092, y - 0.038, name, fontsize=12.0, color=col,
                weight="bold", ha="left", va="center")
        ax.text(0.092, y - 0.082, note, fontsize=8.2, color=SLATE,
                ha="left", va="center")

    # 右：后果
    ax.add_patch(FancyBboxPatch((0.490, 0.400), 0.450, 0.410,
                                boxstyle="round,pad=0.012", facecolor="#f7eae8",
                                edgecolor=RED, linewidth=1.3))
    ax.text(0.514, 0.762, "后果", fontsize=12.0, color=RED, weight="bold",
            ha="left", va="center")
    ax.text(0.514, 0.700,
            "非但无法强化本土产业、\n抵御中国车企竞争，",
            fontsize=9.8, color=DARK, ha="left", va="center", linespacing=1.8)
    ax.text(0.514, 0.618,
            "反而会损害\n欧盟自身汽车工业。",
            fontsize=9.8, color=RED, weight="bold", ha="left", va="center",
            linespacing=1.8)
    ax.text(0.514, 0.520,
            "—— Jim Baumbick，福特欧洲总裁\n（2026-11-17，路透社）",
            fontsize=8.6, color=SLATE, ha="left", va="center",
            linespacing=1.7)

    # 底部：2027 关税账单
    ax.add_patch(FancyBboxPatch((0.070, 0.150), 0.870, 0.140,
                                boxstyle="round,pad=0.010", facecolor=SAND,
                                edgecolor="#d9cdb6", linewidth=1.0))
    ax.text(0.092, 0.255, "另一笔账：2027 年 1 月 1 日起原产地规则收紧", fontsize=9.6,
            color="#8a7a5e", weight="bold", ha="left", va="center")
    ax.text(0.092, 0.212,
            "业内调查：明年跨境电动车不足四分之一合规，将面临 10% 关税",
            fontsize=9.0, color="#7a6746", ha="left", va="center")
    ax.text(0.092, 0.176,
            "一年账单：英国对欧盟出口约 4 亿欧元，欧盟对英国出口约 14 亿欧元",
            fontsize=9.0, color=RED, weight="bold", ha="left", va="center")

    punchline(fig, "保护范围划得越窄，被划在外面的自家产能就越多。")
    footer(fig, "事实：Baumbick 表态据路透社 2026-11-17、Daily Sabah 2026-11-18；关税账单与合规比例据 ACEA/SMMT 联合新闻稿 2026-11-17｜制图：本文")
    fig.savefig(OUT + "图3_排除三个国家.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)
