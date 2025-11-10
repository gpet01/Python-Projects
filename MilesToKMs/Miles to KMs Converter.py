from tkinter import *

FONT = ("Courier",24, "bold")

def miles_to_km():
    mile_input = mile_entry.get()
    try:
        float_mile_input= float(mile_input)
        km= float_mile_input * 1.60934
        km_entry.delete(0,END)
        km_entry.insert(0, f"{km}")
    except ValueError:
        km_entry.delete(0,END)
        km_entry.insert(0,"Wrong")


window = Tk()
window.title("Miles to Kms Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Labels
miles_label = Label(text="Miles",font=FONT)
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to", font=FONT)
is_equal_to_label.grid(column=0, row=1)

KM_label= Label(text="KM", font=FONT)
KM_label.grid(column=2, row=1)

#Entry
mile_entry = Entry(width=12, )
mile_entry.grid(column=1, row=0)
mile_entry.insert(0,"0")

km_entry = Entry(width=12)
km_entry.grid(column=1, row=1)
km_entry.insert(0,"0")

#Button
calculate_button = Button(text="Calculate", width=15, command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()