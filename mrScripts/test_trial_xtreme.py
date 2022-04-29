from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time
import os
import sys
import subprocess

device = MonkeyRunner.waitForConnection()
package = "com.x3m.tx3"
activity = "com.prime31.UnityPlayerProxyActivity"
runComponent = package + "/" + activity

w = int(device.getProperty("display.width"))
h = int(device.getProperty("display.height"))

test_count = 10
print("test count: " + str(test_count))
time_limit = 180
print("time limit: " + str(time_limit))
warmup_time = 60

big_power_profie = {
    2001000: 409.51,
    1961000: 396.05,
    1927000: 384.10,
    1897000: 365.00,
    1868000: 340.66,
    1838000: 249.74,
    1809000: 230.72,
    1779000: 210.44,
    1750000: 157.17,
    1617000: 116.49,
    1484000: 90.90,
    1351000: 72.98,
    1218000: 66.10,
    1085000: 58.18,
     979000: 53.36,
     900000: 50.38
}

little_power_profie = {
    1500000: 94.42,
    1429000: 84.73,
    1367000: 73.16,
    1314000: 60.33,
    1261000: 56.65,
    1208000: 50.23,
    1155000: 45.77,
    1102000: 43.55,
    1050000: 39.42,
     948000: 37.46,
     846000: 35.99,
     745000: 34.29,
     643000: 33.34,
     542000: 30.66,
     501000: 30.07,
     400000: 27.94
}

big_cons = []
little_cons = []

for test_i in range(test_count):
    MonkeyRunner.sleep(4)
    device.startActivity(component=runComponent)
    MonkeyRunner.sleep(5)

    # play button
    device.touch(h/1.12129, w/1.18033, "DOWN_AND_UP")
    MonkeyRunner.sleep(3)
    # select location 511 347
    device.touch(h/2.83125, w/2.07692, "DOWN_AND_UP")
    # device.touch(500, 170, "DOWN_AND_UP")
    MonkeyRunner.sleep(3)
    # select bike 1279 607
    device.touch(1384, 658, "DOWN_AND_UP")
    MonkeyRunner.sleep(3)
    # select level
    device.touch(470, 200, "DOWN_AND_UP")
    MonkeyRunner.sleep(1.5)
    # start
    device.touch(1389, 610, "DOWN_AND_UP")
    MonkeyRunner.sleep(5)

    proc = subprocess.Popen(["adb shell cat /sys/devices/system/cpu/cpu0/cpufreq/stats/time_in_state"], stdout=subprocess.PIPE, shell=True)
    (out1, err2) = proc.communicate()
    proc = subprocess.Popen(["adb shell cat /sys/devices/system/cpu/cpu4/cpufreq/stats/time_in_state"], stdout=subprocess.PIPE, shell=True)
    (out2, err2) = proc.communicate()

    stats = out1.splitlines()
    ints_list = []
    bigCoreStat = dict()
    for row in stats:
        ints_list = map(int, row.split(' '))
        bigCoreStat[ints_list[0]] = ints_list[1]

    stats = out2.splitlines()
    littleCoreStat = dict()
    for row in stats:
        ints_list = map(int, row.split(' '))
        littleCoreStat[ints_list[0]] = ints_list[1]

    start_sec = time.time()
    current_sec = time.time()
    # play
    while current_sec - start_sec < time_limit:
        device.touch(1389, 610, MonkeyDevice.DOWN)
        MonkeyRunner.sleep(10)
        device.touch(1389, 610,  MonkeyDevice.UP)
        # restart 979 606
        device.touch(h/1.48039, w/1.18681, "DOWN_AND_UP")
        device.touch(1460, 60, "DOWN_AND_UP")
        MonkeyRunner.sleep(3)
        current_sec = time.time()

    proc = subprocess.Popen(["adb shell cat /sys/devices/system/cpu/cpu0/cpufreq/stats/time_in_state"], stdout=subprocess.PIPE, shell=True)
    (out1, err1) = proc.communicate()
    proc = subprocess.Popen(["adb shell cat /sys/devices/system/cpu/cpu4/cpufreq/stats/time_in_state"], stdout=subprocess.PIPE, shell=True)
    (out2, err2) = proc.communicate()

    stats = out1.splitlines()
    for row in stats:
        ints_list = map(int, row.split(' '))
        bigCoreStat[ints_list[0]] = ints_list[1] - bigCoreStat[ints_list[0]]

    stats = out2.splitlines()
    for row in stats:
        ints_list = map(int, row.split(' '))
        littleCoreStat[ints_list[0]] = ints_list[1] - littleCoreStat[ints_list[0]]

    big_consumption = 0.0
    for freq in bigCoreStat:
        big_consumption += bigCoreStat[freq] * big_power_profie[freq]
    big_consumption = big_consumption / 360000
    big_cons.append(big_consumption)

    little_consumption = 0.0
    for freq in littleCoreStat:
        little_consumption += littleCoreStat[freq] * little_power_profie[freq]
    little_consumption = little_consumption / 360000
    little_cons.append(little_consumption)

    device.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
    kill_command = 'am force-stop %s' % package
    device.shell(kill_command)

    print("Test #" + str(test_i))
    print("big_cons: " + str(big_consumption))
    print("little_cons: " + str(little_consumption))
    print("overall: " + str(big_consumption + little_consumption))
    print("")

avg_big_cons = sum(big_cons) / test_count
avg_little_cons = sum(little_cons) / test_count
print("Average big core consumption: " + str(avg_big_cons))
print("Average little core consumption: " + str(avg_little_cons))
print("Average consumption: " + str(avg_big_cons + avg_little_cons))