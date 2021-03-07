from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time
import os
import sys
from commands import *


def cmd_video_playing():
    return "adb shell am start -a android.intent.action.VIEW -d file:///sdcard/video.mp4 -t video/mp4"


curr_governor = sys.argv[2]
os.system(cmd_gov_set(0, curr_governor))
os.system(cmd_gov_set(7, curr_governor))


device = MonkeyRunner.waitForConnection()

test_count = int(sys.argv[1])

for test_i in range(test_count):
    MonkeyRunner.sleep(4)
    os.system(cmd_reset(0))
    os.system(cmd_reset(7))
    os.system(cmd_battery_stats_reset())
    os.system(cmd_video_playing())
    MonkeyRunner.sleep(925)
    os.system(cmd_dump_time(0, test_i))
    os.system(cmd_dump_time(7, test_i))
    os.system(cmd_dump_trans(0, test_i))
    os.system(cmd_dump_trans(7, test_i))

    os.system(cmd_battery_stats_dump(package, test_i))
