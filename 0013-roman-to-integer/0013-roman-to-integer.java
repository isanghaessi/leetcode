class Solution {
    public int romanToInt(String s) {
        Map<String, Integer> symbols = new HashMap<>();
        symbols.put("I", 1);
        symbols.put("V", 5);
        symbols.put("X", 10);
        symbols.put("L", 50);
        symbols.put("C", 100);
        symbols.put("D", 500);
        symbols.put("M", 1000);
        symbols.put("IV", 4);
        symbols.put("IX", 9);
        symbols.put("XL", 40);
        symbols.put("XC", 90);
        symbols.put("CD", 400);
        symbols.put("CM", 900);

        int result = 0;
        int i = 0;
        while (i < s.length()) {
            if (i + 1 < s.length()) {
                String doubleNumber = s.substring(i, i + 2);
                if (symbols.containsKey(doubleNumber)) {
                    result += symbols.get(doubleNumber);
                    i += 2;
                } else {
                    result += symbols.get(s.substring(i, i + 1));
                    i++;    
                }
            } else {
                result += symbols.get(s.substring(i, i + 1));
                i++;
            }
        }

        return result;
    }
}