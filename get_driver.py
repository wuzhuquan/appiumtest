from appium import webdriver
from selenium import webdriver
# ecoding=utf-8
__author__ = "Sven_Weng"


def get_driver():
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_experimental_option("androidProcess", "com.tencent.mm:tools")
    desired_caps = {'platformName': 'Android',
                    'platformVersion': '7.1.1',
                    'deviceName': 'CB512BPKD9',
                    #微信
                    'appPackage': 'com.tencent.mm',
                    'appActivity': 'ui.LauncherUI',
                    'ChromeOptions.CAPABILITY':'chrome_option',
                    #技师APP
                    #'appPackage': 'com.xmd.technician',
                    #'appActivity': '.window.WelcomeActivity',
                    #'appWaitActivity': '.window.MainActivity'

                    }

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    driver.implicitly_wait(30)
    return driver
