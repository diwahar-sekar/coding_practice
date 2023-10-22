
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

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        https://leetcode.com/problems/top-k-frequent-elements/
        """

        count = dict()
        freq = [[] for i in range(len(nums) + 1)]
        result = list()

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for key, item in count.items():
            freq[item].append(key)

        for index in range(len(freq) - 1, 1, -1):
            for num in freq[index]:
                result.append(num)
                if len(result) == k:
                    return result

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        https://leetcode.com/problems/product-of-array-except-self/
        """
        prefix, postfix = 1, 1
        list1 = [1] * (len(nums))
        for i in range(len(nums)):
            list1[i]=prefix
            prefix*=nums[i]

        for j in range(len(nums)-1,-1,-1):
            list1[j]*=postfix
            postfix*=nums[j]

        return list1

if __name__ == "__main__":
    solution = Solution()
    # print(solution.containsDuplicate([1,2,3,4]))
    # print(solution.isAnagram(s = "anagram", t = "nagaram"))
    # print(solution.twoSum(nums = [2,7,11,15], target = 9))
    # print(solution.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
    # print((solution.topKFrequent(nums = [1,1,1,2,2,3], k = 2)))
    # print(solution.productExceptSelf([1,2,3,4]))