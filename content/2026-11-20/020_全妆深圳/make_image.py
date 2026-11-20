# -*- coding: utf-8 -*-
"""
《深圳的全妆，和小说里没有的 A 市》配图
绘制说明：本图为程序绘制示意图，不是照片。
  天际线按深圳福田 CBD 一带的地标实际高度比例排布：
    平安金融中心 599 米（画面主塔，最高）
    京基 100    约 442 米
    中国华润大厦（“春笋”）约 392.5 米
    地王大厦    约 384 米（顶部双天线）
  其余为程式生成的示意楼群，不对应具体建筑。
输出：脚本所在目录下 深圳夜景.png
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon

rng = np.random.default_rng(20261120)

W, H, DPI = 16, 9, 150
WATER = 168
SKY_TOP = np.array([7, 11, 21])
SKY_MID = np.array([21, 32, 52])
SKY_HOR = np.array([92, 68, 58])
C_FAR, C_MID, C_NEAR = "#1a2536", "#111c2b", "#070d16"
C_WATER = "#04080e"
WIN_A, WIN_B = "#f7e2ab", "#cfe0f5"

OUT = os.path.dirname(os.path.abspath(__file__)) + os.sep

fig = plt.figure(figsize=(W, H), dpi=DPI)
fig.patch.set_facecolor(C_WATER)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 1600)
ax.set_ylim(0, 900)
ax.axis("off")


# ---------------------------------------------------------------- 天空
grad = np.zeros((320, 1, 3))
for i in range(320):
    t = i / 319.0                       # 0 = 地平线，1 = 天顶
    if t < 0.55:
        c = SKY_HOR + (SKY_MID - SKY_HOR) * (t / 0.55)
    else:
        c = SKY_MID + (SKY_TOP - SKY_MID) * ((t - 0.55) / 0.45)
    grad[i, 0, :] = c / 255.0
ax.imshow(grad, extent=[0, 1600, WATER, 900], aspect="auto", zorder=0,
          interpolation="bicubic")

# 地平线暖辉
for i, a in enumerate(np.linspace(0.55, 0.0, 40)):
    ax.add_patch(Rectangle((0, WATER + i * 5.5), 1600, 6,
                           facecolor="#d59a5c", alpha=a * 0.16,
                           edgecolor="none", zorder=1))

# 星点
n = 110
ax.scatter(rng.uniform(0, 1600, n), rng.uniform(600, 890, n),
           s=rng.uniform(0.3, 1.8, n), color="#e8eefb",
           alpha=rng.uniform(0.12, 0.5, n), zorder=2, linewidths=0)


# ---------------------------------------------------------------- 工具
def window_lights(x, w, top, density, z, s=1.5, cool=0.25):
    if w < 8:
        return
    cols = max(2, int(w / 7.0))
    rows = max(2, int((top - WATER) / 10.0))
    gx = np.linspace(x + 3, x + w - 3, cols)
    gy = np.linspace(WATER + 6, top - 8, min(rows, 80))
    X, Y = np.meshgrid(gx, gy)
    X, Y = X.ravel(), Y.ravel()
    k = rng.random(X.size) < density
    X, Y = X[k], Y[k]
    if X.size == 0:
        return
    cold = rng.random(X.size) < cool
    if cold.sum() > 0:
        ax.scatter(X[cold], Y[cold], s=s, marker="s", color=WIN_B,
                   alpha=rng.uniform(0.15, 0.55, cold.sum()), zorder=z,
                   linewidths=0)
    if (~cold).sum() > 0:
        ax.scatter(X[~cold], Y[~cold], s=s, marker="s", color=WIN_A,
                   alpha=rng.uniform(0.2, 0.8, (~cold).sum()), zorder=z,
                   linewidths=0)


def rect(x, w, top, color, z, dens, mirror=True, s=1.5):
    ax.add_patch(Rectangle((x, WATER), w, top - WATER, facecolor=color,
                           edgecolor="none", zorder=z))
    window_lights(x, w, top, dens, z + 3, s=s)


def poly(pts, color, z):


# ---------------------------------------------------------------- 远层
x = -40
while x < 1640:
    w = rng.uniform(24, 54)
    rect(x, w, WATER + rng.uniform(150, 330), C_FAR, 10, 0.13, mirror=False)
    x += w + rng.uniform(4, 16)

ax.add_patch(Rectangle((0, WATER + 60), 1600, 150, facecolor="#2c3a4e",
                       alpha=0.10, edgecolor="none", zorder=12))

# ---------------------------------------------------------------- 中层
x = -30
while x < 1640:
    w = rng.uniform(28, 62)
    rect(x, w, WATER + rng.uniform(230, 470), C_MID, 16, 0.20, mirror=False)
    x += w + rng.uniform(10, 30)

ax.add_patch(Rectangle((0, WATER), 1600, 120, facecolor="#3a4a60",
                       alpha=0.10, edgecolor="none", zorder=18))

# ---------------------------------------------------------------- 近层地标
# 地王大厦：双天线
lx, lw, top = 452, 56, WATER + 420
rect(lx, lw, top, C_NEAR, 22, 0.26)
for dx in (13, 37):
    ax.plot([lx + dx, lx + dx], [top - 4, top + 96], color=C_NEAR,
            linewidth=2.2, zorder=22, solid_capstyle="butt")
    ax.plot([lx + dx, lx + dx], [WATER - 44, WATER - 2], color="#6f92c0",
            alpha=0.055, linewidth=2.2, zorder=6)

# 京基 100：收分 + 弧形肩部
lx, lw, top = 566, 66, WATER + 500
shoulder = WATER + 462
poly([[lx, WATER], [lx + lw, WATER], [lx + lw - 4, shoulder],
      [lx + lw * 0.72, top - 12], [lx + lw * 0.5, top],
      [lx + lw * 0.28, top - 12], [lx + 4, shoulder]], C_NEAR, 22)
window_lights(lx + 2, lw - 4, shoulder - 6, 0.26, 25)

# 平安金融中心：主塔
lx, lw, top = 726, 84, WATER + 620
bod_top = top - 26
poly([[lx, WATER], [lx + lw, WATER], [lx + lw - 5, bod_top],
      [lx + 5, bod_top]], C_NEAR, 22)
# 塔冠
poly([[lx + 5, bod_top], [lx + lw - 5, bod_top],
      [lx + lw * 0.5 + 9, top + 30], [lx + lw * 0.5 - 9, top + 30]],
     C_NEAR, 22)
# 天线与航空障碍灯
ax.plot([lx + lw / 2, lx + lw / 2], [top + 28, top + 92], color=C_NEAR,
        linewidth=3.0, zorder=22, solid_capstyle="butt")
ax.plot([lx + lw / 2, lx + lw / 2], [WATER - 44, WATER - 2], color="#6f92c0",
        alpha=0.055, linewidth=3.0, zorder=6)
ax.add_patch(Rectangle((lx + lw / 2 - 2.4, top + 90), 4.8, 8,
                       facecolor="#ef4a32", edgecolor="none", zorder=24))
window_lights(lx + 2, lw - 4, bod_top - 8, 0.34, 25, s=1.7, cool=0.15)
# 灯光秀：竖向冷光带
for k in range(4):
    gx = lx + 14 + k * 16
    ax.add_patch(Rectangle((gx, WATER + 16), 2.6, (bod_top - WATER) - 26,
                           facecolor="#7fb0ec", alpha=0.13, edgecolor="none",
                           zorder=27))
ax.add_patch(Polygon([[lx, WATER], [lx + lw, WATER], [lx + lw - 5, bod_top],
                      [lx + 5, bod_top]], closed=True, facecolor="#9cc2f2",
                     alpha=0.05, edgecolor="none", zorder=26))

# 中国华润大厦“春笋”：底部满宽，向上收成尖
lx, lw, top = 862, 64, WATER + 452
t = np.linspace(0, 1, 90)
hw = (lw / 2) * (1 - t ** 2.6) ** 0.62
ys = WATER + (top - WATER) * t
left = np.column_stack([lx + lw / 2 - hw, ys])
right = np.column_stack([lx + lw / 2 + hw, ys])
poly(np.vstack([left, right[::-1]]), C_NEAR, 22)
window_lights(lx + 8, lw - 16, top - 60, 0.22, 25)

# ---------------------------------------------------------------- 其余近层楼
occupied = [(452, 56), (566, 66), (726, 84), (862, 64)]
x = -14
while x < 1640:
    w = rng.uniform(32, 70)
    if any(not (x + w < a - 8 or x > a + b + 8) for a, b in occupied):
        x += w + 8
        continue
    rect(x, w, WATER + rng.uniform(200, 400), C_NEAR, 20, 0.24)
    x += w + rng.uniform(8, 24)

# ---------------------------------------------------------------- 水面
ax.add_patch(Rectangle((0, 0), 1600, WATER, facecolor=C_WATER,
                       edgecolor="none", zorder=5))
for k in range(1, 18):
    y = WATER - k * 9.5
    ax.plot([0, 1600], [y, y], color="#31506f",
            alpha=0.02 + 0.025 * ((k * 7) % 5) / 4.0, linewidth=1.0, zorder=7)
ax.plot([0, 1600], [WATER, WATER], color="#4a6a8c", alpha=0.30,
        linewidth=1.4, zorder=8)
# 水面灯带
for k in range(26):
    gx = rng.uniform(0, 1600)
    gw = rng.uniform(6, 34)
    ax.plot([gx, gx + gw], [WATER - rng.uniform(6, 90)] * 2, color=WIN_A,
            alpha=rng.uniform(0.02, 0.07), linewidth=rng.uniform(1.5, 3.5),
            zorder=9)

fig.savefig(OUT + "深圳夜景.png", dpi=DPI, facecolor=C_WATER)
print("saved:", OUT + "深圳夜景.png")