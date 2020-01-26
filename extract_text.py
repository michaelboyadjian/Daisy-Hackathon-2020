from PIL import Image
import pytesseract
import pandas as pd
import numpy as np
import cv2
import os
import time

def main():

    df = pd.DataFrame(columns=['flyer_name','product_name','unit_promo_price','uom','least_unit_for_promo ','save_per_unit', 'discount','organic'] )   

    for filename in os.listdir('flyer_split'):
        if filename.endswith('.jpeg'):
            path = "flyer_split/" + filename
            im = Image.open("flyer_split/" + filename)
            text = pytesseract.image_to_string(im)

            if text:
                #print(text)
                #print("############################")
                entry = ['', '', '', '', 1, '', '', 0]
                if filename[6] != '_':
                    entry[0] = filename[0:14]
                else:
                    entry[0] = filename[0:13]



                if 'ORGANIC' in text:
                    entry[7] = 1

                df.loc[len(df)] = entry
 
    print(df)

    return True


main()