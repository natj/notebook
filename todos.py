from os import listdir
from os.path import isfile, join
import regexes

from notes import Note
from notes import readNoteFile
from notebook import NoteBook
import shell_util



#create todo notebook
def createTODO(directory):
    nb = NoteBook()
    nb.setTitle("TODO")

    for todof in todoFiles:
        n = readNoteFile(directory + "/" + todof)
        nb.addNote(n)

    return nb


#read temporary notebook file
def readTodoFile(fname):
    nb = NoteBook()
    nb.setTitle("Updated TODO")

    f = open(fname, "r")
    tmp = f.read()
    f.close()

    print("tmp file content--------------")
    tmp = tmp.splitlines()
    print(tmp)

    #filter header out
    c = 0
    while True:
        line = tmp[c]
        #print("skipping {}".format(line))

        mtitle = regexes.REtitle.match(line)
        if mtitle:
            break
        c += 1
    print("skipping {}".format(c))



    return nb


#--------------------------------------------------
#read directory
directory = "todos"
allFiles  = [f for f in listdir(directory) if isfile(join(directory, f))]
todoFiles = [f for f in allFiles if f[0] != "."]
print(todoFiles)

#create notebook from notes in todo directory
nb = createTODO(directory)
nb.print()

#open for read
fname = nb.tmpNoteFile
shell_util.createTempFile(fname)


#create notebook from temporary file
nbtmp = readTodoFile(fname)


#remove tmp file
shell_util.run("rm {}".format(fname))
