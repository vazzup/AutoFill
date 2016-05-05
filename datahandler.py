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
        suffix=self.myTrie.predictWord(text)
        liststore = Gtk.ListStore(str)
        if suffix is not "":
            liststore.append([text + suffix])
        return liststore

    def addUnknownWord(self, text):
        """Adds unknown text to trie and sqlite"""
        self.myTrie.addWord(text)
        self.myCursor.execute("""insert into myStrings values(?, ?)""", (self.maxnum, text))
        self.maxnum+=1
        self.myConnection.commit()

    def close(self):
        """Called when operations are done"""
        myCursor.close()
