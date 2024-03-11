class TrieNode:
    def __init__(self, key:str):
        self.key = key
        self.isWord = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode('')

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if not ch in cur.children:
                cur.children[ch] = TrieNode(ch)
            cur = cur.children[ch]
        cur.isWord = True
    
    def searchFromNode(self, node: TrieNode, word: str) -> bool:
        cur = node
        for i, ch in enumerate(word):
            if ch == '.':
                res = False
                nxtWrd = word[i + 1:]
                return any(self.searchFromNode(v, nxtWrd) for v in cur.children.values())
            if not ch in cur.children:
                return False
            cur = cur.children[ch]
        return cur.isWord

    def search(self, word: str) -> bool:
        return self.searchFromNode(self.root, word)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
