import os

a=os.popen("adb shell getprop ro.serialno")
print(a.readline())