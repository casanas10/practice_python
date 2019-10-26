'''
Write a program that takes an array of strings and a set of strings and return the indices of the starting and
ending index of the shortest subarray covering all strings in the set.

'''

import collections

def find_smallest_subarray_covering_set(paragraph, keywords):

    result = (-1, -1)
    keywords_to_cover = collections.Counter(keywords)

    remaining_to_cover = len(keywords)
    left = 0
    for right, p in enumerate(paragraph):
        if p in keywords:
            keywords_to_cover[p] -= 1
            if keywords_to_cover[p] >= 0:
                remaining_to_cover -= 1

        #keep advancing left until keywords_to_cover does not contain all keywords
        while remaining_to_cover == 0:
            if result == (-1, -1) or right - left < result[1] - result[0]:
                result = (left, right)

            pl = paragraph[left]

            if pl in keywords:
                keywords_to_cover[pl] += 1
                if keywords_to_cover[pl] > 0:
                    remaining_to_cover += 1

            left += 1

    return result


paragraph = "apple banana apple apple dog cat apple dog banana apple cat dog"
paragraph = paragraph.split()
keywords = ["banana", "cat"]

print(find_smallest_subarray_covering_set(paragraph, keywords))