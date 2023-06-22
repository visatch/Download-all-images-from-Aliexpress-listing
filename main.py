from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import argparse
import requests
import os
import time
import shutil

def download_all_images(url, directoryName):
    #Selenium v4+ must be used Service
    service = Service(executable_path='C:/Users/Visa/Dropbox/Document In The US/Etsy/python_code/chromedriver.exe')  # point this to your ChromeDriver location
    driver = webdriver.Chrome(service=service)

    driver.get(url)

    #Wait for content to load 
    time.sleep(10)

    # execute the script to get the image paths 
    urls = driver.execute_script("return window.runParams.data.imageModule.imagePathList")

    # define the directory for storing images
    img_dir = os.path.join(os.getcwd(),directoryName)  

    # Check if directory exist or not -> if exist -> Empty it otherwise create it
    createDirectoryOrEmptyIt(img_dir)

    for i, url in enumerate(urls):
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
    parser.add_argument("--url", help="URL of the product")
    parser.add_argument("--directory", help="The directory that image will be stored")
    
    args = parser.parse_args()
    download_all_images(args.url,args.directory)