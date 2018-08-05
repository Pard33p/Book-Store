"""
A program that stores book information:

Title, Author, Year, ISBN

User can:

View all records
Search an entry
Add entry
Update entry
Delete an entry
Close

"""

from tkinter import *
import backEnd

def getSelectedRow(event):
    #tuple with one item(index) of selected row
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])
    

def viewCommand():
    list1.delete(0,END) #delete from index 0 to END
    for row in backEnd.view():
        list1.insert(END,row)

def searchCommand():
    list1.delete(0,END)
    for row in backEnd.search(titleText.get(),authorText.get(),yearText.get(),isbnText.get()):
        list1.insert(END,row)    

def addCommand():
    backEnd.insert(titleText.get(),authorText.get(),yearText.get(),isbnText.get())
    list1.delete(0,END)
    list1.insert(END,(titleText.get(),authorText.get(),yearText.get(),isbnText.get()))

def deleteCommand():
    backEnd.delete(selected_tuple[0])
    viewCommand()
    
def updateCommand():
    backEnd.update(selected_tuple[0],titleText.get(),authorText.get(),yearText.get(),isbnText.get())
    viewCommand()
    

window = Tk()
window.wm_title("Book Store")
l1 = Label(window,text="Title")
l1.grid(row=0,column=0)

l2 = Label(window,text="Author")
l2.grid(row=0,column=2)

l3 = Label(window,text="Year")
l3.grid(row=1,column=0)

l4 = Label(window,text="ISBN")
l4.grid(row=1,column=2)

titleText = StringVar()
e1 = Entry(window,textvariable=titleText)
e1.grid(row=0,column=1)

authorText = StringVar()
e2 = Entry(window,textvariable=authorText)
e2.grid(row=0,column=3)

yearText = StringVar()
e3 = Entry(window,textvariable=yearText)
e3.grid(row=1,column=1)

isbnText = StringVar()
e4 = Entry(window,textvariable=isbnText)
e4.grid(row=1,column=3)

list1 = Listbox(window,height=10,width=35)
list1.grid(row=2,column=0,rowspan=10,columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=10)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',getSelectedRow)


b1 = Button(window,text="View All Books",width=15,command=viewCommand)
b1.grid(row=2,column=3)

b2 = Button(window,text="Search Entry",width=15,command=searchCommand)
b2.grid(row=3,column=3)

b3 = Button(window,text="Add Entry",width=15,command=addCommand)
b3.grid(row=4,column=3)

b4 = Button(window,text="Update Selected",width=15,command=updateCommand)
b4.grid(row=5,column=3)

b5 = Button(window,text="Delete Selected",width=15,command=deleteCommand)
b5.grid(row=6,column=3)

b6 = Button(window,text="Close",width=15,command=window.destroy)
b6.grid(row=7,column=3)



window.mainloop() 
