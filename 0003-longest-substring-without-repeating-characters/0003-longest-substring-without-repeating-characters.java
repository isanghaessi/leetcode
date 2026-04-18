class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> seen = new HashMap<>();

        int result = 0;

        int i = 0;
        int j = 0;
        while(j < s.length()) {
            char current = s.charAt(j);
            if (seen.containsKey(current)) {
                result = Math.max(result, j - i);
                
                int prev =  seen.get(current);
                while (i <= prev) {
                    seen.remove(s.charAt(i));
                    i++;
                }
            }

            seen.put(current, j);
            j++;
        }

        result = Math.max(result, j - i);

        return result;
    }
}