class Node:
    
    """This class represents Nodes of Tries. The constructor expects a character
    as a parameter for the Node"""
    
    def __init__(self, character):
        self.character = character    #character of node
        self.children = {}
        for i in "abcdefghijklmnopqrstuvwxyz":
            self.children[i] = None    #children nodes
        self.frequent_child = None    #childnode with max frequency
        self.max_frequency_child = 0    #maximum frequency of children
        self.frequency = 1    #no. of times this character has been called
        self.max_suffix = ""    #suffix with characters that are most called
        self.parent_node = None    #node of origination
        
    def addChild(self, character):
        if self.children[character] is None:    #Node doesn't exist
            self.children[character] = Node(character)    
            self.children[character].parent_node = self
        else:
            self.children[character].frequency+=1    #Node exists; Update freq
        return self.children[character]
    
class Trie:
    """Class for Trie structure itself."""
    def __init__(self):
        self.root_node = Node(None)

    def addWord(self, word):
        """To add a word to the Trie"""
        word = word.strip()
        if len(word) is 0:
            return
        current_node = self.root_node
        for character in word:
            current_node = current_node.addChild(character)    #Add/Update all child nodes
        while current_node is not self.root_node:
            if current_node.parent_node.max_frequency_child < current_node.frequency:    #Update maximums for all nodes
                current_node.parent_node.max_frequency_child = current_node.frequency
                current_node.parent_node.frequent_child = current_node
                current_node.parent_node.max_suffix = current_node.character + current_node.max_suffix
            current_node = current_node.parent_node
            
        
    def predictWord(self, prefix):
        """To predict the word depending on given prefix"""
        prefix = prefix.strip()
        if len(prefix) is 0:
            return ""
        current_character = self.root_node
        for character in prefix:
            if current_character.children[character] is None:
                break
            else:
                current_character = current_character.children[character]
        if current_character is None:
            return ""
        else:
            return current_character.max_suffix
        
