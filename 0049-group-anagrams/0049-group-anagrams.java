class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anagrams = new HashMap<>();

        for(String str: strs) {
            char[] chars = str.toCharArray();
            Arrays.sort(chars);
            String sortedStr = new String(chars);
            anagrams.putIfAbsent(sortedStr, new ArrayList<>());
            anagrams.get(sortedStr).add(str);
        }

        return new ArrayList<>(anagrams.values());
    }
}