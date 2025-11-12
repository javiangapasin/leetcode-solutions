int removeDuplicates(int* nums, int numsSize) {
    if (numsSize == 0) return 0; // Edge case: empty array

    int numDupes[numsSize]; // Temporary array to store unique elements
    int k = 0; // Index for unique elements

    for (int i = 0; i < numsSize; i++) {
        // Add element to numDupes only if it's not equal to the previous element or it's the first element
        if (i == 0 || nums[i] != nums[i - 1]) {
            numDupes[k] = nums[i];
            k++;
        }
    }

    // Copy unique elements back to nums
    for (int p = 0; p < k; p++) {
        nums[p] = numDupes[p];
    }

    return k; // Number of unique elements
}