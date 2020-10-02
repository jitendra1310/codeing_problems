from PIL import Image

mac = Image.open('/var/www/html/udemy/python/Imges/example.jpg','r')
mac.crop((0,0,100,100)).show()
pencils = Image.open('/var/www/html/udemy/python/Imges/pencils.jpg','r')
#mac.show()