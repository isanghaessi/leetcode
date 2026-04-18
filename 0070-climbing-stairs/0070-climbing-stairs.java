class Solution {
    Map<Integer, Integer> ways = new HashMap<>();

    public int climbStairs(int n) {
        if (n < 0) {
            return 0;
        }
        if (n == 1) {
            return 1;
        }
        if (n == 2) {
            return 2;
        }

        if (ways.containsKey(n)) {
            return ways.get(n);
        }

        int result = climbStairs(n -1) + climbStairs(n - 2);
        ways.put(n, result);

        return result;
    }
}