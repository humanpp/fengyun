# -*- coding: utf-8 -*-
"""
《雷达被炸，油价没跳》配套图表

事实来源：
- 伊朗伊斯兰革命卫队 2026-11-15 声明、巴林国防军总司令部声明、巴林内政部两次警报、
  伊朗外交部发言人巴加埃表态（新华社德黑兰／利雅得电）
- BBC、卫报、半岛电视台、法新社同日报道
- 布伦特 95.84 美元/桶（周跌约 2%）、现货金 3883 美元/盎司（当日 +0.18%、当周约 −4.6%）
- 霍尔木兹海峡：EIA 数据，约 2000 万桶/日、占全球石油液体消费约 1/5、海运石油贸易约 1/4、最窄 33 公里

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


def arrow_right(d, x0, x1, y, color=GRAY):
    d.line([(x0, y), (x1 - 10, y)], fill=color, width=3)
    d.polygon([(x1 - 12, y - 8), (x1 - 12, y + 8), (x1, y)], fill=color)


# ------------------------------------------------------- 图 1 时间线
def fig1():
    img, d = canvas()
    head(d, "11 月 15 日，一天里发生了什么",
         "伊朗方面宣布打击、巴林方面拦截并拉警报，同一时间市场给出的却是另一个答案")

    rows = [
        ("上午", "宣布打击", "伊朗革命卫队：6 架无人机打击里法直升机基地的美军防空雷达", NAVY),
        ("随后", "巴林拦截", "巴林国防军：多架无人机在到达目标前被拦截摧毁", NAVY),
        ("同日", "两次警报", "巴林内政部两次发布安全警报，呼吁民众前往最近安全地点", RED),
        ("同日", "伊方定性", "伊朗外交部发言人巴加埃：这是“回应美国侵略”", NAVY),
        ("同日", "另一条消息", "伊朗称霍尔木兹以南两艘油轮触雷，其中一艘载油约 200 万桶（未获独立证实）", RED),
        ("收盘", "市场反应", "布伦特 95.84 美元／桶，一周跌约 2%；现货金 3883 美元，当日仅涨 0.18%", NAVY),
    ]

    y = 200
    d.line([(128, y + 46), (128, y + 46 + 5 * 112)], fill=LIGHT, width=3)
    for i, (tm, tag, txt, color) in enumerate(rows):
        cy = y + 46
        last = i == len(rows) - 1
        if last:
            d.rounded_rectangle([80, y - 12, 1720, y + 100], radius=14,
                                fill=PALE, outline=LIGHT, width=1)
        d.ellipse([118, cy - 11, 140, cy + 11], fill=color)
        d.text((176, y + 14), tm, font=F(21, True), fill=color)
        d.text((176, y + 52), tag, font=F(19), fill=GRAY)
        para(d, (400, y + 24), txt, 21, DARK, maxw=1270, lh=1.5)
        y += 112

    footer(d, "据新华社、BBC、卫报、半岛电视台、法新社 2026-11-15 报道及当日市场收盘数据整理。")
    img.save(OUT + "图1_一天里发生了什么.png", quality=95)
    return img


# ------------------------------------------------------- 图 2 那条水道
def fig2():
    img, d = canvas()
    head(d, "为什么是这个地方：一条最窄 33 公里的水道",
         "巴林紧邻波斯湾西岸；所有波斯湾产油国的出口，几乎都要穿过霍尔木兹海峡")

    # 三段示意
    panels = [
        (80, "波斯湾", "所有波斯湾产油国的出口起点", NAVY,
         "巴林 · 里法基地就在这一侧"),
        (660, "霍尔木兹海峡", "最窄处 33 公里", RED,
         "北侧伊朗，南侧阿曼与阿联酋"),
        (1240, "阿曼湾 → 阿拉伯海", "出海峡之后进入印度洋航线", NAVY,
         "再往东，是亚洲的主要买家"),
    ]
    for i, (x0, name, desc, color, note) in enumerate(panels):
        box(d, x0, 250, x0 + 480, 470)
        d.rounded_rectangle([x0, 250, x0 + 480, 262], radius=4, fill=color)
        d.text((x0 + 34, 300), name, font=F(29, True), fill=color)
        para(d, (x0 + 34, 356), desc, 20, DARK, maxw=412, lh=1.45)
        d.text((x0 + 34, 428), note, font=F(18), fill=GRAY)
        if i < 2:
            arrow_right(d, x0 + 492, x0 + 566, 360)

    # 数据条
    box(d, 80, 520, 1720, 700, fill="white", outline=LIGHT, width=2)
    stats = [("约 2000 万桶", "每天经过海峡的石油"),
             ("约 1/5", "占全球石油液体消费"),
             ("约 1/4", "占全球海运石油贸易"),
             ("33 公里", "海峡最窄处宽度")]
    for i, (big, lab) in enumerate(stats):
        x0 = 116 + i * 405
        d.text((x0, 552), big, font=F(32, True), fill=RED if i == 3 else NAVY)
        d.text((x0, 608), lab, font=F(19), fill=GRAY)
        if i < 3:
            d.line([(x0 + 340, 548), (x0 + 340, 632)], fill=LIGHT, width=1)

    d.text((80, 732), "美国能源信息署：一旦这里关闭，几乎没有替代方案能把油运出去。",
           font=F(21), fill=DARK)
    d.text((80, 772), "所以伊朗打的是雷达，市场读的是“这条水道的风险在上升”。",
           font=F(21, True), fill=NAVY)

    footer(d, "流量与占比：美国能源信息署（EIA）数据；最窄处 33 公里据 BBC 中文。示意图，非按比例绘制。")
    img.save(OUT + "图2_那条水道.png", quality=95)
    return img


# ------------------------------------------------------- 图 3 传导链
def fig3():
    img, d = canvas()
    head(d, "从海峡到油箱，要走五站",
         "军事事件不会直接改油价，它先改保险费和运费，再改到岸成本，最后才轮到调价窗口")

    gates = [
        ("海峡风险", "无人机、触雷、警报\n通航是否受影响", RED),
        ("保费与运费", "战争险加价\n油轮日租金跳涨", NAVY),
        ("到岸成本", "到港的每一桶油\n都比上周贵一点", NAVY),
        ("调价窗口", "十个工作日一调\n不足 50 元/吨不调", NAVY),
        ("加油机", "92 号汽油每升\n多几毛钱", RED),
    ]
    x = 80
    for i, (name, body, color) in enumerate(gates):
        box(d, x, 250, x + 280, 470)
        d.rounded_rectangle([x, 250, x + 280, 262], radius=4, fill=color)
        d.text((x + 28, 292), name, font=F(24, True), fill=color)
        para(d, (x + 28, 346), body, 19, DARK, maxw=224, lh=1.5)
        if i < 4:
            arrow_right(d, x + 292, x + 352, 360)
        x += 340

    box(d, 80, 530, 1720, 660, fill="white", outline=RED, width=2)
    d.text((112, 556), "粗算一笔", font=F(21, True), fill=RED)
    d.text((112, 596), "原油涨 10%　→　92 号汽油约涨 6%—7%　→　一箱 50 升多花二三十块",
           font=F(24, True), fill=DARK)

    para(d, (80, 700), "前面几站都发生在你看见价格之前：保费、运费、期货与掉期。"
                       "你能感到的，只有最后一站。",
         21, GRAY, maxw=1600, lh=1.55)

    footer(d, "调价机制见《石油价格管理办法》（十个工作日一调、每吨 50 元门槛）；“一箱多花二三十块”为按 92 号汽油现价与原油涨幅所做的粗算，非承诺。")
    img.save(OUT + "图3_从海峡到油箱.png", quality=95)
    return img


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("done")
