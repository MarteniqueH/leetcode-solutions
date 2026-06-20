class Solution(object):
    def numDecodings(self, s):
        #Saves the number that are already been computed 

        memo = {}

        #How many ways can I decode the string starting at index i 

        def dp(i):

        #If I have reached the end of the string, that means the string has been successfully decoded. 

            if i == len(s):
                return 1


            #A zero cannoy be decoded by itself . If I land on zero the decoding path ends .

            if s[i] == '0':
                return 0

                #Have I already solved this exact substring 

            if i in memo:
                return memo[i]

                    #First decision Take one digit 
                    #Counts all the valid decoding that happens after one digit 


            ways = dp(i+1)


                    #Check and see if two digits exist 
                    #Convert them into a number 
                    #Check if it is between 10 and 26 


            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:

                    #If the two digits form a valid letter, count those possiblites 

                ways += dp(i+2)

                    #Before returning save the answer 

            memo[i] = ways
            return ways

        return dp(0)


        