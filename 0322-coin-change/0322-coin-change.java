class Solution {
    public int coinChange(int[] coins, int amount) {
        Map<Integer, Integer> dp = new HashMap<>();
        dp.put(0, 0);

        for (int i = 1; i <= amount; i++) {
            int current = -1;

            for (int j = 0; j < coins.length; j++) {
                if (i - coins[j] < 0) {
                    continue;
                }

                int previous = dp.getOrDefault(i - coins[j], -1);
                if (previous < 0) {
                    continue;
                }

                if (current < 0) {
                    current = previous + 1;
                } else {
                    current = Math.min(current, previous + 1);
                }
            }

            dp.put(i, current);
        }

        return dp.get(amount);
    }
}