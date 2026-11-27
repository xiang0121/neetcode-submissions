class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = defaultdict(int)
        for n in nums:
            hmap[n] += 1
        ans = []
        sorted_items = sorted(hmap.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            ans.append(sorted_items[i][0])
        return ans
