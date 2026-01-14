class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total = 0
        r = 10 ** 9
        res = None
        for _, _, l in squares:
            total += l * l
        l = 0
        def solve(mid):
            running_area = 0
            for square in squares:
                x, y, l = square
                area = l ** 2
                if y + l <= mid:
                    running_area += area
                else:
                    running_area += max(0,(mid - y)) * l
            remaining_area = total - running_area

            if remaining_area <= running_area:
                return True
            else:
                return False
                
        while r - l > 10e-7:
            mid = (l + r) / 2
            if solve(mid):
                res = mid
                r = mid 
            else:
                l = mid
        return res