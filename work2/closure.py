import time
import pyperclip
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import tkinter as tk
from tkinter import messagebox

def closure(driver, search_term, closure_type):
    try:
        i_element = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#applyBonusModalHeader h6 button i")))
        driver.execute_script("arguments[0].click();", i_element)
        time.sleep(1)
    except TimeoutException:
        print("X not found on page")
    finally:
        driver.get('https://core.altbetexchange.com/core/#/app/core/players/search')
        search_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[autofocus="true"]')))
        driver.execute_script("arguments[0].click();", search_field)
        search_field.clear()
        search_field.send_keys(search_term)
        success_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-sm.btn-success')))
        driver.execute_script("arguments[0].click();", success_button)
        time.sleep(1)
        player_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.player-link')))
        driver.execute_script("arguments[0].click();", player_link)
        time.sleep(3)
        elementi = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.fa.fa-pencil-square-o.ng-star-inserted')))
        driver.execute_script("arguments[0].click();", elementi)
        dropdownbutton = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-secondary.filter-dropdown')))
        driver.execute_script("arguments[0].click();", dropdownbutton)
        locka = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//a[text()="Permanent Lock"]')))
        driver.execute_script("arguments[0].click();", locka)
        buttons = driver.find_elements(By.CLASS_NAME, "btn.btn-secondary.filter-dropdown")
        if len(buttons) >= 2:
            second_button = buttons[1]  # Second button
            driver.execute_script("arguments[0].click();", second_button)
        else:
            print("There are not enough buttons with the specified class.")
        lockr = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//a[text()=" Customer Request (CUSTOMER_REQUEST) "]')))
        driver.execute_script("arguments[0].click();", lockr)
        reasontext = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'changeLockStatusComment')))
        driver.execute_script("arguments[0].click();", reasontext)
        if closure_type == "Closure":
            reasontext.send_keys("Account closure request")
        elif closure_type == "Gambling addiction":
            reasontext.send_keys("Account closure request, gambling addiction")
        text_to_copy = "Your account is closed\nHave a great day!"
        pyperclip.copy(text_to_copy)
        pass
