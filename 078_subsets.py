'''
Given a set of 'distinct' integers, nums, return all possible subsets (the power set).
The solution set must 'not' contain duplicate subsets.

Example
    Input: nums = [1,2,3]
    Output: [0,1]
    Output:
                [
                  [3],
                  [1],
                  [2],
                  [1,2,3],
                  [1,3],
                  [2,3],
                  [1,2],
                  []
                ]
Idea:
    - [1,2,3]: {[1]}, {[2]}, {[3]}  --> {[1,2], [1,3]}, {[2,3]} --> {[1,2,3]} #check if avaliable, then append one element in each round
    - maybe can employ recursive!

'''

class Solution(object):
    def addElement(self, sub_nums, nums):
        '''
        :type sub_nums: List[int]
        :type nums: List[int]
        :rtype: List[int] or empty list (if cannot add)
        '''
        listOfsubsets = []
        end_index = nums.index(sub_nums[-1])
        if end_index < len(nums) - 1:
            for el in nums[end_index+1:]:
                listOfsubsets += [sub_nums + [el]]


        return listOfsubsets

    def nextRound(self, current_round_list, nums):
        '''
        :type current_round_list: List[[int]]
        :type nums: List[int]
        :rtype: List[int] or empty list (if cannot add)
        '''
        next_round_list = []
        for sub_lst in current_round_list:
            next_round_list += self.addElement(sub_lst, nums=nums)

        return next_round_list

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #最後在加[]
        listOfsubsets = []

        for el in nums:
            listOfsubsets += [[el]]

        current_round_list = listOfsubsets
        next_round_list = self.nextRound(current_round_list=current_round_list, nums=nums)


        while next_round_list != []:
            listOfsubsets += next_round_list
            current_round_list = next_round_list
            next_round_list = self.nextRound(current_round_list=current_round_list, nums=nums)


        return listOfsubsets + [[]]



if __name__ == "__main__":

    print(Solution().subsets(nums=[]))
