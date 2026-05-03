class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        ''' number should be win k times
        if somehow, the maximum no reaches front.. it will be the winner
        k does allow this or not.
        streak counting - player -> i 
        j -> arr[j] < arr[i] = win += 1
        arr[j] > arr[i] = win = 1 
        i -> ever becomes the max value
        or win count == k. i-> winner
        '''
        current_player = arr[0] 
        win_count = 0
        powerful_player = max(arr)
        for j in range(1, len(arr)):
            if current_player > arr[j]:
                win_count += 1
            elif current_player < arr[j]:
                current_player = arr[j]
                win_count = 1
            if win_count == k or current_player == powerful_player:
                return current_player
        return powerful_player