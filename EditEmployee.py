import EmployeesList as el
import tkinter as tk
HEIGHT = 150
WIDTH = 200

def draw():
    root = tk.Tk()
    names = el.Employees
    root.title("Edit")
    root.resizable(False, False)

    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    frame = tk.Frame(root, bg='#8c8c8c')
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    name_label = tk.Label(frame, text="Name")
    name_label.place(relx=0.05, rely=0.05, relheight=0.2, relwidth=0.9)

    name = tk.StringVar(root)
    name.set(names[0])
    choiceMenu = tk.OptionMenu(frame, name, *names)
    choiceMenu.place(relx=0.05, rely=0.3, relwidth=0.9, relheight=0.3)

    submit_button = tk.Button(frame, text="submit", command=lambda : show_edit_window(name.get(), root))
    submit_button.place(relx=0.05, rely=0.65, relwidth=0.9, relheight=0.3)

def show_edit_window(name, win):
    win.destroy()
    root = tk.Tk()
    perTimeOptions = ["per hour", "per day", "per week", "per month"]
    root.title("Add Employee")
    root.resizable(False, False)

    canvas = tk.Canvas(root, height=700, width=600)
    canvas.pack()

    frame = tk.Frame(root, bg='#8c8c8c')
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    MailLabel = tk.Label(frame, text="Email")
    MailLabel.place(relx=0.2, rely=0.2, relwidth=0.1, relheight=0.05)

    MailEntry = tk.Entry(frame)
    print(el.Mails[name])
    MailEntry.insert(tk.END, el.Mails[name])
    MailEntry.place(relx=0.3, rely=0.2, relwidth=0.4, relheight=0.05)

    AdresLabel = tk.Label(frame, text="Adres")
    AdresLabel.place(relx=0.2, rely=0.3, relwidth=0.1, relheight=0.05)

    AdresEntry = tk.Entry(frame)
    AdresEntry.insert(tk.END, el.Adreses[name])
    AdresEntry.place(relx=0.3, rely=0.3, relwidth=0.4, relheight=0.05)

    SpecLabel = tk.Label(frame, text="Specialization")
    SpecLabel.place(relx=0.15, rely=0.4, relwidth=0.15, relheight=0.05)

    SpecEntry = tk.Entry(frame)
    SpecEntry.insert(tk.END, el.Specialization[name])
    SpecEntry.place(relx=0.3, rely=0.4, relwidth=0.4, relheight=0.05)

    SalaryLabel = tk.Label(frame, text="Salary")
    SalaryLabel.place(relx=0.2, rely=0.5, relwidth=0.1, relheight=0.05)

    SalaryEntry = tk.Entry(frame)
    SalaryEntry.insert(tk.END, el.Salaries[name].split()[0])
    SalaryEntry.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.05)
    
    perTime = tk.StringVar(root)
    perTime.set(el.Salaries[name].split()[1])
    perTimeDropdown = tk.OptionMenu(frame, perTime, *perTimeOptions)
    perTimeDropdown.place(relx=0.7, rely=0.5, relwidth=0.2, relheight=0.05)

    
    errorText = tk.Label(frame, text="", bg='#8c8c8c', fg='#ff1500')
    errorText.place(relx=0.35, rely=0.6, relwidth=0.55, relheight=0.05)

    addButton = tk.Button(frame, text="sumbit", command=lambda: edit(
        name, MailEntry.get(), AdresEntry.get(), SpecEntry.get(), SalaryEntry.get(), perTime.get() ,root, errorText))
    addButton.place(relx=0.2, rely=0.6, relwidth=0.1, relheight=0.05)

def edit(name, mail, adres, spec, salary, salaryTime ,window, errorText):

    if mail == "" or adres == "" or spec == "" or salary == "" or salaryTime == "":
        errorText['text'] = "You have left some free spaces"
        return

    el.Mails[name] = mail
    el.Adreses[name] = adres
    el.Specialization[name] = spec
    el.Salaries[name] = salary + " " + salaryTime
    window.destroy()