import java.util.Scanner;
public class BullsAndCow {
    public static void main(String args[]){
        String secret ,guess;
        Scanner sc = new Scanner (System.in);
        secret = sc.next();
        guess = sc.next();
        Solution sol = new Solution();
        String ans = sol.getHint(secret,guess);
        System.out.println(ans);
    }

    static class Solution {
        public String getHint(String secret, String guess) {
            int [] digit1= new int[10];
            int [] digit2 = new int[10];
            int bull=0,cow=0;
            for(int i=0;i<secret.length();i++)
            {
                if(i<guess.length() && guess.charAt(i)==secret.charAt(i))
                    bull+=1;
                else
                    digit1[secret.charAt(i)-'0']+=1;
            }
            for(int i=0;i<guess.length();i++){
                if(i<secret.length() && secret.charAt(i)==guess.charAt(i))
                    continue;
                else
                    digit2[guess.charAt(i)-'0']+=1;

            }

            for(int i=0;i<10;i++)
                cow+= Math.min(digit1[i],digit2[i]);
            String ans = String.valueOf(bull)+"A"+String.valueOf(cow)+"B";
            return ans;


        }
    }
}
