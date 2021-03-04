from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time
import os
import sys
from commands import *

curr_governor = sys.argv[2]
os.system(cmd_gov_set(0, curr_governor))
os.system(cmd_gov_set(7, curr_governor))

device = MonkeyRunner.waitForConnection()

device.installPackage("apk/com.microblink.photomath_7.5.0_70000578.apk")

package = "com.microblink.photomath"

activity = "com.microblink.photomath.main.activity.LauncherActivity"


runComponent = package + "/" + activity

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

    device.touch(215, 2105, "DOWN_AND_UP")
    MonkeyRunner.sleep(1)

    while current_sec - start_sec < 60:
        # tools
        device.touch(85, 1500, "DOWN_AND_UP")
        MonkeyRunner.sleep(1)

        device.touch(100, 1870, MonkeyDevice.DOWN)
        MonkeyRunner.sleep(0.5)
        device.touch(250, 1885, MonkeyDevice.MOVE)
        MonkeyRunner.sleep(0.3)
        device.touch(250, 1885, MonkeyDevice.UP)
        MonkeyRunner.sleep(0.5)

        # ()/()
        device.touch(100, 1875, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # pi
        device.touch(100, 2240, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # ->
        device.touch(625, 1500, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # 6
        device.touch(805, 1875, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # ->
        device.touch(625, 1500, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # ->
        device.touch(625, 1500, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # ()/()
        device.touch(100, 1875, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # pi
        device.touch(100, 2240, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # ->
        device.touch(625, 1500, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # 3
        device.touch(805, 2050, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # ->
        device.touch(625, 1500, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)
        # ->
        device.touch(625, 1500, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # 2
        device.touch(625, 2050, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # tools
        device.touch(85, 1500, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.5)

        # sec
        device.touch(810, 2230, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # x
        device.touch(275, 2050, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # ->
        device.touch(625, 1500, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # -
        device.touch(975, 2050, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # 8
        device.touch(625, 1685, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # tools
        device.touch(85, 1500, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # csc
        device.touch(975, 2245, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # x
        device.touch(275, 2050, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # ->
        device.touch(625, 1500, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # tools
        device.touch(85, 1500, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.5)

        # cot
        device.touch(975, 2050, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # x
        device.touch(275, 2050, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # ->
        device.touch(625, 1500, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # ->
        device.touch(625, 1500, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # x
        device.touch(275, 2050, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # show solution
        device.touch(525, 1280, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.5)

        # show steps
        device.touch(530, 1700, "DOWN_AND_UP")
        MonkeyRunner.sleep(1)

        # back
        device.touch(80, 180, "DOWN_AND_UP")
        MonkeyRunner.sleep(1)

        # back again
        device.touch(900, 800, "DOWN_AND_UP")
        MonkeyRunner.sleep(1)

        # delete formula
        device.touch(985, 340, "DOWN_AND_UP")
        MonkeyRunner.sleep(1)
        current_sec = time.time()

    os.system(cmd_dump_time(0, test_i))
    os.system(cmd_dump_time(7, test_i))
    os.system(cmd_dump_trans(0, test_i))
    os.system(cmd_dump_trans(7, test_i))

    os.system(cmd_battery_stats_dump(package, test_i))

    device.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
    kill_command = 'am force-stop %s' % package
    device.shell(kill_command)
