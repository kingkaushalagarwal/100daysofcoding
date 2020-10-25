import java.util.*;
import java.io.*;
public class find_number_created_by_digit_1_3_5_7 {
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Solution sol = new Solution();
        long ans = sol.find(n);
        System.out.println(ans);
    }

    static class Solution{
        public long GP(int a,int r,int n){
            if (n==0)
                return 0;
            long temp = (long) (a*(Math.pow(r,n)-1))/(r-1);
            return temp;
        }
        public long calculate(List<Integer> array,int i,int[]allowed,long []dp,int length){
            //base case
            if (i>=array.size())
                return 1;

            long ans = 0L;
            for(int j=0;j<4;j++){
                if (array.get(i)>allowed[j])
                    ans+= dp[length-i-1];
                else{
                    if (array.get(i)==allowed[j])
                        ans+= calculate(array,i+1,allowed,dp,length);
                 }
            }
            return ans;

        }
        public long find(int n){
            long ans=0L;
            int allowed []=  {9,7,3,1};
            int length=0,num =n;
            List<Integer> array = new ArrayList<>();

            //creating dp array
            long dp[] = new long[19];
            for(int i=0;i<19;i++)
                dp[i]= (long) Math.pow(4,i);

            while (num!=0){
                int d = num%10;
                length+=1;
                array.add(d);
                num = (int)num/10;

            }
            Collections.reverse(array);
            long a= GP(4,4,length-1) ;
            long b=calculate(array,0,allowed,dp,length);
            ans = a+b;
            return ans;
        }
    }
}

