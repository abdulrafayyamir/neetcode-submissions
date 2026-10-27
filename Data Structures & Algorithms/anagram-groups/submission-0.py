from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            # 1. Create a defaultdict where every new key automatically starts with an empty list []
        res=defaultdict(list)

        for s in strs:


            # 2. Sort the word to create its "fingerprint" key (e.g., "eat" -> "aet")
            sorted_s= "".join(sorted(s))
            # 3. Append the original word directly into the list for that key 
            # (defaultdict automatically creates the list if it doesn't exist yet!)
            res[sorted_s].append(s)
        # 4. Return all the grouped lists of words from our dictionary
        return list(res.values())