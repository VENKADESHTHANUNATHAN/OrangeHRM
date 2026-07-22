from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class project():
 def test(self):
    #open browser
    driver=webdriver.Chrome()
    baseurl="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    driver.get(baseurl)
    driver.implicitly_wait(10)
    

    #maximize window
    driver.maximize_window()
    time.sleep(3)
#step1
    #search username
    search_username = driver.find_element(By.NAME,'username')
    search_username.send_keys("Admin")

    #search password 
    search_password = driver.find_element(By.NAME,'password')
    search_password.send_keys("admin123")
    time.sleep(3) 

    #click login
    xpath_login="//button[@type='submit']"
    search_login = driver.find_element(By.XPATH,xpath_login).click()
    time.sleep(3)
    print("The user is logged in successfully")

    
    #click logout
    xpath_click=driver.find_element(By.XPATH,"//i [@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']").click()
    time.sleep(3)
    xpath_logout="//a[@href='/web/index.php/auth/logout']"
    search_logout = driver.find_element(By.XPATH,xpath_logout).click()
    time.sleep(3)
#step 2
    #again search username
    search_username = driver.find_element(By.NAME,'username')
    search_username.send_keys("Admin")

    #again search password 
    search_password = driver.find_element(By.NAME,'password')
    search_password.send_keys("invalidpassword")
    time.sleep(3) 

    #again click login
    xpath_login="//button[@type='submit']"
    search_login = driver.find_element(By.XPATH,xpath_login).click()
    time.sleep(3)
    xpath_invalid="//p[text()='Invalid credentials']"
    search_invalid = driver.find_element(By.XPATH,xpath_invalid).text
    print(search_invalid)
    print("A vaid error message for invalid credentials is dispalyed")
    time.sleep(3)

#step 3
    #then search username
    search_username = driver.find_element(By.NAME,'username')
    search_username.send_keys("Admin")

    #then search password 
    search_password = driver.find_element(By.NAME,'password')
    search_password.send_keys("admin123")
    time.sleep(3) 

    #then click login
    xpath_login="//button[@type='submit']"
    search_login = driver.find_element(By.XPATH,xpath_login).click()
    time.sleep(3)

    #click pim
    xpath_pim="//a[@href='/web/index.php/pim/viewPimModule']"
    #xpath_pim="//li [@class='oxd-main-menu-item-wrapper'][2]"
    search_pim = driver.find_element(By.XPATH,xpath_pim).click()
    time.sleep(3)

    #click add button
    xpath_add="//button[@class='oxd-button oxd-button--medium oxd-button--secondary']"
    #search_add = driver.find_element(By.NAME,' Add ').click()
    search_addd= driver.find_element(By.XPATH,xpath_add).click()
    time.sleep(3)

    #click firstname
    xpath_firstname="//input [@class='oxd-input oxd-input--active orangehrm-firstname']"
    search_firstname = driver.find_element(By.XPATH,xpath_firstname)
    search_firstname.send_keys("Naveen")
    time.sleep(3)

    #click Middlename
    xpath_Middlename="//input[@class='oxd-input oxd-input--active orangehrm-middlename']"
    search_Middlename = driver.find_element(By.XPATH,xpath_Middlename)
    search_Middlename.send_keys("Venkat")
    time.sleep(3)

    #click lastname
    xpath_lastname="//input[@class='oxd-input oxd-input--active orangehrm-lastname']"
    search_lastname = driver.find_element(By.XPATH,xpath_lastname)
    search_lastname.send_keys("T")
    time.sleep(3)

    #click save
    xpath_save="//button[@type='submit']"
    search_save = driver.find_element(By.XPATH,xpath_save).click()
    time.sleep(3)
    
    #click nickname
    xpath_nickname="(//input [@class='oxd-input oxd-input--active'])[2]"
    search_nickname = driver.find_element(By.XPATH,xpath_nickname)
    search_nickname.send_keys("boss")
    time.sleep(3)
    
    #click other id
    xpath_other_id="//label[text()='Other Id']/../following-sibling::div/input"
    search_other_id = driver.find_element(By.XPATH,xpath_other_id)
    search_other_id.send_keys("voter id")
    time.sleep(3)

    #click Driver's License Number
    xpath_License_Number="(//input [@class='oxd-input oxd-input--active'])[4]"
    search_License_Number = driver.find_element(By.XPATH,xpath_License_Number)
    search_License_Number.send_keys("1234567")
    time.sleep(3)
    
    #expiry date
    xpath_expiry_date="(//input [@class='oxd-input oxd-input--active'])[5]"
    date_tab=driver.find_element(By.XPATH,xpath_expiry_date)
    date_tab.send_keys("2022-12-12")
    time.sleep(3)

    #click ssn Number
    xpath_ssn_Number="(//input [@class='oxd-input oxd-input--active'])[6]"
    search_ssn_Number = driver.find_element(By.XPATH,xpath_ssn_Number)
    search_ssn_Number.send_keys("1234567")
    time.sleep(3)

    #click sin Number
    xpath_sin_Number="(//input [@class='oxd-input oxd-input--active'])[7]"
    search_sin_Number = driver.find_element(By.XPATH,xpath_sin_Number)
    search_sin_Number.send_keys("1234567")
    time.sleep(3)
    
    #click nationality
    click_nationality=driver.find_element(By.XPATH,"(//div[@ class='oxd-select-text oxd-select-text--active'])[1]")
    action=ActionChains(driver)
    action.move_to_element(click_nationality).click().perform()
    xpath_Indian="//span[text()='Indian']"
    search_Indian = driver.find_element(By.XPATH,xpath_Indian)
    action.move_to_element(search_Indian ).click().perform()
    time.sleep(3)

    #click marital status
    click_marital_status=driver.find_element(By.XPATH,"(//div[@class='oxd-select-text oxd-select-text--active'])[2]")
    action=ActionChains(driver)
    action.move_to_element(click_marital_status).click().perform()
    xpath_single="//span [text()='Single']"
    search_single = driver.find_element(By.XPATH,xpath_single)
    action.move_to_element(search_single).click().perform()
    time.sleep(3)
    
    #dob
    xpath_dob_date="(//input[@placeholder='yyyy-mm-dd'])[2]"
    date_tab=driver.find_element(By.XPATH,xpath_dob_date)
    date_tab.send_keys("2022-12-12")
    time.sleep(3)
    
    #gender
    xpath_male="(//span[@ class='oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input'])[1]"
    search_male = driver.find_element(By.XPATH,xpath_male).click()
    time.sleep(3)
    
    #click military service
    xpath_military_service="(//input [@class='oxd-input oxd-input--active'])[10]"
    search_military_service = driver.find_element(By.XPATH,xpath_military_service)
    search_military_service.send_keys("no")
    
    
    #click smoker
    xpath_smoker="//i[@class='oxd-icon bi-check oxd-checkbox-input-icon']"
    search_smoker = driver.find_element(By.XPATH,xpath_smoker).click()
    
    #click save
    xpath_save="//button[@type='submit'][1]"
    search_save = driver.find_element(By.XPATH,xpath_save).click()
    time.sleep(3)

    #blood type
    click_blood_type=driver.find_element(By.XPATH,"(//div[@class='oxd-select-text oxd-select-text--active'])[3]")
    action=ActionChains(driver)
    action.move_to_element(click_blood_type).click().perform()
    xpath_blood_group="//span[text()='A+']"
    search_blood_group= driver.find_element(By.XPATH,xpath_blood_group)
    action.move_to_element(search_blood_group).click().perform()
    time.sleep(10)

    #click save
    xpath_save="(//button[@type='submit'])[2]"
    search_save = driver.find_element(By.XPATH,xpath_save).click()
    time.sleep(3)
    print("successful employee addition")
    
