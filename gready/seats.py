#Interview Bit 
class Solution:
    # @param A : string
    # @return an integer
    def find(self, ind, pos, people):
        cost = 0;
        k = 1;
        n = len(people)

        for i in range(ind - 1, -1, -1):
            cost += abs(people[i] - (pos - k))
            k += 1
        k = 1
        for i in range(ind + 1, n):
            cost += abs(people[i] - (pos + k))
            k += 1
            return cost


def seats(self, A):
    people = []
    for i in range(len(A)):
        if A[i] == 'x':
            people.append(i)
    # total number of people are odd
    n = len(people)
    if n == 0:
        return 0
    if n % 2 == 1:
        ind = n // 2
        pos = people[ind]
        cost = self.find(ind, pos, people)
        return cost % (10 ** 7 + 3)
    else:
        ind1 = n // 2 - 1
        ind2 = n // 2
        pos1 = people[ind1]
        cost1 = self.find(ind1, pos1, people)
        pos2 = people[ind2]
        cost2 = self.find(ind2, pos2, people)
        return min(cost1, cost2) % (10 ** 7 + 3)





