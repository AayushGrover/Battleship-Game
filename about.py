from Tkinter import*
window=Tk()
window.config(bg="orange")#sets background of window as orange
window.title("ABOUT")#adds ABOUT as the title of window

topFrame=Frame(window)#adds a topframe in window
topFrame.config(bg="orange")
topFrame.pack(side=TOP,fill=X)

title=Label(topFrame,text="ABOUT",bg="orange")#adds a label containing text ABOUT.
title.config(fg="yellow",font=30)
title.pack(side=TOP)

gap1=Label(topFrame,bg="orange")#creates a gap between text and ABOUT label
gap1.config(height=2)
gap1.pack(side=TOP)
#adds text to topframe.
label1=Label(topFrame,text="The BATTLESHIP GAME is created by:\n\nABHIRAMON R.\n\nATHARVA DESHPANDE\n\nNAMAN DOSI\n\n\nWe invite your valuable suggestions on our mail id: btship123@gmail.com\n\n\n                    ~THANKS FOR PLAYING OUR GAME~",anchor=W,justify=LEFT)
label1.config(font=30,bg="orange")
label1.pack(side=LEFT)

window.mainloop()

