def findRestaurants(list1, list2):

    #ensures list1 is the minimum
    if len(list1) > len(list2):
        findRestaurants(list2, list1)

    map = {str : i for i, str in enumerate(list1)}

    minIndexSum = float("inf")
    output = []
    for i, str in enumerate(list2):
        if str in map:
            current_index_sum = map[str] + i
            if current_index_sum < minIndexSum:
                minIndexSum = current_index_sum
                output = []
                output.append(str)
            elif current_index_sum == minIndexSum:
                output.append(str)
    return output

list1 = ["Shogun", "KFC", "Burger King", "Tapioca Express"]
list2 = ["KFC", "Shogun", "Burger King"]

output = findRestaurants(list1, list2)

print(output)