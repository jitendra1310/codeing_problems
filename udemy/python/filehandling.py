import os,shutil,send2trash

#print(os.getcwd())
#print(os.listdir("/var/www/html/udemy"))
shutil.move("pa.txt","/var/www/html/udemy/")

""" 
#wrire a file 
f = open("pa.txt",'w+')
f.write("This is test stiring") 
f.close() """