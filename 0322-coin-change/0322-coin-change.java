class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, -1);
        dp[0] = 0;

        for (int i = 1; i <= amount; i++) {
            for (int j = 0; j < coins.length; j++) {
                if (i - coins[j] < 0) {
                    continue;
                }

                int previousIndex = i - coins[j];
                if (previousIndex < 0 || dp[previousIndex] < 0) {
                    continue;
                }

                int currentCount = dp[previousIndex] + 1;
                if (dp[i] < 0) {
                    dp[i] = currentCount;
                } else {
                    dp[i] = Math.min(dp[i], currentCount);
                }
            }
        }

        return dp[amount];
    }
}