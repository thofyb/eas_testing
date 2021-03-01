from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time


device = MonkeyRunner.waitForConnection()

device.installPackage("apk/wolframalpha_v1.4.11.2019072303.apk")

package = "com.wolfram.android.alpha"

activity = "com.wolfram.android.alpha.activity.SplashScreenActivity"

runComponent = package + "/" + activity

device.startActivity(component=runComponent)
MonkeyRunner.sleep(3)

device.touch(800, 360, MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(0.1)

for i in range(0, 25):
    device.press("KEYCODE_DEL", MonkeyDevice.DOWN_AND_UP)


device.touch(200, 200, MonkeyDevice.DOWN_AND_UP)

# FT e^(-2*pi*t^2) sin(t)
start_sec = time.time()
current_sec = time.time()
while current_sec - start_sec < 1500:
    # UP
    device.touch(70, 2090, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(0.1)
    # UP
    device.touch(70, 2090, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(0.1)
    # F
    device.touch(420, 1950, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(0.1)
    # T
    device.touch(495, 1780, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(0.1)
    # UP
    device.touch(70, 2090, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(0.1)
    # SPACE
    device.touch(530, 2230, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(0.1)
    # e
    device.touch(270, 1770, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(0.1)
    # ^
    device.touch(470, 1300, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(0.1)
    # (
    device.touch(700, 1305, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(0.1)
    # -
    device.touch(165, 1305, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(0.1)
    # 2
    device.touch(165, 1455, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(0.1)
    # *
    device.touch(265, 1305, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(0.1)
    # p
    device.touch(1030, 1795, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(0.1)
    # i
    device.touch(805, 1790, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(0.1)
    # *
    device.touch(265, 1305, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(0.1)
    # t
    device.touch(495, 1780, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(0.1)
    # ^
    device.touch(470, 1305, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(0.1)
    # 2
    device.touch(165, 1455, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(0.1)
    # )
    device.touch(805, 1305, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(0.1)
    # SPACE
    device.touch(530, 2230, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(0.1)
    # s
    device.touch(215, 1965, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(0.1)
    # i
    device.touch(805, 1790, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(0.1)
    # n
    device.touch(745, 2100, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(0.1)
    # (
    device.touch(700, 1305, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(0.1)
    # t
    device.touch(495, 1780, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(0.1)
    # )
    device.touch(805, 1305, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(0.1)

    device.press("KEYCODE_ENTER", MonkeyDevice.DOWN_AND_UP)

    MonkeyRunner.sleep(15)

    device.touch(800, 360, MonkeyDevice.DOWN_AND_UP)
    MonkeyRunner.sleep(0.1)

    for i in range(0, 25):
        device.press("KEYCODE_DEL", MonkeyDevice.DOWN_AND_UP)
    current_sec = time.time()
