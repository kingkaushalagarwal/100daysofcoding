import java.util.Scanner;

public class LengthOfLastWord {
    public static void main(String args[]){
        Solution sol = new Solution();
        Scanner sc = new Scanner(System.in);
        String word = sc.nextLine();
        int ans = sol.lengthOfLastWord(word);
        System.out.println(ans);
    }
    static class Solution {
        public int lengthOfLastWord(String string) {
            int n = string.length();
            if (n==0)
                return 0;
            String [] word = string.split(" ");
            if(word.length==0)
                return 0;
            int wl = word.length;
            return word[wl-1].length();

        }
    }
}