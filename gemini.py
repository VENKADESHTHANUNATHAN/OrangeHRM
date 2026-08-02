import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class OrangeHRMProject:

    def __init__(self):
        # குரோம் ஆப்சன்ஸ் அமைத்து ஹேங் ஆவதைத் தடுத்தல்
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")  # maximize_window-க்கு பதிலாக நேரடி ஆர்க்யூமென்ட்
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        # டிரைவர் தொடக்கம்
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=options
        )
        self.wait = WebDriverWait(self.driver, 15)

    def test(self):
        driver = self.driver
        wait = self.wait

        baseurl = (
            "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        )
        driver.get(baseurl)

        # === STEP 1: VALID LOGIN & LOGOUT ===
        wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("admin123")

        xpath_login = "//button[@type='submit']"
        driver.find_element(By.XPATH, xpath_login).click()
        print("The user is logged in successfully")

        # Logout
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

        # === STEP 2: INVALID LOGIN ===
        wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("invalidpassword")
        driver.find_element(By.XPATH, xpath_login).click()

        xpath_invalid = "//p[text()='Invalid credentials']"
        search_invalid = wait.until(
            EC.presence_of_element_located((By.XPATH, xpath_invalid))
        ).text
        print(f"Error Message Displayed: {search_invalid}")

        # === STEP 3: ADD EMPLOYEE ===
        driver.refresh()
        wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.XPATH, xpath_login).click()

        # Go to PIM
        xpath_pim = "//a[@href='/web/index.php/pim/viewPimModule']"
        wait.until(EC.element_to_be_clickable((By.XPATH, xpath_pim))).click()

        # Click Add Button
        xpath_add = (
            "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']"
        )
        wait.until(EC.element_to_be_clickable((By.XPATH, xpath_add))).click()

        # Fill Names
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

        # Save basic details
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        print("Employee basic details saved!")
        time.sleep(5)

        # Search & Edit profile
        driver.find_element(By.XPATH, xpath_pim).click()

        xpath_search_employee_name = (
            "(//input[@placeholder='Type for hints...'])[1]"
        )
        wait.until(
            EC.presence_of_element_located((By.XPATH, xpath_search_employee_name))
        ).send_keys("Naveen")

        driver.find_element(By.XPATH, "//button[text()=' Search ']").click()
        time.sleep(3)

        xpath_edit = "//button/i[@class='oxd-icon bi-pencil-fill']"
        wait.until(EC.element_to_be_clickable((By.XPATH, xpath_edit))).click()
        print("Navigated to Personal Details via Search Profile successfully!")

        # Fill Personal Details
        nickname_field = wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//label[contains(text(),'Nickname')]/../following-sibling::div/input",
                )
            )
        )
        nickname_field.send_keys("boss")

        driver.find_element(
            By.XPATH,
            "//label[contains(text(),'Other Id')]/../following-sibling::div/input",
        ).send_keys("voter id")

        driver.find_element(
            By.XPATH,
            "//label[contains(text(),\"Driver's License Number\")]/../following-sibling::div/input",
        ).send_keys("1234567")

        action = ActionChains(driver)

        # Nationality
        nat_dropdown = driver.find_element(
            By.XPATH,
            "//label[text()='Nationality']/../following-sibling::div//div[@class='oxd-select-text-input']",
        )
        action.move_to_element(nat_dropdown).click().perform()
        xpath_Indian = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Indian']"))
        )
        action.move_to_element(xpath_Indian).click().perform()

        # Marital Status
        marital_dropdown = driver.find_element(
            By.XPATH,
            "//label[text()='Marital Status']/../following-sibling::div//div[@class='oxd-select-text-input']",
        )
        action.move_to_element(marital_dropdown).click().perform()
        xpath_single = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Single']"))
        )
        action.move_to_element(xpath_single).click().perform()

        # Gender (Male)
        driver.find_element(By.XPATH, "//label[text()='Male']").click()

        # Save Personal Details
        driver.find_element(By.XPATH, "(//button[@type='submit'])[1]").click()
        print("Successful employee addition and details update")
        time.sleep(3)

        # === STEP 4: UPDATE LICENSE NUMBER ===
        driver.find_element(By.XPATH, xpath_pim).click()
        wait.until(
            EC.presence_of_element_located((By.XPATH, xpath_search_employee_name))
        ).send_keys("Naveen")
        driver.find_element(By.XPATH, "//button[text()=' Search ']").click()
        time.sleep(2)

        wait.until(EC.element_to_be_clickable((By.XPATH, xpath_edit))).click()

        license_edit = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//label[contains(text(),\"Driver's License Number\")]/../following-sibling::div/input",
                )
            )
        )
        license_edit.clear()
        license_edit.send_keys("567889")

        driver.find_element(By.XPATH, "(//button[@type='submit'])[1]").click()
        print("Successful employee updated")
        time.sleep(3)

        # === STEP 5: DELETE EMPLOYEE ===
        driver.find_element(By.XPATH, xpath_pim).click()
        wait.until(
            EC.presence_of_element_located((By.XPATH, xpath_search_employee_name))
        ).send_keys("Naveen")
        driver.find_element(By.XPATH, "//button[text()=' Search ']").click()
        time.sleep(2)

        xpath_delete = "//button/i[@class='oxd-icon bi-trash']"
        wait.until(
            EC.element_to_be_clickable((By.XPATH, xpath_delete))
        ).click()

        xpath_confirm = "//button[contains(., 'Yes, Delete')]"
        wait.until(
            EC.element_to_be_clickable((By.XPATH, xpath_confirm))
        ).click()
        print("Successful employee deletion")

        time.sleep(2)
        driver.quit()


# Execution
project = OrangeHRMProject()
project.test()
