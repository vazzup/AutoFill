import trie, os
print('Loading file...')
myTrie = trie.Trie()
if os.path.exists('search_history.txt'):
    with open('search_history.txt', 'r+') as file:
        print("File Loaded")
        print("Retrieving Data...")
        for line in file:
            myTrie.addWord(line.strip())
print("Data Retrieved")
print ("Add *word*: Add word to dictionary")
print("Prefix *prefix*: Find most probable suffix for given prefix")
print("Exit : Exit the application")
command = input().strip().lower().split()
word = ""
file = open('search_history.txt', 'ab+')
if len(command) is 2:
    word = command[1]
command = command[0]
while command != "exit":
    if command == "add":
        myTrie.addWord(word)
        print("Word added")
        file.write(bytes(word+"\n", 'utf-8'))
    elif command == "prefix":
        suffix = myTrie.predictWord(word)
        if len(suffix) is not 0:
            print(suffix)
        else :
            print("No suggestions")
    else:
        print(command, "is an invalid command")
    print("Enter new command")
    command = input().strip().lower().split()
    if len(command) is 2:
        word = command[1]
    command = command[0]
file.close()
print("Goodbye!")
