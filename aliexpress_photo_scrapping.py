from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
import argparse
import requests
import os
import time
import shutil

# No longer works
# def download_all_images_by_excecuting_the_script(url, directoryName):
#     #set chrome options
#     chrome_options = Options()
#     # chrome_options.add_argument("--headless")

#     #Selenium v4+ must be used Service
#     service = Service(executable_path='chromedriver.exe')  # point this to your ChromeDriver location
#     driver = webdriver.Chrome(service=service, options=chrome_options)

#     driver.get(url)

#     #Wait for content to load 
#     time.sleep(10)

#     # execute the script to get the image paths 
#     urls = driver.execute_script("return window.runParams.data.imageModule.imagePathList")

#     # define the directory for storing images
#     img_dir = os.path.join(os.getcwd(),directoryName)  

#     # Check if directory exist or not -> if exist -> Empty it otherwise create it
#     createDirectoryOrEmptyIt(img_dir)

#     for i, url in enumerate(urls):
#         response = requests.get(url, stream=True)
#         with open(os.path.join(img_dir, f'image_{i}.jpg'), 'wb') as out_file:
#             out_file.write(response.content)
#         print(f"Downloaded image_{i}.jpg")

#     driver.quit()  

def download_all_images_by_scrapping(url, directoryName):
    def trim_url(url):
        index = url.find(".jpg")
        if index != -1:
            return url[:index+4]
        
    #set chrome options
    chrome_options = Options()
    # chrome_options.add_argument("--headless")

    # setup the webdriver
    service = Service(executable_path='chromedriver.exe')  # point this to your ChromeDriver location
    driver = webdriver.Chrome(service=service,options=chrome_options)
    driver.implicitly_wait(5)

    driver.get(url)

    time.sleep(5)

    title = driver.find_element(By.XPATH, "//h1[@data-pl='product-title']").text

    content = driver.find_element(By.CLASS_NAME,'pdp-info-left')
    imgs = content.find_elements(By.TAG_NAME, "img")
    # imgs = content.find_elements(By.TAG_NAME, "li")

    imgs_url = []
    for i in imgs:
        img_url = trim_url(i.get_attribute('src'))
        imgs_url.append(img_url)

    print(imgs_url)

    # define the directory for storing images
    img_dir = os.path.join(os.getcwd(),os.path.join(directoryName,title))  

    # Check if directory exist or not -> if exist -> Empty it otherwise create it
    createDirectoryOrEmptyIt(img_dir)

    for i, url in enumerate(imgs_url):
        response = requests.get(url, stream=True)
        with open(os.path.join(img_dir, f'image_{i}.jpg'), 'wb') as out_file:
            out_file.write(response.content)
        print(f"Downloaded image_{i}.jpg")

    driver.quit()

def createDirectoryOrEmptyIt(directory):
    path_to_directory = os.path.join(os.getcwd(),directory)
    if not os.path.exists(path_to_directory):
        os.makedirs(path_to_directory)
    else:
        for filename in os.listdir(path_to_directory):
            file_path = os.path.join(path_to_directory,filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (file_path,e))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download all images from Aliexpress")
    parser.add_argument("--url",type=str, help="URL of the product")
    parser.add_argument("--directory",type=str, help="The directory that image will be stored")

    args = parser.parse_args()
    
    if not args.url or not args.directory:
        parser.error("url and directory cannot be empty")

    download_all_images_by_scrapping(args.url,args.directory)