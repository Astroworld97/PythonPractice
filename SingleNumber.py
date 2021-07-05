#source: https://leetcode.com/problems/single-number/submissions/
class Solution:

    def singleNumber(self, nums):
        d = dict()
        for i in nums:
            if i in d:
                newQuantity = d.get(i) + 1
                d.update({i: newQuantity})
            else:
                d.update({i: 1})
        for i in d.keys():
            num = d.get(i)
            if num == 1:
                return i
        return 1000

if __name__ == '__main__':
    nums = [2, 2, 1]
    s = Solution()
    x = s.singleNumber(nums)
    print(x)
