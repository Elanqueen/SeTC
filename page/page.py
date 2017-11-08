class pageLogin:
    cardid=[By.ID,'loginform-username']
    password=[By.ID,'loginform-password']
    remember_me=[By.ID,'loginform-rememberme']
    submit=[By.NAME,'login-button']

class pageLostPassword:
    lost_pw=[By.Id,'']
    
class pageSearch:
    select_catogery=[By.TAG_NAME,'select']
    value_title=[By.ID,'scope_title1']
    value_creator=[By.ID,'scope_creator1']
    txt=[By.NAME,'vl(freeText0)']
    button=[By.LINK_TEXT,'高级检索']
   # content_catogery=[]