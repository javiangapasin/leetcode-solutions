class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        
        # First find the total sum of the array, and then subtract that from the left part of the array which we can keep adding onto
        # This will basicially give us the sum of the right array
        # Then we can keep moving i up and adding to the left array for each partition
        # Finally we'll check if the partitions are even using the modulus operator which wil return a 0 if there is no remainder, meaning it's even

        total_sum = sum(nums)
        left_sum = 0
        partition_count = 0

        for i in range (len(nums) -1):
            left_sum += nums[i]
            right_sum = total_sum - left_sum

            # Check to see if both are even
            if (left_sum % 2) == (right_sum % 2):
                partition_count += 1

        return partition_count