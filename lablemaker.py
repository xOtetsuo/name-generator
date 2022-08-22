from PIL import Image, ImageDraw, ImageFont
import random 
""" 
labels = "update.txt"
stilo = "comp.txt"
labelsplit = open(labels).read().splitlines()
randomlabel = random.choice(labelsplit)
stilosplit = open(stilo).read().splitlines()
randomstilo = random.choice(stilosplit)
combinedlabel = randomlabel + ' ' + randomstilo

 """

label = "hst.txt"
labelsplit = open(label).read().splitlines()
randomlabel = random.choice(labelsplit)
im = Image.open("80.png")
box = ((590, 275, 80, 185))
draw = ImageDraw.Draw(im)
draw.rectangle(box, outline="#000")
text = randomlabel
font_size = 10
size = None
while (size is None or size[0] > box[2] - box[0] or size[1] > box[3] - box[1]) and font_size > 0:
	font = ImageFont.truetype("vcr.ttf", font_size)
	size = font.getsize_multiline(text)
	font_size -= 1
draw.multiline_text((box[0], box[1]), text, "#000000", font)
im.save("out.png")



""" font_size = 100
size = None
draw = ImageDraw.Draw(img)
draw.rectangle(box, outline="#000")
text = randomlabel + "\n" + randomstilo
while (size is None or size[0] > box[2] - box[0] or size[1] > box[3] - box[1]) and font_size > 0:
	font = ImageFont.truetype("vcr.ttf",  font_size)
	size = font.getsize_multiline(text)
	font_size -= 1
draw.multiline_text((box[0], box[1]), text, "#000", font)
 """

#draw.text((85, 187),randomlabel,(0,0,0),font=fontsize, align="right")
#draw.text((210, 210),randomstilo, (0,0,0),font=fontsize, align="center")
#img.save("labels/" + randomlabel + " " + randomstilo + ".png")
#img.save("image.png")