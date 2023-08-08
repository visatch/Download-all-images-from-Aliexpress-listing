import selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from typing import List
import argparse
import requests
import os
import time
from main import createDirectoryOrEmptyIt

def temu_download_all_thumbnails_pictures(url: str, directoryName:str) -> List[str]:
    chrome_options = Options()
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

    chrome_options.add_argument(f"user-agent={USER_AGENT}")  
    # chrome_options.add_argument("--headless")
    #visashopping1711@gmail.com

    service = Service(executable_path='C:/Users/Visa/Dropbox/Document In The US/Etsy/python_code/chromedriver.exe')  # point this to your ChromeDriver location
    driver = selenium.webdriver.Chrome(service=service, options=chrome_options)

    driver.get(url)

    time.sleep(25)

    results = driver.find_element(By.CLASS_NAME, "_2AOclWz7").find_elements(By.TAG_NAME, "img")
    list_of_url = []

    for i in results:
        each_url = i.get_attribute("src") or i.get_attribute("data-src")
        
        for extension in [".jpg", ".jpeg"]:
            if extension in each_url:
                each_url = each_url.split(extension, 1)[0] + extension
                break

        list_of_url.append(each_url)

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
    parser = argparse.ArgumentParser(description="Download all images from Aliexpress")
    parser.add_argument("--url",type=str, help="URL of the product")
    parser.add_argument("--directory",type=str, help="The directory that image will be stored")

    args = parser.parse_args()
    
    if not args.url or not args.directory:
        parser.error("url and directory cannot be empty")

    temu_download_all_thumbnails_pictures(args.url,args.directory)
