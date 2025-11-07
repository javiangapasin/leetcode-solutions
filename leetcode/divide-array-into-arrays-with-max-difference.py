#We'll need the numpy library to help with the matrix
import numpy as np

class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        #First, we sort nums from smallest to largest
        nums.sort()

        #Create a matrix with 3 columns for size 3, and length of nums / 3 
        answer_matrix = np.zeros(((len(nums) / 3), 3), dtype=int)
        row = 0

        #Itereate through each set of 3 numbers
        for i in range (0, len(nums), 3):

            #If the difference between the first number and the third number
            #is greater than the k value, we know that it isn't possible for
            #any two elements to be less than k, so return an empty array
            if (nums[i+2] - nums [i] > k):
                return []

            #Otherwise, add the 3 numbers as a row to the answer matrix
            answer_matrix[row] = [nums[i], nums[i+1], nums[i+2]]

            #Advance the row 
            row += 1

        #Return as a list
        return answer_matrix.tolist()