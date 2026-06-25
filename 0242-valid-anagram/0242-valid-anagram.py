class Solution(object):
    def isAnagram(self, s, t):
        #If the length of the two strings are different automatically return False 

        if len(s) != len(t):
            return False 

        #Initalize a dictionary that will hold each charater and how frequently they exist in the string 

        frequent = {}

        #Count how mant times each character appears in s 

        for char in s: 

            #If the character not seen before start at 0 then add 1 
            #If the charater has already been added to the dictionary just increase the value by 1 

            frequent[char] = frequent.get(char,0) + 1

        #Now process the t by canceling out charaters from the dictionary 

        for char in t:
            if char not in frequent:
                return False 

        #If the character is listed in the dictionary remove one occurance
            frequent[char] -= 1

        #If count goes below 0, t has more of the specific character than s; making it not an anagram
            if frequent[char] < 0:
        
                return False 

        return True 