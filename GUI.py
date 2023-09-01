import tkinter as tk

import subprocess
import threading
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import ttk
from work2 import applyfreespins
from work2 import applybonus
from work2 import verifyaccount
from work2 import closure

def on_button_click(button_name):
    message = ""
    if button_name == "Apply Bonus":
        term_window = tk.Toplevel(root)
        term_window.title("Enter Search Term")
        term_label = tk.Label(term_window, text="Enter username:")
        term_label.grid(row=0, column=0, columnspan=2)
        search_entry = tk.Entry(term_window)
        search_entry.grid(row=1, column=0, columnspan=2)
        # Add a label for the new dropdown list
        bonus_label = tk.Label(term_window, text="Select bonus type:")
        bonus_label.grid(row=2, column=0, columnspan=2)

        # Add a dropdown list with bonus options
        bonus_options = ["Welcome bonus", "Cashback", "Bonus", "SA CALL CENTER"]
        bonus_combobox = ttk.Combobox(term_window, values=bonus_options)
        bonus_combobox.grid(row=3, column=0, columnspan=2)

        def on_ok_click():
            if not search_entry.get():
                return
            search_term = search_entry.get()
            bonus_type = bonus_combobox.get()  # Get the selected bonus type
            term_window.destroy()
            try:
                subprocess.Popen(["python", "work2/applybonus.py", search_term, bonus_type], shell=True)
                thread = threading.Thread(target=applybonus.applybonus, args=(driver, search_term, bonus_type))
                thread.start()
                message = "Press Apply to proceed!"
            except FileNotFoundError:
                message = "Error: applybonus.py not found in work2 folder."
            label.config(text=message)
        ok_button = tk.Button(term_window, text="OK", command=on_ok_click)
        ok_button.grid(row=4, column=0, columnspan=2)
        search_entry.bind('<Return>', lambda event: on_ok_click())
        search_entry.focus_set()

    elif button_name == "Apply Free Spins":
        term_window = tk.Toplevel(root)
        term_window.title("Enter Free Spins Details")
        term_label1 = tk.Label(term_window, text="Enter username:")
        term_label1.grid(row=0, column=0)
        spins_entry1 = tk.Entry(term_window)
        spins_entry1.grid(row=0, column=1)
        term_label2 = tk.Label(term_window, text="Enter amount:")
        term_label2.grid(row=1, column=0)
        spins_entry2 = tk.Entry(term_window)
        spins_entry2.grid(row=1, column=1)
        def on_ok_click():
            search_term = spins_entry1.get()
            input_text = spins_entry2.get()
            if not search_term or not input_text:
                return
            term_window.destroy()
            try:
                subprocess.Popen(["python", "work2/applyfreespins.py", search_term, input_text], shell=True)
                thread = threading.Thread(target=applyfreespins.applyfreespins, args=(driver, search_term, input_text))
                thread.start()
                message = "Press Apply to proceed!"
            except FileNotFoundError:
                message = "Error: applyfreespins.py not found in work2 folder."
            label.config(text=message)
        ok_button = tk.Button(term_window, text="OK", command=on_ok_click)
        ok_button.grid(row=2, column=0, columnspan=2)
        spins_entry1.bind('<Return>', lambda event: on_ok_click())
        spins_entry2.bind('<Return>', lambda event: on_ok_click())
        spins_entry1.focus_set()
    elif button_name == "Verify Account":
        term_window = tk.Toplevel(root)
        term_window.title("Enter Account Details")
        term_label1 = tk.Label(term_window, text="Enter username:")
        term_label1.grid(row=0, column=0)
        search_entry = tk.Entry(term_window)
        search_entry.grid(row=0, column=1)
        term_label2 = tk.Label(term_window, text="Enter email:")
        term_label2.grid(row=1, column=0)
        email_entry = tk.Entry(term_window)
        email_entry.grid(row=1, column=1)
        # Add a label for the new dropdown list
        verify_label = tk.Label(term_window, text="Select verify type:")
        verify_label.grid(row=2, column=0, columnspan=2)

        # Add a dropdown list with bonus options
        verify_options = ["Change email", "Send email"]
        verify_combobox = ttk.Combobox(term_window, values=verify_options)
        verify_combobox.grid(row=3, column=0, columnspan=2)
        def on_ok_click():
            search_term = search_entry.get()
            email_term = email_entry.get()
            verify_type = verify_combobox.get()  # Get the selected bonus type
            if not email_term or not search_term:
                return
            term_window.destroy()
            try:
                subprocess.Popen(["python", "work2/verifyaccount.py", search_term, email_term, verify_type], shell=True)
                thread = threading.Thread(target=verifyaccount.verifyaccount, args=(driver, search_term, email_term, verify_type))
                thread.start()
                message = "Check answer and proceed!"
            except FileNotFoundError:
                message = "Error: verifyaccount.py not found in work2 folder."
            label.config(text=message)
        ok_button = tk.Button(term_window, text="OK", command=on_ok_click)
        ok_button.grid(row=4, column=0, columnspan=2)
        search_entry.bind('<Return>', lambda event: on_ok_click())
        email_entry.bind('<Return>', lambda event: on_ok_click())
        search_entry.focus_set()
    elif button_name == "Closure":
        term_window = tk.Toplevel(root)
        term_window.title("Enter Search Term")
        term_label = tk.Label(term_window, text="Enter username:")
        term_label.grid(row=0, column=0, columnspan=2)
        search_entry = tk.Entry(term_window)
        search_entry.grid(row=1, column=0, columnspan=2)
        # Add a label for the new dropdown list
        closure_label = tk.Label(term_window, text="Select closure type:")
        closure_label.grid(row=2, column=0, columnspan=2)

        # Add a dropdown list with bonus options
        closure_options = ["Closure", "Gambling addiction"]
        closure_combobox = ttk.Combobox(term_window, values=closure_options)
        closure_combobox.grid(row=3, column=0, columnspan=2)
        def on_ok_click():
            if not search_entry.get():
                return
            search_term = search_entry.get()
            closure_type = closure_combobox.get()  # Get the selected bonus type
            term_window.destroy()
            try:
                subprocess.Popen(["python", "work2/closure.py", search_term, closure_type], shell=True)
                thread = threading.Thread(target=closure.closure, args=(driver, search_term, closure_type))
                thread.start()
                message = "Press Apply to proceed!"
            except FileNotFoundError:
                message = "Error: closure.py not found in work2 folder."
            label.config(text=message)
        ok_button = tk.Button(term_window, text="OK", command=on_ok_click)
        ok_button.grid(row=4, column=0, columnspan=2)
        search_entry.bind('<Return>', lambda event: on_ok_click())
        search_entry.focus_set()
