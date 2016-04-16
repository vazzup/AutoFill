import trie

file = open('search_history.txt', 'w+')
print("File Loaded")
myTrie = trie.Trie()
for line in file:
    myTrie.addWord(line.strip())
print("Data Retrieved")
print ("Add : Add word to dictionary")
print("Prefix : Find most probable suffix for given prefix")
print("Exit : Exit the application")
command = input().strip().lower()
while command != "exit":
    if command == "add":
        print("Enter word to be added")
        word = input().strip()
        myTrie.addWord(word)
        print("Word added")
    elif command == "prefix":
        print("Enter prefix to be completed")
        prefix = input().strip()
        print(myTrie.predictWord(prefix))
    else:
        print("Incorrect command")
    print("Enter new command")
    command = input().strip()
