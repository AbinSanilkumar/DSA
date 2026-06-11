# class Solution:
#     def SecondLargest(self,nums):
#         Blarge=float("-inf")
#         Slarge=float("-inf")

#         for num in nums:
#             if num > Blarge:
#                 Slarge=Blarge
#                 Blarge=num
            
#             elif num > Slarge and num != Blarge:
#                 Slarge=num
#         return Slarge
            



class Solution:
    def Secondsmallest(self,nums):
        smallest=float("inf")
        ssmallest=float("inf")

        for num in nums:
            if num < smallest:
                ssmallest=smallest
                smallest=num

            elif num < ssmallest and num != smallest:
                ssmallest=num
        return ssmallest















