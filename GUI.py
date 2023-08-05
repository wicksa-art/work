import tkinter as tk
import subprocess

def on_button_click(button_name):
    message = ""
    if button_name == "Apply Bonus":
        # Create a new window to get the search term from the user
        term_window = tk.Toplevel(root)
        term_window.title("Enter Search Term")

        # Entry widget to get the search term
        term_label = tk.Label(term_window, text="Enter the search term:")
        term_label.pack()
        search_entry = tk.Entry(term_window)
        search_entry.pack()

        # Function to handle the OK button click in the new window
        def on_ok_click():
            if not search_entry.get():
                return  # Do nothing if the search term is empty

            search_term = search_entry.get()
            term_window.destroy()

            try:
                # Run the applybonus.py script from work2 folder with the provided search term as an argument
                process = subprocess.Popen(["python", "work2/applybonus.py", search_term],
                                           stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                stdout, stderr = process.communicate()

                if stdout:
                    message = "Bonus applied successfully!"
                else:
                    message = "Error: applybonus.py encountered an issue."

            except FileNotFoundError:
                message = "Error: applybonus.py not found in work2 folder."

            label.config(text=message)

        # Bind the Enter key press event to the on_ok_click function
        search_entry.bind('<Return>', lambda event: on_ok_click())

        # Set the focus on the input field
        search_entry.focus_set()

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
