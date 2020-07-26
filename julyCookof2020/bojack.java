/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
    	Scanner sc =  new Scanner(System.in);
	    int n;
        int t = sc.nextInt();
		while(t-->0){
			n = sc.nextInt();
			System.out.print(2*n+" ");
			for(int i=0;i<n;i++)
				System.out.print("a");
			for(int i=0;i<n;i++)
				System.out.print("b");
			System.out.println();


	    }
    }
}

