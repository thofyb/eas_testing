import time
import os
import sys
from commands import cmd_start_test

current_dir = os.getcwd

test_flappy_bird = current_dir + "/test_flappy_bird.py"

test_camera = current_dir + "/test_camera.py"

test_photomath = current_dir + "/test_photomath.py"

test_trial_xtreme = current_dir + "/test_trial_xtreme.py"

test_video = current_dir + "/test_video.py"

test_typing = current_dir + "/test_typing.py"

curr_governor = sys.argv[2]
test_count = int(sys.argv[1])

os.system(cmd_start_test(test_flappy_bird, curr_governor, test_count))

time.sleep(180)

os.system(cmd_start_test(test_trial_xtreme, curr_governor, test_count))

time.sleep(180)

os.system(cmd_start_test(test_typing, curr_governor, test_count))

time.sleep(180)

os.system(cmd_start_test(test_camera, curr_governor, test_count))

time.sleep(180)

os.system(cmd_start_test(test_video, curr_governor, test_count))

time.sleep(180)

os.system(cmd_start_test(test_photomath, curr_governor, test_count))

