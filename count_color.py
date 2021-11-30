from PIL import Image

#reading the image
content = Image.open('color.tif')
pixels = list(content.getdata())

#function to return count of pixels for given color code
def color_count(color_code, px_val):
  count = 0
  for l in range(len(px_val)):
    if tuple(px_val[l][:3]) == color_code:
      count+=1
  return count

# calculating the color count of each color 
red_count = color_count((255, 0, 0), pixels)
green_count = color_count((0, 255, 0), pixels)
blue_count = color_count((0, 0, 255), pixels)
yellow_count = color_count((255, 255, 0), pixels)
pink_count = color_count((255, 20, 147), pixels)
cyan_count = color_count((0, 255, 255), pixels)
magenta_count = color_count((255, 0, 255), pixels)

#printing the output
print("Red     :", red_count)
print("Green   :", green_count)
print("Blue    :", blue_count)
print("Yellow  :", yellow_count)
print("Pink    :", pink_count)
print("Cyan    :", cyan_count)
print("Magenta :", magenta_count)