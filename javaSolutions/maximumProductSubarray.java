import java.util.List;
import java.util.ArrayList;
import java.util.Scanner;
public class maximumProductSubarray {
    public static void main(String args[]){
        List<Integer> nums = new ArrayList<>();
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        for(String n : input.split(" "))
            nums.add(Integer.parseInt(n));

        Solution sol = new Solution();
        int ans =sol.maxProduct(nums);
        System.out.println(ans);
    }
    static class Solution {

        public int maxProduct(List<Integer> nums) {
            int r = nums.get(0);
            int imax=r,imin=r;
            for(int i=1;i<nums.size();i++)
            {
                if (nums.get(i)<0)
                {
                    int temp = imin;
                    imin = imax;
                    imax= temp;
                }
                imax = Math.max(imax*nums.get(i),nums.get(i));
                imin = Math.min(imin*nums.get(i),nums.get(i));
                r = Math.max(r,imax);

            }
            return r;
        }
    }
}
