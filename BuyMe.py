import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome(executable_path='C:/Users/Eitan_Cegla/Desktop/Eitan/DevOps/Class3/chromedriver.exe')
driver.get("https://buyme.co.il/")
button_enter = driver.find_element_by_class_name("seperator-link")
button_enter.click()
# ------------------------- A. Registration Screen ------------------------------
# link_signup = driver.find_element_by_class_name("text-btn")
# link_signup.click()
name = "Robarto"
# firstName_txt = driver.find_elements_by_xpath("//input[@placeholder='שם פרטי']")
# firstName_txt[0].send_keys(name)
# mail_txt = driver.find_elements_by_xpath("//input[@placeholder='מייל']")
# mail_txt[0].send_keys("Roberto@Gonzales.com")
# pass_txt = driver.find_elements_by_xpath("//input[@placeholder='סיסמה']")
# password = "Ab345678"
# pass_txt[0].send_keys(password)
# mail_txt = driver.find_elements_by_xpath("//input[@placeholder='אימות סיסמה']")
# mail_txt[0].send_keys(password)
# driver.execute_script("arguments[0].click();", driver.find_element_by_class_name("fa-check"))
# button_signup = driver.find_element_by_class_name("ui-btn")
# button_signup.click()
# ------------------------------------------------------------------------------

# --------------------------Sign up to an existing user-------------------------
mail_txt = driver.find_elements_by_xpath("//input[@placeholder='מייל']")
mail_txt[0].send_keys("Roberto@Gonzales.com")
pass_txt = driver.find_elements_by_xpath("//input[@placeholder='סיסמה']")
password = "Ab345678"
pass_txt[0].send_keys(password)
button_signup = driver.find_element_by_class_name("ui-btn")
button_signup.click()
# ------------------------------------------------------------------------------

# -------------------------- B. Home Screen ----------------------------------------------
time.sleep(1)
amount_list = driver.find_elements_by_xpath("//*[@id='ember664_chosen']")
amount_list[0].click()
amount_selection = driver.find_elements_by_xpath("//*[@data-option-array-index='5']")
amount_selection[0].click()
area_list = driver.find_elements_by_xpath("//*[@id='ember679_chosen']")
area_list[0].click()
area_selection = driver.find_elements_by_xpath("//*[@data-option-array-index='5']")
area_selection[0].click()
category_list = driver.find_elements_by_xpath("//*[@id='ember688_chosen']")
category_list[0].click()
category_selection = driver.find_elements_by_xpath("//*[@data-option-array-index='5']")
category_selection[0].click()
present_search = driver.find_element_by_id("ember723")
present_search.click()
# ----------------------------------------------------------------------------------------

# ----------------------------- C.Choose business screen ---------------------------------
time.sleep(1)
business_selection = driver.find_elements_by_xpath("//*[@class='card-item ember-view']")
business_selection[0].click()
time.sleep(1)
price_text = driver.find_elements_by_xpath("//input[@placeholder='מה הסכום?']")
price_text[0].send_keys("500")
price_text[0].send_keys(Keys.ENTER)
# -----------------------------------------------------------------------------------------

# ----------------------------- D. Sender & Receiver information screen ----------------------------
time.sleep(1)
forsomeone_radio = driver.find_elements_by_xpath("//*[@id='ember1294']")
forsomeone_radio[0].click()
time.sleep(1)
receiver_name = driver.find_elements_by_xpath("//*[@id='ember1321']")
receiver_name[0].send_keys("Receiver")
receiver_name[0].send_keys(Keys.TAB)
sender_name = driver.find_elements_by_xpath("//*[@id='ember1323']")
sender_name[0].send_keys(name)
blessing = driver.find_elements_by_xpath("//*[@id='ember1342']")
blessing[0].send_keys("מזל טוב!!!!")
picture = driver.find_elements_by_xpath("//*[@id='ember1350']")
picture[0].send_keys('C:/Users/Eitan_Cegla/Desktop/Eitan/DevOps/hurt.jpg')
event_list = driver.find_elements_by_xpath("//*[@id='ember1325_chosen']")
event_list[0].click()
time.sleep(1)
event_selection = driver.find_elements_by_xpath("//*[@data-option-array-index='2']")
event_selection[0].click()
driver.execute_script("arguments[0].click();", driver.find_element_by_id("step-2-later-options"))
choose_mail = driver.find_elements_by_xpath("//*[@id='ember1287']/div[4]")
choose_mail[0].click()
time.sleep(1)
receiver_mail = driver.find_elements_by_xpath("//*[@placeholder='כתובת המייל של מקבל/ת המתנה']")
receiver_mail[0].send_keys("Maestro@a.com")

save_button = driver.find_element_by_class_name("btn-save")
save_button.click()
pay_button = driver.find_elements_by_xpath("//*[@id='ember1287']/div[5]/button")
pay_button[0].click()
print("github descktop test")

print("ggggg")


# ----------------------------------------------------------------------------------------------------


