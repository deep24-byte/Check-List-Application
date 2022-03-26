from tkinter import *
from tkinter import messagebox
root = Tk()

#ROOT PROPERTIES
root.title("My Checklist App")
root.geometry("500x500")
root.resizable(0,0)



#Setting uo general fonts and colours
myFont = ("Ariel",12)
rootColour = "#3b5998"
buttonsColour = "#f7f7f7"
root.config(bg=rootColour)




#function defining
def addIteam():
    if listEntery.get() =="":
        #message popup
        messagebox.showinfo("Illegal Entry in the list","cannot enterblank iteam in the list")
        
    else:
        listBox.insert(END,listEntery.get())
        listEntery.delete(0,END)

# function to remove the anchored (selected)item from list

def removeIteam():
    listBox.delete(ANCHOR)

def clearList():
    listBox.delete(0,END)

#function to save the listbox contents into an external txt file.

def saveList():
    with open("checklist.txt",'w') as f:
        listTuple = listBox.get(0,END)
        for items in listTuple:
            f.write(items + "\n")


#function to re call stored element in text file

def openList():
    try:
        
        with open("checklist.txt",'r') as f:
            for line in f:
            
                listBox.insert(END,line)
    except:
        
        pass
        
    
 

    
    


#crating layout of the app
#creating frames
inputFrame = Frame(root,bg =rootColour,)
outputFrame = Frame(root,bg=rootColour)
buttonsFrame = Frame(root,bg=rootColour)
inputFrame.pack()
outputFrame.pack()
buttonsFrame.pack()

#layout of element in inpuut frame - entery widget,add item button

listEntery = Entry(inputFrame,width = 25,borderwidth= 3,font=myFont)
listAddButton = Button(inputFrame,text = "Add Item",borderwidth=2,font=myFont,bg =buttonsColour,padx=2,pady=10,command = addIteam)
listEntery.grid(row=0,column=0,padx=5,pady=5)
listAddButton.grid(row=0,column=1,padx=5,pady=5)



#creat layout of element in input frame listbox and scrollbar
scrollBar = Scrollbar(outputFrame)
listBox = Listbox(outputFrame,height=15,width=45,borderwidth=3,font=myFont)

scrollBar.config(command=listBox.yview)

listBox.grid(row=0,column=0)
scrollBar.grid(row=0,column=1,sticky="NS")



#creat layout of elements in out framr=e - lidtbox and sctollbar


listRemoveButton = Button(buttonsFrame,text="Remove Item",borderwidth=2,font=myFont,bg =buttonsColour,command= removeIteam)
listClearButton = Button(buttonsFrame,text="Clear List",borderwidth=2,font=myFont,bg =buttonsColour,command= clearList)
saveButton = Button(buttonsFrame,text="save",borderwidth=2,font=myFont,bg =buttonsColour,command = saveList)
quitButton = Button(buttonsFrame,text="Extit",borderwidth=2,font=myFont,bg =buttonsColour,command=root.destroy)

listRemoveButton.grid(row=0,column=0,padx=2,pady=10)
listClearButton.grid(row=0,column=1,padx=2,pady=10,ipadx=15)
saveButton.grid(row=0,column=2,padx=2,pady=10,ipadx=15)
quitButton.grid(row=0,column=3,padx=2,pady=10,ipadx=15)





#main loop
openList()
root.mainloop()


