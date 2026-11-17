# -*- coding: utf-8 -*-
"""
《你的相册里有什么》配套图表

事实来源：意大利个人数据保护局（Garante）2026-11-14 处罚公告（805 百万欧元、
涉事功能“浏览 Facebook 时从相册获取推荐”、默认开启、单一授权覆盖多用途、
约 2000 万意大利安卓用户、60 天内默认关闭并单独同意）；新华社 11-14 罗马电、
BBC／美联社／卫报同日报道；安莎社（罚款约占 Meta 全球营业额 0.47%）。

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


# ------------------------------------------------------------ 图 1 罚款
def fig1():
    img, d = canvas()
    head(d, "59 亿元，是怎么算出来的",
         "2026 年 11 月 14 日，意大利个人数据保护局对 Meta 爱尔兰公司作出处罚")

    d.text((80, 226), "8.05 亿欧元", font=F(64, True), fill=RED)
    d.text((80, 320), "约合人民币 59 亿元　·　8.87 亿美元", font=F(23), fill=DARK)
    d.text((80, 364), "按当日汇率折算，约 0.47% 的 Meta 全球营业额",
           font=F(19), fill=GRAY)

    stats = [
        ("约 2000 万", "受影响的意大利安卓用户", RED),
        ("60 天", "整改期限：默认关闭，单独征求同意", NAVY),
        ("0.47%", "罚款额占 Meta 全球营业额", NAVY),
    ]
    y = 226
    for big, lab, color in stats:
        d.line([(860, y - 12), (860, y + 118)], fill=LIGHT, width=1)
        d.text((900, y), big, font=F(34, True), fill=color)
        para(d, (900, y + 56), lab, 19, GRAY, maxw=820, lh=1.4)
        y += 118

    # 0.47% 比例尺
    d.text((80, 512), "把罚款放进 Meta 的全球营收里", font=F(21), fill=GRAY)
    d.rounded_rectangle([80, 556, 1720, 602], radius=8, fill=PALE,
                        outline=LIGHT, width=1)
    d.rounded_rectangle([80, 556, 92, 602], radius=6, fill=RED)
    d.text((110, 618), "红的这一小条 = 罚款，约占营收 0.47%", font=F(19, True),
           fill=RED)
    d.text((1720, 618), "整条 = 一年全球营收", font=F(19), fill=GRAY,
           anchor="ra")

    d.rounded_rectangle([80, 700, 1720, 764], radius=12, fill=PALE,
                        outline=LIGHT, width=1)
    d.text((108, 732), "比例很小，绝对数很大——这是 GDPR 罚单的典型形状，"
                       "也是它被认真对待的原因。", font=F(22, True), fill=DARK,
           anchor="lm")

    footer(d, "数据：Garante 2026-11-14 公告；新华社、BBC、美联社、卫报同日报道；安莎社（营收占比 0.47%）。")
    img.save(OUT + "图1_罚款的数字.png", quality=95)
    return img


# ------------------------------------------------------------ 图 2 三件事
def fig2():
    img, d = canvas()
    head(d, "这个功能，做错了三件事",
         "意大利监管机构认定的问题：不在“读相册”，在“怎么拿到同意”")

    rows = [
        ("默认开启", "用户没有被问过。功能自 2023 年上线起，就替你开着。",
         "合规做法", "默认关闭，让用户主动打开", RED),
        ("一揽子授权", "一个“允许访问相册”，同时覆盖发图、修图、相册推荐好几个用途。",
         "合规做法", "按用途分别授权，一个用途一次同意", RED),
        ("没有专项同意", "推荐发帖和上传头像，是两件事，却用一次同意打包处理。",
         "合规做法", "就“从相册取推荐”单独弹窗、单独征求", NAVY),
    ]

    y = 200
    for name, desc, tag, right, color in rows:
        h = 170
        box(d, 80, y, 1720, y + h)
        d.rounded_rectangle([80, y, 90, y + h], radius=4, fill=color)
        d.text((130, y + 32), name, font=F(28, True), fill=color)
        para(d, (130, y + 86), desc, 20, DARK, maxw=880, lh=1.5)
        d.line([(1090, y + 30), (1090, y + h - 30)], fill=LIGHT, width=1)
        d.text((1136, y + 32), tag, font=F(17), fill=GRAY)
        para(d, (1136, y + 66), right, 21, NAVY, True, maxw=520, lh=1.45)
        y += h + 22

    d.rounded_rectangle([80, 800, 1720, 864], radius=12, fill=PALE,
                        outline=LIGHT, width=1)
    d.text((108, 832), "一句话：同意被做成了一个开关，而它本该是几个问题。",
           font=F(22, True), fill=DARK, anchor="lm")

    footer(d, "据 Garante 2026-11-14 处罚公告中认定的违规情形整理；右侧“合规做法”为公告整改要求的概括。")
    img.save(OUT + "图2_三件事.png", quality=95)
    return img


# ------------------------------------------------------------ 图 3 自查
def fig3():
    img, d = canvas()
    head(d, "三分钟自查",
         "不用卸载任何东西，先把权限范围收窄，再关掉那几个默认打开的开关")

    steps = [
        ("01", "看清单：谁在要相册权限", NAVY,
         "iPhone：设置 → 隐私与安全性 → 照片",
         "安卓：设置 → 应用 → 权限 → 照片和视频",
         "一眼能看到哪些 App 拿走了“全部照片”。社交、修图、购物类 App 是重点。"),
        ("02", "改范围：从“全部”改成“选中”", NAVY,
         "把“完整访问”“所有照片”改成“选中的照片”",
         "只需授权你要发的那几张，其余留在手机里",
         "iOS 与较新的安卓都支持部分授权；改完不影响正常发图。"),
        ("03", "关推荐：把默认值翻过来", RED,
         "找“从相册获取推荐”“自动生成回忆”“智能相册”",
         "这些开关的出厂值，往往是开的",
         "关掉之后，App 就没有理由要求常驻访问相册了。"),
    ]

    y = 200
    for num, title, color, l1, l2, note in steps:
        h = 176
        box(d, 80, y, 1720, y + h)
        d.rounded_rectangle([80, y, 90, y + h], radius=4, fill=color)
        d.text((126, y + 28), num, font=F(24, True), fill=LIGHT)
        d.text((186, y + 26), title, font=F(27, True), fill=color)
        d.text((186, y + 76), l1, font=F(20), fill=DARK)
        d.text((186, y + 110), l2, font=F(20), fill=DARK)
        d.line([(860, y + 26), (860, y + h - 26)], fill=LIGHT, width=1)
        para(d, (900, y + 78), note, 18, GRAY, maxw=790, lh=1.5)
        y += h + 20

    d.rounded_rectangle([80, 800, 1720, 864], radius=12, fill="white",
                        outline=RED, width=2)
    d.text((108, 832), "改权限不影响正常使用；真正需要相册的 App，会在你用到时再问一次。",
           font=F(21, True), fill=RED, anchor="lm")

    footer(d, "操作路径以 iOS 与安卓近期版本为准，不同机型菜单名称略有差异；图内建议仅供参考。")
    img.save(OUT + "图3_三分钟自查.png", quality=95)
    return img


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")
