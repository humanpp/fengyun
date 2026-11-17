# -*- coding: utf-8 -*-
"""
《41 万买的房，为什么退不掉》配套图表

事实来源：央视《每周质量报告》2026-11-15《"低价游"背后的"买房陷阱"》
及央广网、央视新闻客户端同日报道（无锡合富至胜营销策划有限公司揽客、
丹阳海景房产经纪有限公司带看、出卖人为日照丽城建设发展有限公司乳山山译分公司、
总公司 2023 年 11 月被裁定宣告破产、41 万元成交、同款二手房不足 9 万元、
20% 违约金即 8.2 万元、建行乳山支行面签并教客户谎报婚姻状态）

风格：白底、深蓝 #1f3a5f 配砖红 #b5544a、标题即结论。
依赖：Pillow。输出目录 = 脚本所在目录
"""
import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1800, 1020
NAVY = (31, 58, 95)
RED = (181, 84, 74)
GRAY = (138, 143, 152)
LIGHT = (216, 219, 224)
DARK = (43, 47, 54)
PALE = (238, 240, 243)

REG = "C:/Windows/Fonts/msyh.ttc"
BOLD = "C:/Windows/Fonts/msyhbd.ttc"
OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep

_f = {}


def F(size, bold=False):
    if (size, bold) not in _f:
        _f[(size, bold)] = ImageFont.truetype(BOLD if bold else REG, size)
    return _f[(size, bold)]


def wrap(d, s, f, maxw):
    lines, cur = [], ""
    for ch in s:
        if ch == "\n":
            lines.append(cur)
            cur = ""
            continue
        if d.textlength(cur + ch, font=f) <= maxw:
            cur += ch
        else:
            lines.append(cur)
            cur = ch
    if cur:
        lines.append(cur)
    return lines


def para(d, xy, s, size, color=DARK, bold=False, maxw=None, lh=1.5):
    f = F(size, bold)
    lines = wrap(d, s, f, maxw) if maxw else s.split("\n")
    x, y = xy
    for ln in lines:
        d.text((x, y), ln, font=f, fill=color)
        y += int(size * lh)
    return y


def head(d, main, sub):
    d.text((80, 62), main, font=F(43, True), fill=DARK)
    para(d, (80, 132), sub, 21, GRAY, maxw=1640, lh=1.35)


def footer(d, s):
    para(d, (80, 962), s, 16, GRAY, maxw=1640, lh=1.4)


def canvas():
    img = Image.new("RGB", (W, H), "white")
    return img, ImageDraw.Draw(img)


# ------------------------------------------------------------ 图 1 四个环节
def fig1():
    img, d = canvas()
    head(d, "一笔 41 万，卡在四个环节上",
         "揽客在无锡，带看在丹阳，成交在乳山，面签在乳山的银行——四段各在一地")

    stages = [
        ("01", "揽客", "无锡合富至胜营销策划有限公司", "江苏 无锡",
         "在短视频平台找博主引客，门头挂“山东威海海景豪宅服务中心”", "合同上：没有"),
        ("02", "带看", "丹阳海景房产经纪有限公司", "江苏 丹阳",
         "组织张女士参团，看房、游说、催签，全程陪同", "合同上：没有"),
        ("03", "签约", "出卖人：日照丽城建设发展有限公司乳山山译分公司", "山东 乳山",
         "补充协议约定 20% 违约金；总公司已于 2023 年 11 月被裁定宣告破产", "合同上：只有它"),
        ("04", "贷款", "建设银行乳山支行面签", "山东 乳山",
         "中介现场教客户谎报婚姻状态；房贷不通时改走信用贷、消费贷", "合同上：有"),
    ]

    y, h = 210, 560
    for i, (num, name, who, place, desc, mark) in enumerate(stages):
        x0 = 80 + i * 415
        color = RED if i >= 2 else NAVY
        d.rounded_rectangle([x0, y, x0 + 385, y + h], radius=14, fill=PALE,
                            outline=LIGHT, width=1)
        d.rounded_rectangle([x0, y, x0 + 385, y + 8], radius=4, fill=color)
        d.text((x0 + 26, y + 34), num, font=F(20, True), fill=LIGHT)
        d.text((x0 + 26, y + 68), name, font=F(30, True), fill=color)
        para(d, (x0 + 26, y + 124), who, 19, DARK, maxw=333, lh=1.45)
        d.text((x0 + 26, y + 250), place, font=F(18), fill=GRAY)
        d.line([(x0 + 26, y + 288), (x0 + 359, y + 288)], fill=LIGHT, width=1)
        para(d, (x0 + 26, y + 306), desc, 18, GRAY, maxw=333, lh=1.5)
        d.text((x0 + 26, y + h - 58), mark, font=F(21, True), fill=color)
        if i < 3:
            d.text((x0 + 392, y + 250), "→", font=F(34, True), fill=LIGHT)

    d.rounded_rectangle([80, 800, 1720, 862], radius=12, fill=PALE,
                        outline=LIGHT, width=1)
    d.text((108, 831), "四个环节，三张不同的名片，一句没人录音的承诺——最后只剩一个人签字。",
           font=F(22, True), fill=DARK, anchor="lm")

    footer(d, "据央视《每周质量报告》2026-11-15 报道中张女士的经历整理；企业信息经全国企业破产重整案件信息网核对。")
    img.save(OUT + "图1_四个环节.png", quality=95)
    return img


