def singleNumber(self, nums: list) -> int:
    d = dict()
    for i in nums:
        if i in d:
            newQuantity = d.get(i) + 1
            dict.update({i: newQuantity})
        else:
            dict.update({i: 0})
    for i in range(0, len(d)):
        num = d.get(i)
        if num == 1:
            return i
    return 1000


if __name__ == '__main__':
    nums = [2, 2, 1]
    singleNumber(nums)
