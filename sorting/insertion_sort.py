def insertion_sort(list):

    for i in range(1, len(list)):

        cur = list[i]

        j = i-1
        while j >= 0 and cur < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = cur

    return list

def main():

    nums = [7,3,1,2]

    print(insertion_sort(nums))


if __name__ == "__main__":
    main()