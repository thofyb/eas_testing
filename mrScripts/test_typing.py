from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time
import os
import sys
from commands import *

curr_governor = sys.argv[2]
os.system(cmd_gov_set(0, curr_governor))
os.system(cmd_gov_set(7, curr_governor))

device = MonkeyRunner.waitForConnection()

device.installPackage("apk/Notes_v2.3.3_apkpure.com.apk")

package = "com.ogden.memo"

activity = "com.ogden.memo.ui.MemoMain"

runComponent = package + "/" + activity

w = int(device.getProperty("display.width"))
h = int(device.getProperty("display.height"))

folder_name = curr_governor + "/test_typing"

test_count = int(sys.argv[1])

time_limit = 900

for test_i in range(test_count):

    MonkeyRunner.sleep(4)
    os.system(cmd_reset(0))
    os.system(cmd_reset(7))
    os.system(cmd_battery_stats_reset())

    os.system(cmd_gfxinfo_reset())
    device.startActivity(component=runComponent)
    MonkeyRunner.sleep(3)

    device.touch(w/1.08, h/13.32353, "DOWN_AND_UP")

    start_sec = time.time()
    current_sec = time.time()
    while current_sec - start_sec < time_limit:
        device.type("UTvjfEMLXa")
        current_sec = time.time()
        os.system(cmd_dump_time(0, test_i, folder_name))
        os.system(cmd_dump_time(7, test_i, folder_name))
        os.system(cmd_dump_trans(0, test_i, folder_name))
        os.system(cmd_dump_trans(7, test_i, folder_name))
        os.system(cmd_gfxinfo_dump(package, test_i, folder_name))

        os.system(cmd_battery_stats_dump(package, test_i))

    device.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
    kill_command = 'am force-stop %s' % package
    device.shell(kill_command)
