class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            if i in dic.keys():
                dic[i] += 1
            else:
                dic[i] = 1
        topk = sorted(dic, key=dic.get, reverse=True)[:k]
        print(topk)
        return topk
