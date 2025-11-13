int removeElement(int* nums, int numsSize, int val) {
    if (numsSize <= 0){
        return 0;
    }
    int notVal[numsSize]; // Temporary array to store elements not equal to val
    int j = 0; // Index for notVal array, and it's counter for size

    // Fill the notVal array with elements not equal to val
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] != val) {
            notVal[j] = nums[i];
            j++;
        }
    }

    // Copy the elements back from notVal to nums
    for (int k = 0; k < j; k++) { // Use `j` as the valid size of `notVal`
        nums[k] = notVal[k];
    }

    return j; // Return the count of elements not equal to val
}