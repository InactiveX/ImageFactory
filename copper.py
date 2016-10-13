import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import os
import string
import sys
import settings as s

def Copyrighter (im):
    im1=s.TBP_DIR + im
    font = ImageFont.truetype('miso-bold.otf', 100)
    img = Image.open(im1)
    draw = ImageDraw.Draw(img)
    draw.text((450, 550), "Jenny Woolley Photography", (255, 238, 147), font=font)

    try:
        img.save(s.OK_DIR + 'JW-'+ im)
        # archive
        img.save(s.ARC_DIR + 'JW-' + im)
        #optimsed
        img.save(s.OK_DIR + 'OPT-' + im, optimize = True, progressive = True)
        #now the thumbnail
        size = (86, 86)
        img.thumbnail(size, Image.ANTIALIAS)
        img.save(s.OK_DIR + 'TH-' + im)
        im1='Success !'
    except IOError:
        print ('Error saving ' + im)
        im1 = im + ' failed with I/O Error. Is this an image file?'
    return im1

dirs = s.TBP_DIR



for file in os.listdir(s.TBP_DIR):
    print(file)
    print('Copyrighting ' + Copyrighter(file))
