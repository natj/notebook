from notes import Note
from notes import Inbox, TaskList


class NoteBook:

    notes = []
    title = "Notebook"

    previewLen = 80

    # name of the main temporary note file
    tmpNoteFile = "notebook-tmp.md"

    # --------------------------------------------------
    # special notes always present

    # name of the inbox
    inbox = Inbox
    tasklist = TaskList

    def __init__(self):
        self.notes = []

        # add inbox
        # inbox = Note()
        # inbox.setTitle(self.inbox_name)
        # self.inbox = inbox

        ##add tasklist
        # tasklist = Note()
        # tasklist.setTitle(self.tasklist_name)
        # self.tasklist = tasklist

    # add a new note
    def addNote(self, note):

        if note.title == self.inbox.title:
            self.inbox = Inbox(note)
        elif note.title == self.tasklist.title:
            self.tasklist = TaskList(note)
        else:
            self.notes.append(note)

    # set notebook title
    def setTitle(self, title):
        self.title = title

    # print notebook
    def print(self):

        msg = ""
        msg += "# {}\n".format(self.title)
        msg += "\n"

        msg = self.inbox.print(msg)
        msg = self.tasklist.print(msg)

        # loop over all notes and collect text
        for note in self.notes:
            msg = note.print(msg)

        msg = msg.rstrip()  # remove all trailing newlines

        f = open(self.tmpNoteFile, "w")
        f.write(msg)
        f.close()


# --------------------------------------------------
# Testing
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
    # nb = NoteBook()
    # for note in [note1, note2, note3, note4]:
    #    print(note.createName() )

    #    nb.addNote(note)
    #
    # nb.print()
