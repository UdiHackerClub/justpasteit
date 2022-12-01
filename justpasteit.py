import random
from random import randint
import requests
import time

links = 0
while links < 100:
    randomnumber = (randint(0,99999))
    link = "https://justpaste.it/"
    valid = link + str(randomnumber)
    
    print (randomnumber)
    
    response = requests.get(valid, headers = {'User-agent': 'your bot 0.1'})
    
    print(response.url)
    print(response.status_code)

    links = links + 1
    print("=========" + str(links) + "=========")

    if response.status_code == 200:
        file = open('200.txt', 'a')
        file.write(response.url + "\n")
        file.close()
        time.sleep(2)
        pass
    if response.status_code == 404:
        file = open('400.txt', 'a')
        file.write(response.url + "\n")
        file.close()
        time.sleep(2)
        pass

    if response.status_code == 451:
        file = open('451blocked.txt', 'a')
        file.write(response.url + "\n")
        file.close()
        time.sleep(2)
        pass

    if response.status_code == 429:
        file = open('retry.txt', 'a')
        file.write(response.url + "\n")
        file.close()
        time.sleep(2)
        pass      

    pass