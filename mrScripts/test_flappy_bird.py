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

test_count = int(sys.argv[1])

for test_i in range(test_count):

    MonkeyRunner.sleep(4)

    os.system(cmd_reset(0))
    os.system(cmd_reset(7))
    os.system(cmd_battery_stats_reset())

    device.startActivity(component=runComponent)
    MonkeyRunner.sleep(5)
    device.touch(270, 1530, "DOWN_AND_UP")

    start_sec = time.time()
    current_sec = time.time()

    while current_sec - start_sec < 900:
        device.touch(270, 1530, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.6)
        current_sec = time.time()

    os.system(cmd_dump_time(0, test_i))
    os.system(cmd_dump_time(7, test_i))
    os.system(cmd_dump_trans(0, test_i))
    os.system(cmd_dump_trans(7, test_i))

    os.system(cmd_battery_stats_dump(package, test_i))

    device.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
    kill_command = 'am force-stop %s' % package
    device.shell(kill_command)
