import tkinter as tk


class resolution:
    def __init__(self,val) -> None:
        self.__val=val
    def getval(self):
        return self.__val
    def setval(self,val):
        self.__val=val;



def getResolution(resolution:resolution):
    root = tk.Tk()
    root.geometry("300x200") 
    # Define function to retrieve selected value from dropdown
    def select_value(value):
        # Do something with the selected integer value here
        resolution.setval(value)
        print(f"The selected value is {value}")

    def ok_button_pressed():
        root.destroy() 


    # Create label and dropdown widget
    label = tk.Label(root, text="Select Resolution:",font=('Arial', 14))
    label.pack()
    options = list(range(10,101,10))
    default_value = tk.StringVar(value=options[-1])

    dropdown = tk.OptionMenu(root, default_value, *options, command=select_value)
    dropdown.config(width=10,font=('Arial', 14)) # Set the width of the dropdown button
    dropdown.pack()

    ok_button = tk.Button(root,width=10, text="OK", command=ok_button_pressed, bg="green", fg="white", font=('Arial', 12), padx=10, pady=5)
    ok_button.pack(pady=20)
    ok_button.pack()

    root.mainloop()


res=resolution(10)
getResolution(res)
print(f"The final resolution is {res.getval()}")
