from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.extensions.android.nativekey import AndroidKey
from appium.options.android import UiAutomator2Options

desired_caps = {
    'platformName': 'Android',  # 被测手机是安卓
    'platformVersion': '10',  # 手机安卓版本，如果是鸿蒙系统，依次尝试 12、11、10 这些版本号
    'automationName': 'UiAutomator2',
    "deviceName": '192.168.31.8:5555',
    'appPackage': 'com.bilibili.app.in',  # 启动APP Package名称
    'appActivity': 'tv.danmaku.bili.MainActivityV2',  # 启动Activity名称
    'unicodeKeyboard': True,  # 自动化需要输入中文时填True
    'resetKeyboard': True,  # 执行完程序恢复原来输入法
    'noReset': True,  # 不要重置App
    'newCommandTimeout': 6000,
    # 'app': r'd:\apk\bili.apk',

}

# 连接Appium Server，初始化自动化环境
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',
                          options=UiAutomator2Options().load_capabilities(desired_caps))

# 设置缺省等待时间
driver.implicitly_wait(5)

# 如果有`青少年保护`界面，点击`我知道了`
iknow = driver.find_elements(By.ID, "text3")
if iknow:
    iknow.click()

# 根据id定位搜索位置框，点击
driver.find_element(By.ID, 'com.bilibili.app.in:id/search_text').click()

# 根据id定位搜索输入框，点击
sbox = driver.find_element(By.ID, 'com.bilibili.app.in:id/search_text')
sbox.send_keys('白月黑羽')
# 输入回车键，确定搜索
driver.press_keycode(AndroidKey.ENTER)

# 选择（定位）所有视频标题
eles = driver.find_elements(By.ID, 'title')

for ele in eles:
    # 打印标题
    print(ele.text)

input('**** Press to quit..')
driver.quit()
