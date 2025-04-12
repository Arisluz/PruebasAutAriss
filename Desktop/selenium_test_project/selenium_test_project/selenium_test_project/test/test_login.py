def test_login_success(driver):
    driver.get("https://buggy.justtestit.org/")
    wait = WebDriverWait(driver, 30)  

   
    username_field = wait.until(EC.visibility_of_element_located((By.ID, "user")))
    password_field = wait.until(EC.visibility_of_element_located((By.ID, "password"))) 
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))  

    username_field.send_keys("seleniumuser123")
    password_field.send_keys("Selenium123!")
    login_button.click()

    
    welcome_message = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[text()='Welcome']")))
    assert welcome_message.is_displayed(), "El login no fue exitoso"

    driver.save_screenshot("screenshots/login_success.png")
