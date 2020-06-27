from PIL import Image,ImageFilter

img =Image.open('Images/4.4 pikachu.jpg')
filtered_img =img.filter(ImageFilter.BLUR)
filtered_img2 =img.convert('L')
rotate_img = img.rotate(90)
resize_img = img.resize((300,300))

print(img)
print(img.format)
print(img.size)
print(img.mode)

print(dir(img))
#in this we need to use png format rather than using jpg
#because the ImageFilter supports png format
filtered_img.save("blur.png")
filtered_img2.save("gray.png",'png')
filtered_img2.show()
rotate_img.show()
resize_img.show()


