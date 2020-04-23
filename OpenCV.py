import cv2
#for the scan the image the path of the image should give with the two \\
#1 means cloured image
img = cv2.imread("C:\\Users\\Pasindu Thiwanka\\Desktop\\a.jpg",1)
print(img)
print(img.shape)
print(type(img))

#0 means black and white
img = cv2.imread("C:\\Users\\Pasindu Thiwanka\\Desktop\\a.jpg",0)
print(img)