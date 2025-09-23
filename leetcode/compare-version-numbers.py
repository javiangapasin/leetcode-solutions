class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        #Split the string into a list based on the ., this will give us a list of each revision
        split1 = version1.split('.')
        split2 = version2.split('.')

        #Get the length of both strings
        len1, len2 = len(split1), len(split2)

        #We're going to iterate through each string, the max length amount of times
        #The max length will be the longest length between the two
        #We are going to compare each index, as each index is a revision
        #We ignore zeros, and if the string is shorter and there's nothing there, we put a 0 there
        max_len = max(len1,len2)

        #Get the revision from each list and compare as an INTEGER
        for i in range(max_len):

            #First check the current revision and see if it's within the length. 
            #If it is, get the integer value of the revision
            if (i < len1):
                revision1 = int(split1[i])

            #If i goes beyond the length of the string, just put a 0 there
            #E.g [1,0,1] and [1,0,0,1].
            #When going through the first string, i will hit 3, which is the length, meaning we've gone past length of the string
            #So just add a 0 here for comparison sake
            else:
                revision1 = 0

            #Do the same with the second revision
            if (i < len2):
                revision2 = int(split2[i])
            else:
                revision2 = 0

            #Now do a simple comparison.
            if (revision1 < revision2):
                return -1
            elif (revision1 > revision2):
                return 1

        #If the loop finishes before returning, it means they're equal and we return 0
        return 0