from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Scenario 1: Successful login with valid credentials
def test_successful_login():
    # Given the user is on the Automation Practice login page
    driver = webdriver.Chrome()
    driver.get("http://automationpractice.pl/index.php?controller=authentication&back=my-account")
    driver.maximize_window()
    
    # When the user enters valid credentials and clicks login
    driver.find_element(By.ID, "email").send_keys("valid_email@example.com")
    driver.find_element(By.ID, "passwd").send_keys("valid_password")
    driver.find_element(By.ID, "SubmitLogin").click()
    time.sleep(3)
    
    # Then the user should be redirected to their account page
    assert "My account" in driver.title, "Login failed for valid credentials"
    
    driver.quit()

# Scenario 2: Login with invalid credentials
def test_invalid_login():
    # Given the user is on the Automation Practice login page
    driver = webdriver.Chrome()
    driver.get("http://automationpractice.pl/index.php?controller=authentication&back=my-account")
    driver.maximize_window()
    
    # When the user enters invalid credentials and clicks login
    driver.find_element(By.ID, "email").send_keys("invalid_email@example.com")
    driver.find_element(By.ID, "passwd").send_keys("invalid_password")
    driver.find_element(By.ID, "SubmitLogin").click()
    time.sleep(3)
    
    # Then an error message should be displayed
    error_message = driver.find_element(By.XPATH, "//div[@class='alert alert-danger']//li").text
    assert "Authentication failed" in error_message, "Expected error message not displayed"
    
    driver.quit()

# Scenario 3: Login with empty fields
def test_empty_fields():
    # Given the user is on the Automation Practice login page
    driver = webdriver.Chrome()
    driver.get("http://automationpractice.pl/index.php?controller=authentication&back=my-account")
    driver.maximize_window()
    
    # When the user leaves both fields empty and clicks login
    driver.find_element(By.ID, "SubmitLogin").click()
    time.sleep(3)
    
    # Then an error message should be displayed
    error_message = driver.find_element(By.XPATH, "//div[@class='alert alert-danger']//li").text
    assert "An email address required" in error_message, "Expected error message not displayed for empty fields"
    
    driver.quit()

# Execute the tests
if __name__ == "__main__":
    test_successful_login()
    test_invalid_login()
    test_empty_fields()
