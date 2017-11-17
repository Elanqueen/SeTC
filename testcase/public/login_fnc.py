#coding = utf-8

import os,sys
root_path = os.path.abspath(os.path.dirname(os.path.dirname(os.getcwd())))
print(root_path)
sys.path.append(os.path.abspath(os.path.join(root_path,'page')))

from page import pageLogin

def login(self,username,password):
    driver = self
    element=driver.find_element(pageLogin.cardid[0],pageLogin.cardid[1])
    element.clear()
    element.send_keys(username)
    element = driver.find_element(pageLogin.password[0],pageLogin.password[1])
    element.clear()
    element.send_keys(password)
    driver.find_element(pageLogin.submit[0],pageLogin.submit[1]).click()


'''
def logout_fnc(self):
    driver=self.driver
    driver
    
  '''  
