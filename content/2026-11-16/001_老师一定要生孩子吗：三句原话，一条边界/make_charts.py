# -*- coding: utf-8 -*-
"""
《老师一定要生孩子吗：三句原话，一条边界》配套图表

事实来源：
- 央视新闻频道《朝闻天下》2026-11-15“关注校园举报乱象”（原话、央视定调）
- 新京报/央视网报道中转述的接诉员陈昱陈述（9 月前两周收到近 40 封举报信；
  全校近 6000 名学生、90 多个班；过去一年四五封）
- 人民日报客户端 2026-10-21 评论《一有分歧就举报，老师还怎么教孩子》援引的统计
  （有学校近年实质性有效合规投诉约占 5%；西南某基层教育局 2024 年 1—8 月
  收到 128 条举报教师信息，查实基本属实 7 起）

风格：克制传媒风，白底、低饱和配色、标题即结论。
依赖：Pillow（本机 Python 无 matplotlib，故手绘版式）。
输出目录 = 脚本所在目录
"""
import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1800, 1020
BG = "white"
NAVY = (31, 58, 95)
RED = (181, 84, 74)
GRAY = (138, 143, 152)
LIGHT = (216, 219, 224)
DARK = (43, 47, 54)
PALE = (238, 240, 243)
RED_PALE = (246, 236, 234)

REG = "C:/Windows/Fonts/msyh.ttc"
BOLD = "C:/Windows/Fonts/msyhbd.ttc"
OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep

_fonts = {}


def F(size, bold=False):
    key = (size, bold)
    if key not in _fonts:
        _fonts[key] = ImageFont.truetype(BOLD if bold else REG, size)
    return _fonts[key]


def tw(d, s, f):
    return d.textlength(s, font=f)


def wrap(d, s, f, maxw):
    """按像素宽度折行，中文逐字断行。"""
    lines, cur = [], ""
    for ch in s:
        if ch == "\n":
            lines.append(cur)
            cur = ""
            continue
        if tw(d, cur + ch, f) <= maxw:
            cur += ch
        else:
            lines.append(cur)
            cur = ch
    if cur:
        lines.append(cur)
    return lines


def para(d, xy, s, size, color=DARK, bold=False, maxw=None, lh=1.55,
         anchor="la"):
    f = F(size, bold)
    lines = wrap(d, s, f, maxw) if maxw else s.split("\n")
    x, y = xy
    for ln in lines:
        d.text((x, y), ln, font=f, fill=color, anchor=anchor)
        y += int(size * lh)
    return y


def title_block(d, main, sub):
    d.text((80, 62), main, font=F(43, True), fill=DARK, anchor="la")
    if sub:
        para(d, (80, 132), sub, 21, GRAY, maxw=1640, lh=1.35)


def footer(d, s):
    para(d, (80, 962), s, 16, GRAY, maxw=1640, lh=1.4)


def takeaway(d, y, s):
    f = F(22, True)
    w = min(tw(d, s, f), 1640)
    d.rounded_rectangle([80, y, 80 + w + 56, y + 52], radius=12,
                        fill=PALE, outline=LIGHT, width=1)
    d.text((108, y + 26), s, font=f, fill=DARK, anchor="lm")


def new_canvas():
    img = Image.new("RGB", (W, H), BG)
    return img, ImageDraw.Draw(img)


# ------------------------------------------------------------------ 图 1
def fig1():
    img, d = new_canvas()
    title_block(d, "三句原话，三种被举报的“问题”",
                "央视新闻频道《朝闻天下》2026 年 11 月 15 日披露的校园举报案例，原话未作删改")

    rows = [
        ("举报原话",
         "“老师一定要生孩子吗？能不能保证新老师不怀孕？”",
         "出处：原班主任休产假，学校安排新教师接任，家长据此举报。",
         "这句话在要求",
         "为一位教师要不要生育、什么时候生育，作出担保。", NAVY),
        ("举报原话",
         "“这么小的孩子就干脏活累活，老师不能干吗？没钱请保洁吗？”",
         "出处：学校让学生轮流打扫厕所，本意是劳动教育；家长未与老师沟通。",
         "这句话在要求",
         "劳动教育可以存在，但不能落到自己孩子身上。", NAVY),
        ("接诉员原话",
         "“很多事在孩子看来没什么问题。”",
         "出处：该校接诉员陈昱——孩子不觉得有问题，家长一听说就焦虑，甚至觉得受了侮辱。",
         "这句话在说明",
         "被举报的“问题”，常常不在孩子身上，在家长的想象里。", RED),
    ]

    y = 196
    for tag, quote, src, tag2, note, color in rows:
        h = 186
        d.rounded_rectangle([80, y, 1720, y + h], radius=14, fill=PALE,
                            outline=LIGHT, width=1)
        d.rounded_rectangle([80, y, 90, y + h], radius=4, fill=color)
        d.text((126, y + 26), tag, font=F(17), fill=color, anchor="la")
        qy = para(d, (126, y + 56), quote, 27, DARK, True, maxw=980, lh=1.42)
        para(d, (126, qy + 2), src, 18, GRAY, maxw=980, lh=1.4)
        d.line([(1150, y + 30), (1150, y + h - 26)], fill=LIGHT, width=1)
        d.text((1196, y + 26), tag2, font=F(17), fill=GRAY, anchor="la")
        para(d, (1196, y + 58), note, 21, DARK, maxw=490, lh=1.5)
        y += h + 30

    takeaway(d, 848, "三句话里，没有一句在问：孩子到底学到了什么。")
    footer(d, "原话与出处：央视《朝闻天下》2026-11-15 报道及新京报、央视网转述。")
    img.save(OUT + "图1_三句原话.png", quality=95)
    return img


