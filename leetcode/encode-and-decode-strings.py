class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        # To encode, we're going to have to keep track of the number of characters in the string to copy
        # We're also going to have to use some form of delimiter to know how to seperate the strings when decoding
        # We'll format the strings as follows
        # 6$string (length, delimiter ($), and the word itself)
        for s in strs:
            result += str(len(s)) + "$" + s
        return result

    def decode(self, s: str) -> List[str]:

        result_list = []
        i = 0
        current_str = ""

        # Itereate through the string
        # We'll need two pointers, one to advance throughout the string and then one to keep track of where we started counting
    
        while i < len(s):

            # We'll set j = to i and then go through the string until we find a delmiter
            j = i 
            while s[j] != "$":
                # If we haven't found the delmiter yet, we'll keep moving j forward until we do so
                j += 1 
            # Once we find our delimiter, i will still be at our starting point
            # The length will be all the characters from i to j, excluding j
            # This takes into account double digit lengths as well, length is guaranteed because of how we encoded the string
            length = int(s[i:j])

            # J would be on the delimiter after iterating, so move it up
            j = j + 1 

            # Now loop through the array {length} amount of times, and keep incrementing j
            for k in range(length):
                current_str += s[j]
                j += 1
            result_list.append(current_str)

            # J after exiting the loop would now be on the integer
            i = j 
            current_str = ""

        return result_list
        
