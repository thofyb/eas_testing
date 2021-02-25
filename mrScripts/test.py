from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time


device = MonkeyRunner.waitForConnection()

device.installPackage("apks/Notes_v2.3.3_apkpure.com.apk")

package = "com.ogden.memo"

activity = "com.ogden.memo.ui.MemoMain"

runComponent = package + "/" + activity

device.startActivity(component=runComponent)
MonkeyRunner.sleep(3)

print("new note...")
device.touch(1000, 170, "DOWN_AND_UP")

start_sec = time.time()
current_sec = time.time()
while current_sec - start_sec < 1500:
    device.type("UTvjfEMLXa")
    current_sec = time.time()
