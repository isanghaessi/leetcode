import collections

class TrieNode:
    def __init__(self, word = False):
        self.word = word
        self.children = collections.defaultdict()

        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        current = self.root
        for i, w in enumerate(word):
            if w not in current.children.keys():
                current.children[w] = TrieNode()
            if i == len(word) - 1:
                current.children[w].word = True
            current = current.children[w]
            

    def search(self, word: str) -> bool:
        current = self.root
        for w in word:
            if w not in current.children.keys():
                
                return False
            current = current.children[w]
        
        return current.word
        

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for p in prefix:
            if p not in current.children.keys():
                
                return False
            current = current.children[p]
        
        return True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)