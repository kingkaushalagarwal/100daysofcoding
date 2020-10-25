import java.util.*;
import java.io.*;
public class CoinChange {
    public static void main(String args[]) throws IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        Solution sol = new Solution();
        int n = Integer.parseInt(in.readLine());
        int []coins = new int[n];
        String input = in.readLine();
        String []arr =  input.split(" ");
        int k=0;
        for(String s:arr)
        { coins[k] = Integer.parseInt(s);
            k+=1;
        }
        int amount = Integer.parseInt(in.readLine());
        int ans = sol.coinChange(coins,amount);
        System.out.println(ans);
    }

    static class Solution {
        public int coinChange(int[] coins, int amount) {
            int l = coins.length;
            if (amount==0)
                return 0;
            int []dp = new int[amount+1];
            for(int i=0;i<(amount+1);i++)
                dp[i]=-1;
            dp[0]=0;
            for(int i=0;i<l;i++)
                for(int j=1;j<(amount+1);j++)
                    if( (j-coins[i])>=0 && dp[j-coins[i]]!=-1)
                        if(dp[j]==-1)
                            dp[j]=dp[j-coins[i]]+1;
                        else
                            dp[j]=Math.min(dp[j],dp[j-coins[i]]+1);
                    else
                        dp[j]=dp[j];
            return dp[amount];

        }
    }
}
