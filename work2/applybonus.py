import time
import pyperclip
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
found_items = []  # Store detected items here
def applybonus(driver, search_term, bonus_type):
    try:
        i_element = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#applyBonusModalHeader h6 button i")))
        driver.execute_script("arguments[0].click();", i_element)
        time.sleep(1)
    except TimeoutException:
        print("X not found on page")
    finally:
        driver.get('https://core.altbetexchange.com/core/#/app/core/players/search')
        search_field = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[autofocus="true"]')))
        driver.execute_script("arguments[0].click();", search_field)
        search_field.clear()
        search_field.send_keys(search_term)
        success_button = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-sm.btn-success')))
        driver.execute_script("arguments[0].click();", success_button)
        time.sleep(1)
        player_link = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.player-link')))
        driver.execute_script("arguments[0].click();", player_link)
        time.sleep(3)
        span = driver.find_element(By.CSS_SELECTOR, "span.flag-icon")
        img = span.find_element(By.TAG_NAME, "img")
        src = img.get_attribute("src")
        first_div = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//div[text()=' APPLY BONUS ']")))
        driver.execute_script("arguments[0].click();", first_div)
        second_div = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "//div[text()=' Manual Bonus ']")))
        driver.execute_script("arguments[0].click();", second_div)
        time.sleep(2)
        if bonus_type == "Welcome bonus":
            if ("assets/flags/fi.svg" in src) or ("assets/flags/jp.svg" in src) or ("assets/flags/se.svg" in src):
                input_element = WebDriverWait(driver, 3).until(
                    EC.element_to_be_clickable((By.XPATH, "//input [@formcontrolname='amount']")))
                input_element.clear()
                input_element.send_keys('5')
            else:
                input_element = WebDriverWait(driver, 3).until(
                    EC.element_to_be_clickable((By.XPATH, "//input [@formcontrolname='amount']")))
                input_element.clear()
                input_element.send_keys('9')
            input_element = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//input [@formcontrolname='wagerRequirement']")))
            input_element.clear()
            input_element.send_keys('100')
            input_element = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//input [@formcontrolname='expires']")))
            input_element.clear()
            input_element.send_keys('7')
            input_element = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//textarea [@formcontrolname='comment']")))
            input_element.clear()
            input_element.send_keys('Welcome no deposit bonus')
            element_to_click = driver.find_element(By.XPATH, '//mat-label[text()="Select Transaction Tag"]')
            parent_div = element_to_click.find_element(By.XPATH, '../../..')
            driver.execute_script("arguments[0].click();", parent_div)
            option_element = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//mat-option/span[normalize-space()='Bonus']")))
            driver.execute_script("arguments[0].click();", option_element)
            text_to_copy = "Your bonus has been added to your account. Enjoy!\nAlso I would like to remind you that there is a 125% bonus and up to 100 free spins on your first deposit.\nAnything else I can help you with?"
            pyperclip.copy(text_to_copy)
        elif bonus_type == "Cashback":
            input_element = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//input [@formcontrolname='amount']")))
            input_element.clear()
            input_element = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//input [@formcontrolname='wagerRequirement']")))
            input_element.clear()
            input_element.send_keys('10')
            input_element = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//textarea [@formcontrolname='comment']")))
            input_element.clear()
            input_element.send_keys('cashback')
            element_to_click = driver.find_element(By.XPATH, '//mat-label[text()="Select Transaction Tag"]')
            parent_div = element_to_click.find_element(By.XPATH, '../../..')
            driver.execute_script("arguments[0].click();", parent_div)
            option_element = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//mat-option/span[normalize-space()='CashBack']")))
            driver.execute_script("arguments[0].click();", option_element)
            text_to_copy = "Your cashback has been added to your account. Enjoy!\nAnything else I can help you with?"
            pyperclip.copy(text_to_copy)
        elif bonus_type == "Bonus":
            input_element = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//input [@formcontrolname='amount']")))
            input_element.clear()
            input_element = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//input [@formcontrolname='wagerRequirement']")))
            input_element.clear()
            input_element.send_keys('40')
            input_element = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//textarea [@formcontrolname='comment']")))
            input_element.clear()
            input_element.send_keys('Deposit bonus')
            element_to_click = driver.find_element(By.XPATH, '//mat-label[text()="Select Transaction Tag"]')
            parent_div = element_to_click.find_element(By.XPATH, '../../..')
            driver.execute_script("arguments[0].click();", parent_div)
            option_element = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//mat-option/span[normalize-space()='Bonus']")))
            driver.execute_script("arguments[0].click();", option_element)
            text_to_copy = "Your bonus has been added to your account. Enjoy!\nAnything else I can help you with?"
            pyperclip.copy(text_to_copy)
        elif bonus_type == "SA CALL CENTER":
            input_element = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//input [@formcontrolname='amount']")))
            input_element.clear()
            input_element.send_keys('200')
            input_element = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//input [@formcontrolname='wagerRequirement']")))
            input_element.clear()
            input_element.send_keys('100')
            input_element = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//input [@formcontrolname='expires']")))
            input_element.clear()
            input_element.send_keys('7')
            input_element = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//textarea [@formcontrolname='comment']")))
            input_element.clear()
            input_element.send_keys('SA CALL CENTER')
            element_to_click = driver.find_element(By.XPATH, '//mat-label[text()="Select Transaction Tag"]')
            parent_div = element_to_click.find_element(By.XPATH, '../../..')
            driver.execute_script("arguments[0].click();", parent_div)
            option_element = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//mat-option/span[normalize-space()='Bonus']")))
            driver.execute_script("arguments[0].click();", option_element)
            text_to_copy = "Your bonus has been added to your account. Enjoy!\nAnything else I can help you with?"
            pyperclip.copy(text_to_copy)
    pass
