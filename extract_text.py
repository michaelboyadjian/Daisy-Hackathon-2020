from PIL import Image
import pytesseract
import pandas as pd
import numpy as np
import cv2
import os
import time
import re
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def main():

    items = pd.read_csv('product_dictionary.csv')
    units = pd.read_csv('units_dictionary.csv')

    ItemList = items['product_name'].tolist()
    UnitList = units['units'].tolist()

    # Create pandas dataframe
    df = pd.DataFrame(columns=['flyer_name','product_name','unit_promo_price','uom','least_unit_for_promo ','save_per_unit', 'discount','organic'] )   

    # Iterate through all images
    for filename in os.listdir('flyer_split'):

        if filename.endswith('.jpeg'):
            path = "flyer_split/" + filename
            im = Image.open("flyer_split/" + filename)

            # Extract text using pytesserect
            text = pytesseract.image_to_string(im)

            if text:

                # Create dataframe entry
                entry = ['', '', '', '', 1, '', '', 0]

                # Format the flyer name
                if filename[6] != '_':
                    entry[0] = filename[0:14]
                else:
                    entry[0] = filename[0:13]

                # Check Product Name
                ratios = []
                for i in ItemList:
                    ratios += [fuzz.ratio(i, text)]
                index = ratios.index(max(ratios))
                entry[1] = ItemList[index]
                ItemList.remove(ItemList[index])

                # Check Unit of Measure
                ratios = []
                for i in UnitList:
                    if " " + i + " " in text:
                        entry[3] = i


                # Check discount amount
                if 'SAVE' in text:
                    loc = text.find('SAVE')
                    substring = text[loc+4 : loc+15]
                    substring = re.sub(r"\s+", "", substring, flags=re.UNICODE)
                    if 'on' in substring:
                        onloc = substring.find("on")
                        try: 
                            entry[5] = "%.2f" % round(float(substring[1:onloc])/float(substring[onloc+2]), 2 )
                            entry[4] = int(substring[onloc+2])
                        except: continue
                    elif '/' in substring:
                        dashloc = substring.find("/")
                        try:
                            entry[5] = "%.2f" % round(float(substring[1:dashloc]), 2)
                        except: continue


                # Check if product is organic
                if 'ORGANIC' in text:
                    entry[7] = 1

                print(entry)
                df.loc[len(df)] = entry
 
    print(df)

    return True


main()