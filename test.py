from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import requests
import os
import time

# setup the webdriver
service = Service(executable_path='C:/Users/Visa/Dropbox/Document In The US/Etsy/python_code/chromedriver.exe')  # point this to your ChromeDriver location
driver = webdriver.Chrome(service=service)

driver.get('https://www.aliexpress.us/item/3256804709361506.html')

time.sleep(15)

# execute the script to get the image paths 
urls = driver.execute_script("return window.runParams.data.imageModule.imagePathList")

# define the directory for storing images
img_dir = os.path.join(os.getcwd(),'hook1')  # update this to your desired path

for i in urls:
    print(i)

for i, url in enumerate(urls):
    response = requests.get(url, stream=True)
    with open(os.path.join(img_dir, f'image_{i}.jpg'), 'wb') as out_file:
        out_file.write(response.content)
    print(f"Downloaded image_{i}.jpg")

driver.quit()
