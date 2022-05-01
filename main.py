from tkinter import *

class App():
    def __init__(self,master):
        self.master = master
        self.frame = Frame(master)
        self.frame.pack(pady=10)
        self.ui()
    def ui(self):
        self.lb = Listbox(self.frame,width=400,height=10,font = ('Arial 15'))
        self.lb.pack()

        self.sent = Entry(self.frame,width=200,font=('Arial 20'))

        self.sent.pack(pady=10)

        btn_add = Button(self.frame,text="Add Action to List",command=self.add_action)
        btn_add.pack(pady=10)
        btn_remove = Button(self.frame,text="Remove Selected Action",command=self.remove_action)
        btn_remove.pack(pady=10)
    def add_action(self):
        
        ent_value = self.sent.get()
        if ent_value != '':
            self.lb.insert(0,ent_value)
        else:
            self.lbl = Label(self.frame,text="Has No selected Anyone of Value",fg="red")
            self.lbl.pack(pady=10)

    def remove_action(self):

        lb_value = self.lb.get(ACTIVE)

        idx = self.lb.get(0,END).index(lb_value)

        if lb_value != '' and idx != None:
            self.lb.delete(0,idx)

if __name__ == '__main__':
    root = Tk()
    root.geometry('400x500')
    root.resizable(False,False)
    root.iconbitmap('assets/todo.ico')
    root.title('  ****** Todo List By Me *******  ')
    app = App(root)
    root.mainloop()