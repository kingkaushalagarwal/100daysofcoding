import java.util.Scanner;
public class HouseRobber {
    public static void main(String args[])
    {
        Solution sol = new Solution();
        Scanner sc = new Scanner(System.in);
        int n;
        n = sc.nextInt();
        int nums[]=new int[n];
        for(int i=0;i<n;i++)
            nums[i]=sc.nextInt();
        int ans = sol.rob(nums);
        System.out.println(ans);

    }
    static class Solution {
        public int rob(int[] nums) {
            int n = nums.length;
            if(n==0)
                return 0;
            if (n==1)
                return nums[0];
            int p2 = nums[0];
            int p1 = Math.max(p2,nums[1]);
            int temp;
            for(int i=2;i<n;i++)
            {
                temp = Math.max(p1,p2+nums[i]);
                p2= p1;
                p1 = temp;
            }
            return p1;


        }
    }
}
//[2,7,9,3,1]