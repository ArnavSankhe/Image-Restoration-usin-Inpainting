import cv2
import matplotlib.pyplot as plt
import numpy as np 

def main():

    frame=cv2.imread("Inked4.2.01_LI.jpg")
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    lower_red = np.array([110,50,50]) 
    upper_red = np.array([130,255,255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame, mask= mask) 
    cv2.imshow('frame',frame) 
    cv2.imshow('mask',mask) 
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
       # cv2.waitKey(0)		 

    # Destroying present windows on screen 
    #path ="C:\Users\ARNAV\Desktop\dsp\Python-OpenCV3-master\Dataset"
    imgpath =   "Inked4.2.01_LI.jpg"
    #maskpath =  "Mask.tiff"
    img = cv2.imread(imgpath, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    #mask= cv2.imread(maskpath, 0)
    
    output1 = cv2.inpaint(img, mask, 500, cv2.INPAINT_TELEA)
    
    output2 = cv2.inpaint(img, mask, 500, cv2.INPAINT_NS)

    output = [img, mask, output1, output2]
    titles = ['Damaged Image', 'Mask', 'TELEA', 'NS']
    
    
    for i in range(4):
        plt.subplot(2, 2, i+1)
        if i == 1:
            plt.imshow(output[i], cmap='gray')
        else:
            plt.imshow(output[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()
    cv2.destroyAllWindows() 
if __name__ == "__main__":
    main()



