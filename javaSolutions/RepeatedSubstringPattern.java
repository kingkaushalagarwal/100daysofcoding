import java.util.*;
import java.io.*;
public class RepeatedSubstringPattern {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String string = br.readLine();
        boolean ans = repeatedSubStringPattern(string);
        System.out.println(ans);
    }

    public static boolean repeatedSubStringPattern(String str){
        int l = str.length();
        for(int i= l/2;i>=1;i--)
        {   if(l%i==0)
            {
                int m = l/i;
                String subS = str.substring(0,i);
                StringBuilder sb = new StringBuilder();
                for(int j=0;j<m;j++) {
                    sb.append(subS);
                }
                if (sb.toString().equals(str)) return true;

            }
        }

        return false;
    }
}
