import os
import sys
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import tkinter as tk
from tkinter import messagebox

# Make sure a command line argument was given
# Make the window full screen and move it to the second monitor
#driver.set_window_position(-1920, 0)  # adjust coordinates as needed
#driver.maximize_window()
#driver.minimize_window()
found_items = [] # Store detected items here

def applyfreespins(driver, search_term, input_text):

    #insert
    search_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[autofocus="true"]')))
    search_field.click()
    search_field.clear()
    search_field.send_keys(search_term)

    # Wait for the button to be clickable and click it
    success_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-sm.btn-success')))
    driver.execute_script("arguments[0].click();", success_button)

    time.sleep(1)

    player_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.player-link')))
    driver.execute_script("arguments[0].click();", player_link)

    time.sleep(2)

    #flag
    span = driver.find_element(By.CSS_SELECTOR, "span.flag-icon")
    img = span.find_element(By.TAG_NAME, "img")
    src = img.get_attribute("src")
    next_element_xpath = "//td[text()='Deposits']/following-sibling::*"
    try:
        WebDriverWait(driver, 2).until(EC.text_to_be_present_in_element((By.XPATH, next_element_xpath), "ZAR0.00"))
    except TimeoutException:
        pass
    next_element = driver.find_element(By.XPATH, next_element_xpath)
    if next_element.text.strip() == "ZAR0.00":
        print("Yes, the currency is ZAR0.00")
    else:
        print("No, the currency is not ZAR0.00")

    first_div = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[text()=' APPLY BONUS ']")))
    first_div.click()

    # Wait for the second div to be clickable and click it
    second_div = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[text()=' Free Round ']")))
    driver.execute_script("arguments[0].click();", second_div)

    time.sleep(2)

    input_element = driver.find_element(By.CSS_SELECTOR, 'input[matinput][required]')
    input_element.click()
    input_element.clear()
    input_element.send_keys(input_text)

    # Wait for the span with class 'mat-select-placeholder ng-tns-c25-40 ng-star-inserted' to be clickable and click it
    span_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Select a subProduct']")))
    driver.execute_script("arguments[0].click();", span_element)

    time.sleep(1)

    if ("assets/flags/ca.svg" in src) or ("assets/flags/no.svg" in src) or ("assets/flags/in.svg" in src):
        option_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//mat-option/span[normalize-space()='Spinomenal']")))
        driver.execute_script("arguments[0].click();", option_element)

        time.sleep(1)

        second_span_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Select a game']")))
        second_span_element.click()

        time.sleep(1)

        # Find all elements that match either selector
        all_elements = driver.find_elements(By.CSS_SELECTOR, 'a.fa.fa-desktop.ng-star-inserted, a.fa.fa-mobile-phone.ng-star-inserted')

        # If there are any matching elements
        if all_elements:
            # Get the first one
            first_element = all_elements[0]

            # Check its classes to determine what it is
            classes = first_element.get_attribute("class").split(' ')
            if 'fa-desktop' in classes:
                option_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//mat-option/span/span[normalize-space()='Book of Tusk Casino']")))
                driver.execute_script("arguments[0].click();", option_element)
            elif ('fa-mobile-phone' in classes) or ([] in classes):
                option_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//mat-option/span/span[normalize-space()='Book of Tusk Casino_Mobile']")))
                driver.execute_script("arguments[0].click();", option_element)

    else:
        option_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//mat-option/span[normalize-space()='Platipus']")))
        driver.execute_script("arguments[0].click();", option_element)

        time.sleep(1)

        second_span_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Select a game']")))
        second_span_element.click()

        time.sleep(1)


        # Find all elements that match either selector
        all_elements = driver.find_elements(By.CSS_SELECTOR, 'a.fa.fa-desktop.ng-star-inserted, a.fa.fa-mobile-phone.ng-star-inserted')
        print(all_elements)
        time.sleep(1)

        # If there are any matching elements
        if all_elements:
            # Get the first one
            first_element = all_elements[0]

            # Check its classes to determine what it is
            classes = first_element.get_attribute("class").split(' ')
            if 'fa-desktop' in classes:
                option_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//mat-option/span/span[normalize-space()='Wild Spin']")))
                driver.execute_script("arguments[0].click();", option_element)
            elif ('fa-mobile-phone' in classes) or ([] in classes):
                option_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//mat-option/span/span[normalize-space()='Wild Spin_Mobile']")))
                driver.execute_script("arguments[0].click();", option_element)



    # Create a root window but immediately hide it, we just want to show messagebox
    root = tk.Tk()
    root.withdraw()

    confirmation = messagebox.askyesno('Confirmation', 'Do you want to navigate to search page?')
    if confirmation == True:
        try:
            i_element = driver.find_element(By.CSS_SELECTOR, "#applyBonusModalHeader h6 button i")
            driver.execute_script("arguments[0].click();", i_element)
        except NoSuchElementException:
            print("i_element not found on webpage")
        driver.get('https://core.altbetexchange.com/core/#/app/core/players/search')
        root.destroy()


    #except NoSuchElementException:
        #print("Element not found on the page.")
    #except TimeoutException:
        #print("Timeout while waiting for the elements to load on the page.")

    pass