# Python3 implementation of the approach
from math import gcd as __gcd


# Function to return the maximum
# possible gcd after replacing
# a single element
def MaxGCD(a, n):
    # Prefix and Suffix arrays
    Prefix = [0] * (n + 2);
    Suffix = [0] * (n + 2);

    # Single state dynamic programming relation
    # for storing gcd of first i elements
    # from the left in Prefix[i]
    Prefix[1] = a[0];

    for i in range(2, n + 1):
        Prefix[i] = __gcd(Prefix[i - 1], a[i - 1]);

    # Initializing Suffix array
    Suffix[n] = a[n - 1];

    # Single state dynamic programming relation
    # for storing gcd of all the elements having
    # index greater than or equal to i in Suffix[i]
    for i in range(n - 1, 0, -1):
        Suffix[i] = __gcd(Suffix[i + 1], a[i - 1]);

    # If first or last element of
    # the array has to be replaced
    ans = max(Suffix[2], Prefix[n - 1]);

    # If any other element is replaced
    for i in range(2, n):
        ans = max(ans, __gcd(Prefix[i - 1],
                             Suffix[i + 1]));

    # Return the maximized gcd
    return ans;


# Driver code
if __name__ == "__main__":
    a = [6, 7, 8];
    n = len(a);

    print(MaxGCD(a, n));

# This code is contributed by AnkitRai01
