class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        List<Integer> prevResult = collide(asteroids);
        while (true) {
            List<Integer> nextResult = collide(prevResult.stream().mapToInt(value -> value).toArray());

            if (prevResult.equals(nextResult)) {
                return prevResult.stream().mapToInt(value -> value).toArray();
            }
            
            prevResult = nextResult;
        }
    }

    private List<Integer> collide(int[] asteroids) {
        List<Integer> result = new ArrayList<>();

        int i = 0;
        while (i < asteroids.length) {
            List<Integer> rights = new ArrayList<>();
            while (i < asteroids.length && asteroids[i] > 0) {
                rights.add(asteroids[i]);
                i++;
            }

            List<Integer> lefts = new ArrayList<>();
            while (i < asteroids.length && asteroids[i] < 0) {
                lefts.add(asteroids[i]);
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