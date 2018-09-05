import urllib
import urllib.request
from bs4 import BeautifulSoup
import os
from PIL import Image 
i=1
url = input('Enter website url : ')

##images will be stored here,change location according to your liking
os.chdir('C:/Users/Bhavyom/Desktop/TestPython')

try:

    page = urllib.request.urlopen(url)
##if url is itself an image
    if url.split('.')[len(url.split('.'))-1] in ('png','jpeg','jpg'):
        filename = str(i)
        i=i+1
        imagefile = open(filename + ".jpg","wb")
        imagefile.write(urllib.request.urlopen(url).read())
        imagefile.close()
        print('Saved Successufully')
    else :
##if url contain alot of images        
        soup = BeautifulSoup(page,"html.parser")
    
        
        for img in soup.findAll('img'):
            temp = img.get('src')
    
            if temp[:5] not in ('http:','https'):
                imageUrl = url + temp
            else :
                imageUrl = temp
            print(imageUrl)
            filename = str(i)
            i=i+1
    
            imagefile = open(filename + ".jpg","wb")
            imagefile.write(urllib.request.urlopen(imageUrl).read())
            imagefile.close()
            print('Saved Successufully')

##image filter,for filtering images with width and height less than 500px            
    for item1 in os.listdir():    
        with Image.open(item1) as image1:
            width,height = image1.size
            image1.close()
            if width>=500 and height>=500:
                pass
            else:
                os.remove(item1)
                print(item1 + ' Removed Successfully')

except Exception as e:
    print(e)
    

