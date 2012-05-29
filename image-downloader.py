import urllib2

image_path = raw_input("path of the images: ")
image_prefix = raw_input("prefix of the images: ")
dir_downloads = raw_input("choose a directory from your computer: ")
    
counter = 1

try:
    while True:
        image_name = image_prefix + str(counter).zfill(2) + '.jpg'
        image_source = image_path + "/" + image_name
        
        print "downloading image: " + image_source
        
        link = urllib2.urlopen(image_source).read()
        
        if link.startswith('404'):
            print "The image doesn't exists."
            break
        
       	image_destiny = dir_downloads + '/' + image_name
        
        f = open(image_destiny, 'wb')
        f.write(link)
        f.close()
        
        counter += 1

except IOError:
    print "No such file or directory named: " + image_destiny
except:
    print "The image could not be downloaded."


