from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dict:
                answer = [dict[complement], i]
                return answer
            else:
                dict[nums[i]] = i
        return
    
def main():
    nums = [3, 2, 4]
    target = 6
    solution = Solution()
    answer = solution.twoSum(nums, target)
    print(answer)

if __name__ == "__main__":
    main()