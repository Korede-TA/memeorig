# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 02:17:15 2018

@author: Ebere
"""

# upload.py
import os
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

app = ClarifaiApp(api_key='e0d74bb523d14cdcbb1903b266ac83af')
# Counter variables
current_batch = 0
counter = 0
batch_size = 32

images = [url for url in s for s in imgsearch()]
row_count = len(images)
print("Total number of images:", row_count)
while(counter < row_count):
    print("Processing batch: #", (current_batch+1))
    imageList = []
    for current_index in range(counter, counter+batch_size - 1):
        try:
            imageList.append(ClImage(url=images[current_index]))
        except IndexError:
            break
    app.inputs.bulk_create_images(imageList)
    counter = counter + batch_size
    current_batch = current_batch + 1
