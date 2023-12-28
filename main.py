from tkinter import *

screen = Tk()
screen.title("BMI Calculator")
screen.minsize(width=250, height=300)

def button_clicked():
    def bmi_calculate():
        try:
            weight = float(entry_weight.get())
            height = float(entry_height.get())
        except ValueError:
            t.config(text="Please enter valid numbers for weight and height.")
            return
        if weight <= 0 or height <= 0:
            t.config(text="Please enter positive values for weight and height.")
        else:
            bmi = weight / (height ** 2)
            t.config(text=f"Your BMI: {bmi} - {get_bmi_category(bmi)}")

    def get_bmi_category(bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal Weight"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    bmi_calculate()

label_weight = Label(text="Enter Your Weight (kg):", font=("Arial", 8, "bold"))
label_weight.pack(pady=5)
entry_weight = Entry(width=18)
entry_weight.pack(pady=5)
entry_weight.focus()

label_height = Label(text="Enter Your Height (m):", font=("Arial", 8, "bold"))
label_height.pack(pady=5)
entry_height = Entry(width=18)
entry_height.pack(pady=5)

b = Button(text="Calculate", width=15, command=button_clicked)
b.pack(pady=5)

t = Label(text="")
t.pack(pady=5)

screen.mainloop()
