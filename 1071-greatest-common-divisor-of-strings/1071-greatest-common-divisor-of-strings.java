class Solution {
    public String gcdOfStrings(String str1, String str2) {
        if (str1.length() < str2.length()) {
            String temp = str1;
            str1 = str2;
            str2 = temp;
        }

        String result = str2;

        for (int i = str2.length(); i > 0; i--) {
            result = str2.substring(0, i);

            if (check(result, str1) && check(result, str2)) {
                return result;
            }
        }

        return result;
    }

    boolean check(String divide, String str) {
        if (str.length() % divide.length() > 0) {
            return false;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < str.length() / divide.length(); i ++) {
            sb.append(divide);
        }

        return sb.toString().equals(str);
    }
}