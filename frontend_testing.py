from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
user_id = 62

def frontend_test(user_id):
    driver = webdriver.Chrome(service=Service("C:\temp\chromedriver.exe"))

    driver.get('http://127.0.0.1:5001/users/get_user_name/' + str(user_id))
    user = driver.find_element(By.ID, "user")
    return (user.text)
    driver.quit()

user_name = frontend_test(str(user_id))
print (user_name)