from PIL import Image

#reading the image and putiing the pixel values in a list
content = Image.open('color.tif')
pixels = list(content.getdata())

#function to check if the pixel is of given color and put in the output image if true
def extract_color(color_code, px_val):
	image_tup = list()
	for l in range(len(px_val)):
		if tuple(px_val[l][:3]) == color_code:
			image_tup.append(tuple(px_val[l][:3]))
		else:
			image_tup.append((255, 255, 255))
	return image_tup

#function to check if the pixel is of given color and remove it from the output image if true
def remove_color(color_code, px_val):
	image_tup = list()
	for l in range(len(px_val)):
		if tuple(px_val[l][:3]) == color_code:
			image_tup.append((255, 255, 255))
		else:
			image_tup.append(tuple(px_val[l][:3]))
	return image_tup

#Performing the Color Extraction for each color	
# Red only
red_only = extract_color((255, 0, 0), pixels)
new_img = Image.new(content.mode,content.size)
new_img.putdata(red_only)
new_img.save('red_only.tif')

# Green only
green_only = extract_color((0, 255, 0), pixels)
new_img = Image.new(content.mode,content.size)
new_img.putdata(green_only)
new_img.save('green_only.tif')

# Blue only
blue_only = extract_color((0, 0, 255), pixels)
new_img = Image.new(content.mode,content.size)
new_img.putdata(blue_only)
new_img.save('blue_only.tif')

#Performing the Color Removal of the given color
# Missing red
no_red = remove_color((255, 0, 0), pixels)
new_img = Image.new(content.mode,content.size)
new_img.putdata(no_red)
new_img.save('no_red.tif')

# Missing green
no_green = remove_color((0, 255, 0), pixels)
new_img = Image.new(content.mode,content.size)
new_img.putdata(no_green)
new_img.save('no_green.tif')

# Missing blue
no_blue = remove_color((0, 0, 255), pixels)
new_img = Image.new(content.mode,content.size)
new_img.putdata(no_blue)
new_img.save('no_blue.tif')