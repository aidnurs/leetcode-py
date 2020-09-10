class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m=max(candies)
        arr=[]
        for can in candies:
            arr.append((can+extraCandies)>=m)
        return arr;
        