from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time
import os

device = MonkeyRunner.waitForConnection()

device.installPackage("apk/com-dotgears-flappybird.apk")

package = "com.dotgears.flappybird"

activity = "com.dotgears.flappy.SplashScreen"

cmd_reset = "adb shell dumpsys batterystats --reset"

cmd_dump = "adb shell dumpsys batterystats --charged com.dotgears.flappybird > res/batterystats.txt"

runComponent = package + "/" + activity

# os.system(cmd_reset)
MonkeyRunner.sleep(7)

device.startActivity(component=runComponent)
MonkeyRunner.sleep(3)
device.touch(270, 1530, "DOWN_AND_UP")

start_sec = time.time()
current_sec = time.time()
while current_sec - start_sec < 60:
    device.touch(270, 1530, "DOWN_AND_UP")
    MonkeyRunner.sleep(0.6)
    current_sec = time.time()

os.system(cmd_dump)
