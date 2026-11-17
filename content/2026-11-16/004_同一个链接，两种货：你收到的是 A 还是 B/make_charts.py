# -*- coding: utf-8 -*-
"""
《同一个链接，两种货》配套图表

事实来源：
- 中国消费者协会 2026-11-12《中消协观点：网购"AB货"同价不同质 公平交易不容"欺生凌弱"》
- 中国青年报社会调查中心与问卷网 1001 人调查（2026-11-12 公布）

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


def box(d, x0, y0, x1, y1, fill=PALE, outline=LIGHT, radius=14, width=1):
    d.rounded_rectangle([x0, y0, x1, y1], radius=radius, fill=fill,
                        outline=outline, width=width)


def arrow(d, x, y0, y1, color=GRAY):
    d.line([(x, y0), (x, y1 - 12)], fill=color, width=2)
    d.polygon([(x - 7, y1 - 14), (x + 7, y1 - 14), (x, y1)], fill=color)


# ------------------------------------------------------- 图 1 一个链接两条路
def fig1():
    img, d = canvas()
    head(d, "一个链接，两条发货路径",
         "中消协点名的第二类表现：同一链接、同一价格，按消费者特征区别发货")

    box(d, 570, 208, 1230, 274)
    d.text((900, 241), "同 一 链 接　同 一 价 格", font=F(26, True), fill=DARK,
           anchor="mm")

    arrow(d, 900, 278, 330)
    box(d, 470, 332, 1330, 420, fill="white", outline=NAVY, width=2)
    d.text((900, 356), "平台算法画像", font=F(24, True), fill=NAVY, anchor="ma")
    d.text((900, 392), "收货地区 · 退换货记录 · 投诉记录 · 消费习惯",
           font=F(20), fill=GRAY, anchor="ma")

    # 分岔
    for x in (450, 1350):
        d.line([(900, 420), (900, 456)], fill=GRAY, width=2)
        d.line([(x, 456), (900, 456)], fill=GRAY, width=2)
        arrow(d, x, 456, 496)

    panels = [
        (210, "A 货", NAVY, "城区消费者 / 维权意识强的消费者",
         "收到品质正常的商品", "页面展示的那一件，和手里的一致"),
        (1010, "B 货", RED, "偏远农村消费者 / 被判定“退货不便”",
         "收到降级、减配的商品", "同一笔付款，拿到的是另一个版本"),
    ]
    for x0, tag, color, who, what, note in panels:
        box(d, x0, 500, x0 + 580, 790)
        d.rounded_rectangle([x0, 500, x0 + 580, 512], radius=4, fill=color)
        d.text((x0 + 34, 542), tag, font=F(34, True), fill=color)
        para(d, (x0 + 34, 606), who, 21, DARK, maxw=512, lh=1.45)
        d.text((x0 + 34, 672), what, font=F(22, True), fill=color)
        para(d, (x0 + 34, 716), note, 19, GRAY, maxw=512, lh=1.45)

    d.text((900, 830), "中消协：“看人下菜碟”的恃强凌弱之举，突破诚信底线、触碰法律红线。",
           font=F(22, True), fill=DARK, anchor="ma")

    footer(d, "据中国消费者协会 2026-11-12《中消协观点：网购“AB货”同价不同质 公平交易不容“欺生凌弱”》原文整理。")
    img.save(OUT + "图1_一个链接两条路.png", quality=95)
    return img


# ------------------------------------------------------- 图 2 踩过坑的人
def fig2():
    img, d = canvas()
    head(d, "一千人里，多少人踩过这个坑",
         "中国青年报社会调查中心与问卷网联合调查，样本 1001 人（2026 年 11 月 12 日公布）")

    # 左：两个大数字
    d.text((80, 210), "亲身经历", font=F(21), fill=GRAY)
    d.text((80, 246), "68.4%", font=F(86, True), fill=RED)
    d.text((80, 350), "受访者说自己在网购中踩过“AB货”", font=F(20), fill=DARK)
    d.text((80, 392), "另有 13.6% 表示“不确定”", font=F(19), fill=GRAY)

    d.line([(80, 440), (620, 440)], fill=LIGHT, width=2)
    d.text((80, 462), "治理想法", font=F(21), fill=GRAY)
    d.text((80, 498), "62.6%", font=F(58, True), fill=NAVY)
    d.text((80, 578), "期待建立“AB货”商家黑名单及公示制度", font=F(20), fill=DARK)

    # 右：品类条形
    x0, y0 = 700, 240
    d.text((x0, y0 - 46), "哪些品类最容易遇到“AB货”", font=F(23, True), fill=NAVY)
    d.text((x0, y0 - 12), "按受访者选择比例排序，可多选", font=F(18), fill=GRAY)

    data = [("服装鞋帽", 73.2, RED), ("生鲜水果", 48.8, NAVY),
            ("小家电 / 数码", 45.8, NAVY), ("美妆护肤", 42.7, NAVY),
            ("食品饮料", 36.0, NAVY), ("家纺家饰", 32.2, NAVY)]
    unit = 760 / 80.0
    y = y0 + 40
    for name, val, color in data:
        d.text((x0, y), name, font=F(20), fill=DARK, anchor="lm")
        d.rounded_rectangle([x0 + 240, y - 17, x0 + 240 + int(val * unit), y + 17],
                            radius=6, fill=color)
        d.text((x0 + 240 + int(val * unit) + 18, y), "%.1f%%" % val,
               font=F(20, True), fill=color, anchor="lm")
        y += 74

    d.text((700, 800), "差异不在参数表上，在克重、走线、成分和产地这类细节里。",
           font=F(21, True), fill=DARK)

    footer(d, "数据：中国青年报社会调查中心与问卷网 1001 人调查（2026-11-12 公布）；品类为多选题，受访者选择比例。")
    img.save(OUT + "图2_踩过坑的人有多少.png", quality=95)
    return img


# ------------------------------------------------------- 图 3 三件能做的事
def fig3():
    img, d = canvas()
    head(d, "三件能做的事",
         "都不用专业知识，只需要在下单前多看两分钟，收货时多拍两张照片")

    cards = [
        ("01", "看评价里的“批次”", NAVY,
         "把带图评价按时间翻一遍，看同一位置有没有两种状态：袖口走线、标签印字、包装版本。",
         "差评里那句“和上次买的不一样”，是最便宜的检测报告。"),
        ("02", "看退货率，不看评分", NAVY,
         "评分可以养，退货率难养。爆款退货率明显高于同类，说明货和页面之间有落差。",
         "同一链接下，不同批次评价对不上，本身就是信号。"),
        ("03", "对“便宜得离谱”保持警惕", RED,
         "同款价格低得反常，通常不是渠道优势，是降配：换成分、减克重、换产地。",
         "低价的成本，最后往往由收到 B 货的那个人承担。"),
    ]

    for i, (num, title, color, body, tail) in enumerate(cards):
        x0 = 80 + i * 550
        box(d, x0, 220, x0 + 530, 620)
        d.rounded_rectangle([x0, 220, x0 + 530, 232], radius=4, fill=color)
        d.text((x0 + 34, 258), num, font=F(22, True), fill=LIGHT)
        para(d, (x0 + 34, 300), title, 25, color, True, maxw=462, lh=1.4)
        d.line([(x0 + 34, 372), (x0 + 496, 372)], fill=LIGHT, width=1)
        para(d, (x0 + 34, 396), body, 19, DARK, maxw=462, lh=1.55)
        para(d, (x0 + 34, 500), tail, 17, GRAY, maxw=462, lh=1.5)

    box(d, 80, 660, 1720, 760, fill="white", outline=RED, width=2)
    d.text((112, 690), "还有一件事，中消协专门提了：收到货先别急着剪吊牌。",
           font=F(22, True), fill=RED)
    d.text((112, 726), "商品页面、直播录屏、下单记录、开箱实物照片——这几样留好，才是后面所有主张的起点。",
           font=F(20), fill=DARK)

    footer(d, "做法据中消协 2026-11-12 提示（证据留存）及媒体公开报道中的辨别思路整理，供参考，不构成法律意见。")
    img.save(OUT + "图3_三件能做的事.png", quality=95)
    return img


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")
