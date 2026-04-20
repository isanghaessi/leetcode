class Solution {
    public String gcdOfStrings(String str1, String str2) {
        if (str1.length() < str2.length()) {
            String temp = str1;
            str1 = str2;
            str2 = temp;
        }

        int i = 0;
        while (i < str2.length() && str1.charAt(i) == str2.charAt(i)) {
            i++;
        }

        String result = str2.substring(0, i);

        for (int j = result.length(); j >= 0; j--) {
            result = result.substring(0, j);

            if (check(result, str2) && check(result, str1)) {
                return result;
            }
        }

        return result;
    }

    boolean check(String divide, String str) {
        if (divide.length() < 1) {
            return false;
        }

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