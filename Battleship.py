from Tkinter import *
import os

root = Tk()
root.title("BATTLESHIP")				# adds a title to window, BATTLESHIP.
cwgt=Canvas(root,height=615,width=1250)
cwgt.pack(expand=True, fill=BOTH)

#To add image as a background to window. 
image1=PhotoImage(file="btship.gif")
cwgt.img=image1
cwgt.create_image(0, 0, anchor=NW, image=image1)

def startgame(): 						# on pressing the button, this method is called, which starts the game.
	cmd="python btshipgui.py"
	file=os.popen(cmd)
	root.destroy()

b1=Button(cwgt, text="START GAME", bd=0,bg="red",font=30,command=startgame)		# creates a START GAME button.
b1.pack(side=BOTTOM)
cwgt.create_window(20,20, window=b1, anchor=NW)
root.mainloop()