root = tk.Tk()
root.title("User Input App")
root.geometry("400x200")
buttons = ["Apply Bonus", "Apply Free Spins", "Verify Account", "Closure"]
for button_name in buttons:
    button = tk.Button(root, text=button_name, command=lambda name=button_name: on_button_click(name))
    button.pack()
options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
service = Service(r'C:\\Users\\kleym\\Documents\\GitHub\\scripts\\chromedriver-win32\\chromedriver.exe')
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://core.altbetexchange.com/core/#/login/staff')
username_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'username')))
username_field.send_keys('peterk')
password_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'password')))
password_field.send_keys('kfH693FpX9c9')
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.login-button.ng-tns-c1-0.ng-star-inserted')))
driver.execute_script("arguments[0].click();", login_button)
new_player_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-target="#sidebar-player-new"]')))
driver.execute_script("arguments[0].click();", new_player_link)
search_player_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[routerlink="/app/core/players/search"]')))
driver.execute_script("arguments[0].click();", search_player_link)
dropdown_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Contains") and contains(@class, "dropdown-toggle") and contains(@class, "btn") and contains(@class, "btn-default") and contains(@class, "btn-block") and contains(@class, "filter-dropdown")]')))
driver.execute_script("arguments[0].click();", dropdown_button)
email_span = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Equals"]')))
driver.execute_script("arguments[0].click();", email_span)
label = tk.Label(root, text="")
label.pack()
root.mainloop()