import os


def get_deviceid():
    deviceslist=[]
    device = os.popen("adb devices")
    print(len(device))
    for i in range(1,len(device)-1):
        deviceslist.append(device[i].split()[0])
    return deviceslist
print(get_deviceid())