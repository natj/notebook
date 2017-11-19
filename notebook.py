from notes import Note





class NoteBook:

    notes = []
    title = "Notebook"

    previewLen = 80

    #name of the main temporary note file
    tmpNoteFile = "note-tmp.md"


    #add a new note
    def addNote(self, note):
        self.notes.append(note)

    #set notebook title 
    def setTitle(self, title):
        self.title = title

    #print notebook
    def print(self):

        msg = ""
        msg += "# {}\n".format(self.title)
        msg += "-----\n"
        msg += "\n"


        #loop over all notes and collect text
        for note in self.notes:
            msg += "## {}\n".format(note.title) 
            msg += "---:{}\n".format(note.hash())

            prewv = note.body
            if len(prewv) > self.previewLen:
                prewv = prewv[:140]
                prewv += "  . . ."

            msg += " {}\n".format(prewv)
            msg += "\n"

        msg += "\n"

        print(msg)

        f = open(self.tmpNoteFile,'w')
        f.write(msg)
        f.close()



if __name__ == "__main__":
    note1 = Note()
    note1.setTitle("note number 1")
    note1.setBody("Blaablaa, this is comment.")
    
    note2 = Note()
    note2.setTitle("note number 2")
    note2.setBody("blaablaa, this is another comment.")
    
    note3 = Note()
    note3.setTitle("Lenghty note")
    note3.setBody(
    "This is a note with a very long text body.\n"
    + "it continues all the way to here. and to \n"
    + "here: Seems long, right?. Now it finally almost.\n"
    + "here: Seems long, right?. xxx xxx xxx xxx xxx x.\n"
    + "here: Seems long, right?. Now it finally ends."
                 )
    
    note4 = Note()
    note4.setTitle("Different note")
    note4.setBody("only small text")

    note1.name = "note"
    note1.setDateNow()
    note1.save("todo")

    ##################################################
    #nb = NoteBook()
    #for note in [note1, note2, note3, note4]:
    #    print(note.createName() )

    #    nb.addNote(note)
    #
    #nb.print()








