def test_logout(driver):
    driver.get("https://buggy.justtestit.org/")
    wait = WebDriverWait(driver, 30)  # Aumentamos a 30 segundos

    # Login primero
    username_field = wait.until(EC.visibility_of_element_located((By.ID, "user")))
    password_field = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))

    username_field.send_keys("seleniumuser123")
    password_field.send_keys("Selenium123!")
    login_button.click()

    # Esperamos que el botón de logout esté visible
    logout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout")))
    logout_button.click()

    # Aseguramos que la URL haya cambiado correctamente
    assert driver.current_url == "https://buggy.justtestit.org/"

    driver.save_screenshot("screenshots/logout_success.png")
