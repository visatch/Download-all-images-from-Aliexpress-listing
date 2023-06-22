import requests
import os

# list of image URLs
urls = ['https://ae01.alicdn.com/kf/S886a060177ca4ea28d25c433bc3745eeX/Creative-Cute-Animal-Squirrel-Hook-Adhesive-Sticker-Key-Storage-Door-Wall-Kitchen-Bedroom-Storage-Funny-Gift.jpg',
        'https://ae01.alicdn.com/kf/Sb201ac4097854ce7a8139fec801bfd5fG/Creative-Cute-Animal-Squirrel-Hook-Adhesive-Sticker-Key-Storage-Door-Wall-Kitchen-Bedroom-Storage-Funny-Gift.jpg',
        'https://ae01.alicdn.com/kf/S6e1cd510fbb94a18b19e88fd263ba69eT/Creative-Cute-Animal-Squirrel-Hook-Adhesive-Sticker-Key-Storage-Door-Wall-Kitchen-Bedroom-Storage-Funny-Gift.jpg',
        'https://ae01.alicdn.com/kf/S8b026a7e2db945f4aeab24259d8c4ba70/Creative-Cute-Animal-Squirrel-Hook-Adhesive-Sticker-Key-Storage-Door-Wall-Kitchen-Bedroom-Storage-Funny-Gift.jpg',
        'https://ae01.alicdn.com/kf/S330e7b96799c4775805b5dcc91d073f9w/Creative-Cute-Animal-Squirrel-Hook-Adhesive-Sticker-Key-Storage-Door-Wall-Kitchen-Bedroom-Storage-Funny-Gift.jpg',
        'https://ae01.alicdn.com/kf/Sf76498baf56e4227801e8d782a874b10b/Creative-Cute-Animal-Squirrel-Hook-Adhesive-Sticker-Key-Storage-Door-Wall-Kitchen-Bedroom-Storage-Funny-Gift.jpg']

# define the directory for storing images
img_dir = os.path.join(os.getcwd(),'hook')  # update this to your desired path

for i, url in enumerate(urls):
    response = requests.get(url, stream=True)
    with open(os.path.join(img_dir, f'image_{i}.jpg'), 'wb') as out_file:
        out_file.write(response.content)
    print(f"Downloaded image_{i}.jpg")
