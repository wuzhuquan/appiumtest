from appium import webdriver
# ecoding=utf-8
__author__ = "Sven_Weng"


def get_driver():

    desired_caps = {'platformName': 'Android',
                    'platformVersion': '7.0',
                    'deviceName': 'CB512BPKD9',
                    'appPackage': 'com.android.calculator2',
                    'appActivity': '.Calculator'
                    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    driver.implicitly_wait(30)
    return driver
