import gi, datahandler
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self, name):
        Gtk.Window.__init__(self, title = name)

        #Data Handler
        self.dataHandler = datahandler.DataHandler()

        #VBox Definition
        self.vBox = Gtk.VBox(spacing = 10)
        self.add(self.vBox)
        
        #Entry Definition
        self.entry = Gtk.Entry()
        self.entryCompletion = Gtk.EntryCompletion()
        self.liststore = Gtk.ListStore(str)
        self.entryCompletion.set_model(self.liststore)
        self.entry.set_completion(self.entryCompletion)
        self.entry.connect("changed", self.onEntryChangedEvent)
        self.entryCompletion.set_text_column(0)
        self.vBox.pack_start(self.entry, True, True, 0)
        
        #Button Definition
        self.button = Gtk.Button(label = "Search")
        self.button.connect("clicked", self.onButtonClickEvent)
        self.vBox.pack_start(self.button, True, True, 0)

    def onEntryChangedEvent(self, entry):
        text = entry.get_text().lower()
        print("Keypress detected")
        self.entryCompletion.set_model(self.dataHandler.getPrediction(text))

    def onButtonClickEvent(self, button):
        self.dataHandler.addUnknownWord(self.entry.get_text().lower())
        print("Text added")
            
window = MyWindow("AutoFill")
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
