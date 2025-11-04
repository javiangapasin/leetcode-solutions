class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:

        frequencies = {}
        #Count frequencies
        for element in nums:
            #Look each number up in the hashmup
            #If it already exists, get it's current count
            #If it doesn't exist, give it a default of 0, and then add 1
            frequencies[element] = frequencies.get(element,0) + 1

        max_freq = 0
        total_freq = 0

        for frequency in frequencies.values():
            if frequency > max_freq:
                max_freq = frequency
                total_freq = frequency
            elif frequency == max_freq:
                total_freq += frequency
        
        
        print(frequencies)
        return total_freq