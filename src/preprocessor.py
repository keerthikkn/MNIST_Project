import numpy as np
import cv2
from PIL import Image


def process():
    
    try:
        
        img = Image.open('src\image.jpg')
        grey_img = img.convert("L")
        resized_img = grey_img.resize((28,28))
        resized_img = np.array(resized_img).flatten()

        black = np.count_nonzero(resized_img < 128)
        white = np.count_nonzero(resized_img > 128)

        if black<white:   #checking and converting to black background 
            resized_img = 255 - resized_img
            print("converted to black background")

        np_array = (resized_img)/255
        
        for i in range(len(np_array)):
                if np_array[i]<0.25:
                    np_array[i] = 0
                elif np_array[i]>0.75:
                    np_array[i] = 1
        array_2d = np.reshape(np_array, (1, -1))

        return array_2d
    
    except Exception as e:
        print(f"Error occurred at preprocessor.py --> {e}")
        