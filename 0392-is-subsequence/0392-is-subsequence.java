class Solution {
    public boolean isSubsequence(String s, String t) {
        int si = 0;
        int ti = 0;

        while (si < s.length() && ti < t.length()) {
            char sc = s.charAt(si);

            while (ti < t.length() && t.charAt(ti) != sc) {
                ti++;
            }

            if (ti >= t.length()) {
                break;
            }

            si++;
            ti++;
        }

        return si == s.length();
    }
}