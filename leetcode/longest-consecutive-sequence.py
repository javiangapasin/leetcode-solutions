from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # If the list is empty or only has 1 value, return 0 or 1
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        
        # Otherwise:
        # 1. Transform the list into a set to get rid of duplicates
        # 2. Turn this back into a list so we can iterate easier and access indexes
        # 3. Sort the list
        list_set = sorted(list(set(nums)))

        # Initialize an empty hashmap with ints as values
        hashmap = defaultdict(int)

        # Itereate through each number in the sorted list
        for number in list_set:

            # Look to see if the current number - 1 is in there
            # If it is, create a hashmap key with the current number and the index it's at
            if (number - 1 not in list_set):
                hashmap[number] = list_set.index(number)
        
        # Just to make sure we catch the last element
        # Create an element in the hashmap with the key being the last number in the list
        # The value will be the index of that last number / the length of the set
        hashmap[list_set[len(list_set)-1]] = len(list_set)

        # Set values for current and max differences and then turn the hashmap values into a list
        current_difference = 0
        max_difference = 0
        index_list = list(hashmap.values())
        print(index_list)
        print(list_set)
        if (len(index_list) == 1):
            return len(list_set)

        # To make sure we don't go out of bounds, start checking after the first element
        # The first element will always be the start of a sequence, even if it's only one
        for i in range(0, len(index_list)):
            if (i != 0):
                current_difference = index_list[i] - index_list[i-1]
                if (current_difference > max_difference):
                    max_difference = current_difference

        return max_difference