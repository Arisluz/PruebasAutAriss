from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random


def wait_and_type(driver, by, value, text, wait, pause=1):
    element = wait.until(EC.visibility_of_element_located((by, value)))
    element.send_keys(text)
    time.sleep(pause)

def test_register_user(driver):
    driver.get("https://buggy.justtestit.org/")
    time.sleep(1.5) 

    driver.find_element(By.LINK_TEXT, "Register").click()
    time.sleep(2)  

    wait = WebDriverWait(driver, 15)  
    username = f"user{random.randint(1000,9999)}"
    email = f"{username}@test.com"
    password = "Test1234!"

    wait_and_type(driver, By.ID, "username", username, wait, 1)
    wait_and_type(driver, By.ID, "firstName", "Test", wait, 1)
    wait_and_type(driver, By.ID, "lastName", "User", wait, 1)
    wait_and_type(driver, By.ID, "password", password, wait, 1)
    wait_and_type(driver, By.ID, "confirmPassword", password, wait, 1)

    driver.find_element(By.XPATH, '//button[text()="Register"]').click()
    time.sleep(2)  

    
    success_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
    assert "Registration is successful" in success_message.text

    driver.save_screenshot(f"screenshots/register_success_{username}.png")
