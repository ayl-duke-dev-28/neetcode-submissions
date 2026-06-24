class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root                    # start at the root every time
        for char in word:                   # walk one character at a time
            if char not in node.children:   # no node for this char yet
                node.children[char] = TrieNode()   # create it
            node = node.children[char]      # step into it
        node.is_end = True                  # mark end of word

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:   # missing character -> word not here
                return False
            node = node.children[char]
        return node.is_end                  # True only if a word actually ends here

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:   # prefix doesn't exist
                return False
            node = node.children[char]
        return True                         # made it through all prefix chars