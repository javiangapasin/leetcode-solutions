class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {} #initialize an empty hashmap
        #each key value pair will be the element, and it's frequency

        for element in nums: #iterate through each element in nums array
            if element not in hashmap: #first check if it's in hashmap already
                hashmap[element] = 0 #set to 0 if not
                hashmap[element] += 1 #then add

            else: #if it's already in the hashmap, add a count of one
                hashmap[element] += 1

            if hashmap[element] > 1: #if the current element has count > 1, return true
                return True

        return False