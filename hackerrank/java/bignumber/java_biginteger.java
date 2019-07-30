import java.io.*;
import java.util.*;
import java.math.BigInteger;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scanner = new Scanner(System.in);
        String s1 = scanner.nextLine();
        String s2 = scanner.nextLine();
        scanner.close();

        BigInteger b1 = new BigInteger(s1);
        BigInteger b2 = new BigInteger(s2);

        System.out.println(b1.add(b2));
        System.out.println(b1.multiply(b2));
    }
}

