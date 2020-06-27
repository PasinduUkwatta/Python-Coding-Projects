from PIL import Image,ImageFilter

img = Image.open('Images/6.1 astro.jpg')
print(img.size)

resize_img = img.resize((400 ,400))
print(resize_img.size)
resize_img.show()
resize_img.save("tumbnail.jpg")
