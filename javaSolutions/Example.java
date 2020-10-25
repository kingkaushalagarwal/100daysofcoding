import java.io.*;
import java.util.*;
public class Example {
    public static void ll(){
        LinkedList a = new LinkedList();
        a.add(1);
        a.add(2);
        a.add(3);
        a.removeFirst();
        System.out.println(a);
    }
    public static void main(String args[]) throws IOException {
        ll();
        char []ch = {'a','b','c'};
        String s = new String(ch);
        System.out.println(s);
//        int n;
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        n = Integer.parseInt(br.readLine());
//        String []words=new String[n];
//        for (int i=0;i<n;i++)
//        {
//            words[i]=br.readLine();
//        }
//        String ans = Main.lengthiestWord(words);
//        System.out.println(ans);

    }
    static class Main{
        public static String lengthiestWord(String [] words){
         String string= words[0];
         int n =words.length;
         int length= string.length();
         for(String s:words)
         {
             int l = s.length();
             if (l>length){
                 length =l ;
                 string = s;
             }
             else{
                 if(l==length && s.compareTo(string)<0)
                    string = s;
             }

         }

         return string;

        }

    }

}
