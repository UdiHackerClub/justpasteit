from selenium import webdriver
from time import sleep
import os
import re
import os

_src = "/home/otavio/Desktop/Projects/juspasteit/"
_ext = ".png"

myfile = open("200.txt", "r")

url = myfile.readline()

while url:
    url = myfile.readline() 

    driver = webdriver.Firefox()
    driver.get(url)
    sleep(1)

    driver.get_screenshot_as_file("printou.png")
    driver.quit()
    print("renaming...")

    for i,filename in enumerate(os.listdir(_src)):
        if filename.endswith(_ext):
            os.rename(filename, _src+'Sites-' + str(i).zfill(3)+_ext)

myfile.close()
