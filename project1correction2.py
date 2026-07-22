import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class project:

    def test(self):
        # தானாகவே சரியான குரோம் டிரைவரை எடுத்துக்கொள்ளும்
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )
        wait = WebDriverWait(driver, 10)  # 10 செகண்ட் வரை காத்திருக்கும் அமைப்பு

        baseurl = (
            "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        )
        driver.get(baseurl)

        # maximize window
        driver.maximize_window()

        # === STEP 1: VALID LOGIN & LOGOUT ===
        # search username
        wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")

        # search password
        driver.find_element(By.NAME, "password").send_keys("admin123")

        # click login
        xpath_login = "//button[@type='submit']"
        driver.find_element(By.XPATH, xpath_login).click()
        print("The user is logged in successfully")

        # click logout
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
        # again search username
        wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")

        # again search password
        driver.find_element(By.NAME, "password").send_keys("invalidpassword")

        # again click login
        driver.find_element(By.XPATH, xpath_login).click()

        xpath_invalid = "//p[text()='Invalid credentials']"
        search_invalid = wait.until(
            EC.presence_of_element_located((By.XPATH, xpath_invalid))
        ).text
        print(f"Error Message Displayed: {search_invalid}")
        print("A valid error message for invalid credentials is displayed")

        # === STEP 3: ADD EMPLOYEE ===
        driver.refresh()  # பழைய எர்ரர் பக்கத்தை ரீஃப்ரெஷ் செய்கிறது

        # login again
        wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.XPATH, xpath_login).click()

        # click pim
        xpath_pim = "//a[@href='/web/index.php/pim/viewPimModule']"
        wait.until(EC.element_to_be_clickable((By.XPATH, xpath_pim))).click()

        # click add button
        xpath_add = (
            "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']"
        )
        wait.until(EC.element_to_be_clickable((By.XPATH, xpath_add))).click()

        # click firstname
        xpath_firstname = (
            "//input[@class='oxd-input oxd-input--active orangehrm-firstname']"
        )
        wait.until(
            EC.presence_of_element_located((By.XPATH, xpath_firstname))
        ).send_keys("Naveen")

        # click Middlename
        xpath_Middlename = (
            "//input[@class='oxd-input oxd-input--active orangehrm-middlename']"
        )
        driver.find_element(By.XPATH, xpath_Middlename).send_keys("Venkat")

        # click lastname
        xpath_lastname = (
            "//input[@class='oxd-input oxd-input--active orangehrm-lastname']"
        )
        driver.find_element(By.XPATH, xpath_lastname).send_keys("T")

        # click save (எம்ப்ளாயி-ஐ உருவாக்கும் முதல் சேவ்)
        xpath_save = "//button[@type='submit']"
        driver.find_element(By.XPATH, xpath_save).click()
        print("Employee created successfully!")

        # மிக முக்கியம்: டேட்டாபேஸ்ல சேவ் ஆகி அடுத்த பேஜ் லோட் ஆக 5 செகண்ட் கட்டாயம் தேவை
        time.sleep(5)

        # click nickname (உறுதியான புதிய XPATH)
        nickname_field = wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//input[ancestor::div[contains(@class,'oxd-input-group')][.//label[contains(normalize-space(),'Nickname')]]]",
                )
            )
        )
        nickname_field.send_keys("boss")

        # click other id
        other_id_field = driver.find_element(
            By.XPATH,
            "//input[ancestor::div[contains(@class,'oxd-input-group')][.//label[contains(normalize-space(),'Other Id')]]]",
        )
        other_id_field.send_keys("voter id")

        # click Driver's License Number
        license_field = driver.find_element(
            By.XPATH,
            "//input[ancestor::div[contains(@class,'oxd-input-group')][.//label[contains(normalize-space(),\"Driver's License Number\")]]]",
        )
        license_field.send_keys("1234567")

        # expiry date
        expiry_field = driver.find_element(
            By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[1]"
        )
        expiry_field.send_keys("2028-12-12")

        action = ActionChains(driver)

        # click nationality
        nat_dropdown = driver.find_element(
            By.XPATH,
            "//label[text()='Nationality']/../following-sibling::div//div[@class='oxd-select-text-input']",
        )
        action.move_to_element(nat_dropdown).click().perform()
        xpath_Indian = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Indian']"))
        )
        action.move_to_element(xpath_Indian).click().perform()

        # click marital status
        marital_dropdown = driver.find_element(
            By.XPATH,
            "//label[text()='Marital Status']/../following-sibling::div//div[@class='oxd-select-text-input']",
        )
        action.move_to_element(marital_dropdown).click().perform()
        xpath_single = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Single']"))
        )
        action.move_to_element(xpath_single).click().perform()

        # dob
        dob_field = driver.find_element(
            By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[2]"
        )
        dob_field.send_keys("1995-05-15")

        # gender (Male)
        driver.find_element(By.XPATH, "//label[text()='Male']").click()

        # click save for Personal Details
        driver.find_element(By.XPATH, "(//button[@type='submit'])[1]").click()
        print("Successful employee addition")
        time.sleep(3)

        # === STEP 4: SEARCH & UPDATE ===
        driver.find_element(By.XPATH, xpath_pim).click()

        # search employee name
        xpath_search_employee_name = (
            "(//input[@placeholder='Type for hints...'])[1]"
        )
        wait.until(
            EC.presence_of_element_located((By.XPATH, xpath_search_employee_name))
        ).send_keys("Naveen")

        # click search button
        xpath_search = "//button[text()=' Search ']"
        driver.find_element(By.XPATH, xpath_search).click()
        time.sleep(2)

        # click edit icon button
        xpath_edit = "//button/i[@class='oxd-icon bi-pencil-fill']"
        wait.until(EC.element_to_be_clickable((By.XPATH, xpath_edit))).click()

        # click Driver's License Number and Update
        license_edit = wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//input[ancestor::div[contains(@class,'oxd-input-group')][.//label[contains(normalize-space(),\"Driver's License Number\")]]]",
                )
            )
        )
        license_edit.clear()  # பழைய மதிப்பை அழிக்கிறது
        license_edit.send_keys("567889")

        # click save
        driver.find_element(By.XPATH, "(//button[@type='submit'])[1]").click()
        print("Successful employee updated")
        time.sleep(3)

        # === STEP 5: DELETE EMPLOYEE ===
        driver.find_element(By.XPATH, xpath_pim).click()

        # search employee name again
        wait.until(
            EC.presence_of_element_located((By.XPATH, xpath_search_employee_name))
        ).send_keys("Naveen")
        driver.find_element(By.XPATH, xpath_search).click()
        time.sleep(2)

        # click delete icon button
        xpath_delete = "//button/i[@class='oxd-icon bi-trash']"
        wait.until(
            EC.element_to_be_clickable((By.XPATH, xpath_delete))
        ).click()

        # confirm delete pop-up button
        xpath_confirm = "//button[contains(., 'Yes, Delete')]"
        wait.until(
            EC.element_to_be_clickable((By.XPATH, xpath_confirm))
        ).click()
        print("Successful employee deletion")

        time.sleep(2)
        driver.quit()


us = project()
us.test()