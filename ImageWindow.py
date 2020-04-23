import cv2

img = cv2.imread("C:\\Users\\Pasindu Thiwanka\\Desktop\\a.jpg",1)
cv2.imshow("stat class",img)

resize = cv2.resize(img,(600,600))
cv2.imshow("stat class",resize)
#0 means when user press any key ,th window will closed
#when we give a time in the brackets in ms, it will automatically disspera after the time
cv2.waitKey(0)

cv2.destroyAllWindows()