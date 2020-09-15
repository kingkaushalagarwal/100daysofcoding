import java.util.*;

class Solution{

    public int wordBreak(String s, ArrayList<String> B){
        boolean [] t = new boolean[s.length()+1];
        t[0]=true;
        Set<String> dict = new HashSet<>(B);
        for(int i=0;i<s.length();i++){
            if(!t[i])
                continue;
            for(String a:dict){
                int len = a.length();
                int end = i+len;
                if (end > s.length())
                    continue;

                if(t[end]) continue;
                if(s.substring(i,end).equals(a))
                    t[end] = true;

            }
        }

        return t[s.length()]?1:0;
    }
}