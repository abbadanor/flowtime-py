import time
import math
starttime = time.time()
counter = 0

def rest(secs):
    return -0.0000000035613*pow(secs,3) + 0.000016025641 * pow(secs,2) + 0.1839743589744 * secs

while True:
    if counter < 60*90:
        print(str(math.floor(rest(counter) / 60)) + ", sekunder: " + str(counter) + ", minuter: " + str(counter / 60))
    else:
        print("15, ta en paus!")
    time.sleep(1 - ((time.time() - starttime) % 1))
    counter += 1
