#time limit exceed unable to optimize type two query
#only subtask 1 pass 10/100
import sysn
    if t==1:
        a[b-1]=k
    else:
        start = b-1;end = k-1
        #left to right
        if start==end:
            print(a[start])
        elif start<end:
            if h[end]>=h[start]:
                print(-1)
                continue
            tast=0;heightInd = None;
            for j in range(end,start-1,-1):
                if heightInd==None:
                    heightInd = j
                    tast += a[j]
                else:
                    if h[j]>h[heightInd]:
                        heightInd = j
                        tast += a[j]
            if heightInd!=start:
                print(-1)
            else:
                print(tast)
        else:
            if h[end] >= h[start]:
                print(-1)
                continue
            tast = 0;
            heightInd = None;
            for j in range( end,start + 1):
                if heightInd == None:
                    heightInd = j
                    tast += a[j]
                else:
                    if h[j] > h[heightInd]:
                        heightInd = j
                        tast += a[j]
            if heightInd != start:
                print(-1)
            else:
                print(tast)
