def test_login_invalid_credentials(driver):
    driver.get("https://buggy.justtestit.org/")
    time.sleep(2)

    wait = WebDriverWait(driver, 30)  

    
    wait_and_type(driver, By.ID, "user", "wronguser", wait, 1)
    wait_and_type(driver, By.ID, "password", "wrongpassword", wait, 1)

    
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
    login_button.click()
    time.sleep(2)

    error_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
    assert "Invalid username/password" in error_message.text

    driver.save_screenshot("screenshots/login_failed.png")
