from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

# from login_page import LoginPage
# from dashboard_page import DashboardPage
# from employee_page import EmployeePage


class OrangeHRMProject:

    def __init__(self):

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )

        self.driver.maximize_window()
        self.driver.get(
            "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        )

        self.wait = WebDriverWait(self.driver, 20)

        self.login = LoginPage(self.driver, self.wait)
        self.dashboard = DashboardPage(self.driver, self.wait)
        self.employee = EmployeePage(self.driver, self.wait)

    def run(self):

        try:

            print("=" * 60)
            print("STEP 1 : VALID LOGIN")
            print("=" * 60)

            self.login.login(
                username="Admin",
                password="admin123"
            )

            print("Login Successful\n")

            print("=" * 60)
            print("STEP 2 : LOGOUT")
            print("=" * 60)

            self.dashboard.logout()

            print("Logout Successful\n")

            print("=" * 60)
            print("STEP 3 : INVALID LOGIN")
            print("=" * 60)

            self.login.invalid_login(
                username="Admin",
                password="wrongpassword"
            )

            print("Invalid Login Verified\n")

            self.driver.refresh()

            print("=" * 60)
            print("STEP 4 : LOGIN AGAIN")
            print("=" * 60)

            self.login.login(
                username="Admin",
                password="admin123"
            )

            print("Login Successful\n")

            print("=" * 60)
            print("STEP 5 : OPEN PIM")
            print("=" * 60)

            self.dashboard.open_pim()

            print("=" * 60)
            print("STEP 6 : ADD EMPLOYEE")
            print("=" * 60)

            self.employee.add_employee(
                firstname="Naveen",
                middlename="Venkat",
                lastname="T"
            )

            print("Employee Added Successfully\n")

            print("=" * 60)
            print("STEP 7 : UPDATE PERSONAL DETAILS")
            print("=" * 60)

            self.employee.update_personal_details(
                nickname="Boss",
                other_id="VOTER123",
                license_number="123456789"
            )

            print("Personal Details Updated\n")

            print("=" * 60)
            print("STEP 8 : SEARCH EMPLOYEE")
            print("=" * 60)

            self.dashboard.open_pim()

            self.employee.search_employee(
                employee_name="Naveen"
            )

            print("Employee Found\n")

            print("=" * 60)
            print("STEP 9 : EDIT EMPLOYEE")
            print("=" * 60)

            self.employee.edit_employee(
                new_license="567889"
            )

            print("Employee Updated\n")

            print("=" * 60)
            print("STEP 10 : DELETE EMPLOYEE")
            print("=" * 60)

            self.dashboard.open_pim()

            self.employee.search_employee(
                employee_name="Naveen"
            )

            self.employee.delete_employee()

            print("Employee Deleted Successfully\n")

            print("=" * 60)
            print("PROJECT EXECUTED SUCCESSFULLY")
            print("=" * 60)

        except Exception as e:

            print("PROJECT FAILED")
            print(e)

        finally:

            self.driver.quit()


if __name__ == "__main__":

    project = OrangeHRMProject()

    project.run()

#Login
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver, wait):

        self.driver = driver
        self.wait = wait

        self.username = (By.NAME, "username")
        self.password = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")
        self.dashboard = (By.XPATH, "//h6[text()='Dashboard']")
        self.invalid_message = (
            By.XPATH,
            "//p[text()='Invalid credentials']"
        )

    def enter_username(self, username):

        user = self.wait.until(
            EC.visibility_of_element_located(self.username)
        )

        user.clear()
        user.send_keys(username)

    def enter_password(self, password):

        pwd = self.wait.until(
            EC.visibility_of_element_located(self.password)
        )

        pwd.clear()
        pwd.send_keys(password)

    def click_login(self):

        self.wait.until(
            EC.element_to_be_clickable(self.login_button)
        ).click()

    def login(self, username, password):

        self.enter_username(username)

        self.enter_password(password)

        self.click_login()

        self.wait.until(
            EC.visibility_of_element_located(self.dashboard)
        )

        print("Login Successful")

    def invalid_login(self, username, password):

        self.enter_username(username)

        self.enter_password(password)

        self.click_login()

        error = self.wait.until(
            EC.visibility_of_element_located(
                self.invalid_message
            )
        )

        print("Error Message :", error.text)

        assert (
            error.text == "Invalid credentials"
        ), "Invalid Login Test Failed"

        print("Invalid Login Test Passed")



#dashboard_page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:

    def __init__(self, driver, wait):

        self.driver = driver
        self.wait = wait

        # Dashboard
        self.dashboard_header = (
            By.XPATH,
            "//h6[text()='Dashboard']"
        )

        # User Dropdown
        self.user_dropdown = (
            By.XPATH,
            "//p[@class='oxd-userdropdown-name']"
        )

        # Logout
        self.logout_button = (
            By.XPATH,
            "//a[text()='Logout']"
        )

        # Username textbox (Login page verification)
        self.username = (
            By.NAME,
            "username"
        )

        # PIM Menu
        self.pim_menu = (
            By.XPATH,
            "//span[text()='PIM']"
        )

        # Employee List Header
        self.employee_header = (
            By.XPATH,
            "//h5[text()='Employee Information']"
        )

    # -----------------------------
    # Verify Dashboard
    # -----------------------------
    def verify_dashboard(self):

        self.wait.until(
            EC.visibility_of_element_located(
                self.dashboard_header
            )
        )

        print("Dashboard Loaded Successfully")

    # -----------------------------
    # Logout
    # -----------------------------
    def logout(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.user_dropdown
            )
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(
                self.logout_button
            )
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(
                self.username
            )
        )

        print("Logout Successful")

    # -----------------------------
    # Open PIM Module
    # -----------------------------
    def open_pim(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.pim_menu
            )
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(
                self.employee_header
            )
        )

        print("PIM Module Opened Successfully")


