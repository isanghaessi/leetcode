class Solution {
    public int longestOnes(int[] nums, int k) {
        int result = 0;

        int l = 0;
        while (l < nums.length) {
            if (nums[l] == 0) {
                l++;
                continue;
            }

            int r = l + 1;
            while(r < nums.length && nums[r] == 1) {
                r++;
            }

            int _l = l - 1;
            int _r = r;
            int _k = k;
            while (_l >= 0) {
                if (nums[_l] == 0) {
                    if (_k > 0) {
                        _k--;
                    } else {
                        break;
                    }
                }
                _l--;
            }
            while (_r < nums.length && _k > 0 && nums[_r] == 0) {
                if (nums[_r] == 0) {
                    if (_k > 0) {
                        _k--;
                    } else {
                        break;
                    }
                }
                _r++;
            }

            result = Math.max(result, (_r - 1) - (_l + 1) + 1);

            while (l < nums.length && nums[l] == 1) {
                l++;
            }
        }

        return Math.max(result, k);
    }
}