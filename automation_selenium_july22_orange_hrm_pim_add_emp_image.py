import subprocess
import time

from select import select
from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from automation_screenshot import take_screenshot

my_chromedriver = webdriver.Chrome()
my_chromedriver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
my_chromedriver.maximize_window()
time.sleep(5)
element_username = my_chromedriver.find_element(By.NAME, "username")
element_username.send_keys("Admin")
element_password = my_chromedriver.find_element(By.NAME, "password")
element_password.send_keys("admin123")
element_login_btn = my_chromedriver.find_element(By.XPATH, '//form/div[3]/button')
element_login_btn.click()
time.sleep(10)

element_pim_link = my_chromedriver.find_element(By.XPATH, "//span[text()='PIM']")
element_pim_link.click()
time.sleep(5)

element_pim_tabs = my_chromedriver.find_elements(By.XPATH, "//a[@class='oxd-topbar-body-nav-tab-item']")
for i in range(0, len(element_pim_tabs)):
    print(element_pim_tabs[i].text)

element_pim_tabs[1].click()
time.sleep(5)

tab_add_employee = my_chromedriver.find_element(By.XPATH,
                                                   "//div[@class='orangehrm-card-container']/*[text()='Add Employee']")

if tab_add_employee.is_displayed():
    print('Continue adding an employee...')

# try:
    pim_add_img_btn = my_chromedriver.find_element(By.XPATH, "(//button)[3]")
    pim_emp_name = my_chromedriver.find_element(By.XPATH, "//input[@name='firstName']")
    pim_emp_name.send_keys("Kate")

    pim_emp_name = my_chromedriver.find_element(By.XPATH, "//input[@name='lastName']")
    pim_emp_name.send_keys("Hudson")

    pim_save = my_chromedriver.find_element(By.XPATH, "//button[@type='submit']")

    pim_add_img_btn.click()
    script_path = "C:\\C Drive_GUVI_Lectures\\auto_id_exe\\Orange.exe"
    subprocess.run(script_path, shell=True)
    time.sleep(5)
    pim_save.click()
    time.sleep(5)

    print("Kate Hudson")
    take_screenshot(my_chromedriver)

