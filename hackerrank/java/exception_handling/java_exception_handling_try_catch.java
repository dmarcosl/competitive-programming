import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s1 = scanner.nextLine();
        String s2 = scanner.nextLine();
        scanner.close();

        try {
            Integer i1 = Integer.valueOf(s1);
            Integer i2 = Integer.valueOf(s2);

            if (i2 == 0) {
                System.out.println("java.lang.ArithmeticException: / by zero");
                return;
            }
            System.out.println(i1 / i2);
        } catch (Exception e) {
            System.out.println("java.util.InputMismatchException");
        }
    }
}

