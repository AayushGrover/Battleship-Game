from btship__engine import *
from Tkinter import *
import os
'''
This program is opened if new game button is pressed in btshipgui.py program. It calls btshipgui.py program
when new button is pressed in this program. Otherwise it is identical to it.
'''

window=Tk()
window.config(bg="white")
window.title("BATTLESHIP")

topFrame=Frame(window)
topFrame.config(bg="white")
topFrame.pack(side=TOP,fill=X)

title=Label(topFrame,text="BATTLESHIP",bg="red")
title.config(font=50)
title.pack(side=TOP)

label1=Label(topFrame)
label1.config(width=15,bg="white")
label1.pack(side=TOP)

label2=Label(topFrame,text="YOUR TERRITORY",fg="blue")
label2.config(font=30,width=15)
label2.pack(side=LEFT)

blank=Label(topFrame)
blank.config(width=30,font=25,bg="white")
blank.pack(side=RIGHT,fill=X)

label3=Label(topFrame,text="ENEMY TERRITORY",fg="blue")
label3.config(font=30,width=15)
label3.pack(side=RIGHT)

rightFrame=Frame(window)
rightFrame.config(bg="white")
leftFrame=Frame(window)
leftFrame.config(bg="white")

userframe=Frame(leftFrame)
userframe.config()
userGrid=[]
for j in range(10):
    Brow=[]
    for i in range(10):
        b=Button(userframe,bg="lightblue")
        b.config(height=1,width=2)
        b.grid(row=j,column=i)
        Brow.append(b)
    userGrid.append(Brow)
userframe.pack(side=LEFT)

compframe=Frame(rightFrame)
compframe.config()
compGrid=[]
for j in range(10):
    Brow=[]
    for i in range(10):
        
        b=Button(compframe,bg="lightblue")
        b.config(height=1,width=2)
        b.grid(row=j,column=i)
        Brow.append(b)
    compGrid.append(Brow)
compframe.pack(side=LEFT)
def quit():
    window.destroy()  
def newgame():
    cmd="python btshipgui.py"
    f=os.popen(cmd)
    quit()
def rules():
    cmd="python rules.py"
    f=os.popen(cmd)
def about():
    cmd="python about.py"
    f=os.popen(cmd)

newgamebutton=Button(rightFrame,text="New Game",bg="light green", command=newgame)
optionsbutton=Button(rightFrame,text="Rules",bg="light green", command=rules)
rulesbutton=Button(rightFrame,text="About",bg="light green", command=about)
aboutbutton=Button(rightFrame,text="Quit",bg="light green",command=quit)

aboutbutton.config(height=3,width=10,font=25)
aboutbutton.pack(side=BOTTOM)

rulesbutton.config(height=3,width=10,font=25)
rulesbutton.pack(side=BOTTOM)
 
optionsbutton.config(height=3,width=10,font=25)
optionsbutton.pack(side=BOTTOM)

newgamebutton.config(height=3,width=10,font=25)
newgamebutton.pack(side=BOTTOM)

bottomFrame=Frame(window,height=50,width=60)
bottomFrame.config(bg="white")
label4=Label(topFrame,text="")
label4.config(bg="white",font=45,width=50)
label4.pack(side=TOP)
leftFrame.config(height=30)
rightFrame.config(height=30)

gap1=Label(window,bg="white")
gap1.config(width=16,height=26)


comp=Comp(userGrid)
user=User(compGrid,comp,label4)



leftFrame.pack(side=LEFT)
gap1.pack(side=LEFT)
rightFrame.pack(side=RIGHT)

bottomFrame.pack(side=BOTTOM,fill=X)


window.mainloop()
