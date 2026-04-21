class Solution {
    public boolean closeStrings(String word1, String word2) {
        if (word1.length() != word2.length()) {
            return false;
        }

        int alphaLength = 'z' - 'a' + 1;

        int[] counter1 = new int[alphaLength];
        int[] counter2 = new int[alphaLength];

        for (char c: word1.toCharArray()) {
            counter1[c - 'a']++;
        }
        for (char c: word2.toCharArray()) {
            counter2[c - 'a']++;
        }

        for (int i = 0; i < alphaLength; i++) {
            int current1 = counter1[i];
            int current2 = counter2[i];

            if ((current1 > 0 && current2 <= 0) || (current2 > 0 && current1 <= 0)) {
                return false;
            }
        }

        Arrays.sort(counter1);
        Arrays.sort(counter2);

        for (int i = 0; i < alphaLength; i++) {
            int current1 = counter1[i];
            int current2 = counter2[i];

            if (current1 != current2) {
                return false;
            }
        }

        return true;
    }
}