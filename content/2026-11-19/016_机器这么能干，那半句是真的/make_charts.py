# -*- coding: utf-8 -*-
"""
《机器这么能干，那半句是真的》配套图表
事实口径（2026-11-19，逐条核对原始报道与研究摘要后）：
  · 智元（AGIBOT）6 台精灵 G2 人形机器人于 2026 年 11 月 2 日 10:00 至 3 日 10:00，
    在上海徐汇区一家正常营业的好德便利店连续工作 24 小时，分任迎宾、取货打包、
    巡检补货、制作咖啡、收银出餐与清洁桌面；门店照常营业、顾客照常进店；
    24 小时内累计完成 1,730 项任务，其中接待顾客 683 次、取送商品 369 件、
    补货巡检 277 次、制作咖啡 147 次；直播全网超 200 万人观看；
    6 台机器人中 4 台通过「转正」考核、2 台暂未通过核验
    （新华社 11-04、央广网 11-06、智元官方 11-03/11-09、羊城派 11-04、深圳新闻网 11-04）。
  · 团队自述：首次实地部署尚未达到百分之百成功率；当前最紧迫的问题是作业节拍（运行速度），
    出于安全考虑机器人暂以平缓、限速方式完成任务（央广网 11-06 引算法专家王溯恺、副总裁任广辉）。
  · 中国网络视听协会 2026 年第一季度《微短剧创作指引》：全行业上线微短剧约 12.8 万部，
    其中 AI 微短剧约 12.2 万部，占比超过 95%（人民网 05-02、光明日报 05-02、
    上海市新闻办 05-02、中国网络视听节目服务协会 08-13）。
  · 同一份指引：以 2026 年春节档为例，真人剧上线量约为 AI 剧的 1/50，
    但总播放量达到 AI 剧的 25 倍（人民网 05-02、光明日报 05-02、上海市新闻办 05-02）。
  · 国家广电总局局长曹淑敏 2026 年 11 月 4 日在中国广播电视精品创作大会上介绍：
    今年前 10 个月已上线微短剧近 55 万部，是 2025 年全年的近 17 倍，其中 AI 剧超过 94%（财新 11-14）。
  · 普洛cter & Gamble 预注册田野实验：791 名在职专业人员随机分配至单独作业、
    双人团队、以及其中一方配备生成式 AI 的条件；结果显示使用 AI 的个人，
    其创新工作质量与不使用 AI 的两人团队相当；而「人 + AI」团队产出卓越想法的
    可能性显著更高（Dell'Acqua、Lakhani、Mollick 等，《Organization Science》，
    2026 年 6 月 12 日在线发表；密歇根大学罗斯商学院 11-17 新闻稿）。
  · 「一个人加 AI 干二十个人的活」：素材原文转述的网络流行说法，
    本文检索未找到任何研究、统计或企业披露支持这一倍数（记为「未找到出处」）。
本文换算（非当事方口径）：1,730 ÷ 24 ≈ 每小时 72 项；再按 6 台均摊 ≈ 每台每小时 12 项；
12.2 ÷ 12.8 ≈ 95.3%；12.8 − 12.2 = 0.6 万部（真人微短剧，按合计数相减得到）。
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

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep


def base(title, sub):
    fig = plt.figure(figsize=(12, 6.8))
    fig.patch.set_facecolor("white")
    fig.text(0.045, 0.950, title, fontsize=20, color=DARK, weight="bold",
             ha="left", va="top")
    fig.text(0.045, 0.876, sub, fontsize=10.4, color=GRAY, ha="left", va="top")
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
    fig = base("6 台上岗，4 台转正",
               "2026 年 11 月 2 日 10:00 — 3 日 10:00｜上海徐汇一家正常营业的便利店｜6 台智元精灵 G2")
    ax = canvas(fig)

    x0 = 0.300
    scale = 0.290 / 700.0

    rows = [
        ("接待顾客", "683 次", 683, NAVY),
        ("取送商品", "369 件", 369, NAVY),
        ("补货巡检", "277 次", 277, NAVY),
        ("制作咖啡", "147 次", 147, NAVY),
        ("其余任务", "254 项", 254, LIGHT),
    ]

    y = 0.845
    for name, note, v, color in rows:
        ax.add_patch(Rectangle((x0, y - 0.036), max(v * scale, 0.004), 0.072,
                               facecolor=color, edgecolor="none"))
        ax.text(0.028, y + 0.021, name, fontsize=10.6, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(0.028, y - 0.026, note, fontsize=8.4, color=GRAY, ha="left",
                va="center")
        tx = x0 + max(v * scale, 0.004) + 0.014
        ax.text(tx, y, "{:,}".format(v), fontsize=11.6, color=DARK,
                weight="bold", ha="left", va="center")
        y -= 0.145

    ax.add_patch(FancyBboxPatch((0.028, 0.088), 0.590, 0.098,
                                boxstyle="round,pad=0.008",
                                facecolor="white", edgecolor=LIGHT,
                                linewidth=1.0))
    ax.text(0.052, 0.155, "合计 1,730 项任务", fontsize=10.0, color=NAVY,
            weight="bold", ha="left", va="center")
    ax.text(0.052, 0.115,
            "1,730 ÷ 24 ≈ 每小时 72 项；6 台均摊，每台每小时约 12 项（本文换算）",
            fontsize=8.6, color=SLATE, ha="left", va="center")

    # 右：考核结果
    ax.text(0.665, 0.858, "24 小时后的考核结果", fontsize=10.0, color=DARK,
            weight="bold", ha="left", va="center")

    cells = [(0.665, 0.700, NAVY), (0.762, 0.700, NAVY), (0.859, 0.700, NAVY),
             (0.665, 0.596, NAVY), (0.762, 0.596, RED), (0.859, 0.596, RED)]
    for cx, cy, color in cells:
        face = color if color == NAVY else "white"
        ax.add_patch(FancyBboxPatch((cx, cy), 0.068, 0.068,
                                    boxstyle="round,pad=0.004",
                                    facecolor=face, edgecolor=color,
                                    linewidth=1.4))

    ax.text(0.665, 0.505, "4 台转正", fontsize=15.0, color=NAVY,
            weight="bold", ha="left", va="center")
    ax.text(0.665, 0.435, "2 台暂未通过核验", fontsize=10.0, color=RED,
            ha="left", va="center")
    ax.text(0.665, 0.352, "首次实地部署尚未达到百分之百成功率；", fontsize=8.6,
            color=SLATE, ha="left", va="center")
    ax.text(0.665, 0.300, "团队自述最紧迫的问题是作业节拍，", fontsize=8.6,
            color=SLATE, ha="left", va="center")
    ax.text(0.665, 0.248, "目前按平缓、限速方式完成任务。", fontsize=8.6,
            color=SLATE, ha="left", va="center")

    punchline(fig, "能干是真的，能干到不需要人，还不是。")
    footer(fig, "事实：任务数据与考核结果据智元官方 11-03/11-09、新华社 11-04、央广网 11-06｜"
                "「其余任务」为合计数相减所得，每小时均摊为本文换算｜制图：本文")
    fig.savefig(OUT + "图1_6台上岗4台转正.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("95% 的产量，25 倍的播放",
               "2026 年第一季度微短剧供给结构，与同年春节档的需求反差")
    ax = canvas(fig)

    # 上：供给结构
    ax.text(0.028, 0.862, "供给端：2026 年一季度全行业上线微短剧", fontsize=10.0,
            color=DARK, weight="bold", ha="left", va="center")

    bx, bw, by, bh = 0.028, 0.944, 0.690, 0.082
    ai_w = bw * (12.2 / 12.8)
    ax.add_patch(Rectangle((bx, by), ai_w, bh, facecolor=NAVY,
                           edgecolor="none"))
    ax.add_patch(Rectangle((bx + ai_w, by), bw - ai_w, bh, facecolor=LIGHT,
                           edgecolor="none"))

    ax.text(bx + ai_w / 2, by + bh / 2, "AI 微短剧  12.2 万部 · 95.3%",
            fontsize=12.0, color="white", weight="bold", ha="center",
            va="center")
    ax.text(bx + bw, by + bh + 0.038, "真人 0.6 万部 · 4.7%", fontsize=9.0,
            color=SLATE, ha="right", va="center")
    ax.text(bx, by - 0.048,
            "合计约 12.8 万部｜AI 占比超过 95%（中国网络视听协会《微短剧创作指引》）",
            fontsize=8.8, color=GRAY, ha="left", va="center")

    ax.plot([0.028, 0.972], [0.560, 0.560], color=LIGHT, linewidth=0.9)

    # 下：春节档对照表
    ax.text(0.028, 0.512, "需求端：2026 年春节档，同一批观众的用脚投票", fontsize=10.0,
            color=DARK, weight="bold", ha="left", va="center")

    col1, col2, col3 = 0.028, 0.560, 0.780
    ax.text(col1, 0.432, "以较小的一方记为 1", fontsize=8.6, color=GRAY,
            ha="left", va="center")
    ax.text(col2, 0.432, "上线量", fontsize=9.4, color=SLATE, weight="bold",
            ha="center", va="center")
    ax.text(col3, 0.432, "总播放量", fontsize=9.4, color=SLATE, weight="bold",
            ha="center", va="center")

    ax.plot([0.028, 0.972], [0.392, 0.392], color=LIGHT, linewidth=0.9)

    ax.text(col1, 0.318, "AI 短剧", fontsize=10.6, color=DARK, weight="bold",
            ha="left", va="center")
    ax.text(col2, 0.318, "50", fontsize=15.0, color=NAVY, weight="bold",
            ha="center", va="center")
    ax.text(col3, 0.318, "1", fontsize=15.0, color=LIGHT, weight="bold",
            ha="center", va="center")

    ax.text(col1, 0.208, "真人短剧", fontsize=10.6, color=DARK, weight="bold",
            ha="left", va="center")
    ax.text(col2, 0.208, "1", fontsize=15.0, color=LIGHT, weight="bold",
            ha="center", va="center")
    ax.text(col3, 0.208, "25", fontsize=15.0, color=RED, weight="bold",
            ha="center", va="center")

    ax.plot([0.028, 0.972], [0.148, 0.148], color=LIGHT, linewidth=0.9)

    ax.text(0.028, 0.108,
            "供给少的那一方，播放量是另一方的 25 倍。产量和需求，在这条赛道上第一次分开走。",
            fontsize=9.4, color=SLATE, ha="left", va="center")

    punchline(fig, "95% 的是产能，25 倍的是需求，这是两件事。")
    footer(fig, "事实：中国网络视听协会 2026 年一季度《微短剧创作指引》"
                "（人民网 05-02、光明日报 05-02、上海市新闻办 05-02）｜"
                "真人 0.6 万部为 12.8 减 12.2 所得｜制图：本文")
    fig.savefig(OUT + "图2_95%的产量25倍的播放.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("一人加 AI，到底等于几个人",
               "同一个问题，三种口径｜数字后面跟着的是证据强度，不是情绪")
    ax = canvas(fig)

    rows = [
        ("1", "不用 AI 的一个人", "基准：这个实验里的对照组",
         "实验设定", GRAY, "white"),
        ("2", "一人 + AI ≈ 两人团队", "791 名 P&G 在职人员随机分组，"
         "AI 使用者的创新工作质量与不用 AI 的两人团队相当",
         "有出处", NAVY, NAVY),
        ("20", "一个人加 AI 干二十个人的活", "素材转述的网络流行说法；"
         "检索未找到任何研究、统计或企业披露支持这一倍数",
         "未找到出处", RED, "white"),
    ]

    y = 0.760
    for num, claim, note, badge, color, face in rows:
        ax.add_patch(FancyBboxPatch((0.028, y - 0.098), 0.944, 0.196,
                                    boxstyle="round,pad=0.006",
                                    facecolor="white", edgecolor=LIGHT,
                                    linewidth=1.0))
        ax.text(0.072, y + 0.010, num, fontsize=26.0, color=color,
                weight="bold", ha="center", va="center")
        ax.text(0.118, y + 0.028, "倍", fontsize=9.4, color=GRAY,
                ha="left", va="center")
        ax.text(0.170, y + 0.034, claim, fontsize=11.6, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(0.170, y - 0.040, note, fontsize=8.4, color=SLATE,
                ha="left", va="center")

        bx = 0.795
        ax.add_patch(FancyBboxPatch((bx, y - 0.030), 0.150, 0.060,
                                    boxstyle="round,pad=0.004",
                                    facecolor=face, edgecolor=color,
                                    linewidth=1.2))
        ax.text(bx + 0.075, y, badge, fontsize=9.0,
                color=("white" if face == NAVY else color),
                weight="bold", ha="center", va="center")
        y -= 0.250

    ax.text(0.028, 0.060,
            "同一项实验里还有一句更要紧的：人与 AI 组成的团队，产出卓越想法的比例显著高于纯人团队，也高于单人加 AI。",
            fontsize=9.0, color=SLATE, ha="left", va="center")

    punchline(fig, "把倍数喊大很容易，把出处写出来很难。")
    footer(fig, "事实：P&G 预注册田野实验（791 名在职人员）载于《Organization Science》"
                "2026-06-12，密歇根大学罗斯商学院 11-17 新闻稿转述｜"
                "「二十个人」一说本文检索未找到出处｜制图：本文")
    fig.savefig(OUT + "图3_一人加AI等于几个人.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)
