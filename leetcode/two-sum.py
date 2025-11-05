class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #Store the numbers and their indexes in a hashtable
        numsTable = {}

        #Iterate over the array to try and find the elements
        for i in range(len(nums)):

            #Calculate the difference between the target and the current number
            difference = target - nums[i]

            #Check if the difference is already a number in the hashtable
            #The following will check if key is in a hashtable and return the value of the index 
            #as well as the current index

            if difference in numsTable:
                return numsTable[difference], i
            
            #Otherwise, add the key value pair to the hashtable
            #numsTable[nums[i]] is the number itself, the value i will be the index
            numsTable[nums[i]] = i