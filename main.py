from PIL import Image, ImageDraw, ImageFont


font = ImageFont.truetype("./fonts/Helvetica.ttf", size=20)
# def id_front(id):
id = 1

#Opening all images
front_template=Image.open("./images/idfont.png").resize((396,612), Image.Resampling.LANCZOS)
potrait = Image.open(f'./images/{id}.jpg').resize((300,300), Image.Resampling.LANCZOS)
qr = Image.open(f'./qrcode/{id}.jpg').resize((80,80), Image.Resampling.LANCZOS)

#Ellipse Making
mask_im = Image.new("L", (290,300), 0)
draw = ImageDraw.Draw(mask_im)
draw.ellipse((110, 100, 290, 280), fill=255)
front_template.paste(potrait, (0, 0), mask_im)

# cropqr = qr.crop(55)
#resized_qr = qr.resize(15,15)
# front_template.paste(potrait, (10,10,10,10))
front_template.paste(qr, (270,490))
# draw = ImageDraw.Draw(front_template)
# # .resize((123,123), Image.Resampling.LANCZOS
# draw.text((60,60), str(id), font=font, fill='black')
# front_template.save(f'./idcards/{id}-front-side.jpg')
#
front_template.show()