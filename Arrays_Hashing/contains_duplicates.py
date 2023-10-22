
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        https://leetcode.com/problems/contains-duplicate/
        """
        check = dict()
        for num in nums:
            if num in check:
                return True
            check[num] = 1

        return False

    def isAnagram(self, s: str, t: str) -> bool:
        """
        https://leetcode.com/problems/valid-anagram/
        """
        if len(s) != len(t):
            return False
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        for letters in alphabets:
            if s.count(letters) != t.count(letters):
                return False
        return True

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """

        https://leetcode.com/problems/two-sum/
        """
        hash_map = dict()
        for index, num in enumerate(nums):
            difference = target - num
            if difference in hash_map:
                return [index, hash_map[difference]]
            hash_map[num] = index
        return []

if __name__ == "__main__":
    solution = Solution()
    # print(solution.containsDuplicate([1,2,3,4]))
    # print(solution.isAnagram(s = "anagram", t = "nagaram"))
    # print(solution.twoSum(nums = [2,7,11,15], target = 9))
