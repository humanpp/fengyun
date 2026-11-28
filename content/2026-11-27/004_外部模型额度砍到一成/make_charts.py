# -*- coding: utf-8 -*-
"""
《一家大厂把外部 AI 额度砍到 10%》配套图表

事实口径（网传通知，未经官方确认）：
  · 2026-11-26「大厂日爆」披露据称腾讯内部通知。
  · 2026-12-01 起非技术岗试点：外部模型默认额度 = 总额度 10%；
    按 700 元默认总额度计，外部 70 元、混元 HY4 630 元。
  · 子公司非技术岗外部模型默认额度为零，额外需求可申请。
  · 2027-01-01 起原则上默认使用混元，调用外部模型须申请额度。
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "_kit")))

from chart_kit import (NAVY, RED, GRAY, SLATE, LIGHT, DARK, PALE, TEAL,
                       page, save, card, vbars, flow, columns)


def fig1():
    fig, ax = page(
        "700 元额度，怎么分",
        "网传方案：外部模型拿 10%，自研模型拿 90%",
        source="来源：2026-11-26「大厂日爆」披露的据称内部通知。该通知未经腾讯官方确认，"
               "本图仅呈现网传方案的额度结构。",
        punch="不是「禁止使用外部模型」，而是「默认使用自研」。",
        foot="说明：额度数值为网传方案口径，真实性与最终执行标准以腾讯官方口径为准。")

    vbars(ax, [
        ("混元 HY4", 630, NAVY),
        ("外部模型", 70, RED),
    ], x0=0.180, base_y=0.330, max_h=0.300, width=0.220, gap=0.180,
        scale=700, unit=" 元", label_size=9.2, value_size=18.0)

    ax.text(0.045, 0.700, "默认月额度 700 元", fontsize=10.0, color=DARK,
            weight="bold", ha="left", va="center")

    card(ax, 0.045, 0.190, 0.900, 0.066, LIGHT, face=PALE)
    ax.text(0.068, 0.223, "子公司非技术岗：外部模型默认额度为 0，额外需求须单独申请。",
            fontsize=7.6, color=SLATE, ha="left", va="center", zorder=7)

    save(fig, "图1_七百元怎么分")


def fig2():
    fig, ax = page(
        "两步走，中间隔了一年",
        "先试点非技术岗，再全面切换默认项",
        source="来源：2026-11-26「大厂日爆」披露的据称内部通知（未经官方确认）。",
        punch="先动非技术岗，是阻力最小的切入口。",
        foot="说明：时间节点与适用范围均为网传方案，实际执行以官方口径为准。")

    flow(ax, [
        ("2026.12.01", "非技术岗试点\n外部额度 10%", NAVY),
        ("2027.01.01", "原则上默认自研\n外采须申请", TEAL),
        ("结果", "默认项改变\n选择成本转移", RED),
    ], y=0.560, x0=0.075, w=0.255, h=0.130, gap=0.060, arrow_color=GRAY)

    card(ax, 0.045, 0.300, 0.900, 0.190, LIGHT, face="white")
    ax.text(0.068, 0.458, "为什么先动非技术岗", fontsize=8.6, color=DARK,
            weight="bold", ha="left", va="center", zorder=7)
    ax.plot([0.068, 0.922], [0.438, 0.438], color=LIGHT, linewidth=0.9, zorder=7)

    rows = [
        ("岗位特征", "使用场景分散、单点影响小，切换的试错成本最低。"),
        ("数据价值", "文案、总结、问答是最高频场景，反馈量最密集。"),
        ("风险可控", "不涉及研发与生产系统，即便体验下降也不影响交付。"),
    ]
    y = 0.400
    for tag, text in rows:
        ax.text(0.068, y, tag, fontsize=7.6, color=NAVY, weight="bold",
                ha="left", va="center", zorder=7)
        ax.text(0.165, y, text, fontsize=7.5, color=SLATE,
                ha="left", va="center", zorder=7)
        y -= 0.042

    save(fig, "图2_两步走")


def fig3():
    fig, ax = page(
        "三层动机，成本只是最表面的",
        "从采购项，变成基础设施项",
        source="来源：对网传通知内容与公开信息的机制分析，非官方说明。",
        punch="自研模型的第一客户，是自己的员工。",
        foot="说明：本图为基于公开信息的分析框架，不代表企业内部真实决策依据。")

    columns(ax, [
        ("第一层", NAVY, "成本",
         "外部 API 是按量付费的现金支出；\n自研的边际成本主要是算力折旧。\n调用量越大，差距越明显。",
         "性质", "这是所有自建替代外采的\n共同逻辑，不新鲜。"),
        ("第二层", TEAL, "数据闭环",
         "用户怎么提问、哪些回答被采纳、\n哪些被改写、哪些被放弃——\n这些行为只有在自己平台上才有。",
         "性质", "用外部模型，等于把最有价值的\n使用数据送给别人。"),
        ("第三层", RED, "供应链",
         "外部模型可能调不动、涨价、\n或服务条款变化。\n核心工作流挂在别人身上是风险。",
         "性质", "今年以来的算力与模型供应\n不确定性，放大了这层考虑。"),
    ], y=0.330, h=0.400, x0=0.045, gap=0.018, w=0.290)

    save(fig, "图3_三层动机")


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done ->", os.path.dirname(os.path.abspath(__file__)))
