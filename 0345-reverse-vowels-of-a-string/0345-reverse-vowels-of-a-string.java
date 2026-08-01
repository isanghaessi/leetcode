class Solution {
    public String reverseVowels(String s) {
        Set<Character> vowels = new HashSet<>();
        vowels.add('a');
        vowels.add('e');
        vowels.add('i');
        vowels.add('o');
        vowels.add('u');
        vowels.add('A');
        vowels.add('E');
        vowels.add('I');
        vowels.add('O');
        vowels.add('U');

        List<Character> stack = new ArrayList<>();
        for (char c : s.toCharArray()) {
            if (vowels.contains(c)) {
                stack.add(c);
            }
        }

        StringBuilder sb = new StringBuilder();

        for (char c : s.toCharArray()) {
            if (vowels.contains(c)) {
                int lastIndex = stack.size() - 1;
                char current = stack.get(lastIndex);
                stack.remove(lastIndex);

                sb.append(current);
            } else {
                sb.append(c);
            }
        }

        return sb.toString();
    }
}