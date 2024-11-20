import os
from PIL import Image

folder_path = r"C:\Users\FLOS IGNIS\OneDrive\Máy tính\Desktop Background"

for filename in os.listdir(folder_path):
    if filename.endswith(('.png', '.jpeg', '.gif', '.bmp', '.tiff', '.jfif')):  # add more formats if you want
        img_path = os.path.join(folder_path, filename)
        img = Image.open(img_path)
        rgb_img = img.convert('RGB')
        rgb_img.save(img_path[:-4] + '.jpg')
        os.remove(img_path)  # delete the old image
