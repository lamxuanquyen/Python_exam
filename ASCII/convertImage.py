from PIL import Image
import random

pict = Image.open("ngua.jpg")
height, width = pict.size
aspect_ratio = height/width

#print(f'height: {height}px and width: {width}px')
#print(f"format: {pict.format}, size: {pict.size}, mode: {pict.mode}, name: {pict.filename}")

new_width = 240
new_height = aspect_ratio * new_width*0.5
pict = pict.resize((new_width, int(new_height)))
pict = pict.convert('L')


char_ASCII=['!','#','$','%','&','(',')','*','+',',','–','.','/',
            '0','1','2','3','4','5','6','7','8','9',':',';','<','=','>','?','@',
            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q',
            'R','S','T','U','V','W','X','Y','Z','[','^','_','`',']',
            'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
            'r','s','t','u','v','w','x','y','z','{','|','}','~','"', "'"]

random.shuffle(char_ASCII)

chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
#chars = ["i", "o", "#", "%", "!", "-", ":", ":", "&", "*", "i"]
pixels = pict.getdata()
new_pixels = [char_ASCII[pixel//25] for pixel in pixels]
new_pixels = ''.join(new_pixels)
new_pixels_count = len(new_pixels)
ascii_picture = [new_pixels[index:index+new_width]
                 for index in range(0, new_pixels_count, new_width)]
ascii_picture = "\n".join(ascii_picture)

with open('ascii_picture.txt', 'a') as file:
    file.write(ascii_picture)
