import gi, datahandler
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    """Gtk Window class"""
    def __init__(self, name):
        """Constructor"""
        Gtk.Window.__init__(self, title = name)

        """Data Handler definition"""
        self.dataHandler = datahandler.DataHandler()

        """VBox Container Definition"""
        self.vBox = Gtk.VBox(spacing = 10)
        self.add(self.vBox)
        
        """Entry Definition"""
        self.entry = Gtk.Entry()
        self.entryCompletion = Gtk.EntryCompletion()    #EntryCompletion List
        self.liststore = Gtk.ListStore(str)    #Default null ListStore
        self.entryCompletion.set_model(self.liststore)
        self.entry.set_completion(self.entryCompletion)
        self.entry.connect("changed", self.onEntryChangedEvent)    #Upon change in Entry text
        self.entryCompletion.set_text_column(0)    #Sets value of entrycompletion to liststore[0]
        self.vBox.pack_start(self.entry, True, True, 0)
        
        """Button Definition"""
        self.button = Gtk.Button(label = "Search")
        self.button.connect("clicked", self.onButtonClickEvent)    #Upon Button CLick
        self.vBox.pack_start(self.button, True, True, 0)

    def onEntryChangedEvent(self, entry):
        """Called when entry is changed. Gets prediction ListStore from data
           handler and updates entryCompletion"""
        text = entry.get_text().lower()
        #print("Keypress detected")
        self.entryCompletion.set_model(self.dataHandler.getPrediction(text))
            
    def onButtonClickEvent(self, button):
        """Called when button is clicked. Adds entry key to trie, and database"""
        self.dataHandler.addUnknownWord(self.entry.get_text().lower().strip())
        self.entry.set_text("")
        print("Text added")

window = MyWindow("AutoFill")
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
