class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int i = 0;
        while (i < flowerbed.length) {
            if (n == 0) {
                return true;
            }

            if (flowerbed[i] == 0
                && (i - 1 < 0 || flowerbed[i - 1] == 0)
                && (i + 1 >= flowerbed.length || flowerbed[i + 1] == 0)) {
                flowerbed[i] = 1;
                n--;
            }

            i++;
        }

        return n == 0;
    }
}