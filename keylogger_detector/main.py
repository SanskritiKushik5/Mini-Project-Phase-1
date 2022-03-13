from subprocess import Popen, PIPE
import os
import signal
from sys import stdout
from tkinter import *

root = Tk()
root.geometry("700x500")
root.title("Keylogger Detector")
Tops = Frame(root, width=1600, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=800, relief=SUNKEN)
f1.pack(side=LEFT)

lblInfo = Label(Tops, font=('helvetica', 20, 'bold'),
                text="Keylogger Detector \n For Windows",
                fg="Black", bd=10, anchor='w')

lblInfo.grid(row=0, column=0)

potential_keyloggers = ['logkey', 'keylog', 'keysniff',
                        'lkl', 'ttrpld', 'uber', 'vlogger', 'wolfeye', 'kidlogger', 'spyrix']


def exit_detector():
    root.destroy()

def refresh():
    get_process_list()

class Process(object):
    def __init__(self, process_info):
        self.name = process_info[0]
        self.pid = process_info[1]

def get_process_list():
    process_list = []

# tasklist to see processes in Windows cmd
# subprocess PIPE to get output of child process as a string
    sub_process = Popen(['tasklist'], shell=False, stdout=PIPE)

    # Get rid of first line that is the header and spaced names
    sub_process.stdout.readline()
    sub_process.stdout.readline()
    sub_process.stdout.readline()

    for line in sub_process.stdout:
        # all lists have length 6 for no spaced names
        process_info = line.decode("utf-8").replace("b'", "").split()
        if len(process_info) == 6:
            process_list.append(Process(process_info))

    logger_detected = 0

    for process in process_list:
        for logger in potential_keyloggers:
            if (process.name.find(logger) > -1):
                stdout.write('KeyLogger Detected : \n The following process may be a key logger : \n\n' +
                            process.name + ' ----> ' + logger)
                lblInfo = Label(Tops, font=('arial', 12, 'bold'),
                text="KeyLogger Detected : \n The following process may be a key logger : \n\n" + process.name + "--->" + logger,
                fg="Black", bd=10, anchor='w')
                lblInfo.grid(row=1, column=0)

                logger_detected = 1

    if logger_detected == 0:
        lblInfo = Label(Tops, font=('arial', 12, 'bold'),
                text="No KeyLogger was Detected",
                fg="Black", bd=10, anchor='w')

        lblInfo.grid(row=1, column=0)

    # exit()
btnRes = Button(Tops, font=('arial', 10, 'bold'),
                text="Rescan",
                fg="Black", bg="yellow", bd=10, anchor='w', command=refresh)

btnRes.grid(row=7, column=0)

btnExit = Button(Tops, font=('arial', 10, 'bold'),
                text="Exit",
                fg="Black", bg="red", bd=10, anchor='w', command=exit_detector)

btnExit.grid(row=10, column=0)


root.mainloop()


if __name__ == '__main__':
    get_process_list()
