import tkinter as tk
import subprocess

def on_button_click(button_name):
    message = ""
    if button_name == "Apply Bonus":
        # Create a new window to get the search term from the user
        term_window = tk.Toplevel(root)
        term_window.title("Enter Search Term")

        # Entry widget to get the search term
        term_label = tk.Label(term_window, text="Enter username:")
        term_label.grid(row=0, column=0, columnspan=2)
        search_entry = tk.Entry(term_window)
        search_entry.grid(row=1, column=0, columnspan=2)

        # Function to handle the OK button click in the new window
        def on_ok_click():
            if not search_entry.get():
                return  # Do nothing if the search term is empty

            search_term = search_entry.get()
            term_window.destroy()

            try:
                # Run the applybonus.py script from work2 folder with the provided search term as an argument
                subprocess.Popen(["python", "work2/applybonus.py", search_term], shell=True)
                message = "Press Apply to proceed!"

            except FileNotFoundError:
                message = "Error: applybonus.py not found in work2 folder."

            label.config(text=message)

        ok_button = tk.Button(term_window, text="OK", command=on_ok_click)
        ok_button.grid(row=2, column=0, columnspan=2)

        # Bind the Enter key press event to the on_ok_click function
        search_entry.bind('<Return>', lambda event: on_ok_click())

        # Set the focus on the input field
        search_entry.focus_set()

    elif button_name == "Apply Free Spins":
        # Create a new window to get the free spins details from the user
        term_window = tk.Toplevel(root)
        term_window.title("Enter Free Spins Details")

        # Entry widgets to get the free spins details
        term_label1 = tk.Label(term_window, text="Enter username:")
        term_label1.grid(row=0, column=0)
        spins_entry1 = tk.Entry(term_window)
        spins_entry1.grid(row=0, column=1)

        term_label2 = tk.Label(term_window, text="Enter amount:")
        term_label2.grid(row=1, column=0)
        spins_entry2 = tk.Entry(term_window)
        spins_entry2.grid(row=1, column=1)

        # Function to handle the OK button click in the new window
        def on_ok_click():
            search_term = spins_entry1.get()
            input_text = spins_entry2.get()

            if not search_term or not input_text:
                return  # Do nothing if any detail is empty

            term_window.destroy()

            try:
                # Run the applyfreespins.py script from work2 folder with the provided details as arguments
                subprocess.Popen(["python", "work2/applyfreespins.py", search_term, input_text], shell=True)
                message = "Press Apply to proceed!"

            except FileNotFoundError:
                message = "Error: applyfreespins.py not found in work2 folder."

            label.config(text=message)

        ok_button = tk.Button(term_window, text="OK", command=on_ok_click)
        ok_button.grid(row=2, column=0, columnspan=2)

        # Bind the Enter key press event to the on_ok_click function
        spins_entry1.bind('<Return>', lambda event: on_ok_click())
        spins_entry2.bind('<Return>', lambda event: on_ok_click())

        # Set the focus on the first input field
        spins_entry1.focus_set()

    elif button_name == "Verify Account":
        # Create a new window to get the account details from the user
        term_window = tk.Toplevel(root)
        term_window.title("Enter Account Details")

        # Entry widgets to get the account details
        term_label1 = tk.Label(term_window, text="Enter email:")
        term_label1.grid(row=0, column=0)
        email_entry = tk.Entry(term_window)
        email_entry.grid(row=0, column=1)

        term_label2 = tk.Label(term_window, text="Enter username:")
        term_label2.grid(row=1, column=0)
        search_entry = tk.Entry(term_window)
        search_entry.grid(row=1, column=1)

        # Function to handle the OK button click in the new window
        def on_ok_click():
            email_term = email_entry.get()
            search_term = search_entry.get()

            if not email_term or not search_term:
                return  # Do nothing if any detail is empty

            term_window.destroy()

            try:
                # Run the verifyaccount.py script from work2 folder with the provided details as arguments
                subprocess.Popen(["python", "work2/verifyaccount.py", email_term, search_term], shell=True)
                message = "Check answer and proceed!"

            except FileNotFoundError:
                message = "Error: verifyaccount.py not found in work2 folder."

            label.config(text=message)

        ok_button = tk.Button(term_window, text="OK", command=on_ok_click)
        ok_button.grid(row=2, column=0, columnspan=2)

        # Bind the Enter key press event to the on_ok_click function
        email_entry.bind('<Return>', lambda event: on_ok_click())
        search_entry.bind('<Return>', lambda event: on_ok_click())

        # Set the focus on the first input field
        email_entry.focus_set()

root = tk.Tk()
root.title("User Input App")
root.geometry("400x200")

# Create and place buttons
buttons = ["Apply Bonus", "Apply Free Spins", "Verify Account", "Closure"]
for button_name in buttons:
    button = tk.Button(root, text=button_name, command=lambda name=button_name: on_button_click(name))
    button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()
