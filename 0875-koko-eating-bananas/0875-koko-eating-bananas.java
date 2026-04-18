class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        Arrays.sort(piles);

        int min = 1;
        int max = piles[piles.length - 1];

        int result = max;

        while (min <= max) {
            int mid = (min + max) / 2;

            if (eat(piles, h, mid)) {
                result = Math.min(result, mid);
                max = mid - 1;
            } else {
                min = mid + 1;
            }
        }

        return result;
    }

    boolean eat(int[] piles, int h, int k) {
        long spent = 0;
        int i = 0;
        while (i < piles.length) {
            long current = piles[i];
            if (current % k == 0) {
                spent += current / k;
            } else {
                spent += (current / k) + 1;
            }

            if (spent > h) {
                return false;
            }

            i++;
        }

        return true;
    }
}