# ------------------------------------------------------------------ 图 2
def fig2():
    img, d = new_canvas()
    title_block(d, "两周 40 封：举报信的数量，和它被查实的比例",
                "接诉员陈昱所在小学近 6000 名学生、90 多个班；数据来自公开报道与评论援引的统计")

    # ---- 左：时间对比（纵柱，基线 y=700）
    d.text((80, 214), "同一所学校，举报量的变化", font=F(24, True), fill=NAVY)
    d.line([(80, 262), (830, 262)], fill=LIGHT, width=2)

    base_y, unit, bw = 700, 8.5, 130
    bars = [
        ("过去一整年", 5, "4—5 封", GRAY, 250),
        ("今年 9 月前两周", 40, "近 40 封", RED, 480),
    ]
    for label, val, txt, color, x in bars:
        top = base_y - val * unit
        d.rounded_rectangle([x, top, x + bw, base_y], radius=6, fill=color)
        d.text((x + bw / 2, top - 16), txt, font=F(26, True), fill=color,
               anchor="mb")
        d.text((x + bw / 2, base_y + 18), label, font=F(20), fill=DARK,
               anchor="ma")
    d.line([(180, base_y), (860, base_y)], fill=LIGHT, width=2)

    d.text((80, 786), "陈昱：过去一年四五封，就已经“非常可怕”。", font=F(20),
           fill=DARK, anchor="la")
    d.text((80, 826), "今年九月前两周，几乎每天都有红点邮件从教育局转来。",
           font=F(19), fill=GRAY, anchor="la")

    # ---- 右：查实比例
    x0 = 900
    d.text((x0, 214), "西南某基层教育局：举报数与查实数", font=F(24, True),
           fill=NAVY)
    d.line([(x0, 262), (1720, 262)], fill=LIGHT, width=2)
    d.text((x0, 288), "2024 年 1—8 月，收到 128 条举报教师的信息", font=F(20),
           fill=GRAY, anchor="la")

    # 128 格方块阵列：7 格红点 = 查实基本属实
    cols, cell, gap = 16, 40, 8
    for n in range(128):
        r, c = divmod(n, cols)
        cx = x0 + c * (cell + gap)
        cy = 336 + r * (cell + gap)
        fill = RED if n < 7 else LIGHT
        d.rounded_rectangle([cx, cy, cx + cell, cy + cell], radius=6, fill=fill)

    gy = 336 + 8 * (cell + gap) + 10
    d.text((x0, gy), "7 格红点 = 查实基本属实的 7 起", font=F(20, True),
           fill=RED, anchor="la")
    d.text((x0, gy + 44), "另有学校梳理近年投诉：实质性有效合规的约占 5%",
           font=F(19), fill=GRAY, anchor="la")

    takeaway(d, 880, "举报渠道越顺畅，越需要有人先分辨：哪封该查，哪封该打个电话。")
    footer(d, "数据：新京报、央视网关于该校的报道；人民日报客户端 2026-10-21 评论援引的统计。")
    img.save(OUT + "图2_举报量与查实率.png", quality=95)
    return img


# ------------------------------------------------------------------ 图 3
def fig3():
    img, d = new_canvas()
    title_block(d, "一条边界，三个可对照的判据",
                "不判断家长该不该着急，只判断这一次举报，还是不是维权")

    rows = [
        ("01", "先沟通了吗", "扫厕所这件事，家长没跟老师说过一句话。",
         "先问一句“为什么让孩子打扫厕所”，大概率会听到“劳动教育”四个字，事就结束了。",
         "先问，再报", RED),
        ("02", "举报的是事，还是人", "“为什么不让孩子扫地”是事；“老师不能干吗”不是事。",
         "是事，可以核实、可以改；是情绪，没有可核实的答案，只能落到具体的人身上。",
         "事可核，人难核", NAVY),
        ("03", "要的是改进，还是排除", "要求学校说明安排，是改进；要求保证新老师不怀孕，是排除。",
         "改进有止境，做到就可以收；排除没有止境——只要这个人还在，诉求就永远成立。",
         "改进 / 排除", NAVY),
    ]

    y = 200
    for num, head, line1, line2, badge, color in rows:
        h = 208
        d.rounded_rectangle([80, y, 1720, y + h], radius=14, fill=PALE,
                            outline=LIGHT, width=1)
        d.rounded_rectangle([80, y, 90, y + h], radius=4, fill=color)
        d.text((130, y + 38), num, font=F(30, True), fill=LIGHT, anchor="la")
        d.text((196, y + 36), head, font=F(29, True), fill=color, anchor="la")
        para(d, (196, y + 88), line1, 21, DARK, maxw=1180, lh=1.45)
        para(d, (196, y + 138), line2, 19, GRAY, maxw=1180, lh=1.45)
        f = F(18, True)
        bw = tw(d, badge, f) + 40
        d.rounded_rectangle([1680 - bw, y + 34, 1680, y + 78], radius=10,
                            fill="white", outline=color, width=2)
        d.text((1680 - bw / 2, y + 56), badge, font=f, fill=color, anchor="mm")
        y += h + 24

    takeaway(d, 888, "举报是权利；三条都过不去，它就换了性质。")
    footer(d, "据央视《朝闻天下》2026-11-15 报道中的举报原话整理；判据为本文归纳。")
    img.save(OUT + "图3_三个判据.png", quality=95)
    return img


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")
