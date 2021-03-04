def cmd_dump_time(core_i, test_i):
    return '~/Android/Sdk/platform-tools/adb shell cat /sys/devices/system/cpu/cpu' + str(core_i) + '/cpufreq/stats/time_in_state > res/time_in_state_' + str(core_i) + '_' + str(test_i) + '.txt'


def cmd_dump_trans(core_i, test_i):
    return '~/Android/Sdk/platform-tools/adb shell cat /sys/devices/system/cpu/cpu' + str(core_i) + '/cpufreq/stats/trans_table > res/trans_table_' + str(core_i) + '_' + str(test_i) + '.txt'


def cmd_reset(core_i):
    return '~/Android/Sdk/platform-tools/adb shell \"echo 1 > /sys/devices/system/cpu/cpu' + str(core_i) + '/cpufreq/stats/reset\"'


def cmd_gov_set(core_i, gov):
    return '~/Android/Sdk/platform-tools/adb shell \"echo' + gov + ' > /sys/devices/system/cpu/cpu' + str(core_i) + '/cpufreq/scaling_governor\"'


def cmd_battery_stats_reset():
    return '~/Android/Sdk/platform-tools/adb shell dumpsys batterystats --reset'


def cmd_battery_stats_dump(package, test_i):
    return '~/Android/Sdk/platform-tools/adb shell dumpsys batterystats --charged' + package + ' > res/batterystats_' + str(test_i) + '.txt'
