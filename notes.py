import hashlib
import datetime
import regexes


class Note:

    name = ""
    title = ""
    body = ""
    date = ""

    # def __init__(self):

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

    # return date; if not set use today
    def getDate(self):
        if self.date == "":
            self.setDateNow()
        return self.date

    def createName(self):

        tmp = ""

        # if empty name, then create form title
        if self.name == "":

            # TODO detect all illegal characters
            tmp = self.title.replace(" ", "-").lower()
            tmp = tmp.replace("/", "").lower()


        # else lets use the name slot
        else:
            tmp = self.name

        # append date if there is one set
        if not (self.date == ""):
            tmp += "_" + self.date

        # suffix
        tmp += ".md"

        # add this to as my name
        self.setName(tmp)

        return tmp

    def hash(self):
        m = hashlib.md5()

        m.update(self.title.encode("utf-8"))
        m.update(self.body.encode("utf-8"))

        return m.hexdigest()

    # create and save to file
    def save(self, directory):
        fname = directory + "/" + self.createName()
        msg = ""

        # title header
        # msg += "# {}\n".format(self.name)
        # msg += "\n"
        msg += "## {}\n".format(self.title)
        if not (self.date == ""):
            msg += "  created: {}\n".format(self.date)
            msg += " modified: {}\n".format(self.date)
        msg += "--------------------------------------------------\n"

        # body
        # msg += "\n"
        msg += "{}\n".format(self.body)

        # write to file
        # print(msg)
        f = open(fname, "w")
        f.write(msg)
        f.close()

    # print all content
    def print(self, msg):
        msg += "--------------------------------------------------------------\n"
        msg += "## {}\n".format(self.title)
        # msg += "  created: {}\n".format(self.date)
        # msg += " modified: {}\n".format(self.date)
        msg += "---:{}\n".format(self.hash())

        prewv = self.body.rstrip()
        # if len(prewv) > self.previewLen:
        #    prewv = prewv[:140]
        #    prewv += "  . . ."

        msg += "{}\n".format(prewv)
        msg += "\n"

        return msg


class Inbox(Note):
    title = "inbox"
    name = "inbox"

    def __init__(self, note):
        self.body = note.body
        self.date = note.date

    # print all content
    def print(self, msg):
        msg += "--------------------------------------------------------------\n"
        msg += "## {}\n".format(self.title)
        prewv = self.body.rstrip()
        msg += "{}\n".format(prewv)

        msg += "\n"

        return msg


class TaskList(Note):
    title = "tasklist"
    name = "tasklist"

    def __init__(self, note):
        self.body = note.body
        self.date = note.date


    def getTasks(self, msg):
        tasks = []
        for line in msg.splitlines():
            if line == "":
                continue
            mtask = regexes.REtasks.match(line)

            #print("line:", line)
            if mtask:
                t = mtask.group(1)
                #print("    found task that has text:", mtask.group(1))

                mcompl = regexes.REtask_compl.match(t)
                if not(mcompl):
                    tasks.append(t)

        return tasks

    # parse tasks from set of notes
    def createTasks(self, notes):

        msg = "\n"
        for note in notes:
            name = note.title
            #print("**********")
            #print("project name: {}".format(name))
            tasks = self.getTasks(note.body)
            #print("***tasks were:")
            #print(tasks)
             
            msg += "+++ {}\n".format(name)

            itasks = 1
            for task in tasks:
                msg += "- [ ] {}\n".format(task)

                #print only 2 first ones
                if itasks >= 2:
                    break
                itasks += 1

            msg += "\n"

        self.body = msg


    # print all content
    def print(self, msg):
        print("tasklist {} writing to msg".format(self.title))
        msg += "--------------------------------------------------------------\n"
        msg += "## {}\n".format(self.title)
        prewv = self.body.rstrip()
        msg += "{}\n".format(prewv)

        msg += "\n"

        return msg


# read note from file and create an object
def readNoteFile(fname):
    n = Note()
    f = open(fname, "r")

    # read until message
    for line in f:
        if regexes.REmsgb.match(line):
            break

        mname = regexes.REname.match(line)
        if mname:
            n.setName(mname.group(1))

        mtitle = regexes.REtitle.match(line)
        if mtitle:
            n.setTitle(mtitle.group(1))

        mdate = regexes.REdate.match(line)
        if mdate:
            n.setDate(mdate.group(1))

    # read body
    body = ""
    for line in f:
        body += line

    # TODO catch error if there is no --- separator
    n.setBody(body)

    f.close()

    return n
