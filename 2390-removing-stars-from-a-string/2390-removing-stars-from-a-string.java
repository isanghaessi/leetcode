class Solution {
    public String removeStars(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            char current = s.charAt(i);

            if (current != '*') {
                stack.push(current);
            } else {
                stack.pop();
            }
        }

        for (char st: stack) {
            sb.append(st);
        }

        return sb.reverse().toString();
    }
}