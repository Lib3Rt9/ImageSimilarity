import os
from PIL import Image

folder_path = r"C:\Users\FLOS IGNIS\OneDrive\Máy tính\Desktop Background"
width = 426  # replace with your desired width
height = 240  # replace with your desired height

for filename in os.listdir(folder_path):
    if filename.endswith(('.jpg', '.png', '.gif', '.bmp', '.tiff')):  # add more formats if you want
        img_path = os.path.join(folder_path, filename)
        img = Image.open(img_path)
        resized_img = img.resize((width, height))
        resized_img.save(img_path[:-4] + '_resized.jpg')  # save the resized image
        os.remove(img_path)  # delete the original image
