public class Cubes {
    public boolean myFunc(int n) {
        
        long val = Math.abs((long) n);

        long root = Math.round(Math.pow(val, 1.0 / 3.0));

        return (root * root * root) == val;
    }

    // main function
    public static void main(String[] args) {
        Solution solution = new Solution();
        int param1 = 8;
        boolean result = solution.myFunc(param1);

        System.out.println(result);
    }
}
