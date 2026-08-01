class Solution {
    public String gcdOfStrings(String str1, String str2) {
        int len = Math.min(str1.length(), str2.length());

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < len; i++) {
            if (str1.charAt(i) != str2.charAt(i)) {
                break;
            }

            sb.append(str1.charAt(i));
        }
        String candidate = sb.toString();

        for (int i = candidate.length(); i >= 0; i--) {
            String current = candidate.substring(0, i);
            if (doDivide(str2, current) && doDivide(str1, current)) {
                return current;
            }
        }

        return "";
    }

    private boolean doDivide(String s, String t) {
        if (t == null || t.length() == 0) {
            return false;
        }
        if (s.length() % t.length() > 0) {
            return false;
        }

        StringBuilder sb = new StringBuilder(t);
        while (sb.length() < s.length()) {
            sb.append(t);
        }

        return s.equals(sb.toString());
    }
}