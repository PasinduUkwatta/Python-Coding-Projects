from PIL import Image,ImageFilter

img =Image.open('Images/6.1 astro.jpg')

#this will help to resize the image without the crompessing
img.thumbnail((200,200))

img.save("thumnail.jpg")