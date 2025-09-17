// the code of power of two in java 

public class poweroftwo
{
    public static boolean myFunc(int n)
    {
        if (n <= 0)
        {
            return false;
        }
        while (n % 2 ==0)
        {
            n = n / 2;
        }

        return n == 1;

    }

    public static void main(String[] args) {
        
        poweroftwo solution = new poweroftwo();
        int param1 = 16;
        boolean result = solution.myFunc(param1);
        System.out.println(result);

    }

}
