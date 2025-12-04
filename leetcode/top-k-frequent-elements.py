class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Dictionary to store the frequencies of each element
        frequencies = {}

        for num in nums:
            # First check if number already exists in dict, add if not
            if num not in frequencies:
                frequencies[num] = 0
                frequencies[num] += 1
            else:
                frequencies[num] += 1
        
        # Sort the frequencies based on key
        # frequencies.items() will return the dictionary as a list, with tuples of the keys and values, doesn't modify the OG dict
        # key= lambda is a one time function / criteria that we'll use to sort the values
        # In this case, the function is sorted based on the item, and item[1] means sort based on the second item in the tuple (the value)
        # reverse= True makes sure that this is sorted in descending order
        sorted_freqs = sorted(frequencies.items(), key= lambda item: item[1], reverse=True)

        # Convert it back to a dict, but now sorted
        sorted_dict = dict(sorted_freqs)

        # We have to return a list of the elements, so make the keys into a list
        keys_list = list(sorted_dict.keys())

        # Slice to only return the k most frequent elements
        return keys_list[:k]