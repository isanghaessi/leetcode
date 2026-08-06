class Solution {
    public int maxVowels(String s, int k) {
        Set<Character> vowels = new HashSet<>();
        vowels.add('a');
        vowels.add('e');
        vowels.add('i');
        vowels.add('o');
        vowels.add('u');

        int[] sa = new int[s.length()];

        for (int i = 0; i < s.length(); i++) {
            if (vowels.contains(s.charAt(i))) {
                sa[i]++;
            }
        }

        int current = 0;
        int result = 0;
        for (int i = 0; i < k; i++) {
            current += sa[i];
        }
        result = current;

        int l = 0;
        for (int r = k; r < sa.length; r++) {
            current = current - sa[l++] + sa[r];

            if (current > result) {
                result = current;
            }
        }

        return result;
    }
}