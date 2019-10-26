'''

Gary is an avid hiker. He tracks his hikes meticulously, paying close attention to small details like topography.
During his last hike he took exactly n steps. For every step he took, he noted if it was an uphill, U , or a downhill, D
step. Gary's hikes start and end at sea level and each step up or down represents a 1 unit change in altitude.
We define the following terms

A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with
a step down to sea level.
A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with
a step up to sea level.

Count the number of vallyes

_/\      _
   \    /
    \/\/


Innput
s = "UDDDUDUU"
n = 8
Output => 1



'''


# because we only care when we come up to the sea level, that's when you count the valleys
def solution(s, n):

    valleys = 0
    state = 0

    for i in range(len(s)):

        if s[i] == "U":
            state += 1
        if s[i] == "D":
            state -= 1

        if state == 0 and s[i] == "U":
            valleys += 1

    return valleys

def main():
    s = "DDUUDDUDUUUD"
    n = 12

    res = solution(s, n)

    print(res)


    s = "UDDDUDUU"
    n = 8

    res = solution(s, n)

    print(res)

if __name__ == "__main__":
    main()