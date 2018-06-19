#Write a script that reads the current time and converts it to a time of day in hours, minutes, and
#seconds, plus the number of days since the epoch.

import time

epoch = time.time()

def main():
    localTime = time.strftime("%I:%M:%S", time.localtime(epoch))
    daysSinceEpoch = epoch // (24 * 60 * 60)
    print('The local time is', localTime)
    print('Days since epoch:', daysSinceEpoch)
main()


