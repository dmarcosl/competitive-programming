import java.util.Scanner;

public class Solution {

    static boolean isAnagram(String a, String b) {
        
        if (a.length() != b.length()) {
            return false;
        }

        String distinct = "";
        for(String s : a.toLowerCase().split("")) {
            if (distinct.indexOf(s) > 0) {
                continue;
            }
            distinct += s;

            int aNum = a.toLowerCase().split(s, -1).length - 1;
            int bNum = b.toLowerCase().split(s, -1).length - 1;
            
            if (aNum != bNum) {
                return false;
            }
        }
        return true;
    }

  public static void main(String[] args) {
    
        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}

