def partition(list, left, right):

    i = (left - 1)
    pivot = list[right]

    for j in range(left, right):

        if list[j] < pivot:
            i = i + 1

            list[i], list[j] = list[j], list[i]

    list[i+1], list[right] = list[right], list[i+1]

    return (i + 1)


def quick_sort(list, left, right):
    if left < right:
        index = partition(list, left, right)
        quick_sort(list, left, index - 1)
        quick_sort(list, index + 1, right)

    return list

def main():

    list = [10, 7, 8, 9, 1, 5]

    print(quick_sort(list, 0, len(list) - 1))


if __name__ == "__main__":
    main()