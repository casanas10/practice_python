'''
New York Chaos
https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
'''

def minimumBribes(q):

    moves = 0

    for i in range(len(q)):

        if q[i] - (i+1) > 2:
            print("Too chaotic")
            return

        for j in range(max(0, q[i]-2), i):
            if q[j] > q[i]:
                moves += 1
    print(moves)

def main():
    n = 7
    # arr= [5, 1, 2, 3, 7, 8, 6, 4]
    arr = [1, 2, 5, 3, 7, 8, 6, 4]
    res = minimumBribes(arr)


if __name__== "__main__":
    main()