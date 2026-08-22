class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        List<Integer> prevResult = collide(Arrays.stream(asteroids).boxed().toList());
        while (true) {
            List<Integer> nextResult = collide(prevResult);

            if (prevResult.equals(nextResult)) {
                return prevResult.stream().mapToInt(value -> value).toArray();
            }
            
            prevResult = nextResult;
        }
    }

    private List<Integer> collide(List<Integer> asteroids) {
        List<Integer> result = new ArrayList<>();

        int i = 0;
        while (i < asteroids.size()) {
            List<Integer> rights = new ArrayList<>();
            while (i < asteroids.size() && asteroids.get(i) > 0) {
                rights.add(asteroids.get(i));
                i++;
            }

            List<Integer> lefts = new ArrayList<>();
            while (i < asteroids.size() && asteroids.get(i) < 0) {
                lefts.add(asteroids.get(i));
                i++;
            }

            result.addAll(collide(rights, lefts));
        }

        return result;
    }

    private List<Integer> collide(List<Integer> rights, List<Integer> lefts) {
        int r = rights.size() - 1;
        int l = 0;

        while (r >= 0 && l < lefts.size()) {
            if (rights.get(r) < -lefts.get(l)) {
                r--;
            } else if (rights.get(r) > -lefts.get(l)) {
                l++;
            } else {
                r--;
                l++;
            }
        }

        List<Integer> result = new ArrayList<>();
        if (r >= 0) {
            result.addAll(rights.subList(0, r + 1));
        }
        if (l < lefts.size()) {
            result.addAll(lefts.subList(l, lefts.size()));
        }

        return result;
    }
}