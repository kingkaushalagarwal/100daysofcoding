import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.List;
import java.util.Scanner;

public class MinimumAddition {
    public static int [][] preprocessing(int [] nums)
    {   int n = nums.length;
        int [][] new_array =new int [n][32];
        int value;
        int k=0;
        for(int i=0;i<nums.length;i++)
        {
            int bits[] = new int[32];
            value = nums[i];
            k=0;
            while (value>0==true){
                if (value%2 == 1) {
                    bits[k]+=1;
                }
                value = value>>1;
                k+=1;
            }
            for(int j=0;j<32;j++) {
                if (i==0)
                    new_array[i][j] = bits[j];
                else
                    new_array[i][j] = bits[j] + new_array[i-1][j];
            }

        }

        return new_array;

    }
    public static void main(String args[] ) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int []  nums = new int[n];
        Scanner sc = new Scanner(System.in);
        for(int i=0;i<n;i++)
            nums[i] = sc.nextInt();
        int q = Integer.parseInt(String.valueOf(br.readLine()));
        int l,r;
        int new_array[][] = preprocessing(nums);
//        for(int i=0;i<new_array.length;i++) {
//            for (int j = 0; j < 32; j++)
//                System.out.print(new_array[i][j] + " ");
//            System.out.println();
//        }

        for(int i=0;i<q;i++)
        {
                    String st = br.readLine();
            String [] h = st.split(" ");
            l = Integer.parseInt(h[0])-1;
            r = Integer.parseInt(h[1])-1;
//          l = sc.nextInt()-1;
//          r = sc.nextInt()-1;
            int b,diff;
            double number;
            double minn = Math.pow(10,30);

            for(int k=0;k<32;k++)
            {   b =0;
                if((l-1)>=0)
                    b = new_array[l-1][k];
                diff = new_array[r][k]-b;
                number = ((r-l+1 - diff)*Math.pow(2,k));
                minn = Math.min(minn,number);
            }
            System.out.println((int)minn);
        }


    }
}
