'''
Write a program that takes in an input array and finds the distance between the closest pairs of equal entries.
'''

'''
Time COmplexity : O(n) because we iterate through every entry in the array
Space Complexity: O(d) where d is the distinct words in the paragraph 
'''
def find_nearest_repetition(paragraph):

    min_distance = float('inf')
    map = {}
    for index, word in enumerate(paragraph):
        if word in map:
            last_index = map[word]
            min_distance = min(index - last_index, min_distance)
        map[word] = index

    return min_distance if min_distance != float('inf') else -1


paragraph = "All work and no play makes for no work no fun and no result"
p = paragraph.split()
print(find_nearest_repetition(p))