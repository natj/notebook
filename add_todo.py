import shell_util
import os

from notes import Note
from notes import readNoteFile


def readSimpleNote(fname):
    n = Note()
    f = open(fname, "r")
    tmp = f.read()
    f.close()

    tmp = tmp.splitlines()
    n.setTitle( tmp[0] )

    #collect body
    msg = ""
    for i in range(1,len(tmp)):
        msg += tmp[i] + "\n"

    n.setBody(msg)

    return n



try: notesdir = os.environ["NOTES"]
except: notesdir = "."

tododir = notesdir + "/todos"



#################################3
# open editor and modify tmp file
full_path = "{}/tmp-todo.md".format(tododir)
shell_util.openFile(full_path)


#create note from it
#n = readNoteFile(full_path)
n = readSimpleNote(full_path)



#################################3
#analyze and set defaults

#if date is not set, add today
if n.date == "":
    n.setDateNow()


#save to file
n.save(tododir)


# delete temporary
shell_util.run("rm {}".format(full_path))


