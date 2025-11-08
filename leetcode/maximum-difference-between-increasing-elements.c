int maximumDifference(int* nums, int numsSize) {

    // Set initial values to -1 for the current differences
    int maxDiff = -1;
    int currDiff = -1;

    //More complex solution uses N^2 comparisons
    //Compare each element with each other element in the array
    for (int i = 0; i < numsSize; i++){
        for (int j = i; j < numsSize; j++){
            

            //If the current number is less than a number ahead of it
            if (nums[i] < nums[j]){

                //Compute the current difference, then check if 
                //larger than current Max Difference, update if needed
                currDiff = nums[j] - nums[i];
                if (currDiff >= maxDiff){
                    maxDiff = currDiff;
                }
            }
        }
    }

    return maxDiff;
}
