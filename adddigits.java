// add digits question :- of JAVA version 
class Solution {
    public int myFunc(int n) {
        if (n == 0) {
            return 0;
        } else {
            return 1 + (n - 1) % 9;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int param1 = 38;
        int result = solution.myFunc(param1);
        System.out.println(result);
    }
}
