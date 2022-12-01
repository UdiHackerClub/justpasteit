from selenium import webdriver
from time import sleep

myfile = open("200.txt", "r")

url = myfile.readline()

site = url
while url:
    url = myfile.readline() 

    driver = webdriver.Firefox()
    driver.get(url)
    sleep(1)

    driver.get_screenshot_as_file("screenshot.png")
    driver.quit()
    print("end...")

myfile.close()