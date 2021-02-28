# DVFS Testing 

In this repository you can find test cases for testing Dynamic Voltage and Frequency Scaling algorithms.
For running them you need to use [MonkeyRunner (MR)] and [Android Debug Bridge (ADB)] tools from Android SDK. 




# Test cases 

- _Intensive typing_:
    MR script installs (if it's not installed yet) [Notes] application and types a text for 25 minutes.
- _Flappy bird_:  
    MR script installs (if it's not installed yet) [Flappy bird] and plays for 25 minutes.
- _Trial Xtreme 3_:
    MR script installs (if it's not installed yet)
    [Trial Xtreme 3] and plays for 25 minutes.
- _Video Shooting_:
    ADB script activates camera and shoots video for 25 minutes.
- _Video Playback_:
    This case is not a script.
    For starting this case you need to set video from ```/mrScripts``` folder (or your own video) and start to play it with this command:
    ```
    adb shell am start -a android.intent.action.VIEW -t video/mp4 -d <URI>
    ```




[MonkeyRunner (MR)]: <https://developer.android.com/studio/test/monkeyrunner>

[Notes]: <https://apkpure.com/notes/com.ogden.memo>
 
[Android Debug Bridge (ADB)]: <https://developer.android.com/studio/command-line/adb>

[Flappy bird]: <https://en.wikipedia.org/wiki/Flappy_Bird>

[Trial Xtreme 3]: <https://www.youtube.com/watch?v=iGu1R090pYk&ab_channel=TouchGameplay>
