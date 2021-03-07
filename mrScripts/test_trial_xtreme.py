from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time
import os
import sys
from commands import *

curr_governor = sys.argv[2]
os.system(cmd_gov_set(0, curr_governor))
os.system(cmd_gov_set(7, curr_governor))

device = MonkeyRunner.waitForConnection()

device.installPackage("apk/trial_xtreme_3_-1469689232-www.androeed.ru___.apk")

package = "com.x3m.tx3"

activity = "com.prime31.UnityPlayerProxyActivity"

runComponent = package + "/" + activity

w = int(device.getProperty("display.width"))
h = int(device.getProperty("display.height"))

test_count = int(sys.argv[1])

for test_i in range(test_count):

    MonkeyRunner.sleep(4)

    os.system(cmd_reset(0))
    os.system(cmd_reset(7))
    os.system(cmd_battery_stats_reset())

    device.startActivity(component=runComponent)
    MonkeyRunner.sleep(3)
    start_sec = time.time()
    current_sec = time.time()

    # play button
    device.touch(h/1.12129, w/1.18033, "DOWN_AND_UP")
    MonkeyRunner.sleep(3)
    # select location
    device.touch(h/2.83125, w/2.07692, "DOWN_AND_UP")
    MonkeyRunner.sleep(3)
    # select bike
    device.touch(h/1.1325, w/1.18681, "DOWN_AND_UP")
    MonkeyRunner.sleep(3)
    # select level
    device.touch(h/2.22059, w/3.6, "DOWN_AND_UP")
    MonkeyRunner.sleep(1.5)
    # start
    device.touch(h/1.1325, w/1.18681, "DOWN_AND_UP")
    MonkeyRunner.sleep(5)
    # play
    while current_sec - start_sec < 900:
        device.touch(h/1.1325, w/1.18681, MonkeyDevice.DOWN)
        MonkeyRunner.sleep(10)
        device.touch(h/1.1325, w/1.18681, MonkeyDevice.UP)
        # restart
        device.touch(h/1.48039, w/1.18681, "DOWN_AND_UP")
        MonkeyRunner.sleep(3)
        current_sec = time.time()

    os.system(cmd_dump_time(0, test_i))
    os.system(cmd_dump_time(7, test_i))
    os.system(cmd_dump_trans(0, test_i))
    os.system(cmd_dump_trans(7, test_i))

    os.system(cmd_battery_stats_dump(package, test_i))

    device.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
    kill_command = 'am force-stop %s' % package
    device.shell(kill_command)
