from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

text = MonkeyRunner.help("html")

f = open('help.html', 'w')
f.write(text)
f.close()
