class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isend = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
    

    def addWord(self, word: str) -> None:
        curr = self.root
        n = len(word)
        for i in range(n):
            ch = word[i]
            idx = ord(ch) - ord('a')
            if idx not in curr.children:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.isend = True


    def search(self, word: str) -> bool:
        #should be recursive
        n = len(word)
        curr = self.root
        
        def search(curr, i):
            
            if i == n:
                return curr.isend
            
            elif word[i] == '.':
                ch = word[i]
                for child in curr.children:
                    if search(curr.children[child], i+1):
                        return True
                return False
            
            else:
                ch = word[i]
                idx = ord(ch) - ord('a')
                return search(curr.children[idx], i + 1) if idx in curr.children else False
        
        return search(curr, 0)
            

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)