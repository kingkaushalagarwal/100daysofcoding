class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        l = list(A)
        freq = [0] * 26
        visited = [0] * 26
        i = 0;
        stack = []
        for x in A:
            ind = ord(x) - 97
            freq[ind] += 1

        while i < len(A):
            ch = A[i]
            ind = ord(ch) - 97
            if len(stack) == 0 or ch >= stack[-1]:
                if visited[ind] == 0:
                    stack.append(ch)
                    visited[ind] = 1
                freq[ind] -= 1
                i += 1
            elif ch < stack[-1]:
                if visited[ind] == 1:
                    freq[ind] -= 1
                    i += 1
                else:
                    while len(stack) != 0 and ch < stack[-1]:
                        prev_index = ord(stack[-1]) - 97
                        if freq[prev_index] > 0:
                            stack.pop()
                            visited[prev_index] = 0
                        else:
                            break

                    if visited[ind] == 0:
                        stack.append(ch)
                        freq[ind] -= 1
                        visited[ind] = 1
                    i += 1

        return ''.join(stack)