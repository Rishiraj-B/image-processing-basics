from PIL import Image
content = Image.open('lena_color_512.tif')
pixels = list(content.getdata())
original_size = (((len(pixels)*24)/8)/1024)
# Binary
print("Converting RGB to Binary......")
image_out = Image.new('1',content.size)
pixels_out = []
for p in pixels:
	if p[0]>128 or p[1]>128 or p[2]>128:
		pixels_out.append(1)
	else:
		pixels_out.append(0)
image_out.putdata(pixels_out)
image_out.save('binary.tif')
binary_size = (len(pixels_out)/8)/1024
print("Original image size in KB : {:.2f}\nBinary image size in KB : {:.2f}".format(original_size, binary_size))
# Grayscale
print("\n\nConverting RGB to Grayscale......")
image_out = Image.new('L',content.size)
pixels_out = []
for p in pixels:
	val = sum(p)//len(p)
	pixels_out.append(val)
image_out.putdata(pixels_out)
image_out.save('grayscale.tif')
grayscale_size = ((len(pixels_out)*8)/8)/1024
print("Original image size in KB : {:.2f}\nGrayscale image size in KB : {:.2f}".format(original_size, grayscale_size))