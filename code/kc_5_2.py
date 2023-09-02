# kancolle 5-2 script

import subprocess
import time

steps = [(356,  291,    1),     # home              9   - 5 (time, wait time)
         (748,  878,    0),     # go 1              7   - 5
         (857,  722,    0),     # go 2              8   - 5
         (1450, 1377,   0),     # southern area     7   - 5
         (1711, 717,    0),     # 5-2               7   - 5
         (2013, 1356,   1),     # decide            9   - 5
         (1843, 1357,   3),     # start             15  - 10
         (1380, 838,    4),     # campass           60  - 15
         (1437, 861,    1),     # win               10  - 5
         (1375, 835,    2),     # end               12  - 8
         (1642, 821,    2),     # back              12  - 8
         (436,  726,    1),     # refill 1          10  - 5
         (540,  500,    2)      # refill 2          12  - 5
        ]


# 7, 10, 12, 15, 60
sleeptime = [7, 10, 12, 15, 60]

# 10s to start
time.sleep(10)

'''
    total 179s for one round
    one hour is about 20 round
'''
for _ in range(0,26):
    for step in steps:
        process1 = subprocess.Popen(["xdotool", "mousemove", str(step[0]), str(step[1])])
        process1.wait()

        process2 = subprocess.Popen(["xdotool", "click", "1"])
        process2.wait()
        
        print(time.time())
        time.sleep(sleeptime[step[2]])

