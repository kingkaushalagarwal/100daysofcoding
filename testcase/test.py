from math import ceil, log2;

def getMid(s, e):
    return s + (e - s) // 2;

def getSumUtil(arr,st, ss, se, qs, qe, si):
    if (qs <= ss and qe >= se):
        return st[si];

    if (se < qs or ss > qe):
        return 0;
    mid = getMid(ss, se);
    a = 0
    if (arr[mid]==arr[mid+1]):
        a =1
    return a + getSumUtil(arr,st, ss, mid, qs, qe, 2 * si + 1) + getSumUtil(arr,st, mid + 1, se, qs, qe, 2 * si + 2);



def updateValueUtil(st, ss, se, i, diff, si,arr):
    if (i < ss or i > se):
        return 0
    # st[si] = st[si] + diff;
    if (ss == se):
        st[si] = 0;
        return 0;
    if (se != ss):
        mid = getMid(ss, se);
        a=0
        if arr[mid]==arr[mid+1]:
            a=1
        st[i] = a + updateValueUtil(st, ss, mid, i,diff, 2 * si + 1,arr)+ updateValueUtil(st, mid + 1, se, i,diff, 2 * si + 2,arr);
        return st[i];

def updateValue(arr, st, n, i, new_val):
    if (i < 0 or i > n - 1):
        print("Invalid Input", end="");
        return;

    arr[i] = new_val;

    updateValueUtil(st, 0, n - 1, i, new_val, 0,arr);


def getSum(arr,st, n, qs, qe):
    if (qs < 0 or qe > n - 1 or qs > qe):
        print("Invalid Input", end="");
        return -1;

    return getSumUtil(arr,st, 0, n - 1, qs, qe, 0);

def constructSTUtil(arr, ss, se, st, si):
    if (ss == se):
        st[si] = 0;
        return 0 ;

    mid = getMid(ss, se);
    a =0
    if arr[mid]==arr[mid]+1:
        a=1
    st[si] = constructSTUtil(arr, ss, mid, st, si * 2 + 1) +  constructSTUtil(arr, mid + 1, se, st, si * 2 + 2) + a;
    return st[si];



def constructST(arr, n):
    x = (int)(ceil(log2(n)));
    max_size = 2 * (int)(2 ** x) - 1;
    st = [0] * max_size;
    constructSTUtil(arr, 0, n - 1, st, 0);
    return st;


# Driver Code
if __name__ == "__main__":
    arr = [1, 1,3,1,1,10,3];
    n = len(arr);
    st = constructST(arr, n);
    print("Sum of values in given range = ",
          getSum(arr,st, n, 0, len(arr)-1));
    updateValue(arr, st, n, 1, 10);

    print("Updated sum of values in given range = ",
          getSum(arr,st, n, 1, 3), end="");
