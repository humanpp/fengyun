# -*- coding: utf-8 -*-
"""
《香港给AI定七项行动，网信办备案再增133款：AI治理开始"认领任务、定期交卷"》配套图表

事实口径（全部核到官方原文或原始文书）：

一、内地备案/登记（国家网信办《关于发布生成式人工智能服务已备案信息的公告》）
  · 2026年9月至10月期（2026-11-20 17:00 发布）：
    新增 133 款生成式AI服务完成备案，其中 3 款提供手机端侧服务、1 款提供
    拟人化互动服务；1 款备案信息发生变更；通过 API 等方式直接调用已备案模型
    能力的应用或功能，由地方网信办登记，新增 224 款。
    截至 10 月 31 日，累计 1245 款服务完成备案、955 款应用或功能完成登记。
  · 2026年7月至8月期（2026-09-14 18:00 发布）：新增 124 款备案，
    其中 7 款手机端侧；新增登记 133 款；截至 8 月 31 日累计 1112 款备案、
    731 款登记。
  · 首期专门公布手机端侧：2026-07-15《关于发布7款提供手机端侧生成式人工智能
    服务已备案信息的公告》，含"Apple智能""华为小艺AI大模型""vivo蓝心端侧大模型"等。
  · 依据：《生成式人工智能服务管理暂行办法》第十七条——提供具有舆论属性或者
    社会动员能力的生成式人工智能服务的，应当按照国家有关规定开展安全评估，
    并按《互联网信息服务算法推荐管理规定》履行算法备案手续。
  · 备案在"国家网信办"完成，登记在"地方网信办"完成——两级、两个动作。

二、香港七项行动
  · 2026-11-20 政务司司长陈国基召开"人工智能风险管治统筹工作组"首次会议，
    检视及统筹七项具体行动的工作计划和落实方案；工作组按工作进度定期召开会议。
    据政府新闻公报 2026-11-20 13:13（P2026112000406）。
  · 七项行动的"谁来做/什么时间"写在《行政长官2026年施政报告》第123条
    （2026-09-16）：(i) 打击利用AI犯罪—法改会电脑网络罪行小组委员会检视法律、
    财库局今年内就下架金融诈骗内容公众咨询；(ii) 保护未成年使用者—教育局
    《价值观教育课程架构》(2026)，律政司领导小组辖下设"儿童使用社交媒体"专责小组；
    (iii) 推动市场评估AI道德风险—创科局挑选试点部门，采购时要求投标者作安全和
    道德合规申报；(iv) 各行业安全有序应用AI—数字办推动行业指引、认证及治理框架；
    (v) AI产品导致意外的法律责任—律政司领导的工作组检视现行法律，研究以立法或
    规例（含实务守则/行为守则、指引等软法）处理；(vi) 管理AI Agent—数字办政府
    内部试行，明年与香港人工智能研发院发布全社会适用指引；(vii) 就业影响—
    劳福局人力推算中期更新报告分析AI对劳动市场影响。
  · 施政报告第122条：七项行动的表述为"打击利用AI犯罪、保护未成年使用者、
    建立规范AI伦理道德的治理框架、推广应用安全、釐清产品导致意外的责任、
    制定AI Agent安全管理指引，以及研究广泛使用AI所带来的影响"。
  · 施政报告第123条并载明：政务司司长统筹推进，并在数字政策办公室设立AI专员。
  · 脚注12（政府内部现行规范）：AI Agent 只宜用于标准化、重复性的内部政务，
    不得直接面向公众作决定，亦不得取代人员的专业判断；高风险动作须维持人为监督；
    禁止把机密或个人资料输送至外部平台；上线前须完成风险评估；严格控制权限、
    隔离运作环境、保存操作纪录，确保安全、可控、可追溯。
  · 2026-10-08 立法会：律政司司长林定国——"AI犯错，谁来负责？这个议题，
    律政司将会牵头成立专责小组，尽快研究运用AI产品造成损害的法律责任问题。"
    （律政司司长致辞全文，2026-10-08）

三、对照事实
  · 工信部《关于加强智能体终端设备进网管理的通知》（工信厅信管〔2026〕42号），
    成文 2026-10-24、发布 2026-11-06：智能体终端指预置安装智能体的手机、平板、
    可穿戴设备等电信终端设备；进网检测中开展智能体适配验证；终端上使用的智能体
    应参考智能体互联系列国家标准配备唯一身份码；OTA 现网升级须提交方案并经专家
    评估后方可正式提供服务；应用分发平台须公示适配验证列表。
  · Moffatt v. Air Canada, 2024 BCCRT 149（不列颠哥伦比亚民事解决庭，
    2024-02-14 裁决）：航空公司网页聊天机器人提供错误的丧亲票价信息，法庭认定
    公司须对自家网站上的信息负责，判赔 812.02 加元（650.88 元赔偿 +
    36.14 元利息 + 125 元庭费）。

风格：克制传媒风，白底、低饱和配色、标题即结论（沿用本工作区既有规范）
输出目录 = 脚本所在目录
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

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
BLUSH = "#fbf1ef"

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
    fig = plt.figure(figsize=(12, 6.8))
    ax = new_axes(fig)

    header(fig, "这一期：模型层 +133，应用层 +224",
           "两行数字同表发布，但一行在国家网信办备案，一行在地方网信办登记")

    # 左：本期新增，两根柱
    ax.text(0.050, 0.760, "9—10 月新增", fontsize=10.0, color=GRAY,
            ha="left", va="center")
    ax.plot([0.050, 0.500], [0.732, 0.732], color=LIGHT, linewidth=1.0)

    base_y = 0.415
    bar_w = 0.105
    scale = 0.290 / 240.0

    bars = [
        (0.105, 133, NAVY, "备案", "在国家网信办"),
        (0.285, 224, RED, "登记", "在地方网信办"),
    ]
    for x, val, color, label, where in bars:
        h = val * scale
        ax.add_patch(Rectangle((x, base_y), bar_w, h,
                               facecolor=color, edgecolor=color,
                               linewidth=0, zorder=4, alpha=0.90))
        ax.text(x + bar_w / 2, base_y + h + 0.028, f"{val}",
                fontsize=21, color=color, weight="bold",
                ha="center", va="bottom", zorder=6)
        ax.text(x + bar_w / 2, base_y - 0.028, label, fontsize=11.6,
                color=DARK, weight="bold", ha="center", va="top", zorder=6)
        ax.text(x + bar_w / 2, base_y - 0.062, where, fontsize=8.8,
                color=GRAY, ha="center", va="top", zorder=6)

    ax.plot([0.060, 0.492], [base_y, base_y], color=SLATE,
            linewidth=1.1, zorder=5)

    ax.text(0.060, 0.300,
            "133 中是 3 款手机端侧、1 款拟人化互动；\n"
            "224 是通过 API 调用已备案模型的应用或功能。",
            fontsize=9.4, color=SLATE, ha="left", va="top",
            linespacing=1.70)

    # 右：累计
    ax.text(0.585, 0.760, "截至 10 月 31 日累计", fontsize=10.0, color=GRAY,
            ha="left", va="center")
    ax.plot([0.585, 0.952], [0.732, 0.732], color=LIGHT, linewidth=1.0)

    rows = [
        ("生成式AI服务备案", "1245", NAVY),
        ("应用或功能登记", "955", RED),
    ]
    y = 0.640
    for label, value, color in rows:
        ax.text(0.585, y + 0.038, label, fontsize=10.2, color=GRAY,
                ha="left", va="center", zorder=6)
        ax.text(0.585, y - 0.020, value, fontsize=25, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        y -= 0.155

    card(ax, 0.585, 0.235, 0.367, 0.150, LIGHT, face=PALE, lw=1.0)
    ax.text(0.608, 0.353, "登记 ÷ 备案", fontsize=9.6, color=GRAY,
            ha="left", va="center", zorder=6)
    ax.text(0.608, 0.297, "8 月末 0.657  →  10 月末 0.767",
            fontsize=11.4, color=DARK, weight="bold",
            ha="left", va="center", zorder=6)
    ax.text(0.608, 0.261, "两期增量：备案 133、登记 224",
            fontsize=9.0, color=SLATE, ha="left", va="center", zorder=6)

    punchline(fig, "模型层在备案，应用层在登记，两条队伍从前分开排。")
    footer(fig, "事实来源：国家网信办《关于发布生成式人工智能服务已备案信息的公告》"
                "（2026年9月至10月，2026-11-20；2026年7月至8月，2026-09-14）")
    fig.savefig(OUT + "图1_两行数字.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(12, 7.2))
    ax = new_axes(fig)

    header(fig, "七项行动，每一项后面都跟着一个名字和一个时间",
           "不是原则宣示，是写进施政报告第 123 条的任务清单")

    items = [
        ("打击利用AI犯罪", "法改会电脑网络罪行小组委员会检视法律；\n财库局今年内就下架金融诈骗内容作公众咨询"),
        ("加强保护未成年使用者", "教育局《价值观教育课程架构》(2026)；\n律政司领导小组辖下设「儿童使用社交媒体」专责小组"),
        ("推动市场评估AI道德风险", "创科局挑选试点部门，政府AI采购\n要求投标者作安全和道德合规申报"),
        ("推动各行业安全有序应用AI", "数字办推动行业AI应用指引、\n认证及治理框架；金管局、保监局、证监会分别跟进"),
        ("研究AI产品导致意外的法律责任", "律政司领导的工作组检视现行法律，\n研究以立法或软法（守则、指引）处理"),
        ("推出指引管理AI智能体", "数字办政府内部试行，明年与\n香港人工智能研发院发布全社会适用安全管理指引"),
        ("研究AI带来的就业影响", "劳福局人力推算中期更新报告\n分析AI对香港劳动市场的影响"),
    ]

    top = 0.800
    row_h = 0.089
    num_x = 0.052
    name_x = 0.105
    desc_x = 0.410

    for i, (name, desc) in enumerate(items):
        y = top - i * row_h
        highlight = i in (4, 5)

        if i % 2 == 0:
            ax.add_patch(Rectangle((0.045, y - 0.036), 0.908, row_h - 0.008,
                                   facecolor=PALE if not highlight else BLUSH,
                                   edgecolor="none", zorder=1))

        ax.text(num_x, y, f"{i + 1}", fontsize=11.4,
                color=RED if highlight else NAVY, weight="bold",
                ha="left", va="center", zorder=6)
        ax.text(name_x, y, name, fontsize=10.6,
                color=RED if highlight else DARK,
                weight="bold" if highlight else "normal",
                ha="left", va="center", zorder=6)
        ax.text(desc_x, y, desc, fontsize=8.6, color=SLATE,
                ha="left", va="center", linespacing=1.55, zorder=6)

    ax.text(0.045, 0.152,
            "第 5 项和第 6 项，是这份清单里唯一两处直接指向「AI 造成后果之后」的条款。",
            fontsize=9.6, color=DARK, ha="left", va="center")

    punchline(fig, "清单的分量不在七，在每个七后面那个负责单位。")
    footer(fig, "事实来源：《行政长官2026年施政报告》第122、123条（2026-09-16）；"
                "政府新闻公报 2026-11-20 首次会议")
    fig.savefig(OUT + "图2_七项行动.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(12, 7.0))
    ax = new_axes(fig)

    header(fig, "同一个缺口，三种绑法",
           "香港正在研究怎么绑，内地和加拿大已经各绑了一头")

    # 三列
    cols = [
        (0.045, "香港", "在问归谁", NAVY, "white",
         ["第 5 项：律政司领导的工作组，\n检视现行法律是否足够，\n研究立法，或守则、指引等软法",
          "第 6 项：明年发布全社会适用的\nAI Agent 安全管理指引",
          "内部试行期已写死一句：\n不得直接面向公众作决定，\n不得取代人员的专业判断"]),
        (0.365, "内地", "先绑终端", RED, "white",
         ["工信厅信管〔2026〕42号，\n成文 10/24、发布 11/6",
          "预置智能体的手机、平板、\n可穿戴设备，进网检测中\n须做智能体适配验证",
          "智能体参考国家标准\n配备唯一身份码；\nOTA 升级须先报方案再评估"]),
        (0.685, "加拿大", "已经判了", SLATE, "white",
         ["Moffatt v. Air Canada,\n2024 BCCRT 149，2024-02-14",
          "航空公司网页上的聊天机器人\n给了错的丧亲票价，\n公司说那是「另一个主体」",
          "法庭不认：公司须对\n自家网站上的信息负责，\n判赔 812.02 加元"]),
    ]

    for x, name, tag, color, face, bullets in cols:
        card(ax, x, 0.255, 0.270, 0.520, color, face=face,
             lw=1.5 if color != SLATE else 1.2)
        ax.text(x + 0.022, 0.712, name, fontsize=13.6, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(x + 0.022, 0.672, tag, fontsize=9.6, color=GRAY,
                ha="left", va="center", zorder=6)
        ax.plot([x + 0.022, x + 0.248], [0.646, 0.646], color=color,
                linewidth=0.9, alpha=0.35, zorder=5)
        y = 0.600
        for b in bullets:
            ax.text(x + 0.022, y, b, fontsize=8.5, color=DARK,
                    ha="left", va="top", linespacing=1.60, zorder=6)
            y -= 0.126 if b.count("\n") >= 1 else 0.086

    ax.text(0.045, 0.196,
            "三种做法指向同一件事：AI 自己不是责任主体，所以总要有一个"
            "「谁」被绑在上面——开发者、部署者，或者把话放出去的那家公司。",
            fontsize=9.4, color=SLATE, ha="left", va="center")

    punchline(fig, "治理往前挪一步，问的就不是管不管，而是谁签字、几时交卷。")
    footer(fig, "事实来源：《行政长官2026年施政报告》第123条及脚注12；"
                "工信厅信管〔2026〕42号；Moffatt v. Air Canada, 2024 BCCRT 149")
    fig.savefig(OUT + "图3_三种绑法.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)
