import EmployeesList as el
import tkinter as tk
HEIGHT = 700
WIDTH = 800


def draw():
    root = tk.Tk()
    perTimeOptions = ["per hour", "per day", "per week", "per month"]
    root.title("Add Employee")
    root.resizable(False, False)

    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    frame = tk.Frame(root, bg='#8c8c8c')
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    nameLabel = tk.Label(frame, text="Name")
    nameLabel.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.05)

    nameEntry = tk.Entry(frame)
    nameEntry.place(relx=0.3, rely=0.1, relwidth=0.4, relheight=0.05)

    MailLabel = tk.Label(frame, text="Email")
    MailLabel.place(relx=0.2, rely=0.2, relwidth=0.1, relheight=0.05)

    MaliEntry = tk.Entry(frame)
    MaliEntry.place(relx=0.3, rely=0.2, relwidth=0.4, relheight=0.05)

    AdresLabel = tk.Label(frame, text="Adres")
    AdresLabel.place(relx=0.2, rely=0.3, relwidth=0.1, relheight=0.05)

    AdresEntry = tk.Entry(frame)
    AdresEntry.place(relx=0.3, rely=0.3, relwidth=0.4, relheight=0.05)

    SpecLabel = tk.Label(frame, text="Specialization")
    SpecLabel.place(relx=0.15, rely=0.4, relwidth=0.15, relheight=0.05)

    SpecEntry = tk.Entry(frame)
    SpecEntry.place(relx=0.3, rely=0.4, relwidth=0.4, relheight=0.05)

    SalaryLabel = tk.Label(frame, text="Salary")
    SalaryLabel.place(relx=0.2, rely=0.5, relwidth=0.1, relheight=0.05)

    SalaryEntry = tk.Entry(frame)
    SalaryEntry.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.05)
    
    perTime = tk.StringVar(root)
    perTime.set(perTimeOptions[0])
    perTimeDropdown = tk.OptionMenu(frame, perTime, *perTimeOptions)
    perTimeDropdown.place(relx=0.7, rely=0.5, relwidth=0.2, relheight=0.05)

    addButton = tk.Button(frame, text="sumbit", command=lambda: Add(
        nameEntry.get(), MaliEntry.get(), AdresEntry.get(), SpecEntry.get(), SalaryEntry.get(), perTime.get() ,root))
    addButton.place(relx=0.2, rely=0.6, relwidth=0.1, relheight=0.05)


def Add(name, mail, adres, spec, salary, salaryTime ,window):
    el.Employees.append(name)
    el.Mails[name] = mail
    print(el.Adreses)
    el.Adreses[name] = adres
    el.Specialization[name] = spec
    el.Salaries[name] = salary + " " + salaryTime
    window.destroy()
