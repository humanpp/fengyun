# -*- coding: utf-8 -*-
"""
《200 元的团费，680 元的成本》配套图表

事实来源：央视《每周质量报告》2026-11-15《"低价游"背后的"买房陷阱"》
及央广网、央视新闻客户端同日报道（150 元／人、夫妻 200 元、实际成本一人 680 元、
推荐成交提成 5000 元、夏季一周三四百辆大巴、金拇指沙滩停留不足半小时、
售楼处话术、催交 5 万元定金且拒不出示合同）

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


def note(d, y, s, color=DARK, size=22, bold=True):
    f = F(size, bold)
    w = d.textlength(s, font=f)
    d.rounded_rectangle([80, y, 80 + w + 56, y + 54], radius=12, fill=PALE,
                        outline=LIGHT, width=1)
    d.text((108, y + 27), s, font=f, fill=color, anchor="lm")


def canvas():
    img = Image.new("RGB", (W, H), "white")
    return img, ImageDraw.Draw(img)


# ------------------------------------------------------------ 图 1 一辆车的账
def fig1():
    img, d = canvas()
    head(d, "150 元的票，680 元的成本",
         "无锡到乳山单程 700 多公里，三天两夜包吃住；差额由想卖房的人承担")

    d.text((80, 230), "按人头算的一笔账", font=F(24, True), fill=NAVY)
    d.line([(80, 268), (900, 268)], fill=LIGHT, width=2)

    d.text((80, 330), "收进来", font=F(21), fill=GRAY)
    d.rounded_rectangle([260, 312, 466, 384], radius=8, fill=NAVY)
    d.text((486, 348), "150—200 元", font=F(26, True), fill=NAVY, anchor="lm")

    d.text((80, 470), "支出去", font=F(21), fill=GRAY)
    d.rounded_rectangle([260, 452, 960, 524], radius=8, fill=RED)
    d.text((980, 488), "680 元", font=F(26, True), fill=RED, anchor="lm")

    d.line([(466, 300), (466, 540)], fill=NAVY, width=2)
    d.line([(300, 560), (960, 560)], fill=RED, width=2)
    d.line([(300, 560), (300, 546)], fill=RED, width=2)
    d.line([(960, 560), (960, 546)], fill=RED, width=2)
    d.text((630, 578), "缺口 480—530 元／人，由开发商补贴",
           font=F(19, True), fill=RED, anchor="ma")

    para(d, (80, 630), "售票收入只覆盖实际成本的三成左右。剩下那七成，"
                       "就是这趟车的真实票价：它买你的注意力，和一次坐在售楼处的机会。",
         21, DARK, maxw=1600, lh=1.6)

    # 两张数字卡
    cards = [
        ("5000 元", "成功推荐他人购房，能拿到的提成", NAVY),
        ("300—400 辆", "夏季高峰时，他们一周发出的看房大巴", RED),
    ]
    for i, (big, lab, color) in enumerate(cards):
        x0 = 80 + i * 840
        d.rounded_rectangle([x0, 730, x0 + 800, 850], radius=14, fill=PALE,
                            outline=LIGHT, width=1)
        d.rounded_rectangle([x0, 730, x0 + 10, 850], radius=4, fill=color)
        d.text((x0 + 44, 764), big, font=F(38, True), fill=color)
        d.text((x0 + 44, 820), lab, font=F(19), fill=GRAY)

    footer(d, "数据：央视《每周质量报告》2026-11-15 及央广网、央视新闻客户端报道；销售自述成本一人 680 元。")
    img.save(OUT + "图1_一辆车的账.png", quality=95)
    return img


# ------------------------------------------------------------ 图 2 行程
def fig2():
    img, d = canvas()
    head(d, "一趟车的行程：景点只有半小时",
         "记者交 200 元随团，记录下的时间线（报道只给出“周六上午八点多”，钟点为示意）")

    rows = [
        ("周五", "发车", "每周五定期发车，无锡出发，往北 700 多公里", NAVY),
        ("周六 8 点多", "大巴停车", "停在乳山市滨海新区管委会门前，人直接被领到对面广场", NAVY),
        ("随后", "沙滩观光", "金拇指广场紧挨沙滩；停留不到半小时，每位老人身边跟着一到两名西装销售", NAVY),
        ("半小时后", "直奔楼盘", "大巴径直开向鼎泰臻寓；售楼处背景音乐震耳，购房者无法私下交谈", RED),
        ("随后", "第二处楼盘", "香港平远国际城：54 平方米报价 67 万余元，单价 1.24 万元", RED),
        ("收尾", "交钱、签字", "催交 5 万元定金、签认购书；多次要求看购房合同，始终不给", RED),
    ]

    y = 200
    d.line([(128, y + 46), (128, y + 46 + 5 * 112)], fill=LIGHT, width=3)
    for i, (tm, tag, txt, color) in enumerate(rows):
        cy = y + 46
        d.ellipse([118, cy - 11, 140, cy + 11], fill=color)
        if i == len(rows) - 1:
            d.rounded_rectangle([80, y - 10, 1720, y + 100], radius=14,
                                fill=PALE, outline=LIGHT, width=1)
            d.ellipse([118, cy - 11, 140, cy + 11], fill=color)
        d.text((176, y + 16), tm, font=F(21, True), fill=color)
        d.text((176, y + 54), tag, font=F(19), fill=GRAY)
        para(d, (400, y + 26), txt, 22, DARK, maxw=1260, lh=1.5)
        y += 112

    footer(d, "据央视《每周质量报告》2026-11-15 记者随团记录整理。")
    img.save(OUT + "图2_周六的行程.png", quality=95)
    return img


# ------------------------------------------------------------ 图 3 四句话
def fig3():
    img, d = canvas()
    head(d, "售楼处里的四句话，每一句都指向同一个动作",
         "央视记者在鼎泰臻寓、香港平远国际城售楼处听到的原话")

    rows = [
        ("“三到五年，增值空间每平方米 2000 元。”", "鼎泰臻寓售楼处",
         "把一套房子说成一笔确定的收益"),
        ("“月供 1500，租金 1500，以租养贷。”", "鼎泰臻寓售楼处",
         "让你相信这笔贷款会自己还自己"),
        ("“五年托管租金一次性结算，13.4 万。”", "香港平远国际城售楼处",
         "先递给你一笔钱，再谈划算"),
        ("“两万抵五万，车位和现金二选一。”", "鼎泰臻寓售楼处",
         "把所有优惠压缩成今天的决定"),
    ]

    y = 196
    for quote, where, aim in rows:
        h = 148
        d.rounded_rectangle([80, y, 1720, y + h], radius=14, fill=PALE,
                            outline=LIGHT, width=1)
        d.rounded_rectangle([80, y, 90, y + h], radius=4, fill=RED)
        para(d, (126, y + 30), quote, 26, DARK, True, maxw=1000, lh=1.4)
        d.text((126, y + 106), "出处：" + where, font=F(18), fill=GRAY)
        d.line([(1170, y + 30), (1170, y + h - 30)], fill=LIGHT, width=1)
        d.text((1216, y + 30), "这句话要你做的事", font=F(17), fill=GRAY)
        para(d, (1216, y + 60), aim, 21, NAVY, True, maxw=470, lh=1.45)
        y += h + 18

    note(d, 866, "四句话没有一句提到：这房子的备案价是多少，产权还剩几年。", GRAY, 21, False)
    footer(d, "原话：央视《每周质量报告》2026-11-15 报道；该楼盘 2013 年备案均价 7430 元/平方米，产权起算 2001 年。")
    img.save(OUT + "图3_售楼处四句话.png", quality=95)
    return img


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")
