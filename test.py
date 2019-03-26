from PIL import Image, ImageStat, ImageDraw

output_image = Image.new('RGB', (255*2, int(255/2)*2), color = 'white')
d = ImageDraw.Draw(output_image)

for i in range(255):
    d.line((i,255,i,0), fill=(255,i,0))
output_image.show()