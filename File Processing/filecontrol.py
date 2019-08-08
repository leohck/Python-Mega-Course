#  Copyright (c)  8/8/2019
#  Developed by: Leonardo Black | 21 years old | Computer Engineer


import time
import os


filepath = "files"
filename = "info.txt"
originalcontent = "Leonardo Black"
newfile = ""
masterfile = os.path.join(filepath, filename)


def gettime():
    timenow = time.localtime()
    return "{0}{1}{2}{3}{4}{5}".format(timenow[2], timenow[1], timenow[0], timenow[3], timenow[4], timenow[5])


while True:
    try:
        with open(masterfile, "x") as infofile:
            infofile.write(originalcontent)
    except FileExistsError:
        while True:
            with open(masterfile, "r") as infofile:
                infocontent = infofile.read()
                if infocontent == originalcontent:
                    # print(infocontent)
                    pass
                else:
                    print("The {0} file was altered:\n\t Original content:{1}\n\t New Content: {2}".format(filename, originalcontent, infocontent))
                    newfile = "{0}.txt".format(gettime())
                    with open(os.path.join(filepath, newfile), 'x') as _newfile:
                        _newfile.write(infocontent)
                    with open(masterfile, "w") as _masterfile:
                        _masterfile.write(originalcontent)
                    print("The original file was restaured and a new file \'{0}\' was created with the false content on the original file.".format(newfile))
                time.sleep(3)
