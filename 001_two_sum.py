'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.


Example
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Output: Because nums[0] + nums[1] == 9, we return [0, 1].

'''

class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            num1 = nums[i]
            num2 = target - nums[i]
            if num2 in nums[i+1:]:
                return [i, nums.index(num2, i+1)]


if __name__ == "__main__":

    print(Solution().twoSum(nums=[2,7,11,15], target=9))
