import time
import pyperclip
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
found_items = []  # Store detected items here
def applybonus(driver, search_term):
    try:
        i_element = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#applyBonusModalHeader h6 button i")))
        driver.execute_script("arguments[0].click();", i_element)
        time.sleep(1)
    except TimeoutException:
        driver.get('https://core.altbetexchange.com/core/#/app/core/players/search')
        search_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[autofocus="true"]')))
        search_field.click()
        search_field.clear()
        search_field.send_keys(search_term)
        success_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-sm.btn-success')))
        success_button.click()
        time.sleep(2)
        player_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.player-link')))
        player_link.click()
        time.sleep(3)
        span = driver.find_element(By.CSS_SELECTOR, "span.flag-icon")
        img = span.find_element(By.TAG_NAME, "img")
        src = img.get_attribute("src")
        first_div = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[text()=' APPLY BONUS ']")))
        first_div.click()
        second_div = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[text()=' Manual Bonus ']")))
        driver.execute_script("arguments[0].click();", second_div)
        time.sleep(2)
        if ("assets/flags/fi.svg" in src) or ("assets/flags/jp.svg" in src) or ("assets/flags/se.svg" in src):
            input_element = WebDriverWait(driver, 240).until(
                EC.element_to_be_clickable((By.XPATH, "//input [@formcontrolname='amount']")))
            input_element.clear()
            input_element.send_keys('5')
        else:
            input_element = WebDriverWait(driver, 240).until(
                EC.element_to_be_clickable((By.XPATH, "//input [@formcontrolname='amount']")))
            input_element.clear()
            input_element.send_keys('9')
        input_element = WebDriverWait(driver, 240).until(
            EC.element_to_be_clickable((By.XPATH, "//input [@formcontrolname='wagerRequirement']")))
        input_element.clear()
        input_element.send_keys('100')
        input_element = WebDriverWait(driver, 240).until(
            EC.element_to_be_clickable((By.XPATH, "//input [@formcontrolname='expires']")))
        input_element.clear()
        input_element.send_keys('7')
        input_element = WebDriverWait(driver, 240).until(
            EC.element_to_be_clickable((By.XPATH, "//textarea [@formcontrolname='comment']")))
        input_element.clear()
        input_element.send_keys('Welcome no deposit bonus')
        element_to_click = driver.find_element(By.XPATH, '//mat-label[text()="Select Transaction Tag"]')
        parent_div = element_to_click.find_element(By.XPATH, '../../..')
        parent_div.click()
        option_element = WebDriverWait(driver, 240).until(
            EC.element_to_be_clickable((By.XPATH, "//mat-option/span[normalize-space()='Bonus']")))
        driver.execute_script("arguments[0].click();", option_element)
        text_to_copy = "Your bonus has been added to your account. Enjoy!\nAlso I would like to remind you that there is a 125% bonus and up to 100 free spins on your first deposit.\nAnything else I can help you with?"
        pyperclip.copy(text_to_copy)
        pass
