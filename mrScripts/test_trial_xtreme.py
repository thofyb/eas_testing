from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time


device = MonkeyRunner.waitForConnection()

device.installPackage("apk/trial_xtreme_3_-1469689232-www.androeed.ru___.apk")

package = "com.x3m.tx3"

activity = "com.prime31.UnityPlayerProxyActivity"

runComponent = package + "/" + activity

device.startActivity(component=runComponent)
MonkeyRunner.sleep(3)
start_sec = time.time()
current_sec = time.time()

# play button
device.touch(2020, 915, "DOWN_AND_UP")
MonkeyRunner.sleep(3)
# select location
device.touch(800, 520, "DOWN_AND_UP")
MonkeyRunner.sleep(3)
# select bike
device.touch(2000, 970, "DOWN_AND_UP")
MonkeyRunner.sleep(3)
# select level
device.touch(1020, 300, "DOWN_AND_UP")
MonkeyRunner.sleep(1.5)
# start
device.touch(2000, 910, "DOWN_AND_UP")
MonkeyRunner.sleep(5)
# play
while current_sec - start_sec < 1500:
    device.touch(2000, 910, MonkeyDevice.DOWN)
    MonkeyRunner.sleep(10)
    device.touch(2000, 910, MonkeyDevice.UP)
    # restart
    device.touch(1530, 910, "DOWN_AND_UP")
    MonkeyRunner.sleep(3)
    current_sec = time.time()
