class Solution {
    public boolean isPalindrome(String s) {
        if (s == null || s.empty()) {
            return true;
        }

        int l = 0;
        int r = s.length() - 1;
        while (l < r) {
            char ls = s.charAt(l);
            char rs = s.charAt(r);

            if(!Character.isLetterOrDigit(ls)) {
                l++;
            }
            else if(!Character.isLetterOrDigit(rs)) {
                r--;
            } else {
                if(Character.toLowerCase(ls) != Character.toLowerCase(rs)) {
                    return false;
                }
                l++;
                r--;
            }
        }

        return true;
    }
}