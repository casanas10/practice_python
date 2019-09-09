def insertion_sort(list):

    for i in range(1, len(list)):
        cur = list[i]
        j = i
        while j > 0 and list[j-1] > cur:
            list[j] = list[j-1]
            j -= 1
            list[j] = cur
    return list

def main():
    nums = [7,3,1,2]

    print(insertion_sort(nums))


if __name__ == "__main__":
    main()