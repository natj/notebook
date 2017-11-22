from os import listdir
from os.path import isfile, join
import regexes

from notes import Note
from notes import readNoteFile
from notebook import NoteBook
import shell_util



#create todo notebook
def createTODO(directory):

    #get files
    allFiles  = [f for f in listdir(directory) if isfile(join(directory, f))]
    todoFiles = [f for f in allFiles if f[0] != "."]
    print(todoFiles)

    #create notebook
    nb = NoteBook()
    nb.setTitle("TODO")

    for todof in todoFiles:
        n = readNoteFile(directory + "/" + todof)
        nb.addNote(n)

    return nb


#read temporary notebook file
def readTodoFile(fname):

    nbtmp = NoteBook()
    nbtmp.setTitle("Updated TODO")
    nbtmp.tmpNoteFile = "notebook-tmp-C.md"


    f = open(fname, "r")
    tmp = f.read()
    f.close()

    #print("tmp file content--------------")
    tmp = tmp.splitlines()
    #print(tmp)

    #add trailing newlines for easier parsing
    #for i in range(len(tmp)):
    #    tmp[i] += "\n"

    #filter header out
    c = 0
    while True:
        line = tmp[c]
        #print("skipping {}".format(line))

        mtitle = regexes.REtitle.match(line)
        if mtitle:
            break
        c += 1
    #print("skipping {}".format(c))


    ns     = []
    hashes = []
    bodys  = []

    body   = ""
    while (c < len(tmp)):
        line = tmp[c]
        #print("{}".format( line ))

        mtitle = regexes.REtitle.match(line)
        mhash  = regexes.REhash.match(line)
        mdate  = regexes.REdate.match(line)
        mmdate = regexes.REmdate.match(line)

        if mtitle:
            n = Note()
            bodys.append(body)
            body = ""

            s = mtitle.group(1)
            n.setTitle(s)
            ns.append(n)
            #ni += 1
        elif mhash:
            s = mhash.group(1)
            hashes.append(s)
        elif mdate:
            n.setDate(mdate.group(1))
        elif mmdate:
            n.setDate(mmdate.group(1))
        else:
            body += line + "\n"
        c += 1
    bodys.append(body) #append last hanging body

    #strip from trailing newline


    #print("###########################################")
    for i, n in enumerate(ns):

        body = bodys[i+1]
        #print("last char: vvv{}vvv".format(body[-2:]))

        #if (body[-2:] == "\n"): 
        #    print("newline detected")
        #    body = body[:-2]

        #body = body[:-2] #strip trailing newline
        #body = body.rstrip()
        #body += "\n"
        #body += "\n"

        n.setBody(body)
        #print("{} -- {}".format(i, n.title))
        #print("{} hash is {}".format(i, n.hash() ))
        #print("----")
        #print("{}".format(n.body)) 
        #print("----")
        #print("{}".format(body))

        nbtmp.addNote(n)

    return nbtmp


# compare two notebooks and deduce if they differ.
def compareNoteBooks(nb1, nb2):
    modified = []
    added    = []
    removed  = []


    # if note in nb2 is not found in nb1 with same name
    # then it is new
    for note in nb2.notes:
        h = note.hash()

        for ref_note in nb1.notes:
            ref_h = ref_note.hash()
            if (note.title == ref_note.title):
                break
        else:
            print("note {} is added".format(note.title))
            added.append(note)



    # if note in nb2 is not found in nb1 with same hash
    # but is found with a same name then it is modified
    for note in nb2.notes:
        h = note.hash()

        for ref_note in nb1.notes:
            ref_h = ref_note.hash()

            if (h == ref_h): #and (note.title == ref_note.title):
                break
        else:
            for ref_note in nb1.notes:
                ref_h = ref_note.hash()
                if (note.title == ref_note.title):
                    print("note {} is modified".format(note.title))
                    modified.append(note)
                    break


    #if note is not found nb1 with same name
    #union = []
    #for n in nb1.notes:
    #    union.append(n)
    #for n in modified:
    #    union.append(n)



    # if note in nb1 is not found in nb2
    # then it has been removed
    for note in nb1.notes:
        h = note.hash()

        for ref_note in nb2.notes:
            ref_h = ref_note.hash()

            if (note.title == ref_note.title):
                break
        else:
            print("note {} is removed".format(note.title))
            removed.append(note)

    return added, modified, removed



#--------------------------------------------------
#read directory
directory = "todos"
done_directory = "todos/done"


#create notebook from notes in todo directory
nb = createTODO(directory)
nb.print()
print("number of notes: {}".format(  len( nb.notes )))

#open for read
fname = nb.tmpNoteFile
shell_util.openFile(fname) #XXX


#create notebook from temporary file
nbtmp = readTodoFile(fname)
#nbtmp.print() #XXX debug print

print("number of notes: {}".format(  len( nbtmp.notes )))

#compare notebooks
added, modified, removed = compareNoteBooks(nb, nbtmp)

# and now add accordinly

for note in added:
    note.save(directory)

for note in modified:
    note.save(directory)

for note in removed:
    note.save(done_directory)
    #note.setName(note.createName())
    print("note name before removal: {}".format(note.name))

    prog = "rm {}/{}".format(directory, note.name)
    print(prog)
    shell_util.run(prog)



#remove tmp file
#XXX
#shell_util.run("rm {}".format(fname))
