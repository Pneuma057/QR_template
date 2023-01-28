import qrcode
from PIL import Image

Q1 = input ("Please insert the url:")
image= qrcode.make(Q1)

image_name = input("Please insert a image name:") +'.png'
image_file = open(image_name,"wb")
image.save(image_file)
image_file.close()

image_root = './'+ image_name
Image.open(image_root).show()
