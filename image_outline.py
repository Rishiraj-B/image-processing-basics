from PIL import Image

#reading the image
content = Image.open("animal.tif")
#reasingthe pixel values of the image in a list
pixels = content.getdata()
pixels_out = []
width, height = pixels.size

#converting our image to binary
for p in pixels:
	if p[0]>128 or p[1]>128 or p[2]>128:
		pixels_out.append(1)
	else:
		pixels_out.append(0)

#converting the pixel list into height*width array		
pixel_array = []
start = 0
count = width
pixels_final = []
for i in range(height):
	pixel_array.append(pixels_out[start:count])
	start = count
	count += width

#performing erosion operation on each pixel, and removing the pixel if all 9 values are true
for i in range(height):
	for j in range(width):
		if (i>0 and j>0) and (i<height and j<width):
			if pixel_array[i][j] == 1:
				pixels_final.append(pixel_array[i][j])
			else:
				if pixel_array[i-1][j-1] == 0:
					if pixel_array[i-1][j] == 0:
						if pixel_array[i+1][j+1] == 0:
							if pixel_array[i][j-1] == 0:
								if pixel_array[i][j+1] == 0:
									if pixel_array[i+1][j-1] == 0:
										if pixel_array[i+1][j] == 0:
											if pixel_array[i+1][j+1] == 0:
												pixels_final.append(1)
											else:
												pixels_final.append(pixel_array[i][j])
										else:
											pixels_final.append(pixel_array[i][j])
									else:
										pixels_final.append(pixel_array[i][j])
								else:
									pixels_final.append(pixel_array[i][j])
							else:
								pixels_final.append(pixel_array[i][j])
						else:
							pixels_final.append(pixel_array[i][j])
					else:
						pixels_final.append(pixel_array[i][j])
				else:
					pixels_final.append(pixel_array[i][j])
		else:
			pixels_final.append(1)
print(len(pixels_final))

#printing the final output image
image_out = Image.new('1',content.size)
image_out.putdata(pixels_final)
image_out.save('binary.tif')


# clipping_window = [[i-1, j-1], [i-1, j], [i+1, j+1], [i, j-1], [i, j+1], [i+1, j+1], [i+1, j], [i+1, j+1]]