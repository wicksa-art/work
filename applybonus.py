import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Make sure a command line argument was given
if len(sys.argv) < 3:
    print("Please provide a search term as a command line argument.")
    sys.exit()

search_term = sys.argv[1]
input_text = sys.argv[2]

service = Service(r'C:\Users\kleym\Downloads\chromedriver_win32\chromedriver.exe')

driver = webdriver.Chrome(service=service)

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

    # Wait for the first div to be clickable and click it
    first_div = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'mat-tab-label-1-0')))
    first_div.click()

    # Wait for the second div to be clickable and click it
    second_div = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.ID, 'mat-tab-label-3-2')))
    second_div.click()
	
    time.sleep(1)

    # Wait for the span with class 'mat-select-placeholder ng-tns-c25-40 ng-star-inserted' to be clickable and click it
    span_element = WebDriverWait(driver, 240).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.mat-select-placeholder.ng-tns-c25-40.ng-star-inserted')))
    span_element.click()

    # Wait for the span with class 'mat-select-placeholder ng-tns-c25-40 ng-star-inserted' to be clickable and click it
    span_element = WebDriverWait(driver, 240).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.mat-select-placeholder.ng-tns-c25-40.ng-star-inserted')))
    driver.execute_script("arguments[0].click();", span_element)

    # After clicking the span element, the mat-options should be visible. 
    # Wait for the mat-option with id 'mat-option-58' to be clickable, and then click it
    option_element = WebDriverWait(driver, 240).until(EC.element_to_be_clickable((By.XPATH, "//mat-option/span[normalize-space()='Platipus']")))
    driver.execute_script("arguments[0].click();", option_element)

    time.sleep(1)

    second_span_element = WebDriverWait(driver, 240).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.mat-select-placeholder.ng-tns-c25-42.ng-star-inserted')))
    second_span_element.click()

    time.sleep(1)

    option_element = WebDriverWait(driver, 240).until(EC.element_to_be_clickable((By.XPATH, "//mat-option/span/span[normalize-space()='Wild Spin_Mobile']")))
    driver.execute_script("arguments[0].click();", option_element)

    input_element = WebDriverWait(driver, 240).until(EC.element_to_be_clickable((By.ID, 'mat-input-2')))
    input_element.clear()
    input_element.send_keys(input_text)

except NoSuchElementException:
    print("Element not found on the page.")
except TimeoutException:
    print("Timeout while waiting for the elements to load on the page.")

time.sleep(100000)  # wait for 100000 seconds before closing
