#!/usr/bin/python
import os
import sys
import time
import subprocess


def workerFunction():
    tmp = os.popen("speedtest-cli --simple").read()
    split = tmp.split()
    download = split[4]
    print(split)
    fo.write(download + ", " + str(time.strftime("%d/%m/%Y")) + ", " + str(time.strftime("%H:%M:%S"))+"\n")

print("Running SpeedTest")

fo = open("test.txt", "w")

try:
    while(1):
        workerFunction()
        time.sleep(60)

except KeyboardInterrupt:
    print("Test finished")
    fo.close()
    sys.exit(0)