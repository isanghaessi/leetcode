class Solution {
    public int compress(char[] chars) {
        if (chars.length <= 1) {
            return 1;
        }

        StringBuilder sb = new StringBuilder();

        char gc = chars[0];
        int count = 1;
        for (int i = 1; i < chars.length; i++) {
            char cc = chars[i];

            if (gc == cc) {
                count++;
            } else {
                sb.append(gc);
                if (count > 1) {
                    sb.append(String.valueOf(count));
                }

                gc = cc;
                count = 1;
            }
        }

        sb.append(gc);
        if (count > 1) {
            sb.append(String.valueOf(count));
        }

        char[] result = sb.toString().toCharArray();
        for (int i = 0; i < result.length; i++) {
            chars[i] = result[i];
        }

        return result.length;
    }
}