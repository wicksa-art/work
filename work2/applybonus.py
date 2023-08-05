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

# Make sure a command line argument was given
if len(sys.argv) < 2:
    print("Please provide a search term as a command line argument.")
    sys.exit()

search_term = sys.argv[1]

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

service = Service(r'C:\\Users\\kleym\\Downloads\\chromedriver_win32\\chromedriver.exe')

driver = webdriver.Chrome(service=service, options=options)

# Make the window full screen and move it to the second monitor
#driver.set_window_position(-1920, 0)  # adjust coordinates as needed
#driver.maximize_window()
#driver.minimize_window()


driver.get('https://core.altbetexchange.com/core/#/login/staff')

found_items = [] # Store detected items here

try:
    username_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'username')))
    username_field.send_keys('peterk')

    password_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'password')))
    password_field.send_keys('kfH693FpX9c9')

    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.login-button.ng-tns-c1-0.ng-star-inserted')))
    login_button.click()

    new_player_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-target="#sidebar-player-new"]')))
    new_player_link.click()

    search_player_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[routerlink="/app/core/players/search"]')))
    search_player_link.click()

    #insert
    # Clicking on the dropdown
    dropdown_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Contains") and contains(@class, "dropdown-toggle") and contains(@class, "btn") and contains(@class, "btn-default") and contains(@class, "btn-block") and contains(@class, "filter-dropdown")]')))
    dropdown_button.click()

    # Clicking on the span with Email text
    email_span = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Equals"]')))
    email_span.click()

    # Wait for the input field to be clickable, enter the search term into it
    search_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[autofocus="true"]')))   
    search_field.click()
    search_field.send_keys(search_term)
    
    # Wait for the button to be clickable and click it
    success_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-sm.btn-success')))
    success_button.click()

    # Wait for the player link to be clickable and click it
    player_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.player-link')))
    player_link.click()

    time.sleep(1)

    # Wait for the first div to be clickable and click it
    first_div = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'mat-tab-label-1-0')))
    first_div.click()

    # Wait for the second div to be clickable and click it
    second_div = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.ID, 'mat-tab-label-3-1')))
    second_div.click()

    time.sleep(1)

    # Find the element span with the exact class flag-icon
    span = driver.find_element(By.CSS_SELECTOR, "span.flag-icon")

    # Find the element img inside the span
    img = span.find_element(By.TAG_NAME, "img")

    # Get the src attribute of the img
    src = img.get_attribute("src")

    # Check if the src contains "assets/flags/fi.svg"
    if ("assets/flags/fi.svg" in src) or ("assets/flags/jp.svg" in src):
        input_element = WebDriverWait(driver, 240).until(EC.element_to_be_clickable((By.ID, 'mat-input-2')))
        input_element.clear()
        input_element.send_keys('5')
    else:
        input_element = WebDriverWait(driver, 240).until(EC.element_to_be_clickable((By.ID, 'mat-input-2')))
        input_element.clear()
        input_element.send_keys('9')

    input_element = WebDriverWait(driver, 240).until(EC.element_to_be_clickable((By.ID, 'mat-input-3')))
    input_element.clear()
    input_element.send_keys('100')

    input_element = WebDriverWait(driver, 240).until(EC.element_to_be_clickable((By.ID, 'mat-input-4')))
    input_element.clear()
    input_element.send_keys('7')

    input_element = WebDriverWait(driver, 240).until(EC.element_to_be_clickable((By.ID, 'mat-input-6')))
    input_element.clear()
    input_element.send_keys('Welcome no deposit bonus')

    first_mat = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.ID, 'mat-select-3')))
    first_mat.click()

    option_element = WebDriverWait(driver, 240).until(EC.element_to_be_clickable((By.XPATH, "//mat-option/span[normalize-space()='Bonus']")))
    driver.execute_script("arguments[0].click();", option_element)

except NoSuchElementException:
    print("Element not found on the page.")
except TimeoutException:
    print("Timeout while waiting for the elements to load on the page.")

time.sleep(60)  # wait for 100000 seconds before closing