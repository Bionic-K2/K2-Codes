from PIL import ImageSequence
from PIL import Image

gifname = "爆气"
png_x = 0
png_y = 0
trans_x_min = 10000
trans_x_max = 0
trans_y_min = 10000
trans_y_max = 0
gif = Image.open("爆气"+'.gif')
for i, frame in enumerate(ImageSequence.Iterator(gif), 0):
    png_x += frame.size[0]
    png_y = frame.size[1]

png = Image.new("RGBA", (png_x, png_y), "#00FF00")
for i, frame in enumerate(ImageSequence.Iterator(gif), 0):
    frame = frame.convert('RGBA')
    # 第一轮：获取透明区域并染色
    trans_x_min = 10000
    trans_x_max = 0
    trans_y_min = 10000
    trans_y_max = 0
    for yh in range(frame.size[1]):
        for xw in range(frame.size[0]):
            dot = (xw, yh)
            color_d = frame.getpixel(dot)
            if color_d[3] == 0:
                color_d = (0, 255, 0, 255)
                frame.putpixel(dot, color_d)
                if xw >= trans_x_max:
                    trans_x_max = xw
                if xw <= trans_x_min:
                    trans_x_min = xw
                if yh >= trans_y_max:
                    trans_y_max = yh
                if yh <= trans_y_min:
                    trans_y_min = yh

    # 第二轮：清除所有透明域意外的区域
    for yh in range(frame.size[1]):
        for xw in range(frame.size[0]):
            dot = (xw, yh)
            if xw < trans_x_min or xw > trans_x_max or yh < trans_y_min or yh > trans_y_max:
                color_d = (0, 255, 0, 255)
                frame.putpixel(dot, color_d)

    
    png.paste(frame, ((i*frame.size[0]), 0), None)
# 第三轮：清除所有标记区域转变为透明
for yh in range(png.size[1]):
    for xw in range(png.size[0]):
        dot = (xw, yh)
        color_d = png.getpixel(dot)
        if color_d == (0, 255, 0, 255):
            color_d = (0, 0, 0, 0)
            png.putpixel(dot, color_d)
            
png.save(gifname+'.png', 'png')
