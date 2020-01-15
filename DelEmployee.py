import EmployeesList as el
import tkinter as tk
HEIGHT = 150
WIDTH = 200

def draw():
    root = tk.Tk()
    root.title("Delete Employee")
    root.resizable(False, False)

    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    frame = tk.Frame(root, bg='#8c8c8c')
    frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    name_label = tk.Label(frame, text="Name")
    name_label.place(relx=0.05, rely=0.05, relheight=0.2, relwidth=0.9)

    name_entry = tk.Entry(frame)
    name_entry.place(relx=0.05, rely=0.3, relwidth=0.9, relheight=0.3)

    submit_button = tk.Button(frame, text="submit", command=lambda : delete(name_entry.get(), root))
    submit_button.place(relx=0.05, rely=0.65, relwidth=0.9, relheight=0.3)

def delete(name, window):
    el.Employees.remove(name)
    del(el.Adreses[name])
    del(el.Mails[name])
    del(el.Specialization[name])
    del(el.Salaries[name])

    window.destroy()
