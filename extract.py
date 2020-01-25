from PIL import Image
import pytesseract
import pandas as pd

masterlist = []


im = Image.open('flyer_images/week_1_page_1.jpg')
text = pytesseract.image_to_string(im)
text.split()
print(text)



'''
for week in range(1, 53, 1):
    for page in range(1, 5, 1):
        im = Image.open('flyer_images/week_'+str(week)+'_page_'+str(page)+'.jpg')
        text = pytesseract.image_to_string(im)
        masterlist += [[text]]
'''

data = pd.DataFrame({'flyer_name', 'product_name', 'unit_promo_price', 'uom', 'least_unit_for_promo', 'save_per_unit', 'discount', 'organic'})

print(data)