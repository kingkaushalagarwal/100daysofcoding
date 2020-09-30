import java.util.*;
public class FindTheDifference {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        String s,t;
        s = sc.nextLine();
        t = sc.nextLine();
        Solution sol = new Solution();
        char ans = sol.findTheDifference(s,t);
        System.out.println("answer: "+ ans);
    }
    static class Solution {
        public char findTheDifference(String s, String t) {
            int [] letters = new int [26];
            int l1=s.length();
            int l2 = t.length();
            for(int i=0;i<s.length();i++)
            {    letters[s.charAt(i)-'a']-=1;
                letters[t.charAt(i)-'a']+=1;
            }
            letters[t.charAt(l2-1)-'a']+=1;
            char ch='a';
            for(int i=0;i<26;i++)
                if (letters[i]>0)
                    ch +=i;
            return ch;
        }
    }
}