# ------------------------------------------------------------ 图 2 三个数字
def fig2():
    img, d = canvas()
    head(d, "三个数字：41 万、9 万、8.2 万",
         "同一套房，买入价、市价、解约价；单位为元，按同一比例尺绘制")

    unit = 900 / 410000  # 41 万 = 900 像素
    bars = [
        ("合同成交价", 410000, "41 万", RED, "50.6 平方米，2026 年 8 月签约"),
        ("同款二手房市价", 90000, "不足 9 万", GRAY, "同小区、同栋、同面积毛坯"),
        ("解约违约金", 82000, "8.2 万", NAVY, "合同总价的 20%"),
    ]

    y = 240
    for name, val, txt, color, sub in bars:
        d.text((80, y), name, font=F(21), fill=DARK)
        w = max(int(val * unit), 4)
        d.rounded_rectangle([80, y + 40, 80 + w, y + 108], radius=8, fill=color)
        d.text((80 + w + 24, y + 74), txt, font=F(30, True), fill=color,
               anchor="lm")
        d.text((80, y + 120), sub, font=F(18), fill=GRAY)
        y += 190

    d.text((80, 830), "违约金几乎等于一套同款二手房的价钱——这说明签约那一刻，价格就已经不对等了。",
           font=F(22, True), fill=RED)

    footer(d, "价格与违约金条款：央视《每周质量报告》2026-11-15 报道中张女士的购房合同；二手房价格由记者实地询价。")
    img.save(OUT + "图2_三个数字.png", quality=95)
    return img


# ------------------------------------------------------------ 图 3 四个部门
def fig3():
    img, d = canvas()
    head(d, "四个部门，各管一段",
         "跨区域模式把一条链条拆给四只手，每只手都只够得着自己那一段")

    cards = [
        ("文旅", "管旅游经营资质：组织带看、收费揽客，算不算旅游业务",
         "例：无锡合富至胜每周五发车，单人 150 元", "无锡核查主体", NAVY),
        ("住建", "管预售许可、网签备案、合同公示与资金监管",
         "例：该楼盘 2013 年备案 7430 元，2021 年转现房", "乳山核查主体", NAVY),
        ("市场监管", "管虚假宣传、广告与价格：保底涨价、以租养贷",
         "例：“五年托管抵月供”算不算承诺", "两地均参与", RED),
        ("公安", "管诈骗、伪造材料与骗贷：教客户谎报婚姻状态",
         "例：面签前教客户报“离异”", "两地均参与", RED),
    ]

    pos = [(80, 226), (940, 226), (80, 520), (940, 520)]
    for (x0, y0), (name, body, eg, who, color) in zip(pos, cards):
        d.rounded_rectangle([x0, y0, x0 + 780, y0 + 252], radius=14,
                            fill=PALE, outline=LIGHT, width=1)
        d.rounded_rectangle([x0, y0, x0 + 10, y0 + 252], radius=4, fill=color)
        d.text((x0 + 40, y0 + 30), name, font=F(30, True), fill=color)
        para(d, (x0 + 40, y0 + 86), body, 20, DARK, maxw=700, lh=1.45)
        d.text((x0 + 40, y0 + 176), eg, font=F(18), fill=GRAY)
        d.text((x0 + 40, y0 + 212), who, font=F(18), fill=color)

    d.rounded_rectangle([80, 866, 1720, 926], radius=12, fill="white",
                        outline=RED, width=2)
    d.text((108, 896), "中间的缝：揽客地不成交，成交地不揽客——谁都能说这一段不归自己管。",
           font=F(22, True), fill=RED, anchor="lm")

    footer(d, "监管职责划分据《旅游法》《城市房地产管理法》《广告法》及乳山、无锡两地 11 月 15 日核查通报。")
    img.save(OUT + "图3_四个部门.png", quality=95)
    return img


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")
