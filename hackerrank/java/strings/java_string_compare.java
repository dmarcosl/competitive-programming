import java.util.Scanner;

public class Solution {

    public static String getSmallestAndLargest(String s, int k) {
        String smallest = "";
        String largest = "";
        
        for (int i = 0; i < s.length() - k + 1; i++) {
            String subs = s.substring(i, k + i);
            if (smallest.isEmpty() || smallest.compareTo(subs) > 0) {
                smallest = subs;
            }
            if (largest.isEmpty() || largest.compareTo(subs) < 0) {
                largest = subs;
            }
        }
        
        return smallest + "\n" + largest;
    }


    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();
      
        System.out.println(getSmallestAndLargest(s, k));
    }
}

