import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;

public class PartitionLabels {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        String string = sc.next();
        Solution sol = new Solution();
        List<Integer> ll= sol.partitionLabels(string);
        for(int i=0;i<ll.size();i++)
            System.out.print(ll.get(i)+" ");

    }

    static class Solution {
        public List<Integer> partitionLabels(String S) {
            int [] last = new int [26];
            for(int i=0;i<S.length();i++)
                last[S.charAt(i)-'a']=i;
            int j=0,anchor=0;
            List<Integer> ans = new ArrayList();
            for(int i=0;i<S.length();i++)
            {
                j = Math.max(j,last[S.charAt(i)-'a']);
                if(i==j){
                    ans.add(i-anchor+1);
                    anchor=i+1;
                }
            }
            return ans;
        }
    }
}
