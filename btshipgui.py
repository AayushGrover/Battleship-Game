from btship__engine import *
from Tkinter import *
import os
window=Tk()
window.config(bg="white") #will set the background of window to white.
window.title("BATTLESHIP")#will give the title to window as BATTLESHIP.

topFrame=Frame(window)# creates a top frame.
topFrame.config(bg="white")
topFrame.pack(side=TOP,fill=X)

title=Label(topFrame,text="BATTLESHIP",bg="red")#will set the title to BATTLESHIP.
title.config(font=50)#sets the size of the text to 50.
title.pack(side=TOP)

label1=Label(topFrame)
label1.config(width=15,bg="white")
label1.pack(side=TOP)

label2=Label(topFrame,text="YOUR TERRITORY",fg="blue")#adds text as YOUR TERRITORY
label2.config(font=30,width=15)												#fg sets the text of the colour to blue
label2.pack(side=LEFT)

blank=Label(topFrame)#adds a blank label to create gap.
blank.config(width=30,font=25,bg="white")#width sets the width of the label as 30.
blank.pack(side=RIGHT,fill=X)

label3=Label(topFrame,text="ENEMY TERRITORY",fg="blue")#adds text as ENEMY TERRITORY
label3.config(font=30,width=15)
label3.pack(side=RIGHT)

rightFrame=Frame(window)
rightFrame.config(bg="white")
leftFrame=Frame(window)
leftFrame.config(bg="white")

userframe=Frame(leftFrame)
userframe.config()
userGrid=[]
#to create a 10X10 grid with buttons
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
#to create a 10X10 grid with buttons
for j in range(10):
    Brow=[]
    for i in range(10):
        
        b=Button(compframe,bg="lightblue")
        b.config(height=1,width=2)
        b.grid(row=j,column=i)
        Brow.append(b)
    compGrid.append(Brow)
compframe.pack(side=LEFT)
def quit():#quits the game
    window.destroy()  
def newgame():#pressing the button starts a new game
    cmd="python btshipgui2.py"#links the newgame button to btshipgui2.py file
    f=os.popen(cmd)
    quit()
def rules():#pressing the button opens the rules window 
    cmd="python rules.py"
    f=os.popen(cmd)
def about():#pressing the button open the about window 
    cmd="python about.py"
    f=os.popen(cmd)

newgamebutton=Button(rightFrame,text="New Game",bg="light green", command=newgame)#creates a new game button
optionsbutton=Button(rightFrame,text="Rules",bg="light green", command=rules)#creates a options button
rulesbutton=Button(rightFrame,text="About",bg="light green", command=about)#creates a rules button
aboutbutton=Button(rightFrame,text="Quit",bg="light green",command=quit)#creates a about button

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



leftFrame.pack(side=LEFT)#creates a leftframe in window
gap1.pack(side=LEFT)
rightFrame.pack(side=RIGHT)#creates a rightframe in window

bottomFrame.pack(side=BOTTOM,fill=X)#creates a bottom frame in window


window.mainloop()
