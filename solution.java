// POWER OF TWOO LEETCODE PROBLEM (IN TERMS OF JAVA)
class Solution {
    public boolean myFunc(int n) {
        if (n <= 0) {
            return false;
        }
        while (n % 2 == 0) {
            n = n / 2;
        }
        return n == 1;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int param1 = 16;
        boolean result = solution.myFunc(param1);
        System.out.println(result);
    }
}
