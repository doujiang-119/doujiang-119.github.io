# -*- coding: utf-8 -*-
"""提取每张图中的点缀色（高饱和像素聚类），用于确认强调色色号。"""
from PIL import Image
from collections import Counter
import colorsys, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

IMAGES = [
    ("01-3Webb", r"C:\Users\Administrator\.workbuddy\clipboard-images\clipboard-2026-10-17T08-43-16-153Z-50b17000.jpg"),
    ("02-Maggie", r"D:\Documents\xwechat_files\wxid_xze69ec8502c22_0e60\temp\RWTemp\2026-10\d1e3bc2d56718c50318a9939b193e8c4.png"),
    ("03-章节卡片", r"D:\Documents\xwechat_files\wxid_xze69ec8502c22_0e60\temp\RWTemp\2026-10\83cb6da4e61558d521db4beaecbabdb9.jpg"),
    ("04-全球足迹", r"D:\Documents\xwechat_files\wxid_xze69ec8502c22_0e60\temp\RWTemp\2026-10\8f9684402fc9963938438d332395882d.jpg"),
    ("05-小红书成果", r"D:\Documents\xwechat_files\wxid_xze69ec8502c22_0e60\temp\RWTemp\2026-10\d6268d5b82e815805302758b28232651.jpg"),
    ("06-Nonsense评价区", r"D:\Documents\xwechat_files\wxid_xze69ec8502c22_0e60\temp\RWTemp\2026-10\2ae3a2a9a69821df44f1e3ee971ee078.jpg"),
]

def hx(c):
    return "#{:02X}{:02X}{:02X}".format(*c[:3])

for name, path in IMAGES:
    img = Image.open(path).convert("RGB")
    img.thumbnail((300, 300))
    sat_pixels = []
    for p in img.get_flattened_data() if hasattr(img, "get_flattened_data") else img.getdata():
        r, g, b = p
        h, l, s = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
        if s > 0.42 and 0.18 < l < 0.72:  # 有明显彩色且不太暗不太亮
            sat_pixels.append(p)
    if not sat_pixels:
        print(f"== {name}: 无高饱和点缀色")
        continue
    cnt = Counter(sat_pixels)
    total = len(sat_pixels)
    top = cnt.most_common(6)
    print(f"== {name}  高饱和像素 {total} 个")
    print("   ", "  ".join(f"{hx(c)}({round(v*100.0/total)}%)" for c, v in top))
