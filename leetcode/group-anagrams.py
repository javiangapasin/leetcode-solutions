from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # We'll need a hashmap where the keys are frequencies of characters for each string
        # The values will be a list of the words themselvse
        # The default dict will help eliminate the need for checking if the key already exists
        # E.g {("c:1, a:1, t:1"): ['act','cat']}, where the freqs are the key and the list is the value
        freq_list = defaultdict(list)

        for word in strs:
            char_count = [0] * 26 # Intialize a frequency array for characters from a to z, 26 characters, do this for each word

            # Then, we need to build the keys / frequency counts for the characters in the word
            for char in word:

                # We calculate the index of the array / it's order in the alphabet (ord gives us the Unicode val)
                # We take the ASCII value of the current char and subtract 'a' from it
                # E.g: ASCII of 'a' = 97. ASCII 'b' = 98. Then. 98-97 = 1, which would be the 2nd index / 2nd part of the alphabet
                char_count[ord(char) - ord("a")] += 1

            # Note that hashmap / dict keys are immutable, this dict needs an immuatable value for its key
            # So, we make it a tuple, so that it's hashable / immutable (constant throughout it's lifetime)
            # Because we have a default dict, it will make the key if it doesn't exist
            freq_list[tuple(char_count)].append(word) # Append the word to the list
     
        return list(freq_list.values())