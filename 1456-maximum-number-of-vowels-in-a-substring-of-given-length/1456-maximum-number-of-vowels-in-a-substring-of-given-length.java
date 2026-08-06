class Solution {
    public int maxVowels(String s, int k) {
        Set<Character> vowels = new HashSet<>();
        vowels.add('a');
        vowels.add('e');
        vowels.add('i');
        vowels.add('o');
        vowels.add('u');

        int result = 0;
        int vc = 0;
        for (int i = 0; i < k; i++) {
            if (vowels.contains(s.charAt(i))) {
                vc++;
            }
        }
        result = vc;

        int l = 0;
        for (int r = k; r < s.length(); r++) {
            if (vowels.contains(s.charAt(l++))) {
                vc--;
            }
            if (vowels.contains(s.charAt(r))) {
                vc++;
            }

            if (result < vc) {
                result = vc;
            }
        }

        return result;
    }
}