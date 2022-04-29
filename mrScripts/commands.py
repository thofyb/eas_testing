def cmd_dump_time(core_i, test_i, folder_name):
    return 'adb shell cat /sys/devices/system/cpu/cpu' + str(core_i) + '/cpufreq/stats/time_in_state > res/' + folder_name + '/time_in_state_' + str(core_i) + '_' + str(test_i) + '.txt'


def cmd_dump_trans(core_i, test_i, folder_name):
    return 'adb shell cat /sys/devices/system/cpu/cpu' + str(core_i) + '/cpufreq/stats/trans_table > res/' + folder_name + '/trans_table_' + str(core_i) + '_' + str(test_i) + '.txt'


def cmd_reset(core_i):
    return 'adb shell \"echo 1 > /sys/devices/system/cpu/cpu' + str(core_i) + '/cpufreq/stats/reset\"'


def cmd_gov_set(core_i, gov):
    return 'adb shell \"echo ' + gov + ' > /sys/devices/system/cpu/cpu' + str(core_i) + '/cpufreq/scaling_governor\"'


def cmd_battery_stats_reset():
    return 'adb shell dumpsys batterystats --reset'


def cmd_battery_stats_dump(package, test_i, folder_name):
    return 'adb shell dumpsys batterystats --charged ' + package + ' > res/' + folder_name + '/batterystats_' + str(test_i) + '.txt'


def cmd_gfxinfo_reset():
    return 'adb shell dumpsys gfxinfo --reset'


def cmd_gfxinfo_dump(package, test_i, folder_name):
    return 'adb shell dumpsys gfxinfo ' + package + ' > res/' + folder_name + '/frames_' + str(test_i) + '.txt'


def cmd_video_playing():
    return "adb shell am start -a android.intent.action.VIEW -d file:///sdcard/video.mp4 -t video/mp4"

def cmd_start_test(test, governor, test_cnt):
    return "monkeyrunner" + test + " " + str(test_cnt) + " " + governor
