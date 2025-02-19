import os

import requests
from bs4 import BeautifulSoup

# URL of the webpage
URL = "www.example.com"

# Send a request to fetch the webpage content
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

# Find the first image tag
img_tag = soup.find("img")

# Extract image URL
if img_tag and "src" in img_tag.attrs:
    img_url = img_tag["src"]

    # If the URL is relative, make it absolute
    if img_url.startswith("//"):
        img_url = "https:" + img_url
    elif img_url.startswith("/"):
        img_url = URL + img_url

    # Get the image content
    img_response = requests.get(img_url)

    # Save the image
    img_name = os.path.basename(img_url)  # Get image filename
    with open(img_name, "wb") as file:
        file.write(img_response.content)

    print(f"Image downloaded as {img_name}")
else:
    print("No image found on the page.")
