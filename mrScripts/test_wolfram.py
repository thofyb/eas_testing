from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time


device = MonkeyRunner.waitForConnection()

device.installPackage("apk/wolframalpha_v1.4.11.2019072303.apk")

package = "com.wolfram.android.alpha"

activity = "com.wolfram.android.alpha.activity.SplashScreenActivity"

runComponent = package + "/" + activity

device.startActivity(component=runComponent)
MonkeyRunner.sleep(3)

device.touch(200, 200, MonkeyDevice.DOWN_AND_UP)

device.type("Fourier transform e^(-2*pi*t^2) sin(t)")
print("typed")
device.press("KEYCODE_ENTER", MonkeyDevice.DOWN_AND_UP)
