#Compliement of base 10 integer
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        number = 0
        p = 0
        if N == 0:
            return 1

        while N > 0:
            if N & 1 == 0:
                number += 2 ** p
            N = N >> 1
            p += 1
        return number