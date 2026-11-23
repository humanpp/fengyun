# -*- coding: utf-8 -*-
"""
《零 Token 费的账单：Linger 好用吗，边界在哪》配套图表

事实口径（核到 docs.heylinger.com 与官网）：
  · 桌面与浏览器：macOS / Windows 可接已登录 Chrome；Linux 仅 X11，不能接管已登录 Chrome；
    桌面与浏览器共用一个输入槽位，每次输入先记日志。
  · 硬件：Mac ≥16 GiB 统一内存；NVIDIA ≥8 GiB 显存 + 系统内存（参考 32 GiB）；
    跑 125B 需 12 GB 显存 + 64 GB 内存。
  · 首字：官方 12GB+32GB 规划档约 3 分钟；社区记录 128K 上下文约 144 秒。
  · 外部服务：语音 Soniox / xAI；连接器 Composio；记忆后台走 Codex 或 Claude Code 默认模型。
  · 安全：文档明确 "None of this is a sandbox"；TEAMHUB_PERMISSION_REVIEW 默认 false；
    Pi 运行时跳过检查；确认卡覆盖“别人看得见的写”。

输出目录 = 脚本所在目录
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei"]
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
Y_PUNCH = 0.068
Y_FOOT = 0.020


def header(fig, title, sub):
    fig.text(0.045, Y_TITLE, title, fontsize=19, color=DARK,
             weight="bold", ha="left", va="top")
    fig.text(0.045, Y_SUB, sub, fontsize=10.4, color=GRAY,
             ha="left", va="top")


def footer(fig, text):
    fig.text(0.045, Y_FOOT, text, fontsize=7.6, color=GRAY,
             ha="left", va="bottom")


def punchline(fig, text):
    fig.text(0.045, Y_PUNCH, text, fontsize=10.4, color=DARK,
             ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.7", facecolor=PALE,
                       edgecolor=LIGHT, linewidth=0.9))


def card(ax, x, y, w, h, edge, face="white", lw=1.2, z=2):
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
    """一句话 → Agent 团队 → 你的电脑 → 结果"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "一句话，怎么变成一次操作",
           "你在 Room 里说一句，剩下的在你自己电脑上完成")

    steps = [
        ("01", "你派活", "复杂任务丢进 Room\n不用拆步骤", NAVY),
        ("02", "Another Me 组队", "拉起不同职能的 Agent\n你只看一个对话框", TEAL),
        ("03", "用你的电脑", "已登录的 Chrome、桌面 App\nshell 与文件", SLATE),
        ("04", "结果回来", "草稿、待办、会议纪要\n回到同一个会话", RED),
    ]
    w, gap = 0.208, 0.028
    x = 0.045
    for tag, name, note, color in steps:
        card(ax, x, 0.400, w, 0.285, color, lw=1.5)
        ax.text(x + 0.020, 0.628, tag, fontsize=10.0, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(x + 0.020, 0.570, name, fontsize=12.0, color=DARK,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(x + 0.020, 0.500, note, fontsize=8.8, color=SLATE,
                ha="left", va="top", linespacing=1.8, zorder=6)
        x += w + gap

    for i in range(3):
        xa = 0.045 + i * (w + gap) + w + 0.004
        ax.add_patch(FancyArrowPatch(
            (xa, 0.542), (xa + gap - 0.008, 0.542),
            arrowstyle="-|>", mutation_scale=15, color=GRAY, lw=1.4))

    ax.text(0.045, 0.330,
            "macOS 与 Windows 能接已登录的 Chrome；Linux 只支持 X11 桌面，也接不了已登录的 Chrome。",
            fontsize=9.2, color=GRAY, ha="left", va="center")
    ax.text(0.045, 0.280,
            "桌面与浏览器共用一个输入槽位：两个 Agent 不会抢鼠标，每次输入先记日志再执行。",
            fontsize=9.2, color=GRAY, ha="left", va="center")

    punchline(fig, "它不是聊天窗口，是一个工作台。")
    footer(fig, "事实来源：docs.heylinger.com（How Linger works、Desktop and browser、Rooms）")
    fig.savefig(OUT + "图1_一句话变动作.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 2
def fig2():
    """四笔账"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "Token 是 0，账单不是",
           "四笔钱，官方文档里都写着")

    items = [
        ("硬件", "16 GiB 起", "Mac 统一内存；NVIDIA 8 GiB 显存起，\n官方参考配置 32 GiB 内存", NAVY),
        ("等 待", "约 3 分钟", "12GB+32GB 规划档的首字延迟；\n128K 上下文的社区记录约 144 秒", RED),
        ("外部服务", "按次计费", "语音 Soniox / xAI；Gmail、Slack 走\nComposio 中转；记忆后台走云端模型", SLATE),
        ("托管版", "价格未公布", "开源自托管免费；对外托管要商业授权，\n官方计划推出托管服务", TEAL),
    ]
    pos = [(0.045, 0.555), (0.515, 0.555), (0.045, 0.320), (0.515, 0.320)]
    for (x, y), (label, value, note, color) in zip(pos, items):
        card(ax, x, y, 0.440, 0.205, color, lw=1.4)
        ax.text(x + 0.022, y + 0.155, label, fontsize=9.0, color=GRAY,
                ha="left", va="center", zorder=6)
        ax.text(x + 0.022, y + 0.103, value, fontsize=14.0, color=color,
                weight="bold", ha="left", va="center", zorder=6)
        ax.text(x + 0.022, y + 0.052, note, fontsize=8.6, color=DARK,
                ha="left", va="center", linespacing=1.5, zorder=6)

    ax.text(0.045, 0.248,
            "本地推理不产生 API 账单，但显卡、内存、电费、等待和外部服务都得自己付。",
            fontsize=9.2, color=GRAY, ha="left", va="center")

    punchline(fig, "省下的是 Token 费，不是总成本。")
    footer(fig, "事实来源：docs.heylinger.com（Hardware compatibility、Meetings、How Linger works）；36氪 2026-11-21")
    fig.savefig(OUT + "图2_账单.png", dpi=170)
    plt.close(fig)


# ---------------------------------------------------------------- 图 3
def fig3():
    """权限链与两个缺口"""
    fig = plt.figure(figsize=(12, 6.9))
    ax = new_axes(fig)

    header(fig, "护栏不是沙箱",
           "官方文档：这些都不是沙箱；复核默认关闭")

    card(ax, 0.045, 0.560, 0.250, 0.180, NAVY, lw=1.5)
    ax.text(0.067, 0.690, "你的账号权限", fontsize=11.4, color=NAVY,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.067, 0.612, "文件 · 已登录应用 · shell", fontsize=8.8,
            color=SLATE, ha="left", va="center", zorder=6)

    card(ax, 0.375, 0.560, 0.250, 0.180, SLATE, lw=1.5)
    ax.text(0.397, 0.690, "Guardrail", fontsize=11.4, color=SLATE,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.397, 0.612, "规则 → 可选的模型复核", fontsize=8.8,
            color=SLATE, ha="left", va="center", zorder=6)

    card(ax, 0.705, 0.560, 0.250, 0.180, RED, lw=1.5)
    ax.text(0.727, 0.690, "动作", fontsize=11.4, color=RED,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.727, 0.612, "发信 · 跑命令 · 点击输入", fontsize=8.8,
            color=SLATE, ha="left", va="center", zorder=6)

    for x0 in (0.300, 0.630):
        ax.add_patch(FancyArrowPatch(
            (x0, 0.650), (x0 + 0.066, 0.650),
            arrowstyle="-|>", mutation_scale=15, color=GRAY, lw=1.4))

    card(ax, 0.045, 0.300, 0.440, 0.205, RED, lw=1.5)
    ax.text(0.067, 0.462, "缺口一：复核默认关闭", fontsize=11.0, color=RED,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.067, 0.400,
            "TEAMHUB_PERMISSION_REVIEW 默认 false。\n"
            "没开之前，开放式动作带你账号的完整权限执行。",
            fontsize=8.8, color=DARK, ha="left", va="top",
            linespacing=1.7, zorder=6)

    card(ax, 0.515, 0.300, 0.440, 0.205, RED, lw=1.5)
    ax.text(0.537, 0.462, "缺口二：Pi 跳过检查", fontsize=11.0, color=RED,
            weight="bold", ha="left", va="center", zorder=6)
    ax.text(0.537, 0.400,
            "Pi 运行时上的 Agent，即使开了复核，\n"
            "也会跳过 Computer 的权限检查。",
            fontsize=8.8, color=DARK, ha="left", va="top",
            linespacing=1.7, zorder=6)

    ax.text(0.045, 0.245,
            "确认卡（confirmation card）只覆盖“别人看得见的写”：发邮件、发 Slack、改 Notion 永远要你点同意。",
            fontsize=9.0, color=GRAY, ha="left", va="center")

    punchline(fig, "确认卡管得住写信，管不住跑命令。")
    footer(fig, "事实来源：docs.heylinger.com（Approvals and permission review、Desktop and browser）")
    fig.savefig(OUT + "图3_权限缺口.png", dpi=170)
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", OUT)
