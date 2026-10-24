class Solution {
    public int maxProfit(int[] prices) {

        // keep track of the higest difference 
        // lowest buyPrice seen so far 

        int highestProfit = 0; 

        int lowestValue = Integer.MAX_VALUE; 

        for(int i = 0; i < prices.length; i++){
            if(prices[i] < lowestValue){
                lowestValue = prices[i];
            }else{

                highestProfit = Math.max(highestProfit, prices[i]- lowestValue);
            }
        }

        return highestProfit;



        
        
    }
}