#Brute-Force Approach
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    return [i,j]

#Optimal Aproach using Dictonary
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp={}
        for i in range(len(nums)):
            if target-nums[i] in mapp:
                return [i,mapp[target-nums[i]]]
            mapp[nums[i]]=i
