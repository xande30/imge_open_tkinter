import os
import sys
from tkinter import *
from colorama import Fore, Back

imgdir = '..//pythonProject//'
imgfile = 'hellopython.GIF'
if len(sys.argv) > 1:
    imgfile = sys.argv[1]
imgpath = os.path.join(imgdir, imgfile)

win = Tk()
win.title(imgfile)
imgobj = PhotoImage(file=imgpath)
Label(win, image=imgobj).pack()
Button(win, text='Do you like the image?',bd=2,background='green', fg='yellow').pack()
print(Fore.LIGHTGREEN_EX,Back.LIGHTBLACK_EX,imgobj.width(), imgobj.height())
if __name__ == '__main__':
    win.mainloop()
