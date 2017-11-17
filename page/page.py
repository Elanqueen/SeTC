#! /usr/bin/env python
#coding=utf-8

from selenium.webdriver.common.by import By

class pageLogin:
    cardid=[By.ID,'loginform-username']
    password=[By.ID,'loginform-password']
    remember_me=[By.ID,'loginform-rememberme']
    submit=[By.NAME,'login-button']

#class pageLostPassword:
 #   lost_pw=[By.ID,'']
    
class pageSearch:
    select_catogery=[By.TAG_NAME,'select']
    value_title=[By.ID,'scope_title1']
    value_creator=[By.ID,'scope_creator1']
    txt=[By.NAME,'vl(freeText0)']
    button=[By.LINK_TEXT,'高级检索']
    ggjs=[By.XPATH,'html/body/div[2]/div/div[1]/div[2]/form/div[1]/div[1]/div[2]/div/div/button']
   # content_catogery=[]