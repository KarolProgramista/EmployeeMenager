from tkinter import font
import tkinter as tk
import pickle
import AddEmployee as ae
import EmployeesList as el

HEIGHT = 700
WIDTH = 800

root = tk.Tk()

root.title("Employee Menager")


class Application(object):

    # Constructor
    def __init__(self):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
        self.canvas.pack()
        self.load()
        self.draw()

    # Drawing window and content
    def draw(self):


        leftFrame = tk.Frame(root, bg="#7f7f7f")
        leftFrame.place(relx=0, rely=0, relwidth=0.2, relheight=1)

        # Drawing tool bar
        self.drawSubmenu()

        count = 0
        for a in el.Employers:
            newname = ('button' + str(count))
            print(newname)
            newname = tk.Button(leftFrame, text=a, command=lambda index=count: self.showInfo(el.Employers[index]))
            newname.grid(row=count, column=1)
            count += 1

        rightFrame = tk.Frame(root, bg="#a3a3a3")
        rightFrame.place(relx=0.2, rely=0, relwidth=0.8, relheight=1)

        self.text = tk.Label(rightFrame, font=40)
        self.text.place(x=0, y=30, relwidth=1, relheight=0.9, width=- 18)

    # Drawing toolbar
    def drawSubmenu(self):
        self.menu = tk.Menu(root)

        submenu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Employees", menu=submenu)

        submenu.add_command(label="Add", command=lambda: ae.draw())
        submenu.add_command(label="Refresh", command=lambda: self.draw())
        submenu.add_command(label="Save Configuration", command=lambda: self.save())

        root.config(menu=self.menu, width=50, height=30)

    # Showing info about person
    def showInfo(self, name):
        print(name)
        final_str = (f"""
          {name}
        eMail: {el.Mails[name]}
        Adres: {el.Adreses[name]}
        Specialization: {el.Specialization[name]}
        Salary: {el.Salaries[name]}""")

        self.text['text'] = final_str

    # Saveing data
    def save(self):
        employersSaveFile = open('ESF.dat', 'wb')
        mailsSaveFile = open('MSF.dat', 'wb')
        adresesSaveFile = open('ASF.dat', 'wb')
        specSaveFile = open('SSF.dat', 'wb')
        salariesSaveFile = open('SaSF.dat', 'wb')

        pickle.dump(el.Employers, employersSaveFile)
        pickle.dump(el.Mails, mailsSaveFile)
        pickle.dump(el.Adreses, adresesSaveFile)
        pickle.dump(el.Specialization, specSaveFile)
        pickle.dump(el.Salaries, salariesSaveFile)

        employersSaveFile.close()
        mailsSaveFile.close()
        adresesSaveFile.close()
        specSaveFile.close()
        salariesSaveFile.close()

    # Loadnig data
    def load(self):
        try:
            employersSaveFile = open('ESF.dat', 'rb')
            mailsSaveFile = open('MSF.dat', 'rb')
            adresesSaveFile = open('ASF.dat', 'rb')
            specSaveFile = open('SSF.dat', 'rb')
            salariesSaveFile = open('SaSF.dat', 'rb')

            el.Employers = pickle.load(employersSaveFile)
            el.Mails = pickle.load(mailsSaveFile)
            el.Adreses = pickle.load(adresesSaveFile)
            el.Specialization = pickle.load(specSaveFile)
            el.Salaries = pickle.load(salariesSaveFile)

            employersSaveFile.close()
            mailsSaveFile.close()
            adresesSaveFile.close()
            specSaveFile.close()
            salariesSaveFile.close()
        except:
            print("There aren't save files.")


# Starting app
app = Application()
app.draw
root.mainloop()
