
from typing import List
import collections
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

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        https://leetcode.com/problems/group-anagrams/
        """
        result = collections.defaultdict(list)

        for word in strs:
            s = [0] * 26
            for ch in word:
                s[ord(ch) - ord("a")] += 1
            result[tuple(s)].append(word)
        return result.values()
if __name__ == "__main__":
    solution = Solution()
    # print(solution.containsDuplicate([1,2,3,4]))
    # print(solution.isAnagram(s = "anagram", t = "nagaram"))
    # print(solution.twoSum(nums = [2,7,11,15], target = 9))
    # print(solution.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
#