import time
import pyperclip
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import tkinter as tk
from tkinter import messagebox

def verifyaccount(driver, email_term, search_term):
    try:
        i_element = WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#applyBonusModalHeader h6 button i")))
        driver.execute_script("arguments[0].click();", i_element)
    except TimeoutException:
        driver.get('https://core.altbetexchange.com/core/#/app/core/players/search')
        search_player_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[routerlink="/app/core/players/search"]')))
        search_player_link.click()
        time.sleep(1)
        dropdown_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.dropdown-toggle.btn.btn-default.btn-block.filter-dropdown')))
        dropdown_button.click()
        email_span = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Email"]')))
        email_span.click()
        search_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[autofocus="true"]')))
        search_field.click()
        search_field.clear()
        search_field.send_keys(email_term)
        success_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-sm.btn-success')))
        success_button.click()
        time.sleep(1)
        player_link = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.player-link')))
        player_link.click()
    except (NoSuchElementException, TimeoutException):
        dropdown_button = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.dropdown-toggle.btn.btn-default.btn-block.filter-dropdown')))
        dropdown_button.click()
        email_span = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="User Id"]')))
        email_span.click()
        time.sleep(1)
        search_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[autofocus="true"]')))
        search_field.click()
        search_field.clear()
        search_field.send_keys(search_term)
        # Wait for the button to be clickable and click it
        success_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-sm.btn-success')))
        success_button.click()
        time.sleep(1)
        player_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.player-link')))
        player_link.click()

    first_div = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'mat-tab-label-2-9')))
    first_div.click()
    second_div = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//i[contains(@class, "fa fa-question-circle")]/following::div[contains(@class, "ng-star-inserted")][1]')))
    second_div.click()
    email_change = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'profileEmail')))
    email_change.clear()
    email_change.send_keys(email_term)
    text_to_copy = "Done, I've sent you another activation email, make sure to check junk/spam folder\nAlso I would like to remind you that there is a 125% bonus and up to 100 free spins on your first deposit\nAnything else I can help you with?"
    pyperclip.copy(text_to_copy)
    pass