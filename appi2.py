from appium import webdriver

class bot():

    def __init__(self):
        self.starting()
        self.test_LoginWithRightCredential()

    def test_LoginWithRightCredential(self):
        email = driver.find_element_by_id("com.ATG.World:id/email")
        email.send_keys("wiz_saurabh@rediffmail.com")
        password = driver.find_element_by_id("com.ATG.World:id/password")
        password.send_keys("Pass@123")
        signin = driver.find_element_by_id("com.ATG.World:id/email_sign_in_button")
        signin.click()
        print("test_LoginWithRightCredential passed")
        driver.implicitly_wait(5)
        driver.find_element_by_id("com.ATG.World:id/btnGotit").click()
        driver.implicitly_wait(3)
        driver.find_element_by_id("com.ATG.World:id/btnGotit").click()
        driver.implicitly_wait(5)
        driver.find_element_by_id("com.ATG.World:id/fab").click()
        driver.implicitly_wait(3)
        driver.find_element_by_id("com.ATG.World:id/image_fab_clicked").click()
        driver.implicitly_wait(3)
        driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        driver.implicitly_wait(3)
        driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        driver.implicitly_wait(3)
        driver.find_element_by_id("android:id/text1").click()
        driver.implicitly_wait(3)
        driver.find_element_by_id("com.google.android.apps.photos:id/image").click()
        driver.implicitly_wait(3)
        driver.find_element_by_xpath('//android.view.ViewGroup[@content-desc="Photo taken on Oct 3, 2021 6:12:26 PM"]').click()
        driver.implicitly_wait(3)
        driver.find_element_by_id("com.ATG.World:id/layout_select_group_container").click()
        driver.implicitly_wait(3)
        driver.find_element_by_id("com.ATG.World:id/layout_select_group_container").click()
        driver.implicitly_wait(3)
        driver.find_element_by_id("com.ATG.World:id/group_background").click()
        driver.implicitly_wait(3)
        driver.find_element_by_id("com.ATG.World:id/layout_group_list_done").click()
        driver.implicitly_wait(3)
        driver.find_element_by_id("com.ATG.World:id/layout_group_list_done").click()
        driver.implicitly_wait(3)



    def starting(self):
        driver.find_element_by_id("com.ATG.World:id/getStartedTv").click()
        driver.implicitly_wait(5)
        driver.find_element_by_id("com.ATG.World:id/login_email").click()
        driver.implicitly_wait(5)



desired_cap ={
    "platformName": "android",
    "deviceName": "emulator-5554",
    "app" : r"C:\Users\avinash\Downloads\21032020.apk",
    "appActivity": "com.atg.world.activity.SplashActivity",
    "appPackage": "com.ATG.World"


}

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)

mybot = bot()
mybot.starting()
mybot.test_LoginWithRightCredential()



