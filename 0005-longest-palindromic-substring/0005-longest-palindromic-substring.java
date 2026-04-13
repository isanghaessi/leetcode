import java.util.*;

class Solution {
    public String longestPalindrome(String s) {
        if (s.length() < 2) {
            return s;
        }

        String result = "";

        for (int i = 0; i < s.length(); i++) {
            String odd = check(s, i, i);
            String even = check(s, i, i + 1);
            String candidate = odd.length() > even.length() ? odd : even;

            if (result.length() < candidate.length()) {
                result = candidate;
            }
        }

        return result;
    }

    String check(String s, int left, int right) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }

        return s.substring(left + 1, right);
    }
}