from sys import stdin, stdout
from collections import deque


def main():
    while True:
        line = stdin.readline()
        if not line:
            break
        dur, downp, amt, depr = line.split()
        if int(dur) < 0:
            break
        dur, downp, amt, depr = int(dur), float(downp), float(amt), int(depr)

        # now we have a list from deque
        vals = deque()
        for val in range(int(depr)):
            month, percent = stdin.readline().split()
            vals.append((int(month), float(percent)))
            # print(vals)

        debt = amt / dur
        owe = amt
        month, currPercent = vals.popleft()
        worth = amt + downp
        worth -= currPercent * worth
        currMonth = 0
        if vals:
            nextMonth, nextPercent = vals.popleft()
        # print("month {}\namount is {}, owe is {}".format(currMonth, worth, owe))

        for i in range(1, dur + 1):
            if owe < worth:
                if currMonth == 1:
                    print("{} month".format(currMonth))
                    break
                else:
                    print("{} months".format(currMonth))
                    break
            currMonth += 1
            owe -= debt

            if nextMonth == i:
                currPercent = nextPercent
                if vals:
                    nextMonth, nextPercent = vals.popleft()
                    # print("nextMonth {}, currPercent {}".format(nextMonth, currPercent))
            worth = worth - currPercent * worth
            # print("curr Percent {}".format(currPercent))
            print("month {}\namount is {}, owe is {}".format(currMonth, worth,owe))
            
            if currMonth == dur:
                print("{} months".format(currMonth))
                break
  

if __name__ == "__main__":
    main()
