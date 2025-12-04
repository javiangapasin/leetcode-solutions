class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # just get the product of everything before and then the product of everything after and multiply

        # Create arrays to store the products of everything left of our numbers and right of our numbers
        left_arr = [0] * len(nums)
        right_arr = [0] * len(nums)

        # Set the default product / multiplication values to 1. Mulitplying by 1 does nothing, use for out of bounds multiplier
        # E.g 1 [1,2,4,6]
        left_product = 1
        right_product = 1

        # Now iterate through the array, with i being the pointer that moves left
        for i in range (len(nums)):

            # Keep a second index pointer that iterates backwards from the right side of the array
            j = -i-1

            # Left array will store the products of everything left of the array, starting with the default multiplier
            left_arr[i] = left_product

            #Right array will store similar products
            right_arr[j] = right_product

            # Then we update the left and right products.
            # We multiply the current product with the current number that the left and right pointer are at

            # E.g. i = 0, j = 3
            # 1 [1,2,4,6] 1
            # ^  ^     ^  ^
            # L  i     j  R 
            # Left product is going to be 1, outside of the array, multiplied with the current i
            left_product *= nums[i]

            # Right product is similar, but moving left and starting with j
            right_product *= nums[j]

        # By the end of the pass through the array, the left and right arrays should store the products of everything left or right
        # To get the actual answer, we can just multiply the left and right arrays together
        results = [0] * len(nums)

        for k in range(0, len(nums)):
            results[k] = left_arr[k] * right_arr[k]

        return results