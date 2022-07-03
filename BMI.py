from tkinter import messagebox
from tkinter import *


# Body Mass Index


BMI_INFO_CONSTANT = 'BMI INFO'

def show_BMI_results(bmi):
    if bmi < 18.5:
        messagebox.showinfo(BMI_INFO_CONSTANT, f'{bmi} -> Underweight')
    elif 18.5 < bmi < 24.9:
        messagebox.showinfo(BMI_INFO_CONSTANT, f'{bmi} -> Normal')
    elif 24.9 < bmi < 29.9:
        messagebox.showinfo(BMI_INFO_CONSTANT, f'{bmi} -> Overweight')
    elif bmi > 29.9:
        messagebox.showinfo(BMI_INFO_CONSTANT, f' {bmi} -> Obesity')
    else:
        messagebox.showerror(BMI_INFO_CONSTANT, 'Something went wrong! Check your kilograms and weight again')


def calculate_bmi():
    kilograms = int(weight_in_kg.get())
    meters = int(height_in_cm.get()) / 100
    bmi = kilograms / (meters * meters)
    bmi = float(f"{bmi:.1f}")
    show_BMI_results(bmi)


root = Tk()

var = IntVar()

root.title('PythonGuides')
root.geometry('400x300')
root.config(bg='black')

app_frame = Frame(root, padx=100, pady=100)
app_frame.pack(expand=True)

height_label = Label(app_frame, bg='grey', text="Enter Height in CM: ")
height_label.grid(row=1, column=1)

weight_label = Label(app_frame, bg='grey', text="Enter Weight in KG: ", )
weight_label.grid(row=2, column=1)

height_in_cm = Entry(app_frame)
height_in_cm.grid(row=1, column=2, pady=5)

weight_in_kg = Entry(app_frame)
weight_in_kg.grid(row=2, column=2, pady=5)

frame3 = Frame(app_frame)
frame3.grid(row=5, columnspan=3, pady=10)

calculate_BMI_button = Button(frame3, text='Calculate your BMI', command=calculate_bmi)
calculate_BMI_button.pack(side=LEFT)

root.mainloop()
