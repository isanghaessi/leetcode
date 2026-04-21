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
            if (counter.containsKey(c)) {
                counter.put(c, counter.get(c) + 1);
            } else {
                counter.put(c, 1);
            }
        }

        return counter;
    }

    boolean isPossible(Map<Character, Integer> counter1, Map<Character, Integer> counter2) {
        Set<Character> keys1 = counter1.keySet();
        Set<Character> keys2 = counter2.keySet();

        if (!keys1.equals(keys2)) {
            return false;
        }

        List<Integer> values1 = counter1.values().stream().sorted().toList();
        List<Integer> values2 = counter2.values().stream().sorted().toList();

        for (int i = 0; i < values1.size(); i++) {
            if (!values1.get(i).equals(values2.get(i))) {
                return false;
            }
        }

        return true;
    }
}