import time

import pyperclip
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

found_items = []  # Store detected items here

def applyfreespins(driver, search_term, input_text):
    try:
        i_element = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#applyBonusModalHeader h6 button i")))
        driver.execute_script("arguments[0].click();", i_element)
        time.sleep(1)
    except TimeoutException:
        print("X not found on page")
    finally:
        driver.get('https://core.altbetexchange.com/core/#/app/core/players/search')
        search_field = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[autofocus="true"]')))
        search_field.click()
        search_field.clear()
        search_field.send_keys(search_term)
        success_button = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-sm.btn-success')))
        driver.execute_script("arguments[0].click();", success_button)
        time.sleep(2)
        player_link = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.player-link')))
        driver.execute_script("arguments[0].click();", player_link)
        time.sleep(2)
        # flag
        span = driver.find_element(By.CSS_SELECTOR, "span.flag-icon")
        img = span.find_element(By.TAG_NAME, "img")
        src = img.get_attribute("src")
        next_element_xpath = "//td[text()='Deposits']/following-sibling::*"
        try:
            WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element((By.XPATH, next_element_xpath), "ZAR0.00"))
        except TimeoutException:
            pass
        next_element = driver.find_element(By.XPATH, next_element_xpath)
        if next_element.text.strip() == "ZAR0.00":
            print("Yes, the currency is ZAR0.00")
        else:
            print("No, the currency is not ZAR0.00")
        first_div = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//div[text()=' APPLY BONUS ']")))
        driver.execute_script("arguments[0].click();", first_div)
        second_div = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//div[text()=' Free Round ']")))
        driver.execute_script("arguments[0].click();", second_div)
        time.sleep(3)
        input_element = driver.find_element(By.CSS_SELECTOR, 'input[matinput][required]')
        driver.execute_script("arguments[0].click();", input_element)
        input_element.clear()
        input_element.send_keys(input_text)
        span_element = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Select a subProduct']")))
        driver.execute_script("arguments[0].click();", span_element)
        time.sleep(1)
        if ("assets/flags/ca.svg" in src) or ("assets/flags/no.svg" in src) or ("assets/flags/in.svg" in src):
            option_element = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//mat-option/span[normalize-space()='Spinomenal']")))
            driver.execute_script("arguments[0].click();", option_element)
            time.sleep(1)
            second_span_element = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//span[text()='Select a game']")))
            driver.execute_script("arguments[0].click();", second_span_element)
            time.sleep(1)
            all_elements = driver.find_elements(By.CSS_SELECTOR,
                                                'a.fa.fa-desktop.ng-star-inserted, a.fa.fa-mobile-phone.ng-star-inserted')
            if all_elements:
                first_element = all_elements[0]
                classes = first_element.get_attribute("class").split(' ')
                if 'fa-desktop' in classes:
                    option_element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(
                        (By.XPATH, "//mat-option/span/span[normalize-space()='Book of Tusk Casino']")))
                    driver.execute_script("arguments[0].click();", option_element)
                    text_to_copy = "Your free spins are in Book of TuskCasino, good luck!\nAnything else I can help you with?"
                    pyperclip.copy(text_to_copy)
                elif ('fa-mobile-phone' in classes) or ([] in classes):
                    option_element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(
                        (By.XPATH, "//mat-option/span/span[normalize-space()='Book of Tusk Casino_Mobile']")))
                    driver.execute_script("arguments[0].click();", option_element)
                    text_to_copy = "Your free spins are in Book of TuskCasino, good luck!\nAnything else I can help you with?"
                    pyperclip.copy(text_to_copy)
        else:
            option_element = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//mat-option/span[normalize-space()='Platipus']")))
            driver.execute_script("arguments[0].click();", option_element)
            time.sleep(1)
            second_span_element = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//span[text()='Select a game']")))
            driver.execute_script("arguments[0].click();", second_span_element)
            time.sleep(1)
            all_elements = driver.find_elements(By.CSS_SELECTOR,
                                                'a.fa.fa-desktop.ng-star-inserted, a.fa.fa-mobile-phone.ng-star-inserted')
            print(all_elements)
            time.sleep(1)
            if all_elements:
                first_element = all_elements[0]
                classes = first_element.get_attribute("class").split(' ')
                if 'fa-desktop' in classes:
                    option_element = WebDriverWait(driver, 3).until(
                        EC.element_to_be_clickable((By.XPATH, "//mat-option/span/span[normalize-space()='Wild Spin']")))
                    driver.execute_script("arguments[0].click();", option_element)
                    text_to_copy = "Your free spins are in Wild Spin, good luck!\nAnything else I can help you with?"
                    pyperclip.copy(text_to_copy)
                elif ('fa-mobile-phone' in classes) or ([] in classes):
                    option_element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(
                        (By.XPATH, "//mat-option/span/span[normalize-space()='Wild Spin_Mobile']")))
                    driver.execute_script("arguments[0].click();", option_element)
                    text_to_copy = "Your free spins are in Wild Spin, good luck!\nAnything else I can help you with?"
                    pyperclip.copy(text_to_copy)
        pass
