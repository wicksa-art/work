import time
import pyperclip
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import tkinter as tk
from tkinter import messagebox

def closure(driver, search_term):
    try:
        i_element = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#applyBonusModalHeader h6 button i")))
        driver.execute_script("arguments[0].click();", i_element)
        time.sleep(1)
    except TimeoutException:
        driver.get('https://core.altbetexchange.com/core/#/app/core/players/search')
        search_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[autofocus="true"]')))
        search_field.click()
        search_field.clear()
        search_field.send_keys(search_term)
        success_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-sm.btn-success')))
        success_button.click()
        time.sleep(1)
        player_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.player-link')))
        player_link.click()
        time.sleep(2)
        elementi = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.fa.fa-pencil-square-o.ng-star-inserted')))
        elementi.click()
        dropdownbutton = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-secondary.filter-dropdown')))
        dropdownbutton.click()
        locka = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//a[text()="Permanent Lock"]')))
        locka.click()
        buttons = driver.find_elements(By.CLASS_NAME, "btn.btn-secondary.filter-dropdown")
        if len(buttons) >= 2:
            second_button = buttons[1]  # Second button
            second_button.click()
        else:
            print("There are not enough buttons with the specified class.")
        lockr = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//a[text()=" Customer Request (CUSTOMER_REQUEST) "]')))
        lockr.click()
        reasontext = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'changeLockStatusComment')))
        reasontext.click()
        reasontext.send_keys("Account closure request")
        text_to_copy = "Your account is closed\nHave a great day!"
        pyperclip.copy(text_to_copy)
        pass
