# Kamera Sensor Modul
import numpy as np
import cv2
import conf

cam = cv2.VideoCapture(0)

 
def lineDetection():
    # Capture the frames
    ret, img = cam.read()

    # Crop the image
    img = cv2.resize(img, (340, 220))
    img = img[conf.camCropLT[0]:conf.camCropLT[1], conf.camCropLT[2]:conf.camCropLT[3]]

    # Convert to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Gaussian blur
    blur = cv2.GaussianBlur(img_gray,(5,5),0)

    # Color thresholding
    ret,thresh = cv2.threshold(blur,60,255,cv2.THRESH_BINARY_INV)

    # Find the contours of the frame
    _,contours,h = cv2.findContours(thresh.copy(), 1, cv2.CHAIN_APPROX_NONE)

    # Find the biggest contour (if detected)
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        M = cv2.moments(c)

        try:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])

        except ZeroDivisionError:
            return False
            
        cv2.line(img,(cx,0),(cx,720),(255,0,0),1)
        cv2.line(img,(0,cy),(1280,cy),(255,0,0),1)
        cv2.drawContours(img, contours, -1, (0,255,0), 1)
        cdiff = int(cx-70)
        linecoord = [cx,cy,cdiff]

        if conf.debug:
            print("LineDetection:{}".format(linecoord))
            
        return linecoord


def objectDetection():
    kernelOpen=np.ones((5,5))
    kernelClose=np.ones((20,20))

    lowerBound=np.array([conf.camColorLB[0],conf.camColorLB[1],conf.camColorLB[2]])
    upperBound=np.array([conf.camColorUB[0],conf.camColorUB[1],conf.camColorUB[2]])

    obstacles = dict()
    ocount = 0

    for j in range(9):
        ret, img=cam.read()
        img=cv2.resize(img,(340,220))

    #convert BGR to HSV
    imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    # create the Mask
    mask=cv2.inRange(imgHSV,lowerBound,upperBound)
    #morphology
    maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
    maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)

    maskFinal=maskClose
    _,conts,h=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    
    cv2.drawContours(img,conts,-1,(255,0,0),3)
   
    for i in range(len(conts)):
        x,y,w,h=cv2.boundingRect(conts[i])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255), 2)
        contdim = [x,y,w,h]
        obstacles[ocount]=contdim
        ocount += 1
                
    if conf.debug:
        print("ObjectDetection:{}".format(obstacles))

    return obstacles
