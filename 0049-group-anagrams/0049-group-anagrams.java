class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anagrams = new HashMap();

        for (String s: strs) {
            String anagramAlpha = getAnagramAlpha(s);
            anagrams.computeIfAbsent(anagramAlpha, (key) -> new ArrayList<>())
            .add(s);
        }

        return new ArrayList<>(anagrams.values());
    }

    String getAnagramAlpha(String str) {
        char[] alphas = str.toCharArray();
        Arrays.sort(alphas);

        return new String(alphas);
    }
}