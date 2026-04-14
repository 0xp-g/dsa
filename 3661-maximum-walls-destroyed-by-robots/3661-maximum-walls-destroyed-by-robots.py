class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        robots_with_dist = sorted(zip(robots, distance))
        robots_sorted = [r for r, _ in robots_with_dist]
        dist_sorted = [d for _, d in robots_with_dist]
        walls_sorted = sorted(walls)
        
        n = len(robots_sorted)
    
        def count_walls_in_range(L: int, R: int) -> int:
            if L > R:
                return 0
            left_idx = bisect.bisect_left(walls_sorted, L)
            right_idx = bisect.bisect_right(walls_sorted, R)
            return right_idx - left_idx
    
        @lru_cache(None)
        def dp(idx: int, prev_dir: int) -> int:
            if idx == n:
                return 0
            
            curr_pos = robots_sorted[idx]
            curr_dist = dist_sorted[idx]
            
            #SHOOT LEFT
            left_boundary = curr_pos - curr_dist
            if idx > 0:
                prev_pos = robots_sorted[idx - 1]
                # If the previous robot shot RIGHT, its bullet came towards us!
                if prev_dir == 1:
                    # Calculate how far its bullet reached
                    prev_reach = min(curr_pos - 1, prev_pos + dist_sorted[idx - 1])
                    # We can only count walls starting AFTER its bullet stopped
                    left_boundary = max(left_boundary, prev_reach + 1)
                else:
                    # Prev robot shot left, so it didn't cross into our space.
                    # We just can't shoot past its body.
                    left_boundary = max(left_boundary, prev_pos + 1)
            
            left_walls = count_walls_in_range(left_boundary, curr_pos)
            # Pass 0 to tell the next robot we shot Left
            opt_left = left_walls + dp(idx + 1, 0)
            
            
            #SHOOT RIGHT
            right_boundary = curr_pos + curr_dist
            if idx + 1 < n:
                # We can't shoot past the next robot's body
                next_pos = robots_sorted[idx + 1]
                right_boundary = min(right_boundary, next_pos - 1)
            
            right_walls = count_walls_in_range(curr_pos, right_boundary)
            # Pass 1 to tell the next robot we shot Right
            opt_right = right_walls + dp(idx + 1, 1)
            
            return max(opt_left, opt_right)
    
        # Pass -1 initially since there is no previous robot
        result = dp(0, -1)
        dp.cache_clear()
        return result