#!/bin/bash

adb shell "am start -a android.media.action.VIDEO_CAPTURE"
sleep 3
adb shell "input keyevent 27"
start_time="$(date -u +%s.%N)"
limit=1501.0000

while true; do
   end_time="$(date -u +%s.%N)"
   elapsed="$(bc <<< "$end_time-$start_time")"
   if (( $(echo "$elapsed >= $limit" | bc -l) ));
   then
      adb shell "input keyevent 27"
      break
   fi
done 
