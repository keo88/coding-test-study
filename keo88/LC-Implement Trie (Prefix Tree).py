class Node:
    def __init__(self, val: str):
        self.val = val
        self.data = None
        self.children = {}

class Trie:

    def __init__(self):
        self.head = Node('')


    def insert(self, word: str) -> None:
        cur = self.head
        for ch in word:
            if not ch in cur.children:
                cur.children[ch] = Node(ch)
            cur = cur.children[ch]
        cur.data = word

    def search(self, word: str) -> bool:
        cur = self.head
        for ch in word:
            if not ch in cur.children:
                return False
            cur = cur.children[ch]
        if cur.data and cur.data == word:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.head
        for ch in prefix:
            if not ch in cur.children:
                return False
            cur = cur.children[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
