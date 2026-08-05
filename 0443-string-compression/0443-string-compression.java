class Solution {
    public int compress(char[] chars) {
        if (chars.length <= 1) {
            return 1;
        }

        char[] result = new char[chars.length];
        int ri = 0;

        char gc = chars[0];
        int count = 1;
        for (int i = 1; i < chars.length; i++) {
            char cc = chars[i];

            if (gc == cc) {
                count++;
            } else {
                result[ri++] = gc;
                if (count > 1) {
                    ri = print(result, ri, String.valueOf(count));
                }

                gc = cc;
                count = 1;
            }
        }

        result[ri++] = gc;
        if (count > 1) {
            ri = print(result, ri, String.valueOf(count));
        }

        for (int i = 0; i < ri; i++) {
            chars[i] = result[i];
        }

        return ri;
    }

    private int print(char[] array, int index, String str) {
        char[] strChars = str.toCharArray();
        for(int i = 0; i < strChars.length; i++) {
            array[index + i] = strChars[i];
        }

        return index + str.length();
    }
}