# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestValidloginwait():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_validloginwait(self):
    self.driver.get("https://www.saucedemo.com/")
    self.driver.maximize_window()

    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "user-name")))
    loginUserNameInput = self.driver.find_element(By.ID, "user-name")
    loginUserNameInput.click()
    self.driver.find_element(By.ID, "user-name")
    loginUserNameInput.send_keys("standard_user")
    
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "password")))
    loginPasswordInput = self.driver.find_element(By.ID, "password")
    loginPasswordInput.send_keys("secret_sauce")
    
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "login-button")))
    loginButton = self.driver.find_element(By.ID, "login-button")
    loginButton.click()