from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time
import os
import sys
from commands import *

curr_governor = sys.argv[2]
os.system(cmd_gov_set(0, curr_governor))
os.system(cmd_gov_set(7, curr_governor))

device = MonkeyRunner.waitForConnection()

device.installPackage("apk/com-dotgears-flappybird.apk")

package = "com.dotgears.flappybird"

activity = "com.dotgears.flappy.SplashScreen"

runComponent = package + "/" + activity

w = int(device.getProperty("display.width"))
h = int(device.getProperty("display.height"))

time_limit = 900

folder_name = curr_governor + "/test_flappy_bird"

test_count = int(sys.argv[1])

for test_i in range(test_count):

    MonkeyRunner.sleep(4)

    os.system(cmd_reset(0))
    os.system(cmd_reset(7))
    os.system(cmd_battery_stats_reset())

    os.system(cmd_gfxinfo_reset())

    device.startActivity(component=runComponent)
    MonkeyRunner.sleep(5)
    device.touch(w/4, h/1.48039, "DOWN_AND_UP")

    start_sec = time.time()
    current_sec = time.time()

    while current_sec - start_sec < time_limit:
        device.touch(w/4, h/1.48039, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.6)
        current_sec = time.time()

    os.system(cmd_gfxinfo_dump(package, test_i, folder_name))
    os.system(cmd_dump_time(0, test_i, folder_name))
    os.system(cmd_dump_time(7, test_i, folder_name))
    os.system(cmd_dump_trans(0, test_i, folder_name))
    os.system(cmd_dump_trans(7, test_i, folder_name))

    os.system(cmd_battery_stats_dump(package, test_i, folder_name))

    device.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
    kill_command = 'am force-stop %s' % package
    device.shell(kill_command)

