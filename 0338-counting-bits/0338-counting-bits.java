class Solution {
    public int[] countBits(int n) {
        int[] result = new int[n + 1];
        
        for (int i = 0; i <= n; i++) {
            result[i] = get(i);
        }

        return result;
    }

    int get(int n) {
        int result = 0;

        while (n > 0) {
            result += (n % 2);
            n /= 2;
        }

        return result;
    }
}