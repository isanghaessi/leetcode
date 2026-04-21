class Solution {
    public int[] countBits(int n) {
        int[] result = new int[n + 1];

        List<Integer> bin = new ArrayList<>();
        bin.add(0);
        
        for (int i = 1; i <= n; i++) {
            result[i] = plus(bin);
        }

        return result;
    }

    int plus(List<Integer> bin) {
        int i = 0;
        bin.set(i, bin.get(i) + 1);

        while (bin.get(i) > 1) {
            bin.set(i, 0);

            i++;

            if (i >= bin.size()) {
                bin.add(0);
            }
            bin.set(i, bin.get(i) + 1);
        }

        return bin.stream().filter((v) -> v == 1).toList().size();
    }
}