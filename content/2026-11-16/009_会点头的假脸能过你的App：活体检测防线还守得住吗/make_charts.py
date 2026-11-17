# -*- coding: utf-8 -*-
"""
《会点头的假脸，已经能过你的 App》配套图表
事实来源：杭州市中级人民法院典型案例，央广网/中国之声 2026-11-14/15 报道；
东盟《数字经济框架协定》（DEFA）2026-11-14 马尼拉签署
风格：克制传媒风，白底、低饱和配色、标题即结论
输出目录 = 脚本所在目录
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch, Circle

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["figure.facecolor"] = "white"
plt.rcParams["axes.facecolor"] = "white"

NAVY = "#1f3a5f"
RED = "#b5544a"
GRAY = "#8a8f98"
LIGHT = "#d8dbe0"
DARK = "#2b2f36"
PALE = "#eef0f3"
SAND = "#b9a887"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep


def canvas(fig):
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    return ax


def footer(fig, text):
    fig.text(0.045, 0.035, text, fontsize=8.4, color=GRAY, ha="left", va="bottom")


def takeaway(fig, y, text, size=10.4):
    fig.text(0.045, y, text, fontsize=size, color=DARK, ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


def head(fig, title, sub):
    fig.text(0.045, 0.935, title, fontsize=19, color=DARK, ha="left",
             va="center", weight="bold")
    fig.text(0.045, 0.868, sub, fontsize=10.8, color=GRAY, ha="left", va="center")


# ---------------------------------------------------------------- 图 1
def fig1():
    fig = plt.figure(figsize=(12, 6.8))
    ax = canvas(fig)
    head(fig, "假脸是怎么进来的",
         "杭州中院案例里的四步；前三步都发生在用户手里那台手机上")

    steps = [
        ("01", "拿到素材", ["手机号、头像照片、", "身份信息"], "账号风控与信息最小化"),
        ("02", "生成动作", ["AI 换脸，按指令", "点头、眨眼、摇头"], "合成内容的标识与水印"),
        ("03", "替换镜头", ["虚拟相机接管摄像头", "平台打开的是播放器"], "终端设备完整性检测"),
        ("04", "通过认证", ["登录、改绑手机号", "替人做虚假实名"], "多因子验证与人工复核"),
    ]
    w, h, yb = 0.200, 0.280, 0.430
    xs = [0.055, 0.285, 0.515, 0.745]
    for (num, title, lines, guard), x in zip(steps, xs):
        ax.add_patch(Rectangle((x, yb), w, h, facecolor="#fafafb",
                               edgecolor=LIGHT, linewidth=1.0))
        ax.add_patch(Rectangle((x, yb + h - 0.012), w, 0.012, facecolor=NAVY,
                               edgecolor="none"))
        ax.text(x + 0.014, yb + h - 0.042, num, fontsize=9, color=GRAY,
                va="center")
        ax.text(x + 0.014, yb + h - 0.088, title, fontsize=13.5, color=NAVY,
                weight="bold", va="center")
        for i, ln in enumerate(lines):
            ax.text(x + 0.014, yb + h - 0.140 - i * 0.042, ln, fontsize=9.4,
                    color=DARK, va="center")
        ax.plot([x + 0.014, x + w - 0.014], [yb + 0.076, yb + 0.076],
                color=LIGHT, lw=1.0)
        ax.text(x + 0.014, yb + 0.038, "该守的一环", fontsize=8.6, color=GRAY,
                va="center")
        ax.text(x + 0.014, yb + 0.010, guard, fontsize=8.8, color=RED,
                va="center", weight="bold")

    for i in range(3):
        ax.add_patch(FancyArrowPatch((xs[i] + w + 0.006, yb + h / 2),
                                     (xs[i + 1] - 0.006, yb + h / 2),
                                     arrowstyle="-|>", mutation_scale=13,
                                     color=GRAY, lw=1.2))

    ax.add_patch(Rectangle((0.055, 0.300), 0.890, 0.075, facecolor="#f7f4ef",
                           edgecolor=LIGHT, linewidth=1.0))
    ax.text(0.075, 0.337, "真正被打掉的前提：采集端可信。",
            fontsize=10.2, color=DARK, weight="bold", va="center")
    ax.text(0.400, 0.337,
            "App 以为自己用了摄像头，其实播放的是一段合成视频——后面所有算法都在对视频做判断。",
            fontsize=9.4, color=GRAY, va="center")

    takeaway(fig, 0.150, "绕过密码只是表象：被攻破的是“证明你是你”这道流程。")
    footer(fig, "据杭州市中级人民法院典型案例及央广网、中国之声 2026-11-14/15 报道整理；“该守的一环”为本文归纳。")
    fig.savefig(OUT + "图1_假脸怎么进来的.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    fig = plt.figure(figsize=(12, 6.8))
    ax = canvas(fig)
    head(fig, "四层防线，最薄的一层在采集端",
         "动作挑战失效之后，压力从算法端移到设备端与流程端")

    headers = [(0.085, "防线"), (0.205, "现状"), (0.330, "问题出在哪"),
               (0.660, "该补什么")]
    for x, t in headers:
        ax.text(x, 0.800, t, fontsize=9.6, color=GRAY, va="center")

    rows = [
        ("采集端", "最薄", RED, "虚拟相机、投屏、模拟器都能冒充真摄像头",
         "设备完整性、摄像头链路校验"),
        ("校验端", "参差", SAND, "大机构看得出噪声与深度，中小 App 只看动作",
         "多模态反伪造 + 环境信息"),
        ("流程端", "缺口", RED, "人脸一通过，改绑、改密、转账就一路放行",
         "高风险动作叠加二次验证"),
        ("合规端", "待落地", SAND, "“不得作为唯一验证方式”需要真能用的替代通道",
         "人工复核、线下核身"),
    ]
    for i, (name, tag, color, problem, fix) in enumerate(rows):
        y = 0.700 - i * 0.135
        ax.add_patch(Rectangle((0.055, y - 0.055), 0.890, 0.110,
                               facecolor=PALE if i % 2 == 0 else "#f8f8f9",
                               edgecolor=LIGHT, linewidth=1.0))
        ax.text(0.085, y, name, fontsize=12.5, color=NAVY, weight="bold",
                va="center")
        ax.add_patch(Rectangle((0.205, y - 0.024), 0.070, 0.048,
                               facecolor="white", edgecolor=color, linewidth=1.1))
        ax.text(0.240, y, tag, fontsize=8.6, color=color, ha="center",
                va="center", weight="bold")
        ax.text(0.330, y, problem, fontsize=9.4, color=DARK, va="center")
        ax.text(0.660, y, fix, fontsize=9.4, color=GRAY, va="center")

    takeaway(fig, 0.150, "人脸只是钥匙串上的第一把钥匙，不该是唯一的一把。")
    footer(fig, "据央广网、中国之声报道与公开的银行远程核验说明整理；分层与“现状”评级为本文归纳。")
    fig.savefig(OUT + "图2_四层防线.png", dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    fig = plt.figure(figsize=(12, 6.8))
    head(fig, "风险越高，越不能只凭一张脸",
         "横轴是场景风险，纵轴是验证强度；点的位置为定性示意，非统计数据")

    ax = fig.add_axes([0.105, 0.245, 0.510, 0.480])
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 2)
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ("top", "right", "left", "bottom"):
        ax.spines[s].set_color(LIGHT)

    quads = [
        ((0, 0), "#f4f5f4", "低风险 · 弱验证", GRAY, 0.10),
        ((1, 0), "#f8e9e6", "高风险 · 弱验证", RED, 0.10),
        ((0, 1), "#eef2f7", "低风险 · 强验证", NAVY, 0.86),
        ((1, 1), "#f6f2e9", "高风险 · 强验证", SAND, 0.86),
    ]
    for (x, y), fill, label, color, dy in quads:
        ax.add_patch(Rectangle((x, y), 1, 1, facecolor=fill, edgecolor="white",
                               linewidth=2.0))
        ax.text(x + 0.055, y + dy, label, fontsize=9.0, color=color,
                va="center", weight="bold")

    ax.set_xlabel("场景风险：查余额 → 改绑 → 转账", fontsize=9.6, color=GRAY)
    ax.set_ylabel("验证强度", fontsize=9.6, color=GRAY)

    points = [
        ("只用一张脸", 1.62, 0.46, RED, -0.17, "center"),
        ("人脸 + 短信验证码", 1.55, 1.20, SAND, 0.16, "center"),
        ("人脸 + 硬件 / 人工复核", 0.62, 1.50, NAVY, 0.16, "center"),
    ]
    for name, x, y, color, dy, ha in points:
        ax.add_patch(Circle((x, y), 0.042, facecolor=color, edgecolor="white",
                            linewidth=1.6, zorder=5))
        ax.text(x, y + dy, name, fontsize=9.4, color=color, ha=ha,
                va="center", weight="bold", zorder=6)

    ax.add_patch(FancyArrowPatch((1.52, 0.58), (0.72, 1.38), arrowstyle="-|>",
                                 mutation_scale=14, color=DARK, lw=1.2,
                                 linestyle=(0, (4, 3)), zorder=3))
    ax.plot([0.09, 0.21], [0.44, 0.44], color=DARK, lw=1.2,
            linestyle=(0, (4, 3)))
    ax.text(0.25, 0.44, "个人可移动的方向", fontsize=8.8, color=DARK,
            va="center")

    # 右栏：具体动作
    fig.text(0.640, 0.780, "把脸降级，四件事", fontsize=12.5, color=DARK,
             weight="bold", va="center")
    items = [
        ("关掉非必要的人脸支付、免密支付", "大额交易加二次验证"),
        ("少放正脸素材", "多角度自拍、手持证件照、露脸视频"),
        ("盯账户异动", "改绑、异地登录、授信查询、收货地址"),
        ("中招后的顺序", "冻结改密 → 报警 → 录屏留证"),
    ]
    for i, (t, n) in enumerate(items):
        y = 0.700 - i * 0.135
        ax2 = fig.add_axes([0, 0, 1, 1])
        ax2.set_xlim(0, 1)
        ax2.set_ylim(0, 1)
        ax2.axis("off")
        ax2.add_patch(Rectangle((0.640, y - 0.050), 0.310, 0.100,
                                facecolor="#fafafb", edgecolor=LIGHT,
                                linewidth=1.0))
        ax2.text(0.660, y + 0.014, t, fontsize=9.8, color=DARK, va="center",
                 weight="bold")
        ax2.text(0.660, y - 0.026, n, fontsize=8.8, color=GRAY, va="center")

    takeaway(fig, 0.108, "多因素认证是最便宜的一道补丁：拿到脸之后，还得再拿到一样东西。")
    footer(fig, "象限与点位为本文据场景风险与验证强度所作的定性示意；建议部分据报道中专家的公开表述与通用安全实践整理。")
    fig.savefig(OUT + "图3_验证强度矩阵.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")
