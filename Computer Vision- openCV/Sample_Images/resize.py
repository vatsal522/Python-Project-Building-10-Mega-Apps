import cv2
import glob #finds the pathname with a certain pattern.

images=glob.glob("*.jpg")

for x in images:
    img=cv2.imread(x,0) #0 because it'll read the img in black and white
    re=cv2.resize(img,(100,100))
    cv2.imshow("Hey",re)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+x,re)
