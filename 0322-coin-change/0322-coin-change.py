class Solution(object):
    def coinChange(self, coins, amount):
        #Create an array the size of amount + 1
        #Initial fill it in with infinity because the goal is to find the minimum 
        #Inital assumption is that every amount is impossible 

        dp = [float('inf')] * (amount + 1)

        #Create base case to 
        #To make amount 0, 0 coins are needed

        dp[0] = 0 

        #Now the goal is to computer answer for every amount starting at 1 and ending at the amount value given 

        for i in range(1, amount +1):

            #For each i, every coin should be tried

            for coin in coins:

                #To check if the coin can be used. 
                #If the coin is too large skip it 

                if i  >= coin:

                    #If the coin is not too large:
                    #Take the best way to use it 
                    #Then add the 1 coin to the current coin 

                    dp[i] = min(

                        dp[i], #current Best
                        dp[i-coin] + 1 #Best way to make (i - coin) + 1
                    )
        return dp[amount] if dp[amount] != float('inf') else -1






        