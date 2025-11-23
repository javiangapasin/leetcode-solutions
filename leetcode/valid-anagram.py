class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # If they are not the same length, automatically not an anagram
        if len(s) != len(t):
            return False

        s_count = {} # Hashmap to count the frequencies of each character in s
        t_count = {} # Hashmap to count the frequencies of each character in t

        # Check each character in S and add to hashmap if needed
        for character in s:
            if character not in s_count:
                s_count[character] = 0 # Initialize to 0
                s_count[character] += 1 # Then add 1
            else:
                s_count[character] += 1
        
        # Check each character in T and add to hashmap if needed
        for character in t:
            if character not in t_count:
                t_count[character] = 0 # Initialize to 0
                t_count[character] += 1 # Then add 1
            else:
                t_count[character] += 1

        # Check the characters

        equal = False # Initialize a flag to false

        for character in s_count: # For each character in s
            if character in t_count: # If the character is in t
                if s_count.get(character) == t_count.get(character): # Check to see if the counts are the same
                    equal = True # Set flag to true

                # If the frequencies for a character aren't the same, immediately return False
                else: 
                    return False
            # Similarly, if the character isn't in t count, immediately return false, not an anagram
            else:
               return False

        # Return the current value of the equal flag
        return equal