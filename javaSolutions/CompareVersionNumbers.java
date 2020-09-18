import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class CompareVersionNumbers {
    public static void main(String args[]){
        Solution sol = new Solution();
        String version1,version2;
        Scanner sc = new Scanner(System.in);
        version1 = sc.next();
        version2 = sc.next();
        int ans = sol.compareVersion1(version1,version2);
        System.out.println(ans);
    }
    static class Solution {
        public int compareVersion2(String version1 ,String version2)
        {
            String [] levels1 = version1.split("\\.");
            String [] levels2 = version2.split("\\.");
            int length = Math.max(levels1.length,levels2.length );
            for(int i=0;i<length;i+=1)
            {
                Integer v1 = i < levels1.length ? Integer.parseInt(levels1[i]):0;
                Integer v2 = i<levels2.length ? Integer.parseInt(levels2[i]):0;
                int compare= v1.compareTo(v2);
                if (compare!=0)
                    return compare;
            }
            return 0;
        }

        public int compareVersion1(String version1, String version2) {
            List<Integer> st1 = new ArrayList();
            List<Integer> st2 = new ArrayList();

            for (String s : version1.split("\\."))
                st1.add(Integer.parseInt(s));
            for (String s : version2.split("\\."))
                st2.add(Integer.parseInt(s));
            int l1= st1.size();
            int l2 = st2.size();
            int i=0,j=0;
            while (i<l1 && j<l2)
            {   if (st1.get(i) <st2.get(j))
                    return -1;
                else
                    if (st1.get(i)>st2.get(j))
                        return 1;
                    else{
                        i+=1;
                        j+=1;
                    }

            }
            while(i<l1) {
                if (st1.get(i) != 0)
                    return 1;
                i+=1;
            }
            while(j<l2){
                if(st2.get(j)!=0)
                    return -1;
                j+=1;
            }
            int num =10;
            String str = String.valueOf(num);
            return 0;
        }
    }
}
