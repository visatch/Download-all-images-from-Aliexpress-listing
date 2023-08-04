import selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from typing import List
import requests
import os
import time
from main import createDirectoryOrEmptyIt

def aliexpress_download_all_thumbnails_pictures(url: str, directoryName:str) -> List[str]:
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    service = Service(executable_path='C:/Users/Visa/Dropbox/Document In The US/Etsy/python_code/chromedriver.exe')  # point this to your ChromeDriver location
    driver = selenium.webdriver.Chrome(service=service, options=chrome_options)

    driver.get(url)

    time.sleep(10)

    results = driver.find_element(By.CLASS_NAME, "images-view-wrap").find_elements(By.TAG_NAME, "li")

    list_of_url = []

    for i in results:
        each_url = i.find_element(By.TAG_NAME, "img").get_attribute("src")
        list_of_url.append(each_url[:each_url.find(".jpg")+4])

    driver.quit()

    # define the directory for storing images
    img_dir = os.path.join(os.getcwd(),directoryName)  

    # Check if directory exist or not -> if exist -> Empty it otherwise create it
    createDirectoryOrEmptyIt(img_dir)

    for i, url in enumerate(list_of_url):
        response = requests.get(url, stream=True)
        with open(os.path.join(img_dir, f'image_{i}.jpg'), 'wb') as out_file:
            out_file.write(response.content)
        print(f"Downloaded image_{i}.jpg")



if __name__ == "__main__":
    aliexpress_download_all_thumbnails_pictures("https://www.aliexpress.us/item/3256803583930760.html","Cat Paw Scissors")
# src="https://ae01.alicdn.com/kf/Sacedac4293a34fe69a33930cb6c74132R/Cute-Multifunctional-Stainless-Steel-Hand-Scissors-Mini-Portable-Kawaii-Cat-Paw-Art-Scissors-School-Stationery-Novelty.jpg_220x220.jpg_.webp"

# print(src[:src.find(".jpg")+4])
