from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import date
from selenium.webdriver.support.ui import Select


def print_base_info(driver1):
    print("driver.title:" + driver1.title)
    print("driver.current_url:" + driver1.current_url)
    # driver1.maximize_window()
    driver1.set_window_size(1900,1000)

def clickById(idStr):
    ele =driver.find_element(By.ID,idStr)
    ele.click()

def sendKeysByID(idStr,valueStr):
    ele = driver.find_element(By.ID,idStr)
    ele.send_keys(valueStr)

def selectByValue(idStr,valueStr):
    ele = driver.find_element(By.ID,idStr)
    Select(ele).select_by_value(valueStr)

def login():
    # 执行登录
    print("开始登录")
    username = driver.find_element(By.ID,"user_id")
    username.send_keys('admin')
     
    password = driver.find_element(By.ID,"psw")
    password.send_keys('admin')
    
    clickById("login")
    print("登录成功")
#
driver =  webdriver.Chrome()
driver.get("http://localhost:8080/")
print_base_info(driver)
time.sleep(1)

#
login()
time.sleep(1)
#

def insertBlood():
    clickById("menuli-1")
    time.sleep(1)
    clickById("btn_Add")
    time.sleep(1)

    selectByValue("IceDoorNoA","2")

    sendKeysByID("SeizureTime",date.today().strftime("%Y-%m-%d") + " 00:00:00")
    sendKeysByID("SeizureLocation","广东省深圳市南山区大新路")
    sendKeysByID("BloodSampleTime",date.today().strftime("%Y-%m-%d") + " 00:00:00")
    sendKeysByID("BloodSampleLocation","广东省深圳市南山区大新路")
    sendKeysByID("PoliceNoB","212222")
    sendKeysByID("PartyName","江某人")
    sendKeysByID("DriverLicenseNo","420581199601201632")
    sendKeysByID("Telephone","15671042869")
    sendKeysByID("VoucherNo","123456")
    sendKeysByID("ExpiratoryTime",date.today().strftime("%Y-%m-%d") + " 00:00:00")
    sendKeysByID("ExpiratoryValue","52")
    sendKeysByID("BloodSampleNo","u3")

    clickById("update") 
    time.sleep(2)
    driver._switch_to.alert.accept()


insertBlood()
time.sleep(1)
