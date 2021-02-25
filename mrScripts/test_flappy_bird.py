from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time


device = MonkeyRunner.waitForConnection()

device.installPackage("apk/com-dotgears-flappybird.apk")

package = "com.dotgears.flappybird"

activity = "com.dotgears.flappy.SplashScreen"

runComponent = package + "/" + activity

device.startActivity(component=runComponent)
MonkeyRunner.sleep(3)

device.touch(270, 1530, "DOWN_AND_UP")

start_sec = time.time()
current_sec = time.time()
while current_sec - start_sec < 1500:
    device.touch(270, 1530, "DOWN_AND_UP")
    MonkeyRunner.sleep(0.6)
    current_sec = time.time()
