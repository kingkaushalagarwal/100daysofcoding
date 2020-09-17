#Largest time for given digit
#https://leetcode.com/explore/featured/card/september-leetcoding-challenge/554/week-1-september-1st-september-7th/3445/
class Solution:
    def convert(self, arr, l):
        return [arr[x] for x in l]

    def checkValid(self, arr, M):
        l = self.convert(arr, M)
        HH = l[0] * 10 + l[1]
        MM = l[2] * 10 + l[3]
        if HH >= 0 and HH <= 23 and MM >= 0 and MM <= 59:
            return True
        else:
            return False

    def compareValue(self, arr, m1, m2):
        l1 = self.convert(arr, m1)
        l2 = self.convert(arr, m2)
        HH1 = l1[0] * 10 + l1[1]
        MM1 = l1[2] * 10 + l1[3]
        HH2 = l2[0] * 10 + l2[1]
        MM2 = l2[2] * 10 + l2[3]
        if HH1 > HH2:
            return m1
        if HH2 > HH1:
            return m2
        if MM1 > MM2:
            return m1
        if MM2 > MM1:
            return m2
        return m1

    def find(self, arr, k, l, maxx):
        if k == 4:
            if self.checkValid(arr, l) == True:
                if maxx[0] == None:
                    maxx[0] = l
                else:
                    maxx[0] = self.compareValue(arr, l, maxx[0])
        for i in range(4):
            if i not in l:
                self.find(arr, k + 1, l + [i], maxx)

    def largestTimeFromDigits(self, arr: List[int]) -> str:
        maxx = [None]
        self.find(arr, 0, [], maxx)
        if maxx[0] == None:
            return ""
        else:
            l = self.convert(arr, maxx[0])
            return str(l[0]) + str(l[1]) + ":" + str(l[2]) + str(l[3])
