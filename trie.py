class Node:
    def __init__(self, character):
        self.character = character
        for i in "abcdefghijklmnopqrstuv":
            self.children[i] = None
        self.frequent_child = None
        self.max_frequency_child = 0
        self.frequency = 1
        self.max_suffix = ""
        self.parent_node = None
        
    def addChild(self, character):
        if self.children[character] is None:
            self.children[character] = Node(character)
            self.children[character].parent_node = self
        else self.children[character].frequency+=1
        return self.children[character]
    
class Trie:
    def __init__(self):
        self.root_node = Node(None)

    def addWord(self, word):
        if len(word) is 0:
            return
        current_node = self.root_node
        for character in word:
            current_node = current_node.addChild(character)
        
    def predictWord(self, prefix):
        if len(prefix) is 0:
            return ""
        current_character = self.root_node
        
        
