from PIL import Image, ImageDraw, ImageFont
import textwrap
import random



def create_img():
    # Open image
    #img = Image.open("white#100.png")
    img = Image.open("template.png")
    font = ImageFont.truetype(font='vcr.ttf', size=72)
    # Create DrawText object
    draw = ImageDraw.Draw(im=img)
    

    label = "hst.txt"
    labelsplit = open(label).read().splitlines()
    randomlabel = random.choice(labelsplit)

    # Define our text
    # Define the text to be used on our image
    text = randomlabel
    # Create a new version of our text with maximum of 35 chars per line
    text = textwrap.fill(text=text, width=19)
    "\n".join(f"{str(len(x))} - {x}" for x in text.splitlines())
    # Add text to the image
    draw.text(xy=(700, 440), text=text, font=font, fill='#000000', anchor='ms', align='center')
    # View the updated image
    vertical_img = img.transpose(method=Image.FLIP_TOP_BOTTOM)
    vertical_img.save('images/' + text  + '#1' + '.png')
# 


with open("hst.txt") as f: # 1) open file
 for line in f: # 2) loop over all lines in file
  create_img() # 3) create image for each line
