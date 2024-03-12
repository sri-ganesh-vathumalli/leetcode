class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        self.left = [1]
        self.right = [1]
        for i in range(1, len(nums)):
            self.left.append(self.left[i - 1] * nums[i - 1])
        print(self.left)
        for i in range(1, len(nums)):
            self.right.append(self.right[i - 1] * nums[len(nums) - i])
        self.right = list(reversed(self.right))
        print(self.right)
        product_arr = [self.right[i] * self.left[i] for i in range(len(nums))]
        return product_arr
