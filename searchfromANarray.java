import java.util.*;
import java.util.Scanner;

public class leetcode1 {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);

        // taking the size as input
        System.out.println("Enter the size of array:- ");
        int size = scanner.nextInt();

        int[] array = new int[size];

        // enter elements asarray
        System.out.println("Enter the  " + size + " elements of an array");
        for (int i = 0; i < size; i++) {
            array[i] = scanner.nextInt();
        }
        // take the value

        System.out.println("Enter the value to search ");
        int value = scanner.nextInt();

        // find the index

        int index = -1;
        for (int i = 0; i < array.length; i++) {
            if (array[i] == value) {
                index = i;
                break;

            }
        }
        // output
        if (index != -1) {
            System.out.println("Value is " + value + " and position:- " + index);
        } else {
            System.out.println("value is not found ");
        }
    }
}