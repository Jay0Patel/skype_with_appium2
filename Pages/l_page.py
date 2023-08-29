import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip


class LaunchPage():
    def __init__(self, driver):
        self.driver = driver

    def sign_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.CLASS_NAME, "android.widget.Button"))).click()

    def email_enter(self, email):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.CLASS_NAME, "android.widget.EditText"))).send_keys(
            email)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.Button[@text='Next']"))).click()

    def code_email(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (AppiumBy.XPATH, "//android.widget.TextView[@text='Email code to dev1.intellify@gmail.com']"))).click()
        except:
            self.driver.background_app(-1)
            self.driver.start_activity('com.google.android.gm', 'com.google.android.gm.ConversationListActivityGmail')
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (AppiumBy.XPATH, "//android.widget.TextView[@text='Your single-use code']"))).click()
            Otp_line = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH,
                                                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.widget.TextView[4]")))
            text = Otp_line.text.split('Your single-use code is: ')[-1]
            pyperclip.copy(text)
            self.OTP_pass = pyperclip.paste()

    def Otp(self):
        self.driver.activate_app('com.skype.raider')
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.CLASS_NAME, "android.widget.EditText"))).send_keys(self.OTP_pass)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.Button[@text='Sign in']"))).click()
        time.sleep(10)

    def FCE(self):
        time.sleep(5)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Continue']"))).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.Button[@text='Allow']"))).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Finish']"))).click()
        time.sleep(10)
