void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) {

    int lastElement = nums1Size-1;
    //m points to the index of the last element in nums1 
    //n points to the index of the last element in nums2

    //While there are still elements in the array
    while (m > 0 && n > 0){

        //If nums1's last element is greater than nums2's last element 
        if (nums1[m-1] > nums2[n-1]){
            nums1[lastElement] = nums1[m-1];
            m--;
        }
        else{
            nums1[lastElement] = nums2[n-1];
            n--;
        }
        lastElement--;
    }

    //Fill nums1 with remaining elements from nums2
    while (m <= 0 && n > 0) {
        nums1[lastElement] = nums2[n-1];
        n--;
        lastElement--;
    }
    //Fill nums2 with remaining elements from nums1
    while (n <= 0 && m > 0) {
        nums1[lastElement] = nums1[m-1];
        m--;
        lastElement--;
    }




}