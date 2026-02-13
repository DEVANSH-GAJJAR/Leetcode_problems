public class Cubes {
    public boolean myFunc(int n) {
        
        long val = Math.abs((long) n);

        // Calculate the cube root using Math.pow and round it to the nearest integer
        long root = Math.round(Math.pow(val, 1.0 / 3.0));

        // Verify if the cube of the calculated root equals the original magnitude
        return (root * root * root) == val;
    }

    // Example usage
    public static void main(String[] args) {
        Solution solution = new Solution();
        int param1 = 8;
        boolean result = solution.myFunc(param1);

        System.out.println(result);
    }
}
