class Solution {
    public int maxProfit(int[] prices) {
        int min = prices[0];

        int result = 0;

        for (int i = 0; i < prices.length; i++) {
            int current = prices[i];

            min = Math.min(min, current);

            result = Math.max(result, current - min);
        }

        return result;
    }
}