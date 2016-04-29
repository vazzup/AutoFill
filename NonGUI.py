import trie, os, sqlite3
print('Loading database...')
myTrie = trie.Trie()
myConnection = sqlite3.connect('myDatabase.db')
myCursor = myConnection.cursor()
print("Database loaded...")
print("Retrieving Data")
myCursor.execute("""create table if not exists myStrings (stringID int primary key not NULL, string text)""")
myCursor.execute("""select * from myStrings""")
maxnum = -1
for row in myCursor:
	myTrie.addWord(row[1])
	maxnum = max(maxnum, row[0])
maxnum += 1
print("Data Retrieved")
print ("Add *word*: Add word to dictionary")
print("Prefix *prefix*: Find most probable suffix for given prefix")
print("Exit : Exit the application")
commandInput = input().strip().lower().split()
word = ""
command = ""
if len(commandInput) is 2:
    word = commandInput[1]
command = commandInput[0].strip().lower()
while command != "exit":
        if command == "add":
                myTrie.addWord(word)
                print("Word added")
                myCursor.execute("""insert into myStrings values(?, ?)""", (maxnum, word))
                maxnum+=1
                myConnection.commit()
        elif command == "prefix":
                suffix = myTrie.predictWord(word)
                if len(suffix) is not 0:
                    print(suffix)
                else :
                    print("No suggestions")
        else:
                print(command, "is an invalid command")
        print("Enter new command")
        commandInput = input().strip().lower().split()
        if len(commandInput) is 2:
                word = commandInput[1]
        command = commandInput[0].strip().lower()
myCursor.close()
print("Goodbye!")
