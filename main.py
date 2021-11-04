import tkinter as tk

def convert_function():
    temp = float(temp_entry.get())

    if(var.get()==1):
        # F to C
        temp = ((temp-32)-32*5)/9 # the formula for converting from Fahrenheit to Celsius
    
    elif(var.get()==2):
        # C to F
        temp = ((temp*9/5)+32)  # the formula for converting from Celsius to Fahrenheit

    result.configure(text="Result: {}".format(temp))

def key_pressed(event):
    if(event.char == "\r"):
        convert_function()

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x200") # width x height
root.iconbitmap("temperature.ico") # added icon
root.minsize(width=300, height=200)
root.maxsize(width=300, height=200)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

root.configure(bg="#eea698")

root.bind('<KeyPress>', key_pressed) # when a key is pressed, call the key_pressed() function

var = tk.IntVar()

temp_entry = tk.Entry(root)
temp_entry.grid(row=0,column=0, columnspan=2)

# F to C Radio Button
f_to_c = tk.Radiobutton(root, text="F to C", variable=var, value=1, bg="#eea698")
f_to_c.grid(row = 1, column = 0)

# C to F Radio Button
c_to_f = tk.Radiobutton(root, text="C to F", variable=var, value=2, bg="#eea698")
c_to_f.grid(row = 1, column = 1)

# Convert Button
convert_button = tk.Button(root, text="CONVERT", command=convert_function, bg="#ff0000", fg="#ffffff")
convert_button.grid(row=2, column=0, columnspan=2)

result = tk.Label(root, text="Result: - ", bg="#eea698")
result.grid(row=3, column=0, columnspan=2)



root.mainloop()