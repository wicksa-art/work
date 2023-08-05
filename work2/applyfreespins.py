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
if len(sys.argv) < 3:
    print("Please provide a search term as a command line argument.")
    sys.exit()

search_term = sys.argv[1]
input_text = sys.argv[2]

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

    #flag
    # Find the element span with the exact class flag-icon
    span = driver.find_element(By.CSS_SELECTOR, "span.flag-icon")

    # Find the element img inside the span
    img = span.find_element(By.TAG_NAME, "img")

    # Get the src attribute of the img
    src = img.get_attribute("src")

    # direct XPath to the next element of deposit_element
    next_element_xpath = "//td[text()='Deposits']/following-sibling::*"

    # Try waiting until the next_element has the text "ZAR0.00"
    try:
        WebDriverWait(driver, 2).until(EC.text_to_be_present_in_element((By.XPATH, next_element_xpath), "ZAR0.00"))
    except TimeoutException:
        pass

    # Then find the next_element and do the comparison
    next_element = driver.find_element(By.XPATH, next_element_xpath)

    if next_element.text.strip() == "ZAR0.00":
        print("Yes, the currency is ZAR0.00")
    else:
        print("No, the currency is not ZAR0.00")

    time.sleep(1)

    # Wait for the first div to be clickable and click it
    first_div = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'mat-tab-label-1-0')))
    first_div.click()

    time.sleep(0.5)

    # Wait for the second div to be clickable and click it
    second_div = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'mat-tab-label-3-2')))
    second_div.click()

    time.sleep(1)

    # Wait for the span with class 'mat-select-placeholder ng-tns-c25-40 ng-star-inserted' to be clickable and click it
    span_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.mat-select-placeholder.ng-tns-c25-40.ng-star-inserted')))
    span_element.click()

    time.sleep(1)

    # Wait for the span with class 'mat-select-placeholder ng-tns-c25-40 ng-star-inserted' to be clickable and click it
    span_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.mat-select-placeholder.ng-tns-c25-40.ng-star-inserted')))
    driver.execute_script("arguments[0].click();", span_element)

    time.sleep(1)

    if ("assets/flags/ca.svg" in src) or ("assets/flags/no.svg" in src) or ("assets/flags/in.svg" in src):
        option_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//mat-option/span[normalize-space()='Spinomenal']")))
        driver.execute_script("arguments[0].click();", option_element)

        time.sleep(1)

        second_span_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.mat-select-placeholder.ng-tns-c25-42.ng-star-inserted')))
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

        input_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'mat-input-2')))
        input_element.clear()
        input_element.send_keys(input_text)

    else:
        option_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//mat-option/span[normalize-space()='Platipus']")))
        driver.execute_script("arguments[0].click();", option_element)

        time.sleep(1)

        second_span_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.mat-select-placeholder.ng-tns-c25-42.ng-star-inserted')))
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

        input_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'mat-input-2')))
        input_element.clear()
        input_element.send_keys(input_text)

except NoSuchElementException:
    print("Element not found on the page.")
except TimeoutException:
    print("Timeout while waiting for the elements to load on the page.")

time.sleep(60)  # wait for 100000 seconds before closing

driver.quit()