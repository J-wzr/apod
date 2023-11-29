import requests
import streamlit as st
FILEPATH = "image.jpg"


api_key = "7ATjHlwLLoQGZxfpEWQlu38aKJYtNZkkR7NCBTWt"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"


# getting all the content and bundling it into a python dictionary
response = requests.get(url)
content = response.json()


# extracting specific fields
title = content["title"]
description = content["explanation"]
image_address = content["url"]

# downloading the image
image = requests.get(image_address)
with open(FILEPATH, "wb") as file:
    file.write(image.content)

# displaying the image on the web page
st.set_page_config("Astronomy Picture of the Day",
                   "blackFavicon.png")
st.balloons()
st.header(title)
st.text("An application that shows the astronomy picture of the day.")
st.image(FILEPATH)
st.write(description)