import hashlib
import datetime 
import regexes



class Note:

    name  = ""
    title = ""
    body  = ""

    date  = ""


    #def __init__(self):

    def setName(self, name):
        self.name = name

    def setTitle(self, title):
        self.title = title

    def setBody(self, body):
        body = body.rstrip()
        body += "\n"

        self.body = body

    def setDate(self, date):
        self.date = date

    def setDateNow(self):
        self.date = datetime.datetime.now().strftime("%d-%m-%y")

    def createName(self):

        tmp = ""

        #if empty name, then create form title
        if self.name == "":
            tmp = self.title.replace(' ', '-').lower()
        #else lets use the name slot
        else:
            tmp = self.name

        #append date if there is one set
        if not( self.date == "" ):
            tmp += "_" + self.date

        #suffix
        tmp += ".md"
        return tmp

    def hash(self):
        m = hashlib.md5()

        m.update(self.title.encode('utf-8'))
        m.update(self.body.encode('utf-8'))

        return m.hexdigest()

    #create and save to file
    def save(self, directory):
        fname = directory + "/" + self.createName()
        msg = ""

        #title header
        #msg += "# {}\n".format(self.name)
        #msg += "\n"
        msg += "## {}\n".format(self.title)
        if not(self.date == ""):
            msg += "  created: {}\n".format(self.date)
            msg += " modified: {}\n".format(self.date)
        msg += "--------------------------------------------------\n"

        # body
        msg += "\n"
        msg += "{}\n".format( self.body )


        #write to file
        #print(msg)
        f = open(fname,'w')
        f.write(msg)
        f.close()



# read note from file and create an object
def readNoteFile(fname):
    n = Note()
    f = open(fname, "r")

    #read until message
    for line in f:
        if regexes.REmsgb.match(line):
            break

        mname = regexes.REname.match(line)
        if mname:
            n.setName( mname.group(1) )

        mtitle = regexes.REtitle.match(line)
        if mtitle:
            n.setTitle( mtitle.group(1) )

        mdate = regexes.REdate.match(line)
        if mdate:
            n.setDate( mdate.group(1) )


    #read body
    body = "" 
    for line in f:
        body += line

    #TODO catch error if there is no --- separator
    n.setBody(body)  

    f.close()

    return n


