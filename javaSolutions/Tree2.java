import java.util.*;

public class Tree2 {
    public static void main(String args[]){
        int t,n;
        Scanner sc = new Scanner(System.in);
        Set<Integer> s;
        Integer []arr;
        t =sc.nextInt();
        while(t-->0)
        {   n = sc.nextInt();
            arr= new Integer[n];
            for(int j=0;j<n;j++)
                arr[j] = sc.nextInt();
            s = new HashSet<Integer>();
            s.addAll(Arrays.asList(arr));
            if(s.contains(0))
                System.out.println(s.size()-1);
            else
                System.out.println(s.size());

        }

    }
}
