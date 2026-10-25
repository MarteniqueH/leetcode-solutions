

class Solution {
    public long maximumCoins(int[][] coins, int k) {
        return Math.max(slide(coins, k), slide(negateLeftRight(coins), k));
    }

    private int[][] negateLeftRight(int[][] coins) {
        int[][] res = new int[coins.length][3];
        for (int i = 0; i < coins.length; i++) {
            res[i][0] = -coins[i][1];
            res[i][1] = -coins[i][0];
            res[i][2] = coins[i][2];
        }
        return res;
    }

    private long slide(int[][] coins, int k) {
        Arrays.sort(coins, (a, b) -> Integer.compare(a[0], b[0]));
        long res = 0;
        long windowSum = 0;
        int j = 0;

        for (int i = 0; i < coins.length; i++) {
            int li = coins[i][0];
            int ri = coins[i][1];
            int ci = coins[i][2];

            int rightBoundary = li + k;

            while (j + 1 < coins.length && coins[j + 1][0] < rightBoundary) {
                int lj = coins[j][0];
                int rj = coins[j][1];
                int cj = coins[j][2];
                windowSum += (long) (rj - lj + 1) * cj;
                j++;
            }

            long last = 0;
            if (j < coins.length && coins[j][0] < rightBoundary) {
                int lj = coins[j][0];
                int rj = coins[j][1];
                int cj = coins[j][2];
                last = (long) (Math.min(rightBoundary - 1, rj) - lj + 1) * cj;
            }

            res = Math.max(res, windowSum + last);
            windowSum -= (long) (ri - li + 1) * ci;
        }

        res = Math.max(res, windowSum);
        return res;
    }
}
        

