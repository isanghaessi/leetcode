/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

public class Solution extends GuessGame {
    public int guessNumber(int n) {
        return check(0, n);
    }

    int check(int l, int r) {
        int mid = (int)(((long)l + r) / 2);
        int guessed = guess(mid);

        if (guessed == 0) {
            return mid;
        } else if (guessed < 0) {
            return check(l, mid - 1);
        } else {
            return check(mid + 1, r);
        }
    }
}