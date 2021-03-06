import trie, sqlite3, gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
class DataHandler:
    """Class to handle data from sqlite database"""
    def __init__(self):
        """Constructor;
           myTrie - Trie to predict words
           myConnection, myCursor - to handle sqlite
           maxnum - index of string"""
        self.myTrie = trie.Trie()
        '''Connecting to sqlite and creating table'''
        self.myConnection = sqlite3.connect('myDatabase.db')
        self.myCursor = self.myConnection.cursor()
        self.myCursor.execute("""create table if not exists myStrings (stringID int primary key not NULL, string text)""")
        self.myCursor.execute("""select * from myStrings""")
        self.maxnum = -1
        '''Building trie'''
        for row in self.myCursor:
            self.myTrie.addWord(row[1])
            self.maxnum = row[0]
        '''Trie built'''
        self.maxnum += 1

    def getPrediction(self, text):
        """Returns ListStore containing prediction"""
        liststore = Gtk.ListStore(str)
        if text == "":
            return liststore
        temp2 = text
        text = text.strip().split()
        temp = ""
        for i in text[:-1]:
            temp+=i
            temp+=" "
        text = text[-1]
        suffix=self.myTrie.predictWord(text)
        if suffix != "":
            if temp != " ":
                liststore.append([temp + text + suffix])
            else:
                liststore.append([text+suffix])
        else:
            predict = ""
            tofind = text
            while predict == "" and len(tofind) is not 0:
                tofind = tofind[:-1]
                predict=self.myTrie.predictWord(tofind)
                
            if temp != " ":
                liststore.append([temp + text + " Did You Mean " + tofind + predict])
            else:
                liststore.append([text + " Did You Mean " + tofind + predict])
        return liststore

    def addUnknownWord(self, text):
        """Adds unknown text to trie and sqlite"""
        text = text.split()
        for word in text:
            self.myTrie.addWord(word)
            self.myCursor.execute("""insert into myStrings values(?, ?)""", (self.maxnum, word))
            self.maxnum+=1
            self.myConnection.commit()

    def close(self):
        """Called when operations are done"""
        myCursor.close()
