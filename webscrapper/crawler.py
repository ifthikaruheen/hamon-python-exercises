import requests
from bs4 import BeautifulSoup
import os
import urllib.request
from urllib.parse import urlparse, urljoin

def download_images(url):
    # Send an HTTP GET request to the URL
    # url = 'https://media.gettyimages.com/photos/indian-actor-amir-khan-1988-picture-id499342585?k=6&m=499342585&s=612x612&w=0&h=4jP2Zn9qP_R5kN8NpOwTTCDBO2SEVeqfZDcF0VebaKw='
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}

    response = requests.get(url, headers=headers)

    if response.status_code==200:
        soup =  BeautifulSoup(response.text, 'html.parser')
        image_tags=soup.find_all('img')
        count=0
        for image_tag in image_tags:
            img_url = image_tag.get('src')
            if img_url:
                if "s=2048x2048" not in img_url:
                    img_filename = os.path.basename(urlparse(img_url).path)
                    img_path = os.path.join("images", img_filename)
                    if not os.path.exists("images"):
                        os.mkdir("images")
                try: 
                    urllib.request.urlretrieve(img_url, img_path)
                    count+=1
                    print(f"Downloaded {count}th file: {img_filename}")
                except Exception as e:
                    print(f"Failed to download {img_filename}: {str(e)}")            
    else:
         print(f"Failed to retrieve data. Status code: {response.status_code}")     

download_images('https://www.gettyimages.in/photos/aamir-khan-actor')
