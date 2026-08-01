class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int gc = Arrays.stream(candies)
            .max()
            .getAsInt();

        List<Boolean> result = new ArrayList<>();
        for (int candy : candies) {
            result.add(candy + extraCandies >= gc);
        }

        return result;
    }
}