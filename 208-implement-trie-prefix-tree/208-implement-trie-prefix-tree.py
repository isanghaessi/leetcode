from pprint import *

class Trie:
    def __init__(self):
        self.nextDict = {}
        self.end = False
    
    def insert(self, word: str) -> None:
        current = self
        i = 0
        while i < len(word):
            if word[i] in current.nextDict:
                current = current.nextDict[word[i]]
            else:
                newTrie = Trie()
                current.nextDict[word[i]] = newTrie
                current = newTrie
            if i == len(word) - 1:
                current.end = True
            i += 1
        

    def search(self, word: str) -> bool:
        current = self
        i = 0
        while i < len(word):
            if word[i] in current.nextDict:
                current = current.nextDict[word[i]]
            else:
                
                return False
            i += 1
        
        return current.end
        

    def startsWith(self, prefix: str) -> bool:
        current = self
        i = 0
        while i < len(prefix):
            if prefix[i] in current.nextDict:
                current = current.nextDict[prefix[i]]
            else:
                
                return False
            i += 1
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)