class Solution {
    public String reverseWords(String s) {
        Deque<String> words = new ArrayDeque<>();
        StringBuilder sb = new StringBuilder();

        int i = 0;
        while(i < s.length()) {
            char current = s.charAt(i);

            if (Character.isLetterOrDigit(current)) {
                sb.append(current);
                i++;
            } else {
                if (sb.length() > 0) {
                    words.push(sb.toString());
                    sb.setLength(0);
                }

                while(i < s.length() && !Character.isLetterOrDigit(s.charAt(i))) {
                    i++;
                }
            }
        }

        if (sb.length() > 0) {
            words.push(sb.toString());
            sb.setLength(0);
        }

        while (words.size() > 0) {
            sb.append(words.pop());

            if (words.size() > 0) {
                sb.append(" ");
            }
        }

        return sb.toString();
    }
}