# -*- coding: utf-8 -*-
"""采样截图的背景色 / 主色 / 点缀色，输出十六进制色号。仅用于版式学习。"""
from PIL import Image
from collections import Counter
import sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

IMAGES = [
    ("01-3Webb首屏", r"C:\Users\Administrator\.workbuddy\clipboard-images\clipboard-2026-10-17T08-43-16-153Z-50b17000.jpg"),
    ("02-Maggie首屏", r"D:\Documents\xwechat_files\wxid_xze69ec8502c22_0e60\temp\RWTemp\2026-10\d1e3bc2d56718c50318a9939b193e8c4.png"),
    ("03-章节卡片", r"D:\Documents\xwechat_files\wxid_xze69ec8502c22_0e60\temp\RWTemp\2026-10\83cb6da4e61558d521db4beaecbabdb9.jpg"),
    ("04-全球足迹", r"D:\Documents\xwechat_files\wxid_xze69ec8502c22_0e60\temp\RWTemp\2026-10\8f9684402fc9963938438d332395882d.jpg"),
    ("05-小红书成果", r"D:\Documents\xwechat_files\wxid_xze69ec8502c22_0e60\temp\RWTemp\2026-10\d6268d5b82e815805302758b28232651.jpg"),
    ("06-Nonsense评价区", r"D:\Documents\xwechat_files\wxid_xze69ec8502c22_0e60\temp\RWTemp\2026-10\2ae3a2a9a69821df44f1e3ee971ee078.jpg"),
    ("07-Nonsense首屏", r"D:\Documents\xwechat_files\wxid_xze69ec8502c22_0e60\temp\RWTemp\2026-10\a69a280e13f2b487d171fc6381a0f6a9.jpg"),
]

def hx(rgb):
    return "#{:02X}{:02X}{:02X}".format(*rgb[:3])

def quantize(img, n=8):
    small = img.convert("RGB").copy()
    small.thumbnail((160, 160))
    q = small.quantize(colors=n, method=Image.MEDIANCUT).convert("RGB")
    cnt = Counter(q.getdata())
    total = sum(cnt.values())
    return [(hx(c), round(v * 100.0 / total, 1)) for c, v in cnt.most_common(n)]

def point(img, fx, fy):
    w, h = img.size
    p = img.convert("RGB").getpixel((int(w * fx), int(h * fy)))
    return hx(p)

for name, path in IMAGES:
    try:
        img = Image.open(path)
    except Exception as e:
        print(f"== {name}: 读取失败 {e}")
        continue
    print(f"== {name}  ({img.size[0]}x{img.size[1]})")
    print("  主要颜色(量化占比): ", "  ".join(f"{c}({p}%)" for c, p in quantize(img)))
    # 采样关键位置: 左上角(背景) / 中左(背景/文字区) / 中心
    print(f"  左上角 {point(img,0.02,0.05)}   中左 {point(img,0.05,0.5)}   中心 {point(img,0.5,0.45)}   右上角 {point(img,0.97,0.05)}")
