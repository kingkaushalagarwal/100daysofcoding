package november_long_leetcode;
import java.io.*;
public class Q5 {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int []position = new int[n];
        String [] s = br.readLine().split(" ");
        int k=0;
        for(String st:s){
            position[k] = Integer.parseInt(st);
            k+=1;
        }
        int answer = Solution.minCostToMoveChips(position);
        System.out.println("answer : " + answer);

    }

    static class Solution {
        public static int minCostToMoveChips(int[] position) {
            int odd = 0;
            int even = 0;
            for (int i=0;i<position.length;i++)
                if(position[i]%2==1)
                    odd+=1;  //odd value
                else
                    even+=1; //even value
            if (odd==0 || even==0)
                return 0;
            else
                return Math.min(even,odd);
        }
    }
}
