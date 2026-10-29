from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each number
        count = Counter(nums)
        
        # Step 2: Create empty buckets where index = frequency
        # Size is len(nums) + 1 to safely include the maximum possible frequency
        freq = [[] for _ in range(len(nums) + 1)]
        
        for num, cnt in count.items():
            freq[cnt].append(num)
            
        # Step 3: Collect top k elements by walking backwards from highest frequency
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num) 
                if len(res) == k:
                    return res