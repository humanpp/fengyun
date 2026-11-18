# -*- coding: utf-8 -*-
"""
《Qwen4-Max 开了 API，Qwen4 的开源权重还没来》配套图表
事实口径（均已核对原始来源）：
  · 2026-08-03 阿里发布 Qwen3.8-Max（2.4T 总参 / 95B 激活，1M 上下文，
    Text Arena 第 5、Vision Arena 第 2）。官方博客明确："这是 Qwen-Max 级模型
    首次开源权重，开放权重将于下周发布。"
  · 2026-08-12/13 权重实际开源，仓库 Qwen/Qwen3.8-2.4T-A95B，BF16 与 FP8 两版，
    约 4.89TB，许可为自定义的 Qwen3.8-Max License（带年收入门槛）。
  · Qwen3.8-27B 走 Apache 2.0；Qwen3.8-Flash-Next 走 qwen-community-1.0。
  · 2026-08-26 开源 Qwen3.8-Flash-Next，官方模型卡称其为 "an experimental
    preview of the architecture that will underpin Qwen4"（Qwen4 架构的预览版）。
    规格：125B 主干 + 51B n-gram embedding + 4B MTP ≈ 180B 落盘，每 token 激活约 6B。
  · 2026-09-22 云栖大会，阿里云通义千问负责人刘大一恒公布：Qwen4 采用全新架构、
    已在训练中；Qwen4.5、Qwen5 规划扩展至 5–10 万亿参数；未给任何发布日期。
  · 2026-11-11 10:00 起 Qwen4-Max 预览开放（模型 ID qwen4-max-preview），
    仅通过 Token Plan，至 11-25 24:00（UTC+8）结束。
  · 2026-11-16 Qwen4-Max 正式版上线，可通过 API（QwenCloud）与 Token Plan 调用，
    也可在 Qwen Studio、QwenWork、Qoder 使用。稀疏 MoE，总参 2.4 万亿，
    每 token 激活约 710 亿（官方标注，较 Qwen3.8-Max 的 95B 少约 25%；
    部分中文报道写 950 亿，与"减少 25%"不自洽，本文采用 710 亿口径），
    100 万 token 上下文，原生支持文本/图片/视频输入、文本输出。
    国内 API 输入由 12 元降至 10 元／百万 token，输出由 36 元降至 30 元，降约 17%；
    国际版输入 1.50 美元、输出 4.50 美元／百万 token，缓存输入 0.075 美元。
    兼容 OpenAI Chat Completions / Responses 与 Anthropic Messages API。
  · 该次发布不开放权重。官方仅称"Qwen4 系列中规模更小的开放权重模型将很快
    面向全球开发者发布"，未给规模、许可证与时间表。
  · 2026-11-16 同日，开源量化团队 Unsloth AI 预告更小的 Qwen4 模型即将发布，
    Qwen4-27B 可在 16GB 内存配置运行，GGUF 将采用 Unsloth Dynamic 3.1。
  · 官方自建 Work360 基准（覆盖 721 个专业领域）Qwen4-Max 得 52.69，
    Qwen3.8-Max 为 47.74。官方 16 项基准对比中，对 Claude Opus 5.5 为 6 胜 10 负；
    Terminal-Bench 4.0 得 48.5，低于 Kimi K3.1 的 67.2；ProgramBench 得 31.5，
    Opus 5.5 为 65。成本降幅口径不一（官方约 60%、企业版 58%、MetaEra 62%）。
    以上据阿里巴巴云官方博客、IT之家、WelclAI（2026-11-17）、Crypto Briefing、
    SiliconANGLE、MetaEra、Hugging Face 模型卡、tbreak 等公开材料。
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
GREEN = "#4f6b58"

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
    fig = base("三个月里，开源的承诺被兑现了一次，然后被收回",
               "2026 年 8 月至 11 月，阿里在权重这件事上的六个动作")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    events = [
        ("08/03", "Qwen3.8-Max 发布", "官方：Max 级首次开源权重，下周发布", GREEN),
        ("08/12", "权重真的开了", "Qwen3.8-2.4T-A95B，BF16／FP8 约 4.89TB", GREEN),
        ("08/26", "架构预览版开源", "Qwen3.8-Flash-Next，官方称 Qwen4 架构预览", GREEN),
        ("09/22", "Qwen4 官宣在训练", "云栖大会，无模型卡、无权重、无日期", NAVY),
        ("11/11", "Qwen4-Max 预览", "仅 Token Plan，至 11-25 结束", NAVY),
        ("11/16", "正式版 API 上线", "不开放权重；「更小的很快开源」，无型号与日期", RED),
    ]

    ax.plot([0.148, 0.148], [0.130, 0.930], color=LIGHT, linewidth=1.4)

    ys = [0.885, 0.730, 0.575, 0.420, 0.265, 0.118]
    for (date, head, body, color), yy in zip(events, ys):
        ax.plot([0.148], [yy], marker="o", markersize=7, color=color,
                zorder=4, clip_on=False)
        ax.text(0.126, yy, date, fontsize=9.4, color=color, weight="bold",
                ha="right", va="center")
        ax.text(0.183, yy + 0.032, head, fontsize=11.0, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(0.183, yy - 0.040, body, fontsize=8.7, color=SLATE,
                ha="left", va="center")

    ax.add_patch(FancyBboxPatch((0.640, 0.700), 0.315, 0.230,
                                boxstyle="round,pad=0.014", facecolor=SAND,
                                edgecolor="#d9cdb6", linewidth=1.0, zorder=2))
    ax.text(0.662, 0.898, "开源阵营真正想要的许可", fontsize=9.2, color="#7a6746",
            ha="left", va="center", zorder=3)
    ax.text(0.662, 0.855, "是 Apache 2.0。", fontsize=10.4, color="#7a6746",
            weight="bold", ha="left", va="center", zorder=3)
    ax.text(0.662, 0.775, "Max 级开源用的是自定义许可，\n带年收入门槛。", fontsize=8.6,
            color="#7a6746", ha="left", va="center", linespacing=1.7, zorder=3)

    punchline(fig, "上一代是「下周就给」，这一代是「以后会给」。")
    footer(fig, "依据：阿里云官方博客（2026-08-03）、Hugging Face 模型卡、IT之家（2026-11-16）、WelclAI（2026-11-17）｜制图：本文")
    fig.savefig(OUT + "图1_三个月里的开源与闭源.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 2
def fig2():
    fig = base("「开源」不是一个开关，是一个梯度",
               "同一家公司的四个档位，四套不同的许可")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    rows = [
        ("Qwen3.8-27B", "Apache 2.0", "最宽松，商用几乎无门槛", 0.90, GREEN),
        ("Qwen3.8-Flash-Next", "qwen-community-1.0", "社区许可，附加限制条款", 0.68, GREEN),
        ("Qwen3.8-Max（2.4T）", "Qwen3.8-Max License", "自定义许可，带年收入门槛", 0.46, NAVY),
        ("Qwen4-Max", "无权重", "只有 API，拿不到模型文件", 0.22, RED),
    ]

    base_x, max_w = 0.430, 0.400
    yy = 0.780
    for name, lic, note, ratio, color in rows:
        ax.text(0.045, yy + 0.012, name, fontsize=10.2, color=DARK,
                weight="bold", ha="left", va="center")
        ax.text(0.045, yy - 0.036, lic, fontsize=8.8, color=color, ha="left",
                va="center")
        ax.add_patch(Rectangle((base_x, yy - 0.032), max_w, 0.064,
                               facecolor=PALE, edgecolor="none", zorder=2))
        ax.add_patch(Rectangle((base_x, yy - 0.032), max_w * ratio, 0.064,
                               facecolor=color, edgecolor="none", zorder=3))
        ax.text(base_x + max_w + 0.018, yy, note, fontsize=8.8, color=SLATE,
                ha="left", va="center")
        yy -= 0.190

    ax.plot([base_x, base_x], [0.140, 0.845], color=LIGHT, linewidth=1.0)
    ax.text(base_x, 0.862, "开放程度 →", fontsize=8.4, color=GRAY, ha="left",
            va="center")

    punchline(fig, "旗舰从来没给过最宽松的那一档，这次连最严的那一档也没了。")
    footer(fig, "依据：Hugging Face 模型卡与许可原文、阿里云官方博客、WelclAI（2026-11-17）｜制图：本文")
    fig.savefig(OUT + "图2_开源是个梯度.png", dpi=150, facecolor="white")
    plt.close(fig)


# ------------------------------------------------------------------ 图 3
def fig3():
    fig = base("现在想用 Qwen4，只有这四种拿法",
               "一条能用，一条限时，一条是旧架构，一条要等")
    ax = fig.add_axes([0.045, 0.135, 0.915, 0.700])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    cells = [
        (0.045, 0.545, "① 调 API", "能用", GREEN,
         "QwenCloud／百炼，按 token 计费\n输入 10 元、输出 30 元每百万\n权重拿不到"),
        (0.515, 0.545, "② 限时预览", "进行中，25 日止", GRAY,
         "11 月 11 日至 25 日 24 时\n仅 Token Plan 订阅用户\n到期后只能改走 API"),
        (0.045, 0.180, "③ 本地跑旧架构", "能跑，但不是 Qwen4", NAVY,
         "Qwen3.8-Flash-Next，8 月 26 日开源\n官方称其为 Qwen4 架构预览\n每 token 激活约 6B"),
        (0.515, 0.180, "④ 等开源", "无型号、无许可、无日期", RED,
         "官方只说「更小的很快发布」\nUnsloth 预告 27B 可跑 16GB\n但没有官方时间表"),
    ]

    for x, y, title, tag, color, body in cells:
        ax.add_patch(Rectangle((x, y), 0.440, 0.345, facecolor="white",
                               edgecolor=color, linewidth=1.1, zorder=2))
        ax.text(x + 0.022, y + 0.292, title, fontsize=11.4, color=DARK,
                weight="bold", ha="left", va="center", zorder=3)
        ax.add_patch(FancyBboxPatch((x + 0.022, y + 0.208), 0.230, 0.056,
                                    boxstyle="round,pad=0.008",
                                    facecolor=PALE, edgecolor="none", zorder=3))
        ax.text(x + 0.137, y + 0.236, tag, fontsize=8.6, color=color,
                weight="bold", ha="center", va="center", zorder=4)
        ax.plot([x + 0.022, x + 0.418], [y + 0.176, y + 0.176], color=LIGHT,
                linewidth=0.9, zorder=3)
        ax.text(x + 0.022, y + 0.100, body, fontsize=8.6, color=SLATE,
                ha="left", va="center", linespacing=1.85, zorder=3)

    punchline(fig, "架构 8 月就给了，权重到今天还没给。差的不是技术。")
    footer(fig, "依据：百炼与 QwenCloud 文档、Qwen 官方模型卡、Unsloth AI 预告（2026-11-16）｜制图：本文")
    fig.savefig(OUT + "图3_现在只有四种拿法.png", dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done:", OUT)
