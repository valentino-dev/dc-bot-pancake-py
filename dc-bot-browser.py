from selenium import webdriver
import time
import random

password = "ubicornbugedibug"
email = "servus.dei.34@gmail.com"


def sendkeys(message, destination):
    for char in message:
        time.sleep(random.random()*0.2)
        destination.send_keys(char)

driver = webdriver.Firefox()
driver.get("https://discord.com/channels/456446844768354306/762750490432897024")

email_field = driver.find_element_by_name("email")
time.sleep(random.random()*2)
sendkeys(email, email_field)

password_field = driver.find_element_by_name("password")
time.sleep(random.random()*2)
sendkeys(password, password_field)

time.sleep(random.random()*2)

password_field.submit()


text_field = driver.finde("placeholder-37qJjk fontSize16Padding-3Wk7zP")
text_field.click
text_field.send_keys("test")
time.sleep(5)
driver.quit()