#employee_page.py (Part-1)

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class EmployeePage:

    def __init__(self, driver, wait):

        self.driver = driver
        self.wait = wait

    # ==========================================
    # ADD EMPLOYEE
    # ==========================================

    def add_employee(self, firstname, middlename, lastname):

        self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[normalize-space()='Add']"
                )
            )
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(
                (By.NAME, "firstName")
            )
        ).send_keys(firstname)

        self.driver.find_element(
            By.NAME,
            "middleName"
        ).send_keys(middlename)

        self.driver.find_element(
            By.NAME,
            "lastName"
        ).send_keys(lastname)

        self.driver.find_element(
            By.XPATH,
            "//button[@type='submit']"
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//h6[text()='Personal Details']"
                )
            )
        )

        print("Employee Added Successfully")

    # ==========================================
    # PERSONAL DETAILS
    # ==========================================

    def update_personal_details(
        self,
        nickname,
        other_id,
        license_number
    ):

        nickname_box = self.wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//label[text()='Nickname']/../following-sibling::div/input"
                )
            )
        )

        nickname_box.clear()

        nickname_box.send_keys(nickname)

        otherid = self.driver.find_element(
            By.XPATH,
            "//label[text()='Other Id']/../following-sibling::div/input"
        )

        otherid.clear()

        otherid.send_keys(other_id)

        license_box = self.driver.find_element(
            By.XPATH,
            "//label[contains(text(),\"Driver's License Number\")]/../following-sibling::div/input"
        )

        license_box.clear()

        license_box.send_keys(license_number)

        # -----------------------------
        # Nationality
        # -----------------------------

        self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "(//div[@class='oxd-select-text oxd-select-text--active'])[1]"
                )
            )
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//span[text()='Indian']"
                )
            )
        ).click()

        # -----------------------------
        # Marital Status
        # -----------------------------

        self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "(//div[@class='oxd-select-text oxd-select-text--active'])[2]"
                )
            )
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//span[text()='Single']"
                )
            )
        ).click()

        # -----------------------------
        # Gender
        # -----------------------------

        self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//label[text()='Male']"
                )
            )
        ).click()

        # -----------------------------
        # Save
        # -----------------------------

        self.driver.find_element(
            By.XPATH,
            "(//button[@type='submit'])[1]"
        ).click()

        print("Personal Details Updated Successfully")


#part2

    # ==========================================
    # SEARCH EMPLOYEE
    # ==========================================

    def search_employee(self, employee_name):

        search_box = self.wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "(//input[@placeholder='Type for hints...'])[1]"
                )
            )
        )

        search_box.clear()

        search_box.send_keys(employee_name)

        self.driver.find_element(
            By.XPATH,
            "//button[normalize-space()='Search']"
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//div[@class='oxd-table-body']"
                )
            )
        )

        print("Employee Search Completed")

    # ==========================================
    # CLICK EDIT BUTTON
    # ==========================================

    def open_employee(self):

        self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[.//i[contains(@class,'bi-pencil-fill')]]"
                )
            )
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//h6[text()='Personal Details']"
                )
            )
        )

        print("Employee Profile Opened")

    # ==========================================
    # EDIT EMPLOYEE
    # ==========================================

    def edit_employee(self, new_license):

        self.open_employee()

        license_box = self.wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//label[contains(text(),\"Driver's License Number\")]/../following-sibling::div/input"
                )
            )
        )

        license_box.clear()

        license_box.send_keys(new_license)

        self.driver.find_element(
            By.XPATH,
            "(//button[@type='submit'])[1]"
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//h6[text()='Personal Details']"
                )
            )
        )

        print("Employee Updated Successfully")



#part3

    # ==========================================
    # DELETE EMPLOYEE
    # ==========================================

    def delete_employee(self):

        self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[.//i[contains(@class,'bi-trash')]]"
                )
            )
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//div[@class='orangehrm-modal-footer']"
                )
            )
        )

        print("Delete Confirmation Popup Displayed")

        self.confirm_delete()

    # ==========================================
    # CONFIRM DELETE
    # ==========================================

    def confirm_delete(self):

        self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[normalize-space()='Yes, Delete']"
                )
            )
        ).click()

        self.wait.until(
            EC.invisibility_of_element_located(
                (
                    By.XPATH,
                    "//div[@class='oxd-loading-spinner']"
                )
            )
        )

        print("Employee Deleted Successfully")

    # ==========================================
    # VERIFY EMPLOYEE PAGE
    # ==========================================

    def verify_employee_list(self):

        self.wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//h5[text()='Employee Information']"
                )
            )
        )

        print("Employee List Page Loaded")

    # ==========================================
    # CLEAR SEARCH BOX
    # ==========================================

    def clear_search_box(self):

        search_box = self.wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "(//input[@placeholder='Type for hints...'])[1]"
                )
            )
        )

        search_box.clear()

    # ==========================================
    # VERIFY PERSONAL DETAILS PAGE
    # ==========================================

    def verify_personal_details(self):

        self.wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//h6[text()='Personal Details']"
                )
            )
        )

        print("Personal Details Page Verified")

    # ==========================================
    # CLOSE DRIVER
    # ==========================================

    def close_browser(self):

        self.driver.quit()

        print("Browser Closed Successfully")

        