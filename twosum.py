class solution:
    
    def twosum(self,nums: list[int], target: int):
        h = {}
        for i, num in enumerate(nums):
            h[num] = i
    
        for i, num in enumerate(nums):
            desired = target - num
            if desired in h and h[desired] != i:
                return i, h[desired]


            

            


    