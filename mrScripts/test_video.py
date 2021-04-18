from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time
import os
import sys
from commands import cmd_reset, cmd_gov_set, cmd_dump_time, cmd_battery_stats_reset, cmd_video_playing
from commands import cmd_gfxinfo_dump, cmd_battery_stats_dump, cmd_gfxinfo_reset

curr_governor = sys.argv[2]
os.system(cmd_gov_set(0, curr_governor))
os.system(cmd_gov_set(7, curr_governor))


device = MonkeyRunner.waitForConnection()

device.installPackage("apk/vlc.apk")

package = "org.videolan.vlc"

folder_name = curr_governor + "/test_video"

test_count = int(sys.argv[1])

time_limit = 925

for test_i in range(test_count):
    MonkeyRunner.sleep(4)
    os.system(cmd_reset(0))
    os.system(cmd_reset(7))
    os.system(cmd_battery_stats_reset())
    os.system(cmd_gfxinfo_reset())

    os.system(cmd_video_playing())

    MonkeyRunner.sleep(time_limit)

    os.system(cmd_dump_time(0, test_i, folder_name))
    os.system(cmd_dump_time(7, test_i, folder_name))
    os.system(cmd_dump_trans(0, test_i, folder_name))
    os.system(cmd_dump_trans(7, test_i, folder_name))
    os.system(cmd_gfxinfo_dump(package, test_i, folder_name))
    os.system(cmd_battery_stats_dump(package, test_i, folder_name))
