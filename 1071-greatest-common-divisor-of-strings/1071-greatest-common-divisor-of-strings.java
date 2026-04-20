class Solution {
    public String gcdOfStrings(String str1, String str2) {
        // if (str1.length() < str2.length()) {
        //     String temp = str1;
        //     str1 = str2;
        //     str2 = temp;
        // }

        if (!(str1 + str2).equals(str2 + str1)) {
            return "";
        }

        return str1.substring(0, greatCommonDivider(str1.length(), str2.length()));
    }

    int greatCommonDivider(int a, int b) {
        return b == 0 ? a : greatCommonDivider(b, a % b);
    }
}