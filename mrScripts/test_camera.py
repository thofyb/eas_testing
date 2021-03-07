from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time
import os
import sys
from commands import *

curr_governor = sys.argv[2]
os.system(cmd_gov_set(0, curr_governor))
os.system(cmd_gov_set(7, curr_governor))

device = MonkeyRunner.waitForConnection()

device.installPackage("apk/Open_Camera_v1.48.1_apkpure.com.apk")

package = "net.sourceforge.opencamera"

activity = "net.sourceforge.opencamera.MainActivity"

runComponent = package + "/" + activity

test_count = int(sys.argv[1])

for test_i in range(test_count):

    MonkeyRunner.sleep(4)

    os.system(cmd_reset(0))
    os.system(cmd_reset(7))
    os.system(cmd_battery_stats_reset())

    device.startActivity(component=runComponent)
    MonkeyRunner.sleep(5)

    # 2255 770
    device.touch(h/1.01116, w/1.38462, "DOWN_AND_UP")
    MonkeyRunner.sleep(2)

    # 2190 540
    device.touch(h/1.03425, w/2, "DOWN_AND_UP")
    MonkeyRunner.sleep(903)
    device.touch(h/1.03425, w/2, "DOWN_AND_UP")

    os.system(cmd_dump_time(0, test_i))
    os.system(cmd_dump_time(7, test_i))
    os.system(cmd_dump_trans(0, test_i))
    os.system(cmd_dump_trans(7, test_i))

    os.system(cmd_battery_stats_dump(package, test_i))

    device.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
    kill_command = 'am force-stop %s' % package
    device.shell(kill_command)
