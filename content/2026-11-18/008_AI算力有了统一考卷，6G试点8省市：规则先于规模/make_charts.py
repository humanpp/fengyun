# -*- coding: utf-8 -*-
"""
《AI 算力有了「统一考卷」，6G 试点 8 省市：规则开始先于规模》配套图表
事实口径（均已核对官方原文）：
  · 市场监管总局（国家标准委）批准发布《智能计算集群效能指标与测试方法》
    国家标准化指导性技术文件，标准号 GB/Z 328-2026，发布日期 2026-10-30，
    2026-11-17 由市场监管总局对外公布；由 SWG32（全国智能计算标准化工作组）归口，
    主管部门国家标准委；标准类别为方法，CCS L80，ICS 35.080。
    主要起草单位 20 家，含之江实验室、阿里云、中国电信、中兴通讯、中国信通院、
    蚂蚁科技、成都超算、中国软件评测中心、浪潮信息、超聚变、中移（苏州）软件、
    海光信息、浙江大华、京东科技、联想（北京）、上海超级计算中心、上海曦智科技、
    深圳思谋信息、中国科学院计算机网络信息中心等。
  · 指标体系：训练效能从计算性能、收敛性能、稳定性能、混合集群性能四个维度设置
    模型算力利用率、训练计算能效、收敛速度、有效训练时间占比等指标；推理效能围绕
    吞吐率、响应时延、并发处理能力及计算能效；针对异构算力协同提出混合训练效率、
    能效损失比。文件同时明确测试流程、计算方法与结果报告要求，提供基准参考模型及
    典型测试框架。背景：集群向千卡、万卡乃至更大规模发展，传统以硬件峰值算力为主
    的评价方式难以反映实际效能。
    来源：市场监管总局 2026-11-17 发布稿；全国标准信息公共服务平台标准详情页。
  · 工业和信息化部办公厅《关于同意北京市等8个省（市）开展6G创新发展部省协同试点
    工作的复函》，工信厅通信函〔2026〕558 号，成文并发布于 2026-11-17。同意北京市、
    河北省、上海市、江苏省、浙江省、安徽省、湖北省、广东省为试点省（市）。复函共
    六条，其中：第三条要求涉及 6G 商业应用的须依规取得电信业务经营许可，未获许可前
    不得开展商业化应用场景探索；第四条要求涉频率、台站、发射设备须依法取得相应许可
    与型号核准；第五条要求规范 6G 新闻宣传、内外有别严格审查；第六条明确按《6G 创新
    发展部省协同试点专项行动管理办法》定期开展试点评价。
  · 前置文件：工信部办公厅《关于组织开展6G创新发展部省协同试点专项行动的通知》
    （工信厅通信函﹝2026﹞255 号，2026-06-04），提出到 2029 年为 6G 商用落地提供
    支撑；有关省（市）选择 1 至 3 个特色发展方向编制方案，2026-07-31 前报送；
    实施期限原则上为 3 年，自批复之日起计算。
风格：克制传媒风，白底、低饱和配色、标题即结论。输出目录 = 脚本所在目录。
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch

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


# ------------------------------------------------------------------ 图 1
def fig1():
    fig = base("这张考卷考什么",
               "GB/Z 328-2026：训练四项、推理四项，外加异构协同两项")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # 左：训练侧
    ax.add_patch(Rectangle((0.045, 0.305), 0.440, 0.605, facecolor="white",
                           edgecolor=LIGHT, linewidth=1.1, zorder=2))
    ax.text(0.068, 0.856, "训练侧", fontsize=12.4, color=NAVY, weight="bold",
            ha="left", va="center", zorder=3)
    ax.text(0.068, 0.806, "从计算、收敛、稳定、混合集群四个维度看",
            fontsize=8.8, color=GRAY, ha="left", va="center", zorder=3)
    train = ["模型算力利用率", "训练计算能效", "收敛速度", "有效训练时间占比"]
    yy = 0.720
    for i, item in enumerate(train, 1):
        ax.text(0.068, yy, f"0{i}", fontsize=9.6, color=RED, weight="bold",
                ha="left", va="center", zorder=3)
        ax.text(0.115, yy, item, fontsize=10.4, color=DARK, ha="left",
                va="center", zorder=3)
        yy -= 0.108

    # 右：推理侧
    ax.add_patch(Rectangle((0.515, 0.305), 0.440, 0.605, facecolor="white",
                           edgecolor=LIGHT, linewidth=1.1, zorder=2))
    ax.text(0.538, 0.856, "推理侧", fontsize=12.4, color=NAVY, weight="bold",
            ha="left", va="center", zorder=3)
    ax.text(0.538, 0.806, "围绕实际服务场景下的性能表现",
            fontsize=8.8, color=GRAY, ha="left", va="center", zorder=3)
    infer = ["吞吐率", "响应时延", "并发处理能力", "计算能效"]
    yy = 0.720
    for i, item in enumerate(infer, 1):
        ax.text(0.538, yy, f"0{i}", fontsize=9.6, color=RED, weight="bold",
                ha="left", va="center", zorder=3)
        ax.text(0.585, yy, item, fontsize=10.4, color=DARK, ha="left",
                va="center", zorder=3)
        yy -= 0.108

    # 底：异构协同
    ax.add_patch(FancyBboxPatch((0.045, 0.130), 0.910, 0.140,
                                boxstyle="round,pad=0.012", facecolor=SAND,
                                edgecolor="#d9cdb6", linewidth=1.0, zorder=2))
    ax.text(0.070, 0.225, "异构协同", fontsize=10.0, color="#7a6746",
            weight="bold", ha="left", va="center", zorder=3)
    ax.text(0.070, 0.168, "混合训练效率　·　能效损失比", fontsize=11.0,
            color="#7a6746", ha="left", va="center", zorder=3)

    punchline(fig, "以前各家报各家的数，现在要按同一套流程、同一个基准模型跑。")
    footer(fig, "依据：GB/Z 328-2026 指标设置，据市场监管总局 2026-11-17 发布稿与标准详情页｜制图：本文")
    fig.savefig(OUT + "图1_这张考卷考什么.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("6G 试点的规则链条，比试点本身更长",
               "从印发通知到复函批复，前后五个月")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    events = [
        ("2026/06/04", "专项行动通知印发",
         "每省选 1 至 3 个特色发展方向（工信厅通信函﹝2026﹞255 号）", NAVY),
        ("2026/07/31", "工作方案报送截止",
         "经省级政府审核后报工信部，随后进入形式审查、现场评审", NAVY),
        ("2026/11/17", "复函同意 8 个省市",
         "京津冀沪苏浙皖鄂粤；工信厅通信函〔2026〕558 号", RED),
        ("批复起 3 年", "实施期限原则上三年",
         "自批复之日起计算，到期按《管理办法》开展试点评价", NAVY),
        ("2029 年", "通知设定的商用目标",
         "为 6G 商用落地提供支撑，试点需在此之前跑出结果", NAVY),
    ]

    ax.plot([0.150, 0.150], [0.240, 0.930], color=LIGHT, linewidth=1.4)

    ys = [0.890, 0.720, 0.550, 0.380, 0.210]
    for (date, head, body, color), yy in zip(events, ys):
        ax.plot([0.150], [yy], marker="o", markersize=7, color=color,
                zorder=4, clip_on=False)
        ax.text(0.128, yy, date, fontsize=9.0, color=color, weight="bold",
                ha="right", va="center")
        ax.text(0.185, yy + 0.032, head, fontsize=11.2, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(0.185, yy - 0.040, body, fontsize=8.7, color=SLATE,
                ha="left", va="center")

    # 右侧：复函里的三条边界
    ax.add_patch(FancyBboxPatch((0.640, 0.330), 0.315, 0.635,
                                boxstyle="round,pad=0.014", facecolor="white",
                                edgecolor=RED, linewidth=1.1, zorder=2))
    ax.text(0.662, 0.930, "复函里的三条边界", fontsize=10.2, color=RED,
            weight="bold", ha="left", va="center", zorder=3)
    edges = [
        ("第三条", "未获许可前，不得开展\n商业化应用场景探索"),
        ("第四条", "频率、台站、发射设备\n须依法取得相应许可"),
        ("第五条", "规范 6G 新闻宣传，\n内外有别、严格审查"),
    ]
    yy = 0.855
    for tag, body in edges:
        ax.text(0.662, yy, tag, fontsize=9.4, color=RED, weight="bold",
                ha="left", va="center", zorder=3)
        ax.text(0.662, yy - 0.078, body, fontsize=8.6, color=SLATE, ha="left",
                va="center", linespacing=1.7, zorder=3)
        yy -= 0.170

    punchline(fig, "先划边界，再发许可；试点还没开始，红线已经画完了。")
    footer(fig, "依据：工信部复函（工信厅通信函〔2026〕558 号）与 2026-06-04 专项行动通知｜制图：本文")
    fig.savefig(OUT + "图2_6G试点的规则链条.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("两份文件，同一个动作",
               "一份统一评价口径，一份划出许可边界——都发生在放量之前")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # 左：算力
    ax.add_patch(Rectangle((0.045, 0.330), 0.440, 0.570, facecolor="white",
                           edgecolor=LIGHT, linewidth=1.1, zorder=2))
    ax.text(0.068, 0.852, "算力：先统一怎么量", fontsize=11.6, color=NAVY,
            weight="bold", ha="left", va="center", zorder=3)
    left = [
        "GB/Z 328-2026，10 月 30 日发布",
        "指导性技术文件，不是强制标准",
        "20 家单位共同起草",
        "目的是让不同架构、不同规模可比",
    ]
    yy = 0.762
    for item in left:
        ax.text(0.068, yy, "·  " + item, fontsize=9.2, color=SLATE,
                ha="left", va="center", zorder=3)
        yy -= 0.118

    # 右：通信
    ax.add_patch(Rectangle((0.515, 0.330), 0.440, 0.570, facecolor="white",
                           edgecolor=RED, linewidth=1.1, zorder=2))
    ax.text(0.538, 0.852, "通信：先划清能做与不能做", fontsize=11.6, color=RED,
            weight="bold", ha="left", va="center", zorder=3)
    right = [
        "558 号复函，11 月 17 日批复",
        "8 个省市，实施期原则上 3 年",
        "商业化前须先取得电信业务许可",
        "频率与设备须依法核准",
    ]
    yy = 0.762
    for item in right:
        ax.text(0.538, yy, "·  " + item, fontsize=9.2, color=SLATE,
                ha="left", va="center", zorder=3)
        yy -= 0.118

    ax.plot([0.500, 0.500], [0.330, 0.900], color=LIGHT, linewidth=1.0,
            linestyle=(0, (4, 4)))

    # 底：结论 + 限定
    ax.add_patch(FancyBboxPatch((0.045, 0.150), 0.910, 0.145,
                                boxstyle="round,pad=0.012", facecolor=SAND,
                                edgecolor="#d9cdb6", linewidth=1.0, zorder=2))
    ax.text(0.070, 0.248, "但要说准一点：", fontsize=9.2, color="#7a6746",
            ha="left", va="center", zorder=3)
    ax.text(0.070, 0.190,
            "规则不是先于一切，是先于下一轮更大规模的扩张。",
            fontsize=10.8, color="#7a6746", weight="bold", ha="left",
            va="center", zorder=3)

    punchline(fig, "建完了再统一口径，等于让所有人返工；建之前定，成本最低。")
    footer(fig, "依据：市场监管总局发布稿、全国标准信息公共服务平台、工信部复函与专项行动通知｜制图：本文")
    fig.savefig(OUT + "图3_两份文件同一个动作.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)
