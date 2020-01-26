import cv2

def main():

    # Run SplitFlyer on all flyer images
    for week in range(1, 2, 1):
        for page in range(1, 5, 1):
            SplitFlyer(week, page)

    return True


def SplitFlyer(week, page):

    # Path to flyer and read in image using CV
    path = 'flyer_images/week_'+str(week)+'_page_'+str(page)+'.jpg'
    image = cv2.imread(path)

    # Apply grayscale and blurgit 
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(image_gray, (7,7), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Dilate image
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
    dilate = cv2.dilate(thresh, kernel, iterations=8)

    # Find contours
    contours = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]

    # To draw contours on entire flyer page
    for c in contours:
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(image, (x, y), (x + w, y + h), (36, 255, 12), 2)

    # Break up flyer into individual segments and save to flyer_split directory
    for c in range(len(contours)):
        x, y, width, height = cv2.boundingRect(contours[c])
        roi = image[y:y+height, x:x+width]
        cv2.imwrite("flyer_split/week_"+str(week)+"_page_"+str(page)+"_item"+str(c)+".jpeg", roi)

    return True

main()