class Solution {
    public int maxArea(int[] height) {

        int l = 0;
        int r = height.length - 1;
        int result = cal(height, l, r);

        while (l < r) {
            int left = height[l];
            int right = height[r];

            if (left > right) {
                while (l < r && height[r] <= right) {
                    r--;
                }
            } else {
                while (l < r && height[l] <= left) {
                    l++;
                }
            }

            if (l < r) {
                result = Math.max(result, cal(height, l, r));
            }
        }

        return result;
    }

    private int cal(int[] arr, int l, int r) {
        return (r - l) * Math.min(arr[l], arr[r]);
    }
}