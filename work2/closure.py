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
driver.set_window_position(-1920, 0)  # adjust coordinates as needed
driver.maximize_window()

driver.get('https://core.altbetexchange.com/core/#/login/staff')

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

    time.sleep(1)

    # Clicking on the dropdown
    dropdown_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.dropdown-toggle.btn.btn-default.btn-block.filter-dropdown')))
    dropdown_button.click()

    # Clicking on the span with Email text
    email_span = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Email"]')))
    email_span.click()
    #search

    search_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[autofocus="true"]')))
    search_field.click()
    search_field.send_keys(search_term)

    # Wait for the button to be clickable and click it
    success_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-sm.btn-success')))
    success_button.click()

    # Attempt to click on player_link
    player_link = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.player-link')))
    player_link.click()

    search_field = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[autofocus="true"]')))
    search_field.click()
    search_field.send_keys(search_term)

    # Wait for the button to be clickable and click it
    success_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-sm.btn-success')))
    success_button.click()

    player_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.player-link')))
    player_link.click()

    second_div = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//i[contains(@class, "fa fa-question-circle")]/following::div[contains(@class, "ng-star-inserted")][1]')))
    second_div.click()

    email_change = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'profileEmail')))
    email_change.clear()
    email_change.send_keys(search_term)

except NoSuchElementException:
    print("Element not found on the page.")
except TimeoutException:
    print("Timeout while waiting for the elements to load on the page.")

time.sleep(100000)  # wait for 100000 seconds before closing