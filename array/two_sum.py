
'''
Given an array of integers, return the indices of the two numbers such that they add up to specific target.
Assume each input has exactly one solution and no elem is used twice.

Example :
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''



def two_pass_twoSum(nums, target):

    hash_table = {}

    for index, num in enumerate(nums):
        hash_table[num] = index

    for index, num in enumerate(nums):
        compliment = target - num
        if compliment in hash_table and hash_table[compliment] != index:
            return hash_table[compliment], index

    raise ValueError


def twoSum(nums, target):

    hash_table = {}

    for index, num in enumerate(nums):
        compliment = target - num
        if compliment in hash_table and hash_table[compliment] != index:
            return hash_table[compliment], index
        else:
            hash_table[num] = index

    raise ValueError

def main():
    nums = [2, 7, 11, 15]
    target = 9

    print(twoSum(nums, target))


if __name__ == "__main__":
    main()