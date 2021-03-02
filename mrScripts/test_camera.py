from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time


device = MonkeyRunner.waitForConnection()

device.installPackage("apk/Open_Camera_v1.48.1_apkpure.com.apk")

package = "net.sourceforge.opencamera"

activity = "net.sourceforge.opencamera.MainActivity"

runComponent = package + "/" + activity

device.startActivity(component=runComponent)
MonkeyRunner.sleep(5)

# 2255 770
device.touch(2240, 780, "DOWN_AND_UP")
MonkeyRunner.sleep(2)

# 2190 540
device.touch(2190, 540, "DOWN_AND_UP")
MonkeyRunner.sleep(1503)
device.touch(2190, 540, "DOWN_AND_UP")
