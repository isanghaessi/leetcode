class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int gc = candies[0];
        for (int candy : candies) {
            gc = Math.max(gc, candy);
        }

        List<Boolean> result = new ArrayList<>();
        for (int candy : candies) {
            result.add(candy + extraCandies >= gc);
        }

        return result;
    }
}