from tkinter import *
root = Tk()

root.title("Menu")
root.geometry("500x500")

q = IntVar()
q.get()
q.set("1")

def clickme(value):
    my_label=Label(root,text = value)
    my_label.pack()
    
Radiobutton(root, text = "Option 1", variable = q,  value = 1).pack(anchor = "w")
Radiobutton(root, text = "Option 2", variable = q,  value = 2).pack(anchor = "w")
Radiobutton(root, text = "Option 3", variable = q,  value = 3).pack(anchor = "w")
Radiobutton(root, text = "Option 4", variable = q,  value = 4).pack(anchor = "w")
Radiobutton(root, text = "Option 5", variable = q,  value = 5).pack(anchor = "w")

my_label = Label(root, text = q.get())
my_label.pack()

my_button = Button(root, text = "Enter", command = lambda : clickme(q.get()))
my_button.pack()

root.mainloop()
