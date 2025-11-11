/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getConcatenation(int* nums, int numsSize, int* returnSize) {

    // Set the return size to twice the original array size
    // because the concatenated array will contain nums followed by nums again.
    *returnSize = numsSize * 2;

    // Dynamically allocate memory for the new array of size *returnSize.
    // malloc() returns a pointer to the allocated memory block.
    int *newArr = malloc(sizeof(int) * (*returnSize));

    // Loop through all indices of the new array
    for (int i = 0; i < *returnSize; i++) {

        // If index i is greater than or equal to numsSize,
        // we are now in the second half of the new array,
        // so copy elements from the start of nums again.
        if (i >= numsSize) {
            newArr[i] = nums[i - numsSize];
        }
        // Otherwise, just copy the elements from nums as-is.
        else {
            newArr[i] = nums[i];
        }
    }

    // Return the pointer to the new concatenated array.
    // The caller is responsible for freeing the allocated memory.
    return newArr;
}