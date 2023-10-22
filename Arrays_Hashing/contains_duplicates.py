"""
https://leetcode.com/problems/contains-duplicate/
"""
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check = dict()
        for num in nums:
            if num in check:
                return True
            check[num] = 1

        return False
solution = Solution()

if __name__ == "__main__":
    pass
    # print(solution.containsDuplicate([1,2,3,4]))