#step 4
    #click pim
    xpath_pim="//a[@href='/web/index.php/pim/viewPimModule']"
    search_pim = driver.find_element(By.XPATH,xpath_pim).click()
    time.sleep(3)

    #search employee name
    xpath_search_employee_name="(//input[@ placeholder='Type for hints...'])[1]"
    search_employee_name = driver.find_element(By.XPATH,xpath_search_employee_name)
    search_employee_name.send_keys("naveen")
    time.sleep(3)
    
    #search 
    xpath_search="//button[text()=' Search ']"
    search_pim = driver.find_element(By.XPATH,xpath_search).click()
    time.sleep(3)

    #edit
    xpath_edit="(//button[@class='oxd-icon-button oxd-table-cell-action-space'])[2]"
    search_pim = driver.find_element(By.XPATH,xpath_edit).click()
    time.sleep(3)

    #click Driver's License Number
    xpath_License_Number="(//input [@class='oxd-input oxd-input--active'])[4]"
    search_License_Number = driver.find_element(By.XPATH,xpath_License_Number)
    search_License_Number.send_keys("567889")
    time.sleep(3)

    #click save
    xpath_save="//button[@type='submit'][1]"
    search_save = driver.find_element(By.XPATH,xpath_save).click()
    time.sleep(3)
    print("successful employee updated")

#step 5
    #click pim
    xpath_pim="//a[@href='/web/index.php/pim/viewPimModule']"
    search_pim = driver.find_element(By.XPATH,xpath_pim).click()
    time.sleep(3)

    #search employee name
    xpath_search_employee_name="(//input[@ placeholder='Type for hints...'])[1]"
    search_employee_name = driver.find_element(By.XPATH,xpath_search_employee_name)
    search_employee_name.send_keys("naveen")
    time.sleep(3)
    
    #search 
    xpath_search="//button[text()=' Search ']"
    search_pim = driver.find_element(By.XPATH,xpath_search).click()
    time.sleep(3)

    #delete
    xpath_delete="(//button[@class='oxd-icon-button oxd-table-cell-action-space'])[1]"
    search_delete = driver.find_element(By.XPATH,xpath_delete).click()
    time.sleep(3)

    #confirm delete
    xpath_delete="//i[@ class='oxd-icon bi-trash oxd-button-icon']"
    search_delete = driver.find_element(By.XPATH,xpath_delete).click()
    time.sleep(3)
    print("successful employee deletion")

    driver.quit()

us=project()
us.test() 
    

