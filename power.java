class power {
    public boolean myFunc(int n) {
        if (n <= 0) {
            return false;
        }
        while (n % 3 == 0) {
            n = n / 3;
        }
        return n == 1;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int param1 = 27;
        boolean result = solution.myFunc(param1);
        System.out.println(result);
    }
}
