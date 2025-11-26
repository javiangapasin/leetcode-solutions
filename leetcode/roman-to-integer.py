class Solution:
    def romanToInt(self, s: str) -> int:

        # Create a hash map of the roman numerals and their int values
        roman_set = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        current_num = 0

        # Iterate through the string
        for i in range (len(s)):
            # Check if there is a character after and we're in bounds
            if i + 1 < len(s) and roman_set[s[i]] < roman_set[s[i+1]]:

                # If the character infront is greater than the current character
                # we basically subtract the character in front - the current character to get the Int value
                # E.g IV. I < V (1 < 5) so it becomes V - I (5-1) = 4
                current_num -= roman_set.get(s[i])
            else:
                # Otherwise, just add the integer value from our hash table
                current_num += roman_set.get(s[i])   
    
        return current_num