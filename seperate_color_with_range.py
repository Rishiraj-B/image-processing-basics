from PIL import Image

content = Image.open('rainbow.tif')
pixels = list(content.getdata())
# Red only
red_color = list()
for i in range(len(pixels)):
	if pixels[i][0] >= 192 and pixels[i][1] < 128 and pixels[i][2] < 128:
		red_color.append(tuple(pixels[i][:3]))
	else:
		red_color.append((255, 255, 255))
new_img = Image.new(content.mode,content.size)
new_img.putdata(red_color)
new_img.save('red_only.tif')

# Green only
green_color = list()
for i in range(len(pixels)):
	if pixels[i][0] < 128 and pixels[i][1] >= 192 and pixels[i][2] < 128:
		green_color.append(tuple(pixels[i][:3]))
	else:
		green_color.append((255, 255, 255))
new_img = Image.new(content.mode,content.size)
new_img.putdata(green_color)
new_img.save('green_only.tif')

# Blue only
blue_color = list()
for i in range(len(pixels)):
	if pixels[i][0] < 128 and pixels[i][1] < 128 and pixels[i][2] >= 192:
		blue_color.append(tuple(pixels[i][:3]))
	else:
		blue_color.append((255, 255, 255))
new_img = Image.new(content.mode,content.size)
new_img.putdata(blue_color)
new_img.save('blue_only.tif')

# Missing red
red_color = list()
for i in range(len(pixels)):
	if pixels[i][0] >= 192 and pixels[i][1] < 128 and pixels[i][2] < 128:
		red_color.append((255, 255, 255))
	else:
		red_color.append(tuple(pixels[i][:3]))
new_img = Image.new(content.mode,content.size)
new_img.putdata(red_color)
new_img.save('no_red.tif')

# Missing green
green_color = list()
for i in range(len(pixels)):
	if pixels[i][0] < 128 and pixels[i][1] >= 192 and pixels[i][2] < 128:
		green_color.append((255, 255, 255))
	else:
		green_color.append(tuple(pixels[i][:3]))
new_img = Image.new(content.mode,content.size)
new_img.putdata(green_color)
new_img.save('no_green.tif')

# Missing blue
blue_color = list()
for i in range(len(pixels)):
	if pixels[i][0] < 128 and pixels[i][1] < 128 and pixels[i][2] >= 192:
		blue_color.append((255, 255, 255))
	else:
		blue_color.append(tuple(pixels[i][:3]))
new_img = Image.new(content.mode,content.size)
new_img.putdata(blue_color)
new_img.save('no_blue.tif')