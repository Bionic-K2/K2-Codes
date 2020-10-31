from PIL import ImageSequence
from PIL import Image
import os

path = os.getcwd()
gifnames = []
for i in os.listdir(path):
    if os.path.splitext(i)[1] == '.gif':
        gifnames.append(os.path.splitext(i)[0])

def createPNG(gifname):
    png_x = 0
    png_y = 0
    trans_pic = False
    trans_x_min = 10000
    trans_x_max = 0
    trans_y_min = 10000
    trans_y_max = 0
    gif = Image.open(gifname+'.gif')
    for i, frame in enumerate(ImageSequence.Iterator(gif), 0):
        png_x += frame.size[0]
        png_y = frame.size[1]

    png = Image.new("RGBA", (png_x, png_y), "#00FF00")
    for i, frame in enumerate(ImageSequence.Iterator(gif), 0):
        frame = frame.convert('RGBA')
        trans_pic = False
        trans_x_min = 10000
        trans_x_max = 0
        trans_y_min = 10000
        trans_y_max = 0
        # 第一轮：获取透明区域并染色
        for yh in range(frame.size[1]):
            for xw in range(frame.size[0]):
                dot = (xw, yh)
                color_d = frame.getpixel(dot)
                if color_d[3] == 0:
                    trans_pic = True
                    if xw >= trans_x_max:
                        trans_x_max = xw
                    if xw <= trans_x_min:
                        trans_x_min = xw
                    if yh >= trans_y_max:
                        trans_y_max = yh
                    if yh <= trans_y_min:
                        trans_y_min = yh

        # 第二轮：清除所有透明域以外的区域
        for yh in range(frame.size[1]):
            for xw in range(frame.size[0]):
                dot = (xw, yh)
                if (xw < trans_x_min or xw > trans_x_max or yh < trans_y_min or yh > trans_y_max) and trans_pic == True:
                    color_d = (0, 0, 0, 0)
                    frame.putpixel(dot, color_d)
        png.paste(frame, ((i*frame.size[0]), 0), None)
    png.save(gifname+'.png', 'png')

for i in gifnames:
    createPNG(i)