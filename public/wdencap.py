#coding=utf-8

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class SeEncap(object):
    ''' 封装了selenium2的部分方法'''

    def __init__(self, browser="ff"):
        '''
        Run class initialization method, the default is proper
        to drive the Firefox browser. Of course, you can also
        pass parameter for other browser, Chrome browser for the "Chrome",
        the Internet Explorer browser for "internet explorer" or "ie".
        '''
        if browser == "firefox" :
            self.driver = webdriver.Firefox()
        elif browser == "chrome" or browser == "ff":
            self.driver = webdriver.Chrome()
        elif browser == "internet explorer" or browser == "ie":
            self.driver = webdriver.Ie()
        elif browser == "opera":
            self.driver = webdriver.Opera()
        elif browser == "chrome_headless":
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            self.driver = webdriver.Chrome(chrome_options=chrome_options)
        elif browser == 'edge':
            self.driver = webdriver.Edge()
        else:
            raise NameError(
                "Not found %s browser,You can enter 'ie', 'ff', 'opera', 'edge', 'chrome' or 'chrome_headless'." % browser)

    def element_wait(self,cls,secs=5):
        WebDriverWait(self.driver,secs,1).until(EC.presence_of_element_located((cls[0],cls[1])))

    def open(self,url):
        self.driver.get(url)

    def max_window(self):
        self.driver.maximize_window()

    def set_window_size(self,wight,hight):
        self.driver.set_window_size(wight,hight)

    def get_element(self,cls):
        '''定位单一元素
        cls为传入的定位元素元祖，格式为[定位方式,定位元素]，例如：[By.ID,'loginform-username']
        可定位的方式支持：ID,NAME,XPATH,CLASS,LINK_TEXT,
        '''
        element = self.driver.find_element(cls[0],cls[1])
        return element

    def get_elements(self,cls):
        #待继续完善
        '''定位一组元素，返回所有元素
            cls为传入的定位元素元祖，格式为[定位方式,定位元素]，例如：[By.ID,'loginform-username']
            可定位的方式支持：ID,NAME,XPATH,CLASS,LINK_TEXT,
        '''
        elements = self.driver.find_element(cls[0], cls[1])
        return elements

    def type(self,cls,text):
        self.element_wait(cls)
        el=self.get_element(cls)
        el.send_keys(text)

    def element_click(self,el):
        el.click()

    def click(self,cls):
        el=self.get_element(cls)
        el.click()

    def right_click(self, css):
        '''
        Right click element.

        Usage:
        driver.right_click("css=>#el")
        '''
        self.element_wait(css)
        el = self.get_element(css)
        ActionChains(self.driver).context_click(el).perform()

    def clear(self,cls):
        self.element_wait(cls)
        el = self.get_element(cls)
        el.clear()

    def get_text(self,cls):
        self.element_wait(cls)
        el=self.get_element(cls)
        return el.text

    def get_url(self):
        return self.driver.current_url

    def switch_to_new_window(self):
        current_handle=self.driver.current_window_handle
        handles=self.driver.window_handles
        for handle in handles:
            if handle !=current_handle:
                self.driver.switch_to.window(handle)

if __name__=='__main__':
    SeEncap("chrome")