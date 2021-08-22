
#django
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import os

#selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

def autologin(driver, url, username, password):

    driver.get(url)
    #login
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'input[aria-label="ชื่อผู้ใช้"]'))).send_keys("4611101713")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'input[aria-label="รหัสผ่าน"]'))).send_keys("375468")
    #submit
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button[type="submit"]'))).click()
    
    return driver


def scrap(request):

    options = Options()
    options.headless = False
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome("D:/MyCode/TestSelenium",options=options)

    autologin(driver, 'https://homeisolation.dms.go.th/login/',"4611101713", "375468")

def automate_addpatient(request,pk):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    scrap(request)