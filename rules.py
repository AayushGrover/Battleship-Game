from Tkinter import*
window=Tk()
window.config(bg="white")
window.title("RULES")

topFrame=Frame(window)
topFrame.config(bg="white")
topFrame.pack(side=TOP,fill=X)

#rightFrame=Frame(window)

title=Label(topFrame,text="RULES OF THE GAME",bg="white")
title.config(font=50,fg="red")
title.pack(side=TOP)

#rightFrame.config(bg="white",height=70,width=100)
#rightFrame.pack(side=RIGHT,fill=X)

gap1=Label(topFrame,bg="white")
gap1.config(height=2)
gap1.pack(side=TOP)
#creates a label in topframe and adds text to it.
label1=Label(topFrame,text="The game has two 10X10 grids, one for computer and the other for user.The player plays his turn by choosing a tile of the grid of the enemy territory.The game\n has five varities of ships, length varying from 5 blocks to 1 blocks as given in index.There is 1 AIRCRAFT CARRIER[5],1 SUBMARINE[4],1 BATTLESHIP[3],\n2 DESTROYER[2] and 2 PETROL SHIP[1].When a player plays his turn and hits the tile,colour of the tile changes.If the colour changes to red implies a ship\n has been hit else it changes to yellow indicating that he missed.Immediately computer plays its turn, hits a tile in the grid of the user territory.If the colour \nchanges to black, it implies that computer has hit a ship else colour changes to yellow implying computer missed.One who destroys all the ships first,\nwins the game.",anchor=W,justify=LEFT)
label1.config(font=30,bg="white")
label1.pack(side=LEFT)

gap2=Label(window,bg="white")#creates a gap between text and INDEX OF SHIPS label.
gap2.config(height=10)
gap2.pack(side=TOP,fill=X)

label2=Label(window,text="INDEX OF SHIPS")#ceates a label with text INDEX OF SHIPS.
label2.config(font=30,bg="white",fg="green")
label2.pack(side=TOP)

label3=Label(window,text="AIRCRAFT CARRIER  ")#ceates a label with AIRCRAFT CARRIER.
label3.config(font=30,bg="white",fg="blue",anchor=W)
label3.pack(side=LEFT)
#adds a row of 5 buttons
acbuttons=[]
for i in range(5):
	b=Button(window,height=1,width=2,bg="red")
	acbuttons.append(b)
	b.pack(side=LEFT)

label4=Label(window,text="")#this is a gap after 5 button. 
label4.config(bg="white",height=0,width=2)
label4.pack(side=LEFT,fill=X)

label5=Label(window,text="SUBMARINE  ")#ceates a label with SUBMARINE.
label5.config(font=30,bg="white",fg="blue",anchor=W)
label5.pack(side=LEFT)
#adds a row of 4 buttons
cbuttons=[]
for i in range(4):
	b=Button(window,height=1,width=2,bg="red")
	acbuttons.append(b)
	b.pack(side=LEFT)

label6=Label(window,text="")#this is a gap after 4 button.
label6.config(bg="white",height=0,width=2)
label6.pack(side=LEFT,fill=X)

label7=Label(window,text="BATTLESHIP  ")#ceates a label BATTLESHIP.
label7.config(font=30,bg="white",fg="blue",anchor=W)
label7.pack(side=LEFT)
#adds a row of 3 buttons
cbuttons=[]
for i in range(3):
	b=Button(window,height=1,width=2,bg="red")
	acbuttons.append(b)
	b.pack(side=LEFT)

label8=Label(window,text="")#this is a gap after 3 button.
label8.config(bg="white",height=0,width=2)
label8.pack(side=LEFT,fill=X)

label9=Label(window,text="DESTROYER  ")#ceates a label with DESTROYER.
label9.config(font=30,bg="white",fg="blue",anchor=W)
label9.pack(side=LEFT)
#adds a row of 2 buttons
cbuttons=[]
for i in range(2):
	b=Button(window,height=1,width=2,bg="red")
	acbuttons.append(b)
	b.pack(side=LEFT)
	
label10=Label(window,text="")#this is a gap after 2 button.
label10.config(bg="white",height=0,width=2)
label10.pack(side=LEFT,fill=X)
		
label11=Label(window,text="PATROL  ")#creates a label with PATROL.
label11.config(font=30,bg="white",fg="blue",anchor=W)
label11.pack(side=LEFT)
#adds a row of 1 buttons
cbuttons=[]
for i in range(1):
	b=Button(window,height=1,width=2,bg="red")
	acbuttons.append(b)
	b.pack(side=LEFT)
	

#mEntry = Entry().pack()

window.mainloop()
