# Author:    Airmole
# weibo:     https://weibo.com/2423156830
# GitHub:    https://github.com/Airmole
# Mail:      admin@airmole.cn

# Created at 2020年3月21日

import pygame
import time
import curses
from pathlib import Path
import convert

# video and bgm path
VIDEO_PATH = "ustb.mp4"

# frame rate of video
FRAME_RATE = 1 / 25


if Path("video_data.py").exists():
    from video_data import video_data
else:
    if not Path(VIDEO_PATH).exists():
        print("视频不存在: ", VIDEO_PATH)
    video_data = convert.write(VIDEO_PATH)
    input("\n转换完成, 按任意键继续...")

count = 0

stdsrc = curses.initscr()
curses.start_color()
stdsrc.resize(90, 300)

time.sleep(0.4)
now = time.time()

for frame_data in video_data:
    for i in range(len(frame_data)):
        stdsrc.addstr(i, 0, frame_data[i], curses.COLOR_WHITE)
    while time.time() - now < count * FRAME_RATE:
        time.sleep(count * FRAME_RATE - time.time() + now)
    stdsrc.refresh()
    count += 1

curses.endwin()
