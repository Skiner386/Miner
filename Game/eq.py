from tkinter import *


class Open():
    def __init__(self):
        self.a = None
        self.Minerals = {'Stone': 1, 'Silver': 1, 'Iron': 1, 'Gold': 1, 'Diamond': 1}

Op = Open()
def masno(parametr):
    class Inventory:
        def __init__(self,condition):
            self.root2 = Tk()
            self.condition = condition
            self.stone = PhotoImage('Images/stone.png')


        def Window(self):
            self.root2.title('Inventory')
            self.root2.geometry('300x300')

        def Images(self):
            self.Lab1 = Label(self.root2, text="Stone:").place(x=10,y=10)
            self.Lab2 = Label(self.root2, text=Op.Minerals['Stone']).place(x=70,y=10)

            self.Lab3 = Label(self.root2, text="Iron:").place(x=10,y=30)
            self.Lab4 = Label(self.root2, text=Op.Minerals['Iron']).place(x=70,y=30)

            self.Lab5 = Label(self.root2, text="Silver:").place(x=10,y=50)
            self.Lab6 = Label(self.root2, text=Op.Minerals['Silver']).place(x=70,y=50)

            self.Lab7 = Label(self.root2, text="Gold:").place(x=10,y=70)
            self.Lab8 = Label(self.root2, text=Op.Minerals['Gold']).place(x=70,y=70)

            self.Lab9 = Label(self.root2, text="Diamond:").place(x=10,y=90)
            self.Lab10 = Label(self.root2, text=Op.Minerals['Diamond']).place(x=70,y=90)

        def Loop(self):
            self.Images()

            if Op.a == False:
                #self.condition._stop_event.set()
                self.root2.destroy()
                #raise Exception
            if Op.a == True:
                self.Window()
                self.root2.mainloop()
        #print(Op.a)

    Inv = Inventory(parametr)
    Inv.Loop()