class Solution(object):
#Creates a dictionary except if the sorted version of the word does not exist yet it will auto create it with a default word
#This avoids having to cheack if that key already exist in the dictionary 
    from collections import defaultdict
    def groupAnagrams(self, strs):

        #Create a bucket organizer so every key will map to a list of words 

        AnagramMap = defaultdict(list)

        #Vist every word in the input lisst one at a time 

        for word in strs:

            #Take the word and return the letters in alphabetical order as a list

            #Join the list of all the letters back 

            key = "".join(sorted(word))

            #Place the orignial word into the bucket labelled by its sorted key

            AnagramMap[key].append(word)

        return list(AnagramMap.values())


        