import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class OrangeHRMProject:

    def test(self):
        # Open browser
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver, 10)  # Explicit wait defined here

        baseurl = (
            "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        )
        driver.get(baseurl)
        driver.maximize_window()

        # --- STEP 1: VALID LOGIN & LOGOUT ---
        # Username
        wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
        # Password
        driver.find_element(By.NAME, "password").send_keys("admin123")
        # Click Login
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        print("The user is logged in successfully")

        # Click Logout
        wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']",
                )
            )
        ).click()
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[@href='/web/index.php/auth/logout']")
            )
        ).click()
        print("Logged out successfully")

        # --- STEP 2: INVALID LOGIN ---
        wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("invalidpassword")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # Verify Error Message
        invalid_msg = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//p[text()='Invalid credentials']")
            )
        ).text
        print(f"Error Message Displayed: {invalid_msg}")

        # --- STEP 3: ADD EMPLOYEE ---
        driver.refresh()  # Refresh to clear invalid login state
        wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # Click PIM
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[@href='/web/index.php/pim/viewPimModule']")
            )
        ).click()

        # Click Add Button
        wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']",
                )
            )
        ).click()

        # Name Fields
        wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//input[@class='oxd-input oxd-input--active orangehrm-firstname']",
                )
            )
        ).send_keys("Naveen")
        driver.find_element(
            By.XPATH,
            "//input[@class='oxd-input oxd-input--active orangehrm-middlename']",
        ).send_keys("Venkat")
        driver.find_element(
            By.XPATH,
            "//input[@class='oxd-input oxd-input--active orangehrm-lastname']",
        ).send_keys("T")

        # Click Save (Initial save to create employee)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        print("Employee Personal Details page loaded")

        # Nickname & Other ID (Using safe relative XPATH)
        nickname_field = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//label[text()='Nickname']/../following-sibling::div/input",
                )
            )
        )
        nickname_field.send_keys("boss")

        driver.find_element(
            By.XPATH,
            "//label[text()='Other Id']/../following-sibling::div/input",
        ).send_keys("voter id")

        # Driver's License
        driver.find_element(
            By.XPATH,
            "//label[text()=\"Driver's License Number\"]/../following-sibling::div/input",
        ).send_keys("1234567")

        # Dropdowns using ActionChains with proper waiting
        action = ActionChains(driver)

        # Nationality
        nat_dropdown = driver.find_element(
            By.XPATH,
            "//label[text()='Nationality']/../following-sibling::div//div[@class='oxd-select-text-input']",
        )
        action.move_to_element(nat_dropdown).click().perform()
        indian_opt = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Indian']"))
        )
        action.move_to_element(indian_opt).click().perform()

        # Marital Status
        marital_dropdown = driver.find_element(
            By.XPATH,
            "//label[text()='Marital Status']/../following-sibling::div//div[@class='oxd-select-text-input']",
        )
        action.move_to_element(marital_dropdown).click().perform()
        single_opt = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Single']"))
        )
        action.move_to_element(single_opt).click().perform()

        # Gender (Male)
        driver.find_element(By.XPATH, "//label[text()='Male']").click()

        # Save Personal Details
        driver.find_element(
            By.XPATH, "(//button[@type='submit'])[1]"
        ).click()
        print("Successful employee addition")
        time.sleep(3)  # Small buffer for data saving

        # --- STEP 4: SEARCH & UPDATE ---
        driver.find_element(
            By.XPATH, "//a[@href='/web/index.php/pim/viewPimModule']"
        ).click()

        # Search Employee
        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Type for hints...'])[1]")
            )
        ).send_keys("Naveen")
        driver.find_element(
            By.XPATH, "//button[text()=' Search ']"
        ).click()

        # Click Edit (Using specific icon button)
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button/i[@class='oxd-icon bi-pencil-fill']")
            )
        ).click()

        # Update License Number
        license_field = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//label[text()=\"Driver's License Number\"]/../following-sibling::div/input",
                )
            )
        )
        license_field.clear()  # Old value-ஐ அழிக்க
        license_field.send_keys("567889")

        driver.find_element(
            By.XPATH, "(//button[@type='submit'])[1]"
        ).click()
        print("Successful employee updated")
        time.sleep(3)

        # --- STEP 5: DELETE EMPLOYEE ---
        driver.find_element(
            By.XPATH, "//a[@href='/web/index.php/pim/viewPimModule']"
        ).click()

        wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "(//input[@placeholder='Type for hints...'])[1]")
            )
        ).send_keys("Naveen")
        driver.find_element(
            By.XPATH, "//button[text()=' Search ']"
        ).click()

        # Click Delete Icon
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button/i[@class='oxd-icon bi-trash']")
            )
        ).click()

        # Confirm Delete Dialog
        wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(., 'Yes, Delete')]")
            )
        ).click()
        print("Successful employee deletion")

        time.sleep(2)
        driver.quit()


us = OrangeHRMProject()
us.test()