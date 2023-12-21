import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class MouseAction:

    def rightClick(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option(name="detach", value=True)
        driver = webdriver.Chrome(options)
        driver.maximize_window()
        driver.get("https://www.bigbasket.com/")
        action=ActionChains(driver)
        tea = driver.find_element(By.XPATH, "(//span[text()='Tea'])[1]")
        action.move_to_element(tea).perform()
        tea.click()
        brand = driver.find_element(By.XPATH,"(//span[text()='Green Tea'])[2]")
        action.move_to_element(brand).perform()
        brand.click()

MouseAction().rightClick()







