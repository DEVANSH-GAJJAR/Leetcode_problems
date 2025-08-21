class Solution {
    public int mySqrt(int x) {
        if (x < 2) return x; // Handle 0 and 1 directly
        
        int result = 1;
        while (result * result <= x) {
            result++;
        }
        return result - 1; // Return the floor value
    }
}
