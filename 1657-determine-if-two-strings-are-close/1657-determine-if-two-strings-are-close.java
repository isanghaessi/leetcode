class Solution {
    public boolean closeStrings(String word1, String word2) {
        if (word1.length() != word2.length()) {
            return false;
        }

        Map<Character, Integer> counter1 = getCounter(word1);    
        Map<Character, Integer> counter2 = getCounter(word2);    

        return isPossible(counter1, counter2);
    }

    Map<Character, Integer> getCounter(String str) {
        Map<Character, Integer> counter = new HashMap<>();

        for (char c: str.toCharArray()) {
            counter.putIfAbsent(c, 0);
            counter.put(c, counter.get(c) + 1);
        }

        return counter;
    }

    boolean isPossible(Map<Character, Integer> counter1, Map<Character, Integer> counter2) {
        if (!counter1.keySet().equals(counter2.keySet())) {
            return false;
        }

        String valueString1 = counter1.values().stream().map((v) -> String.valueOf(v)).sorted().collect(Collectors.joining(""));
        String valueString2 = counter2.values().stream().map((v) -> String.valueOf(v)).sorted().collect(Collectors.joining(""));

        return valueString1.equals(valueString2);
    }
}