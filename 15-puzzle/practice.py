from PIL import Image
 

im = Image.open("test.png")
 
width, height = im.size

PIXEL_SIZE = 128



count = 1
for i in range(4):
    for j in range(4):
        left = i*PIXEL_SIZE
        right = left + PIXEL_SIZE
        top = j*PIXEL_SIZE
        bottom = top + PIXEL_SIZE
        print(left,top,right,bottom)
        # image = im.crop((left,top,right,bottom))
        # image.save(f'test{count}.png')
        count += 1        
