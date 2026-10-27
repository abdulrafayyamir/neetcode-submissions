class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #We need an empty dict to save our iterable elements

        check_dict={}
        
        #We need to iterate over the index and value through enumerate
        for i, num in enumerate(nums):

            #since our exact missing value can be found out by deducting from the target value

            complement=target-num
#check if missing value is already in the empty dict
            if complement in check_dict:
                
                return[check_dict[complement],i]
#save in the dict
            check_dict[num]=i