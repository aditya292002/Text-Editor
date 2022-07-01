from tkinter import Tk,scrolledtext,Menu,filedialog,END,messagebox,simpledialog
import tkinter.scrolledtext as ScrolledText
import tkinter
#root for main window
root=Tk(className="Saloni's Text Editor ")
textArea = ScrolledText.ScrolledText(root,width=100,height=80)



#functions



def newFile():
    if len(textArea.get('1.0',END+'-1c'))>0:
        if messagebox.askyesno('save?','Do you wish to save?'):
            saveFile()
        else:
            textArea.delete('1.0',END)

def openFile():
    file=filedialog.askopenfile(parent=root,mode='rb',title='select a text file')

    if file != None:
        contents = file.read()
        textArea.insert('1.0',contents)
        file.close()

def saveFile():
    file = filedialog.asksaveasfile(mode="w")

    if file != None:
        #slice off the last character from get, as an extra return (enter) is added
        data=textArea.get('1.0',END+'-1c')
        file.write(data)
        file.close()

def findinFile():
    findstring = simpledialog.askstring('Find...','Enter text')
    textdata=textArea.get('1.0',END+'-1c')
    if findstring in textdata:
        print('True')
    else:
        print("False")


def about():
    label = messagebox.showinfo('About','A python alternative to Notepad!')

def help1():
    label = messagebox.showinfo('Help','This is the python alternative to notepad with features like : , 1.Finding if a word is present in the text file , 2.Saving the file /n 3.Opening the file , 4.Opening a new file etc')
    
def exit1():
    if messagebox.askyesno('Quit','Are you sure you want to quit?'):
        root.destroy()  

#def about():
    #if messagebox.showinfo('About','A Python alternative to Notepad')
    
#menu options
menu = Menu(root)
root.config(menu=menu)
fileMenu = Menu(menu)
menu.add_cascade(label='File',menu=fileMenu)
fileMenu.add_command(label='New',command=newFile)
fileMenu.add_command(label='Open',command=openFile)
fileMenu.add_command(label='Save',command=saveFile)
fileMenu.add_command(label='FindinFile',command=findinFile)
fileMenu.add_command(label='Print')
fileMenu.add_separator()
fileMenu.add_command(label='Exit',command=exit1)

helpMenu = Menu(menu)
#menu.add_cascade(label='Format',command=)
menu.add_cascade(label='Help',command=help1)
menu.add_cascade(label='About',command=about)
    
textArea.pack()


root.mainloop()
    

