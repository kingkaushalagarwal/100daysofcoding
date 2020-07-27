class Solution {
    public int minCut(String string) {
    int n = string.length();
    boolean [][]p = new boolean [n][n];
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
            p[i][j]=false;
    for(int i=0;i<n;i++)
        p[i][i]=true;
        
    for(int l=2;l<n+1;l++)    
        for(int i=0;i<n-l+1;i++)
        {
            int j=i+l-1;
            if(l==2)
            {    if (string.charAt(i)==string.charAt(j))
                    p[i][j]=true;
            }
            else
                if (string.charAt(i)==string.charAt(j) && p[i+1][j-1]==true)
                    p[i][j]=true;
            
        }
        
    int []dp =new int [n];
    for(int i=0;i<n;i++)
        dp[i]=-1;
    for(int i=0;i<n;i++)
    {    if (p[0][i]==true)
            dp[i]=0;
        if(dp[i]!=-1)
            for(int j=i+1;j<n;j++)
                if(p[i+1][j]==true)
                    if (dp[j]>dp[i]+1 || dp[j]==-1)
                        dp[j]=dp[i]+1;
    }                   
        
    System.out.println(dp[n-1]);
        
    }
}

