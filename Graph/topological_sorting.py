"""
Possibility of finishing all courses given pre-requisites
Problem Description

There are a total of A courses you have to take, labeled from 1 to A.
Some courses may have prerequisites, for example to take course 2 you have to first take course 1, which is expressed as a pair: [1,2].
So you are given two integer array B and C of same size where for each i (B[i], C[i]) denotes a pair.
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
Return 1 if it is possible to finish all the courses, or 0 if it is not possible to finish all the courses.

Problem Constraints
1 <= A <= 6*104
1 <= length(B) = length(C) <= 105
1 <= B[i], C[i] <= A

Input Format
The first argument of input contains an integer A, representing the number of courses.
The second argument of input contains an integer array, B.
The third argument of input contains an integer array, C.

Output Format
Return 1 if it is possible to finish all the courses, or 0 if it is not possible to finish all the courses.

Example Input
Input 1:
 A = 3
 B = [1, 2]
 C = [2, 3]
Input 2:
 A = 2
 B = [1, 2]
 C = [2, 1]

Example Output
Output 1:
 1
Output 2:
 0
"""
from collections import deque, defaultdict


class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        indegree = [0] * A

        graph = defaultdict(list)
        for i in range(len(B)):
            u = B[i] - 1
            v = C[i] - 1
            graph[u].append(v)
            indegree[v] += 1
        queue = deque()
        for i in range(A):
            if indegree[i] == 0:
                queue.append(i)
        ans = []
        while len(queue) != 0:
            u = queue.popleft()
            ans.append(u)
            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
        if len(ans) == A:
            return 1
        else:
            return 0


