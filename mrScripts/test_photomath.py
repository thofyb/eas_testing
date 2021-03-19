from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time
import os
import sys
from commands import *

curr_governor = sys.argv[2]
os.system(cmd_gov_set(0, curr_governor))
Ыos.system(cmd_gov_set(7, curr_governor))

device = MonkeyRunner.waitForConnection()

device.installPackage("apk/com.microblink.photomath_7.5.0_70000578.apk")

package = "com.microblink.photomath"

activity = "com.microblink.photomath.main.activity.LauncherActivity"

w = int(device.getProperty("display.width"))
h = int(device.getProperty("display.height"))

runComponent = package + "/" + activity

test_count = int(sys.argv[1])

for test_i in range(test_count):

    MonkeyRunner.sleep(4)
    os.system(cmd_gfxinfo_reset())

    os.system(cmd_reset(0))
    os.system(cmd_reset(7))
    os.system(cmd_battery_stats_reset())

    device.startActivity(component=runComponent)

    MonkeyRunner.sleep(3)

    start_sec = time.time()
    current_sec = time.time()

    device.touch(w/5, h/1.08, "DOWN_AND_UP")
    MonkeyRunner.sleep(1)

    while current_sec - start_sec < 900:
        # tools
        device.touch(w/12.7, h/1.51, "DOWN_AND_UP")
        MonkeyRunner.sleep(1)

        device.touch(w/10.8, h/1.21, MonkeyDevice.DOWN)
        MonkeyRunner.sleep(0.5)
        device.touch(w/4.32, h/1.21, MonkeyDevice.MOVE)
        MonkeyRunner.sleep(0.3)
        device.touch(w/4.32, h/1.21, MonkeyDevice.UP)
        MonkeyRunner.sleep(0.5)

        # ()/()
        device.touch(w/10.8, h/1.208, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # pi
        device.touch(w/10.8, h/1.011, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # ->
        device.touch(w/1.728, h/1.51, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # 6
        device.touch(w/1.342, h/1.208, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # ->
        device.touch(w/1.728, h/1.51, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # ->
        device.touch(w/1.728, h/1.51, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # ()/()
        device.touch(w/10.8, h/1.208, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # pi
        device.touch(w/10.8, h/1.011, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # ->
        device.touch(w/1.728, h/1.51, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # 3
        device.touch(w/1.342, h/1.10488, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # ->
        device.touch(w/1.728, h/1.51, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)
        # ->
        device.touch(w/1.728, h/1.51, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # 2
        device.touch(w/1.728, h/1.10488, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # tools
        device.touch(w/12.7, h/1.51, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.5)

        # sec
        device.touch(w/1.33, h/1.0157, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # x
        device.touch(w/3.92727, h/1.10488, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # ->
        device.touch(w/1.728, h/1.51, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # -
        device.touch(w/1.10769, h/1.10488, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # 8
        device.touch(w/1.728, h/1.34421, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # tools
        device.touch(w/12.7, h/1.51, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # csc
        device.touch(w/1.10769, h/1.0157, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # x
        device.touch(w/3.92727, h/1.10488, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # ->
        device.touch(w/1.728, h/1.51, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # tools
        device.touch(w/12.7, h/1.51, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.5)

        # cot
        device.touch(w/1.10769, h/1.10488, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # x
        device.touch(w/3.92727, h/1.10488, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # ->
        device.touch(w/1.728, h/1.51, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # ->
        device.touch(w/1.728, h/1.51, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # x
        device.touch(w/3.92727, h/1.10488, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.3)

        # show solution
        device.touch(w/2.05714, h/1.7695, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.5)

        # show steps
        device.touch(w/2.03774, h/1.33235, "DOWN_AND_UP")
        MonkeyRunner.sleep(1)

        # back
        device.touch(w/13.5, h/12.24324, "DOWN_AND_UP")
        MonkeyRunner.sleep(1)

        # back again
        device.touch(w/1.2, h/2.83125, "DOWN_AND_UP")
        MonkeyRunner.sleep(1)

        # delete formula
        device.touch(w/1.09645, h/6.66176, "DOWN_AND_UP")
        MonkeyRunner.sleep(1)
        current_sec = time.time()

    os.system(cmd_dump_time(0, test_i))
    os.system(cmd_dump_time(7, test_i))
    os.system(cmd_dump_trans(0, test_i))
    os.system(cmd_dump_trans(7, test_i))
    os.system(cmd_gfxinfo_dump(package, test_i))

    os.system(cmd_battery_stats_dump(package, test_i))

    device.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
    kill_command = 'am force-stop %s' % package
    device.shell(kill_command)
