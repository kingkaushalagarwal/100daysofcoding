import java.util.*;
import java.io.*;
public class Scramble_String {
    public static void main(String args[]){
        Solution sol = new Solution();
        String s1,s2;
        Scanner sc= new Scanner(System.in);
        s1 =sc.nextLine();
        s2 =sc.nextLine();
        boolean ans = sol.isScramble(s1,s2);
        System.out.println("Given Strings \n"+s1+"\n"+s2+"\n answer is: "+ans);
     return;
    }
    public static class Solution{

        public boolean isScramble(String s1,String s2)
        {
            if (s1.length()!=s2.length()) return false;
            int len = s1.length();
            boolean [][][]F = new boolean [len][len][len+1];
            for (int k=1;k<=len;++k)
                for(int i=0;i+k<=len;i++)
                    for(int j=0;j+k<=len;j++)
                        if (k==1)
                            F[i][j][k]=s1.charAt(i)==s2.charAt(j);
                        else for(int q=1; q<k && !F[i][j][k];q++){
                            F[i][j][k]=(F[i][j][q] && F[i+q][j+q][k-q])||(F[i][j+k-q][q]&&F[i+q][j][k-q]);

                        }
            return F[0][0][len];
        }
    }

}
