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

class TestValidlogin():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_validlogin(self):
    self.driver.get("https://www.saucedemo.com/")
    self.driver.maximize_window()

    loginUserNameInput =  self.driver.find_element(By.ID, "user-name")
    loginUserNameInput.click()
    self.driver.find_element(By.ID, "user-name")
    loginUserNameInput.send_keys("standard_user")
    
    loginPasswordInput = self.driver.find_element(By.ID, "password")
    loginPasswordInput.click()
    loginPasswordInput = self.driver.find_element(By.ID, "password")
    loginPasswordInput.send_keys("secret_sauce")
    
    loginButton = self.driver.find_element(By.ID, "login-button")
    loginButton.click()