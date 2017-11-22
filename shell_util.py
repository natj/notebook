import shlex
import subprocess
import os


try: editor = os.environ["EDITOR"]
except: editor = "nano"



def run(string):

    # shlex.split will preserve inner quotes
    prog = shlex.split(string)

    print(prog[0])


    if prog[0] == "vi":
        # vi hangs when piping stdout/stderr
        p0 = subprocess.Popen(prog)
        stdout, stderr = p0.communicate()
        rc = p0.returncode
    elif prog[0] in ["vim", "nvim"]:
        print(prog)
        p0 = subprocess.Popen(prog)
        stdout, stderr = p0.communicate()
        rc = p0.returncode
    else:
        p0 = subprocess.Popen(prog, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE)
        stdout0, stderr0 = p0.communicate()
        rc = p0.returncode
        stdout = stdout0.decode('utf-8')
        stderr = stderr0.decode('utf-8')

    return stdout, stderr, rc



def openFile(tmpf):
    prog = "{} {}".format(editor, tmpf)
    print(prog)
    
    stdout, stderr, rc = run(prog)
    print("exiting prog")





