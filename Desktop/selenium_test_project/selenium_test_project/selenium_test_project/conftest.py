import pytest
from selenium import webdriver
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    time.sleep(5)  # Espera 5 segundos antes de cerrar el navegador
    driver.quit()

