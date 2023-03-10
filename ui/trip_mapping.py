import sys
from PIL import Image, ImageDraw

im = Image.new('RGB', (500, 500))

draw = ImageDraw.Draw(im)
draw.line((0, 0) + im.size, fill=128)
draw.line((0, im.size[1], im.size[0], 0), fill=128)

# write to stdout
im.save("./out.png", "PNG")