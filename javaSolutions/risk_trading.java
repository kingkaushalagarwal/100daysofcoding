import java.io.*;
import java.text.DecimalFormat;
import java.util.*;
import java.util.stream.Stream;

public class risk_trading {

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException  {
        Scanner in = new Scanner(System.in);

//        int n = in.nextInt();
//        int m = in.nextInt();

//        double[] p = new double[n];
//        double[] x = new double[n];
//        double[] y = new double[n];
//        double result = 0;

        //get input
//        for(int i = 0; i < n; i++)
//            p[i] = in.nextDouble();
//        for(int i = 0; i < n; i++)
//            x[i] = in.nextDouble();
//        for(int i = 0; i < n; i++)
//            y[i] = in.nextDouble();
//        result = Solution.maximumExpectedMoney(n,m,p,x,y);
//        System.out.println(String.format("%.2f",result));
        DecimalFormat df = new DecimalFormat("#.##");
        float num= Float.parseFloat(df.format(2.456345)) + 4;
        System.out.println(num);



    }
    static class Solution {

        // You may change this function parameters
        public static double maximumExpectedMoney(int n, int m, double[] p, double[] x, double[] y)  {

            float ans = 0;
            for (int i=0;i<x.length;i++){
                x[i] = x[i]*p[i] - y[i]*(1-p[i]);
            }
            Arrays.sort(x);

            for(int i=x.length-1;i>x.length-1-m;i--){
                if (x[i]<0)
                    break;
                ans+=x[i];
            }
            return ans;
        }



    }

}
