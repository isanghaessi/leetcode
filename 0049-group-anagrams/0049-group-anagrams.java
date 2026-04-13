class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anagrams = new HashMap();

        for (String s: strs) {
            String anagramAlpha = getAnagramAlpha(s);
            anagrams.putIfAbsent(anagramAlpha, new ArrayList());
            anagrams.get(anagramAlpha).add(s);
        }

        return anagrams.values().stream().toList();
    }

    String getAnagramAlpha(String str) {
        char[] alphas = str.replaceAll("[^a-z0-9]", "").toLowerCase().toCharArray();
        Arrays.sort(alphas);

        return new String(alphas);
    }
}