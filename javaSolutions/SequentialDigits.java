import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;
public class SequentialDigits {
    public static void main(String args[]){
        Solution sol = new Solution();
        Scanner sc = new Scanner(System.in);
        int low=sc.nextInt();
        int high =sc.nextInt();
        List <Integer> ans = sol.sequentialDigits(low,high);
        for(int i=0;i<ans.size();i++)
            System.out.print(ans.get(i)+" ");
        System.out.println();
    }
    static class Solution {
        public List<Integer> sequentialDigits(int low, int high) {
            List<Integer> arr = new ArrayList<>();
            int num=0;
            for(int i=1;i<10;i++)
            {   num = 0;
                for(int j=i;j<10;j++)
                {
                    num = num*10+j;
                    arr.add(num);
                }
            }
            Collections.sort(arr);
            List<Integer> ans = new ArrayList<>();
            for(int i=0;i<arr.size();i++)
            {
                if (arr.get(i)>=low && arr.get(i)<=high)
                    ans.add(arr.get(i));
            }
            return ans;
        }
    }
}
