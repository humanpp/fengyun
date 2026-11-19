# -*- coding: utf-8 -*-
"""
《美国新规封堵海外数据中心远程用芯片》配套图表
事实口径（2026-11-19，逐条核对公开报道后）：
  · 2026 年 11 月 16 日（周一），美国商务部工业与安全局（BIS）发布临时最终规则
    （IFR），编号 RIN 0694-AK50，标题《解决先进半导体远程访问问题》，
    由财政部与国家安全委员会指导制定（BIS 新闻稿、TechCrunch 11-16）；
  · 门槛：数据中心或任何可提供超过 1200 万 TPP 算力的网络 ≈ 750 张 H100/H200
    （TechCrunch 11-16；摩根士丹利记 700—800 张）；
  · 对象：总部或最终母公司位于 D:5 国家（含中国、俄罗斯、伊朗、朝鲜等）的企业；
    覆盖经中间商、经纪的间接访问；出口商与机房运营方须核查客户股权结构；
  · 五国名单：印尼、马来西亚、新加坡、泰国、巴西，出口/再出口/境内转移先进芯片
    及服务器须许可；输往美国总部企业不适用（TechCrunch、BBC 中文）；
  · 存量业务：规则生效后 90 天内须取得许可；
  · 豁免：商业推荐系统（电商推荐、社交流），接入生成式即失效；
  · 同时废除 2025 年 1 月的《AI 扩散规则》；
  · 联邦公报文件号 2026-23529，定于 2026 年 11 月 19 日刊登、当日生效（虎嗅 11-17）；
  · 中国商务部 11 月 17 日回应：强烈不满、坚决反对（联合早报）；
  · Bernstein：新规封堵此前最重要的漏洞，管制重心从限制芯片出货转向限制算力能力
    本身；利空中国大模型公司与云厂商，利好本土半导体产业链关键公司（信报引述）；
  · 摩根士丹利：对中国互联网 AI 产业偏负面；商业推荐系统豁免；
  · 马来西亚：117 个数据中心项目须遵守新规（云头条 11-19）；
  · 加州政府运营局 11 月 18 日发布 85 页报告《AI Safety in 2026 and Beyond》，
    建议强制前沿模型安全标准、持牌第三方验证、紧急关停权，属建议非法律。
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
    fig = base("管制的抓手，换了三次",
               "从“芯片运到哪里”，到“算力给谁用”——每一次都是给上一层的绕法打补丁")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    rows = [
        ("2022—2024　管“芯片运往哪里”", NAVY,
         "抓手是实体清单与算力阈值，看的是货物流向。",
         "于是有人这样绕：经第三国转口、经中间商代购，卡不进中国，人也不必去。", DARK),
        ("2025　管“各国能有多少算力”", SLATE,
         "《AI 扩散规则》按国家分层配额，看的是算力落在哪一国。",
         "于是有人这样绕：只租不买——卡留在海外机房，网线拉过去就行。", DARK),
        ("2026 年 11 月 16 日　管“算力被谁使用”", RED,
         "1200 万 TPP 以上、服务 D:5 国家总部企业，卖卡卖服务器即须许可。",
         "这一层，今天没有现成的绕法。", RED),
    ]

    yy = 0.845
    for head, color, can, cannot, endcolor in rows:
        ax.add_patch(Rectangle((0.030, yy - 0.168), 0.006, 0.196,
                               facecolor=color, edgecolor="none"))
        ax.text(0.056, yy, head, fontsize=11.2, color=DARK, weight="bold",
                ha="left", va="center")
        ax.text(0.056, yy - 0.058, can, fontsize=8.9, color=GRAY, ha="left",
                va="center")
        ax.text(0.056, yy - 0.110, cannot, fontsize=9.4, color=endcolor,
                ha="left", va="center")
        ax.plot([0.046, 0.960], [yy - 0.158, yy - 0.158], color=LIGHT,
                linewidth=0.8)
        yy -= 0.205

    punchline(fig, "前两次管的是东西在哪，这一次管的是谁在用。")
    footer(fig, "事实：BIS 临时最终规则（RIN 0694-AK50）2026-11-16 发布；"
                "2025 年《AI 扩散规则》被同一份文件废止｜绕法为作者归纳｜制图：本文")
    fig.savefig(OUT + "图1_抓手换了三次.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("四道口子，卡的是同一件事",
               "1200 万 TPP 门槛｜五国名单｜90 天过渡｜穿透式核查")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    cards = [
        (0.030, 0.520, "① 门槛", "1200 万 TPP",
         "约合 750 张 H100 / H200 的算力，\n摩根士丹利记为 700—800 张。"),
        (0.515, 0.520, "② 名单", "五个国家",
         "印尼、马来西亚、新加坡、泰国、巴西，\n出口、再出口、境内转移均须许可。"),
        (0.030, 0.190, "③ 存量", "90 天",
         "已在服务中国客户的机房，须在生效后\n90 天内取得许可，否则停供。"),
        (0.515, 0.190, "④ 穿透", "查到最终母公司",
         "中间商、经纪的间接访问一并覆盖；\n出口商与机房有主动核查义务。"),
    ]

    for x, y, tag, big, body in cards:
        ax.add_patch(FancyBboxPatch((x, y), 0.455, 0.285,
                                    boxstyle="round,pad=0.008",
                                    facecolor="white", edgecolor=LIGHT,
                                    linewidth=1.0))
        ax.text(x + 0.028, y + 0.232, tag, fontsize=9.0, color=GRAY,
                ha="left", va="center")
        ax.text(x + 0.028, y + 0.172, big, fontsize=17.0, color=NAVY,
                weight="bold", ha="left", va="center")
        ax.plot([x + 0.028, x + 0.427], [y + 0.132, y + 0.132], color=LIGHT,
                lw=0.8)
        ax.text(x + 0.028, y + 0.070, body, fontsize=8.8, color=SLATE,
                ha="left", va="center", linespacing=1.8)

    ax.text(0.030, 0.098,
            "另：商业推荐系统（电商推荐、社交流）可豁免，但一旦接入生成式模型即失效；"
            "同时废止 2025 年 1 月的《AI 扩散规则》。",
            fontsize=8.8, color=SLATE, ha="left", va="center")

    punchline(fig, "四道口子对着同一件事：不是卡在哪，是谁在用。")
    footer(fig, "事实：门槛与五国名单据 TechCrunch 11-16、BBC 中文 11-17；"
                "90 天与穿透式核查据 TechCrunch、Gibson Dunn 11-19｜制图：本文")
    fig.savefig(OUT + "图2_四道口子.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("从抢跑，到 90 天",
               "规则 11 月 19 日刊登当日生效，真正的截止日在三个月后")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    items = [
        ("11 月 12 日", "抢跑", "路透：中国 AI 公司加快锁定海外算力，\n担心管制落地", NAVY),
        ("11 月 16 日", "发布", "BIS 临时最终规则，编号 RIN 0694-AK50", NAVY),
        ("11 月 17 日", "回应", "中国商务部：强烈不满、坚决反对", NAVY),
        ("11 月 18 日", "另一份文件", "加州政府运营局发布 AI 安全报告", SLATE),
        ("11 月 19 日", "生效", "联邦公报刊登，当日生效", RED),
        ("此后 90 天", "截止日", "存量数据中心须持证，否则停供", RED),
    ]

    ax.plot([0.150, 0.150], [0.150, 0.850], color=LIGHT, linewidth=1.4)

    yy = 0.820
    for time, head, body, color in items:
        ax.plot([0.150], [yy], marker="o", markersize=7.0, color=color, zorder=3)
        ax.text(0.070, yy, time, fontsize=9.4, color=GRAY, weight="bold",
                ha="right", va="center")
        ax.text(0.195, yy, head, fontsize=10.6, color=DARK, weight="bold",
                ha="left", va="center")
        ax.text(0.400, yy, body, fontsize=9.0, color=SLATE, ha="left",
                va="center", linespacing=1.8)
        yy -= 0.134

    punchline(fig, "发布只用了三天，执行要等九十天——这段时间才是各方腾挪的窗口。")
    footer(fig, "事实：时间线据路透 11-12（经 TechCrunch 转述）、BIS 11-16、"
                "中国商务部 11-17、加州政府运营局 11-18、虎嗅 11-17 关于联邦公报刊登与生效的记述｜制图：本文")
    fig.savefig(OUT + "图3_从抢跑到90天.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)
